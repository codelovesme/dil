# İlkeler

Bu belge projenin anayasasıdır. Kelime seçimiyle ilgili her karar buradaki
kurallara dayanmalı; kural değişecekse önce bu belge değişir.

## 1. Amaç

Bugün yaşayan bütün Türk kavimlerinin **birbirini anlamasını** sağlayacak ortak
bir Türk dili oluşturmak. Bunu yaparken:

- **Öz Türkçe** kelimeler kullanılır; Arapça, Farsça, Rusça, Moğolca vb.
  alıntılar **hiçbir koşulda** seçilmez.
- **Anlaşılırlık** esastır: seçilen biçim, olabildiğince çok kavmin kulağına
  tanıdık gelmelidir.
- **Eskilik** önceliklidir: tarihî metinlerde tanıklanmış kelimeler ve biçimler
  öne çıkar.
- **Kavimler arası denge** gözetilir: bir topluluk ne nüfusuyla ne de içinde
  çok sayıda dil ya da ağız barındırmasıyla diğerlerini ezebilir.

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
kendi kodu (`tur`, `kaz`…) bu yazı dilini gösterir; o da ağızlardan biri gibi
tartılır.

### Ağacı kurma kuralları

Ağacın şekli ağırlıkları belirlediği için ağaç şu kurallarla kurulur:

1. **Diller birleştirilmez.** Her topluluğun dili ayrı bir yapraktır.
2. **Ağız eklemek serbesttir.** Ağırlıkları değiştirmez (§3).
3. **Dil eklemek ağırlıkları değiştirir.** Bu yüzden yeni bir dilin gerekçesi
   `not` alanına yazılır.
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

**Her birleşimde** çocuklar şu oranda tartılır:

```
çocuğun payı  ∝  (çocuğun sayımı) ^ α          α = 0.5
```

| Nerede? | Sayım |
|---|---|
| Dil düzeyinin **üstünde** (diller, dallar, kollar) | Altındaki **dil** sayısı |
| Bir dilin **içinde** (ağızlar, ağız grupları) | Altındaki **ağız** sayısı |

Bu ayrım önemlidir: **Bir dilin kaç ağzının yazıldığı, o dilin ve kolunun
ağırlığını değiştirmez.** Türkiye Türkçesinin 11 ağızlı olması ile Kırımçakçanın
ağızsız olması, ikisinin Batı Oğuz ve Kıpçak-Oğuz içindeki paylarını
etkilemez. Ağızlar sadece kendi dillerinin içinde neyin seçileceğini belirler.

### Ne nüfus ne dil sayısı

- **Nüfus hiç kullanılmaz.** 80 milyonluk bir dil, 5 bin kişilik bir dili ezemez.
- **Dil sayısı doğrudan kullanılmaz.** α = 1 olsaydı 16 dilli Kıpçak kolu tek
  başına kazanırdı. α = 0 olsaydı tek dilli Oğur kolu %50 alırdı. α = 0.5 ile
  büyük kol biraz daha ağırdır, ama dil sayısıyla doğru orantılı değildir.

Bütün ağırlıklar [`AGIRLIKLAR.md`](AGIRLIKLAR.md) dosyasındadır. Ağaç
değişince yeniden üretilir:

```
python3 araclar/puanla.py --agirliklar --agizlar --md > AGIRLIKLAR.md
```

Gerekirse bir düğüme `agirlik_carpani` verilerek elle düzeltme yapılabilir, ama
bu istisna olmalı ve gerekçesi yazılmalıdır.

### Çuvaşçanın %13.8'i neden düzeltilmiyor?

Çuvaşça, Ortak Türkçeden önce ayrılmış bütün bir ana kolun (Oğur) tek yaşayan
temsilcisidir. Ağırlığı bu yüzden yüksektir. Ama tek başına kazanamaz, çünkü
Ortak Türkçenin ağırlığı %86'dır. Sonucu ancak öteki diller iki kelime arasında
neredeyse eşit bölündüğünde belirler. O durumda da eskiden yana karar verdirir,
bu da eskilik ilkesinin ta kendisidir.

## 4. Tarihî tanıklar

Yaşayan diller bir kelimenin **bugünkü** yayılımını ölçer. Tarihî diller ise
**eskiliğini** ölçer. Bunlar [`tarihi.yaml`](tarihi.yaml) dosyasında tutulur ve
her biri ağaçtaki bir dala bağlıdır:

| Tanık | Dal | Ağırlık |
|---|---|---|
| Eski Türkçe (Göktürk, Uygur), 7.–11. yy | Ortak Türkçe | 3 |
| Karahanlıca (DLT, Kutadgu Bilig), 11.–12. yy | Ortak Türkçe | 2 |
| Volga Bulgarcası, 10.–14. yy | Oğur | 1 |
| Kuman-Kıpçakça, 13.–15. yy | Kıpçak | 1 |
| Eski Anadolu Türkçesi, 13.–15. yy | Oğuz | 1 |
| Harezm Türkçesi ve Çağatayca, 14.–19. yy | Karluk | 1 |

Tarihî diller yaşayan dillerin ağırlığını **değiştirmez**. Bir düğümde karar
verilirken o düğümün kendi tanıkları ile üst ve alt düğümlerinin tanıkları
sayılır. Örneğin Oğuz kolunda Eski Türkçe, Karahanlıca ve Eski Anadolu Türkçesi
sayılır, ama Kuman-Kıpçakça sayılmaz.

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

1. **Kök:**
   `kök puanı = anlaşılırlık (en iyi biçimiyle) + β × eskilik`. Burada β = 0.2
   ve sadece `koken: türkçe` olan kökler aday olabilir.
2. **Biçim:** Seçilen kökün, düğümün altında yaşayan biçimleri arasından
   `anlaşılırlık + β × (en eski tanık biçimine ses yakınlığı)` puanı en yüksek
   olan seçilir. Bugün kimsenin kullanmadığı bir biçim seçilmez.

Böylece her birleşim "burada ne olmalı?" sorusuna kendi cevabını verir:

- Oğuz kolunda *dağ*, Kıpçak kolunda *taw*, en tepede *tağ* çıkar.
- "Büyük" için Oğuz kolunda *büyük* (`bedük` kökü), en tepede *uluğ* çıkar.
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

| Parametre | Varsayılan | Anlamı |
|---|---|---|
| α (`--alfa`) | 0.5 | Dil/ağız sayısının ağırlığa etkisi |
| β (`--beta`) | 0.2 | Eskiliğin etkisi |
| taban (`--taban`) | 0.5 | Aynı kökten ama sesleri farklı bir biçimin temel tanıdıklığı |
| eşik (`--esik`) | 0.5 | Bu yayılımın altındaki kökler "canlandırma" sayılır |
