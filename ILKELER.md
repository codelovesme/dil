# İlkeler

Bu belge projenin anayasasıdır. Kelime seçimiyle ilgili her karar buradaki
kurallara dayanmalı; kural değişecekse önce bu belge değişir.

## 1. Amaç ve hedefler

Türk topluluklarını öz Türkçe kelimelerle birbirine bağlamak. Aynı veriden
**üç ayrı soruya** cevap aranır. Bunlar farklı sorulardır ve her biri kendi
ölçüsünü ister. Ayarlar [`hedefler.yaml`](hedefler.yaml) dosyasındadır.

Bunlara iki hedef daha eşlik eder. **Beşinci hedef** çeviridir (§16): verinin
kullanımıdır, kelime seçmez. **Dördüncü hedef**: **tanıklı sözlük** (§14). İlk üç hedef
bir kelime *seçer*; sözlük hiçbir şey seçmez, her kökün bütün hayatını *belgeler*:
hangi dilde, ağızda ve boyda, nerede, kaçıncı yüzyılda, hangi biçim ve anlamla
kullanılmış, kim kaydetmiş. Üç hedefin dayandığı kanıt budur; ölçüsü kapsamdır.

| | 1. Ortak dil **(asıl ürün)** | 2. Ana Türkçe tahmini | 3. En çok kişinin anladığı |
|---|---|---|---|
| **Soru** | Ortak kelime: ne kadar çok farklı grup kullanıyorsa o kadar iyi | Türkçenin en eski hâli neydi? | En fazla insan anlasın |
| **Ölçü** | Yaygınlık: kaç farklı grup kullanıyor (gruplar örgüdeki benzerlikle belirlenir), kimse geride kalmasın | Kök yaşı: kök soy ağacının hangi düğümüne kadar gidiyor | Anlayan kişi sayısı |
| **Kullandığı yapı** | Örgü (`ag.yaml`) + basamak | Soy ağacı (`agac.yaml`) + tarihî tanıklar | Konuşur sayıları + ikinci dil bağları |
| **Biçim** | Köprü biçim: en anlaşılır yaşayan biçim | Dalın en eski tanığının biçimi | En anlaşılır yaşayan biçim |
| **Ürün** | Önerilen ortak dil | Ana Türkçe sözlüğü | Pratik karşılaştırma |

Üç hedefte de geçerli olanlar:

- **Öz Türkçe:** Arapça, Farsça, Rusça, Moğolca vb. alıntılar **hiçbir koşulda**
  seçilmez.
- **Aynı veri:** Kelimeler bir kez araştırılır; üç hedef aynı veriyi kendi
  ölçüsüyle değerlendirir.
- **Üç ölçü yan yana:** Her kelimenin her adayı için üç ölçü birlikte
  gösterilir. Böylece bir seçimin neyi kazandırıp neyi kaybettirdiği görünür.
- **Karşılaştırma:** Üç hedefin aynı kökü seçtiği kavramlar sağlamdır.
  Ayrıştıkları kavramlar tartışmaya açılır:
  [`KARSILASTIRMA.md`](KARSILASTIRMA.md) (`python3 araclar/puanla.py --karsilastir`).

## 2. Veri: soy ağacı, örgü, tanıklar

Diller arasındaki ilişkiler iki ayrı yapıda tutulur:

| Dosya | Ne tutar | Nerede kullanılır |
|---|---|---|
| [`agac.yaml`](agac.yaml) | **Soy ağacı:** hangi dil hangisinden geliyor; diller, ağızlar, konuşur sayıları | Hedef 2'nin temeli; raporlarda alttan yukarı gösterim |
| [`ag.yaml`](ag.yaml) | **Örgü:** diller arasındaki ağırlıklı bağlar (anlaşılırlık, ikinci dil, temas) | Hedef 1, 3 ve Hedef 2'deki ödünç ayıklama |
| [`tarihi.yaml`](tarihi.yaml) | Tarihî tanıklar (Eski Türkçe, Karahanlıca…) | Eskilik, Hedef 2 |
| `sozluk/temel/…` | Kavramlar: her kavramın aday kökleri ve dillerdeki günlük biçimleri | Hedef 1-3 |
| `sozluk/kok/` | Sözlük maddeleri: her kökün bütün tanıkları (yer, yüzyıl, biçim, anlam, kaynak) | Hedef 4; Hedef 1-3'ün kanıtı |

Ağaç ile örgünün ayrılmasının sebebi şudur: diller hem bir soydan gelir hem de
komşularıyla etkileşir. Örneğin Güney Altayca hem Kırgızcaya hem Tuvacaya
yakındır. Soy ağacında bir dil tek bir ebeveynin altında durmak zorundadır.
Örgüde ise birden çok yere, farklı ağırlıklarla bağlanabilir.

### Soy ağacı

Yaşayan bütün Türk dilleri ve bilinen ağızları ağaçta tutulur (40 dil, 89 ağız):

```
Türk dilleri
├── Oğur kolu ............ Çuvaşça
└── Ortak Türkçe
    ├── Halaç kolu ....... Halaçça
    ├── Oğuz kolu ........ Batı Oğuz (Türkiye-Balkan, Azerbaycan), Güney Oğuz (İran),
    │                      Doğu Oğuz, Salarca
    ├── Kıpçak kolu ...... Kıpçak-Bulgar, Kıpçak-Oğuz (Kırım, Kafkas),
    │                      Kıpçak-Nogay, Kırgız-Kıpçak
    ├── Karluk kolu ...... Özbekçe, Doğu Karluk (Uygurca, İli Türkçesi)
    └── Sibirya kolu ..... Kuzey Sibirya, Güney Sibirya (Sarı Uygurca, Sayan, Yenisey-Altay)
```

Diller **birleştirilmez**. Türkçenin ne kadar çeşitlendiği görülsün diye her
dil, bilinen ağızlarına kadar ayrılır. Örneğin Türkiye Türkçesi şu ağızlara
ayrılır:

```
Türkiye Türkçesi
├── Yazı dili                       (otomatik eklenir, kodu: tur)
├── Anadolu ağızları
│   ├── Batı grubu ...... Ege, Teke-Akdeniz, Orta Anadolu, Batı Karadeniz
│   ├── Doğu grubu ...... Erzurum-Kars, Güneydoğu Anadolu, Ahıska
│   └── Kuzeydoğu grubu . Doğu Karadeniz
├── Rumeli ağızları ..... Doğu Rumeli, Batı Rumeli
├── Kıbrıs ağzı
└── Suriye Türkmen ağızları
```

Ağızları olan her dile otomatik olarak bir **"Yazı dili"** ağzı eklenir. Dilin
kendi kodu (`tur`, `kaz`…) bu yazı dilini gösterir:

- **Hedef 1 ve 3:** Yazı dili dilin içinde **%50** pay alır, ağızlar kalan
  %50'yi paylaşır. Anlaşılırlık açısından yazı dili, o dili konuşan herkesin
  ortak paydasıdır.
- **Hedef 2:** Yazı dili ağızlardan biri gibi sayılır, çünkü eski biçimleri
  çoğu zaman ağızlar korur.

Ağacı kurma kuralları:

1. **Ağaç soyu gösterir, yakınlığı değil.** Bir dil soyca bağlı olduğu dalın
   altına konur. Başka dillere yakınlığı örgüye yazılır. "Hangi dalın altına
   koymalı?" sorusu yakınlıktan doğuyorsa, cevap örgüdedir.
2. **Diller birleştirilmez.** Her topluluğun dili ayrı bir yapraktır.
3. **Ağız eklemek serbesttir.** Hiçbir hedefte dilin ağırlığını değiştirmez.
4. **Yeni bir dilin** gerekçesi `not` alanına, yaklaşık konuşur sayısı da
   `konusur` alanına yazılır.
5. **Sınıflandırmada görüş ayrılığı olan yerler `not` ile belirtilir.**
6. **Kapsam dışı kalanlar:** Aynu dili (dilbilgisi Türkçe, söz varlığı büyük
   ölçüde Farsça) ve dilini kaybetmiş topluluklar (ör. Litvanya Tatarları).

### Konuşur sayıları

Her dilin yaklaşık anadili konuşur sayısı `konusur` alanında tutulur.
Belirsiz olanlara `konusur_not` yazılır (tahmin aralığı, kaynak, tanım farkı).
**Aynı insanlar iki kez sayılmaz:** Bir kaynağın sayısı başka bir dilin ağzını
da kapsıyorsa o kısım düşülür. Örneğin Ethnologue'un Balkan Gagavuz Türkçesi
için verdiği ~460 bin, Türkiye'deki Yörükleri de sayar. Biz onları Türkiye
Türkçesinin ağzı olarak tuttuğumuz için burada sadece Balkan toplulukları ve
Surguçlar (~11 bin) sayılır.

### Örgü

[`ag.yaml`](ag.yaml) dosyasında üç tür bağ vardır:

| Bağ | Ne ölçer | Yön | Kullanıldığı yer |
|---|---|---|---|
| **Anlaşılırlık** | A dilini konuşan, B dilini öğrenmeden ne kadar anlar (dilbilimsel yakınlık) | Her iki yön ayrı yazılabilir | Hedef 1 (gruplar), Hedef 3 |
| **İkinci dil** | A konuşurları B'yi okul, medya ya da iki dillilik yoluyla ne kadar bilir | Dinleyen → konuşan | Sadece Hedef 3 |
| **Temas** | B dili A dilinden ne yoğunlukta kelime almış | Veren → alan | Hedef 2 (ödünç ayıklama) |

Anlaşılırlık ile ikinci dil bilinçli olarak ayrıdır. Halaçlar Azerbaycan
Türkçesini iyi bilir, ama iki dil birbirinden uzaktır. Hedef 1 kelimenin insanın
kendi dilinde nasıl duyulduğuyla ilgilendiği için ikinci dil bilgisini saymaz.

**Değerler iki kaynaktan gelir.** Elle yazılan değerler alan bilgisine dayanan
tahminlerdir. [`araclar/orgu.py`](araclar/orgu.py) aynı bağları kendi verimizden
ölçer: iki dilin asıl biçimlerinin aynı kökten olma oranı × o biçimlerin yazım
benzerliği. Ölçü elle verilen tahminlere doğrusal olarak uydurulur. Tahmini
olmayan çiftler bu "beklenen" değerle doldurulur (`ag.yaml`'daki `veriden`
bölümü). Veriden çok sapan tahminler gerekçesiyle düzeltilir ya da korunur;
ayrıntı [`ORGU.md`](ORGU.md)'dedir. Yazılmayan çiftler yine 0 sayılır.

Ölçü ses düzenini ve dilbilgisini görmez. Çalışma yazımı da farkları sildiği
için yakınlığı olduğundan yüksek gösterir. Bu yüzden elle verilen değerin
yerine kendiliğinden geçmez; yalnız boşlukları doldurur ve denetim sağlar.
Örgü her kelimede değil, yalnız büyük gözden geçirmelerde yeniden hesaplanır
(§15). Böylece sonuçlar kelime ekledikçe kendi kendine kaymaz.

## 3. Hedef 1: Ortak dil

Hedef 1'in sorusu **ortak kelimedir**: bir kelimeyi ne kadar çok **farklı grup**
kullanıyorsa o kadar iyidir. Nüfusun önceliği Hedef 3'ün, eskilik Hedef 2'nin
işidir; Hedef 1 yaygınlığa bakar.

### Gruplar etiketle değil, benzerlikle belirlenir

"Kim dil, kim lehçe, kim hangi kolda" diye sorulmaz. Yalnızca "bu dil öteki
dillere ne kadar benziyor?" diye sorulur. Cevap örgüdedir (`ag.yaml`):

- **Birbirine çok benzeyen diller tek bir grup sayılır** ve grubun payını
  aralarında paylaşır.
- **Ayrışmış bir dil kendi başına tam bir grup sayılır.**
- **Arada kalanlar**, ne kadar farklıysa o kadar fazladan ağırlık getirir.

Her dilin ağırlığı:

```
ağırlık(L) = kendine özgülük(L) × basamak(L) / 8

kendine özgülük(L) = b_L / (b_L + Σ  pay(s(L, j)) × b_j)       pay(s) = max(0, (s − 0.5) / 0.5)
                                  j
```

- `b`: **basamak**. Konuşur sayısı her 10 kat arttığında +1 puan (2–8):

  | Konuşur sayısı | Basamak | Örnek |
  |---|---|---|
  | 10 milyon ve üstü | 8 | Türkiye Türkçesi, Azerbaycan Türkçesi, Özbekçe, Kazakça, Uygurca |
  | 1 – 10 milyon | 7 | Türkmence, Tatarca, Başkurtça, Kırgızca, Irak Türkmencesi |
  | 100 bin – 1 milyon | 6 | Çuvaşça, Gagavuzca, Kaşkayca, Kırım Tatarcası, Sahaca, Tuvaca |
  | 10 – 100 bin | 5 | Halaçça, Salarca, Nogayca, Hakasça, Güney Altayca, Balkan Gagavuz Türkçesi |
  | 1 – 10 bin | 4 | Sarı Uygurca, Şorca, Kuzey Altayca |
  | 100 – 1 000 | 3 | Urumca, İli Türkçesi, Dolganca, Duhaca |
  | 100'den az | 2 | Karayca, Kırımçakça, Tofaca, Soyotça, Çulımca, Fuyu Kırgızcası |

  Basamak nüfusu neredeyse siler (80 milyon ile 150 bin: 8'e 6), ama 40
  kişilik bir topluluğun koca bir millet kadar sayılmasını önler.
- `s(L, j)`: L konuşurunun j dilini anlama düzeyi (örgüden).
- **Kendine özgülük:** Benzeri olmayan bir dil 1 alır (Çuvaşça, Halaçça,
  Salarca). Birbirinin aynısı k dil, payı k'ya böler. Yarı yarıya anlaşmak aynı
  grupta olmak demek değildir: 0.5 ve altındaki benzerlik sayılmaz.

### Tanım tartışmaları ağırlığı etkilemez

- Kırımçakça ayrı bir dil sayılırsa Kırım Tatarcası ile toplamı %3.04,
  Kırım Tatarcasının ağzı sayılırsa %2.99'dur. Çok benzedikleri için ayrı
  sayılmaları hiçbir şeyi şişirmez.
- Gagavuzca ayrı dil sayılırsa Türkiye Türkçesiyle toplamı %5.1, ağız
  sayılırsa %3.5'tir. Gagavuzca gerçekten biraz farklı olduğu için ne kadar
  farklıysa o kadar ek ses getirir. Büyük bir dilin gölgesinde kaybolmaz.

Benzerlikler ileride kendi kelime verimizden hesaplandığında elle verilmiş
hiçbir karar kalmayacaktır.

### Sonuç

| Kol | Hedef 1 | Hedef 3 (karşılaştırma için) |
|---|---|---|
| Kıpçak | %31.7 | %13.1 |
| Oğuz | %27.0 | %62.3 |
| Sibirya | %23.4 | %0.4 |
| Karluk | %8.1 | %23.7 |
| Oğur | %5.3 | %0.4 |
| Halaç | %4.4 | %0.02 |

Tam tablo: [`AGIRLIKLAR.md`](AGIRLIKLAR.md).

Bu yöntem çok yakın akrabası olan dillere doğal olarak daha küçük bir pay verir.
Türkiye Türkçesi (%2.9), Türkmenceden (%4.6) düşüktür. Bunun sebebi Türkiye
Türkçesinin önemsiz sayılması değildir: Türkiye, Azerbaycan, Gagavuz ve Kerkük
Türkçeleri büyük ölçüde tek bir grup oluşturur. "Kaç farklı grup kullanıyor"
sorusunun mantığı budur. Kalabalığın etkisi Hedef 3'te ayrıca ölçülür.

#### Neden örgü + karekök kuralı değil?

Daha önce her dili `N / √(çevre)` ile, yani nüfusa dayalı bir karekök kuralıyla
tartmıştık. Bu kural, bir çevrenin tek bir blok gibi oy verdiğini varsayar.
Oysa her topluluğun kendi dili ve kendi kelimeleri vardır. Bu varsayım saçma
sonuçlar doğurdu: bir dil büyük bir dile benzediği için ağırlık kaybediyordu.
150 bin kişilik Gagavuzca %0.06, 40 bin kişilik Hakasça %0.57 alıyordu. Ders:
benzerlik, grubun **paylaşılmasını** belirlemeli; büyük bir komşunun nüfusu
küçük bir dili ezmemeli.

### Kimse geride kalmamalı (taban şartı)

Ağırlıklı ortalama tek başına yetmez: ortalama yüksekken bir topluluk hiç
anlamıyor olabilir. Bu yüzden **100 binden çok konuşuru olan topluluklar**
ayrıca denetlenir. Seçilen biçimi %50'den az anlayan büyük
toplulukların ağırlık payı, 0.5 ile çarpılarak puandan düşülür. Raporda her
büyük topluluğun anlaşılırlığı gösterilir.

Çuvaş, Saha ve Halaç toplulukları ses yapısı bakımından o kadar ayrışmıştır ki
hemen her kelimede en alt sırada kalırlar. Bunlara veto hakkı verilirse hiçbir
kelime seçilemez. Bu yüzden taban şartı bir veto değil, bir cezadır: geride
kalan toplulukların ağırlık payı kadar puan düşer.

### Köprü biçim

En iyi biçim, her topluluğun kendi biçimine düzenli ses değişimleriyle
ulaşabileceği biçimdir:

```
tağ  →  dağ (Oğuz)  ·  taw (Kıpçak)  ·  too (Kırgız)  ·  toğ (Özbek)
```

Bu çoğu zaman eski, korunmuş biçimdir. Burada eskilik bir değer olarak değil,
bir **araç** olarak işe yarar: eski biçim hiçbir yaşayan topluluğa ait değildir
(tarafsızdır) ve her topluluk kendi ses değişimini uygulayarak ondan kendi
biçimine ulaşabilir (çözülebilirdir). Bu yüzden biçim puanına en eski tanık
biçimine yakınlık küçük bir bonus olarak eklenir (β = 0.2).

### Canlandırma

Bir dil seçilen Türkçe kökü kaybetmişse, örneğin alıntı kullanıyorsa, ona üst
dalın kelimesi önerilir ve raporda **"canlandırma"** olarak işaretlenir. En
tepede seçilen kök bugün dillerin ağırlıkça yarısından azında yaşıyorsa bütün
kavram canlandırma olarak işaretlenir. Bu, bedelin görünmesi içindir: o
kelimenin öğretilmesi gerekecektir.

## 4. Hedef 2: Ana Türkçe tahmini (kök yaşı)

Bir kelimenin ne kadar eski olduğu oyla bulunmaz. Tarihî dilbilimin
karşılaştırmalı yöntemindeki soru şudur: **bu kök ağacın hangi düğümüne kadar
geri gidiyor?** Bir kök bir düğümün **en az iki ayrı kolunda** bulunuyorsa
(ya da bir kolunda ve o düğümün kendi tarihî tanığında), o düğümün dilinde de
vardı:

| Kökün bulunduğu yer | Yaşı |
|---|---|
| Hem Oğur kolunda (Çuvaşça) hem Ortak Türkçede | **Ana Türkçe**, en eski katman |
| Ortak Türkçenin birkaç kolunda ya da Eski Türkçede ve bir kolda | Ortak Türkçe |
| Tek bir kolun içinde | O kolun kendi yeniliği |

Seçim:

1. En eski düğüme ulaşan kök kazanır.
2. Eşitlikte o düğümde daha çok hatta bulunan kök kazanır.
3. Sonra daha çok kolda bulunan, sonra en eski metinde geçen, sonra daha çok
   dilde bulunan kök kazanır.

Bu hesapta **ağırlık yoktur**: nüfus da dil sayısı da önemsizdir, önemli olan
kökün soy ağacında nerelerde bulunduğudur. Her dal kendi altındaki kanıta
bakar; "Kıpçakçanın en eski hâli"ni yalnızca Kıpçak kanıtı belirler.

### Türk dilleri arası ödünçler ayıklanır

Çuvaşça yüzyıllardır Tatarcadan kelime alıyor. Tatarcadan alınmış bir kelime,
sahte bir "Ana Türkçe" kanıtı üretir. Gerçek miras kelime Oğur kolunun ses
kurallarını taşır (Ortak Türkçe *z* yerine *r*, *ş* yerine *l*: *taş* →
*çul*). Bu yüzden:

- Biçim kaydında `odunc: tat` yazılmışsa o biçim kanıt sayılmaz.
- `miras: true` yazılmışsa kanıt sayılır.
- İkisi de yoksa otomatik bir uyarı işler: bir dil **kendi kolunda bu kökün
  tek kanıtıysa**, başka bir koldan güçlü bir temas bağı (`ag.yaml`, ≥ 0.5)
  varsa ve biçimi veren dilin biçimine çok benziyorsa (≥ 0.75), "ödünç olabilir"
  diye işaretlenir ve kök yaşında sayılmaz. Aynı kolda başka kanıt varsa
  uyarı verilmez, çünkü yakın akraba dillerin miras kelimeleri de birbirine
  benzer.

### Biçim

Dalın kendi en eski tanığının biçimi seçilir: en tepe ve Ortak Türkçe için
Eski Türkçe (*sub*, *tağ*), Oğuz için Eski Anadolu Türkçesi, Kıpçak için
Kuman-Kıpçakça. Tanık yoksa dalda en çok dilde görülen biçim alınır.

Gerçek yeniden kuruluş ses denkliklerinden yapılır. Örneğin *taş*
kelimesinin Ana Türkçe biçimi *\*tāĺ* olarak kurulur, çünkü Çuvaşça *l* ile
Ortak Türkçe *ş* aynı eski sesten gelir. Bunu otomatik yapamadığımız için
bilim insanlarının kurduğu biçim kökün `ana_turkce` alanına yazılır ve raporda
kendi sonucumuzla yan yana gösterilir. Bizim sonucumuz bir yaklaşımdır.

## 5. Hedef 3: En çok kişinin anladığı

```
anlayan kişi = Σ  N_L × anlama(L)
               L
anlama(L)    = en yükseği( L'nin kendi dilinde anlaması,
                           her j için: bağ(L, j) × j dilinde anlaşılması )
```

Burada bağ, anlaşılırlık ile ikinci dil bağlarının yüksek olanıdır. Örneğin
Azerbaycanlılar bir kelimeyi Türkiye Türkçesindeki biçimi sayesinde de
anlayabilir. Sonuç kişi sayısı olarak verilir: "*büyük*'ü ~117 milyon kişi
anlar."

İkinci dil bağları yalnızca bilinen büyük örnekler için girildiğinden, sonuç
gerçek anlaşılırlığın **alt sınırı** olarak okunmalıdır.

## 6. Kavram kayıtları

Her kavram için birden çok **aday kök** (etimon) olabilir. Örneğin "büyük" için
`uluğ`, `bedük`, `çoñ`, `zur`… Her kökün dillerde farklı **biçimleri** vardır.
Örneğin `tağ` kökü `dağ`, `taw`, `too`, `toğ`, `tu` olarak yaşar.

| Alan | Açıklama |
|---|---|
| `kok` | Kökün kimliği |
| `koken` | `türkçe`, `alıntı:<dil>` veya `belirsiz`. Yalnızca `türkçe` seçilebilir. |
| `tarihi` | Tarihî tanık kodu → biçim (ör. `{ otk: tağ, xqa: tağ, qwm: taw }`) |
| `bicimler` | Dil ya da ağız kodu → biçim. Ayrıntılı biçimde: `{ bicim, tercih, odunc, miras, kaynak }` |
| `ana_turkce` | Bilim insanlarının yeniden kurduğu Ana Türkçe biçim (ör. `"*tāĺ"`) |
| `kaynak`, `not` | Dayanak ve açıklama |

Tercih değerleri (bir dil içindeki eş anlamlılar):

| tercih | Anlamı |
|---|---|
| `1` | Asıl, günlük kelime (varsayılan) |
| `0.5` | Yaygın ama ikincil |
| `0.25` | Nadir, eskimiş, yazı dilinde kalmış, ya da anlamı kaymış |

**Eksik veri yok demek değildir.** Bir dil ya da ağız için hiç veri
girilmemişse hesaba katılmaz. Veri girilmiş ama o kök kullanılmıyorsa 0 sayılır.
Bir dil araştırılmış ama hiçbir aday kökü kullanmıyorsa kavram dosyasındaki `yok`
listesine yazılır. Tarihî tanıklar için aynısı `tarihi_yok` ile yapılır.

## 7. Ortak ölçüler

### Anlaşılırlık

Önerilen biçimi duyan bir dil konuşurunun onu ne kadar tanıyacağını ölçer:

```
dil o kökü kullanıyorsa:   tercih × (taban + (1 − taban) × ses_benzerliği)     taban = 0.5
kullanmıyorsa:             0
```

- **Taban:** Aynı kökten gelen bir kelime, sesleri farklı da olsa yarı yarıya
  tanıdıktır. Gerisini ses benzerliği belirler.
- **Ses benzerliği:** Harf değişimlerinin maliyetiyle ölçülür. Türk dillerinde
  düzenli olarak birbirine dönüşen sesler (t~d, ş~s, ğ~w~v, y~c~j, s~h, ünlü
  çiftleri…) yarım maliyetlidir, çünkü bir Türk kulağı bunları kolayca eşler.
- **Anlaşılırlık sadece Türkçe adaylar arasında karşılaştırılır.** Bir dilin
  alıntı kullanması, o dilde Türkçe adayın değerini 0 yapar; alıntının kendisi
  asla aday olmaz. Yani anlaşılırlık bizi alıntıya **itemez**.

### Eskilik (Hedef 1 ve 3)

Kökü kaydeden tarihî tanıkların ağırlıklı oranıdır. Bir dalda karar verilirken
o dalın kendi, üst ve alt dallarına bağlı tanıklar sayılır.

| Tanık | Dal | Ağırlık |
|---|---|---|
| Eski Türkçe (Göktürk, Uygur), 7.–11. yy | Ortak Türkçe | 3 |
| Karahanlıca (DLT, Kutadgu Bilig), 11.–12. yy | Ortak Türkçe | 2 |
| Volga Bulgarcası, 10.–14. yy | Oğur | 1 |
| Kuman-Kıpçakça, 13.–15. yy | Kıpçak | 1 |
| Eski Anadolu Türkçesi, 13.–15. yy | Oğuz | 1 |
| Harezm Türkçesi ve Çağatayca, 14.–19. yy | Karluk | 1 |

## 8. Seçim ve rapor

Her düğüm (ağız grubu, dil, dal, kol, en tepe) **sadece kendi altına bakarak**
kendi hedefine göre bir kök ve biçim seçer. Böylece her birleşim "burada ne
olmalı?" sorusuna kendi cevabını verir. Örneğin "dağ" için Oğuz kolunda *dağ*,
Kıpçak kolunda *taw*, en tepede *tağ* çıkar. En altta her dilin günlük
kullandığı biçim ayrıca not edilir.

Raporda her aday için üç ölçü yan yana gösterilir:

```
kök    1. yaygınlık puanı                 2. kök yaşı           3. anlayan kişi
uluğ   0.34 'uluğ' en düşük: Çuvaşça   Ortak Türkçe (5 hat)  ~87 milyon (%45)
bedük  0.07 'büyük' en düşük: Türkmen   Ana Türkçe (2 hat)    ~117 milyon (%60)
```

## 9. Ses kuralları (ertelendi)

Ses kurallarını baştan koymak, örneğin "kelime başında hep *t-*" demek, bazı
dillerin seslerini ötekilere dayatma tehlikesi taşır. Türk dillerinin ses
düzenleri birbirine benzese de aynı değildir: Çuvaşçanın *r/l*'si, Sahacanın
*s → h* değişimi, Kazakçanın *ş → s* değişimi gibi her kolun kendi yenilikleri
vardır. Bu yüzden:

- Şimdilik **ses kuralı konmaz**. Her kelimenin biçimi kendi başına seçilir.
- Yeterli kelime (~100) toplandığında Hedef 1'in seçtiği köprü biçimlerde
  **kendiliğinden oluşan** düzenlilikler incelenir. Kural ancak veriden
  çıkarsa ve bir kolun kendine özgü yeniliğini değil, çoğunluğun **ortak ve
  eski** durumunu yansıtıyorsa önerilir.

## 10. Çalışma sırası

Kelimeler **kullanım sıklığına** göre ele alınır. Önce zamirler, sayılar,
temel fiiller, edatlar, sonra temel isim ve sıfatlar gelir. Ekler dilbilgisi
aşamasında ele alınır. Sıra için: [`sozluk/SIRA.md`](sozluk/SIRA.md).

## 11. Yazım

Ortak Latin alfabesi kullanılır. Ortak Türk alfabesiyle uyum sonraki aşamada
kesinleştirilecek. Şimdilik çalışma yazımı Türkiye Türkçesi harflerine şunların
eklenmesiyle oluşur: `ä` (açık e / ə), `ñ` (nazal n), `w`, `x` (hırıltılı h),
`q` (art damak k, gerektiğinde). Verideki biçimler her dilin kendi yazısından
bu alfabeye aktarılır.

## 12. Doğrulama ve kaynaklar

Her kavram dosyasında `dogrulandi` alanı bulunur. Yapay zekâyla üretilen veri
`false` olarak girilir ve kaynakla kontrol edilene kadar öyle kalır.

Kullanılabilecek kaynaklar (sözlükler, etimoloji veritabanları, tarihî metinler,
derlemler, sınıflandırma, konuşur sayıları, anlaşılırlık çalışmaları) **kaynak
sözlüğünde** tutulur: [`kaynaklar/KAYNAKLAR.md`](kaynaklar/KAYNAKLAR.md). Her
kaynağın ne işe yaradığı, adresi, kapsadığı diller, nasıl kullanılacağı ve
güvenilirliği orada yazılıdır.

Kurallar:

- Her kelimede en az bir kaynak Wiktionary dışından olmalıdır.
- Kaynak kimlikleri kökün `kaynak` alanına yazılır (ör. `wiktionary-ana-turkce;
  savelyev-turkic`).
- Güveni düşük kaynaklar (küçük kelime listeleri, kaba tahminler) tek başına
  kanıt sayılmaz.
- **Çok kaynaklı doğrulama.** Bir biçim mümkün olduğunca birbirinden bağımsız
  birkaç kaynakla doğrulanır. Kural tabanlı bir araç (ör. Apertium), bir sözlük
  ya da çekim tablosu (ör. Wiktionary) ve gerçek metin (ör. Universal Dependencies
  derlemleri, Tatoeba) farklı türden kanıtlardır.
- **Çelişki incelenir, geçiştirilmez.** Kaynaklar birbirleriyle ya da yapay
  zekânın bilgisiyle çelişiyorsa, biri seçilip geçilmez. Nedeni aranır ve üçüncü
  bir kaynağa bakılır. Örnek: Azerbaycan Türkçesinde belirtme hâli. Apertium
  ünlüden sonra -yı veriyordu, Wiktionary ve UD derlemi -nı gösterdi; Apertium'un
  bu dosyası Türkiye Türkçesinden uyarlanmıştı.
- **Tek kaynaklı tanık işaretlenir.** Yalnız bir kaynağa dayanan tanığın notunda
  bu açıkça yazılır ("Tek kaynak").
- **Her tanık doğrulama durumunu taşır** (`denetim` alanı):
  `{durum, bicim: [kaynaklar], anlam: [kaynaklar]}`. `bicim`, biçimin o dilde
  var olduğunu gösteren kaynaklardır; `anlam`, o kavram anlamında kullanıldığını
  gösterenler. Durumlar:
  - `dogrulandi` ✓: biçim en az iki bağımsız kaynakta, anlam en az birinde.
  - `kismen` ◑: yalnız biçim doğrulandı ya da kanıt dolaylı.
  - `tek-kaynak` ◐: tek kaynak.
  - `celiski` ✗: kaynaklar birbiriyle ya da yapay zekânın bilgisiyle çelişiyor, çözülmedi.
  - `dogrulanmadi` ⚠: kaynak yok.

  Bağımsızlık sayılırken aynı kaynaktan aktarılan eserler bir sayılır (ör. DLT'yi
  Clauson'dan okuduysak `dlt; clauson` tek kaynaktır). Alan
  `python3 araclar/sozluk.py --denetim-doldur` ile var olan alanlardan kurallarla
  doldurulur; tanık değişirse `--yeniden` ile yeniden hesaplanır. Ne zaman ve hangi
  komutla denetlendiği tutulmaz; yöntem bu bölümde yazılıdır.
- **Çapraz doğrulama aracı.** `araclar/capraz_dogrula.py` yaşayan dil tanıklarını
  Apertium sözlüklerinde, Tatoeba ve UD derlemlerinde (yalnız biçim) ve ASJP'de
  (kavram ve kök) arar; bulunanı tanığın kaynak ve atıf alanına ekler. ASJP'de aynı
  kavram için başka bir kelime görülen tanıklar [`sozluk/CAPRAZ.md`](sozluk/CAPRAZ.md)
  inceleme listesine girer; araç onların durumunu değiştirmez. Notunda çözülmemiş
  çelişki yazan tanığa hiçbir araç dokunmaz.
- **Doğrulanmamış tanık silinmez, işaretlenir.** Hiçbir kaynakla doğrulanamayan
  biçim, yapay zekânın kendi bilgisinden (eğitim verisinden) gelir; nereden
  öğrenildiği gösterilemez. Böyle bir tanık `kaynak: bilgi` ile girilir ve notunda
  "Doğrulanmadı" yazar; sayfalarda ⚠ işaretiyle görünür. Kaynakla denetlenene kadar
  kanıt sayılmaz. Bir kaynak biçimin dilde var olduğunu gösterip anlamını
  göstermiyorsa bu da notta ayrıca yazılır.

## 13. Parametreler

Parametreler her hedef için ayrı ayrı [`hedefler.yaml`](hedefler.yaml)
dosyasında tutulur. Komut satırından seçili hedef için değiştirilebilir
(`--hedef nufus --beta 0.5` gibi).

| Parametre | 1. Ortak dil | 2. Ana Türkçe | 3. En çok kişi | Anlamı |
|---|---|---|---|---|
| yöntem | köprü | yaş | kişi | Ölçünün türü |
| benzerlik eşiği | 0.5 | — | — | Bu anlaşılırlığın altındaki komşular "aynı grup" sayılmaz |
| taban şartı | 100 bin üstü | — | — | Taban şartının uygulandığı diller |
| taban eşiği / cezası | 0.5 / 0.5 | — | — | Kimse geride kalmasın |
| ikinci dil | — | — | evet | İkinci dil yoluyla anlama sayılsın mı |
| β (`--beta`) | 0.2 | — | 0.2 | Eskiliğin etkisi |
| taban (`--taban`) | 0.5 | — | 0.5 | Aynı kökten ama sesleri farklı bir biçimin temel tanıdıklığı |
| ağız α | 0.5 | 0 (eşit) | 0.5 | Ağız sayısının dil içindeki ağırlığa etkisi |
| yazı dili payı | %50 | ağız gibi | %50 | Yazı dilinin dil içindeki payı |
| eşik (`--esik`) | 0.5 | — | 0.5 | Bu yayılımın altındaki kökler "canlandırma" sayılır |

## 14. Hedef 4: Tanıklı sözlük

Her **kök** için bir sözlük maddesi tutulur: `sozluk/kok/<kök>.yaml`. Madde
kavrama değil köke bağlıdır, çünkü anlam kökün peşinden gider. Bir kök dillerde
farklı anlamlara kayabilir ve birden çok kavrama hizmet edebilir. Kavram dosyası
"bu kavram için hangi kökler var, hangisini seçiyoruz?" sorusunu cevaplar. Madde
ise "bu kök nerede, ne zaman, nasıl yaşadı?" sorusunu.

### Tanık

Maddenin çekirdeği tanık listesidir. Her tanık tek bir kayıttır:

| Alan | Açıklama |
|---|---|
| `dil` | Dil ya da ağız kodu (`agac.yaml`), tarihî tanık kodu (`tarihi.yaml`) ya da dal kodu (`oguz`, `kipcak`: kaynak yalnızca "Oğuzlar", "Kıpçaklar" diyorsa) |
| `boy` | Kaynağın adlandırdığı boy ya da ağız (ör. Kâşgarlı'nın "Suvar"ı, Memlük kaynaklarının "Türkmen"i) |
| `yer` | Yer: Orhon, Kâşgar, Memlük Mısır'ı, Lviv, Erzurum… |
| `yuzyil` | Yüzyıl ya da aralık (`8`, `9-14`). Yazılmazsa kaynağın `yuzyil` alanından alınır; yaşayan dillerde varsayılan günümüzdür |
| `bicim` | Çalışma yazımıyla biçim (§11) |
| `yazi` | Özgün yazı: 𐰋𐰤, مَنْ, мин… |
| `anlam` | Bu tanıktaki anlam (kökün temel anlamından farklıysa mutlaka) |
| `metin` | Kelimenin geçtiği özgün metin (Kül Tigin, DLT, Codex Cumanicus…) |
| `kaynak`, `atif` | Bizim okuduğumuz kaynak (kaynak sözlüğü kimliği) ve madde/sayfa. Metin ile kaynak farklı olabilir: Codex Cumanicus'taki biçimi Grønbech'ten okuruz |
| `kaydeden`, `yabanci` | Kaydı tutan kişi ya da topluluk. Türk olmayan bir gözlemci ya da Türkçe olmayan bir dilde yazılmış sözlükse `yabanci: true` |

Kurallar:

- **Kaynaksız tanık yoktur.** Kaynakla doğrulanmamış, genel bilgiye dayanan
  biçim `kaynak: bilgi` diye yazılır ve raporda işaretlenir. Bunlar ilk fırsatta
  bir kaynakla değiştirilir.
- **Tarihî duraklar yalnızca kaynaklı tanıkla dolar.** Yaşayan bir dilin biçimi
  konuşurlarca denetlenebilir; yüzyıllar önceki bir biçim ancak kaynakla.
- **Özgün yazı ile çeviriyazı ayrı tutulur.** Yorum `not`'a yazılır, `bicim`'e
  değil.
- **Alıntılar da kaydedilir, ama seçilmez.** Bir dilde kök kaybolmuş ve yerine
  başka bir kelime geçmişse maddenin `yok` alanına "yerine X (Farsça)" diye
  yazılır. Bu, canlandırmada neyin öğretilmesi gerektiğini gösterir.
- Araştırılıp bulunamayan diller `yok`'a, tarihî duraklar `tarihi_yok`'a yazılır.
  Hiç bakılmamış olanlar yazılmaz; kapsamda eksik görünür.

### Kapsam (Hedef 4'ün ölçüsü)

Sözlük kelime seçmez; ölçüsü maddenin ne kadar eksiksiz olduğudur:

| Seviye | Şart |
|---|---|
| **1** | Bütün yaşayan diller: her dilde en az bir güncel tanık ya da `yok` kaydı. Ağız kapsamı ayrıca ölçülür |
| **2** | + zorunlu tarihî duraklar: Eski Türkçe, Karahanlıca, Harezm-Altın Orda, Memlük Kıpçakçası ve Codex Cumanicus, Eski Anadolu Türkçesi, Çağatayca, Osmanlıca |
| **3** | + en az bir yabancı kayıt (Çin yıllığı, Hotanca liste, Codex Cumanicus, Memlük sözlükçüleri, Avrupalı derlemeciler…) |

Duraklar ve eşikler [`hedefler.yaml`](hedefler.yaml)'da. Her kelimede hedef
Seviye 2'dir; önemli kelimelerde Seviye 3.

Raporda ayrıca tanık sayısı, kaynaklı tanık oranı, bağımsız kaynak sayısı ve en
eski tanığın yüzyılı gösterilir. Dizin: [`sozluk/SOZLUK.md`](sozluk/SOZLUK.md).

### Öteki hedeflerle bağ

- Kavram dosyasındaki `bicimler` ve `tarihi` alanları maddenin tanıklarının
  özetidir. `python3 araclar/sozluk.py --denetle` ikisini karşılaştırır.
  Uyuşmazlık varsa önce tanığa bakılır.
- Hedef 2 için maddenin en eski tanığı, kökün ağaçtaki yaşına ek bir kanıttır.
- "Öz Türkçe" ilkesi için tanıklar ödünç sınamasına yardım eder. Örneğin bir
  kelime ilk kez Moğol döneminde ve yalnız Moğolca temaslı dillerde görünüyorsa
  şüphelidir.

## 15. Yöntem sürümü

**Sürüm 1 — 2026-11-13** (197 kavramda yapılan ilk büyük gözden geçirmeden
sonra; bkz. [`GOZDEN-GECIRME.md`](GOZDEN-GECIRME.md)).

Kurallar ve ayarlar (bu dosya, `hedefler.yaml`, `ag.yaml`) bu sürümde
dondurulmuştur. Yeni kelimeler bu yöntemle eklenir. Değişiklik ancak iki
durumda yapılır:

1. **Veride gerçek bir sorun görülürse.** Örneğin bir kural açıkça yanlış
   sonuç veriyorsa ya da bir veri kaynağı sistemli olarak yanlış okunuyorsa.
   Bu tür düzeltmeler (yazım aktarımı, tanığın yanlış köke düşmesi gibi)
   yöntemi değiştirmez, veriyi düzeltir.
2. **Bir sonraki büyük gözden geçirmede** (~300 kavram). O noktada örgü
   `araclar/orgu.py --yaz` ile yeniden hesaplanır, ses düzeni ve ayrışan
   kavramlar yeniden incelenir, açık sorular karara bağlanır ve sürüm
   numarası artar.

Kural değişiklikleri burada sürüm numarası ve tarihle kaydedilir.

## 16. Hedef 5: Çeviri

**Soru:** Bir metni (cümleden sayfaya) Türk dilleri, ağızları ve ortak dil
arasında ne kadar iyi çevirebiliyoruz? Ayrıntılı plan:
[`uygulama/CEVIRI.md`](uygulama/CEVIRI.md).

- **Kelime seçmez.** Hedef 1–4'ün verisini kullanır: sözlük terim listesi
  olur, örgü en yakın aracı dili seçer, ses ve ek kuralları küçük dillere ve
  ağızlara dönüştürür.
- **Ölçüsü çeviri kalitesidir.** Her dil çifti açık bir test setiyle ölçülür
  (chrF). Sonuç sitede "iyi / deneysel / yok" diye gösterilir. Ölçülmemiş bir
  çift için kalite iddia edilmez.
- **Öz Türkçe ilkesi çeviride de geçerlidir.** Ortak dile ve ağızlara çeviride
  sözlükte öz Türkçe karşılığı olan kelime için alıntı kullanılmaz. Yaşayan bir
  yazı diline çeviride ise o dilin bugünkü kullanımı esastır; çeviri, dili
  olduğu gibi yazar, düzeltmez.
- **Tanık ile çeviri karışmaz.** Motorun ürettiği bir biçim hiçbir zaman
  sözlüğe tanık olarak girmez. Sözlüğe yalnız kaynaklı biçim girer (§14).
- **Python derleyicidir, uygulama okuyucudur.** Veri bu depoda üretilir; çeviri
  hizmeti (Euglena) yalnız buradaki çıktıları okur.
