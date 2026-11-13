#!/usr/bin/env python3
"""Statik siteyi Markdown çıktılarından kurar (GitHub Pages).

Kullanım:
    python3 araclar/yayinla.py             # önce çıktıları üret (ya da --denetle)
    python3 araclar/site.py                # _site/ klasörüne kur
    python3 araclar/site.py --cikti /yol   # başka bir klasöre

Sayfa listesi ve arama dizini cikti/site.json'dan okunur. Depodaki göreli
bağlantılar sitede de çalışır: .md → .html; sayfası olan .yaml dosyası (kavram,
kök) o sayfaya; geri kalan dosyalar GitHub'daki kaynağına gider. Bütün yollar
göreli olduğu için site bir alt yolda (kullanici.github.io/depo/) da, kendi alan
adında da değişmeden çalışır.
"""
from __future__ import annotations

import argparse
import html
import json
import os
import posixpath
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

import markdown

KOK = Path(__file__).resolve().parent.parent
DEPO = os.environ.get("GITHUB_REPOSITORY", "codelovesme/dil")
DAL = os.environ.get("BITIG_DAL", "main")
GITHUB = f"https://github.com/{DEPO}"

MENU = [("sozluk/SOZLUK.md", "Sözlük"), ("sozluk/KAVRAMLAR.md", "Kavramlar"),
        ("KARSILASTIRMA.md", "Karşılaştırma"), ("kaynaklar/KAYNAKLAR.md", "Kaynaklar"),
        ("AGIRLIKLAR.md", "Diller"), ("ILKELER.md", "İlkeler")]

TR = str.maketrans("çğıöşüâîûÇĞİÖŞÜÂÎÛ", "cgiosuaiuCGIOSUAIU")


def slug(metin: str, ayrac: str = "-") -> str:
    s = metin.translate(TR).lower()
    s = re.sub(r"[^a-z0-9]+", ayrac, s).strip(ayrac)
    return s or "bolum"


# ================================================================ bağlantılar

def html_yolu(md_yolu: str) -> str:
    if md_yolu == "README.md":
        return "proje.html"
    return md_yolu[:-3] + ".html"


def baglantilari_cevir(govde: str, sayfa: str, sayfalar: set[str]) -> str:
    """Göreli depo bağlantılarını site bağlantılarına çevirir."""
    dizin = posixpath.dirname(sayfa)

    def cevir(m: re.Match) -> str:
        nitelik, hedef = m.group(1), html.unescape(m.group(2))
        if re.match(r"^(?:[a-z]+:|#|//)", hedef):
            return m.group(0)
        yol, _, capa = hedef.partition("#")
        tam = posixpath.normpath(posixpath.join(dizin, yol)) if yol else sayfa
        if tam.endswith(".yaml") and tam[:-5] + ".md" in sayfalar and tam[:-5] + ".md" != sayfa:
            tam = tam[:-5] + ".md"
        if tam in sayfalar:
            yeni = posixpath.relpath(html_yolu(tam), dizin or ".")
        elif tam.endswith("/") or "." not in posixpath.basename(tam):
            yeni = f"{GITHUB}/tree/{DAL}/{tam}"
        else:
            yeni = f"{GITHUB}/blob/{DAL}/{tam}"
        if capa:
            yeni += "#" + capa
        return f'{nitelik}="{html.escape(yeni, quote=True)}"'

    return re.sub(r'(href)="([^"]*)"', cevir, govde)


# ==================================================================== şablon

def sayfa_html(baslik: str, govde: str, yol: str, site: dict, tur: str = "") -> str:
    kok = "../" * yol.count("/")
    menu = "".join(
        f'<a href="{kok}{html_yolu(m)}"{" aria-current=page" if m == yol else ""}>{ad}</a>'
        for m, ad in MENU)
    zaman = os.environ.get("BITIG_ZAMAN") or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    sha = os.environ.get("GITHUB_SHA", "")[:7]
    kaynak = f'<a href="{GITHUB}/blob/{DAL}/{yol}">kaynak dosya</a> · ' if yol.endswith(".md") else ""
    surum = f' · <a href="{GITHUB}/commit/{sha}">{sha}</a>' if sha else ""
    return f"""<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(baslik)} · Bitig</title>
<meta name="description" content="{html.escape(site['aciklama'])}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%23b4532a'/%3E%3Ctext x='16' y='23' font-size='19' text-anchor='middle' fill='white' font-family='serif'%3E%F0%90%B0%8B%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Old+Turkic&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{kok}varlik/site.css">
<script>try{{var t=localStorage.getItem('bitig-tema');if(t)document.documentElement.dataset.theme=t}}catch(e){{}}</script>
</head>
<body class="tur-{tur}">
<header class="ust">
  <div class="ust-ic">
    <a class="logo" href="{kok}index.html"><span class="runik" aria-hidden="true">𐰋𐰃𐱅𐰃𐰏</span> Bitig</a>
    <nav class="menu" aria-label="Bölümler">{menu}</nav>
    <div class="ara">
      <input id="ara" type="search" placeholder="Ara: kelime, kök, dil, kaynak…" autocomplete="off"
             aria-label="Ara" data-kok="{kok}">
      <ul id="ara-sonuc" role="listbox" hidden></ul>
    </div>
    <button class="tema" type="button" aria-label="Açık/koyu tema" title="Açık/koyu tema">◐</button>
  </div>
</header>
<main class="icerik">
{govde}
</main>
<footer class="alt">
  <p>Bitig — öz Türkçe köklerle ortak Türk dili çalışması. {kaynak}<a href="{GITHUB}">GitHub</a> ·
  güncelleme {zaman}{surum}</p>
</footer>
<script src="{kok}varlik/site.js" defer></script>
</body>
</html>
"""


def ana_sayfa(site: dict) -> str:
    s = site["sayilar"]
    kavramlar = [a for a in site["arama"] if a["t"] == "kavram"]
    satirlar = "".join(
        f'<li><a href="{html.escape(html_yolu(a["yol"]))}"><b>{html.escape(a["ad"])}</b>'
        f'<span>{html.escape(a["ozet"])}</span></a></li>' for a in kavramlar)
    return f"""
<section class="giris">
  <p class="ust-baslik"><span class="runik">𐰋𐰃𐱅𐰃𐰏</span> bitig · Eski Türkçede "yazı, yazıt, kitap"</p>
  <h1>Ortak Türk dili</h1>
  <p class="giris-metin">Bütün Türk topluluklarının birbirini anlamasını kolaylaştıracak, <b>öz ve eski
  Türkçe</b> köklere dayanan bir ortak dil çalışması. Her kelime Çuvaşçadan Sahacaya kırk dilde ve
  ağızlarında araştırılır, sekizinci yüzyıldan bugüne tanıklarıyla belgelenir.</p>
  <ul class="sayilar">
    <li><b>{s['kavram']}</b> kavram</li><li><b>{s['kok']}</b> tanıklı kök</li>
    <li><b>{s['tanik']}</b> tanık</li><li><b>{s['dil']}</b> dil</li><li><b>{s['kaynak']}</b> kaynak</li>
  </ul>
</section>
<section class="hedefler">
  <h2>Dört soru</h2>
  <div class="kartlar">
    <a class="kart" href="KARSILASTIRMA.html"><b>1. Ortak dil</b><span>Ne kadar çok farklı Türk topluluğu kullanıyor? Asıl ürün.</span></a>
    <a class="kart" href="KARSILASTIRMA.html"><b>2. Ana Türkçe</b><span>Kök soy ağacının ne kadar derinine iniyor? Türkçenin en eski hâli.</span></a>
    <a class="kart" href="KARSILASTIRMA.html"><b>3. En çok kişi</b><span>İkinci dil yoluyla da en çok kim anlıyor?</span></a>
    <a class="kart" href="sozluk/SOZLUK.html"><b>4. Tanıklı sözlük</b><span>Her kök nerede, ne zaman, nasıl ve hangi anlamda kullanılmış?</span></a>
  </div>
</section>
<section>
  <h2>Kavramlar</h2>
  <ul class="kavram-listesi">{satirlar}</ul>
  <p><a href="sozluk/SIRA.html">Çalışma sırası</a> · <a href="ILKELER.html">İlkeler</a> · <a href="GOZDEN-GECIRME.html">Gözden geçirme</a> ·
  <a href="proje.html">Proje</a></p>
</section>
"""


# ======================================================================= kur

def md_cevir(metin: str) -> str:
    md = markdown.Markdown(extensions=["tables", "fenced_code", "sane_lists", "toc"],
                           extension_configs={"toc": {"slugify": lambda v, s: slug(v, s)}})
    govde = md.convert(metin)
    # depo içi "üretilir; elle düzenlemeyin" notu sitede gereksiz
    govde = re.sub(r"<blockquote>\s*<p>[^<]*(?:<[^>]+>[^<]*)*?elle düzenlemeyin.*?</blockquote>\s*", "",
                   govde, count=1, flags=re.S)
    govde = re.sub(r"<table>", '<div class="tablo"><table>', govde)
    return govde.replace("</table>", "</table></div>")


def kur(cikti: Path):
    site = json.loads((KOK / "cikti" / "site.json").read_text(encoding="utf-8"))
    if cikti.exists():
        shutil.rmtree(cikti)
    (cikti / "varlik").mkdir(parents=True)
    sayfalar = {p["yol"] for p in site["sayfalar"]}
    for p in site["sayfalar"]:
        yol = p["yol"]
        metin = (KOK / yol).read_text(encoding="utf-8")
        govde = baglantilari_cevir(md_cevir(metin), yol, sayfalar)
        hedef = cikti / html_yolu(yol)
        hedef.parent.mkdir(parents=True, exist_ok=True)
        hedef.write_text(sayfa_html(p["baslik"], govde, yol, site, p["tur"]), encoding="utf-8")
    (cikti / "index.html").write_text(sayfa_html("Ortak Türk dili", ana_sayfa(site), "index.html", site, "ana"),
                                      encoding="utf-8")
    (cikti / "404.html").write_text(sayfa_html(
        "Bulunamadı", '<h1>Sayfa bulunamadı</h1><p>Aradığınız sayfa yok. Yukarıdaki aramayı deneyin ya da '
        '<a href="index.html">ana sayfaya</a> dönün.</p>', "404.html", site), encoding="utf-8")
    arama = [{**a, "yol": html_yolu(a["yol"].split("#")[0]) + ("#" + a["yol"].split("#")[1] if "#" in a["yol"] else "")}
             for a in site["arama"]]
    (cikti / "varlik" / "arama.json").write_text(json.dumps(arama, ensure_ascii=False), encoding="utf-8")
    for ad in ("site.css", "site.js"):
        shutil.copy(KOK / "araclar" / "site" / ad, cikti / "varlik" / ad)
    (cikti / ".nojekyll").write_text("", encoding="utf-8")
    print(f"{len(site['sayfalar']) + 2} sayfa → {cikti}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cikti", default=str(KOK / "_site"), help="çıktı klasörü (varsayılan: _site)")
    kur(Path(ap.parse_args().cikti))


if __name__ == "__main__":
    main()
