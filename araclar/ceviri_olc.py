#!/usr/bin/env python3
"""Hedef 5 ölçüm aracı: çevirileri ceviri/olcu/ test setleriyle chrF ile puanlar.

chrF (Popović 2015): karakter 1–6 gramlarında kesinlik ve duyarlılığın F-β
ortalaması (β = 2). Eklemeli dillerde kelime tabanlı BLEU'dan uygundur. Her iki
taraf önce çalışma yazımına aktarılır (araclar/yazim.py); böylece Kiril ve
Latin yazılı aynı metin aynı sayılır.

  python3 araclar/ceviri_olc.py --kopya              # çevirmeden: kaynak = çeviri
  python3 araclar/ceviri_olc.py --kopya --md > ceviri/KOPYA.md
  python3 araclar/ceviri_olc.py --cevrilen dosya.tsv --kaynak tur --hedef aze
      dosya.tsv: her satırda "<kaynak_id>\\t<çeviri>"

"Kopya" ölçüsü bir taban çizgisidir: iki dil hiç çevrilmeden ne kadar örtüşüyor?
Gerçek bir çeviri bu çizginin belirgin üstünde olmalıdır.
"""
from __future__ import annotations

import argparse
import collections
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from yazim import calisma  # noqa: E402

KOK = Path(__file__).resolve().parent.parent
SETLER = KOK / "ceviri" / "olcu" / "tatoeba"
N, BETA = 6, 2.0


def _ngram(s: str, n: int) -> collections.Counter:
    s = s.replace(" ", "")
    return collections.Counter(s[i:i + n] for i in range(len(s) - n + 1))


def chrf(cevrilenler: list[str], referanslar: list[str]) -> float:
    """Derlem düzeyinde chrF (0–100)."""
    eslesen = [0] * N; hip = [0] * N; ref = [0] * N
    for h, r in zip(cevrilenler, referanslar):
        for n in range(1, N + 1):
            hn, rn = _ngram(h, n), _ngram(r, n)
            eslesen[n - 1] += sum((hn & rn).values())
            hip[n - 1] += sum(hn.values()); ref[n - 1] += sum(rn.values())
    p = sum(e / h for e, h in zip(eslesen, hip) if h) / N
    r = sum(e / f for e, f in zip(eslesen, ref) if f) / N
    if p + r == 0:
        return 0.0
    b2 = BETA ** 2
    return 100 * (1 + b2) * p * r / (b2 * p + r)


def set_oku(kaynak: str, hedef: str):
    """[(kaynak_id, kaynak, hedef)] — dosya hangi sırayla yazılmış olursa olsun."""
    for ad, ters in ((f"{kaynak}-{hedef}.tsv", False), (f"{hedef}-{kaynak}.tsv", True)):
        p = SETLER / ad
        if p.exists():
            rows = list(csv.reader(open(p, encoding="utf-8"), delimiter="\t", quoting=csv.QUOTE_NONE))[1:]
            return [(r[2], r[3], r[1]) if ters else (r[0], r[1], r[3]) for r in rows]
    return None


def ciftler():
    for p in sorted(SETLER.glob("*-*.tsv")):
        a, b = p.stem.split("-")
        yield a, b


def kopya_tablosu(md: bool):
    satirlar = []
    for a, b in ciftler():
        for k, h in ((a, b), (b, a)):
            s = set_oku(k, h)
            hip = [calisma(k, x[1]) for x in s]
            ref = [calisma(h, x[2]) for x in s]
            satirlar.append((k, h, len(s), chrf(hip, ref)))
    if md:
        print("# Çevirisiz örtüşme (kopya taban çizgisi)\n")
        print("> Bu dosya `python3 araclar/ceviri_olc.py --kopya --md > ceviri/KOPYA.md` ile üretilir.\n")
        print("Kaynak cümle hiç çevrilmeden hedef dilin referansıyla karşılaştırıldığında chrF "
              "(iki taraf da çalışma yazımında). Gerçek bir çeviri bu değerin belirgin üstünde "
              "olmalıdır. Değer aynı zamanda iki dilin yazıda ne kadar örtüştüğünü gösterir.\n")
        print("| Kaynak | Hedef | Cümle | chrF |\n|---|---|---|---|")
        for k, h, n, c in sorted(satirlar, key=lambda x: -x[3]):
            print(f"| {k} | {h} | {n} | {c:.1f} |")
    else:
        for k, h, n, c in sorted(satirlar, key=lambda x: -x[3]):
            print(f"{k}→{h}\t{n}\t{c:.1f}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kopya", action="store_true")
    ap.add_argument("--md", action="store_true")
    ap.add_argument("--cevrilen")
    ap.add_argument("--kaynak")
    ap.add_argument("--hedef")
    a = ap.parse_args()
    if a.kopya:
        kopya_tablosu(a.md)
        return
    s = set_oku(a.kaynak, a.hedef)
    if s is None:
        sys.exit(f"{a.kaynak}-{a.hedef} için test seti yok")
    cev = {}
    for satir in open(a.cevrilen, encoding="utf-8"):
        p = satir.rstrip("\n").split("\t", 1)
        if len(p) == 2:
            cev[p[0]] = p[1]
    eksik = [x for x in s if x[0] not in cev]
    if eksik:
        print(f"uyarı: {len(eksik)} cümlenin çevirisi yok; boş sayıldı", file=sys.stderr)
    hip = [calisma(a.hedef, cev.get(x[0], "")) for x in s]
    ref = [calisma(a.hedef, x[2]) for x in s]
    kop = [calisma(a.kaynak, x[1]) for x in s]
    print(f"{a.kaynak}→{a.hedef}: {len(s)} cümle  chrF {chrf(hip, ref):.1f}  (kopya taban çizgisi {chrf(kop, ref):.1f})")


if __name__ == "__main__":
    main()
