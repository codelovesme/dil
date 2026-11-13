# Hedef 5: Çeviri — plan

> Durum (2026-11-13): plan onaylandı. Aşama 1 (ölçüm seti) başladı.

## Amaç

40 Türk dili, onların ağızları ve ileride **ortak dil** arasında çeviri:
tek cümleden sayfalarca metne kadar. Sonra sesli çeviri (konuşma → metin →
çeviri → konuşma).

Öbür hedeflerden farkı şudur:
- Hedef 1–3 bir kelime *seçer*, Hedef 4 *derler*.
- Hedef 5 ise bu verinin *kullanımıdır*. O yüzden puanlamaya değil, kendi
  ölçüsüne dayanır: çeviri kalitesi. Ayrıntı [ILKELER.md §16](../ILKELER.md).

## Kararlar (2026-11-13)

| Konu | Karar |
|---|---|
| Python araçları | **Kalır.** Sözlüğün derleyicisidir: veriyi denetler, puanlar, JSON üretir. Uygulama yalnız bu çıktıları okur |
| Uygulama | Euglena (my-euglena-apps): arayüz, API, çeviri işçisi; sonra ses |
| Motor | **Karma.** Büyük yazı dillerinde LLM (Claude) + bizim sözlük bağlamımız; küçük diller ve ağızlarda kural katmanı; açık modeller (NLLB, MMS) yedek ve karşılaştırma olarak |
| Dilbilgisi | **Öne alındı.** Ekler, çekim ve ses denklikleri çeviri ve ağız dönüşümü için gerekli |
| İlk kapsam | Türkiye, Azerbaycan, Kazak, Özbek, Tatar, Uygur arasında metin çevirisi |

## Mimari

```
 bitig deposu (Python, derleyici)                      my-euglena-apps
 ───────────────────────────────                       ───────────────
 sozluk/ (kavram, kök)      ──┐
 dilbilgisi/ (ekler, çekim) ──┼─ yayinla.py ─▶ cikti/*.json ─▶ bitig-worker ─▶ Mongo
 ceviri/olcu/ (test setleri) ─┘                                     │
                                                                   ▼
 tarayıcı ── bitig-web (metin kutusu, dil seçici, belge) ── bitig-api ── bitig-ceviri (işçi)
                                                                        │  LLM / açık model
                                                                        │  + sözlük bağlamı
                                                                        │  + kural katmanı
                                                                        ▼
                                                              Mongo (işler, önbellek, düzeltmeler)
                                                              Azurite (belgeler, ses)
```

## Motorun katmanları

1. **Bölme.** Metin paragraf ve cümlelere bölünür. Uzun metin arka planda
   işlenir; sonuç parça parça gelir.
2. **Terim sözlüğü.**
   - Metindeki kelimeler bizim sözlükte aranır ve kaynak dildeki kök hedef
     dildeki karşılığa eşlenir.
   - Bu liste motora bağlam olarak verilir; böylece metin boyunca aynı
     kelime aynı karşılıkla çevrilir.
3. **Çeviri.**
   - Büyük yazı dilleri: LLM'e kaynak metin, terim listesi ve hedef dilin
     kısa dilbilgisi notu verilir.
   - Açık model (NLLB-200) aynı cümlelerde karşılaştırma için çalıştırılır.
4. **Kural katmanı (küçük diller ve ağızlar).**
   - Model verisi olmayan dile önce en yakın yazı diline çevrilir. Yakınlık
     örgüye göre seçilir (`ag.yaml`).
   - Sonra o dilden hedefe bizim verimizle dönüştürülür: kelime karşılıkları
     (kök dosyalarındaki tanıklar), ses denklikleri ve ek tabloları.
   - Örnek: Tatarca → Baraba ağzı, Türkiye Türkçesi → Ege ağzı. Apertium'un
     Türk dilleri için açık kural sözlükleri temel alınabilir.
5. **Ortak dil.** Hedef 1'in seçtiği kökler ve sürüm 2'de karara bağlanacak
   ses ve biçim kurallarıyla. Dilbilgisi aşaması bitmeden ortak dile tam
   çeviri yapılamaz.

## Ölçü

Motor ölçmeden seçilmez; her dil çiftinin kalitesi açıkça yazılır.

- **Test setleri** (`ceviri/olcu/`):
  - Tatoeba cümleleri (CC BY): Türkiye, Azerbaycan, Kazak, Özbek, Tatar,
    Uygur, Başkurt, Kırgız, Türkmen, Kırım Tatar, Çuvaş, Saha, Gagauz…
  - FLORES+ (yaklaşık 10 Türk dili, aynı 1012 cümle; erişim için Hugging Face
    anahtarı gerekir).
  - Küçük diller için kaynaklardaki örnek cümlelerden kendi setimiz.
- **Ölçüler:** chrF (karakter tabanlı, eklemeli dillerde BLEU'dan uygun),
  küçük örnekler üzerinde insan değerlendirmesi.
- **Etiket:** her dil çifti sitede "iyi / deneysel / yok" diye gösterilir.
- **Düzeltmeler:** kullanıcının düzelttiği çeviriler Mongo'da toplanır ve
  ölçüm setine eklenebilir.

## Ses (sonra)

- Konuşmadan yazıya: Whisper (Türkiye, Azerbaycan, Kazak, Özbek, Tatar,
  Başkurt, Türkmen, Uygur), Meta MMS (pek çok küçük Türk dili).
- Yazıdan konuşmaya: MMS-TTS.
- Kalite yine dil dil ölçülür.

## Aşamalar

| Aşama | Nerede | Teslim | Bitti sayılması için |
|---|---|---|---|
| **1. Ölçüm seti** | bitig | `ceviri/olcu/`: Tatoeba'dan dil çifti başına test cümleleri, künye ve lisans; `araclar/ceviri_olc.py` (chrF) | 6 ilk dil için her çiftte en az 100 cümle; ölçüm aracı örnek bir çıktıyı puanlıyor |
| **2. Dilbilgisi verisi** | bitig | `sozluk/ek/`: ekler kavram gibi tutulur (biçimler kök dosyalarında tanık), üç hedef ortak dilin ekini de seçer; sıra: [SIRA.md §12](../sozluk/SIRA.md) | İsim ve fiil çekiminin temel ekleri 40 dilde; ortak dilin ek taslağı KARSILASTIRMA'da |
| **3. Terim sözlüğü çıktısı** | bitig | `cikti/sozluk.json`: kavram → dil → biçimler (çekim tabanı) | İşçi bir cümlenin terim listesini çıkarabiliyor |
| **4. İlk motor** | bitig + my-euglena-apps | bitig-ceviri işçisi (LLM + terim listesi), API `Cevir { kaynak, hedef, metin }` | 6 dil arasında ölçüm seti puanlanıyor; sonuçlar raporda |
| **5. Arayüz** | my-euglena-apps | bitig-web'de çeviri sayfası, belge yükleme, kalite etiketi | Gerçek tarayıcıda bir sayfalık metin çevriliyor |
| **6. Küçük diller ve ağızlar** | ikisi | Kural katmanı | Seçilen 3 ağız ve 3 küçük dil için ölçülü sonuç |
| **7. Ses** | my-euglena-apps | ASR → çeviri → TTS | İlk 6 dilde sesli çeviri |

## Gerekenler (sahipten)

- **Ağ izni:** `downloads.tatoeba.org` (Aşama 1). FLORES+ için `huggingface.co`
  ve bir Hugging Face anahtarı.
- **LLM anahtarı** (Aşama 4): işçinin Claude API'sini çağırması için.
- **my-euglena-apps deposu** bu çalışmaya eklenmeli (Aşama 4).
