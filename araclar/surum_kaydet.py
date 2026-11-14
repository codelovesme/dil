#!/usr/bin/env python3
"""İndirilen kaynak dosyalarının sürüm kaydı (kaynaklar/surumler.yaml).

Her kaynak için indirme tarihi, adres kalıbı ve her dosyanın SHA-256 parmak izi
tutulur. Bir kaynakta sonradan hata bulunursa hangi dosyayı kullandığımız tam
olarak bilinir; aynı dosya yeniden indirilip karşılaştırılabilir.

  python3 araclar/surum_kaydet.py --kaynak apertium --tarih 2026-11-14 \\
      --adres "raw.githubusercontent.com/apertium/apertium-<dil>/master/" DOSYA...
"""
import argparse, hashlib, os
from pathlib import Path
import yaml

KOK = Path(__file__).resolve().parent.parent
YOL = KOK / "kaynaklar" / "surumler.yaml"

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("--kaynak", required=True); ap.add_argument("--tarih", required=True); ap.add_argument("--adres", required=True)
ap.add_argument("dosyalar", nargs="+")
a = ap.parse_args()
v = yaml.safe_load(YOL.read_text(encoding="utf-8")) if YOL.exists() else {}
v = v or {}
dosyalar = {}
for f in sorted(a.dosyalar):
    h = hashlib.sha256(open(f, "rb").read()).hexdigest()
    dosyalar[os.path.basename(f)] = {"sha256": h, "bayt": os.path.getsize(f)}
v.setdefault(a.kaynak, [])
v[a.kaynak] = [s for s in v[a.kaynak] if s.get("tarih") != a.tarih] + [{"tarih": a.tarih, "adres": a.adres, "dosyalar": dosyalar}]
YOL.write_text("# Kaynak dosyalarının sürüm kaydı — araclar/surum_kaydet.py ile yazılır.\n"
               + yaml.safe_dump(v, allow_unicode=True, sort_keys=True, width=200), encoding="utf-8")
print(f"{a.kaynak}: {len(dosyalar)} dosya kaydedildi")
