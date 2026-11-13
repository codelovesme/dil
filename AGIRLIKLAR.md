# Ağırlıklar

> Bu dosya `python3 araclar/puanla.py --agirliklar --md > AGIRLIKLAR.md` komutuyla üretilir; elle düzenlemeyin. Her hedef kendi ölçüsünü kullanır (bkz. `hedefler.yaml`, ILKELER.md §1). Bir dilin içinde yazı dili %50, ağızlar kalan %50'yi paylaşır (Hedef 1 ve 3).

## Ortak dil

*Ortak kelime; ne kadar çok farklı grup kullanıyorsa o kadar iyi.* dil ağırlığı = kendine özgülük × basamak / 8; kendine özgülük = b / (b + Σ pay(s) × b_komşu), pay(s) = (s − 0.5) / (1 − 0.5).

| Kol | Ağırlık |
|---|---:|
| Oğur kolu | %5.8 |
| Halaç kolu | %4.9 |
| Oğuz kolu | %27.7 |
| Kıpçak kolu | %28.5 |
| Karluk kolu | %8.6 |
| Sibirya kolu | %24.5 |

| Dil | Kol | Konuşur | Basamak | Kendine özgülük | Ağırlık |
|---|---|---:|---:|---:|---:|
| Çuvaşça | Oğur kolu | 740.000 | 6 | 1.00 | %5.82 |
| Halaçça | Halaç kolu | 42.000 | 5 | 1.00 | %4.85 |
| Salarca | Oğuz kolu | 70.000 | 5 | 1.00 | %4.85 |
| Özbekçe | Karluk kolu | 35.000.000 | 8 | 0.58 | %4.53 |
| Sahaca (Yakutça) | Sibirya kolu | 450.000 | 6 | 0.71 | %4.16 |
| Türkmence | Oğuz kolu | 7.000.000 | 7 | 0.60 | %4.06 |
| Başkurtça | Kıpçak kolu | 1.200.000 | 7 | 0.59 | %4.00 |
| Sarı Uygurca | Sibirya kolu | 4.600 | 4 | 1.00 | %3.88 |
| Tuvaca | Sibirya kolu | 280.000 | 6 | 0.62 | %3.64 |
| Hakasça | Sibirya kolu | 40.000 | 5 | 0.73 | %3.53 |
| Uygurca | Karluk kolu | 11.000.000 | 8 | 0.45 | %3.53 |
| Horasan Türkçesi | Oğuz kolu | 700.000 | 6 | 0.58 | %3.36 |
| Sibirya Tatarcası | Kıpçak kolu | 100.000 | 6 | 0.58 | %3.36 |
| Tatarca | Kıpçak kolu | 4.300.000 | 7 | 0.46 | %3.14 |
| Türkiye Türkçesi | Oğuz kolu | 80.000.000 | 8 | 0.39 | %3.05 |
| Kaşkayca | Oğuz kolu | 950.000 | 6 | 0.52 | %3.01 |
| Güney Altayca | Kıpçak kolu | 55.000 | 5 | 0.61 | %2.97 |
| Irak Türkmencesi (Kerkük) | Oğuz kolu | 2.000.000 | 7 | 0.42 | %2.87 |
| Azerbaycan Türkçesi | Oğuz kolu | 30.000.000 | 8 | 0.37 | %2.85 |
| Kazakça | Kıpçak kolu | 13.000.000 | 8 | 0.34 | %2.61 |
| Karaçay-Malkarca | Kıpçak kolu | 300.000 | 6 | 0.39 | %2.26 |
| Şorca | Sibirya kolu | 3.000 | 4 | 0.56 | %2.18 |
| Kuzey Altayca | Sibirya kolu | 3.000 | 4 | 0.56 | %2.16 |
| Kırgızca | Kıpçak kolu | 5.000.000 | 7 | 0.31 | %2.08 |
| Gagavuzca | Oğuz kolu | 150.000 | 6 | 0.35 | %2.02 |
| Kırım Tatarcası | Kıpçak kolu | 400.000 | 6 | 0.32 | %1.89 |
| Kumukça | Kıpçak kolu | 450.000 | 6 | 0.31 | %1.80 |
| Balkan Gagavuz Türkçesi | Oğuz kolu | 11.000 | 5 | 0.34 | %1.64 |
| Karakalpakça | Kıpçak kolu | 600.000 | 6 | 0.25 | %1.48 |
| Urumca | Kıpçak kolu | 200 | 3 | 0.42 | %1.21 |
| Dolganca | Sibirya kolu | 800 | 3 | 0.38 | %1.12 |
| Çulımca | Sibirya kolu | 40 | 2 | 0.50 | %0.98 |
| Fuyu Kırgızcası | Sibirya kolu | 10 | 2 | 0.50 | %0.97 |
| Nogayca | Kıpçak kolu | 90.000 | 5 | 0.20 | %0.96 |
| Duhaca (Tsaatan) | Sibirya kolu | 500 | 3 | 0.31 | %0.91 |
| İli Türkçesi | Karluk kolu | 120 | 3 | 0.20 | %0.58 |
| Kırımçakça | Kıpçak kolu | 20 | 2 | 0.27 | %0.52 |
| Soyotça | Sibirya kolu | 37 | 2 | 0.25 | %0.49 |
| Tofaca | Sibirya kolu | 40 | 2 | 0.23 | %0.44 |
| Karayca | Kıpçak kolu | 80 | 2 | 0.11 | %0.22 |

## Ana Türkçe tahmini

**Ana Türkçe tahmini** ağırlık kullanmaz. Bir kökün yaşı, soy ağacının (agac.yaml) hangi düğümüne kadar geri gittiğine bakılarak bulunur: bir düğümün en az iki kolunda bulunan kök o düğümün dilinde de vardı. Nüfus ve dil sayısı önemsizdir.

## En çok kişinin anladığı

*En fazla insan anlasın.* dil ağırlığı = konuşur sayısı.

| Kol | Ağırlık |
|---|---:|
| Oğur kolu | %0.4 |
| Halaç kolu | %0.0 |
| Oğuz kolu | %62.3 |
| Kıpçak kolu | %13.1 |
| Karluk kolu | %23.7 |
| Sibirya kolu | %0.4 |

| Dil | Kol | Konuşur | Ağırlık |
|---|---|---:|---:|
| Türkiye Türkçesi | Oğuz kolu | 80.000.000 | %41.25 |
| Özbekçe | Karluk kolu | 35.000.000 | %18.05 |
| Azerbaycan Türkçesi | Oğuz kolu | 30.000.000 | %15.47 |
| Kazakça | Kıpçak kolu | 13.000.000 | %6.70 |
| Uygurca | Karluk kolu | 11.000.000 | %5.67 |
| Türkmence | Oğuz kolu | 7.000.000 | %3.61 |
| Kırgızca | Kıpçak kolu | 5.000.000 | %2.58 |
| Tatarca | Kıpçak kolu | 4.300.000 | %2.22 |
| Irak Türkmencesi (Kerkük) | Oğuz kolu | 2.000.000 | %1.03 |
| Başkurtça | Kıpçak kolu | 1.200.000 | %0.62 |
| Kaşkayca | Oğuz kolu | 950.000 | %0.49 |
| Çuvaşça | Oğur kolu | 740.000 | %0.38 |
| Horasan Türkçesi | Oğuz kolu | 700.000 | %0.36 |
| Karakalpakça | Kıpçak kolu | 600.000 | %0.31 |
| Kumukça | Kıpçak kolu | 450.000 | %0.23 |
| Sahaca (Yakutça) | Sibirya kolu | 450.000 | %0.23 |
| Kırım Tatarcası | Kıpçak kolu | 400.000 | %0.21 |
| Karaçay-Malkarca | Kıpçak kolu | 300.000 | %0.15 |
| Tuvaca | Sibirya kolu | 280.000 | %0.14 |
| Gagavuzca | Oğuz kolu | 150.000 | %0.08 |
| Sibirya Tatarcası | Kıpçak kolu | 100.000 | %0.05 |
| Nogayca | Kıpçak kolu | 90.000 | %0.05 |
| Salarca | Oğuz kolu | 70.000 | %0.04 |
| Güney Altayca | Kıpçak kolu | 55.000 | %0.03 |
| Halaçça | Halaç kolu | 42.000 | %0.02 |
| Hakasça | Sibirya kolu | 40.000 | %0.02 |
| Balkan Gagavuz Türkçesi | Oğuz kolu | 11.000 | %0.01 |
| Sarı Uygurca | Sibirya kolu | 4.600 | %0.00 |
| Şorca | Sibirya kolu | 3.000 | %0.00 |
| Kuzey Altayca | Sibirya kolu | 3.000 | %0.00 |
| Dolganca | Sibirya kolu | 800 | %0.00 |
| Duhaca (Tsaatan) | Sibirya kolu | 500 | %0.00 |
| Urumca | Kıpçak kolu | 200 | %0.00 |
| İli Türkçesi | Karluk kolu | 120 | %0.00 |
| Karayca | Kıpçak kolu | 80 | %0.00 |
| Tofaca | Sibirya kolu | 40 | %0.00 |
| Çulımca | Sibirya kolu | 40 | %0.00 |
| Soyotça | Sibirya kolu | 37 | %0.00 |
| Kırımçakça | Kıpçak kolu | 20 | %0.00 |
| Fuyu Kırgızcası | Sibirya kolu | 10 | %0.00 |

