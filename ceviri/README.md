# Çeviri (Hedef 5)

Plan: [uygulama/CEVIRI.md](../uygulama/CEVIRI.md). İlke: [ILKELER.md §16](../ILKELER.md).

## Ölçüm setleri

`olcu/tatoeba/<dil1>-<dil2>.tsv`: Tatoeba'dan seçilmiş paralel cümleler. Sütunlar
şunlardır: iki dilin cümle kimliği ve cümlesi, `yol` (`dogrudan`: iki cümle Tatoeba'da
doğrudan birbirinin çevirisi; `eng`: İngilizce bir cümle üzerinden bağlı, daha gevşek).
Özet: [`olcu/tatoeba/OZET.tsv`](olcu/tatoeba/OZET.tsv).

- **Kaynak ve lisans:** [Tatoeba](https://tatoeba.org), CC BY 2.0 FR. Her cümle
  kimliğiyle tutulur; yazarı ve geçmişi `https://tatoeba.org/sentences/show/<kimlik>`
  adresindedir.
- **Seçim:** `python3 araclar/ceviri_veri.py <indirme_klasörü>`. Kurallar aracın
  başında yazılıdır (kısa/uzun cümleler ve tekrarlar atılır, çift başına en çok
  200 cümle, seçim belirlenimci).
- **Sınırlar:** Tatoeba cümleleri kısa ve günlüktür; çoğu Türkiye Türkçesi ya da
  İngilizceden çevrilmiştir. Bu yüzden diller arası benzerliği olduğundan yüksek
  gösterebilir. Uzun metin ölçümü için ikinci bir set (FLORES+) gerekir.

## Ölçüm

`python3 araclar/ceviri_olc.py`: chrF (karakter 1–6 gram, β = 2). İki taraf önce
çalışma yazımına aktarılır (`araclar/yazim.py`), böylece Kiril ve Latin yazılı aynı
metin aynı sayılır.

- **Kopya taban çizgisi:** [KOPYA.md](KOPYA.md). Kaynak cümle hiç çevrilmeden
  hedefin referansıyla karşılaştırılır. Bir çeviri motoru bu değerin belirgin
  üstünde olmalıdır.
