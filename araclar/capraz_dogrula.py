#!/usr/bin/env python3
"""Sözlük tanıklarını bağımsız kaynaklarla çapraz doğrular (ILKELER §12).

Her yaşayan dil tanığı (ağızlar hariç) şu kaynaklarda aranır:
  apertium               Apertium biçimbilim sözlüğünde bu biçim var mı?          → yalnız biçim
  tatoeba                Tatoeba cümlelerinde bu biçim kelime olarak geçiyor mu?  → yalnız biçim
  universal-dependencies UD derlemlerinde bu biçim baş biçim (lemma) olarak var mı? → yalnız biçim
  asjp                   ASJP'de bu kavramın bu dildeki kaydı bu biçime benziyor mu? → anlam ve kök
                         (kaba iskelet benzerliği ≥ 0,6: aynı kelimenin kaydı olduğunu gösterir,
                         ünlü ve yazım farklarını göstermez; ASJP biçimi atıfta yazılıdır)

Bulunan kanıt tanığın `kaynak` ve `atif` alanlarına eklenir; ardından `denetim`
yeniden hesaplanır (araclar/sozluk.py --denetim-doldur --yeniden). ASJP'de aynı
kavram için belirgin biçimde farklı bir kelime görülen tanıklar inceleme listesine
yazılır (sozluk/CAPRAZ.md); bu bir çelişki olabilir ya da yalnız eş anlamlı bir
kelime. Durumu kendiliğinden değiştirmez.

  python3 araclar/capraz_dogrula.py --apertium D --tatoeba D --ud D --asjp D [--yaz]

Ağ gerektirmez; kaynaklar önceden indirilir (adresler kaynaklar/kaynaklar.yaml'da).
"""
from __future__ import annotations

import argparse
import bz2
import collections
import csv
import glob
import os
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from yazim import calisma  # noqa: E402

KOK = Path(__file__).resolve().parent.parent
KOK_DIZIN = KOK / "sozluk" / "kok"
RAPOR = KOK / "sozluk" / "CAPRAZ.md"
UD_KOD = {"tr": "tur", "kk": "kaz", "ug": "uig", "ky": "kir", "tt": "tat", "uz": "uzb", "az": "aze", "sah": "sah"}
ASJP_ISO = {"azj": "aze", "uzn": "uzb"}             # öbürleri aynı kodla
ASJP_KAVRAM = {"I": "ben", "you": "sen", "we": "biz", "this": "bu", "who": "kim", "what": "ne", "many": "cok",
               "one": "bir", "two": "iki", "big": "buyuk", "long": "uzun", "small": "kucuk", "woman": "kadin",
               "man": "er", "person": "kisi", "fish": "balik", "bird": "kus", "dog": "it", "louse": "bit",
               "tree": "agac", "seed": "tohum", "leaf": "yaprak", "root": "kok-bitki", "bark": "kabuk",
               "skin": "deri", "blood": "kan", "bone": "kemik", "egg": "yumurta", "horn": "boynuz",
               "tail": "kuyruk", "feather": "tuy", "hair": "sac", "head": "bas", "ear": "kulak", "eye": "goz",
               "nose": "burun", "mouth": "agiz", "tooth": "dis", "tongue": "dil", "knee": "diz", "hand": "el",
               "belly": "karin", "neck": "boyun", "heart": "yurek", "liver": "ciger", "drink": "ic", "eat": "ye",
               "bite": "isir", "see": "gor", "hear": "isit", "know": "bil", "sleep": "uyu", "die": "ol",
               "kill": "oldur", "swim": "yuz-fiil", "fly": "uc-fiil", "walk": "yuru", "come": "gel", "lie": "yat",
               "sit": "otur", "stand": "tur", "give": "ver", "say": "de", "sun": "gunes", "moon": "ay",
               "star": "yildiz", "water": "su", "rain": "yagmur", "stone": "tas", "sand": "kum", "earth": "yer",
               "cloud": "bulut", "smoke": "duman", "fire": "ates", "ash": "kul", "burn": "yan", "mountain": "dag",
               "red": "kizil", "green": "yesil", "yellow": "sari", "white": "ak", "black": "kara", "night": "gece",
               "hot": "sicak", "cold": "soguk", "full": "dolu", "new": "yeni", "good": "iyi", "dry": "kuru",
               "name": "ad", "flesh": "et-ad", "foot": "ayak"}
# ASJP yazımı → çalışma yazımı (yaklaşık)
ASJP_HARF = {"E": "e", "3": "ı", "S": "ş", "Z": "j", "C": "ç", "j": "c", "N": "ñ", "X": "x", "y": "y", "8": "s",
             "4": "ñ", "5": "ñ", "L": "l", "T": "t", "7": "", "!": "", "G": "ğ", "~": "", "*": "", "\"": "", "$": "",
             "w": "w", "q": "k"}


def kaba(s: str) -> str:
    """Karşılaştırma için kaba iskelet: uyum ve ince ses farkları silinir."""
    s = s.lower()
    for a, b in (("ö", "o"), ("ü", "u"), ("ı", "i"), ("ä", "e"), ("ă", "a"), ("ĕ", "e"), ("ğ", "g"), ("q", "k"),
                 ("x", "k"), ("h", "k"), ("ş", "s"), ("z", "s"), ("ç", "c"), ("j", "c"), ("ñ", "n"), ("w", "v"),
                 ("d", "t"), ("b", "p"), ("g", "k")):
        s = s.replace(a, b)
    return re.sub(r"[^a-z]", "", s)


MASTAR = ("mek", "mak", "maq", "mäk", "moq", "mok", "mog", "arga", "erge", "ırga", "irge", "arğa", "ärgä", "arğo",
          "rga", "rge", "rğo", "uu", "üü", "ou", "ıu", "iu", "iw", "ıw", "ei", "ey", "er", "ır", "u", "ü")
SESLI = set("aeıioöuüäăĕy")


def iskelet(s: str) -> str:
    """Ünsüz iskeleti (kaba sınıflarla)."""
    return "".join(ch for ch in kaba(s) if ch not in SESLI)


def asjp_turleri(f: str):
    """ASJP kaydının denenecek biçimleri: her kelime ve mastar eki atılmış hâli."""
    for k in [f] + f.split():
        yield k
        for m in MASTAR:
            if k.endswith(m) and len(k) - len(m) >= 2:
                yield k[: -len(m)]


def benzer_asjp(b: str, f: str) -> float:
    """Kaba benzerlik; ünsüz iskeleti aynıysa aynı kök sayılır (ASJP ünlüyü değil kökü doğrular)."""
    en = 0.0
    for x in asjp_turleri(f):
        if iskelet(b) and iskelet(b) == iskelet(x):
            return 1.0
        en = max(en, benzer(b, x))
    return en


def olasi_neden(b: str, kayitlar) -> str:
    for _, f in kayitlar:
        if any(f.endswith(m) for m in MASTAR) or " " in f:
            return "mastar ya da birleşik kayıt olabilir"
    return "başka kelime (eş anlamlı ya da hata): elle bakılmalı"


def benzer(a: str, b: str) -> float:
    a, b = kaba(a), kaba(b)
    if not a or not b:
        return 0.0
    p = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        c = [i]
        for j, y in enumerate(b, 1):
            c.append(min(p[j] + 1, c[j - 1] + 1, p[j - 1] + (x != y)))
        p = c
    return 1 - p[-1] / max(len(a), len(b))


def apertium_yukle(d):
    out = {}
    for f in glob.glob(os.path.join(d, "*.lexc")):
        l = Path(f).stem
        s = open(f, encoding="utf-8", errors="ignore").read()
        g = set()
        for m in re.finditer(r"(?m)^\s*([^\s!:%<>;]+)(?:%<\w+%>)*(?::([^\s!:%<>;]+))?\s+[\w-]+\s*;", s):
            g.add(calisma(l, (m.group(2) or m.group(1)).lower()))
        out[l] = g
    return out


def tatoeba_yukle(d):
    out = {}
    for f in glob.glob(os.path.join(d, "*_sentences.tsv.bz2")):
        l = Path(f).name.split("_")[0]
        c = collections.Counter()
        for satir in bz2.open(f, "rt", encoding="utf-8"):
            p = satir.rstrip("\n").split("\t")
            if len(p) >= 3:
                c.update(calisma(l, p[2]).split())
        out[l] = c
    return out


def ud_yukle(d):
    out = collections.defaultdict(set)
    for f in glob.glob(os.path.join(d, "*.conllu")):
        l = UD_KOD.get(Path(f).name.split("_")[0])
        if not l:
            continue
        for satir in open(f, encoding="utf-8"):
            p = satir.split("\t")
            if len(p) == 10 and p[0].isdigit():
                out[l].add(calisma(l, p[2].lower()))
    return out


def asjp_yukle(d):
    L = {r["ID"]: ASJP_ISO.get(r["ISO639P3code"], r["ISO639P3code"])
         for r in csv.DictReader(open(os.path.join(d, "languages.csv"), encoding="utf-8")) if r["Family"] == "Turkic"}
    P = {r["ID"]: r["Name"].lstrip("*") for r in csv.DictReader(open(os.path.join(d, "parameters.csv"), encoding="utf-8"))}
    out = collections.defaultdict(list)   # (dil, kavram dosyası) -> [(doculect, biçim)]
    for r in csv.DictReader(open(os.path.join(d, "forms.csv"), encoding="utf-8")):
        if r["Language_ID"] in L and P.get(r["Parameter_ID"]) in ASJP_KAVRAM:
            b = "".join(ASJP_HARF.get(ch, ch) for ch in r["Value"])
            out[(L[r["Language_ID"]], ASJP_KAVRAM[P[r["Parameter_ID"]]])].append((r["Language_ID"], b))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    for k in ("apertium", "tatoeba", "ud", "asjp"):
        ap.add_argument(f"--{k}", required=True)
    ap.add_argument("--yaz", action="store_true", help="tanıklara yaz ve raporu üret")
    a = ap.parse_args()
    AP, TA, UD, AS = apertium_yukle(a.apertium), tatoeba_yukle(a.tatoeba), ud_yukle(a.ud), asjp_yukle(a.asjp)
    say = collections.Counter(); inceleme = []
    # (kavram dosyası, kök, dil): tanık bu kavramda bu dil için gerçekten kullanılıyor mu?
    KD = set()
    for kp in (KOK / "sozluk" / "temel").glob("*.yaml"):
        kv = yaml.safe_load(kp.read_text(encoding="utf-8"))
        for k in kv.get("kokler") or []:
            for dl in (k.get("bicimler") or {}):
                KD.add((kp.stem, k["kok"], dl))
    for yol in sorted(KOK_DIZIN.glob("*.yaml")):
        if yol.stem.startswith("ek-"):
            continue
        v = yaml.safe_load(yol.read_text(encoding="utf-8"))
        kavramlar = v.get("kavramlar") or []
        satirlar = yol.read_text(encoding="utf-8").split("\n"); degisti = False
        for i, s in enumerate(satirlar):
            if not (s.startswith("  - {") and s.rstrip().endswith("}")):
                continue
            t = yaml.safe_load(s[4:])
            dil = str(t.get("dil", ""))
            if "-" in dil or not t.get("bicim") or "çözülmedi" in str(t.get("not", "")):
                continue      # ağızlar ve açık çelişkiler elle incelenir
            b = calisma(dil, str(t["bicim"]).split(",")[0].split("/")[0].strip()).rstrip("-")
            if not b:
                continue
            kay = [k for k in str(t.get("kaynak", "")).split(";") if k.strip()]
            kay = [k.strip() for k in kay]
            yeni, atif = [], []
            if dil in AP and b in AP[dil] and "apertium" not in kay:
                yeni.append("apertium"); atif.append(f"Apertium {dil} sözlüğünde var")
            if dil in TA and TA[dil].get(b) and "tatoeba" not in kay:
                yeni.append("tatoeba"); atif.append(f"Tatoeba'da {TA[dil][b]} kez")
            if dil in UD and b in UD[dil] and "universal-dependencies" not in kay:
                yeni.append("universal-dependencies"); atif.append("UD derleminde baş biçim")
            asjp = [x for kv in kavramlar if (kv, v["kok"], dil) in KD for x in AS.get((dil, kv), [])]
            if asjp:
                eslesen = [x for x in asjp if benzer_asjp(b, x[1]) >= 0.6]
                if eslesen and "asjp" not in kay:
                    yeni.append("asjp"); atif.append(f"ASJP {eslesen[0][0]}: {eslesen[0][1]}")
                elif not eslesen:
                    inceleme.append((yol.stem, dil, t["bicim"], ", ".join(f"{x[0]}: {x[1]}" for x in asjp[:3]),
                                     olasi_neden(b, asjp)))
            for k in yeni:
                say[k] += 1
            if yeni:
                say["tanik"] += 1
                if a.yaz:
                    t["kaynak"] = "; ".join([k for k in kay if k != "bilgi"] + yeni)
                    t["atif"] = "; ".join(x for x in [str(t.get("atif") or "").strip()] + atif if x)
                    t.pop("denetim", None)
                    satirlar[i] = "  - " + yaml.safe_dump(t, allow_unicode=True, default_flow_style=True, width=10000,
                                                          sort_keys=False).strip().removesuffix("\n...")
                    degisti = True
        if degisti:
            metin = "\n".join(satirlar); yaml.safe_load(metin); yol.write_text(metin, encoding="utf-8")
    print("yeni kanıt:", dict(say))
    print("ASJP ile uyuşmayan:", len(inceleme))
    if a.yaz:
        y = ["# Çapraz doğrulama: inceleme listesi\n",
             "> Bu dosya `python3 araclar/capraz_dogrula.py ... --yaz` ile üretilir; elle düzenlemeyin.\n",
             "ASJP'de aynı kavram için bu dilde kayıtlı kelime, tanığın biçimine benzemiyor (kaba iskelet "
             "benzerliği 0,6'nın altında). Bu bir çelişki olabilir (yanlış biçim, yanlış kök) ya da yalnız "
             "eş anlamlı başka bir kelime. Her satır elle incelenmelidir; araç tanığın durumunu değiştirmez.\n",
             f"Toplam {len(inceleme)} tanık.\n", "| Kök | Dil | Bizim biçim | ASJP kaydı | Olası neden |", "|---|---|---|---|---|"]
        y += [f"| [{k}](kok/{k}.md) | {d} | {b} | {x} | {n} |" for k, d, b, x, n in sorted(inceleme, key=lambda r: (r[4], r[1], r[0]))]
        RAPOR.write_text("\n".join(y) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
