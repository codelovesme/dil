#!/usr/bin/env python3
"""Kaynak sözlüğünden (kaynaklar/kaynaklar.yaml) okunabilir dizin üretir.

Kullanım:
    python3 araclar/kaynaklar.py > kaynaklar/KAYNAKLAR.md
    python3 araclar/kaynaklar.py --ara chv          # bir dil ya da ihtiyaç için kaynaklar
    python3 araclar/kaynaklar.py --ara odunc
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlparse

import yaml

KOK = Path(__file__).resolve().parent.parent
KAYNAK_DOSYASI = KOK / "kaynaklar" / "kaynaklar.yaml"

ALANLAR = {"kimlik", "ad", "url", "tur", "diller", "kullanim", "ne", "nasil", "erisim",
           "bicim", "guven", "durum", "dogrulama", "not"}
TURLER = {
    "etimoloji": "Etimoloji ve karşılaştırmalı sözlükler",
    "veri-seti": "Karşılaştırmalı veri setleri",
    "kavram-listesi": "Kavram listeleri",
    "tarihi": "Tarihî metinler ve sözlükler",
    "sozluk": "Dil sözlükleri",
    "derlem": "Derlemler ve sıklık listeleri",
    "belgeleme": "Küçük diller ve belgeleme",
    "siniflandirma": "Sınıflandırma ve el kitapları",
    "nufus": "Konuşur sayısı ve canlılık",
    "anlasilirlik": "Anlaşılırlık ve benzerlik çalışmaları",
    "ses": "Ses bilgisi",
    "yazim": "Yazım",
    "portal": "Portallar ve kütüphaneler",
    "dergi": "Dergiler ve bibliyografya",
    "arac": "Araçlar",
}
ERISIM = {"acik": "açık", "kismen": "kısmen", "ucretli": "ücretli", "basili": "basılı"}
GUVEN = {"yuksek": "yüksek", "orta": "orta", "dusuk": "düşük"}
GUVEN_SIRA = {"yuksek": 0, "orta": 1, "dusuk": 2}
DURUM = {"denendi": "bu ortamdan açıldı", "arandi": "aramada görüldü", "basili": "basılı"}


DIL_OF: dict[str, str] = {}   # ağız kodu -> dil kodu


def gecerli_kodlar() -> dict[str, str]:
    """Diller, tarihî tanıklar ve 'tum' (ad sırasıyla). Ağız kodları DIL_OF'ta."""
    sys.path.insert(0, str(KOK / "araclar"))
    import puanla  # noqa: E402
    agac = puanla.agac_yukle()
    kodlar = {d.kod: d.ad for d in agac.diller}
    for d in agac.diller:
        for k in d.yaprak_kodlari:
            DIL_OF[k] = d.kod
    kodlar.update({t.kod: t.ad for t in puanla.taniklari_yukle(agac)})
    kodlar["tum"] = "Bütün Türk dilleri"
    return kodlar


def yukle():
    with open(KAYNAK_DOSYASI, encoding="utf-8") as f:
        veri = yaml.safe_load(f)
    kodlar = gecerli_kodlar()
    ihtiyaclar = veri["ihtiyaclar"]
    hatalar = []
    kimlikler = Counter(k["kimlik"] for k in veri["kaynaklar"])
    for k in veri["kaynaklar"]:
        ad = k.get("kimlik", "?")
        if kimlikler[ad] > 1:
            hatalar.append(f"{ad}: kimlik tekrar ediyor")
        if fazla := set(k) - ALANLAR:
            hatalar.append(f"{ad}: bilinmeyen alan {sorted(fazla)}")
        for alan in ("kimlik", "ad", "url", "tur", "diller", "kullanim", "ne", "erisim", "guven", "durum"):
            if alan not in k:
                hatalar.append(f"{ad}: '{alan}' eksik")
        if k.get("tur") not in TURLER:
            hatalar.append(f"{ad}: bilinmeyen tür '{k.get('tur')}'")
        if bilinmeyen := set(k.get("diller", [])) - set(kodlar) - set(DIL_OF):
            hatalar.append(f"{ad}: bilinmeyen dil kodu {sorted(bilinmeyen)}")
        if bilinmeyen := set(k.get("kullanim", [])) - set(ihtiyaclar):
            hatalar.append(f"{ad}: bilinmeyen ihtiyaç {sorted(bilinmeyen)}")
        for alan, sozluk in (("erisim", ERISIM), ("guven", GUVEN), ("durum", DURUM)):
            if k.get(alan) not in sozluk:
                hatalar.append(f"{ad}: geçersiz {alan} '{k.get(alan)}'")
    if hatalar:
        sys.exit("kaynaklar.yaml hataları:\n  " + "\n  ".join(hatalar))
    return veri, kodlar


def host(url: str) -> str:
    return urlparse(url).hostname or ""


def ortam(k: dict, izinli: set[str]) -> str:
    if k["erisim"] == "basili":
        return "—"
    return "izinli" if host(k["url"]) in izinli else f"izinsiz ({host(k['url'])})"


def sirala(liste):
    return sorted(liste, key=lambda k: (GUVEN_SIRA[k["guven"]], k["ad"]))


def kisa(k: dict, izinli: set[str]) -> str:
    etiket = f"{ERISIM[k['erisim']]}, güven: {GUVEN[k['guven']]}"
    o = ortam(k, izinli)
    if o != "—":
        etiket += ", ortam: " + ("✓" if o == "izinli" else "✗")
    return f"[{k['ad']}](#{k['kimlik']}) — {etiket}"


def md(veri, kodlar) -> str:
    izinli = set(veri["izinli_hostlar"])
    ks = veri["kaynaklar"]
    satir = []
    y = satir.append
    y("# Kaynak sözlüğü\n")
    y("> Bu dosya `python3 araclar/kaynaklar.py > kaynaklar/KAYNAKLAR.md` komutuyla "
      "[`kaynaklar.yaml`](kaynaklar.yaml) dosyasından üretilir; elle düzenlemeyin.\n")
    y(f"Toplam **{len(ks)} kaynak**. Her kayıtta: ne işe yaradığı, adresi, kapsadığı diller, "
      "nasıl kullanılacağı, erişim türü, güvenilirlik ve bu ortamdan erişilip erişilemediği.\n")
    y("- **Güven:** yüksek = hakemli ya da uzman eseri; orta = derlenmiş ya da topluluk ürünü; "
      "düşük = küçük liste ya da kaba tahmin.")
    y("- **Ortam:** ✓ bu oturumun ağ izni olan adres; ✗ izin listesine eklenmesi gerekir "
      "(bkz. [Erişim](#bu-ortamdan-erisim)).")
    durumlar = Counter(k["durum"] for k in ks)
    y(f"- **Durum:** {durumlar['denendi']} kaynak bu ortamdan açılıp denetlendi, "
      f"{durumlar['arandi']} kaynak aramada görüldü, {durumlar['basili']} kaynak basılı. "
      "Son denetimin sonucu her kaydın **Doğrulama** satırında.")
    y("- **Hızlı arama:** `python3 araclar/kaynaklar.py --ara <dil kodu ya da ihtiyaç>` "
      "(ör. `--ara chv`, `--ara odunc`).\n")

    y("## İhtiyaca göre\n")
    for ih, ad in veri["ihtiyaclar"].items():
        secilen = sirala([k for k in ks if ih in k["kullanim"]])
        if not secilen:
            continue
        y(f"### {ad}\n")
        for k in secilen:
            y(f"- {kisa(k, izinli)}")
        y("")

    y("## Dile göre\n")
    y("Yalnızca o dili **özellikle** kapsayan kaynaklar. Bütün diller için geçerli kaynaklar "
      "(Wiktionary, StarLing, ESTJa, Savelyev vb.) her dil için ayrıca kullanılabilir.\n")
    y("| Dil | Kaynaklar |")
    y("|---|---|")
    dil_kaynak = defaultdict(list)
    for k in ks:
        for d in {DIL_OF.get(x, x) for x in k["diller"]}:
            if d != "tum":
                dil_kaynak[d].append(k)
    for kod, ad in kodlar.items():
        if kod == "tum":
            continue
        liste = sirala(dil_kaynak.get(kod, []))
        hucre = ", ".join(f"[{k['kimlik']}](#{k['kimlik']})" for k in liste) or "*özel kaynak bulunamadı*"
        y(f"| {ad} (`{kod}`) | {hucre} |")
    y("")

    y("## Bütün kaynaklar\n")
    for tur, baslik in TURLER.items():
        secilen = sirala([k for k in ks if k["tur"] == tur])
        if not secilen:
            continue
        y(f"### {baslik}\n")
        for k in secilen:
            y(f'<a id="{k["kimlik"]}"></a>')
            y(f"#### {k['ad']}\n")
            y(f"<{k['url']}>\n")
            y(f"{k['ne'].strip()}\n")
            if k.get("nasil"):
                y(f"**Nasıl kullanılır:** {k['nasil'].strip()}\n")
            diller = ", ".join("bütün diller" if d == "tum" else kodlar.get(d, f"`{d}` (ağız)")
                               for d in k["diller"])
            y(f"- **Diller:** {diller}")
            y(f"- **İşe yaradığı yer:** {', '.join(veri['ihtiyaclar'][i] for i in k['kullanim'])}")
            y(f"- **Erişim:** {ERISIM[k['erisim']]} · **Biçim:** {k.get('bicim', '—')} · "
              f"**Güven:** {GUVEN[k['guven']]} · **Durum:** {DURUM[k['durum']]} · "
              f"**Ortam:** {ortam(k, izinli)}")
            if k.get("dogrulama"):
                y(f"- **Doğrulama:** {k['dogrulama'].strip()}")
            if k.get("not"):
                y(f"- **Not:** {k['not'].strip()}")
            y(f"- **Kimlik:** `{k['kimlik']}`\n")

    y('<a id="bu-ortamdan-erisim"></a>')
    y("## Bu ortamdan erişim\n")
    y("Bu oturumun ortamında (**dil**) yalnızca şu adreslere izin var: "
      + ", ".join(f"`{h}`" for h in sorted(izinli)) + ".\n")
    y("Çevrim içi kaynakların ihtiyaç duyduğu, henüz izinli olmayan adresler (kaç kaynağın "
      "kullandığına göre). Bir kaynağı kullanmak gerektiğinde ilgili adres ortama eklenir.\n")
    sayac = Counter(host(k["url"]) for k in ks if k["erisim"] != "basili" and host(k["url"]) not in izinli)
    y("| Adres | Kaynak sayısı | Kaynaklar |")
    y("|---|---:|---|")
    for h, n in sayac.most_common():
        isimler = ", ".join(f"`{k['kimlik']}`" for k in ks if host(k["url"]) == h and k["erisim"] != "basili")
        y(f"| `{h}` | {n} | {isimler} |")
    y("")
    return "\n".join(satir)


def ara(veri, kodlar, sorgu: str):
    izinli = set(veri["izinli_hostlar"])
    ks = veri["kaynaklar"]
    if sorgu in veri["ihtiyaclar"]:
        print(f"İhtiyaç: {veri['ihtiyaclar'][sorgu]}\n")
        secilen = [k for k in ks if sorgu in k["kullanim"]]
    elif sorgu in kodlar:
        print(f"Dil: {kodlar[sorgu]}  (özel kaynaklar, sonra genel kaynaklar)\n")
        secilen = ([k for k in ks if sorgu in {DIL_OF.get(x, x) for x in k["diller"]}]
                   + [k for k in ks if "tum" in k["diller"]])
    else:
        q = sorgu.lower()
        secilen = [k for k in ks if q in (k["ad"] + k["ne"] + k.get("nasil", "")).lower()]
        print(f"Metin araması: '{sorgu}'\n")
    for k in secilen:
        print(f"- {k['ad']}\n    {k['url']}\n    {ERISIM[k['erisim']]}, güven: {GUVEN[k['guven']]}, "
              f"ortam: {ortam(k, izinli)}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ara", help="dil kodu, ihtiyaç adı ya da serbest metin")
    a = ap.parse_args()
    veri, kodlar = yukle()
    if a.ara:
        ara(veri, kodlar, a.ara)
    else:
        print(md(veri, kodlar))


if __name__ == "__main__":
    main()
