# Büyük gözden geçirme 1 (197 kavram)

Tarih: 2026-11-13. Bu, çalışma planının 4. adımıdır. Plana göre ilk 10 kelimelik
denemeden sonra yaklaşık 100 kelime toplanacak ve şu üç iş yapılacaktı:

1. Örgüyü veriden hesaplamak.
2. Seçilen köprü biçimlerin ses düzenine bakmak.
3. Ayrışan kavramları incelemek.

Gözden geçirme 197 kavramda yapıldı; olması gerekenden geç. Bu raporun
sonunda yöntem **sürüm 1** olarak donduruldu ([ILKELER.md §15](ILKELER.md)).
Kalan açık sorular sürüm 2'de ele alınacak.

## 1. Örgü (ag.yaml)

Ayrıntılı tablolar [ORGU.md](ORGU.md)'dedir; hesabı yapan araç
[`araclar/orgu.py`](araclar/orgu.py)'dir.

- **Tahminlerin genel yönü doğru çıktı.** Veriden ölçülen yakınlık ile elle
  verilen anlaşılırlık tahminleri arasındaki korelasyon 0,85.
- **Asıl sorun boşluklardı.** `ag.yaml`'da yalnız 68 çiftin değeri vardı ve
  yazılmayan çift 0 sayılıyordu. Böylece veride çok yakın çıkan pek çok dil
  "birbirini hiç anlamıyor" kabul ediliyordu. Örnekler:
  - Azerbaycan–Gagauz (veriden beklenen 0,62)
  - Karay–Kumuk (0,73)
  - Kırgız–Karaçay (0,63)

  Beklenen değeri 0,25 ve üstü olan 263 çift veriden dolduruldu.
- **Veriden çok sapan 6 tahmin düzeltildi.** Yeni değer, tahmin ile beklenenin
  ortasıdır; eski değer satır yorumunda durur.

  | Çift | Eski tahmin | Veriden beklenen | Yeni değer |
  |---|---|---|---|
  | Özbek–Uygur | 0,80 | 0,62 | 0,70 |
  | Kırım Tatar–Kumuk | 0,50 | 0,64 | 0,57 |
  | Türkiye–Türkmen | 0,40/0,45 | 0,56 | 0,47/0,52 |
  | Türkiye–Kırım Tatar | 0,50/0,55 | 0,65 | 0,56/0,61 |
  | Hakas–Orta Çulım | 0,50 | 0,63 | 0,57 |
  | Şor–Orta Çulım | 0,50 | 0,62 | 0,56 |

- **İki tahmin gerekçesiyle korundu.**
  - Halaç–Azerbaycan 0,15: veri 0,42 bekliyor. Temel kelimeler ortak, ama
    Halaççanın ses yapısı uzak; bu ölçü sesi görmüyor.
  - Saha–Dolgan 0,90: veri 0,78 bekliyor. Dolganca Sahacanın yakın bir kolu.
- **Sonuca etkisi:**
  - Hedef 1'de (ortak dil) hiçbir kavramın kökü değişmedi; yalnız iki biçim
    değişti (anda → anta, uruk → uruğ).
  - Hedef 3'te (en çok kişi) 14 kavramın seçimi değişti; çoğu Türkiye
    Türkçesinin kelimesine kaydı (çok, çocuk, koş-, say-, omuz, sopa…).
    Sebebi: Türkiye Türkçesini anlayan Oğuz ve Kıpçak toplulukları artık
    hesaba giriyor.
  - Ayrışan kavram sayısı 26'dan 30'a çıktı.

## 2. Ses düzeni

Hedef 1'in seçtiği 197 köprü biçim incelendi. Kural konmadı (ILKELER §9). Bu
bölüm yalnız kendiliğinden oluşan düzenlilikleri gösterir.

**Kendiliğinden oluşan düzenlilikler** (çoğunluğun ortak ve eski durumu):

- **Kelime başında t-, k- korunuyor.** Oğuz dillerinin d-/g- ile söylediği
  köklerde bile t-/k- seçildi (tağ, til, tiş, köz, kel-, kün…). d-/g- ile
  başlayan tek biçim *dört* (öteki dillerde tört).
- **Kelime başında y- korunuyor.** y- ile başlayan 30 kökün hepsinde y-
  seçildi (yer, yıl, yel…); Kıpçak'taki j-/c-, Sibirya'daki ç-/t- değil.
- **ñ korunuyor** (eñek, teñiz, tereñ, keñ, oñ, yañı).

**Düzensiz kalanlar.** Bunlar sürüm 2'de karara bağlanacak.

- **Sondaki -ğ.**
  - Bir kısmında korunmuş: açığ, katığ, kuruğ, sarığ, uluğ, uruğ, kıdığ.
  - Bir kısmında düşmüş: tolu (tolıg), yiti (yitig), tatlı (tatlığ), teri,
    kişi.
  - Aynı ek (-ığ) farklı kelimelerde farklı biçim alıyor.
- **Ünlüler.**
  - män (ä ile) ama sen, beş, kel- (e ile).
  - Aynı türden kelimelerde ı/u farkı: yağmır, yapırak, yultuz, yumurtğa.
- **Dile özgü yenilikler.**
  - suw, tişiriw: Kıpçak -w.
  - munda: m- başlangıcı.
  - kökräk: Tatar/Uygur ä.

  Bunlar biçimin hangi dilden alındığına göre değişiyor.

Sebep: Hedef 1 kökü veriden seçiyor, biçimi de o kökün en çok köprü kuran
dildeki biçiminden alıyor. Biçimleri tek bir ses düzenine göre düzenleyip
düzenlememek bir dil tasarımı kararıdır (bkz. açık soru 1).

## 3. Ayrışan kavramlar (30)

[KARSILASTIRMA.md](KARSILASTIRMA.md)'de üç hedefin farklı kök seçtiği
kavramlar üç gruba ayrılıyor:

**a) Hedef 3 Türkiye Türkçesinin kelimesini seçiyor, Hedef 1 çoğunluğunkini**
(14):
- çok (köp / çok), çocuk (bala / çocuk), değnek (tayak / sopa)
- göğüs (kökrek / kögüz), kenar (kıdığ / çet), kök (tamır / kök)
- koş- (yügür / koş), omuz (egin / omuz), say- (sana / say)
- sinek (çıbın / siñek), uzak (ırak / uzak), ırmak (su / ırmak)
- ip (bağ / yip), hangi (kayu / kañı)

Bu, yöntemin beklenen davranışı: Türkiye Türkçesinin konuşur sayısı büyük.

**b) Hedef 2 Çuvaşçada da bulunan bir kökü seçiyor** (12):
- vur- (*ur-* yerine çap/şap), at- (taşla yerine bırak/părax)
- koş- (çap), düş- (tüş), gece (keçe), güneş (koyaş)
- de- (te), üfle- (ür), yakın (yağuk), boğaz (boğuz)
- el (elig), yarın

Hedef 2 kökün ağaçta ne kadar yükseğe çıktığına bakar. Bir kök Çuvaşçada ve
tek bir Ortak Türkçe dilinde bulunursa "Ana Türkçe" düzeyine çıkar. Bütün Ortak
Türkçe dillerinde bulunan ama Çuvaşçada olmayan bir kök ise "Ortak Türkçe"
düzeyinde kalır.

Bu, *vur-*'da olduğu gibi, bilim insanlarının Ana Türkçeye kadar götürdüğü
kökleri de (*ur-*) geride bırakabiliyor (bkz. açık soru 2).

**c) Hedef 1 anlamı genişlemiş bir kökü seçiyor** (4):
- bak- (kara-), el (kol), karın (iç), ekşi (açığ)

Bu kökler çoğunlukta yaşıyor, ama ortak dilde başka bir kavramla çakışıyor
(bkz. 4. bölüm).

## 4. Çakışan biçimler

Hedef 1'de aynı biçim birden çok kavrama düşüyor:

| Biçim | Kavramlar | Tür |
|---|---|---|
| açığ | acı, ekşi | aynı kök, iki anlam |
| ığaç | ağaç, odun | aynı kök, iki anlam |
| kün | gün, güneş | aynı kök, iki anlam (birçok dilde böyle) |
| suw | su, ırmak | aynı kök, iki anlam |
| ot | ateş, ot | eşsesli iki kök |
| kara | kara, bak- | eşsesli iki kök |
| et | et, et-/kıl- | eşsesli iki kök |
| kül | kül, gül- | eşsesli iki kök |
| iç | iç-, karın | eşsesli iki kök |
| it | it, it- | eşsesli iki kök |

Çoğu Türk dillerinde de böyle (kün, ot, et). Ama bir kavram, ortak dilde zaten
başka bir anlamı olan bir biçime düşünce (ekşi = açığ, karın = iç, ırmak = su)
ayrım kayboluyor. Şimdilik kural yok (bkz. açık soru 3).

## 5. Bu gözden geçirmede yapılan veri düzeltmeleri

Bunlar yöntemi değil, veriyi düzeltir:

- Codex Cumanicus biçimleri Savelyev'den Latin yazımıyla gelmişti (archa,
  churu, cus…). 13 kökte çalışma yazımına aktarıldı. Yanlış köke düşen bir
  tanık (ya'ox → yağuk) taşındı.
- Wiktionary'den gelen Eski Anadolu ve Osmanlıca fiil biçimleri mastar ekiyle
  gelmişti (almaq, görmäk). 16 kökte ek atıldı. Üreteç artık bunu kendisi
  yapıyor.
- Bir tanık (üfle-: ürmek) yanlış köke yazılmıştı; doğru köke (ür) taşındı.

## 6. Açık sorular (sürüm 2)

1. **Biçim düzenleme.** Ortak dilin biçimleri tanıklı biçim olarak mı kalsın,
   yoksa çoğunluğun ses düzenine göre (sondaki -ğ, ä/e, -w) düzenlensin mi?
   Düzenlenecekse kurallar önce bu rapordaki düzenliliklerden çıkarılır.
2. **Bilimsel kuruluşun ağırlığı.** Hedef 2'de, yaşayan dillerde Çuvaşça
   karşılığı olmasa da bilim insanlarının Ana Türkçeye götürdüğü bir kök
   (`ana_turkce` alanı dolu) Ana Türkçe düzeyinde sayılsın mı?
3. **Çakışma cezası.** Hedef 1, ortak dilde başka bir kavramın biçimiyle
   çakışan adaya ceza versin mi? Yoksa çakışmalar dilbilgisi aşamasında mı
   ele alınsın?

Sonraki büyük gözden geçirme yaklaşık 300 kavramda.
