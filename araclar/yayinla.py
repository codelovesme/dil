#!/usr/bin/env python3
"""Bütün okunur çıktıları tek komutla üretir (site bunlardan kurulur).

Kullanım:
    python3 araclar/yayinla.py              # bütün çıktıları yaz
    python3 araclar/yayinla.py --denetle    # çıktılar veriyle güncel mi? (değilse çıkış kodu 1)

Üretilenler:
    sozluk/temel/<kavram>.md   kavram sayfası: dört hedef, adaylar, ağaç üzerinde seçimler, biçimler
    sozluk/kok/<kök>.md        sözlük maddesi (araclar/sozluk.py)
    sozluk/SOZLUK.md           sözlük dizini ve kapsam
    sozluk/KAVRAMLAR.md        kavram dizini
    KARSILASTIRMA.md           hedeflerin karşılaştırması
    AGIRLIKLAR.md              dil ağırlıkları
    kaynaklar/KAYNAKLAR.md     kaynak sözlüğü
    cikti/site.json            sayfa listesi ve arama dizini
"""
from __future__ import annotations

import argparse
import contextlib
import io
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kaynaklar as kaynak_araci  # noqa: E402
import puanla as P  # noqa: E402
import sozluk as S  # noqa: E402

KOK = P.KOK_DIZIN
URETILDI = "> Bu sayfa `python3 araclar/yayinla.py` ile üretilir; elle düzenlemeyin."


def _h(s) -> str:
    return str(s or "").replace("|", "\\|").replace("\n", " ").strip()


def _yuzde(x: float) -> str:
    return f"%{100 * x:.0f}"


# ============================================================ kavram sayfası

def kavram_md(kv, agac, hedefler, b: S.Baglam, kok_dosyalari: set[str]) -> str:
    h1, h2, h3 = (P._hedef(hedefler, y) for y in ("kopru", "yas", "kisi"))
    secimler = P.hedef_secimleri(kv, agac, hedefler)
    y: list[str] = [f"# {kv.ad}\n", URETILDI + f" Veri: [`{kv.yol.name}`]({kv.yol.name}).\n"]
    y.append(f"- **Anlam:** {_h(kv.v.get('anlam', '')) if hasattr(kv, 'v') else ''}".rstrip())
    y.append(f"- **İngilizce:** {kv.ingilizce}")
    y.append(f"- **Durum:** {'kaynakla doğrulandı' if kv.dogrulandi else 'henüz kaynakla doğrulanmadı'}")
    y.append(f"- **Veri kapsaması:** {_yuzde(P.kapsama(agac, kv, h1))} (Hedef 1 ağırlığıyla) · "
             f"**Tarihî tanık:** {len(kv.bilinen_taniklar)}/{len(h1.taniklar)}")
    y.append("")

    def kok_bag(kimlik: str) -> str:
        return f"[{kimlik}](../kok/{kimlik}.md)" if kimlik in kok_dosyalari else kimlik

    y.append("## Dört hedef\n")
    y.append("| Hedef | Soru | Seçim | Kök |")
    y.append("|---|---|---|---|")
    for i, (kod, s) in enumerate(secimler.items(), 1):
        h = hedefler[kod]
        y.append(f"| {i}. {h.ad} | {_h(h.soru)} | **{s.bicim}** | {kok_bag(s.kok.kimlik)} |")
    kokler4 = [k for k in kv.kokler if k.kimlik in kok_dosyalari]
    if kokler4:
        bag = ", ".join(f"[{k.kimlik}](../kok/{k.kimlik}.md) (seviye "
                        f"{S.Kapsam(S.Madde(S.KOK_DIZIN / (k.kimlik + '.yaml'), b), b).seviye})"
                        for k in kokler4)
        y.append(f"| 4. Tanıklı sözlük | {_h(b.hedef.get('soru'))} | — | {bag} |")
    y.append(f"\nİlk üç hedef **{P.uyum(secimler).lower()}**.\n")

    y.append("## Adaylar ve ölçüler\n")
    y.append("| Kök | Köken | 1. Yaygınlık | En az anlayan büyük topluluk | 2. Kök yaşı | "
             "3. Anlayan kişi | Ana Türkçe |")
    y.append("|---|---|---|---|---|---|---|")
    uyarilar = []
    for k, o in P.aday_olculeri(kv, agac, hedefler):
        if o is None:
            y.append(f"| {kok_bag(k.kimlik)} | {k.koken} | seçilemez | | | | {_h(k.ana_turkce)} |")
            continue
        dusuk = f"{P._kisa_ad(o['en_dusuk'][0])} {_yuzde(o['en_dusuk'][1])}" if o["en_dusuk"] else ""
        oran = o["kisi"] / o["bilinen"] if o["bilinen"] else 0
        y.append(f"| {kok_bag(k.kimlik)} | {k.koken} | {o['p1']:.2f} (*{o['b1']}*) | {dusuk} | "
                 f"{o['yas']} | ~{o['kisi'] / 1e6:.0f} milyon ({_yuzde(oran)}, *{o['b3']}*) | "
                 f"{_h(k.ana_turkce)} |")
        for L, veren in o["supheli"]:
            uyarilar.append(f"{L.ad}'daki *{k.kimlik}* biçimi {h2.dil[veren].ad}'dan ödünç olabilir; "
                            "kök yaşında sayılmadı.")
    secim = secimler[h1.kod]
    if h1.esik is not None and (P.yayilim(agac, secim.kok, kv, h1) or 0) < h1.esik:
        uyarilar.append(f"**Canlandırma:** *{secim.kok.kimlik}* bugün dillerin ağırlıkça yarısından "
                        "azında yaşıyor; öğretilmesi gerekecek.")
    if uyarilar:
        y.append("")
        y.extend(f"- ⚠ {u}" for u in uyarilar)
    _, degerler = P.taban_acigi(agac, secim.kok, secim.bicim, kv, h1)
    if degerler:
        y.append(f"\n**Büyük topluluklarda *{secim.bicim}* biçiminin anlaşılırlığı:** "
                 + ", ".join(f"{P._kisa_ad(L)} {_yuzde(v)}" for L, v in degerler) + ".\n")

    # alttan yukarı: üç hedefin ağaçtaki seçimleri yan yana
    y.append("## Ağaç üzerinde seçimler\n")
    y.append("Her düğüm yalnız kendi altına bakarak seçer. *İtalik*: farklı kök; "
             "**↑**: bu düğümde Türkçe aday yok, üstten alındı (canlandırma).\n")
    y.append(f"| Düğüm | {h1.ad} | {h2.ad} | {h3.ad} | Günlük kullanım |")
    y.append("|---|---|---|---|---|")

    def hucre(s, ust) -> str:
        if s.miras:
            return f"{s.bicim} ↑"
        if ust is not None and s.kok is not ust.kok:
            return f"*{s.bicim}* ({s.kok.kimlik})"
        return s.bicim

    def yuru(ss, usts, derinlik):
        d = ss[0].dugum
        if d.dil_ici and not d.yazi_dili and not any(c in kv.bilinen_diller for c in d.yaprak_kodlari):
            return
        ad = "Yazı dili" if d.yazi_dili else d.ad
        girinti = "&nbsp;&nbsp;" * derinlik + ("**" + ad + "**" if derinlik <= 1 else ad)
        gunluk = ss[0].gunluk or ""
        y.append(f"| {girinti} | " + " | ".join(hucre(s, u) for s, u in zip(ss, usts))
                 + f" | {gunluk} |")
        for i in range(len(ss[0].alt)):
            yuru([s.alt[i] for s in ss], ss, derinlik + 1)

    yuru([secimler[h.kod] for h in (h1, h2, h3)], [None, None, None], 0)
    y.append("")

    # dillerdeki biçimler
    y.append("## Dillerdeki biçimler\n")
    basliklar = [k.kimlik + ("" if k.secilebilir else f" ({k.koken})") for k in kv.kokler]
    y.append("| Kol | Dil | Ağız | " + " | ".join(basliklar) + " |")
    y.append("|---|---|---|" + "---|" * len(kv.kokler))
    for L in agac.diller:
        kodlar = [L.kod] + sorted(L.yaprak_kodlari - {L.kod}, key=lambda c: b.sira.get(c, 999))
        for c in kodlar:
            hucreler = []
            for k in kv.kokler:
                bc = k.bicimler.get(c)
                if bc is None:
                    hucreler.append("")
                    continue
                ek = []
                if bc.tercih < 1:
                    ek.append(f"tercih {bc.tercih:g}")
                if bc.odunc:
                    ek.append(f"ödünç: {bc.odunc}")
                hucreler.append(bc.bicim + (f" ({', '.join(ek)})" if ek else ""))
            if not any(hucreler):
                continue
            agiz = "" if c == L.kod else b.ad.get(c, c)
            y.append(f"| {L.kol.ad if L.kol else ''} | {L.ad} | {agiz} | " + " | ".join(hucreler) + " |")
    if kv.bilinen_diller - {c for k in kv.kokler for c in k.bicimler}:
        yok = sorted(kv.bilinen_diller - {c for k in kv.kokler for c in k.bicimler})
        y.append(f"\nAraştırılıp hiçbir aday kökün bulunmadığı: {', '.join(b.ad.get(c, c) for c in yok)}.")
    tarihi = {t.kod: t for t in h1.taniklar}
    satirlar = [(t, k) for t in h1.taniklar for k in kv.kokler if t.kod in k.tarihi]
    if satirlar:
        y.append("\n**Tarihî tanıklar:** " + "; ".join(
            f"{t.kisa} *{k.tarihi[t.kod]}*" for t, k in satirlar) + ".")
    del tarihi
    y.append("")
    return "\n".join(y) + "\n"


def kavramlar_md(kavramlar, agac, hedefler) -> str:
    y = ["# Kavramlar\n", URETILDI + "\n",
         "Her kavramın sayfasında dört hedefin seçimi, adaylar ve ölçüleri, ağaç üzerindeki "
         "seçimler ve dillerdeki biçimler var. Çalışma sırası: [SIRA.md](SIRA.md).\n"]
    sutunlar = [h for h in hedefler.values()]
    y.append("| Kavram | İngilizce | " + " | ".join(h.ad for h in sutunlar) + " | Durum |")
    y.append("|---|---|" + "---|" * len(sutunlar) + "---|")
    for kv in kavramlar:
        s = P.hedef_secimleri(kv, agac, hedefler)
        yol = kv.yol.relative_to(KOK / "sozluk").with_suffix(".md").as_posix()
        y.append(f"| [{kv.ad}]({yol}) | {kv.ingilizce} | "
                 + " | ".join(f"**{s[h.kod].bicim}**" for h in sutunlar) + f" | {P.uyum(s).lower()} |")
    return "\n".join(y) + "\n"


# ================================================================ site.json

def _baslik(metin: str, yedek: str) -> str:
    for satir in metin.splitlines():
        if satir.startswith("# "):
            return satir[2:].strip()
    return yedek


def site_json(ciktilar: dict[Path, str], kavramlar, agac, hedefler, b, maddeler) -> str:
    sabit = [("README.md", "Proje", "proje"), ("ILKELER.md", "İlkeler", "ilke"),
             ("sozluk/SIRA.md", "Çalışma sırası", "dizin")]
    sayfalar = []
    for yol, baslik, tur in sabit:
        sayfalar.append({"yol": yol, "baslik": baslik, "tur": tur})
    turler = {"sozluk/temel": "kavram", "sozluk/kok": "kok"}
    for p, metin in sorted(ciktilar.items()):
        if p.suffix != ".md":
            continue
        rel = p.relative_to(KOK).as_posix()
        tur = next((v for k, v in turler.items() if rel.startswith(k + "/")), "dizin")
        sayfalar.append({"yol": rel, "baslik": _baslik(metin, p.stem), "tur": tur})

    arama = []
    for kv in kavramlar:
        s = P.hedef_secimleri(kv, agac, hedefler)
        yol = kv.yol.relative_to(KOK).with_suffix(".md").as_posix()
        bicimler = sorted({bc.bicim for k in kv.kokler for bc in k.bicimler.values()}
                          | {v for k in kv.kokler for v in k.tarihi.values()})
        arama.append({"t": "kavram", "ad": kv.ad, "alt": kv.ingilizce, "yol": yol,
                      "ozet": " · ".join(f"{hedefler[h].ad}: {x.bicim}" for h, x in s.items()),
                      "anahtar": bicimler})
    for m in maddeler:
        yol = m.yol.with_suffix(".md").relative_to(KOK).as_posix()
        arama.append({"t": "kok", "ad": m.kok, "alt": str(m.v.get("anlam", "")), "yol": yol,
                      "ozet": f"{len(m.taniklar)} tanık, en eski {S.yuzyil_yaz((S.Kapsam(m, b).ilk,) * 2)}",
                      "anahtar": sorted({t.bicim for t in m.taniklar}
                                        | {str(t.alan.get('yazi')) for t in m.taniklar if t.alan.get('yazi')})})
    for k in b.kaynaklar.values():
        arama.append({"t": "kaynak", "ad": k["ad"], "alt": k["kimlik"],
                      "yol": f"kaynaklar/KAYNAKLAR.md#{k['kimlik']}",
                      "ozet": " ".join(str(k.get("ne", "")).split())[:160], "anahtar": []})
    for L in agac.diller:
        arama.append({"t": "dil", "ad": L.ad, "alt": L.kod, "yol": "AGIRLIKLAR.md",
                      "ozet": f"{L.kol.ad if L.kol else ''}, ~{L.konusur:,} konuşur".replace(",", "."),
                      "anahtar": sorted(L.yaprak_kodlari)})
    veri = {"ad": "Bitig", "aciklama": "Ortak Türk dili: öz Türkçe kökler, tanıklı sözlük ve kaynaklar",
            "sayilar": {"kavram": len(kavramlar), "kok": len(maddeler),
                        "tanik": sum(len(m.taniklar) for m in maddeler), "kaynak": len(b.kaynaklar),
                        "dil": len(agac.diller)},
            "sayfalar": sayfalar, "arama": arama}
    return json.dumps(veri, ensure_ascii=False, indent=1) + "\n"


# ================================================================== üret

def _yakala(fn, *args) -> str:
    tampon = io.StringIO()
    with contextlib.redirect_stdout(tampon):
        fn(*args)
    return tampon.getvalue()


def uret() -> dict[Path, str]:
    """Bütün çıktılar: yol → içerik. Hiçbir şey yazmaz."""
    agac = P.agac_yukle()
    ag = P.Ag(agac)
    taniklar = P.taniklari_yukle(agac)
    hedefler = P.hedefleri_yukle(taniklar, agac, ag)
    kavramlar = P.kavramlari_yukle([], agac, taniklar)
    for kv in kavramlar:   # puanla.Kavram anlamı tutmuyor; sayfa için ham veriyi oku
        kv.v = P.yaml.safe_load(kv.yol.read_text(encoding="utf-8"))
    b = S.Baglam()
    maddeler = S.maddeleri_yukle(b, [])
    kok_dosyalari = {m.kok for m in maddeler}

    c: dict[Path, str] = {}
    for kv in kavramlar:
        c[kv.yol.with_suffix(".md")] = kavram_md(kv, agac, hedefler, b, kok_dosyalari)
    c[KOK / "sozluk" / "KAVRAMLAR.md"] = kavramlar_md(kavramlar, agac, hedefler)
    for m in maddeler:
        c[m.yol.with_suffix(".md")] = S.madde_md(m, b)
    c[S.DIZIN_DOSYASI] = S.dizin_md(maddeler, b)

    c[KOK / "KARSILASTIRMA.md"] = _yakala(P.karsilastirma_raporu, kavramlar, agac, hedefler, True)
    agirlik = io.StringIO()
    with contextlib.redirect_stdout(agirlik):
        print("# Ağırlıklar\n")
        print("> Bu dosya `python3 araclar/puanla.py --agirliklar --md > AGIRLIKLAR.md` komutuyla "
              "üretilir; elle düzenlemeyin. Her hedef kendi ölçüsünü kullanır "
              "(bkz. `hedefler.yaml`, ILKELER.md §1). Bir dilin içinde yazı dili %50, "
              "ağızlar kalan %50'yi paylaşır (Hedef 1 ve 3).\n")
        for x in hedefler.values():
            P.agirlik_raporu(agac, x, True)
    c[KOK / "AGIRLIKLAR.md"] = agirlik.getvalue()
    veri, kodlar = kaynak_araci.yukle()
    c[KOK / "kaynaklar" / "KAYNAKLAR.md"] = kaynak_araci.md(veri, kodlar) + "\n"

    c[KOK / "cikti" / "site.json"] = site_json(c, kavramlar, agac, hedefler, b, maddeler)
    return c


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--denetle", action="store_true", help="yazma; eski çıktı varsa listele ve 1 ile çık")
    a = ap.parse_args()
    ciktilar = uret()
    eski = [p for p, metin in ciktilar.items()
            if not p.exists() or p.read_text(encoding="utf-8") != metin]
    if a.denetle:
        if eski:
            print("Güncel olmayan çıktılar (python3 araclar/yayinla.py ile yenileyin):")
            for p in eski:
                print("  " + p.relative_to(KOK).as_posix())
            sys.exit(1)
        print(f"{len(ciktilar)} çıktı güncel.")
        return
    for p in eski:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(ciktilar[p], encoding="utf-8")
    print(f"{len(ciktilar)} çıktı, {len(eski)} tanesi yenilendi.")


if __name__ == "__main__":
    main()
