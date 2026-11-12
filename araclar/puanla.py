#!/usr/bin/env python3
"""Ortak Türk dili — kelime puanlama ve ağaç üzerinde seçim (üç hedef).

Kullanım:
    python3 araclar/puanla.py                     # tüm kavramlar, asıl hedef (ortak dil)
    python3 araclar/puanla.py tas dag             # sadece belirtilen kavram dosyaları
    python3 araclar/puanla.py --hedef ana         # başka bir hedef: ortak | ana | nufus
    python3 araclar/puanla.py --karsilastir       # üç hedefin seçimlerini yan yana göster
    python3 araclar/puanla.py --derinlik 2        # ağacı 2. seviyeye kadar göster
    python3 araclar/puanla.py --agizlar           # dillerin altındaki ağızları da göster
    python3 araclar/puanla.py --agirliklar        # ağırlık tablosu (seçili hedef)
    python3 araclar/puanla.py --agirliklar --md   # üç hedefin ağırlık tabloları (Markdown)

Hedefler hedefler.yaml'da, yöntem ILKELER.md'de. Kısaca, hesap ALTTAN YUKARI yapılır:
  * Ağızlar birleşerek dili, diller dalı, dallar kolu, kollar en tepeyi oluşturur.
    Her birleşimde çocuklar hedefin ağırlık kuralıyla tartılır.
  * yayılım      : kök, ağırlıkça dillerin ne kadarında yaşıyor (0..1)
  * anlaşılırlık : önerilen biçim, ağırlıkça dillerde ne kadar tanıdık (0..1)
  * eskilik      : kökü kaydeden tarihî tanıkların ağırlıklı oranı (0..1)
  * kök puanı    = ölçü (anlaşılırlık ya da yayılım) + beta * eskilik
  * Sadece kökeni "türkçe" olan kökler aday olabilir.
  * Her düğüm SADECE kendi altına bakarak seçer. Üstten gelen tek şey, verisi
    olmayan ya da Türkçe kökü kaybetmiş düğümlere önerilen kelimedir (canlandırma).
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
TARIHI_DOSYASI = KOK_DIZIN / "tarihi.yaml"
HEDEF_DOSYASI = KOK_DIZIN / "hedefler.yaml"
SOZLUK_DIZIN = KOK_DIZIN / "sozluk"


# ================================================================== ağaç

DUGUM_ALANLARI = {"ad", "kod", "tip", "not", "alt", "agirlik_carpani", "konusur", "konusur_not", "seffaf"}
EN_AZ_BASAMAK, EN_COK_BASAMAK = 2, 8


def basamak(konusur: int) -> int:
    """Büyüklük basamağı: konuşur sayısı her 10 kat arttığında +1 (2..8).

    100'den az: 2 · 100-1000: 3 · 1-10 bin: 4 · 10-100 bin: 5 · 100 bin-1 milyon: 6
    1-10 milyon: 7 · 10 milyon ve üstü: 8
    """
    b = len(str(max(int(konusur), 1)))  # basamak sayısı = floor(log10) + 1
    return max(EN_AZ_BASAMAK, min(EN_COK_BASAMAK, b))


class Dugum:
    def __init__(self, veri: dict, ust: "Dugum | None" = None, dil_ici: bool = False,
                 yazi_dili: bool = False):
        if bilinmeyen := set(veri) - DUGUM_ALANLARI:
            sys.exit(f"agac.yaml: '{veri.get('ad')}' düğümünde bilinmeyen alan(lar): {sorted(bilinmeyen)} "
                     "(adında virgül varsa tırnak içine alın)")
        self.ad: str = veri["ad"]
        self.kod: str = veri["kod"]
        self.tip: str = veri.get("tip", "")
        self.not_: str = veri.get("not", "")
        self.carpan: float = float(veri.get("agirlik_carpani", 1.0))
        self.seffaf: bool = bool(veri.get("seffaf", False))  # sadece soy bilgisi
        self.ust = ust
        self.dil_ici = dil_ici          # bir dilin altında (ağız) mı?
        self.yazi_dili = yazi_dili      # otomatik eklenen "Yazı dili" yaprağı mı?
        alt_veri = veri.get("alt", [])
        self.dil_mi = self.tip == "dil" or (not alt_veri and not dil_ici)
        self.alt = [Dugum(c, self, dil_ici or self.dil_mi) for c in alt_veri]
        if self.dil_mi and self.alt:
            self.alt.insert(0, Dugum({"ad": "Yazı dili", "kod": self.kod}, self, True, True))
        self.yaprak_sayisi = 1 if not self.alt else sum(c.yaprak_sayisi for c in self.alt)
        self.dil_sayisi = 1 if self.dil_mi else sum(c.dil_sayisi for c in self.alt)
        if self.dil_mi and not yazi_dili:
            if "konusur" not in veri:
                sys.exit(f"agac.yaml: '{self.ad}' dilinin `konusur` (konuşur sayısı) alanı eksik")
            self.konusur = int(veri["konusur"])
            self.basamak = basamak(self.konusur)
        ust_duzey = [c for c in self.alt if not c.dil_ici]
        self.basamak_toplam = (self.basamak if self.dil_mi and not yazi_dili
                               else sum(c.basamak_toplam for c in ust_duzey))
        self.konusur_toplam = (self.konusur if self.dil_mi and not yazi_dili
                               else sum(c.konusur_toplam for c in ust_duzey))
        self.yaprak_kodlari = ({self.kod} if not self.alt
                               else set().union(*(c.yaprak_kodlari for c in self.alt)))

    @property
    def yaprak_mi(self) -> bool:
        return not self.alt

    def tartim_cocuklari(self, seffaf: bool) -> list["Dugum"]:
        """Tartımda kardeş sayılan çocuklar. `seffaf` ise şeffaf bir çocuğun yerine
        onun çocukları geçer."""
        if not seffaf:
            return self.alt
        sonuc = []
        for c in self.alt:
            sonuc.extend(c.tartim_cocuklari(True) if c.seffaf else [c])
        return sonuc

    def tum_dugumler(self):
        yield self
        for c in self.alt:
            yield from c.tum_dugumler()

    def ustler(self):
        d = self.ust
        while d is not None:
            yield d
            d = d.ust


def agac_yukle() -> Dugum:
    with open(AGAC_DOSYASI, encoding="utf-8") as f:
        kok = Dugum(yaml.safe_load(f))
    kodlar = [d.kod for d in kok.tum_dugumler() if not d.yazi_dili]
    if tekrar := {k for k in kodlar if kodlar.count(k) > 1}:
        sys.exit(f"agac.yaml içinde tekrar eden kodlar: {sorted(tekrar)}")
    return kok


# ======================================================= tarihî tanıklar

class Tanik:
    def __init__(self, veri: dict, dal: Dugum):
        self.ad: str = veri["ad"]
        self.kod: str = veri["kod"]
        self.dal = dal
        self.agirlik = float(veri.get("agirlik", 1.0))
        self.sira = int(veri.get("sira", 99))
        self.kosullar: list[Dugum] = []  # türetilmiş tanık: kök bu düğümlerin HEPSİNDE varsa

    @property
    def turetilmis(self) -> bool:
        return bool(self.kosullar)

    def ilgili(self, dugum: Dugum) -> bool:
        """Bu tanık, `dugum`de verilen kararda sayılır mı? (kendi, üst ya da alt dalı)"""
        return self.dal is dugum or self.dal in dugum.ustler() or dugum in self.dal.ustler()

    def altinda(self, dugum: Dugum) -> bool:
        """Tanık bu düğüme ya da altındaki bir dala mı bağlı?"""
        return self.dal is dugum or dugum in self.dal.ustler()

    def durum(self, kok: "Kok", kv: "Kavram", taniklar: list["Tanik"]) -> tuple[bool, bool]:
        """(bu kavram için bilgi var mı, kök tanıklanıyor mu)"""
        if not self.turetilmis:
            return self.kod in kv.bilinen_taniklar, self.kod in kok.tarihi
        bilinen = var = True
        for d in self.kosullar:
            altlar = [t for t in taniklar if not t.turetilmis and t.altinda(d)]
            d_bilinen = bool(d.yaprak_kodlari & kv.bilinen_diller) or any(t.kod in kv.bilinen_taniklar for t in altlar)
            d_var = bool(d.yaprak_kodlari & set(kok.bicimler)) or any(t.kod in kok.tarihi for t in altlar)
            bilinen &= d_bilinen
            var &= d_var
        return bilinen, var and bilinen


def taniklari_yukle(agac: Dugum) -> list[Tanik]:
    dugumler = {d.kod: d for d in agac.tum_dugumler() if not d.yazi_dili}
    with open(TARIHI_DOSYASI, encoding="utf-8") as f:
        veri = yaml.safe_load(f) or []
    taniklar = []
    for t in veri:
        if t["dal"] not in dugumler:
            sys.exit(f"tarihi.yaml: '{t['kod']}' için bilinmeyen dal '{t['dal']}'")
        tanik = Tanik(t, dugumler[t["dal"]])
        for k in t.get("kosullar") or []:
            if k not in dugumler:
                sys.exit(f"tarihi.yaml: '{t['kod']}' koşulunda bilinmeyen düğüm '{k}'")
            tanik.kosullar.append(dugumler[k])
        taniklar.append(tanik)
    return sorted(taniklar, key=lambda t: t.sira)


# ============================================================== hedefler

AGIRLIK_TURLERI = {"basamak", "soy", "nufus"}


class Hedef:
    def __init__(self, veri: dict, tum_taniklar: list[Tanik]):
        self.kod: str = veri["kod"]
        self.ad: str = veri["ad"]
        self.soru: str = veri.get("soru", "")
        self.asil: bool = bool(veri.get("asil", False))
        self.agirlik: str = veri["agirlik"]
        if self.agirlik not in AGIRLIK_TURLERI:
            sys.exit(f"hedefler.yaml: '{self.kod}' için bilinmeyen ağırlık türü '{self.agirlik}'")
        self.alfa = float(veri.get("alfa", 0.5))
        self.agiz_alfa = float(veri.get("agiz_alfa", 0.5))
        self.yazi_dili_payi: float | None = veri.get("yazi_dili_payi")  # None: ağızlardan biri gibi
        self.seffaf = bool(veri.get("seffaf", False))
        self.olcu: str = veri.get("olcu", "anlasilirlik")
        self.beta = float(veri.get("beta", 0.2))
        self.taban = float(veri.get("taban", 0.5))
        self.bicim: str = veri.get("bicim", "anlasilir")
        self.esik: float | None = veri.get("esik")
        self.tanik_kapsami: str = veri.get("tanik_kapsami", "ilgili")  # ilgili | alt
        turetilmis = bool(veri.get("turetilmis_taniklar", False))
        self.taniklar = [t for t in tum_taniklar if turetilmis or not t.turetilmis]


def hedefleri_yukle(taniklar: list[Tanik]) -> dict[str, Hedef]:
    with open(HEDEF_DOSYASI, encoding="utf-8") as f:
        return {h.kod: h for h in (Hedef(v, taniklar) for v in yaml.safe_load(f))}


def cocuk_agirligi(c: Dugum, h: Hedef) -> float:
    """Bir çocuğun kardeşleri arasındaki (normalleştirilmemiş) ağırlığı."""
    if h.agirlik == "soy":
        return c.carpan
    if c.dil_ici:  # ağızlar
        return (c.yaprak_sayisi ** h.agiz_alfa) * c.carpan
    if h.agirlik == "nufus":
        return float(c.konusur_toplam) * c.carpan
    return (c.basamak_toplam / c.dil_sayisi) * (c.dil_sayisi ** h.alfa) * c.carpan


def cocuk_agirliklari(dugum: Dugum, h: Hedef) -> list[tuple[Dugum, float]]:
    """Çocuklar ve (normalleştirilmemiş) ağırlıkları.

    Hedefin `yazi_dili_payi` varsa, bir dilin yazı dili o payı, ağızları toplamda
    kalanını alır."""
    cocuklar = [(c, cocuk_agirligi(c, h)) for c in dugum.tartim_cocuklari(h.seffaf)]
    if h.yazi_dili_payi is not None and dugum.dil_mi and len(cocuklar) > 1:
        agizlar = sum(w for c, w in cocuklar if not c.yazi_dili)
        oran = h.yazi_dili_payi / (1 - h.yazi_dili_payi)
        cocuklar = [(c, agizlar * oran if c.yazi_dili else w) for c, w in cocuklar]
    return cocuklar


def paylar(dugum: Dugum, h: Hedef) -> list[tuple[Dugum, float]]:
    cocuklar = cocuk_agirliklari(dugum, h)
    toplam = sum(w for _, w in cocuklar)
    return [(c, w / toplam) for c, w in cocuklar]


def yaprak_agirliklari(dugum: Dugum, h: Hedef) -> dict[str, float]:
    if dugum.yaprak_mi:
        return {dugum.kod: 1.0}
    sonuc: dict[str, float] = {}
    for c, pay in paylar(dugum, h):
        for kod, w in yaprak_agirliklari(c, h).items():
            sonuc[kod] = pay * w
    return sonuc


def ortalama(dugum: Dugum, deger, h: Hedef) -> float | None:
    """Alttan yukarı ağırlıklı ortalama. deger(yaprak_kodu) -> sayı ya da None (veri yok)."""
    if dugum.yaprak_mi:
        return deger(dugum.kod)
    pay = payda = 0.0
    for c, w in cocuk_agirliklari(dugum, h):
        s = ortalama(c, deger, h)
        if s is None:
            continue
        pay += w * s
        payda += w
    return pay / payda if payda else None


# ========================================================= ses yakınlığı
# Biçimlerin birbirine ne kadar benzediği, harf değişimlerinin "maliyeti" ile
# ölçülür. Türk dillerinde düzenli olarak birbirine dönüşen sesler (t~d,
# ş~s, ğ~w~v, y~c~j …) yarım maliyetlidir; bir Türk kulağı bunları kolayca eşler.

SES_SINIFLARI = [set(s) for s in (
    "aäeəăĕ", "ıi", "oöuü",                  # ünlüler
    "td", "kgğqx", "ğwv", "wu", "bpvwf",      # ünsüzler
    "szşç", "cçj", "yjc", "sh", "kh", "nñm", "lr",
)]
UNLULER = set("aäeəăĕıioöuü")


def _normal(s: str) -> str:
    return s.lower().replace("'", "").replace("ʼ", "").replace("’", "").lstrip("*")


def _degisim(a: str, b: str) -> float:
    if a == b:
        return 0.0
    if any(a in s and b in s for s in SES_SINIFLARI):
        return 0.5
    if a in UNLULER and b in UNLULER:
        return 0.75
    return 1.0


def ses_mesafesi(a: str, b: str) -> float:
    a, b = _normal(a), _normal(b)
    onceki = [float(j) for j in range(len(b) + 1)]
    for i, ca in enumerate(a, 1):
        simdiki = [float(i)]
        for j, cb in enumerate(b, 1):
            simdiki.append(min(onceki[j] + 1, simdiki[j - 1] + 1, onceki[j - 1] + _degisim(ca, cb)))
        onceki = simdiki
    return onceki[-1]


def benzerlik(a: str, b: str) -> float:
    uzun = max(len(_normal(a)), len(_normal(b)), 1)
    return max(0.0, 1.0 - ses_mesafesi(a, b) / uzun)


# ================================================================ sözlük

def _bicim_oku(deger) -> tuple[str, float]:
    if isinstance(deger, dict):
        return str(deger["bicim"]), float(deger.get("tercih", 1.0))
    return str(deger), 1.0


class Kok:
    """Bir kavramın aday kökü (etimonu)."""

    def __init__(self, veri: dict):
        self.kimlik: str = str(veri["kok"])
        self.koken: str = str(veri.get("koken", "belirsiz"))
        self.kaynak: str = str(veri.get("kaynak", ""))
        self.not_: str = str(veri.get("not", ""))
        self.ana_turkce: str = str(veri.get("ana_turkce", ""))  # bilimsel yeniden kuruluş (karşılaştırma için)
        self.bicimler = {d: _bicim_oku(v) for d, v in (veri.get("bicimler") or {}).items()}
        self.tarihi = {d: _bicim_oku(v)[0] for d, v in (veri.get("tarihi") or {}).items()}

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
        self.bilinen_taniklar: set[str] = set(veri.get("tarihi_yok") or [])
        for k in self.kokler:
            self.bilinen_diller |= set(k.bicimler)
            self.bilinen_taniklar |= set(k.tarihi)

    def kok(self, kimlik: str) -> Kok:
        return next(k for k in self.kokler if k.kimlik == kimlik)


def kavramlari_yukle(secilenler: list[str], agac: Dugum, taniklar: list[Tanik]) -> list[Kavram]:
    dosyalar = sorted(SOZLUK_DIZIN.rglob("*.yaml"))
    if secilenler:
        dosyalar = [d for d in dosyalar if d.stem in secilenler]
        if bulunamayan := set(secilenler) - {d.stem for d in dosyalar}:
            sys.exit(f"Bulunamayan kavram dosyaları: {sorted(bulunamayan)}")
    gecerli_taniklar = {t.kod for t in taniklar if not t.turetilmis}
    kavramlar = []
    for d in dosyalar:
        with open(d, encoding="utf-8") as f:
            kv = Kavram(d, yaml.safe_load(f))
        if bilinmeyen := kv.bilinen_diller - agac.yaprak_kodlari:
            sys.exit(f"{d.name}: agac.yaml'da olmayan dil/ağız kodları: {sorted(bilinmeyen)}")
        if bilinmeyen := kv.bilinen_taniklar - gecerli_taniklar:
            sys.exit(f"{d.name}: tarihi.yaml'da olmayan tanık kodları: {sorted(bilinmeyen)}")
        kavramlar.append(kv)
    return kavramlar


# ============================================================== ölçüler

def yayilim(dugum, kok: Kok, kv: Kavram, h: Hedef) -> float | None:
    def deger(kod):
        if kod not in kv.bilinen_diller:
            return None
        return kok.bicimler.get(kod, ("", 0.0))[1]
    return ortalama(dugum, deger, h)


def anlasilirlik(dugum, kok: Kok, bicim: str, kv: Kavram, h: Hedef) -> float | None:
    """`bicim` duyulduğunda, ağırlıkça dillerin ne kadarı onu tanır?

    Bir dil bu kökü kullanıyorsa: tercih * (taban + (1 - taban) * ses_benzerliği).
    Kullanmıyorsa 0. Verisi yoksa hesaba katılmaz.
    """
    def deger(kod):
        if kod not in kv.bilinen_diller:
            return None
        if kod not in kok.bicimler:
            return 0.0
        f, tercih = kok.bicimler[kod]
        return tercih * (h.taban + (1 - h.taban) * benzerlik(bicim, f))
    return ortalama(dugum, deger, h)


def eskilik(dugum, kok: Kok, kv: Kavram, h: Hedef) -> float:
    pay = payda = 0.0
    for t in h.taniklar:
        if not (t.altinda(dugum) if h.tanik_kapsami == "alt" else t.ilgili(dugum)):
            continue
        bilinen, var = t.durum(kok, kv, h.taniklar)
        if bilinen:
            payda += t.agirlik
            pay += t.agirlik if var else 0.0
    return pay / payda if payda else 0.0


def en_eski_bicim(dugum, kok: Kok, h: Hedef, sadece_alt: bool = False) -> tuple[str, Tanik] | None:
    """Kronolojik olarak ilk tanığın biçimi. `sadece_alt`: yalnızca bu dala ya da
    altına bağlı tanıklar (ör. Oğuz için Eski Anadolu Türkçesi)."""
    for t in h.taniklar:
        if t.turetilmis or t.kod not in kok.tarihi:
            continue
        if (t.altinda(dugum) if sadece_alt else t.ilgili(dugum)):
            return kok.tarihi[t.kod], t
    return None


def bicim_destegi(dugum: Dugum, kok: Kok, h: Hedef) -> dict[str, float]:
    sayac: dict[str, float] = defaultdict(float)
    for dil, w in yaprak_agirliklari(dugum, h).items():
        if dil in kok.bicimler:
            f, tercih = kok.bicimler[dil]
            sayac[f] += w * tercih
    return sayac


def kapsama(dugum, kv: Kavram, h: Hedef) -> float:
    """Ağırlıkça dillerin ne kadarı için (yazı dili ya da en az bir ağız) veri var."""
    w = yaprak_agirliklari(dugum, h)
    return sum(sum(w[k] for k in d.yaprak_kodlari)
               for d in dugum.tum_dugumler() if d.dil_mi and d.yaprak_kodlari & kv.bilinen_diller)


# ================================================================ seçim

class Secim:
    def __init__(self, dugum, kok, bicim, miras, gunluk=None, puanlar=None, tanik=None):
        self.dugum: Dugum = dugum
        self.kok: Kok = kok
        self.bicim: str = bicim
        self.miras: bool = miras        # bu düğümde Türkçe aday yok -> üstten alındı
        self.gunluk: str | None = gunluk
        self.puanlar: dict = puanlar or {}
        self.tanik: Tanik | None = tanik  # biçim tarihî bir tanıktan alındıysa
        self.alt: list[Secim] = []


def _gunluk(dugum: Dugum, kv: Kavram) -> str | None:
    """Dilin/ağzın bugün en çok kullandığı biçim (alıntı olabilir)."""
    hedef = dugum.alt[0] if (dugum.dil_mi and dugum.alt) else dugum  # dil -> yazı dili
    if not hedef.yaprak_mi:
        return None
    adaylar = [(k.bicimler[hedef.kod][1], k.bicimler[hedef.kod][0])
               for k in kv.kokler if hedef.kod in k.bicimler]
    return max(adaylar)[1] if adaylar else None


def _olcu(dugum, k: Kok, kv: Kavram, h: Hedef) -> tuple[float, dict[str, float]]:
    """(kökün ölçü değeri, biçim -> değer)"""
    bicimler = {f for kod, (f, _) in k.bicimler.items() if kod in dugum.yaprak_kodlari}
    if h.olcu == "yayilim":
        y = yayilim(dugum, k, kv, h) or 0.0
        return y, {f: y for f in bicimler}
    anl = {f: anlasilirlik(dugum, k, f, kv, h) or 0.0 for f in bicimler}
    return max(anl.values()), anl


def sec(dugum: Dugum, kv: Kavram, h: Hedef, ust: Secim | None = None) -> Secim:
    adaylar: dict[str, tuple[float, dict[str, float]]] = {}
    for k in kv.kokler:
        if not k.secilebilir or not yayilim(dugum, k, kv, h):
            continue
        deger, bicimler = _olcu(dugum, k, kv, h)
        adaylar[k.kimlik] = (deger + h.beta * eskilik(dugum, k, kv, h), bicimler)

    gunluk = _gunluk(dugum, kv)
    if not adaylar:
        if ust is None:
            raise ValueError(f"{kv.yol.name}: Türkçe kökenli hiçbir aday yok")
        s = Secim(dugum, ust.kok, ust.bicim, True, gunluk, tanik=ust.tanik)
    else:
        puan = {k: v[0] for k, v in adaylar.items()}
        en_iyi = max(puan, key=lambda k: (puan[k], k))
        kok = kv.kok(en_iyi)
        tanik = None
        if h.bicim == "eski" and (eski := en_eski_bicim(dugum, kok, h, sadece_alt=True)):
            bicim, tanik = eski
        elif dugum.yaprak_mi:
            bicim = kok.bicimler[dugum.kod][0]
        elif h.bicim == "eski":
            destek = bicim_destegi(dugum, kok, h)
            bicim = max(destek, key=lambda f: (destek[f], f))
        else:
            eski = en_eski_bicim(dugum, kok, h)
            bp = {f: v + (h.beta * benzerlik(f, eski[0]) if eski else 0.0)
                  for f, v in adaylar[en_iyi][1].items()}
            bicim = max(bp, key=lambda f: (bp[f], f))
        s = Secim(dugum, kok, bicim, False, gunluk, puan, tanik)

    s.alt = [sec(c, kv, h, s) for c in dugum.alt]
    return s


# ================================================================ çıktı

def _gorunur(d: Dugum, agizlar: bool) -> bool:
    return agizlar or not d.dil_ici


def _kisa(t: Tanik) -> str:
    return t.ad.split(" (")[0]


def yazdir(s: Secim, derinlik: int, agizlar: bool, seviye: int = 0, ust: Secim | None = None):
    if derinlik >= 0 and seviye > derinlik:
        return
    etiket = "  " * seviye + s.dugum.ad
    satir = f"{etiket:<46} {s.bicim:<12}"
    notlar = []
    if ust is not None and s.kok is not ust.kok and not s.miras:
        notlar.append(f"farklı kök: {s.kok.kimlik}")
    if s.tanik is not None and not s.miras:
        notlar.append(f"tanık: {_kisa(s.tanik)}")
    if s.miras:
        notlar.append(f"canlandırma (günlük: {s.gunluk})" if s.gunluk else "üstten (veri yok)")
    elif s.gunluk and s.gunluk != s.bicim:
        notlar.append(f"günlük: {s.gunluk}")
    if notlar:
        satir += "  ← " + "; ".join(notlar)
    print(satir.rstrip())
    for c in s.alt:
        if _gorunur(c.dugum, agizlar):
            yazdir(c, derinlik, agizlar, seviye + 1, s)


def hedef_secimleri(kv: Kavram, agac: Dugum, hedefler: dict[str, Hedef]) -> dict[str, Secim]:
    return {kod: sec(agac, kv, h) for kod, h in hedefler.items()}


def uyum(secimler: dict[str, Secim]) -> str:
    kokler = {s.kok.kimlik for s in secimler.values()}
    return "UYUŞUYOR" if len(kokler) == 1 else "AYRIŞIYOR"


def kavram_raporu(kv: Kavram, agac: Dugum, hedefler: dict[str, Hedef], h: Hedef,
                  derinlik: int, agizlar: bool):
    durum = "doğrulandı" if kv.dogrulandi else "DOĞRULANMADI"
    print("=" * 80)
    print(f"{kv.ad}  ({kv.ingilizce})  [{durum}]   veri kapsaması: %{100 * kapsama(agac, kv, h):.0f}"
          f"   tarihî tanık: {len(kv.bilinen_taniklar)}/{sum(1 for t in h.taniklar if not t.turetilmis)}")
    secimler = hedef_secimleri(kv, agac, hedefler)
    ozet = "   ".join(f"{x.ad}: {s.bicim}" for x, s in ((hedefler[k], s) for k, s in secimler.items()))
    print(f"Üç hedef → {ozet}   [{uyum(secimler)}]")
    print("-" * 80)
    print(f"Hedef: {h.ad} — {h.soru}")
    secim = secimler[h.kod]

    olcu_adi = "anlaşılır" if h.olcu == "anlasilirlik" else "ölçü"
    print(f"\nAdaylar (en tepede):   puan = {'anlaşılırlık' if h.olcu == 'anlasilirlik' else 'yayılım'}"
          f" + {h.beta} × eskilik")
    print(f"  {'kök':<10} {'yayılım':>7} {olcu_adi:>9} {'eskilik':>7} {'puan':>6}   tarihî biçimler")
    for k in kv.kokler:
        y = yayilim(agac, k, kv, h) or 0.0
        e = eskilik(agac, k, kv, h)
        if k.secilebilir and k.kimlik in secim.puanlar:
            o = secim.puanlar[k.kimlik] - h.beta * e
            p = f"{secim.puanlar[k.kimlik]:6.2f}"
        else:
            o, p = 0.0, "     —"
        tarihi = ", ".join(f"{t}: {b}" for t, b in k.tarihi.items()) or "—"
        for t in h.taniklar:
            if t.turetilmis and t.durum(k, kv, h.taniklar)[1]:
                tarihi += f"  [{_kisa(t)} ✓]"
        if k.ana_turkce and h.bicim == "eski":
            tarihi += f"  (bilimsel kuruluş: {k.ana_turkce})"
        uygun = "" if k.secilebilir else f"  (seçilemez: köken={k.koken})"
        print(f"  {k.kimlik:<10} {y:7.2f} {o:9.2f} {e:7.2f} {p}   {tarihi}{uygun}")

    print(f"\nSeçim: {secim.bicim}  (kök: {secim.kok.kimlik})")
    y = yayilim(agac, secim.kok, kv, h) or 0.0
    if h.esik is not None and y < h.esik:
        print(f"  ⚠ CANLANDIRMA: bu kök bugün dillerin ağırlıkça yalnızca %{100 * y:.0f}'inde yaşıyor; "
              f"öğretilmesi gerekecek.")

    if h.olcu == "anlasilirlik":
        print("\nAna kollarda anlaşılırlık (en tepedeki seçim duyulduğunda):")
        kollar = [d for d in agac.tum_dugumler() if d.tip == "kol"]
        degerler = {d.ad: anlasilirlik(d, secim.kok, secim.bicim, kv, h) for d in kollar}
        bilinen = {ad: v for ad, v in degerler.items() if v is not None}
        en_dusuk = min(bilinen, key=bilinen.get) if bilinen else None
        for ad, v in degerler.items():
            isaret = "   ← en az anlayan" if ad == en_dusuk else ""
            print(f"  {ad:<14} {'veri yok' if v is None else f'%{100 * v:.0f}'}{isaret}")
        genel = anlasilirlik(agac, secim.kok, secim.bicim, kv, h)
        print(f"  {'Genel':<14} %{100 * (genel or 0):.0f}")

    print()
    yazdir(secim, derinlik, agizlar)
    print()


def karsilastirma_raporu(kavramlar: list[Kavram], agac: Dugum, hedefler: dict[str, Hedef], md: bool):
    sutunlar = list(hedefler.values())
    satirlar = []
    for kv in kavramlar:
        s = hedef_secimleri(kv, agac, hedefler)
        satirlar.append((kv, [s[h.kod] for h in sutunlar], uyum(s)))
    if md:
        print("# Hedeflerin karşılaştırması\n")
        print("> Bu dosya `python3 araclar/puanla.py --karsilastir --md > KARSILASTIRMA.md` komutuyla "
              "üretilir; elle düzenlemeyin.\n")
        print("Üç hedef aynı kökü seçiyorsa **UYUŞUYOR**, farklı kök seçiyorsa **AYRIŞIYOR**. "
              "Ayrışan kavramlar tartışmaya açıktır. Hücrelerde biçim ve *(kök)* yazılıdır.\n")
        ayrisan = sum(1 for _, _, u in satirlar if u == "AYRIŞIYOR")
        print(f"Toplam {len(satirlar)} kavram, {ayrisan} tanesi ayrışıyor.\n")
        print("| Kavram | " + " | ".join(h.ad for h in sutunlar) + " | Durum |")
        print("|---|" + "---|" * len(sutunlar) + "---|")
        for kv, ss, u in satirlar:
            hucre = [f"{x.bicim} *({x.kok.kimlik})*" for x in ss]
            print(f"| {kv.ad} | " + " | ".join(hucre) + f" | {u} |")
        return
    print(f"{'Kavram':<12}" + "".join(f"{h.ad:<26}" for h in sutunlar) + "Durum")
    for kv, ss, u in satirlar:
        print(f"{kv.ad:<12}" + "".join(f"{x.bicim + ' (' + x.kok.kimlik + ')':<26}" for x in ss) + u)


def agirlik_raporu(agac: Dugum, h: Hedef, agizlar: bool, md: bool):
    w = yaprak_agirliklari(agac, h)

    def genel_pay(d: Dugum) -> float:
        return sum(w[k] for k in d.yaprak_kodlari)

    satirlar = []

    def gez(d: Dugum, seviye: int, ic_pay: float):
        if not _gorunur(d, agizlar):
            return
        agiz = d.yaprak_sayisi if (d.dil_mi and d.alt) else 0
        satirlar.append((seviye, d, ic_pay, genel_pay(d), agiz))
        for c in d.alt:
            gez(c, seviye + 1, genel_pay(c) / genel_pay(d) if genel_pay(d) else 0.0)

    gez(agac, 0, 1.0)
    diller = [d for d in agac.tum_dugumler() if d.dil_mi]
    dil_agirlik = {d.kod: genel_pay(d) for d in diller}
    en_agir = max(diller, key=lambda d: dil_agirlik[d.kod])
    en_hafif = min(diller, key=lambda d: dil_agirlik[d.kod])
    agiz_sayisi = sum(1 for d in agac.tum_dugumler() if d.dil_ici and d.yaprak_mi and not d.yazi_dili)
    ozet = (f"Dil sayısı: {len(diller)}   ağız sayısı: {agiz_sayisi}   "
            f"en ağır dil: {en_agir.ad} %{100 * dil_agirlik[en_agir.kod]:.1f}   "
            f"en hafif dil: {en_hafif.ad} %{100 * dil_agirlik[en_hafif.kod]:.2f}   "
            f"(her dil eşit olsaydı: %{100 / len(diller):.1f})")
    kural = {"basamak": ("basamak (her dil kendi basamağıyla)" if h.alfa == 1
                         else f"(ortalama basamak) × (dil sayısı ^ {h.alfa})"),
             "soy": "her ayrılıkta dallar eşit",
             "nufus": "doğrudan konuşur sayısı"}[h.agirlik]

    if md:
        print(f"## {h.ad}\n")
        print(f"*{h.soru}* Ağırlık: {kural}"
              + ("; Ortak Türkçe düğümü şeffaf." if h.seffaf else "; ağaç olduğu gibi.") + "\n")
        print(f"{ozet}\n")
        print("| Düğüm | Konuşur (yaklaşık) | Basamak | Üst içinde | Genel |")
        print("|---|---:|---:|---:|---:|")
        for seviye, d, ic, genel, agiz in satirlar:
            ad = f"**{d.ad}**" if (d.tip == "kol" or seviye == 0) else d.ad
            if d.dil_mi:
                ad = f"{d.ad} *({agiz} ağız)*" if agiz else d.ad
            girinti = "&nbsp;&nbsp;&nbsp;&nbsp;" * seviye
            dil = d.dil_mi and not d.yazi_dili
            konusur = f"{d.konusur:,}".replace(",", ".") if dil else ""
            bas = str(d.basamak) if dil else ""
            print(f"| {girinti}{ad} | {konusur} | {bas} | %{100 * ic:.1f} | %{100 * genel:.2f} |")
        print()
        return

    print(f"Ağırlıklar — {h.ad} ({kural})      üst içinde    genel\n")
    for seviye, d, ic, genel, agiz in satirlar:
        etiket = "  " * seviye + d.ad + (f" ({agiz} ağız)" if agiz and not agizlar else "")
        if d.dil_mi and not d.yazi_dili:
            etiket += f" [b{d.basamak}]"
        print(f"{etiket:<58} %{100 * ic:5.1f}   %{100 * genel:5.2f}")
    print(f"\n{ozet}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("kavramlar", nargs="*", help="kavram dosya adları (uzantısız)")
    ap.add_argument("--hedef", help="ortak | ana | nufus (varsayılan: asıl hedef)")
    for ad in ("alfa", "beta", "taban", "esik"):
        ap.add_argument(f"--{ad}", type=float, help=f"seçili hedefin {ad} değerini değiştir")
    ap.add_argument("--derinlik", type=int, default=-1, help="gösterilecek en derin seviye (-1: tümü)")
    ap.add_argument("--agizlar", action="store_true", help="dillerin altındaki ağızları da göster")
    ap.add_argument("--agirliklar", action="store_true", help="ağırlık tablosunu göster ve çık")
    ap.add_argument("--karsilastir", action="store_true", help="üç hedefin seçimlerini yan yana göster")
    ap.add_argument("--md", action="store_true", help="tabloları Markdown olarak yaz")
    args = ap.parse_args()

    agac = agac_yukle()
    taniklar = taniklari_yukle(agac)
    hedefler = hedefleri_yukle(taniklar)
    if args.hedef and args.hedef not in hedefler:
        sys.exit(f"Bilinmeyen hedef '{args.hedef}'. Seçenekler: {', '.join(hedefler)}")
    h = hedefler[args.hedef] if args.hedef else next(x for x in hedefler.values() if x.asil)
    for ad in ("alfa", "beta", "taban", "esik"):
        if getattr(args, ad) is not None:
            setattr(h, ad, getattr(args, ad))

    if args.agirliklar:
        if args.md and not args.hedef:
            print("# Ağırlıklar\n")
            print("> Bu dosya `python3 araclar/puanla.py --agirliklar --agizlar --md > AGIRLIKLAR.md` "
                  "komutuyla üretilir; elle düzenlemeyin. Üç hedefin her biri kendi ağırlığını kullanır "
                  "(bkz. `hedefler.yaml`, ILKELER.md §1).\n")
            print("- **Basamak:** dilin büyüklük basamağı (konuşur sayısının 10'luk basamağı, 2–8).")
            print("- **Üst içinde:** düğümün, bir üstündeki birleşimde aldığı pay.")
            print("- **Genel:** düğümün en tepedeki karara toplam etkisi.\n")
            for x in hedefler.values():
                agirlik_raporu(agac, x, args.agizlar, True)
        else:
            agirlik_raporu(agac, h, args.agizlar, args.md)
        return
    kavramlar = kavramlari_yukle(args.kavramlar, agac, taniklar)
    if args.karsilastir:
        karsilastirma_raporu(kavramlar, agac, hedefler, args.md)
        return
    for kv in kavramlar:
        kavram_raporu(kv, agac, hedefler, h, args.derinlik, args.agizlar)


if __name__ == "__main__":
    main()
