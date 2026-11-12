#!/usr/bin/env python3
"""Ortak Türk dili — kelime puanlama ve ağaç üzerinde seçim.

Kullanım:
    python3 araclar/puanla.py                     # tüm kavramlar
    python3 araclar/puanla.py tas dag             # sadece belirtilen kavram dosyaları
    python3 araclar/puanla.py --derinlik 2        # ağacı 2. seviyeye kadar göster
    python3 araclar/puanla.py --agizlar           # dillerin altındaki ağızları da göster
    python3 araclar/puanla.py --agirliklar        # ağırlık tablosu
    python3 araclar/puanla.py --agirliklar --md   # ağırlık tablosu (Markdown)

Yöntem ILKELER.md'de. Kısaca, hesap ALTTAN YUKARI yapılır:
  * Ağızlar birleşerek dili, diller birleşerek dalı, dallar birleşerek kolu,
    kollar birleşerek en tepeyi oluşturur. Her birleşimde çocuklar
    (sayım ** alfa) oranında tartılır. Sayım, dil düzeyinin üstünde DİL sayısı,
    bir dilin içinde AĞIZ sayısıdır.
  * yayılım      : kök, ağırlıkça dillerin ne kadarında yaşıyor (0..1)
  * anlaşılırlık : önerilen biçim, ağırlıkça dillerde ne kadar tanıdık (0..1)
  * eskilik      : kökü kaydeden tarihî tanıkların ağırlıklı oranı (0..1)
  * kök puanı    = anlaşılırlık (en iyi biçimiyle) + beta * eskilik
  * biçim puanı  = anlaşılırlık + beta * (en eski tanık biçimine yakınlık)
  * Sadece kökeni "türkçe" olan kökler aday olabilir.
  * Her düğüm SADECE kendi altına bakarak en iyi kökü ve biçimi seçer. Üstten
    gelen tek şey, verisi olmayan ya da Türkçe kökü kaybetmiş düğümlere önerilen
    kelimedir (canlandırma).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML gerekli:  pip install -r requirements.txt")

KOK_DIZIN = Path(__file__).resolve().parent.parent
AGAC_DOSYASI = KOK_DIZIN / "agac.yaml"
TARIHI_DOSYASI = KOK_DIZIN / "tarihi.yaml"
SOZLUK_DIZIN = KOK_DIZIN / "sozluk"

VARSAYILAN = dict(alfa=0.5, beta=0.2, taban=0.5, esik=0.5)


# ================================================================== ağaç

DUGUM_ALANLARI = {"ad", "kod", "tip", "not", "alt", "agirlik_carpani", "konusur", "konusur_not"}
EN_AZ_BASAMAK, EN_COK_BASAMAK = 2, 8

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
        self.basamak_toplam = (self.basamak if self.dil_mi and not yazi_dili
                               else sum(c.basamak_toplam for c in self.alt if not c.dil_ici))
        self.yaprak_kodlari = ({self.kod} if not self.alt
                               else set().union(*(c.yaprak_kodlari for c in self.alt)))

    @property
    def yaprak_mi(self) -> bool:
        return not self.alt

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


def basamak(konusur: int) -> int:
    """Büyüklük basamağı: konuşur sayısı her 10 kat arttığında +1 (2..8).

    100'den az: 2 · 100-1000: 3 · 1-10 bin: 4 · 10-100 bin: 5 · 100 bin-1 milyon: 6
    1-10 milyon: 7 · 10 milyon ve üstü: 8
    """
    b = len(str(max(int(konusur), 1)))  # basamak sayısı = floor(log10) + 1
    return max(EN_AZ_BASAMAK, min(EN_COK_BASAMAK, b))


def cocuk_agirligi(c: Dugum, alfa: float) -> float:
    """Bir çocuğun kardeşleri arasındaki (normalleştirilmemiş) ağırlığı.

    Bir dilin içinde (ağızlar):   (ağız sayısı) ^ alfa
    Dil düzeyinde ve üstünde:     (ortalama basamak) x (dil sayısı) ^ alfa
    """
    if c.dil_ici:
        return (c.yaprak_sayisi ** alfa) * c.carpan
    return (c.basamak_toplam / c.dil_sayisi) * (c.dil_sayisi ** alfa) * c.carpan


def paylar(dugum: Dugum, alfa: float) -> list[tuple[Dugum, float]]:
    """Çocukların düğüm içindeki payları (toplamı 1)."""
    toplam = sum(cocuk_agirligi(c, alfa) for c in dugum.alt)
    return [(c, cocuk_agirligi(c, alfa) / toplam) for c in dugum.alt]


def yaprak_agirliklari(dugum: Dugum, alfa: float) -> dict[str, float]:
    if dugum.yaprak_mi:
        return {dugum.kod: 1.0}
    sonuc: dict[str, float] = {}
    for c, pay in paylar(dugum, alfa):
        for kod, w in yaprak_agirliklari(c, alfa).items():
            sonuc[kod] = pay * w
    return sonuc


def ortalama(dugum: Dugum, deger, alfa: float) -> float | None:
    """Alttan yukarı ağırlıklı ortalama. deger(yaprak_kodu) -> sayı ya da None (veri yok)."""
    if dugum.yaprak_mi:
        return deger(dugum.kod)
    pay = payda = 0.0
    for c in dugum.alt:
        s = ortalama(c, deger, alfa)
        if s is None:
            continue
        w = cocuk_agirligi(c, alfa)
        pay += w * s
        payda += w
    return pay / payda if payda else None


# ======================================================= tarihî tanıklar

class Tanik:
    def __init__(self, veri: dict, dal: Dugum):
        self.ad: str = veri["ad"]
        self.kod: str = veri["kod"]
        self.dal = dal
        self.agirlik = float(veri.get("agirlik", 1.0))
        self.sira = int(veri.get("sira", 99))

    def ilgili(self, dugum: Dugum) -> bool:
        """Bu tanık, `dugum`de verilen kararda sayılır mı?"""
        return self.dal is dugum or self.dal in dugum.ustler() or dugum in self.dal.ustler()


def taniklari_yukle(agac: Dugum) -> list[Tanik]:
    dugumler = {d.kod: d for d in agac.tum_dugumler() if not d.yazi_dili}
    with open(TARIHI_DOSYASI, encoding="utf-8") as f:
        veri = yaml.safe_load(f) or []
    taniklar = []
    for t in veri:
        if t["dal"] not in dugumler:
            sys.exit(f"tarihi.yaml: '{t['kod']}' için bilinmeyen dal '{t['dal']}'")
        taniklar.append(Tanik(t, dugumler[t["dal"]]))
    return sorted(taniklar, key=lambda t: t.sira)


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
    return s.lower().replace("'", "").replace("ʼ", "").replace("’", "")


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
    gecerli_taniklar = {t.kod for t in taniklar}
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

class Ayar:
    def __init__(self, taniklar, **kw):
        self.taniklar = taniklar
        for k, v in VARSAYILAN.items():
            setattr(self, k, kw.get(k, v))


def yayilim(dugum, kok: Kok, kv: Kavram, a: Ayar) -> float | None:
    def deger(kod):
        if kod not in kv.bilinen_diller:
            return None
        return kok.bicimler.get(kod, ("", 0.0))[1]
    return ortalama(dugum, deger, a.alfa)


def anlasilirlik(dugum, kok: Kok, bicim: str, kv: Kavram, a: Ayar) -> float | None:
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
        return tercih * (a.taban + (1 - a.taban) * benzerlik(bicim, f))
    return ortalama(dugum, deger, a.alfa)


def eskilik(dugum, kok: Kok, kv: Kavram, a: Ayar) -> float:
    pay = payda = 0.0
    for t in a.taniklar:
        if t.kod in kv.bilinen_taniklar and t.ilgili(dugum):
            payda += t.agirlik
            pay += t.agirlik if t.kod in kok.tarihi else 0.0
    return pay / payda if payda else 0.0


def en_eski_bicim(dugum, kok: Kok, a: Ayar) -> str | None:
    for t in a.taniklar:  # kronolojik sırada
        if t.ilgili(dugum) and t.kod in kok.tarihi:
            return kok.tarihi[t.kod]
    return None


def kapsama(dugum, kv: Kavram, a: Ayar) -> float:
    """Ağırlıkça dillerin ne kadarı için (yazı dili ya da en az bir ağız) veri var."""
    w = yaprak_agirliklari(dugum, a.alfa)
    return sum(sum(w[k] for k in d.yaprak_kodlari)
               for d in dugum.tum_dugumler() if d.dil_mi and d.yaprak_kodlari & kv.bilinen_diller)


# ================================================================ seçim

class Secim:
    def __init__(self, dugum, kok, bicim, miras, gunluk=None, puanlar=None):
        self.dugum: Dugum = dugum
        self.kok: Kok = kok
        self.bicim: str = bicim
        self.miras: bool = miras        # bu düğümde Türkçe aday yok -> üstten alındı
        self.gunluk: str | None = gunluk
        self.puanlar: dict = puanlar or {}
        self.alt: list[Secim] = []


def _gunluk(dugum: Dugum, kv: Kavram) -> str | None:
    """Dilin/ağzın bugün en çok kullandığı biçim (alıntı olabilir)."""
    hedef = dugum.alt[0] if (dugum.dil_mi and dugum.alt) else dugum  # dil -> yazı dili
    if not hedef.yaprak_mi:
        return None
    adaylar = [(k.bicimler[hedef.kod][1], k.bicimler[hedef.kod][0])
               for k in kv.kokler if hedef.kod in k.bicimler]
    return max(adaylar)[1] if adaylar else None


def sec(dugum: Dugum, kv: Kavram, a: Ayar, ust: Secim | None = None) -> Secim:
    adaylar: dict[str, tuple[float, dict[str, float]]] = {}
    for k in kv.kokler:
        if not k.secilebilir or not yayilim(dugum, k, kv, a):
            continue
        bicimler = {f for kod, (f, _) in k.bicimler.items() if kod in dugum.yaprak_kodlari}
        anl = {f: anlasilirlik(dugum, k, f, kv, a) or 0.0 for f in bicimler}
        adaylar[k.kimlik] = (max(anl.values()) + a.beta * eskilik(dugum, k, kv, a), anl)

    gunluk = _gunluk(dugum, kv)
    if not adaylar:
        if ust is None:
            raise ValueError(f"{kv.yol.name}: Türkçe kökenli hiçbir aday yok")
        s = Secim(dugum, ust.kok, ust.bicim, True, gunluk)
    else:
        puan = {k: v[0] for k, v in adaylar.items()}
        en_iyi = max(puan, key=lambda k: (puan[k], k))
        kok = kv.kok(en_iyi)
        if dugum.yaprak_mi:
            bicim = kok.bicimler[dugum.kod][0]
        else:
            eski = en_eski_bicim(dugum, kok, a)
            bp = {f: v + (a.beta * benzerlik(f, eski) if eski else 0.0)
                  for f, v in adaylar[en_iyi][1].items()}
            bicim = max(bp, key=lambda f: (bp[f], f))
        s = Secim(dugum, kok, bicim, False, gunluk, puan)

    s.alt = [sec(c, kv, a, s) for c in dugum.alt]
    return s


# ================================================================ çıktı

def _gorunur(d: Dugum, agizlar: bool) -> bool:
    return agizlar or not d.dil_ici


def yazdir(s: Secim, derinlik: int, agizlar: bool, seviye: int = 0, ust: Secim | None = None):
    if derinlik >= 0 and seviye > derinlik:
        return
    etiket = "  " * seviye + s.dugum.ad
    satir = f"{etiket:<46} {s.bicim:<12}"
    notlar = []
    if ust is not None and s.kok is not ust.kok and not s.miras:
        notlar.append(f"farklı kök: {s.kok.kimlik}")
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


def kavram_raporu(kv: Kavram, agac: Dugum, a: Ayar, derinlik: int, agizlar: bool):
    durum = "doğrulandı" if kv.dogrulandi else "DOĞRULANMADI"
    print("=" * 80)
    print(f"{kv.ad}  ({kv.ingilizce})  [{durum}]   veri kapsaması: %{100 * kapsama(agac, kv, a):.0f}"
          f"   tarihî tanık: {len(kv.bilinen_taniklar)}/{len(a.taniklar)}")
    print("-" * 80)
    secim = sec(agac, kv, a)

    print("Adaylar (en tepede):")
    print(f"  {'kök':<10} {'yayılım':>7} {'anlaşılır':>9} {'eskilik':>7} {'puan':>6}   tarihî biçimler")
    for k in kv.kokler:
        y = yayilim(agac, k, kv, a) or 0.0
        e = eskilik(agac, k, kv, a)
        if k.secilebilir and k.kimlik in secim.puanlar:
            anl = secim.puanlar[k.kimlik] - a.beta * e
            p = f"{secim.puanlar[k.kimlik]:6.2f}"
        else:
            anl, p = 0.0, "     —"
        tarihi = ", ".join(f"{t}: {b}" for t, b in k.tarihi.items()) or "—"
        uygun = "" if k.secilebilir else f"  (seçilemez: köken={k.koken})"
        print(f"  {k.kimlik:<10} {y:7.2f} {anl:9.2f} {e:7.2f} {p}   {tarihi}{uygun}")

    y = yayilim(agac, secim.kok, kv, a) or 0.0
    print(f"\nSeçim: {secim.bicim}  (kök: {secim.kok.kimlik})")
    if y < a.esik:
        print(f"  ⚠ CANLANDIRMA: bu kök bugün dillerin ağırlıkça yalnızca %{100 * y:.0f}'inde yaşıyor; "
              f"öğretilmesi gerekecek.")

    print("\nAna kollarda anlaşılırlık (en tepedeki seçim duyulduğunda):")
    kollar = [d for d in agac.tum_dugumler() if d.tip == "kol"]
    degerler = {d.ad: anlasilirlik(d, secim.kok, secim.bicim, kv, a) for d in kollar}
    bilinen = {ad: v for ad, v in degerler.items() if v is not None}
    en_dusuk = min(bilinen, key=bilinen.get) if bilinen else None
    for ad, v in degerler.items():
        isaret = "   ← en az anlayan" if ad == en_dusuk else ""
        print(f"  {ad:<14} {'veri yok' if v is None else f'%{100 * v:.0f}'}{isaret}")
    genel = anlasilirlik(agac, secim.kok, secim.bicim, kv, a)
    print(f"  {'Genel':<14} %{100 * (genel or 0):.0f}")

    print()
    yazdir(secim, derinlik, agizlar)
    print()


def agirlik_raporu(agac: Dugum, alfa: float, agizlar: bool, md: bool):
    w = yaprak_agirliklari(agac, alfa)

    satirlar = []  # (seviye, ad, üst içindeki pay, genel pay, dil sayısı, ağız sayısı)

    def gez(d: Dugum, seviye: int, ic_pay: float, genel: float):
        if not _gorunur(d, agizlar):
            return
        agiz = d.yaprak_sayisi if (d.dil_mi and d.alt) else 0
        satirlar.append((seviye, d, ic_pay, genel, agiz))
        for c, pay in (paylar(d, alfa) if d.alt else []):
            gez(c, seviye + 1, pay, genel * pay)

    gez(agac, 0, 1.0, 1.0)
    diller = [d for d in agac.tum_dugumler() if d.dil_mi]
    dil_agirlik = {d.kod: sum(w[k] for k in d.yaprak_kodlari) for d in diller}
    en_agir = max(diller, key=lambda d: dil_agirlik[d.kod])
    en_hafif = min(diller, key=lambda d: dil_agirlik[d.kod])
    agiz_sayisi = sum(1 for d in agac.tum_dugumler() if d.dil_ici and d.yaprak_mi and not d.yazi_dili)
    ozet = (f"Dil sayısı: {len(diller)}   ağız sayısı: {agiz_sayisi}   "
            f"en ağır dil: {en_agir.ad} %{100 * dil_agirlik[en_agir.kod]:.1f}   "
            f"en hafif dil: {en_hafif.ad} %{100 * dil_agirlik[en_hafif.kod]:.1f}   "
            f"(her dil eşit olsaydı: %{100 / len(diller):.1f})")

    if md:
        print("# Ağırlıklar\n")
        print("> Bu dosya `python3 araclar/puanla.py --agirliklar --agizlar --md > AGIRLIKLAR.md` "
              "komutuyla üretilir; elle düzenlemeyin.\n")
        print(f"α = {alfa}. {ozet}\n")
        print("- **Üst içinde:** düğümün, bir üstündeki birleşimde aldığı pay.")
        print("- **Genel:** düğümün en tepedeki karara toplam etkisi.\n")
        print("- **Basamak:** dilin büyüklük basamağı (konuşur sayısının 10'luk basamağı, 2–8).\n")
        print("| Düğüm | Konuşur (yaklaşık) | Basamak | Üst içinde | Genel |")
        print("|---|---:|---:|---:|---:|")
        for seviye, d, ic, genel, agiz in satirlar:
            ad = d.ad if not (d.tip in ("kol",) or seviye <= 1) else f"**{d.ad}**"
            if d.dil_mi:
                ad = f"{d.ad} *({agiz} ağız)*" if agiz else d.ad
            girinti = "&nbsp;&nbsp;&nbsp;&nbsp;" * seviye
            dil = d.dil_mi and not d.yazi_dili
            konusur = f"{d.konusur:,}".replace(",", ".") if dil else ""
            bas = str(d.basamak) if dil else ""
            print(f"| {girinti}{ad} | {konusur} | {bas} | %{100 * ic:.1f} | %{100 * genel:.2f} |")
        return

    print(f"Ağırlıklar (alfa = {alfa})      üst içinde    genel\n")
    for seviye, d, ic, genel, agiz in satirlar:
        etiket = "  " * seviye + d.ad + (f" ({agiz} ağız)" if agiz and not agizlar else "")
        if d.dil_mi and not d.yazi_dili:
            etiket += f" [b{d.basamak}]"
        print(f"{etiket:<58} %{100 * ic:5.1f}   %{100 * genel:5.2f}")
    print(f"\n{ozet}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("kavramlar", nargs="*", help="kavram dosya adları (uzantısız)")
    for ad, deger in VARSAYILAN.items():
        ap.add_argument(f"--{ad}", type=float, default=deger)
    ap.add_argument("--derinlik", type=int, default=-1, help="gösterilecek en derin seviye (-1: tümü)")
    ap.add_argument("--agizlar", action="store_true", help="dillerin altındaki ağızları da göster")
    ap.add_argument("--agirliklar", action="store_true", help="ağırlık tablosunu göster ve çık")
    ap.add_argument("--md", action="store_true", help="ağırlık tablosunu Markdown olarak yaz")
    args = ap.parse_args()

    agac = agac_yukle()
    if args.agirliklar:
        agirlik_raporu(agac, args.alfa, args.agizlar, args.md)
        return
    taniklar = taniklari_yukle(agac)
    ayar = Ayar(taniklar, **{k: getattr(args, k) for k in VARSAYILAN})
    for kv in kavramlari_yukle(args.kavramlar, agac, taniklar):
        kavram_raporu(kv, agac, ayar, args.derinlik, args.agizlar)


if __name__ == "__main__":
    main()
