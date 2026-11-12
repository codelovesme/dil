# dil: Ortak Türk Dili

Bütün Türk kavimlerinin birbirini anlamasını kolaylaştıracak, **öz ve eski
Türkçe** kelimelere dayanan ortak bir dil oluşturma çalışması.

Aynı veriden üç hedefe cevap aranır:

| Hedef | Soru | Ağırlık |
|---|---|---|
| **1. Ortak dil** (asıl ürün) | Bütün Türk kavimleri birbirini anlasın | Ağaç + büyüklük basamağı |
| **2. Ana Türkçe tahmini** | Türkçenin en eski hâli neydi? | Soy: her ayrılıkta dallar eşit |
| **3. En çok kişinin anladığı** | En fazla insan anlasın | Konuşur sayısı |

Üç hedefin aynı kökü seçtiği kelimeler sağlamdır; ayrıştıkları kelimeler
tartışmaya açılır: **[KARSILASTIRMA.md](KARSILASTIRMA.md)**.

- Kelimeler **Türk dilleri ağacı** üzerinde seçilir. Asıl hedefte kişi sayısı
  sadece büyüklük basamağı olarak sayılır (her 10 kat = +1 puan). Böylece
  hiçbir topluluk, kalabalığıyla ya da içindeki dil veya ağız sayısıyla
  diğerlerini ezemez.
- Hesap **alttan yukarı** yapılır. Ağızlar birleşip dili, diller dalı, dallar
  kolu, kollar ortak dili oluşturur. Her birleşim "burada ne olmalı?" sorusuna
  kendi cevabını verir. Örneğin Oğuz kolunda *dağ*, Kıpçak kolunda *taw*, en
  tepede *tağ* çıkar.
- Ölçüler: **anlaşılırlık** (biçim ne kadar tanıdık), **eskilik** (tarihî
  metinlerde var mı), **yayılım** (kök ne kadar yaşıyor). Alıntılar üç hedefte
  de hiçbir koşulda seçilmez.

Ayrıntılar: **[ILKELER.md](ILKELER.md)**

## Yapı

```
ILKELER.md          kriterler ve kurallar
hedefler.yaml       üç hedefin ağırlık, ölçü ve biçim ayarları
agac.yaml           Türk dilleri ağacı (40 dil, 89 ağız, konuşur sayıları)
tarihi.yaml         tarihî tanıklar (Eski Türkçe, Karahanlıca, Kuman-Kıpçakça…)
AGIRLIKLAR.md       üç hedefin ağırlık tabloları (üretilir)
KARSILASTIRMA.md    her kavram için üç hedefin seçimi (üretilir)
sozluk/SIRA.md      kelimelerin çalışma sırası (sıklığa göre)
sozluk/temel/       temel söz varlığı: her kavram için bir dosya
araclar/puanla.py   puanlama ve ağaç üzerinde seçim
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

# üretilen dosyaları yenile
python3 araclar/puanla.py --agirliklar --agizlar --md > AGIRLIKLAR.md
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
