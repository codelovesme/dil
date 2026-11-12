#!/usr/bin/env python3
"""Ortak Türk dili — kelime puanlama ve seçim (üç hedef).

Kullanım:
    python3 araclar/puanla.py                     # tüm kavramlar, asıl hedef (ortak dil)
    python3 araclar/puanla.py tas dag             # sadece belirtilen kavram dosyaları
    python3 araclar/puanla.py --hedef ana         # başka bir hedef: ortak | ana | nufus
    python3 araclar/puanla.py --karsilastir       # üç hedefin seçimlerini yan yana göster
    python3 araclar/puanla.py --derinlik 2        # ağacı 2. seviyeye kadar göster
    python3 araclar/puanla.py --agizlar           # dillerin altındaki ağızları da göster
    python3 araclar/puanla.py --agirliklar        # dil ağırlıkları (seçili hedef)
    python3 araclar/puanla.py --agirliklar --md   # ağırlık tabloları (Markdown)

Veri: agac.yaml (soy ağacı, diller, ağızlar, konuşur sayıları), ag.yaml (örgü:
anlaşılırlık ve temas bağları), tarihi.yaml (tarihî tanıklar), hedefler.yaml,
sozluk/ (kavramlar). Yöntem ILKELER.md'de. Üç ölçü:

  * Hedef 1 — yaygınlık puanı: kelimeyi ne kadar çok FARKLI grup kullanıyor? Gruplar
    etiketle değil örgüdeki benzerlikle belirlenir: her dil
    kendine özgülük × basamak / 8 ile tartılır. Birbirinin aynısı diller bir
    grubun payını paylaşır, ayrışmış bir dil kendi başına bir gruptur. Seçilen biçimin ortalama anlaşılırlığı,
    büyük topluluklardan biri geride kalırsa ceza ile azaltılır.
  * Hedef 2 — kök yaşı: kök soy ağacının hangi düğümüne kadar geri gidiyor?
    Bir düğümün en az iki kolunda (ya da bir kolunda ve o düğümün tarihî
    tanığında) bulunan kök, o düğümün dilinde de vardı. Türk dilleri arası
    ödünçler ayıklanır.
  * Hedef 3 — anlayan kişi: her dil konuşur sayısıyla tartılır; ikinci dil
    yoluyla anlama örgüden eklenir.

Sadece kökeni "türkçe" olan kökler aday olabilir. Her düğüm sadece kendi
altına bakarak seçer; verisi olmayan ya da Türkçe kökü kaybetmiş düğümlere
üstün kelimesi önerilir (canlandırma).
"""

from __future__ import annotations

import argparse
import math
import sys
from collections import Counter
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML gerekli:  pip install -r requirements.txt")

KOK_DIZIN = Path(__file__).resolve().parent.parent
AGAC_DOSYASI = KOK_DIZIN / "agac.yaml"
AG_DOSYASI = KOK_DIZIN / "ag.yaml"
TARIHI_DOSYASI = KOK_DIZIN / "tarihi.yaml"
HEDEF_DOSYASI = KOK_DIZIN / "hedefler.yaml"
SOZLUK_DIZIN = KOK_DIZIN / "sozluk"


# ============================================================== soy ağacı

DUGUM_ALANLARI = {"ad", "kod", "tip", "not", "alt", "agirlik_carpani", "konusur", "konusur_not"}
EN_AZ_BASAMAK, EN_COK_BASAMAK = 2, 8


def basamak(konusur: int) -> int:
    """Büyüklük basamağı: konuşur sayısı her 10 kat arttığında +1 (2..8). Bilgi amaçlı."""
    b = len(str(max(int(konusur), 1)))
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
        self.ust = ust
        self.dil_ici = dil_ici          # bir dilin altında (ağız) mı?
        self.yazi_dili = yazi_dili      # otomatik eklenen "Yazı dili" yaprağı mı?
        alt_veri = veri.get("alt", [])
        self.dil_mi = self.tip == "dil" or (not alt_veri and not dil_ici)
        self.alt = [Dugum(c, self, dil_ici or self.dil_mi) for c in alt_veri]
        if self.dil_mi and self.alt:
            self.alt.insert(0, Dugum({"ad": "Yazı dili", "kod": self.kod}, self, True, True))
        self.yaprak_sayisi = 1 if not self.alt else sum(c.yaprak_sayisi for c in self.alt)
        if self.dil_mi:
            if "konusur" not in veri:
                sys.exit(f"agac.yaml: '{self.ad}' dilinin `konusur` (konuşur sayısı) alanı eksik")
            self.konusur = int(veri["konusur"])
            self.basamak = basamak(self.konusur)
        self.diller: list[Dugum] = [self] if self.dil_mi else [d for c in self.alt for d in c.diller]
        self.yaprak_kodlari = ({self.kod} if not self.alt
                               else set().union(*(c.yaprak_kodlari for c in self.alt)))
        self.kol: Dugum | None = None   # agac_yukle doldurur

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
    for d in kok.tum_dugumler():
        d.kol = d if d.tip == "kol" else next((u for u in d.ustler() if u.tip == "kol"), None)
    return kok


# ================================================================== örgü

class Ag:
    """Diller arası ağırlıklı bağlar (ag.yaml)."""

    def __init__(self, agac: Dugum):
        with open(AG_DOSYASI, encoding="utf-8") as f:
            veri = yaml.safe_load(f) or {}
        self.diller = {d.kod: d for d in agac.diller}
        self.anla: dict[tuple[str, str], float] = {}     # dilbilimsel
        self.ikinci: dict[tuple[str, str], float] = {}   # ikinci dil (dinleyen, konusan)
        self.temas: dict[tuple[str, str], float] = {}
        for satir in veri.get("anlasilirlik") or []:
            a, b, ab = satir[0], satir[1], float(satir[2])
            ba = float(satir[3]) if len(satir) > 3 else ab
            self._denetle(a, b)
            self.anla[(a, b)], self.anla[(b, a)] = ab, ba
        for dinleyen, konusan, deger in veri.get("ikinci_dil") or []:
            self._denetle(dinleyen, konusan)
            self.ikinci[(dinleyen, konusan)] = float(deger)
        for veren, alan, deger in veri.get("temas") or []:
            self._denetle(veren, alan)
            self.temas[(veren, alan)] = float(deger)

    def _denetle(self, *kodlar):
        for k in kodlar:
            if k not in self.diller:
                sys.exit(f"ag.yaml: bilinmeyen dil kodu '{k}' (ağız değil, dil kodu olmalı)")

    def anlar(self, dinleyen: str, konusan: str) -> float:
        return 1.0 if dinleyen == konusan else self.anla.get((dinleyen, konusan), 0.0)

    def komsular(self, kod: str, ikinci_dil: bool = False):
        """(komşu, anlama düzeyi). ikinci_dil: ikinci dil bilgisini de kat (en yükseği)."""
        sonuc: dict[str, float] = {}
        for (a, b), s in self.anla.items():
            if a == kod:
                sonuc[b] = s
        if ikinci_dil:
            for (a, b), s in self.ikinci.items():
                if a == kod:
                    sonuc[b] = max(s, sonuc.get(b, 0.0))
        yield from sonuc.items()

    def verenler(self, alan: str):
        for (v, a), d in self.temas.items():
            if a == alan:
                yield v, d


# ======================================================= tarihî tanıklar

class Tanik:
    def __init__(self, veri: dict, dal: Dugum):
        self.ad: str = veri["ad"]
        self.kod: str = veri["kod"]
        self.dal = dal
        self.agirlik = float(veri.get("agirlik", 1.0))
        self.sira = int(veri.get("sira", 99))

    def ilgili(self, dugum: Dugum) -> bool:
        """Kendi, üst ya da alt dalına bağlı mı?"""
        return self.dal is dugum or self.dal in dugum.ustler() or dugum in self.dal.ustler()

    def altinda(self, dugum: Dugum) -> bool:
        """Bu düğüme ya da altındaki bir dala mı bağlı?"""
        return self.dal is dugum or dugum in self.dal.ustler()

    @property
    def kisa(self) -> str:
        return self.ad.split(" (")[0]


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


# ============================================================== hedefler

YONTEMLER = {"kopru", "yas", "kisi"}


class Hedef:
    def __init__(self, veri: dict, taniklar: list[Tanik], agac: Dugum, ag: Ag):
        self.kod: str = veri["kod"]
        self.ad: str = veri["ad"]
        self.soru: str = veri.get("soru", "")
        self.asil: bool = bool(veri.get("asil", False))
        self.yontem: str = veri["yontem"]
        if self.yontem not in YONTEMLER:
            sys.exit(f"hedefler.yaml: '{self.kod}' için bilinmeyen yöntem '{self.yontem}'")
        self.ikinci_dil = bool(veri.get("ikinci_dil", False))
        self.beta = float(veri.get("beta", 0.2))
        self.taban = float(veri.get("taban", 0.5))
        self.agiz_alfa = float(veri.get("agiz_alfa", 0.5))
        self.yazi_dili_payi: float | None = veri.get("yazi_dili_payi")
        self.buyuk_topluluk = int(veri.get("buyuk_topluluk", 1_000_000))
        self.taban_esik = float(veri.get("taban_esik", 0.5))
        self.taban_cezasi = float(veri.get("taban_cezasi", 0.0))
        self.cevre_esik = float(veri.get("cevre_esik", 0.5))
        self.esik: float | None = veri.get("esik")
        self.bicim: str = veri.get("bicim", "anlasilir")
        self.taniklar = taniklar
        self.ag = ag
        self.dil = {d.kod: d for d in agac.diller}
        self.agirlik = self._agirliklar(agac)

    def _agirliklar(self, agac: Dugum) -> dict[str, float]:
        """Her dilin ağırlığı (normalleştirilmemiş)."""
        N = {d.kod: float(d.konusur) for d in agac.diller}
        if self.yontem == "kisi":
            return N
        if self.yontem == "kopru":
            b = {d.kod: float(d.basamak) for d in agac.diller}
            return {L: self.ozgunluk(L, b) * b[L] / EN_COK_BASAMAK for L in N}
        return {L: 1.0 for L in N}  # yas: ağırlık kullanılmaz

    def benzerlik_payi(self, s: float) -> float:
        """Anlaşılırlığı s olan bir komşu "aynı grup" sayılmaya ne kadar yakın?
        Eşiğin altı hiç, üstü orantılı: (s - eşik) / (1 - eşik). Yarı yarıya
        anlaşmak aynı grupta olmak demek değildir."""
        return max(0.0, (s - self.cevre_esik) / (1 - self.cevre_esik))

    def ozgunluk(self, L: str, b: dict[str, float]) -> float:
        """Kendine özgülük (0..1): dil, kendine çok benzeyen dillerle grubunu ne kadar
        paylaşıyor? Benzeri yoksa 1. Birbirinin aynısı k dil, payı k'ya böler; böylece
        bir dili ayrı dil ya da ağız saymak ağırlığı şişirmez."""
        return b[L] / (b[L] + sum(self.benzerlik_payi(s) * b[j] for j, s in self.ag.komsular(L)))


def hedefleri_yukle(taniklar, agac, ag) -> dict[str, Hedef]:
    with open(HEDEF_DOSYASI, encoding="utf-8") as f:
        return {h.kod: h for h in (Hedef(v, taniklar, agac, ag) for v in yaml.safe_load(f))}


# ========================================================= ses yakınlığı
# Türk dillerinde düzenli olarak birbirine dönüşen sesler (t~d, ş~s, ğ~w~v,
# y~c~j …) yarım maliyetlidir; bir Türk kulağı bunları kolayca eşler.

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

class Bicim:
    def __init__(self, deger):
        if isinstance(deger, dict):
            self.bicim = str(deger["bicim"])
            self.tercih = float(deger.get("tercih", 1.0))
            self.odunc: str | None = deger.get("odunc")    # başka bir Türk dilinden ödünç (veren kodu)
            self.miras: bool = bool(deger.get("miras", False))  # miras olduğu doğrulandı
        else:
            self.bicim, self.tercih, self.odunc, self.miras = str(deger), 1.0, None, False


class Kok:
    """Bir kavramın aday kökü (etimonu)."""

    def __init__(self, veri: dict):
        self.kimlik: str = str(veri["kok"])
        self.koken: str = str(veri.get("koken", "belirsiz"))
        self.kaynak: str = str(veri.get("kaynak", ""))
        self.not_: str = str(veri.get("not", ""))
        self.ana_turkce: str = str(veri.get("ana_turkce", ""))
        self.bicimler: dict[str, Bicim] = {d: Bicim(v) for d, v in (veri.get("bicimler") or {}).items()}
        self.tarihi: dict[str, str] = {d: (v["bicim"] if isinstance(v, dict) else str(v))
                                       for d, v in (veri.get("tarihi") or {}).items()}

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


# ===================================================== toplama (hesap)

def dil_ici_agirliklar(dugum: Dugum, h: Hedef) -> list[tuple[Dugum, float]]:
    """Bir dilin (ya da ağız grubunun) çocukları ve ağırlıkları."""
    cocuklar = [(c, (c.yaprak_sayisi ** h.agiz_alfa) * c.carpan) for c in dugum.alt]
    if h.yazi_dili_payi is not None and dugum.dil_mi and len(cocuklar) > 1:
        agizlar = sum(w for c, w in cocuklar if not c.yazi_dili)
        oran = h.yazi_dili_payi / (1 - h.yazi_dili_payi)
        cocuklar = [(c, agizlar * oran if c.yazi_dili else w) for c, w in cocuklar]
    return cocuklar


def dil_degeri(dugum: Dugum, yaprak, h: Hedef) -> float | None:
    """Bir dilin (ya da dilin içindeki bir düğümün) değeri: ağızlardan alttan yukarı.
    yaprak(kod) -> sayı ya da None (veri yok)."""
    if dugum.yaprak_mi:
        return yaprak(dugum.kod)
    pay = payda = 0.0
    for c, w in dil_ici_agirliklar(dugum, h):
        v = dil_degeri(c, yaprak, h)
        if v is not None:
            pay += w * v
            payda += w
    return pay / payda if payda else None


def toplam(dugum: Dugum, dil_fn, yaprak, h: Hedef) -> float | None:
    """Düğümün değeri. Dilin içindeyse ağızlardan, üstündeyse dillerden (hedefin
    dil ağırlıklarıyla) hesaplanır. dil_fn(dil) -> dilin değeri ya da None."""
    if dugum.dil_ici or dugum.dil_mi:
        return dil_fn(dugum) if dugum.dil_mi else dil_degeri(dugum, yaprak, h)
    pay = payda = 0.0
    for L in dugum.diller:
        v = dil_fn(L)
        if v is not None:
            w = h.agirlik[L.kod]
            pay += w * v
            payda += w
    return pay / payda if payda else None


# ============================================================== ölçüler

def _tercih_yapragi(kok: Kok, kv: Kavram):
    def f(kod):
        if kod not in kv.bilinen_diller:
            return None
        return kok.bicimler[kod].tercih if kod in kok.bicimler else 0.0
    return f


def _anlama_yapragi(kok: Kok, bicim: str, kv: Kavram, h: Hedef):
    def f(kod):
        if kod not in kv.bilinen_diller:
            return None
        if kod not in kok.bicimler:
            return 0.0
        b = kok.bicimler[kod]
        return b.tercih * (h.taban + (1 - h.taban) * benzerlik(bicim, b.bicim))
    return f


def yayilim(dugum, kok, kv, h) -> float | None:
    yaprak = _tercih_yapragi(kok, kv)
    return toplam(dugum, lambda L: dil_degeri(L, yaprak, h), yaprak, h)


def dil_anlamasi(L: Dugum, kok, bicim, kv, h) -> float | None:
    """L dilinin konuşurlarının `bicim`i anlama düzeyi (ikinci dil dahil, hedef izin verirse)."""
    yaprak = _anlama_yapragi(kok, bicim, kv, h)
    kendi = dil_degeri(L, yaprak, h)
    if not h.ikinci_dil:
        return kendi
    yoldan = [s * v for j, s in h.ag.komsular(L.kod, ikinci_dil=True)
              if (v := dil_degeri(h.dil[j], yaprak, h)) is not None]
    if kendi is None and not yoldan:
        return None
    return max([kendi or 0.0] + yoldan)


def anlasilirlik(dugum, kok, bicim, kv, h) -> float | None:
    return toplam(dugum, lambda L: dil_anlamasi(L, kok, bicim, kv, h),
                  _anlama_yapragi(kok, bicim, kv, h), h)


def anlayan_kisi(dugum, kok, bicim, kv, h) -> tuple[float, float]:
    """(anlayan kişi, verisi olan dillerin toplam konuşuru)"""
    pay = payda = 0.0
    for L in dugum.diller:
        v = dil_anlamasi(L, kok, bicim, kv, h)
        if v is not None:
            pay += L.konusur * v
            payda += L.konusur
    return pay, payda


def eskilik(dugum, kok, kv, h) -> float:
    pay = payda = 0.0
    for t in h.taniklar:
        if t.ilgili(dugum) and t.kod in kv.bilinen_taniklar:
            payda += t.agirlik
            pay += t.agirlik if t.kod in kok.tarihi else 0.0
    return pay / payda if payda else 0.0


def en_eski_bicim(dugum, kok, h, sadece_alt=False) -> tuple[str, Tanik] | None:
    for t in h.taniklar:  # kronolojik sırada
        if t.kod in kok.tarihi and (t.altinda(dugum) if sadece_alt else t.ilgili(dugum)):
            return kok.tarihi[t.kod], t
    return None


def taban_acigi(dugum, kok, bicim, kv, h) -> tuple[float, list[tuple[Dugum, float]]]:
    """Büyük toplulukların ağırlıkça ne kadarı biçimi taban_esik'ten az anlıyor?"""
    degerler = [(L, v) for L in dugum.diller if L.konusur >= h.buyuk_topluluk
                if (v := dil_anlamasi(L, kok, bicim, kv, h)) is not None]
    toplam_w = sum(h.agirlik[L.kod] for L, _ in degerler)
    eksik = sum(h.agirlik[L.kod] for L, v in degerler if v < h.taban_esik)
    return (eksik / toplam_w if toplam_w else 0.0), sorted(degerler, key=lambda x: x[1])


def kapsama(dugum, kv, h) -> float:
    toplam_w = sum(h.agirlik[L.kod] for L in dugum.diller)
    bilinen = sum(h.agirlik[L.kod] for L in dugum.diller if L.yaprak_kodlari & kv.bilinen_diller)
    return bilinen / toplam_w if toplam_w else 0.0


# ----------------------------------------------- Hedef 2: kök yaşı

def supheli_odunc(L: Dugum, kok: Kok, kv: Kavram, h: Hedef) -> str | None:
    """L'deki biçim başka koldan bir Türk dilinden ödünç olabilir mi? (veren kodu)

    Açıkça `odunc` yazılmışsa ödünçtür, `miras: true` yazılmışsa değildir. Bunların
    dışında yalnızca L kendi kolunda bu kökün TEK kanıtıysa şüphelenilir (ör.
    Çuvaşça Oğur kolunun tek dilidir): yakın akraba dillerin miras kelimeleri de
    birbirine benzediği için, aynı kolda başka kanıt varsa benzerlik bir şey
    söylemez."""
    kodlar = [k for k in L.yaprak_kodlari if k in kok.bicimler]
    if not kodlar:
        return None
    for k in kodlar:
        b = kok.bicimler[k]
        if b.miras:
            return None
        if b.odunc:
            return b.odunc
    if any(D is not L and D.yaprak_kodlari & set(kok.bicimler) for D in (L.kol.diller if L.kol else [])):
        return None
    for veren, yogunluk in h.ag.verenler(L.kod):
        V = h.dil[veren]
        if yogunluk < 0.5 or V.kol is L.kol:
            continue
        vb = [kok.bicimler[k].bicim for k in V.yaprak_kodlari if k in kok.bicimler]
        if vb and any(benzerlik(kok.bicimler[k].bicim, x) >= 0.75 for k in kodlar for x in vb):
            return veren
    return None


def dil_tanikliyor(L, kok, kv, h) -> bool:
    return bool(L.yaprak_kodlari & set(kok.bicimler)) and supheli_odunc(L, kok, kv, h) is None


def kol_tanikliyor(c: Dugum, kok, kv, h) -> bool:
    return (any(dil_tanikliyor(L, kok, kv, h) for L in c.diller)
            or any(t.altinda(c) and t.kod in kok.tarihi for t in h.taniklar))


def kok_yasi(dugum: Dugum, kok, kv, h) -> tuple[int, int, Dugum] | None:
    """(derinlik, genişlik, ulaşılan düğüm). Derinlik 0: kök bu düğümün dilinde vardı."""
    if dugum.dil_mi:
        return (0, 1, dugum) if dil_tanikliyor(dugum, kok, kv, h) else None
    hatlar = [c for c in dugum.alt if kol_tanikliyor(c, kok, kv, h)]
    dogrudan = [t for t in h.taniklar if t.dal is dugum and t.kod in kok.tarihi]
    if len(hatlar) + len(dogrudan) >= 2:
        return 0, len(hatlar) + len(dogrudan), dugum
    en_iyi = None
    for c in hatlar:
        if (r := kok_yasi(c, kok, kv, h)) is not None:
            aday = (r[0] + 1, r[1], r[2])
            if en_iyi is None or (aday[0], -aday[1]) < (en_iyi[0], -en_iyi[1]):
                en_iyi = aday
    if en_iyi is None and dogrudan:
        return 1, 1, dugum  # yalnızca tek bir tarihî tanıkta
    return en_iyi


def yas_etiketi(r, kok_dugum: Dugum) -> str:
    if r is None:
        return "—"
    _, genislik, d = r
    ad = "Ana Türkçe" if d is kok_dugum else d.ad
    return f"{ad} ({genislik} hat)"


def yas_anahtari(dugum, kok, kv, h):
    r = kok_yasi(dugum, kok, kv, h)
    if r is None:
        return None
    kollar = {L.kol for L in dugum.diller if dil_tanikliyor(L, kok, kv, h)}
    tanik_sira = min((t.sira for t in h.taniklar if t.altinda(dugum) and t.kod in kok.tarihi), default=99)
    dil_sayisi = sum(1 for L in dugum.diller if dil_tanikliyor(L, kok, kv, h))
    return (r[0], -r[1], -len(kollar), tanik_sira, -dil_sayisi)


# ================================================================ seçim

class Secim:
    def __init__(self, dugum, kok, bicim, miras, gunluk=None, puanlar=None, tanik=None):
        self.dugum: Dugum = dugum
        self.kok: Kok = kok
        self.bicim: str = bicim
        self.miras: bool = miras        # bu düğümde Türkçe aday yok -> üstten alındı
        self.gunluk: str | None = gunluk
        self.puanlar: dict = puanlar or {}
        self.tanik: Tanik | None = tanik
        self.alt: list[Secim] = []


def _gunluk(dugum: Dugum, kv: Kavram) -> str | None:
    """Dilin/ağzın bugün en çok kullandığı biçim (alıntı olabilir)."""
    hedef = dugum.alt[0] if (dugum.dil_mi and dugum.alt) else dugum
    if not hedef.yaprak_mi:
        return None
    adaylar = [(k.bicimler[hedef.kod].tercih, k.bicimler[hedef.kod].bicim)
               for k in kv.kokler if hedef.kod in k.bicimler]
    return max(adaylar)[1] if adaylar else None


def _yaygin_bicim(dugum: Dugum, kok: Kok, eski: str | None = None) -> str:
    """En çok dilde görülen biçim; eşitlikte en eski tanık biçimine en yakın olan,
    o da eşitse daha çok kişinin kullandığı."""
    sayac = Counter(kok.bicimler[k].bicim for k in dugum.yaprak_kodlari if k in kok.bicimler)
    kisi: Counter = Counter()
    for L in dugum.diller:
        for k in L.yaprak_kodlari:
            if k in kok.bicimler:
                kisi[kok.bicimler[k].bicim] += L.konusur
    return max(sayac, key=lambda f: (sayac[f], round(benzerlik(f, eski), 6) if eski else 0.0, kisi[f], f))


def kopru_puani(dugum, kok, bicim, kv, h) -> float:
    a = anlasilirlik(dugum, kok, bicim, kv, h) or 0.0
    if h.yontem == "kopru" and h.taban_cezasi:
        a -= h.taban_cezasi * taban_acigi(dugum, kok, bicim, kv, h)[0]
    return a


def sec(dugum: Dugum, kv: Kavram, h: Hedef, ust: Secim | None = None) -> Secim:
    gunluk = _gunluk(dugum, kv)
    puan: dict[str, float] = {}
    bicim_puanlari: dict[str, dict[str, float]] = {}
    yas_anah: dict[str, tuple] = {}
    for k in kv.kokler:
        if not k.secilebilir or not yayilim(dugum, k, kv, h):
            continue
        if h.yontem == "yas" and not (dugum.dil_mi or dugum.dil_ici):
            if (anah := yas_anahtari(dugum, k, kv, h)) is None:
                continue
            yas_anah[k.kimlik] = anah
            puan[k.kimlik] = -anah[0]
            continue
        if h.yontem == "yas":  # dilin içinde: en çok tercih edilen kök
            puan[k.kimlik] = yayilim(dugum, k, kv, h) or 0.0
            continue
        bicimler = {k.bicimler[c].bicim for c in dugum.yaprak_kodlari if c in k.bicimler}
        bp = {f: kopru_puani(dugum, k, f, kv, h) for f in bicimler}
        bicim_puanlari[k.kimlik] = bp
        puan[k.kimlik] = max(bp.values()) + h.beta * eskilik(dugum, k, kv, h)

    if not puan:
        if ust is None:
            raise ValueError(f"{kv.yol.name}: Türkçe kökenli hiçbir aday yok")
        s = Secim(dugum, ust.kok, ust.bicim, True, gunluk, tanik=ust.tanik)
    else:
        if yas_anah:
            en_iyi = min(yas_anah, key=lambda k: (yas_anah[k], k))
        else:
            en_iyi = max(puan, key=lambda k: (puan[k], k))
        kok = kv.kok(en_iyi)
        tanik = None
        if h.bicim == "eski" and (eski := en_eski_bicim(dugum, kok, h, sadece_alt=True)):
            bicim, tanik = eski
        elif dugum.yaprak_mi:
            bicim = kok.bicimler[dugum.kod].bicim
        elif h.bicim == "eski" or en_iyi not in bicim_puanlari:
            eski = en_eski_bicim(dugum, kok, h)
            bicim = _yaygin_bicim(dugum, kok, eski[0] if eski else None)
        else:
            eski = en_eski_bicim(dugum, kok, h)
            bp = {f: v + (h.beta * benzerlik(f, eski[0]) if eski else 0.0)
                  for f, v in bicim_puanlari[en_iyi].items()}
            bicim = max(bp, key=lambda f: (bp[f], f))
        s = Secim(dugum, kok, bicim, False, gunluk, puan, tanik)

    s.alt = [sec(c, kv, h, s) for c in dugum.alt]
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
    if s.tanik is not None and not s.miras:
        notlar.append(f"tanık: {s.tanik.kisa}")
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


def _kisa_ad(L: Dugum) -> str:
    """Parantezsiz dil adı: 'Irak Türkmencesi (Kerkük)' -> 'Irak Türkmencesi'."""
    return L.ad.split(" (")[0]


def hedef_secimleri(kv, agac, hedefler) -> dict[str, Secim]:
    return {kod: sec(agac, kv, h) for kod, h in hedefler.items()}


def uyum(secimler: dict[str, Secim]) -> str:
    return "UYUŞUYOR" if len({s.kok.kimlik for s in secimler.values()}) == 1 else "AYRIŞIYOR"


def _hedef(hedefler, yontem) -> Hedef:
    return next(h for h in hedefler.values() if h.yontem == yontem)


def aday_olculeri(kv, agac, hedefler):
    """Her aday kök için üç ölçü."""
    h1, h2, h3 = _hedef(hedefler, "kopru"), _hedef(hedefler, "yas"), _hedef(hedefler, "kisi")
    sonuc = []
    for k in kv.kokler:
        if not k.secilebilir or not yayilim(agac, k, kv, h1):
            sonuc.append((k, None))
            continue
        bicimler = {b.bicim for b in k.bicimler.values()}

        def secilen(h, puan_fn):
            """Hedefin seçimdeki biçim kuralının aynısı: puan + β × eski biçime yakınlık."""
            eski = en_eski_bicim(agac, k, h)
            return max(bicimler, key=lambda f: (puan_fn(f) + (h.beta * benzerlik(f, eski[0]) if eski else 0.0), f))

        b1 = secilen(h1, lambda f: kopru_puani(agac, k, f, kv, h1))
        p1 = kopru_puani(agac, k, b1, kv, h1) + h1.beta * eskilik(agac, k, kv, h1)
        en_dusuk = taban_acigi(agac, k, b1, kv, h1)[1]
        b3 = secilen(h3, lambda f: anlasilirlik(agac, k, f, kv, h3) or 0.0)
        kisi, bilinen = anlayan_kisi(agac, k, b3, kv, h3)
        r = kok_yasi(agac, k, kv, h2)
        supheli = [(L, v) for L in agac.diller if (v := supheli_odunc(L, k, kv, h2))]
        sonuc.append((k, dict(b1=b1, p1=p1, en_dusuk=en_dusuk[0] if en_dusuk else None,
                              yas=yas_etiketi(r, agac), b3=b3, kisi=kisi, bilinen=bilinen,
                              supheli=supheli)))
    return sonuc


def kavram_raporu(kv, agac, hedefler, h, derinlik, agizlar):
    durum = "doğrulandı" if kv.dogrulandi else "DOĞRULANMADI"
    h1 = _hedef(hedefler, "kopru")
    print("=" * 88)
    print(f"{kv.ad}  ({kv.ingilizce})  [{durum}]   veri kapsaması (Hedef 1 ağırlığıyla): "
          f"%{100 * kapsama(agac, kv, h1):.0f}   tarihî tanık: {len(kv.bilinen_taniklar)}/{len(h.taniklar)}")
    secimler = hedef_secimleri(kv, agac, hedefler)
    ozet = "   ".join(f"{hedefler[k].ad}: {s.bicim}" for k, s in secimler.items())
    print(f"Üç hedef → {ozet}   [{uyum(secimler)}]")
    print("-" * 88)

    print("Adaylar ve üç ölçü (en tepede):")
    print(f"  {'kök':<9} {'1. yaygınlık puanı':<30} {'2. kök yaşı':<26} 3. anlayan kişi")
    for k, o in aday_olculeri(kv, agac, hedefler):
        if o is None:
            print(f"  {k.kimlik:<9} (seçilemez: köken={k.koken})")
            continue
        dusuk = f"en düşük: {_kisa_ad(o['en_dusuk'][0])} %{100 * o['en_dusuk'][1]:.0f}" if o["en_dusuk"] else ""
        p1 = f"{o['p1']:.2f} '{o['b1']}' {dusuk}"
        oran = o["kisi"] / o["bilinen"] if o["bilinen"] else 0
        p3 = f"~{o['kisi'] / 1e6:.0f} milyon (%{100 * oran:.0f}) '{o['b3']}'"
        print(f"  {k.kimlik:<9} {p1:<30} {o['yas']:<26} {p3}")
        for L, veren in o["supheli"]:
            print(f"  {'':<9}   ⚠ {L.ad}: ödünç olabilir (veren: {h.dil[veren].ad}); kök yaşında sayılmadı")
        if k.ana_turkce:
            print(f"  {'':<9}   bilimsel Ana Türkçe kuruluşu: {k.ana_turkce}")

    secim = secimler[h.kod]
    print(f"\nHedef: {h.ad} — {h.soru}")
    print(f"Seçim: {secim.bicim}  (kök: {secim.kok.kimlik})")
    if h.esik is not None and (yayilim(agac, secim.kok, kv, h) or 0) < h.esik:
        print(f"  ⚠ CANLANDIRMA: bu kök bugün dillerin ağırlıkça yarısından azında yaşıyor; "
              f"öğretilmesi gerekecek.")
    if h.yontem == "kopru":
        _, degerler = taban_acigi(agac, secim.kok, secim.bicim, kv, h)
        if degerler:
            print("Büyük topluluklarda anlaşılırlık: "
                  + ", ".join(f"{_kisa_ad(L)} %{100 * v:.0f}" for L, v in degerler))
    print()
    yazdir(secim, derinlik, agizlar)
    print()


def karsilastirma_raporu(kavramlar, agac, hedefler, md):
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
        ayrisan = sum(1 for *_, u in satirlar if u == "AYRIŞIYOR")
        print(f"Toplam {len(satirlar)} kavram, {ayrisan} tanesi ayrışıyor.\n")
        print("| Kavram | " + " | ".join(h.ad for h in sutunlar) + " | Durum |")
        print("|---|" + "---|" * len(sutunlar) + "---|")
        for kv, ss, u in satirlar:
            print(f"| {kv.ad} | " + " | ".join(f"{x.bicim} *({x.kok.kimlik})*" for x in ss) + f" | {u} |")
        return
    print(f"{'Kavram':<12}" + "".join(f"{h.ad:<26}" for h in sutunlar) + "Durum")
    for kv, ss, u in satirlar:
        print(f"{kv.ad:<12}" + "".join(f"{x.bicim + ' (' + x.kok.kimlik + ')':<26}" for x in ss) + u)


def agirlik_raporu(agac: Dugum, h: Hedef, md: bool):
    if h.yontem == "yas":
        metin = (f"**{h.ad}** ağırlık kullanmaz. Bir kökün yaşı, soy ağacının (agac.yaml) hangi "
                 "düğümüne kadar geri gittiğine bakılarak bulunur: bir düğümün en az iki kolunda "
                 "bulunan kök o düğümün dilinde de vardı. Nüfus ve dil sayısı önemsizdir.")
        print(f"## {h.ad}\n\n{metin}\n" if md else metin)
        return
    toplam_w = sum(h.agirlik.values())
    N = {L.kod: float(L.konusur) for L in agac.diller}
    kollar = [d for d in agac.tum_dugumler() if d.tip == "kol"]
    kural = ("dil ağırlığı = kendine özgülük × basamak / 8; kendine özgülük = b / (b + Σ pay(s) × b_komşu), "
             f"pay(s) = (s − {h.cevre_esik}) / (1 − {h.cevre_esik})"
             if h.yontem == "kopru" else "dil ağırlığı = konuşur sayısı")
    b = {L.kod: float(L.basamak) for L in agac.diller}
    if md:
        print(f"## {h.ad}\n\n*{h.soru}* {kural}.\n")
        print("| Kol | Ağırlık |\n|---|---:|")
        for k in kollar:
            print(f"| {k.ad} | %{100 * sum(h.agirlik[L.kod] for L in k.diller) / toplam_w:.1f} |")
        print()
        cevre_baslik = " Basamak | Kendine özgülük |" if h.yontem == "kopru" else ""
        print(f"| Dil | Kol | Konuşur |{cevre_baslik} Ağırlık |")
        print("|---|---|---:|" + ("---:|---:|" if h.yontem == "kopru" else "") + "---:|")
        for L in sorted(agac.diller, key=lambda L: -h.agirlik[L.kod]):
            cevre = f" {L.basamak} | {h.ozgunluk(L.kod, b):.2f} |" if h.yontem == "kopru" else ""
            print(f"| {L.ad} | {L.kol.ad if L.kol else ''} | {L.konusur:,} |".replace(",", ".")
                  + cevre + f" %{100 * h.agirlik[L.kod] / toplam_w:.2f} |")
        print()
        return
    print(f"Ağırlıklar — {h.ad}: {kural}\n")
    for k in kollar:
        print(f"  {k.ad:<16} %{100 * sum(h.agirlik[L.kod] for L in k.diller) / toplam_w:5.1f}")
    print()
    for L in sorted(agac.diller, key=lambda L: -h.agirlik[L.kod]):
        cevre = f"  b{L.basamak}  özgülük {h.ozgunluk(L.kod, b):.2f}" if h.yontem == "kopru" else ""
        print(f"  {L.ad:<30} {L.konusur:>12,}{cevre}   %{100 * h.agirlik[L.kod] / toplam_w:5.2f}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("kavramlar", nargs="*", help="kavram dosya adları (uzantısız)")
    ap.add_argument("--hedef", help="ortak | ana | nufus (varsayılan: asıl hedef)")
    for ad in ("beta", "taban", "esik", "taban_cezasi"):
        ap.add_argument(f"--{ad}", type=float, help=f"seçili hedefin {ad} değerini değiştir")
    ap.add_argument("--derinlik", type=int, default=-1, help="gösterilecek en derin seviye (-1: tümü)")
    ap.add_argument("--agizlar", action="store_true", help="dillerin altındaki ağızları da göster")
    ap.add_argument("--agirliklar", action="store_true", help="dil ağırlıklarını göster ve çık")
    ap.add_argument("--karsilastir", action="store_true", help="üç hedefin seçimlerini yan yana göster")
    ap.add_argument("--md", action="store_true", help="tabloları Markdown olarak yaz")
    args = ap.parse_args()

    agac = agac_yukle()
    ag = Ag(agac)
    taniklar = taniklari_yukle(agac)
    hedefler = hedefleri_yukle(taniklar, agac, ag)
    if args.hedef and args.hedef not in hedefler:
        sys.exit(f"Bilinmeyen hedef '{args.hedef}'. Seçenekler: {', '.join(hedefler)}")
    h = hedefler[args.hedef] if args.hedef else next(x for x in hedefler.values() if x.asil)
    for ad in ("beta", "taban", "esik", "taban_cezasi"):
        if getattr(args, ad) is not None:
            setattr(h, ad, getattr(args, ad))

    if args.agirliklar:
        if args.md and not args.hedef:
            print("# Ağırlıklar\n")
            print("> Bu dosya `python3 araclar/puanla.py --agirliklar --md > AGIRLIKLAR.md` komutuyla "
                  "üretilir; elle düzenlemeyin. Her hedef kendi ölçüsünü kullanır "
                  "(bkz. `hedefler.yaml`, ILKELER.md §1). Bir dilin içinde yazı dili %50, "
                  "ağızlar kalan %50'yi paylaşır (Hedef 1 ve 3).\n")
            for x in hedefler.values():
                agirlik_raporu(agac, x, True)
        else:
            agirlik_raporu(agac, h, args.md)
        return
    kavramlar = kavramlari_yukle(args.kavramlar, agac, taniklar)
    if args.karsilastir:
        karsilastirma_raporu(kavramlar, agac, hedefler, args.md)
        return
    for kv in kavramlar:
        kavram_raporu(kv, agac, hedefler, h, args.derinlik, args.agizlar)


if __name__ == "__main__":
    main()
