#!/usr/bin/env python3
"""Hedef 5 ölçüm seti: Tatoeba'dan Türk dilleri arasında paralel cümleler.

Tatoeba dışa aktarımları (https://downloads.tatoeba.org/exports/per_language/) bir
klasöre indirilir; bu araç onlardan dil çifti başına bir test seti seçer ve
ceviri/olcu/tatoeba/ altına yazar. Ağ gerektirmez; CI'da çalışmaz.

  python3 araclar/ceviri_veri.py <indirme_klasoru>

Seçim kuralları (sürüm 1):
  * Önce iki dil arasında doğrudan bağlı cümle çiftleri (Tatoeba "links").
  * Doğrudan çift EN_AZ'dan azsa, İngilizce üzerinden bağlananlarla tamamlanır
    (yol: eng). Bunlar daha gevşektir; raporda ayrı sayılır.
  * Kısa (2 kelimeden az) ve aşırı uzun (40 kelimeden çok) cümleler, aynı
    cümlenin tekrarları ve uzunluk oranı 3'ten büyük çiftler atılır.
  * Çift başına en çok EN_COK cümle; seçim cümle kimliğinin karmasına göre
    yapılır, yani her çalıştırmada aynı sonucu verir.
"""
from __future__ import annotations

import bz2
import collections
import hashlib
import itertools
import os
import sys
from pathlib import Path

KOK = Path(__file__).resolve().parent.parent
HEDEF = KOK / "ceviri" / "olcu" / "tatoeba"
# Tatoeba kodu -> bizim kodumuz (agac.yaml)
DILLER = {"tur": "tur", "aze": "aze", "kaz": "kaz", "uzb": "uzb", "tat": "tat", "uig": "uig",
          "bak": "bak", "kir": "kir", "tuk": "tuk", "crh": "crh", "chv": "chv", "sah": "sah",
          "gag": "gag", "kum": "kum", "krc": "krc", "kaa": "kaa", "nog": "nog", "alt": "alt",
          "tyv": "tyv", "kjh": "kjh", "klj": "klj", "ota": "ota"}
ILK = ["tur", "aze", "kaz", "uzb", "tat", "uig"]
EN_AZ, EN_COK, OBUR_ESIK = 100, 200, 50


def cumleler(d, a):
    f = d / f"{a}_sentences.tsv.bz2"
    out = {}
    if f.exists():
        for satir in bz2.open(f, "rt", encoding="utf-8"):
            p = satir.rstrip("\n").split("\t")
            if len(p) >= 3:
                out[int(p[0])] = p[2].strip()
    return out


def baglar(d, a, b):
    out = set()
    for x, y, f in ((a, b, d / f"{a}-{b}_links.tsv.bz2"), (b, a, d / f"{b}-{a}_links.tsv.bz2")):
        if f.exists():
            for satir in bz2.open(f, "rt"):
                p = satir.split("\t")
                if len(p) >= 2:
                    i, j = int(p[0]), int(p[1])
                    out.add((i, j) if x == a else (j, i))
    return out


def uygun(s, t):
    ka, kb = len(s.split()), len(t.split())
    if min(ka, kb) < 2 or max(ka, kb) > 40:
        return False
    return max(len(s), len(t)) / max(1, min(len(s), len(t))) <= 3


def karma(*x) -> str:
    return hashlib.sha1("|".join(map(str, x)).encode()).hexdigest()


def main():
    d = Path(sys.argv[1])
    C = {a: cumleler(d, a) for a in DILLER}
    eng = {a: collections.defaultdict(set) for a in DILLER}
    for a in DILLER:
        for x, e in baglar(d, a, "eng"):
            eng[a][e].add(x)
    HEDEF.mkdir(parents=True, exist_ok=True)
    ozet = []
    for a, b in itertools.combinations(DILLER, 2):
        dogrudan = [(x, y, "dogrudan") for x, y in baglar(d, a, b) if x in C[a] and y in C[b]]
        ilk_cift = a in ILK and b in ILK
        if not ilk_cift and len(dogrudan) < OBUR_ESIK:
            continue
        adaylar = dogrudan
        if ilk_cift and len(dogrudan) < EN_AZ:
            ara = [(x, y, "eng") for e in eng[a] if e in eng[b] for x in eng[a][e] for y in eng[b][e]
                   if x in C[a] and y in C[b]]
            adaylar = dogrudan + ara
        gorulen, secilen = set(), []
        for x, y, yol in sorted(adaylar, key=lambda t: (t[2] != "dogrudan", karma(*t[:2]))):
            s, t = C[a][x], C[b][y]
            if x in gorulen or s in gorulen or not uygun(s, t):
                continue
            gorulen |= {x, s}
            secilen.append((x, s, y, t, yol))
            if len(secilen) >= EN_COK:
                break
        if not secilen:
            continue
        ka, kb = DILLER[a], DILLER[b]
        with open(HEDEF / f"{ka}-{kb}.tsv", "w", encoding="utf-8") as f:
            f.write(f"{ka}_id\t{ka}\t{kb}_id\t{kb}\tyol\n")
            for x, s, y, t, yol in secilen:
                f.write(f"{x}\t{s}\t{y}\t{t}\t{yol}\n")
        n_d = sum(1 for r in secilen if r[4] == "dogrudan")
        ozet.append((ka, kb, len(secilen), n_d))
    with open(HEDEF / "OZET.tsv", "w", encoding="utf-8") as f:
        f.write("dil1\tdil2\tcumle\tdogrudan\n")
        for r in ozet:
            f.write("\t".join(map(str, r)) + "\n")
    print(f"{len(ozet)} dil çifti yazıldı: {HEDEF}")


if __name__ == "__main__":
    main()
