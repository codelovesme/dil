# dil: Ortak Türk Dili

Bütün Türk kavimlerinin birbirini anlamasını kolaylaştıracak, **öz ve eski
Türkçe** kelimelere dayanan ortak bir dil oluşturma çalışması.

Aynı veriden beş soruya cevap aranır; her birinin kendi ölçüsü vardır. İlk üçü kelime seçer, dördüncüsü kökün bütün tanıklarını belgeler, beşincisi veriyi çeviride kullanır:

| Hedef | Soru | Ölçü |
|---|---|---|
| **1. Ortak dil** (asıl ürün) | Ortak kelime: ne kadar çok farklı grup kullanıyor? | Yaygınlık; gruplar etiketle değil örgüdeki benzerlikle belirlenir |
| **2. Ana Türkçe tahmini** | Türkçenin en eski hâli neydi? | Kök yaşı: kök soy ağacının hangi düğümüne kadar gidiyor |
| **3. En çok kişinin anladığı** | En fazla insan anlasın | Anlayan kişi sayısı (ikinci dil dahil) |
| **4. Tanıklı sözlük** | Her kök nerede, ne zaman, nasıl, hangi anlamda kullanılmış? | Kapsam: diller, ağızlar, tarihî duraklar, kaynaklar |
| **5. Çeviri** | Bir metni Türk dilleri, ağızları ve ortak dil arasında ne kadar iyi çevirebiliyoruz? | Çeviri kalitesi (chrF), dil çifti başına; plan: [uygulama/CEVIRI.md](uygulama/CEVIRI.md) |

Her kelimenin her adayı için üç ölçü yan yana gösterilir. Üç hedefin aynı kökü
seçtiği kelimeler sağlamdır; ayrıştıkları kelimeler tartışmaya açılır:
**[KARSILASTIRMA.md](KARSILASTIRMA.md)**.

- Diller iki yapıda tutulur: **soy ağacı** (hangi dil hangisinden geliyor) ve
  **örgü** (diller arasındaki ağırlıklı anlaşılırlık, ikinci dil ve temas
  bağları). Bir dil soyca tek bir dalın altındadır, ama örgüde birçok dile
  bağlanabilir.
- Hesap **alttan yukarı** gösterilir. Ağızlar birleşip dili, diller dalı, dallar
  kolu, kollar en tepeyi oluşturur. Her birleşim "burada ne olmalı?" sorusuna
  kendi cevabını verir. Örneğin Oğuz kolunda *dağ*, Kıpçak kolunda *taw*, en
  tepede *tağ* çıkar.
- Alıntılar üç hedefte de hiçbir koşulda seçilmez.

Ayrıntılar: **[ILKELER.md](ILKELER.md)**

Site: bütün çıktılar her `main` güncellemesinde statik bir siteye dönüşüp GitHub
Pages'te yayınlanır (alan adı ileride `bitig.codeloves.me`).

## Yapı

```
ILKELER.md          kriterler ve kurallar
hedefler.yaml       beş hedefin ayarları (sözlüğün tarihî durakları dahil)
agac.yaml           soy ağacı: 40 dil, 89 ağız, konuşur sayıları
ag.yaml             örgü: anlaşılırlık, ikinci dil ve temas bağları (tahmini)
tarihi.yaml         tarihî tanıklar (Eski Türkçe, Karahanlıca, Kuman-Kıpçakça…)
AGIRLIKLAR.md       üç hedefin ağırlık tabloları (üretilir)
KARSILASTIRMA.md    her kavram için üç hedefin seçimi (üretilir)
ORGU.md             örgünün veriden denetimi (araclar/orgu.py --yaz ile üretilir)
GOZDEN-GECIRME.md   büyük gözden geçirme raporu (yöntem sürüm 1)
kaynaklar/          kaynak sözlüğü: ~170 kaynak, ihtiyaca ve dile göre (KAYNAKLAR.md)
sozluk/SIRA.md      kelimelerin çalışma sırası (sıklığa göre)
sozluk/temel/       temel söz varlığı: her kavram için bir dosya (seçim)
sozluk/kok/         tanıklı sözlük: her kök için tanıklar (.yaml) ve okunur sayfa (.md)
sozluk/SOZLUK.md    sözlük dizini ve kapsam tablosu (üretilir)
araclar/sozluk.py   sözlük: doğrulama, kapsam, sayfa üretimi
araclar/puanla.py   puanlama ve ağaç üzerinde seçim
araclar/ceviri_veri.py  Hedef 5: Tatoeba'dan ölçüm seti seçer (ceviri/olcu/)
araclar/ceviri_olc.py   Hedef 5: chrF ölçümü; --kopya ile çevirisiz taban çizgisi
araclar/yazim.py    yazıları çalışma yazımına aktarır (Kiril, Latin, Uygur)
araclar/orgu.py     örgüyü veriden ölçer, ag.yaml'daki boşlukları doldurur (gözden geçirmelerde)
araclar/yayinla.py  bütün okunur çıktılar: kavram ve kök sayfaları, dizinler, cikti/site.json
araclar/site.py     statik site (GitHub Pages; .github/workflows/site.yml)
uygulama/PLAN.md    bitig.codeloves.me: site planı ve ileride Euglena uygulamaları
.claude/skills/kelime-arastir/   bir kelimeyi araştırma yöntemi ve şablon
```

Yeni kelime eklemek için Claude'a "*göz kelimesini araştır*" demek yeterli.
Araştırma `kelime-arastir` yöntemine göre yapılır.

## Kullanım

```bash
pip install -r requirements.txt

python3 araclar/puanla.py                     # bütün kavramlar (asıl hedef: ortak dil)
python3 araclar/puanla.py buyuk --derinlik 3  # tek kavram, ilk 3 seviye
python3 araclar/puanla.py su --agizlar        # ağızlar dahil
python3 araclar/puanla.py buyuk --hedef ana   # başka hedef: ortak | ana | nufus
python3 araclar/puanla.py --karsilastir       # üç hedef yan yana
python3 araclar/puanla.py --agirliklar --hedef nufus   # bir hedefin ağırlıkları

python3 araclar/sozluk.py                     # sözlük: bütün köklerin kapsamı
python3 araclar/sozluk.py ben                 # tek kök: eksik duraklar ve diller
python3 araclar/sozluk.py --denetle           # kök dosyaları ile kavram dosyaları uyumlu mu
python3 araclar/sozluk.py --yaz               # sozluk/kok/*.md ve sozluk/SOZLUK.md üret

python3 araclar/yayinla.py                    # bütün okunur çıktıları üret (sayfalar + cikti/site.json)
python3 araclar/yayinla.py --denetle          # çıktılar güncel mi (CI de bunu çalıştırır)
python3 araclar/site.py                       # statik siteyi _site/ altına kur

# üretilen dosyaları yenile
python3 araclar/puanla.py --agirliklar --md > AGIRLIKLAR.md
python3 araclar/puanla.py --karsilastir --md > KARSILASTIRMA.md
```

Örnek ("dağ", alttan yukarı):

```
Türk dilleri                         tağ      ← ortak dil
  Oğur kolu                          tu
  Ortak Türkçe                       tağ
    Oğuz kolu                        dağ
    Kıpçak kolu                      taw
    Karluk kolu                      tağ
    Sibirya kolu                     tağ
      Kuzey Sibirya                  xaya     ← farklı kök: kaya
```

## Yol haritası

- [x] Aşama 0: İlkeler, dil ve ağız ağacı, ağırlıklar, puanlama aracı
- [ ] Aşama 1: Temel söz varlığı (~200 kavram, Swadesh + Leipzig-Jakarta listeleri)
- [ ] Aşama 2: Ses ve yazım kuralları, ortak alfabe
- [ ] Aşama 3: Dilbilgisi (ekler, çekim, söz dizimi)
- [ ] Aşama 4: Konulara göre genişletme, eski köklerden yeni kelime türetme
- [ ] Aşama 5: Örnek metinler, karşılıklı anlaşılırlık denemeleri

> **Not:** `sozluk/` altındaki veriler şimdilik örnektir ve `dogrulandi: false`
> olarak işaretlidir. Kaynaklarla kontrol edilmeden kesin kabul edilmemelidir.
