# dil: Ortak Türk Dili

Bütün Türk kavimlerinin birbirini anlamasını kolaylaştıracak, **öz ve eski
Türkçe** kelimelere dayanan ortak bir dil oluşturma çalışması.

- Kelimeler nüfusa göre değil, **Türk dilleri ağacındaki yayılımlarına** göre
  seçilir. Hiçbir topluluk, kalabalığıyla veya içindeki dil sayısıyla diğerlerini
  ezemez.
- En tepede tek bir ortak kelime seçilir: Eski Türkçe biçime en yakın yaşayan biçim. Ağaç dallandıkça
  her dal, gerekirse kendi eş anlamlısını ve kendi ses biçimini alır. En altta her
  dilin günlük kullandığı biçim de not edilir.

Ayrıntılar: **[ILKELER.md](ILKELER.md)**

## Yapı

```
ILKELER.md          kriterler ve kurallar
agac.yaml           Türk dilleri ağacı (34 yaşayan dil)
tarihi.yaml         tarihî tanıklar (Eski Türkçe, Karahanlıca, Kuman-Kıpçakça…)
sozluk/temel/       temel söz varlığı: her kavram için bir dosya
araclar/puanla.py   puanlama ve ağaç üzerinde seçim
.claude/skills/kelime-arastir/   bir kelimeyi araştırma yöntemi ve şablon
```

Yeni kelime eklemek için Claude'a "*göz kelimesini araştır*" demek yeterli.
Araştırma `kelime-arastir` yöntemine göre yapılır.

## Kullanım

```bash
pip install -r requirements.txt

python3 araclar/puanla.py --agirliklar        # dil ağırlıkları
python3 araclar/puanla.py                     # bütün kavramlar
python3 araclar/puanla.py buyuk --derinlik 2  # tek kavram, ilk 2 seviye
```

Örnek ("büyük"):

```
Türk dilleri                               uluğ
  Oğur kolu                                pısăk    ← farklı kök: bedük
  Ortak Türkçe                             uluğ
    Oğuz kolu                              büük     ← farklı kök: bedük
    Kıpçak kolu                            ullu
    Karluk kolu                            uluğ
    Sibirya kolu                           uluğ
```

## Yol haritası

- [x] Aşama 0: İlkeler, dil ağacı, puanlama aracı
- [ ] Aşama 1: Temel söz varlığı (~200 kavram, Swadesh + Leipzig-Jakarta listeleri)
- [ ] Aşama 2: Ses ve yazım kuralları, ortak alfabe
- [ ] Aşama 3: Dilbilgisi (ekler, çekim, söz dizimi)
- [ ] Aşama 4: Konulara göre genişletme, eski köklerden yeni kelime türetme
- [ ] Aşama 5: Örnek metinler, karşılıklı anlaşılırlık denemeleri

> **Not:** `sozluk/` altındaki veriler şimdilik örnektir ve `dogrulandi: false`
> olarak işaretlidir. Kaynaklarla kontrol edilmeden kesin kabul edilmemelidir.
