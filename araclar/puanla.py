#!/usr/bin/env python3
"""Ortak Türk dili — kelime puanlama ve ağaç üzerinde seçim.

Kullanım:
    python3 araclar/puanla.py                  # tüm kavramlar
    python3 araclar/puanla.py tas dag          # sadece belirtilen kavram dosyaları
    python3 araclar/puanla.py --agirliklar     # her dilin ağırlığını göster
    python3 araclar/puanla.py --derinlik 2     # ağacı 2. seviyeye kadar göster
    python3 araclar/puanla.py --alfa 0.3 --delta 0.1 --beta 0.25

Yöntem ILKELER.md'de anlatılıyor. Kısaca:
  * Her düğümün çocukları arasındaki ağırlık  (yaprak_sayısı ** alfa).
    alfa=0 -> her dal eşit, alfa=1 -> her dil eşit.
  * Bir kökün bir düğümdeki yayılımı = çocuklarının yayılımının ağırlıklı
    ortalaması (verisi olmayan çocuklar hesaba katılmaz).
  * Puan = yayılım + beta * (Eski Türkçede tanıklanmış mı).
  * Sadece kökeni "türkçe" olan kökler seçilebilir.
  * Kökten yapraklara doğru her düğüm kendi en iyi kökünü seçer; ama bir üst
    düğümün seçimi, en iyi seçenekten en fazla `delta` geride ise korunur
    (süreklilik payı).
"""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML gerekli:  pip install -r requirements.txt")

KOK_DIZIN = Path(__file__).resolve().parent.parent
AGAC_DOSYASI = KOK_DIZIN / "agac.yaml"
SOZLUK_DIZIN = KOK_DIZIN / "sozluk"

VARSAYILAN_ALFA = 0.5
VARSAYILAN_BETA = 0.2
VARSAYILAN_DELTA = 0.15


# ----------------------------------------------------------------- ağaç

class Dugum:
    def __init__(self, veri: dict, ust: "Dugum | None" = None):
        self.ad: str = veri["ad"]
        self.kod: str = veri["kod"]
        self.carpan: float = float(veri.get("agirlik_carpani", 1.0))
        self.ust = ust
        self.alt = [Dugum(c, self) for c in veri.get("alt", [])]
        self.yaprak_sayisi = 1 if not self.alt else sum(c.yaprak_sayisi for c in self.alt)

    @property
    def yaprak_mi(self) -> bool:
        return not self.alt

    def yapraklar(self):
        if self.yaprak_mi:
            yield self
        for c in self.alt:
            yield from c.yapraklar()

    def tum_dugumler(self):
        yield self
        for c in self.alt:
            yield from c.tum_dugumler()


def agac_yukle() -> Dugum:
    with open(AGAC_DOSYASI, encoding="utf-8") as f:
        kok = Dugum(yaml.safe_load(f))
    kodlar = [d.kod for d in kok.tum_dugumler()]
    tekrar = {k for k in kodlar if kodlar.count(k) > 1}
    if tekrar:
        sys.exit(f"agac.yaml içinde tekrar eden kodlar: {sorted(tekrar)}")
    return kok


def cocuk_agirligi(c: Dugum, alfa: float) -> float:
    return (c.yaprak_sayisi ** alfa) * c.carpan


def yaprak_agirliklari(dugum: Dugum, alfa: float) -> dict[str, float]:
    """Düğümün alt ağacındaki her dilin (toplamı 1 olan) ağırlığı."""
    if dugum.yaprak_mi:
        return {dugum.kod: 1.0}
    toplam = sum(cocuk_agirligi(c, alfa) for c in dugum.alt)
    sonuc: dict[str, float] = {}
    for c in dugum.alt:
        pay = cocuk_agirligi(c, alfa) / toplam
        for kod, w in yaprak_agirliklari(c, alfa).items():
            sonuc[kod] = pay * w
    return sonuc


# --------------------------------------------------------------- sözlük

class Kok:
    """Bir kavramın aday kökü (etimonu)."""

    def __init__(self, veri: dict):
        self.kimlik: str = str(veri["kok"])
        self.eski_turkce: str | None = veri.get("eski_turkce") or None
        self.koken: str = str(veri.get("koken", "belirsiz"))
        self.kaynak: str = str(veri.get("kaynak", ""))
        self.not_: str = str(veri.get("not", ""))
        self.bicimler: dict[str, tuple[str, float]] = {}
        for dil, deger in (veri.get("bicimler") or {}).items():
            if isinstance(deger, dict):
                self.bicimler[dil] = (str(deger["bicim"]), float(deger.get("tercih", 1.0)))
            else:
                self.bicimler[dil] = (str(deger), 1.0)

    @property
    def secilebilir(self) -> bool:
        return self.koken == "türkçe"


class Kavram:
    def __init__(self, yol: Path, veri: dict):
        self.yol = yol
        self.ad: str = veri["kavram"]
        self.ingilizce: str = veri.get("ingilizce", "")
        self.dogrulandi: bool = bool(veri.get("dogrulandi", False))
        self.kokler = [Kok(k) for k in veri.get("kokler", [])]
        self.bilinen_diller: set[str] = set(veri.get("yok") or [])
        for k in self.kokler:
            self.bilinen_diller |= set(k.bicimler)

    def kok(self, kimlik: str) -> Kok:
        return next(k for k in self.kokler if k.kimlik == kimlik)


def kavramlari_yukle(secilenler: list[str], agac: Dugum) -> list[Kavram]:
    dosyalar = sorted(SOZLUK_DIZIN.rglob("*.yaml"))
    if secilenler:
        dosyalar = [d for d in dosyalar if d.stem in secilenler]
        bulunamayan = set(secilenler) - {d.stem for d in dosyalar}
        if bulunamayan:
            sys.exit(f"Bulunamayan kavram dosyaları: {sorted(bulunamayan)}")
    gecerli_diller = {y.kod for y in agac.yapraklar()}
    kavramlar = []
    for d in dosyalar:
        with open(d, encoding="utf-8") as f:
            kv = Kavram(d, yaml.safe_load(f))
        bilinmeyen = kv.bilinen_diller - gecerli_diller
        if bilinmeyen:
            sys.exit(f"{d.name}: agac.yaml'da olmayan dil kodları: {sorted(bilinmeyen)}")
        kavramlar.append(kv)
    return kavramlar


# ------------------------------------------------------------ puanlama

def yayilim(dugum: Dugum, kok: Kok, kavram: Kavram, alfa: float) -> float | None:
    """Kökün düğüm altındaki yayılımı (0..1). Hiç veri yoksa None."""
    if dugum.yaprak_mi:
        if dugum.kod not in kavram.bilinen_diller:
            return None
        return kok.bicimler.get(dugum.kod, ("", 0.0))[1]
    pay = payda = 0.0
    for c in dugum.alt:
        s = yayilim(c, kok, kavram, alfa)
        if s is None:
            continue
        w = cocuk_agirligi(c, alfa)
        pay += w * s
        payda += w
    return pay / payda if payda else None


def kapsama(dugum: Dugum, kavram: Kavram, alfa: float) -> float:
    """Düğümün ağırlığının ne kadarı için veri var (0..1)."""
    w = yaprak_agirliklari(dugum, alfa)
    return sum(v for k, v in w.items() if k in kavram.bilinen_diller)


def puan(dugum, kok, kavram, alfa, beta) -> float | None:
    y = yayilim(dugum, kok, kavram, alfa)
    if y is None:
        return None
    return y + (beta if kok.eski_turkce else 0.0)


def baskin_bicim(dugum: Dugum, kok: Kok, alfa: float, delta: float,
                 ust_bicim: str | None) -> str | None:
    """Kökün düğüm altındaki dillerde ağırlıkça en yaygın biçimi.

    Üst düğümün biçimi, en yaygın biçimden en fazla `delta` geride ise korunur
    (biçimde de süreklilik payı) — böylece dallar ses farkları yüzünden
    gereksiz yere parçalanmaz.
    """
    sayac: dict[str, float] = defaultdict(float)
    for dil, w in yaprak_agirliklari(dugum, alfa).items():
        if dil in kok.bicimler:
            bicim, tercih = kok.bicimler[dil]
            sayac[bicim] += w * tercih
    if not sayac:
        return None
    toplam = sum(sayac.values())
    en_iyi, en_iyi_pay = max(sayac.items(), key=lambda kv: (kv[1], kv[0]))
    if ust_bicim in sayac and (en_iyi_pay - sayac[ust_bicim]) / toplam < delta:
        return ust_bicim
    return en_iyi


# -------------------------------------------------------------- seçim

class Secim:
    def __init__(self, dugum, kok, bicim, puanlar, miras, gunluk=None):
        self.dugum: Dugum = dugum
        self.kok: Kok = kok
        self.bicim: str = bicim
        self.puanlar: dict[str, float] = puanlar
        self.miras: bool = miras  # veri yok ya da Türkçe aday yok -> üstten alındı
        self.gunluk: str | None = gunluk  # yapraklarda: dilin bugün en çok kullandığı biçim
        self.alt: list[Secim] = []


def sec(dugum: Dugum, kavram: Kavram, alfa, beta, delta, ust: Secim | None = None) -> Secim:
    puanlar: dict[str, float] = {}
    for k in kavram.kokler:
        if not k.secilebilir:
            continue
        y = yayilim(dugum, k, kavram, alfa)
        if y:  # None ya da 0 değil
            puanlar[k.kimlik] = y + (beta if k.eski_turkce else 0.0)

    gunluk = None
    if dugum.yaprak_mi and dugum.kod in kavram.bilinen_diller:
        adaylar = [(k.bicimler[dugum.kod][1], k.bicimler[dugum.kod][0])
                   for k in kavram.kokler if dugum.kod in k.bicimler]
        gunluk = max(adaylar)[1] if adaylar else None

    if not puanlar:
        if ust is None:
            raise ValueError(f"{kavram.yol.name}: Türkçe kökenli hiçbir aday yok")
        s = Secim(dugum, ust.kok, ust.bicim, {}, miras=True, gunluk=gunluk)
    else:
        en_iyi = max(puanlar, key=lambda k: (puanlar[k], k))
        if ust is not None and ust.kok.kimlik in puanlar:
            if puanlar[en_iyi] - puanlar[ust.kok.kimlik] < delta:
                en_iyi = ust.kok.kimlik
        kok = kavram.kok(en_iyi)
        if ust is None:  # en tepe: Eski Türkçe biçim
            bicim = kok.eski_turkce or kok.kimlik
        elif dugum.yaprak_mi:
            bicim = kok.bicimler[dugum.kod][0]
        else:
            bicim = baskin_bicim(dugum, kok, alfa, delta, ust.bicim) or ust.bicim
        s = Secim(dugum, kok, bicim, puanlar, miras=False, gunluk=gunluk)

    s.alt = [sec(c, kavram, alfa, beta, delta, s) for c in dugum.alt]
    return s


# -------------------------------------------------------------- çıktı

def yazdir(s: Secim, derinlik: int, seviye: int = 0, ust: Secim | None = None):
    if derinlik >= 0 and seviye > derinlik:
        return
    girinti = "  " * seviye
    etiket = f"{girinti}{s.dugum.ad}"
    satir = f"{etiket:<42} {s.bicim:<14}"
    notlar = []
    if ust is not None and s.kok is not ust.kok:
        notlar.append(f"farklı kök: {s.kok.kimlik}")
    if s.miras:
        notlar.append("üstten" + (" (veri yok)" if s.gunluk is None else ""))
    if s.gunluk and s.gunluk != s.bicim:
        notlar.append(f"günlük: {s.gunluk}")
    if notlar:
        satir += "  ← " + "; ".join(notlar)
    print(satir)
    for c in s.alt:
        yazdir(c, derinlik, seviye + 1, s)


def kavram_raporu(kv: Kavram, agac: Dugum, alfa, beta, delta, derinlik):
    durum = "doğrulandı" if kv.dogrulandi else "DOĞRULANMADI"
    print("=" * 78)
    print(f"{kv.ad}  ({kv.ingilizce})  [{durum}]  kapsama: %{100 * kapsama(agac, kv, alfa):.0f}")
    print("-" * 78)
    print("Adaylar (en tepede):")
    for k in sorted(kv.kokler, key=lambda k: -(puan(agac, k, kv, alfa, beta) or 0)):
        y = yayilim(agac, k, kv, alfa) or 0.0
        p = puan(agac, k, kv, alfa, beta) or 0.0
        eski = f"ET: {k.eski_turkce}" if k.eski_turkce else "ET: —"
        uygun = "" if k.secilebilir else f"  (seçilemez: köken={k.koken})"
        print(f"  {k.kimlik:<10} yayılım {y:5.2f}  puan {p:5.2f}  {eski}{uygun}")
    print()
    yazdir(sec(agac, kv, alfa, beta, delta), derinlik)
    print()


def agirlik_raporu(agac: Dugum, alfa: float):
    print(f"Dil ağırlıkları (alfa = {alfa}):\n")
    w = yaprak_agirliklari(agac, alfa)

    def gez(d: Dugum, seviye: int, pay: float):
        etiket = "  " * seviye + d.ad
        print(f"{etiket:<44} %{100 * pay:5.1f}")
        if d.alt:
            toplam = sum(cocuk_agirligi(c, alfa) for c in d.alt)
            for c in d.alt:
                gez(c, seviye + 1, pay * cocuk_agirligi(c, alfa) / toplam)

    gez(agac, 0, 1.0)
    print(f"\nDil sayısı: {len(w)}   en ağır: %{100 * max(w.values()):.1f}   "
          f"en hafif: %{100 * min(w.values()):.1f}   (her dil eşit olsaydı: %{100 / len(w):.1f})")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("kavramlar", nargs="*", help="kavram dosya adları (uzantısız)")
    ap.add_argument("--alfa", type=float, default=VARSAYILAN_ALFA)
    ap.add_argument("--beta", type=float, default=VARSAYILAN_BETA)
    ap.add_argument("--delta", type=float, default=VARSAYILAN_DELTA)
    ap.add_argument("--derinlik", type=int, default=-1, help="gösterilecek en derin seviye (-1: tümü)")
    ap.add_argument("--agirliklar", action="store_true", help="dil ağırlıklarını göster ve çık")
    a = ap.parse_args()

    agac = agac_yukle()
    if a.agirliklar:
        agirlik_raporu(agac, a.alfa)
        return
    for kv in kavramlari_yukle(a.kavramlar, agac):
        kavram_raporu(kv, agac, a.alfa, a.beta, a.delta, a.derinlik)


if __name__ == "__main__":
    main()
