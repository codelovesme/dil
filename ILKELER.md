# İlkeler

Bu belge projenin anayasasıdır. Kelime seçimiyle ilgili her karar buradaki
kurallara dayanmalı; kural değişecekse önce bu belge değişir.

## 1. Amaç ve hedefler

Türk topluluklarını öz Türkçe kelimelerle birbirine bağlamak. Aynı veriden
**üç ayrı soruya** cevap aranır. Bunlar farklı sorulardır ve her biri kendi
ölçüsünü ister. Ayarlar [`hedefler.yaml`](hedefler.yaml) dosyasındadır.

| | 1. Ortak dil **(asıl ürün)** | 2. Ana Türkçe tahmini | 3. En çok kişinin anladığı |
|---|---|---|---|
| **Soru** | Bütün Türk toplulukları birbirini anlasın: bir köprü dil | Türkçenin en eski hâli neydi? | En fazla insan anlasın |
| **Ölçü** | Köprü puanı: toplulukların anlaşılırlığı, kimse geride kalmasın | Kök yaşı: kök soy ağacının hangi düğümüne kadar gidiyor | Anlayan kişi sayısı |
| **Kullandığı yapı** | Örgü (`ag.yaml`) + konuşur sayıları | Soy ağacı (`agac.yaml`) + tarihî tanıklar | Konuşur sayıları + ikinci dil bağları |
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
| `sozluk/` | Kavramlar: her kökün dillerdeki biçimleri | Hepsi |

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
    ├── Oğuz kolu ........ Batı Oğuz (Türkiye-Balkan), Azerbaycan grubu, Doğu Oğuz
    ├── Kıpçak kolu ...... Kıpçak-Bulgar, Kıpçak-Oğuz (Kırım, Kafkas),
    │                      Kıpçak-Nogay, Kırgız-Kıpçak
    ├── Karluk kolu ...... Özbekçe, Doğu Karluk (Uygurca, İli Türkçesi)
    └── Sibirya kolu ..... Kuzey Sibirya, Güney Sibirya (Sayan, Yenisey-Altay)
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
| **Anlaşılırlık** | A dilini konuşan, B dilini öğrenmeden ne kadar anlar (dilbilimsel yakınlık) | Her iki yön ayrı yazılabilir | Hedef 1, 3 |
| **İkinci dil** | A konuşurları B'yi okul, medya ya da iki dillilik yoluyla ne kadar bilir | Dinleyen → konuşan | Sadece Hedef 3 |
| **Temas** | B dili A dilinden ne yoğunlukta kelime almış | Veren → alan | Hedef 2 (ödünç ayıklama) |

Anlaşılırlık ile ikinci dil bilinçli olarak ayrıdır. Halaçlar Azerbaycan
Türkçesini iyi bilir, ama iki dil birbirinden uzaktır. Hedef 1 kelimenin insanın
kendi dilinde nasıl duyulduğuyla ilgilendiği için ikinci dil bilgisini saymaz.

**Değerler şimdilik tahminidir.** Yalnızca önemli bağlar girilir, yazılmayan
çiftler 0 sayılır. Yaklaşık 100 kavram toplandığında bağlar kendi verimizden
(iki dilin ortak kök oranı ve biçim benzerliği) yeniden hesaplanacak ve
tahminlerle karşılaştırılacak. Böylece proje ilerledikçe örgü kendi kendini
düzeltir.

## 3. Hedef 1: Ortak dil (köprü dil)

Türkiyeli, Kazak, Özbek, Tatar ya da Saha bu dili en az çabayla anlayabilmeli,
kolayca öğrenebilmeli ve hiçbir topluluk onu "başkasının dili" olarak
görmemeli.

### Ağırlık: örgü + karekök kuralı

Kazakça ile Kırgızca, Özbekçe ile Uygurca, Türkiye Türkçesi ile Azerbaycan
Türkçesi zaten birbirini büyük ölçüde anlar. Köprü kurulması gereken yer bu
"anlaşılırlık çevrelerinin" **arasıdır**. Bu, iki katmanlı bir yapıdır: kişiler
çevrelerini, çevreler ortak dili belirler. Böyle bir yapıda her kişinin sesinin
eşit etkili olması için bilinen kural, her çevrenin oyunun nüfusunun
**karekökü** ile orantılı olmasıdır (Penrose kuralı). Örgüyle yazıldığında her
dilin ağırlığı:

```
ağırlık(L) = N_L / √(çevre_L)

çevre_L = N_L + Σ  pay(s(L, j)) × N_j        pay(s) = max(0, (s − 0.5) / 0.5)
              j
```

- `N`: konuşur sayısı, `s(L, j)`: L konuşurunun j dilini anlama düzeyi.
- **Eşik:** Yarı yarıya anlaşmak aynı çevrede olmak demek değildir. 0.5 ve
  altındaki anlaşılırlık çevreye katılmaz; üstü orantılı katılır.
- Bağlar "çevre içinde 1, dışında 0" olsaydı bu formül, dilleri kesin bölgelere
  ayırıp bölge nüfusunun karekökünü almakla tıpatıp aynı sonucu verirdi. Örgü,
  hiçbir dili bir bölgeye zorla sokmadan aynı hesabı yapar.

Sonuçta kollar şu ağırlıkları alır (tam tablo: [`AGIRLIKLAR.md`](AGIRLIKLAR.md)):

| Kol | Hedef 1 | Hedef 3 (karşılaştırma için) |
|---|---|---|
| Oğuz | %46.7 | %62.3 |
| Kıpçak | %24.5 | %13.1 |
| Karluk | %21.3 | %23.7 |
| Sibirya | %4.5 | %0.4 |
| Oğur | %2.5 | %0.4 |
| Halaç | %0.6 | %0.02 |

Karekök iki uç arasında doğal bir orta yoldur:

- **Nüfusa göre** tartılsaydı Batı Oğuz tek başına çoğunluğu alırdı ve ortak dil
  fiilen Türkiye Türkçesi olurdu.
- **Topluluklar eşit** tartılsaydı 42 bin kişilik Halaçlar 80 milyonluk
  Türkiye Türkçesiyle aynı oyu alırdı. Bu dili gerçekte kullanacak insanlar
  açısından bu adil değildir.

Ölmekte olan küçük diller (Tofaca, Soyotça, Fuyu Kırgızcası…) bu hedefte
neredeyse hiç ağırlık almaz, çünkü bu dilin kullanıcıları onlar olmayacak. Bu
dillerin değeri Hedef 2'de, Ana Türkçenin tanıkları olarak korunur.

### Kimse geride kalmamalı (taban şartı)

Ağırlıklı ortalama tek başına yetmez: ortalama yüksekken bir topluluk hiç
anlamıyor olabilir. Bu yüzden **büyük topluluklar** (1 milyondan çok konuşuru
olan diller) ayrıca denetlenir. Seçilen biçimi %50'den az anlayan büyük
toplulukların ağırlık payı, 0.5 ile çarpılarak puandan düşülür. Raporda her
büyük topluluğun anlaşılırlığı gösterilir.

Çuvaş, Saha ve Halaç toplulukları ses yapısı bakımından o kadar ayrışmıştır ki
hemen her kelimede en alt sırada kalırlar. Bunlara veto hakkı verilirse hiçbir
kelime seçilemez. Bu yüzden taban şartı büyük topluluklara uygulanır; küçük
toplulukların anlaşılırlığı ağaç çıktısında görünür.

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
kök    1. köprü puanı                 2. kök yaşı           3. anlayan kişi
uluğ   0.10 'uluğ' en düşük: Türkiye   Ortak Türkçe (5 hat)  ~87 milyon (%45)
bedük  0.31 'büyük' en düşük: Türkmen  Ana Türkçe (2 hat)    ~117 milyon (%60)
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
`false` olarak girilir ve kaynakla kontrol edilene kadar öyle kalır. Temel
kaynaklar:

- G. Clauson, *An Etymological Dictionary of Pre-Thirteenth-Century Turkish* (1972)
- Kâşgarlı Mahmud, *Dîvânu Lugâti't-Türk*
- E. V. Sevortyan vd., *Etimologičeskij slovar' tjurkskix jazykov*
- M. Räsänen, *Versuch eines etymologischen Wörterbuchs der Türksprachen* (1969)
- A. Dybo, StarLing Türk etimoloji veritabanı (Ana Türkçe kuruluşları)
- TDK, *Karşılaştırmalı Türk Lehçeleri Sözlüğü*; *Derleme Sözlüğü* (Anadolu ağızları)

## 13. Parametreler

Parametreler her hedef için ayrı ayrı [`hedefler.yaml`](hedefler.yaml)
dosyasında tutulur. Komut satırından seçili hedef için değiştirilebilir
(`--hedef nufus --beta 0.5` gibi).

| Parametre | 1. Ortak dil | 2. Ana Türkçe | 3. En çok kişi | Anlamı |
|---|---|---|---|---|
| yöntem | köprü | yaş | kişi | Ölçünün türü |
| çevre eşiği | 0.5 | — | — | Bu anlaşılırlığın altındaki komşular çevreye katılmaz |
| büyük topluluk | 1 milyon | — | — | Taban şartının uygulandığı diller |
| taban eşiği / cezası | 0.5 / 0.5 | — | — | Kimse geride kalmasın |
| ikinci dil | — | — | evet | İkinci dil yoluyla anlama sayılsın mı |
| β (`--beta`) | 0.2 | — | 0.2 | Eskiliğin etkisi |
| taban (`--taban`) | 0.5 | — | 0.5 | Aynı kökten ama sesleri farklı bir biçimin temel tanıdıklığı |
| ağız α | 0.5 | 0 (eşit) | 0.5 | Ağız sayısının dil içindeki ağırlığa etkisi |
| yazı dili payı | %50 | ağız gibi | %50 | Yazı dilinin dil içindeki payı |
| eşik (`--esik`) | 0.5 | — | 0.5 | Bu yayılımın altındaki kökler "canlandırma" sayılır |
