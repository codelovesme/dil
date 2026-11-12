# Ağırlıklar

> Bu dosya `python3 araclar/puanla.py --agirliklar --md > AGIRLIKLAR.md` komutuyla üretilir; elle düzenlemeyin. Her hedef kendi ölçüsünü kullanır (bkz. `hedefler.yaml`, ILKELER.md §1). Bir dilin içinde yazı dili %50, ağızlar kalan %50'yi paylaşır (Hedef 1 ve 3).

## Ortak dil

*Bütün Türk toplulukları birbirini anlasın; köprü dil.* dil ağırlığı = N / √(çevre); çevre = N + Σ pay(anlaşılırlık) × N_komşu, pay = (s − 0.5) / (1 − 0.5)  (örgü + karekök).

| Kol | Ağırlık |
|---|---:|
| Oğur kolu | %2.5 |
| Halaç kolu | %0.6 |
| Oğuz kolu | %46.7 |
| Kıpçak kolu | %24.5 |
| Karluk kolu | %21.3 |
| Sibirya kolu | %4.5 |

| Dil | Kol | Konuşur | Anlaşılırlık çevresi | Ağırlık |
|---|---|---:|---:|---:|
| Türkiye Türkçesi | Oğuz kolu | 80.000.000 | 87.08 milyon | %24.79 |
| Özbekçe | Karluk kolu | 35.000.000 | 41.60 milyon | %15.69 |
| Azerbaycan Türkçesi | Oğuz kolu | 30.000.000 | 56.01 milyon | %11.59 |
| Kazakça | Kıpçak kolu | 13.000.000 | 16.56 milyon | %9.24 |
| Türkmence | Oğuz kolu | 7.000.000 | 7.28 milyon | %7.50 |
| Uygurca | Karluk kolu | 11.000.000 | 32.00 milyon | %5.62 |
| Tatarca | Kıpçak kolu | 4.300.000 | 5.18 milyon | %5.46 |
| Kırgızca | Kıpçak kolu | 5.000.000 | 13.10 milyon | %3.99 |
| Çuvaşça | Oğur kolu | 740.000 | 0.74 milyon | %2.49 |
| Sahaca (Yakutça) | Sibirya kolu | 450.000 | 0.45 milyon | %1.94 |
| Başkurtça | Kıpçak kolu | 1.200.000 | 4.21 milyon | %1.69 |
| Kumukça | Kıpçak kolu | 450.000 | 0.61 milyon | %1.67 |
| Tuvaca | Sibirya kolu | 280.000 | 0.28 milyon | %1.53 |
| Karaçay-Malkarca | Kıpçak kolu | 300.000 | 0.50 milyon | %1.23 |
| Salarca | Oğuz kolu | 70.000 | 0.07 milyon | %0.76 |
| Irak Türkmencesi (Kerkük) | Oğuz kolu | 2.000.000 | 68.00 milyon | %0.70 |
| Horasan Türkçesi | Oğuz kolu | 700.000 | 9.50 milyon | %0.66 |
| Halaçça | Halaç kolu | 42.000 | 0.04 milyon | %0.59 |
| Kaşkayca | Oğuz kolu | 950.000 | 21.95 milyon | %0.59 |
| Hakasça | Sibirya kolu | 40.000 | 0.04 milyon | %0.57 |
| Karakalpakça | Kıpçak kolu | 600.000 | 13.06 milyon | %0.48 |
| Kırım Tatarcası | Kıpçak kolu | 400.000 | 8.42 milyon | %0.40 |
| Sarı Uygurca | Sibirya kolu | 4.600 | 0.00 milyon | %0.20 |
| Sibirya Tatarcası | Kıpçak kolu | 100.000 | 4.42 milyon | %0.14 |
| Kuzey Altayca | Sibirya kolu | 3.000 | 0.00 milyon | %0.13 |
| Güney Altayca | Kıpçak kolu | 55.000 | 2.05 milyon | %0.11 |
| Şorca | Sibirya kolu | 3.000 | 0.01 milyon | %0.08 |
| Nogayca | Kıpçak kolu | 90.000 | 11.93 milyon | %0.08 |
| Gagavuzca | Oğuz kolu | 150.000 | 48.16 milyon | %0.06 |
| Çulımca | Sibirya kolu | 40 | 0.00 milyon | %0.00 |
| Balkan Gagavuz Türkçesi | Oğuz kolu | 11.000 | 56.12 milyon | %0.00 |
| Dolganca | Sibirya kolu | 800 | 0.36 milyon | %0.00 |
| Duhaca (Tsaatan) | Sibirya kolu | 500 | 0.17 milyon | %0.00 |
| Urumca | Kıpçak kolu | 200 | 0.28 milyon | %0.00 |
| Karayca | Kıpçak kolu | 80 | 0.16 milyon | %0.00 |
| Soyotça | Sibirya kolu | 37 | 0.11 milyon | %0.00 |
| Tofaca | Sibirya kolu | 40 | 0.14 milyon | %0.00 |
| Fuyu Kırgızcası | Sibirya kolu | 10 | 0.02 milyon | %0.00 |
| Kırımçakça | Kıpçak kolu | 20 | 0.36 milyon | %0.00 |
| İli Türkçesi | Karluk kolu | 120 | 33.30 milyon | %0.00 |

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

