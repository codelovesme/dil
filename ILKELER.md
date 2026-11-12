# İlkeler

Bu belge projenin anayasasıdır. Kelime seçimiyle ilgili her karar buradaki
kurallara dayanmalı; kural değişecekse önce bu belge değişir.

## 1. Amaç ve hedefler

Türk kavimlerini öz Türkçe kelimelerle birbirine bağlamak. Aynı veriden
**üç ayrı hedefe** cevap aranır, çünkü bunlar farklı sorulardır ve her biri
farklı bir ağırlık ister. Hedeflerin ayarları [`hedefler.yaml`](hedefler.yaml)
dosyasındadır.

| | 1. Ortak dil **(asıl ürün)** | 2. Ana Türkçe tahmini | 3. En çok kişinin anladığı |
|---|---|---|---|
| **Soru** | Bütün Türk kavimleri birbirini anlasın | Türkçenin en eski hâli neydi? | En fazla insan anlasın |
| **Ne sayılır** | Kavim / topluluk | Soy hattı (dal) | Kişi |
| **Ağırlık** | Her dil kendi büyüklük basamağıyla (kavimler eşit, kalabalık ezemez) | Her ayrılıkta dallar eşit (Oğur %50, Ortak Türkçe %50); nüfus sayılmaz | Doğrudan konuşur sayısı |
| **Ölçü** | Anlaşılırlık | Yayılım (kök hangi soy hatlarında yaşıyor) | Anlaşılırlık |
| **Eskilik** | Küçük bonus (β = 0.2) | Ana ölçü kadar önemli (β = 1.0), Ana Türkçe tanıklığı dahil | Küçük bonus (β = 0.2) |
| **Biçim** | En anlaşılır yaşayan biçim | Dalın en eski tanığının biçimi; yaşamasa da olur | En anlaşılır yaşayan biçim |

Üç hedefte de geçerli olanlar:

- **Öz Türkçe:** Arapça, Farsça, Rusça, Moğolca vb. alıntılar **hiçbir koşulda**
  seçilmez.
- **Alttan yukarı hesap** ve aynı ağaç, aynı veri.
- **Karşılaştırma:** Üç hedefin aynı kökü seçtiği kavramlar sağlamdır. Ayrıştığı
  kavramlar tartışmaya açılır ve ayrıca listelenir:

```
python3 araclar/puanla.py --karsilastir
```

Asıl ürün, **Hedef 1: Ortak dil**dir. Hedef 2 ve 3 kaynak ve karşılaştırma
içindir. Hedef 1'in ilkeleri:

- **Anlaşılırlık** esastır: seçilen biçim, olabildiğince çok kavmin kulağına
  tanıdık gelmelidir.
- **Eskilik** eşitlik bozucudur: tarihî metinlerde tanıklanmış kelimeler ve
  biçimler öne çıkar.
- **Kavimler arası denge** gözetilir: bir topluluk ne nüfusuyla ne de içinde
  çok sayıda dil ya da ağız barındırmasıyla diğerlerini ezebilir. Kişi sayısı
  sayılır, ama sadece büyüklük basamağı olarak (§3).

## 2. Türk dilleri ağacı

Yaşayan bütün Türk dilleri ve bilinen ağızları [`agac.yaml`](agac.yaml)
dosyasında bir **ağaç** olarak tutulur (40 dil, 89 ağız):

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
kendi kodu (`tur`, `kaz`…) bu yazı dilini gösterir. Hedef 1 ve 3'te yazı dili
dilin içinde **%50** pay alır, ağızlar kalan %50'yi paylaşır; çünkü anlaşılırlık
açısından yazı dili o dili konuşan herkesin ortak paydasıdır. Hedef 2'de yazı
dili ağızlardan biri gibi sayılır, çünkü eski biçimleri çoğu zaman ağızlar
korur.

### Ağacı kurma kuralları

Ağacın şekli ağırlıkları belirlediği için ağaç şu kurallarla kurulur:

1. **Diller birleştirilmez.** Her topluluğun dili ayrı bir yapraktır.
2. **Ağız eklemek serbesttir.** Ağırlıkları değiştirmez (§3).
3. **Dil eklemek ağırlıkları değiştirir.** Bu yüzden yeni bir dilin gerekçesi
   `not` alanına, yaklaşık konuşur sayısı da `konusur` alanına yazılır.
4. **Birbirine çok yakın diller ortak bir alt grupta toplanır.** Örneğin Kırım
   Tatarcası, Karayca, Kırımçakça ve Urumca "Kırım grubu"nda; Tofaca, Duhaca ve
   Soyotça "Tayga Sayan"da toplanır. Böylece payı aralarında paylaşırlar ve
   sayıca çoğalmaları dalı şişirmez.
5. **Tek dilli alt dal açılmaz.** Kardeşleri arasında tek başına duran bir dil,
   gruplanmış dillerden daha fazla pay alır. Örneğin eskiden Salarca Türkiye
   Türkçesinin iki katı ağırlıktaydı. Bunun istisnası, gerçekten ayrı bir soy
   hattını temsil edenlerdir: Çuvaşça, Halaçça, Özbekçe, Tuvaca, Sarı Uygurca.
6. **Sınıflandırmada görüş ayrılığı olan yerler `not` ile belirtilir.** Bu
   durumda seçim, anlaşılırlık amacına uygun olandan yana yapılır. Örneğin
   Güney Altayca, Kırgızcaya yakınlığı nedeniyle Kırgız-Kıpçak grubuna
   alınmıştır.
7. **Kapsam dışı kalanlar:** Aynu dili (dilbilgisi Türkçe, söz varlığı büyük
   ölçüde Farsça) ve dilini kaybetmiş topluluklar (ör. Litvanya Tatarları).

## 3. Ağırlıklar

### Hesap alttan yukarı yapılır

Bir kelime araştırılırken önce en alttaki ağızlara bakılır: Ege ağzı *su*'ya ne
diyor, Rumeli ağızları ne diyor? Ağızlar birleşir ve Türkiye Türkçesinde ne
olması gerektiğine karar verilir. Diller birleşir ve Batı Oğuz için karar
verilir. Bu böyle devam ederek en tepeye, ortak dile ulaşılır.

**Her birleşimde** çocuklar şu oranda tartılır (Hedef 1):

| Nerede? | Çocuğun ağırlığı |
|---|---|
| Dil düzeyinde ve **üstünde** (diller, dallar, kollar) | altındaki dillerin **basamaklarının toplamı** |
| Bir dilin **içinde** | yazı dili %50; ağızlar kalan %50'yi (ağız sayısı)^0.5 oranında paylaşır |

Yani Hedef 1'de her dil, ağaçta nerede durursa dursun, **sadece kendi
basamağıyla** tartılır. Ağaç, kararların hangi sırayla birleştirildiğini
belirler, ama bir dilin ağırlığını değiştirmez.

### Büyüklük basamağı: kişi sayısı sayılır ama ezemez

Temel kriterimiz şudur: *bir kelimenin kaç kavim/ülke tarafından kullanıldığı,
kaç kişi tarafından kullanıldığından daha önemlidir.* Kişi sayısı daha az
önemlidir, ama yok sayılmaz. Bu yüzden her dilin konuşur sayısı doğrudan değil,
**basamak** olarak hesaba girer. Konuşur sayısı her 10 kat arttığında dil 1
puan alır:

| Konuşur sayısı | Basamak | Örnek |
|---|---|---|
| 10 milyon ve üstü | 8 | Türkiye Türkçesi, Azerbaycan Türkçesi, Özbekçe, Kazakça, Uygurca |
| 1 – 10 milyon | 7 | Türkmence, Tatarca, Başkurtça, Kırgızca, Irak Türkmencesi |
| 100 bin – 1 milyon | 6 | Çuvaşça, Gagavuzca, Kaşkayca, Kırım Tatarcası, Sahaca, Tuvaca |
| 10 – 100 bin | 5 | Halaçça, Salarca, Nogayca, Hakasça, Güney Altayca, Balkan Gagavuz Türkçesi |
| 1 – 10 bin | 4 | Sarı Uygurca, Şorca, Kuzey Altayca |
| 100 – 1 000 | 3 | Urumca, İli Türkçesi, Dolganca, Duhaca |
| 100'den az | 2 | Karayca, Kırımçakça, Tofaca, Soyotça, Çulımca, Fuyu Kırgızcası |

- **Kalabalık ezemez.** 80 milyonluk Türkiye Türkçesi (basamak 8) ile 3 bin
  kişilik Şorca (basamak 4) arasında 27.000 kat kişi farkı vardır, basamak
  farkı ise sadece 2 kattır.
- **Hata payına dayanıklıdır.** Konuşur sayıları yaklaşıktır ve
  [`agac.yaml`](agac.yaml) dosyasında `konusur` alanında tutulur. Belirsiz
  olanlara `konusur_not` yazılır (tahmin aralığı, kaynak, tanım farkı). Bir
  tahmin 2 kat yanlış olsa bile basamak çoğu zaman değişmez.
- **Aynı insanlar iki kez sayılmaz.** Bir kaynağın sayısı başka bir dilin
  ağzını da kapsıyorsa düşülür. Örneğin Ethnologue'un Balkan Gagavuz Türkçesi
  için verdiği ~460 bin, Türkiye'deki Yörükleri de sayar. Biz onları Türkiye
  Türkçesinin ağzı olarak tuttuğumuz için burada sadece Balkan toplulukları
  ve Surguçlar (~11 bin) sayılır.
- **Ağaçtaki yer ağırlığı değiştirmez.** Eskiden bir dalın ağırlığı
  (ortalama basamak) × (dil sayısı)^0.5 idi. Bu durumda seyrek bir daldaki dil,
  kalabalık bir daldakinden ağır çıkıyordu: 120 kişilik İli Türkçesi %2.0,
  400 bin kişilik Kırım Tatarcası %1.4 alıyordu. Ayrıca ağırlıklar, tartışmalı
  sınıflandırma kararlarına bağlı kalıyordu. Şimdi (α = 1) Türkiye Türkçesi,
  Kazakça ve Özbekçe eşittir (üçü de basamak 8, %3.9); Kırım Tatarcası İli
  Türkçesinin iki katıdır. Ağacın yapısı yalnızca Hedef 2'de, soyun önemli
  olduğu yerde belirleyicidir.
- **Küçük diller şişmez.** Basamak 2 alan en küçük altı dilin toplamı %6'dır,
  yani bir buçuk büyük dil kadar. Bunun bedeli, kolların kavim sayısına göre
  ağırlık almasıdır (14 kavimli Kıpçak kolu %37, 3 kavimli Karluk kolu %9). Bu,
  "herkes anlasın" hedefine uygundur: daha çok kavim anlıyorsa daha çok
  ağırlık.
- **Tesadüfi eşitlik olmaz.** Basamak olmadan bütün diller 1 birim
  sayılıyordu. O zaman ağırlığı sadece ağacın şekli belirliyordu ve simetrik
  bir dalda (ör. 3 grup × 3 dilden oluşan Oğuz kolu) Türkiye Türkçesi
  Kaşkaycayla eşit çıkıyordu.

### Ağızlar ağırlığı değiştirmez

**Bir dilin kaç ağzının yazıldığı, o dilin ve kolunun ağırlığını
değiştirmez.** Türkiye Türkçesinin 12 ağızlı olması ile Kırımçakçanın ağızsız
olması, ikisinin ağırlıklarını etkilemez. Ağızlar sadece kendi dillerinin
içinde neyin seçileceğini belirler.

Bütün ağırlıklar [`AGIRLIKLAR.md`](AGIRLIKLAR.md) dosyasındadır. Ağaç
değişince yeniden üretilir:

```
python3 araclar/puanla.py --agirliklar --agizlar --md > AGIRLIKLAR.md
```

Gerekirse bir düğüme `agirlik_carpani` verilerek elle düzeltme yapılabilir, ama
bu istisna olmalı ve gerekçesi yazılmalıdır.

### Hedeflere göre ağırlık

Bu bölümdeki basamak kuralı **Hedef 1** içindir. Öteki hedefler aynı ağacı
farklı tartar:

| Kol | 1. Ortak dil | 2. Ana Türkçe | 3. En çok kişi |
|---|---|---|---|
| Oğur (Çuvaşça) | %2.9 | %50 | %0.4 |
| Halaç | %2.4 | %10 | %0.02 |
| Oğuz | %28.0 | %10 | %62.3 |
| Kıpçak | %36.7 | %10 | %13.1 |
| Karluk | %9.2 | %10 | %23.7 |
| Sibirya | %20.8 | %10 | %0.4 |

Tam tablolar [`AGIRLIKLAR.md`](AGIRLIKLAR.md) dosyasındadır.

**Hedef 1'de her dil kendi basamağıyla tartılır.** Çuvaşça, anlaşılması
gereken bir topluluk olarak sıradan bir dildir: yaklaşık 740 bin konuşur,
basamak 6, ağırlık %2.9. Ortak Türkçe düğümü şeffaftır (`seffaf: true`): soy
bilgisi olarak ağaçta durur, Hedef 1 ve 3'te ağırlık hesabında atlanır.

**Hedef 2'de ağaç olduğu gibi tartılır.** Burada soru topluluk değil soydur.
Türk dillerinin ilk ayrılığı Oğur ile Ortak Türkçe arasında olduğu için Çuvaşça
%50 alır. Bu hedefte Çuvaşça en önemli tanıktır.

**Hedef 3'te doğrudan konuşur sayısı kullanılır.** Türkiye Türkçesi tek başına
%41 alır; Oğuz, Karluk ve Kıpçak kolları ağırlığın %99'unu toplar.

## 4. Tarihî tanıklar

Yaşayan diller bir kelimenin **bugünkü** yayılımını ölçer. Tarihî diller ise
**eskiliğini** ölçer. Bunlar [`tarihi.yaml`](tarihi.yaml) dosyasında tutulur ve
her biri ağaçtaki bir dala bağlıdır:

| Tanık | Dal | Ağırlık |
|---|---|---|
| **Ana Türkçe tanıklığı** (türetilmiş, aşağıya bakın) | Türk dilleri | 2 |
| Eski Türkçe (Göktürk, Uygur), 7.–11. yy | Ortak Türkçe | 3 |
| Karahanlıca (DLT, Kutadgu Bilig), 11.–12. yy | Ortak Türkçe | 2 |
| Volga Bulgarcası, 10.–14. yy | Oğur | 1 |
| Kuman-Kıpçakça, 13.–15. yy | Kıpçak | 1 |
| Eski Anadolu Türkçesi, 13.–15. yy | Oğuz | 1 |
| Harezm Türkçesi ve Çağatayca, 14.–19. yy | Karluk | 1 |

Tarihî diller yaşayan dillerin ağırlığını **değiştirmez**. Bir düğümde karar
verilirken hangi tanıkların sayılacağı hedefe göre değişir:

- **Hedef 1 ve 3:** Düğümün kendi tanıkları ile üst ve alt düğümlerinin
  tanıkları sayılır. Örneğin Oğuz kolunda Eski Türkçe, Karahanlıca ve Eski
  Anadolu Türkçesi sayılır, ama Kuman-Kıpçakça sayılmaz. Bu, eski kelimeye
  genel bir eğilim verir.
- **Hedef 2:** Sadece düğümün kendi ve alt düğümlerinin tanıkları sayılır.
  "Kıpçakçanın en eski hâli neydi?" sorusunu yalnızca Kıpçak kanıtı cevaplar.
  Biçim de dalın kendi en eski tanığından alınır: Oğuz için Eski Anadolu
  Türkçesi, Kıpçak için Kuman-Kıpçakça, en tepe için Eski Türkçe.

### Ana Türkçe tanıklığı

Türk dillerinin ilk ayrılığı Oğur ile Ortak Türkçe arasındadır. Bir kök **iki
tarafta da** bulunuyorsa, ayrılıktan önce de vardı, yani Ana Türkçeye kadar
uzanır. Bu tanık bir metin değildir; kendiliğinden hesaplanır:

- Kök Oğur kolunda (Çuvaşçada ya da Volga Bulgarcasında) **ve** Ortak Türkçede
  (yaşayan bir dilde ya da tarihî bir tanıkta) varsa tanıklanmış sayılır.
- İki taraftan birinde hiç veri yoksa hesaba katılmaz.
- **Sadece Hedef 2'de ve sadece en tepede** sayılır. Hedef 1'de sayılmaz,
  çünkü orada soru eskilik değil anlaşılırlıktır.
- Kavramın bir kökü için bilim insanlarının yeniden kurduğu Ana Türkçe biçim
  biliniyorsa `ana_turkce` alanına yazılır (ör. `ana_turkce: "*tāš"`). Hedef 2
  raporunda kendi sonucumuzla yan yana gösterilir. Gerçek yeniden kuruluş
  ses kurallarına dayanan karşılaştırmalı yöntemle yapılır; bizim sonucumuz bir
  yaklaşımdır.

Örneğin "büyük" için *bedük* kökü Çuvaşçada *pısăk* olarak yaşadığı için bu
tanıklığı alır; *uluğ* almaz.

## 5. Kök ve biçim

Her kavram için birden çok **aday kök** (etimon) olabilir. Örneğin "büyük" için
`uluğ`, `bedük`, `çoñ`, `zur`… Her kökün dillerde farklı **biçimleri** vardır.
Örneğin `tağ` kökü dillerde `dağ`, `taw`, `too`, `toğ`, `tu` olarak yaşar.

Her kök kaydında şunlar bulunur:

| Alan | Açıklama |
|---|---|
| `kok` | Kökün kimliği |
| `koken` | `türkçe`, `alıntı:<dil>` veya `belirsiz` |
| `tarihi` | Tarihî tanık kodu → biçim (ör. `{ otk: tağ, xqa: tağ, qwm: taw }`) |
| `bicimler` | Dil ya da ağız kodu → biçim, gerekirse `tercih` ile |
| `kaynak`, `not` | Dayanak ve açıklama |

### Tercih değerleri (bir dil içindeki eş anlamlılar)

| tercih | Anlamı |
|---|---|
| `1` | Asıl, günlük kelime (varsayılan) |
| `0.5` | Yaygın ama ikincil |
| `0.25` | Nadir, eskimiş, yazı dilinde kalmış, ya da anlamı kaymış |

## 6. Ölçüler

Üç ölçü vardır, üçü de 0 ile 1 arasındadır ve alttan yukarı aynı ağırlıklarla
hesaplanır.

### Yayılım: kök yaşıyor mu?

Bir dilde (ağızda) değeri o dildeki `tercih` değeridir, kökü kullanmıyorsa 0'dır.

### Anlaşılırlık: biçim tanınıyor mu?

Önerilen biçimi duyan bir dil konuşurunun onu ne kadar tanıyacağını ölçer:

```
dil o kökü kullanıyorsa:   tercih × (taban + (1 − taban) × ses_benzerliği)     taban = 0.5
kullanmıyorsa:             0
```

- **Taban:** Aynı kökten gelen bir kelime, sesleri farklı da olsa yarı yarıya
  tanıdıktır. Gerisini ses benzerliği belirler.
- **Ses benzerliği:** Harf değişimlerinin maliyetiyle ölçülür. Türk dillerinde
  düzenli olarak birbirine dönüşen sesler (t~d, ş~s, ğ~w~v, y~c~j, s~h, ünlü
  çiftleri…) **yarım maliyetlidir**, çünkü bir Türk kulağı bunları kolayca
  eşler.
- **Anlaşılırlık sadece Türkçe adaylar arasında karşılaştırılır.** Bir dilin
  alıntı kullanması, o dilde Türkçe adayın değerini 0 yapar. Ama alıntının
  kendisi asla aday olmaz. Yani anlaşılırlık bizi alıntıya **itemez**.

### Eskilik: tarihte var mı?

Kökü kaydeden tarihî tanıkların ağırlıklı oranıdır.

### Eksik veri yok demek değildir

Bir dil ya da ağız için hiç veri girilmemişse hesaba katılmaz, ortalamadan
çıkar. Veri girilmiş ama o kök kullanılmıyorsa 0 sayılır. Bir dil araştırılmış
ama hiçbir aday kökü kullanmıyorsa kavram dosyasındaki `yok` listesine yazılır.
Tarihî tanıklar için aynısı `tarihi_yok` listesiyle yapılır.

## 7. Seçim

Her düğüm (ağız grubu, dil, dal, kol, en tepe) **sadece kendi altına bakarak**
iki karar verir:

1. **Kök:** `kök puanı = ölçü + β × eskilik`. Sadece `koken: türkçe` olan
   kökler aday olabilir.
   - Hedef 1 ve 3'te ölçü, kökün en iyi biçiminin **anlaşılırlığıdır** (β = 0.2).
   - Hedef 2'de ölçü, kökün soy hatlarındaki **yayılımıdır** (β = 1.0).
2. **Biçim:**
   - Hedef 1 ve 3'te, seçilen kökün düğümün altında yaşayan biçimleri arasından
     `anlaşılırlık + β × (en eski tanık biçimine ses yakınlığı)` puanı en
     yüksek olan seçilir. Bugün kimsenin kullanmadığı bir biçim seçilmez.
   - Hedef 2'de, dalın kendi en eski tanığının biçimi seçilir (ör. Eski Türkçe
     *sub*). Tanık yoksa dalın en yaygın biçimi alınır.

Böylece her birleşim "burada ne olmalı?" sorusuna kendi cevabını verir:

- Oğuz kolunda *dağ*, Kıpçak kolunda *taw*, en tepede *tağ* çıkar.
- "Büyük" için Hedef 1'de Oğuz kolunda *büyük* (`bedük` kökü), en tepede
  *uluğ* çıkar. Hedef 2'de en tepede *bedük*, Hedef 3'te *büyük* çıkar.
- En altta her dilin günlük kullandığı biçim ayrıca not edilir.

### Canlandırma

Bir dil seçilen Türkçe kökü kaybetmişse, örneğin alıntı kullanıyorsa, ona üst
dalın kelimesi önerilir ve raporda **"canlandırma"** olarak işaretlenir. En
tepede seçilen kök bugün dillerin ağırlıkça %50'sinden azında yaşıyorsa, bütün
kavram canlandırma olarak işaretlenir. Bu, bedelin görünmesi içindir: o kelimenin
öğretilmesi gerekecektir.

### En az anlayan topluluk

Her raporda en tepedeki seçimin **her ana kolda** ne kadar anlaşıldığı
gösterilir ve en az anlayan kol işaretlenir. Ortalama iyi olsa bile geride
kalan bir topluluk varsa görülür.

## 8. Ses kuralları (ertelendi)

Ses kurallarını baştan koymak, örneğin "kelime başında hep *t-*" demek, bazı
dillerin seslerini ötekilere dayatma tehlikesi taşır. Ayrıca Türk dillerinin
ses düzenleri birbirine benzese de aynı değildir. Çuvaşçanın *r/l*'si,
Sahacanın *s → h* değişimi, Kazakçanın *ş → s* değişimi gibi her kolun kendi
yenilikleri vardır. Bu yüzden:

- Şimdilik **ses kuralı konmaz**. Her kelimenin biçimi, anlaşılırlık ve eskilik
  ölçüleriyle kendi başına seçilir.
- Yeterli kelime (~100) toplandığında seçilen biçimlerde **kendiliğinden
  oluşan** düzenlilikler incelenir. Kural ancak veriden çıkarsa ve bir kolun
  kendine özgü yeniliğini değil, çoğunluğun **ortak ve eski** durumunu
  yansıtıyorsa önerilir.

## 9. Çalışma sırası

Kelimeler **kullanım sıklığına** göre ele alınır. Önce zamirler, sayılar,
temel fiiller, edatlar, sonra temel isim ve sıfatlar gelir. Ekler dilbilgisi
aşamasında ele alınır. Sıra için: [`sozluk/SIRA.md`](sozluk/SIRA.md).

## 10. Yazım

Ortak Latin alfabesi kullanılır. Ortak Türk alfabesiyle uyum sonraki aşamada
kesinleştirilecek. Şimdilik çalışma yazımı Türkiye Türkçesi harflerine şunların
eklenmesiyle oluşur: `ä` (açık e / ə), `ñ` (nazal n), `w`, `x` (hırıltılı h),
`q` (art damak k, gerektiğinde). Verideki biçimler, her dilin kendi yazısından
bu alfabeye aktarılır.

## 11. Doğrulama ve kaynaklar

Her kavram dosyasında `dogrulandi` alanı bulunur. Yapay zekâyla üretilen veri
`false` olarak girilir ve kaynakla kontrol edilene kadar öyle kalır. Temel
kaynaklar:

- G. Clauson, *An Etymological Dictionary of Pre-Thirteenth-Century Turkish* (1972)
- Kâşgarlı Mahmud, *Dîvânu Lugâti't-Türk*
- E. V. Sevortyan vd., *Etimologičeskij slovar' tjurkskix jazykov*
- M. Räsänen, *Versuch eines etymologischen Wörterbuchs der Türksprachen* (1969)
- TDK, *Karşılaştırmalı Türk Lehçeleri Sözlüğü*; *Derleme Sözlüğü* (Anadolu ağızları)

## 12. Parametreler

Parametreler her hedef için ayrı ayrı [`hedefler.yaml`](hedefler.yaml)
dosyasında tutulur. Komut satırından seçili hedef için değiştirilebilir
(`--hedef ana --beta 0.5` gibi).

| Parametre | 1. Ortak dil | 2. Ana Türkçe | 3. En çok kişi | Anlamı |
|---|---|---|---|---|
| ağırlık | basamak | soy | nüfus | Dillerin ve dalların nasıl tartıldığı (§3) |
| α (`--alfa`) | 1.0 | — | — | Dil sayısının dal ağırlığına etkisi (1: her dil kendi basamağıyla) |
| ağız α | 0.5 | — | 0.5 | Ağız sayısının dil içindeki ağırlığa etkisi |
| yazı dili payı | %50 | ağız gibi | %50 | Yazı dilinin dil içindeki payı |
| β (`--beta`) | 0.2 | 1.0 | 0.2 | Eskiliğin etkisi |
| taban (`--taban`) | 0.5 | — | 0.5 | Aynı kökten ama sesleri farklı bir biçimin temel tanıdıklığı |
| eşik (`--esik`) | 0.5 | — | 0.5 | Bu yayılımın altındaki kökler "canlandırma" sayılır |
