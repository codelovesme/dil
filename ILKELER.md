# İlkeler

Bu belge projenin anayasasıdır. Kelime seçimiyle ilgili her karar buradaki
kurallara dayanmalı; kural değişecekse önce bu belge değişir.

## 1. Amaç

Bütün Türk kavimlerinin birbirini kolayca anlamasını sağlayacak **ortak bir Türk
dili** oluşturmak. Bunu yaparken:

- **Öz Türkçe** kelimeler kullanılır; Arapça, Farsça, Rusça, Moğolca vb.
  alıntılar elenir.
- **Eskilik** önceliklidir: Eski Türkçede tanıklanmış kelimeler öne çıkar.
- **Kavimler arası denge** gözetilir: bir topluluk ne nüfusuyla ne de içinde
  çok sayıda küçük dil barındırmasıyla diğerlerini ezebilir.

## 2. Kapsam: Türk dilleri ağacı

Yaşayan bütün Türk dilleri [`agac.yaml`](agac.yaml) dosyasında bir **ağaç**
olarak tutulur:

```
Türk dilleri
├── Oğur kolu ............ Çuvaşça
└── Ortak Türkçe
    ├── Halaç kolu
    ├── Oğuz kolu ........ Batı Oğuz, Doğu Oğuz, Salarca
    ├── Kıpçak kolu ...... Kıpçak-Bulgar, Kıpçak-Oğuz, Kıpçak-Nogay, Kırgızca
    ├── Karluk kolu ...... Özbekçe, Uygurca, İli Türkçesi
    └── Sibirya kolu ..... Kuzey Sibirya, Güney Sibirya (Sayan, Yenisey, Altay)
```

Sınıflandırmanın tartışmalı olduğu yerler dosyada `not` ile işaretlidir.
Ağaçta yapılan bir değişiklik bütün ağırlıkları otomatik olarak günceller.

## 3. Ağırlıklar: ne nüfus ne dil sayısı

İki tehlike var:

1. **Nüfus baskısı.** 80 milyonluk bir dil, 5 bin kişilik bir dili ezer.
   → Nüfus **hiç** kullanılmaz.
2. **Dil sayısı baskısı.** Kıpçak kolunda 12 dil, Oğur kolunda 1 dil var.
   Her dile eşit oy verirsek Kıpçak kolu tek başına kazanır.
   → Dillere de eşit oy verilmez.

**Çözüm: ağaç ağırlığı.** Ağacın her düğümünde, çocuklar arasındaki ağırlık
şöyle bölüşülür:

```
çocuğun ağırlığı  ∝  (çocuğun altındaki dil sayısı) ^ α
```

| α | Anlamı |
|---|---|
| `0` | Her dal eşit (Çuvaşça tek başına %50 alır, bu çok aşırı) |
| `1` | Her dil eşit (kalabalık kollar kazanır) |
| **`0.5`** (varsayılan) | Arası: büyük kol biraz daha ağır, ama dil sayısıyla doğru orantılı değil |

α = 0.5 ile en ağır dil %14.8 (Çuvaşça, kendi başına bir ana kol), en hafif
dil %1.7. Her dil eşit olsaydı herkes %2.9 alırdı. Tam tablo için:

```
python3 araclar/puanla.py --agirliklar
```

Gerekirse bir düğüme `agirlik_carpani` verilerek elle düzeltme yapılabilir, ama
bu istisna olmalı ve gerekçesi yazılmalıdır.

### Çuvaşçanın %14.8'i neden düzeltilmiyor?

Çuvaşça tek başına bir dil gibi görünür, ama aslında Ortak Türkçeden önce
ayrılmış bütün bir ana kolun (Oğur) tek yaşayan temsilcisidir. Ağırlığı bu yüzden
yüksek. Bu bilinçli bir karardır:

- **Tek başına kazanamaz.** Ortak Türkçe %85 ağırlığa sahip. Çuvaşça ancak öteki
  diller iki kök arasında neredeyse eşit bölündüğünde sonucu belirler.
- **Bu, istediğimiz şeydir.** Hem Çuvaşçada hem Ortak Türkçede bulunan bir kök,
  büyük olasılıkla Ana Türkçeye kadar uzanır. Başa baş durumda eskiden yana karar
  vermek, eskilik ilkesinin ta kendisidir.

## 3a. Tarihî tanıklar

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

## 4. Kök ve biçim

Her kavram için birden çok **aday kök** (etimon) olabilir. Örneğin "büyük" için:
`uluğ`, `bedük`, `çoñ`, `zur`… Her kökün dillerde farklı **biçimleri** vardır:
`tağ` → `dağ`, `taw`, `too`, `toğ`, `tu`…

Her kök kaydında şunlar bulunur:

| Alan | Açıklama |
|---|---|
| `kok` | Kökün kimliği |
| `tarihi` | Tarihî tanık kodu → biçim (ör. `{ otk: tağ, xqa: tağ, qwm: taw }`) |
| `koken` | `türkçe`, `alıntı:<dil>` veya `belirsiz` |
| `kaynak` | Dayanak |
| `bicimler` | Dil kodu → biçim. Eş anlamlılar için `tercih` (aşağıya bakın) |

### Tercih değerleri (bir dil içindeki eş anlamlılar)

| tercih | Anlamı |
|---|---|
| `1` | Asıl, günlük kelime (varsayılan) |
| `0.5` | Yaygın ama ikincil |
| `0.25` | Nadir, eskimiş, yazı dili, ya da anlamı kaymış |

## 5. Puan

Bir kökün bir düğümdeki **yayılımı**, çocuklarının yayılımlarının ağırlıklı
ortalamasıdır. Bir yaprakta (dilde) yayılım o dildeki `tercih` değeridir.

Bir kökün bir düğümdeki **eskiliği**, o düğümde sayılan tarihî tanıklardan
kökü kaydedenlerin ağırlıklı oranıdır (0–1).

```
puan = yayılım + β · eskilik        β = 0.2
```

- **Eleme:** Sadece `koken: türkçe` olan kökler seçilebilir. `belirsiz` olanlar
  araştırılana kadar seçilemez.
- **Eksik veri ≠ yok:** Bir dil için hiç veri girilmemişse o dil hesaba
  katılmaz (ortalamadan çıkar). Veri girilmiş ama o kök kullanılmıyorsa 0 sayılır.
  Her raporda verinin ağacın yüzde kaçını kapsadığı (`kapsama`) gösterilir.
  Bir dil araştırılmış ama kavram için hiçbir aday kökü kullanmıyorsa kavram
  dosyasındaki `yok` listesine yazılır. Tarihî tanıklar için de aynısı geçerli:
  araştırılmış ama kelime bulunamamışsa `tarihi_yok` listesine yazılır.

## 6. Seçim: ağaç boyunca yukarıdan aşağıya

1. **En tepe (Türk dilleri):** En yüksek puanlı Türkçe kök seçilir. Biçimi,
   **en eski tanığın biçimine en yakın yaşayan biçimdir**. Bugün kimsenin
   konuşmadığı bir biçim seçilmez: Eski Türkçe *sub* için *su*, *tağ* için
   *tağ* (Uygurca ve Hakasçada yaşıyor) seçilir. Yakınlık harf mesafesiyle
   ölçülür, eşitlikte daha yaygın biçim kazanır.
2. **Her dal:** Kendi alt ağacına göre en iyi kökü yeniden hesaplar.
   - Üst dalın kökü, en iyi seçenekten **δ'dan az geride** ise korunur
     (**süreklilik payı**, δ = 0.15). Böylece dil gereksiz yere parçalanmaz,
     ama bir dalın güçlü bir tercihi varsa (örneğin Oğuz kolunda `bedük` →
     *büyük*) o dal farklı bir eş anlamlı seçebilir.
   - Dalın biçimi, o kökün dalın dillerindeki **ağırlıkça en yaygın biçimidir**.
     Burada da süreklilik payı uygulanır: üst dalın biçimi yeterince yaygınsa
     korunur.
3. **Her dil (yaprak):**
   - **Ortak dildeki karşılığı:** Yukarıdaki kurala göre seçilir. Dil Türkçe
     kökü kaybetmişse (ör. alıntı kullanıyorsa) üst dalın kelimesi önerilir:
     bu, **yeniden canlandırmadır**.
   - **Günlük kullanım:** Dilin bugün en çok kullandığı biçim ayrıca not edilir.

## 7. Yazım

Ortak Latin alfabesi kullanılır. Ortak Türk alfabesiyle uyum sonraki aşamada
kesinleştirilecek. Şimdilik çalışma yazımı:

- Türkiye Türkçesi harfleri, artı `ä` (açık e / ə), `ñ` (nazal n), `w`,
  `x` (hırıltılı h), `q` (art damak k, gerektiğinde)
- Verideki biçimler, her dilin kendi yazısından bu alfabeye aktarılır.

## 8. Doğrulama ve kaynaklar

Her kavram dosyasında `dogrulandi` alanı bulunur. Yapay zekâyla üretilen veri
`false` olarak girilir ve kaynakla kontrol edilene kadar öyle kalır. Temel
kaynaklar:

- G. Clauson, *An Etymological Dictionary of Pre-Thirteenth-Century Turkish* (1972)
- Kâşgarlı Mahmud, *Dîvânu Lugâti't-Türk*
- E. V. Sevortyan vd., *Etimologičeskij slovar' tjurkskix jazykov*
- TDK, *Karşılaştırmalı Türk Lehçeleri Sözlüğü*
- M. Räsänen, *Versuch eines etymologischen Wörterbuchs der Türksprachen* (1969)

## 9. Parametreler

| Parametre | Varsayılan | Anlamı |
|---|---|---|
| α (`--alfa`) | 0.5 | Dil sayısının dal ağırlığına etkisi |
| β (`--beta`) | 0.2 | Eskilik (tarihî tanıklık) bonusu |
| δ (`--delta`) | 0.15 | Süreklilik payı (kök ve biçim) |
