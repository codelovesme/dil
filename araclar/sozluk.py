#!/usr/bin/env python3
"""Ortak Türk dili — Hedef 4: tanıklı sözlük.

Kullanım:
    python3 araclar/sozluk.py                 # bütün köklerin kapsam özeti
    python3 araclar/sozluk.py ben             # tek kök: kapsam ve eksikler
    python3 araclar/sozluk.py --denetle       # kök dosyaları ile kavram dosyalarını karşılaştır
    python3 araclar/sozluk.py --yaz           # sozluk/kok/<kök>.md ve sozluk/SOZLUK.md üret

Veri: sozluk/kok/<kök>.yaml (sözlük maddesi). Her madde kökün bütün tanıklarını tutar:
hangi dilde, ağızda ya da boyda; nerede; kaçıncı yüzyılda; hangi biçim ve anlamla;
hangi metinde; kim kaydetmiş; hangi kaynaktan okunmuş. Kurallar ILKELER.md §14'te.
Kavram dosyaları (sozluk/temel/…) seçim içindir; kök dosyaları belgeleme içindir.
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import puanla  # noqa: E402
from puanla import yaml  # noqa: E402

KOK = puanla.KOK_DIZIN
KOK_DIZIN = KOK / "sozluk" / "kok"
KAYNAK_DOSYASI = KOK / "kaynaklar" / "kaynaklar.yaml"
DIZIN_DOSYASI = KOK / "sozluk" / "SOZLUK.md"

GUNUMUZ = 21          # yüzyılı yazılmamış yaşayan dil tanığı günümüze aittir
YASAYAN_ESIK = 20     # bu yüzyıldan itibaren tanık "yaşayan dil" kapsamına girer
MADDE_ALANLARI = {"kok", "anlam", "koken", "ana_turkce", "kavramlar", "etimoloji", "kaynak",
                  "not", "taniklar", "yok", "tarihi_yok"}
TANIK_ALANLARI = {"dil", "boy", "yer", "yuzyil", "bicim", "yazi", "anlam", "metin", "kaynak",
                  "atif", "kaydeden", "yabanci", "not"}


# ============================================================ yardımcılar

def yuzyil_coz(v) -> tuple[int, int] | None:
    """'8' → (8, 8); '13-15' → (13, 15)."""
    if v is None or v == "":
        return None
    m = re.fullmatch(r"\s*(\d+)\s*(?:[-–]\s*(\d+))?\s*", str(v))
    if not m:
        raise ValueError(f"yüzyıl anlaşılamadı: {v!r}")
    a = int(m.group(1))
    return a, int(m.group(2) or a)


def yuzyil_yaz(r: tuple[int, int]) -> str:
    if r[0] >= GUNUMUZ:
        return "günümüz"
    return f"{r[0]}. yy" if r[0] == r[1] else f"{r[0]}.–{r[1]}. yy"


def kaynak_listesi(v) -> list[str]:
    return [x.strip() for x in str(v or "").split(";") if x.strip()]


class Baglam:
    """Ağaç, tanık kodları, kaynaklar ve Hedef 4 ayarları."""

    def __init__(self):
        self.agac = puanla.agac_yukle()
        self.taniklar = puanla.taniklari_yukle(self.agac)
        self.dugum = {d.kod: d for d in self.agac.tum_dugumler() if not d.yazi_dili}
        self.tarihi = {t.kod: t for t in self.taniklar}
        self.ad = {k: d.ad for k, d in self.dugum.items()}
        for d in self.agac.diller:
            if d.alt:
                self.ad[d.kod] = d.ad
        self.ad.update({k: t.kisa for k, t in self.tarihi.items()})
        # her ağız/dil kodu → dil düğümü
        self.dil_of: dict[str, puanla.Dugum] = {}
        for L in self.agac.diller:
            for k in L.yaprak_kodlari | {L.kod}:
                self.dil_of[k] = L
        self.agizlar = sorted(k for L in self.agac.diller for k in L.yaprak_kodlari if k != L.kod)
        with open(KAYNAK_DOSYASI, encoding="utf-8") as f:
            self.kaynaklar = {k["kimlik"]: k for k in yaml.safe_load(f)["kaynaklar"]}
        with open(puanla.HEDEF_DOSYASI, encoding="utf-8") as f:
            self.hedef = next(h for h in yaml.safe_load(f) if h["yontem"] == "derleme")
        self.duraklar = self.hedef.get("duraklar", [])
        self.sira = {d.kod: i for i, d in enumerate(self.agac.tum_dugumler())}
        self.sira.update({k: -10 + t.sira for k, t in self.tarihi.items()})

    def gecerli(self, kod: str) -> bool:
        return kod in self.dugum or kod in self.tarihi

    def yasayan_mi(self, kod: str) -> bool:
        return kod in self.dil_of

    def kapsar(self, durak_kodu: str, kod: str) -> bool:
        """Durağın `dil` kodu bu tanık kodunu kapsıyor mu? (kod kendisi ya da altında)"""
        if durak_kodu == "yasayan":
            return self.yasayan_mi(kod)
        if durak_kodu == kod:
            return True
        d = self.dugum.get(kod)
        return d is not None and any(u.kod == durak_kodu for u in d.ustler())


# ================================================================ madde

class Tanik:
    def __init__(self, v: dict, b: Baglam, hatalar: list[str], yer: str):
        if fazla := set(v) - TANIK_ALANLARI:
            hatalar.append(f"{yer}: bilinmeyen alan {sorted(fazla)}")
        self.dil = str(v.get("dil", ""))
        self.bicim = str(v.get("bicim", ""))
        for alan in ("dil", "bicim", "kaynak"):
            if not v.get(alan):
                hatalar.append(f"{yer}: '{alan}' eksik")
        if self.dil and not b.gecerli(self.dil):
            hatalar.append(f"{yer}: bilinmeyen dil/ağız/tanık kodu '{self.dil}'")
        self.kaynaklar = kaynak_listesi(v.get("kaynak"))
        for k in self.kaynaklar:
            if k != "bilgi" and k not in b.kaynaklar:
                hatalar.append(f"{yer}: kaynaklar.yaml'da olmayan kaynak '{k}'")
        self.alan = {a: v.get(a) for a in TANIK_ALANLARI}
        self.yabanci = bool(v.get("yabanci", False))
        # yüzyıl: tanıktan, yoksa kaynaktan, yoksa yaşayan dilse günümüz
        try:
            r = yuzyil_coz(v.get("yuzyil"))
            if r is None:
                r = next((yuzyil_coz(b.kaynaklar[k]["yuzyil"]) for k in self.kaynaklar
                          if k in b.kaynaklar and b.kaynaklar[k].get("yuzyil")), None)
            if r is None and b.yasayan_mi(self.dil):
                r = (GUNUMUZ, GUNUMUZ)
        except ValueError as e:
            hatalar.append(f"{yer}: {e}")
            r = None
        if r is None:
            hatalar.append(f"{yer}: yüzyıl yok (tarihî tanıkta ya da kaynakta yazılmalı)")
            r = (0, 0)
        self.yuzyil = r

    @property
    def kaynakli(self) -> bool:
        return any(k != "bilgi" for k in self.kaynaklar)

    @property
    def gunumuz(self) -> bool:
        return self.yuzyil[0] >= YASAYAN_ESIK


class Madde:
    def __init__(self, yol: Path, b: Baglam):
        self.yol = yol
        with open(yol, encoding="utf-8") as f:
            v = yaml.safe_load(f) or {}
        self.hatalar: list[str] = []
        if fazla := set(v) - MADDE_ALANLARI:
            self.hatalar.append(f"{yol.name}: bilinmeyen alan {sorted(fazla)}")
        for alan in ("kok", "anlam", "koken", "taniklar"):
            if alan not in v:
                self.hatalar.append(f"{yol.name}: '{alan}' eksik")
        self.v = v
        self.kok = str(v.get("kok", yol.stem))
        self.taniklar = [Tanik(t, b, self.hatalar, f"{yol.name} tanık {i + 1} ({t.get('dil')})")
                         for i, t in enumerate(v.get("taniklar") or [])]
        self.yok: dict = v.get("yok") or {}
        self.tarihi_yok: dict = v.get("tarihi_yok") or {}
        for k in self.yok:
            if not b.gecerli(k):
                self.hatalar.append(f"{yol.name}: 'yok' içinde bilinmeyen kod '{k}'")
        durak_adlari = {d["ad"] for d in b.duraklar}
        for k in self.tarihi_yok:
            if k not in durak_adlari:
                self.hatalar.append(f"{yol.name}: 'tarihi_yok' içinde bilinmeyen durak '{k}'")
        for k in kaynak_listesi(v.get("kaynak")):
            if k not in b.kaynaklar:
                self.hatalar.append(f"{yol.name}: kaynaklar.yaml'da olmayan kaynak '{k}'")


def maddeleri_yukle(b: Baglam, secilenler: list[str]) -> list[Madde]:
    dosyalar = sorted(KOK_DIZIN.glob("*.yaml"))
    if secilenler:
        dosyalar = [d for d in dosyalar if d.stem in secilenler]
        if eksik := set(secilenler) - {d.stem for d in dosyalar}:
            sys.exit(f"Bulunamayan kök dosyaları: {sorted(eksik)}")
    maddeler = [Madde(d, b) for d in dosyalar]
    if hatalar := [h for m in maddeler for h in m.hatalar]:
        sys.exit("Hatalar:\n  " + "\n  ".join(hatalar))
    return maddeler


# =============================================================== kapsam

class Kapsam:
    """Hedef 4'ün ölçüsü: madde ne kadar eksiksiz?"""

    def __init__(self, m: Madde, b: Baglam):
        gunumuz = [t for t in m.taniklar if t.gunumuz and b.yasayan_mi(t.dil)]
        dolu_dil = {b.dil_of[t.dil].kod for t in gunumuz} | {b.dil_of[k].kod for k in m.yok if k in b.dil_of}
        self.diller = [L for L in b.agac.diller]
        self.eksik_diller = [L for L in self.diller if L.kod not in dolu_dil]
        dolu_agiz = {t.dil for t in gunumuz} | set(m.yok)
        self.agiz_dolu = sum(1 for a in b.agizlar if a in dolu_agiz)
        self.agiz_toplam = len(b.agizlar)
        self.duraklar = []   # (durak, dolu mu, tanık sayısı)
        for d in b.duraklar:
            a, z = yuzyil_coz(d["yuzyil"])
            n = sum(1 for t in m.taniklar
                    if t.kaynakli and any(b.kapsar(k, t.dil) for k in d["dil"])
                    and t.yuzyil[0] <= z and t.yuzyil[1] >= a)
            self.duraklar.append((d, n > 0 or d["ad"] in m.tarihi_yok, n))
        self.tanik = len(m.taniklar)
        self.kaynakli = sum(1 for t in m.taniklar if t.kaynakli)
        self.kaynaklar = Counter(k for t in m.taniklar for k in t.kaynaklar if k != "bilgi")
        self.yabanci = sum(1 for t in m.taniklar if t.yabanci)
        self.yuzyillar = sorted({y for t in m.taniklar for y in range(t.yuzyil[0], t.yuzyil[1] + 1)
                                 if y < GUNUMUZ})
        self.ilk = min((t.yuzyil[0] for t in m.taniklar), default=None)
        s1 = not self.eksik_diller
        s2 = s1 and all(dolu for d, dolu, _ in self.duraklar if d.get("zorunlu", True))
        s3 = s2 and self.yabanci >= int(b.hedef.get("yabanci_en_az", 1))
        self.seviye = 3 if s3 else 2 if s2 else 1 if s1 else 0

    @property
    def eksik_duraklar(self):
        return [d for d, dolu, _ in self.duraklar if not dolu]

    def ozet(self) -> str:
        zorunlu = [x for x in self.duraklar if x[0].get("zorunlu", True)]
        return (f"seviye {self.seviye} · diller {len(self.diller) - len(self.eksik_diller)}/{len(self.diller)}"
                f" · ağızlar {self.agiz_dolu}/{self.agiz_toplam}"
                f" · duraklar {sum(1 for _, d, _ in zorunlu if d)}/{len(zorunlu)}"
                f" · tanık {self.tanik} (kaynaklı %{100 * self.kaynakli / max(self.tanik, 1):.0f})"
                f" · kaynak {len(self.kaynaklar)} · yabancı kayıt {self.yabanci}")


# ============================================================ denetim

def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.strip().lower()).replace("ė", "e")


def denetle(maddeler: list[Madde], b: Baglam) -> int:
    """Kavram dosyalarındaki `bicimler`/`tarihi` ile kök dosyasının tanıklarını karşılaştır."""
    kavramlar = {kv.yol.stem: kv for kv in puanla.kavramlari_yukle([], b.agac, b.taniklar)}
    sorun = 0
    for m in maddeler:
        for ad in m.v.get("kavramlar") or []:
            kv = kavramlar.get(ad)
            if kv is None:
                print(f"{m.kok}: kavram dosyası yok: {ad}")
                sorun += 1
                continue
            try:
                k = kv.kok(m.kok)
            except StopIteration:
                print(f"{m.kok}: '{ad}' kavramında bu kök yok")
                sorun += 1
                continue
            gunumuz: dict[str, set[str]] = {}
            tarihi: dict[str, set[str]] = {}
            for t in m.taniklar:
                bicimler = {_norm(x) for x in t.bicim.split("/")}
                if t.gunumuz and b.yasayan_mi(t.dil):
                    gunumuz.setdefault(t.dil, set()).update(bicimler)
                elif t.dil in b.tarihi:
                    tarihi.setdefault(t.dil, set()).update(bicimler)
            for kod, bc in k.bicimler.items():
                if kod not in gunumuz:
                    print(f"{m.kok} ← {ad}: {kod} kavramda var ({bc.bicim}), kök dosyasında tanığı yok")
                    sorun += 1
                elif _norm(bc.bicim) not in gunumuz[kod]:
                    print(f"{m.kok} ← {ad}: {kod} biçimi farklı: kavram {bc.bicim}, "
                          f"tanık {', '.join(sorted(gunumuz[kod]))}")
                    sorun += 1
            coklu = len(m.v.get("kavramlar") or []) > 1   # kök başka kavramlarda da kullanılıyor
            for kod in ([] if coklu else gunumuz):
                if kod not in k.bicimler:
                    print(f"{m.kok} → {ad}: {kod} tanıklı ama kavram dosyasında yok")
                    sorun += 1
            for kod, bc in k.tarihi.items():
                if _norm(bc) not in tarihi.get(kod, set()):
                    print(f"{m.kok} ← {ad}: tarihî {kod} = {bc} kök dosyasındaki tanıklarda yok")
                    sorun += 1
    print(f"\n{sorun} uyuşmazlık." if sorun else "Kök ve kavram dosyaları uyumlu.")
    return sorun


# ============================================================== çıktı

def _hucre(s) -> str:
    return str(s or "").replace("|", "\\|").replace("\n", " ").strip()


def _kaynak_bag(kimlikler: list[str], b: Baglam) -> str:
    return ", ".join("bilgi*" if k == "bilgi" else f"[{k}](../../kaynaklar/KAYNAKLAR.md#{k})"
                     for k in kimlikler)


def madde_md(m: Madde, b: Baglam) -> str:
    k = Kapsam(m, b)
    v = m.v
    y: list[str] = []
    y.append(f"# {m.kok}\n")
    y.append(f"> Bu sayfa `python3 araclar/sozluk.py --yaz` ile [`{m.yol.name}`]({m.yol.name}) "
             "dosyasından üretilir; elle düzenlemeyin.\n")
    y.append(f"- **Anlam:** {v.get('anlam', '')}")
    if v.get("ana_turkce"):
        y.append(f"- **Ana Türkçe:** {v['ana_turkce']}")
    y.append(f"- **Köken:** {v.get('koken', '')}")
    if v.get("kavramlar"):
        y.append("- **Kavramlar:** " + ", ".join(f"[{a}](../temel/{a}.yaml)" for a in v["kavramlar"]))
    if v.get("etimoloji"):
        y.append(f"- **Etimoloji:** {' '.join(str(v['etimoloji']).split())}")
    if k.ilk is not None:
        y.append(f"- **En eski tanık:** {yuzyil_yaz((k.ilk, k.ilk))}")
    y.append("")

    y.append("## Kapsam\n")
    y.append(f"**{k.ozet()}**\n")
    for d, dolu, n in k.duraklar:
        isaret = "✓" if dolu else ("✗" if d.get("zorunlu", True) else "·")
        ek = f" ({n} tanık)" if n else (" (araştırıldı, yok)" if dolu else "")
        y.append(f"- {isaret} {d['ad']}, {d['yuzyil']}. yy{ek}")
    if k.eksik_diller:
        y.append(f"\nTanığı olmayan diller: {', '.join(L.ad for L in k.eksik_diller)}.")
    y.append("\n`bilgi*`: kaynakla doğrulanmamış, genel Türkoloji bilgisine dayanan tanık.\n")

    tarihi = sorted((t for t in m.taniklar if not t.gunumuz),
                    key=lambda t: (t.yuzyil, b.sira.get(t.dil, 999)))
    if tarihi:
        y.append("## Zaman çizelgesi\n")
        y.append("| Yüzyıl | Dil / boy | Yer | Biçim | Yazı | Metin | Kaydeden | Kaynak |")
        y.append("|---|---|---|---|---|---|---|---|")
        for t in tarihi:
            a = t.alan
            dil = b.ad.get(t.dil, t.dil) + (f" ({a['boy']})" if a.get("boy") else "")
            kaydeden = _hucre(a.get("kaydeden")) + (" 🌍" if t.yabanci else "")
            kaynak = _kaynak_bag(t.kaynaklar, b) + (f" — {a['atif']}" if a.get("atif") else "")
            y.append(f"| {yuzyil_yaz(t.yuzyil)} | {_hucre(dil)} | {_hucre(a.get('yer'))} | "
                     f"**{_hucre(t.bicim)}** | {_hucre(a.get('yazi'))} | {_hucre(a.get('metin'))} | "
                     f"{kaydeden} | {kaynak} |")
        y.append("\n🌍 yabancı gözlemcinin ya da Türkçe olmayan bir dilde yazılmış sözlüğün kaydı.\n")
        notlu = [t for t in tarihi if t.alan.get("not")]
        if notlu:
            y.append("Notlar:\n")
            for t in notlu:
                y.append(f"- {yuzyil_yaz(t.yuzyil)}, {b.ad.get(t.dil, t.dil)}"
                         f"{' (' + t.alan['boy'] + ')' if t.alan.get('boy') else ''}: "
                         f"{' '.join(str(t.alan['not']).split())}")
            y.append("")

    y.append("## Yaşayan diller ve ağızlar\n")
    y.append("| Kol | Dil | Ağız | Biçim | Yazı | Anlam | Kaynak | Not |")
    y.append("|---|---|---|---|---|---|---|---|")
    gunumuz = sorted((t for t in m.taniklar if t.gunumuz), key=lambda t: b.sira.get(t.dil, 999))
    for t in gunumuz:
        L = b.dil_of.get(t.dil)
        agiz = b.ad.get(t.dil, t.dil) if (L and t.dil != L.kod) else ""
        y.append(f"| {L.kol.ad if L and L.kol else ''} | {L.ad if L else t.dil} | {agiz} | "
                 f"**{_hucre(t.bicim)}** | {_hucre(t.alan.get('yazi'))} | {_hucre(t.alan.get('anlam'))} | "
                 f"{_kaynak_bag(t.kaynaklar, b)} | {_hucre(t.alan.get('not'))} |")
    for kod, aciklama in m.yok.items():
        y.append(f"| | {b.ad.get(kod, kod)} | | — | | | | kök yok: {_hucre(aciklama)} |")
    y.append("")

    y.append("## Kaynakça\n")
    for kim in sorted(k.kaynaklar, key=lambda x: -k.kaynaklar[x]):
        y.append(f"- [{b.kaynaklar[kim]['ad']}](../../kaynaklar/KAYNAKLAR.md#{kim}) — {k.kaynaklar[kim]} tanık")
    return "\n".join(y) + "\n"


def dizin_md(maddeler: list[Madde], b: Baglam) -> str:
    y = ["# Tanıklı sözlük (Hedef 4)\n",
         "> Bu dosya `python3 araclar/sozluk.py --yaz` ile üretilir; elle düzenlemeyin. "
         "Her kök için tanıklar `sozluk/kok/<kök>.yaml` dosyasındadır. Seviyeler ve duraklar "
         "`hedefler.yaml`'da, kurallar ILKELER.md §14'te.\n",
         "Seviye 1: bütün yaşayan diller · Seviye 2: + tarihî duraklar · Seviye 3: + yabancıların kayıtları\n",
         "| Kök | Anlam | Seviye | Diller | Ağızlar | Duraklar | Tanık | Kaynaklı | Kaynak | En eski | Eksik duraklar |",
         "|---|---|---|---|---|---|---|---|---|---|---|"]
    for m in maddeler:
        k = Kapsam(m, b)
        zorunlu = [x for x in k.duraklar if x[0].get("zorunlu", True)]
        eksik = ", ".join(d["ad"].split(" (")[0] for d in k.eksik_duraklar if d.get("zorunlu", True))
        y.append(f"| [{m.kok}](kok/{m.yol.stem}.md) | {_hucre(m.v.get('anlam'))} | {k.seviye} | "
                 f"{len(k.diller) - len(k.eksik_diller)}/{len(k.diller)} | {k.agiz_dolu}/{k.agiz_toplam} | "
                 f"{sum(1 for _, d, _ in zorunlu if d)}/{len(zorunlu)} | {k.tanik} | "
                 f"%{100 * k.kaynakli / max(k.tanik, 1):.0f} | {len(k.kaynaklar)} | "
                 f"{yuzyil_yaz((k.ilk, k.ilk)) if k.ilk else '—'} | {eksik or '—'} |")
    return "\n".join(y) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("kokler", nargs="*", help="kök dosya adları (uzantısız)")
    ap.add_argument("--denetle", action="store_true", help="kavram dosyalarıyla uyumu denetle")
    ap.add_argument("--yaz", action="store_true", help="Markdown sayfalarını üret")
    args = ap.parse_args()
    b = Baglam()
    maddeler = maddeleri_yukle(b, args.kokler)
    if args.denetle:
        sys.exit(1 if denetle(maddeler, b) else 0)
    if args.yaz:
        for m in maddeler:
            m.yol.with_suffix(".md").write_text(madde_md(m, b), encoding="utf-8")
        if not args.kokler:
            DIZIN_DOSYASI.write_text(dizin_md(maddeleri_yukle(b, []), b), encoding="utf-8")
        print(f"{len(maddeler)} madde yazıldı.")
        return
    for m in maddeler:
        k = Kapsam(m, b)
        print(f"{m.kok:<12} {k.ozet()}")
        if args.kokler:
            for d in k.eksik_duraklar:
                print(f"    eksik durak: {d['ad']} ({d['yuzyil']}. yy)"
                      f"{'' if d.get('zorunlu', True) else ' [isteğe bağlı]'}")
            if k.eksik_diller:
                print(f"    tanığı olmayan diller: {', '.join(L.ad for L in k.eksik_diller)}")
            bilgi = [t.dil for t in m.taniklar if not t.kaynakli]
            if bilgi:
                print(f"    kaynaksız (bilgi) tanıklar: {', '.join(bilgi)}")


if __name__ == "__main__":
    main()
