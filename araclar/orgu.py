#!/usr/bin/env python3
"""Örgüyü (ag.yaml, anlaşılırlık bağları) toplanan veriden yeniden hesaplar.

Her dil çifti için, iki dilde de verisi olan kavramlarda:
  ortak  : iki dilin asıl (en yüksek tercihli) biçimi aynı kökten mi? (1; yalnız
           ikincil biçimler ortaksa 0.5; değilse 0)
  benzer : aynı kökten olan asıl biçimlerin çalışma yazımında benzerliği
           (1 - düzenleme uzaklığı / uzun olanın boyu)
  ölçü   = ortak oranı × ortalama benzerlik
Ölçü, ag.yaml'daki elle verilmiş tahminlere doğrusal olarak uydurulur
(tahmin ≈ a·ölçü + b); "beklenen" değer budur.

Kullanım:
  python3 araclar/orgu.py            # raporu yazdır (Markdown)
  python3 araclar/orgu.py --yaz      # ORGU.md'yi yaz, ag.yaml'daki "veriden" bölümünü yenile

ag.yaml'a yazma kuralları (yöntem sürüm 1):
  * Tahmini olmayan çiftler, beklenen değer ≥ ESIK ise veriden doldurulur
    ("veriden" bölümü; elle düzenlenmez, bu araçla yenilenir).
  * Elle verilmiş tahminlere bu araç dokunmaz; sapmalar raporda listelenir.
"""
from __future__ import annotations

import itertools
import re
import statistics as st
import sys
from pathlib import Path

import yaml

KOK = Path(__file__).resolve().parent.parent
AG = KOK / "ag.yaml"
RAPOR = KOK / "ORGU.md"
EN_AZ_KAVRAM = 40        # bir çift için gereken ortak veri
ESIK = 0.25              # bu beklenen değerin altındaki boş çiftler 0 kalır
SAPMA = 0.12             # raporda "sapan tahmin" sayılan fark
BAS, SON = "  # >>> veriden (araclar/orgu.py --yaz ile üretilir; elle düzenlemeyin)", "  # <<< veriden"


def _norm(s) -> str:
    return str(s).lower().split(",")[0].split("/")[0].strip()


def _lev(a: str, b: str) -> int:
    p = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        c = [i]
        for j, y in enumerate(b, 1):
            c.append(min(p[j] + 1, c[j - 1] + 1, p[j - 1] + (x != y)))
        p = c
    return p[-1]


def veri_yukle() -> dict[str, dict[str, list[tuple[str, str, float]]]]:
    """kavram -> dil -> [(kök, biçim, tercih)] (ağızlar ve Türk dilleri arası ödünçler hariç)."""
    veri = {}
    for p in sorted((KOK / "sozluk").rglob("*.yaml")):
        if "kok" in p.parts:
            continue
        v = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        if "kavram" not in v or "kokler" not in v:
            continue
        d: dict[str, list] = {}
        for k in v["kokler"]:
            ad = k["kok"] if str(k.get("koken", "türkçe")) == "türkçe" else "ALINTI:" + k["kok"]
            for dil, b in (k.get("bicimler") or {}).items():
                if "-" in dil:
                    continue
                tr = 1.0
                if isinstance(b, dict):
                    if b.get("odunc"):
                        continue
                    tr, b = float(b.get("tercih", 1)), b.get("bicim")
                d.setdefault(dil, []).append((ad, _norm(b), tr))
        veri[v["kavram"]] = d
    return veri


def olc(veri) -> dict[tuple[str, str], tuple[int, float, float]]:
    diller = sorted({l for d in veri.values() for l in d})
    sonuc = {}
    for a, b in itertools.combinations(diller, 2):
        n, ortak, benz = 0, 0.0, []
        for d in veri.values():
            if a not in d or b not in d:
                continue
            n += 1
            asil_a, asil_b = max(d[a], key=lambda x: x[2]), max(d[b], key=lambda x: x[2])
            if asil_a[0] == asil_b[0]:
                ortak += 1
                fa, fb = asil_a[1], asil_b[1]
                benz.append(1 - _lev(fa, fb) / max(len(fa), len(fb), 1))
            elif {k for k, *_ in d[a]} & {k for k, *_ in d[b]}:
                ortak += 0.5
        if n >= EN_AZ_KAVRAM:
            sonuc[(a, b)] = (n, ortak / n, st.mean(benz) if benz else 0.0)
    return sonuc


def elle_tahminler() -> dict[tuple[str, str], float]:
    """ag.yaml'daki elle verilmiş anlaşılırlık değerleri (veriden bölümü hariç), iki yönün ortalaması."""
    metin = AG.read_text(encoding="utf-8")
    if BAS in metin:
        metin = metin[: metin.index(BAS)] + metin[metin.index(SON) + len(SON):]
    t = {}
    for x in (yaml.safe_load(metin) or {}).get("anlasilirlik") or []:
        ab = float(x[2]); ba = float(x[3]) if len(x) > 3 else ab
        t[tuple(sorted(x[:2]))] = (ab + ba) / 2
    return t


def uydur(olcum, tahmin):
    ortak = [(o * s, tahmin[k]) for k, (n, o, s) in olcum.items() if k in tahmin]
    xs, ys = zip(*ortak)
    mx, my = st.mean(xs), st.mean(ys)
    sxy = sum((x - mx) * (y - my) for x, y in ortak)
    sxx = sum((x - mx) ** 2 for x in xs); syy = sum((y - my) ** 2 for y in ys)
    a = sxy / sxx
    return a, my - a * mx, sxy / (sxx * syy) ** 0.5, len(ortak)


def beklenen(a, b, x):
    return max(0.0, min(0.95, a * x + b))


def rapor(veri, olcum, tahmin, a, b, r, n_ortak, dolan) -> str:
    satir = ["# Örgünün veriden denetimi", "",
             "> Bu dosya `python3 araclar/orgu.py --yaz` komutuyla üretilir; elle düzenlemeyin.", "",
             f"Veri: {len(veri)} kavram. Ölçülen dil çifti: {len(olcum)} "
             f"(en az {EN_AZ_KAVRAM} ortak kavram). Elle tahmini olan çift: {len(tahmin)}.", "",
             "**Ölçü** = (asıl biçimleri aynı kökten olan kavramların oranı) × (o biçimlerin yazım benzerliği). "
             "Ölçü, ses düzenini ve dilbilgisini görmez ve çalışma yazımı farkları sildiği için benzerliği "
             "olduğundan yüksek gösterir; bu yüzden doğrudan değil, elle verilmiş tahminlere uydurularak kullanılır.", "",
             f"Uydurma: **tahmin ≈ {a:.2f} · ölçü {b:+.2f}**, korelasyon **{r:.2f}** ({n_ortak} çift).", "",
             "## Sapan tahminler", "",
             f"Elle verilen değerin veriden beklenenden {SAPMA} üzerinde farklı olduğu çiftler. "
             "Bu araç elle verilen değerleri değiştirmez; düzeltme ag.yaml'da gerekçesiyle yapılır.", "",
             "| Çift | Kavram | Ortak kök | Benzerlik | Ölçü | ag.yaml | Beklenen | Fark |", "|---|---|---|---|---|---|---|---|"]
    sap = []
    for k, (n, o, s) in olcum.items():
        if k in tahmin:
            e = beklenen(a, b, o * s)
            if abs(tahmin[k] - e) > SAPMA:
                sap.append((abs(tahmin[k] - e), k, n, o, s, tahmin[k], e))
    for _, k, n, o, s, t, e in sorted(sap, reverse=True):
        satir.append(f"| {k[0]}–{k[1]} | {n} | {o:.2f} | {s:.2f} | {o*s:.2f} | {t:.2f} | {e:.2f} | {t-e:+.2f} |")
    satir += ["", "## Veriden doldurulan çiftler", "",
              f"ag.yaml'da değeri olmayan (önceden 0 sayılan) ve beklenen değeri ≥ {ESIK} olan çiftler. "
              "ag.yaml'ın `veriden` bölümüne yazılır.", "",
              "| Çift | Kavram | Ortak kök | Benzerlik | Beklenen |", "|---|---|---|---|---|"]
    for k, n, o, s, e in sorted(dolan, key=lambda x: -x[4]):
        satir.append(f"| {k[0]}–{k[1]} | {n} | {o:.2f} | {s:.2f} | {e:.2f} |")
    return "\n".join(satir) + "\n"


def main():
    yaz = "--yaz" in sys.argv
    veri = veri_yukle()
    olcum = olc(veri)
    tahmin = elle_tahminler()
    a, b, r, n_ortak = uydur(olcum, tahmin)
    dolan = []
    for k, (n, o, s) in olcum.items():
        if k not in tahmin:
            e = beklenen(a, b, o * s)
            if e >= ESIK:
                dolan.append((k, n, o, s, e))
    md = rapor(veri, olcum, tahmin, a, b, r, n_ortak, dolan)
    if not yaz:
        print(md)
        return
    RAPOR.write_text(md, encoding="utf-8")
    metin = AG.read_text(encoding="utf-8")
    blok = [BAS, f"  # {len(veri)} kavramdan; tahmin ≈ {a:.2f}·ölçü {b:+.2f} (r = {r:.2f}). Ayrıntı: ORGU.md"]
    blok += [f"  - [{k[0]}, {k[1]}, {round(e, 2):.2f}]" for k, n, o, s, e in sorted(dolan)]
    blok.append(SON)
    if BAS in metin:
        metin = metin[: metin.index(BAS)] + "\n".join(blok) + metin[metin.index(SON) + len(SON):]
    else:
        i = metin.index("\nikinci_dil:")
        metin = metin[:i].rstrip("\n") + "\n" + "\n".join(blok) + "\n" + metin[i:]
    yaml.safe_load(metin)
    AG.write_text(metin, encoding="utf-8")
    print(f"ORGU.md yazıldı; ag.yaml'a {len(dolan)} çift veriden yazıldı (r = {r:.2f}).")


if __name__ == "__main__":
    main()
