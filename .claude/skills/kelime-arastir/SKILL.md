---
name: kelime-arastir
description: Ortak Türk dili için bir kavramı/kelimeyi bütün Türk dillerinde araştırır, sozluk/ altına kavram dosyasını yazar, puanlar ve sonucu raporlar. Kullanıcı "X'i araştır", "X kelimesine bak", "X ekle" dediğinde kullan.
---

# Kelime araştırma yöntemi

Kullanıcı tek bir kavram verir (ör. "göz", "gelmek", "büyük"). Amaç, o kavramın
`agac.yaml`'daki **yaşayan dillerdeki ve ağızlarındaki** ve `tarihi.yaml`'daki
**tarihî tanıklardaki** karşılıklarını toplamak, kökenlerini belirlemek ve
`araclar/puanla.py` ile ortak dildeki karşılığını seçmektir. Kurallar
`ILKELER.md`'dedir; önce onu oku.

## 1. Kavramı netleştir

- Anlamı tek cümleyle ve İngilizce karşılığıyla yaz. Anlam belirsizse (ör.
  "yüz": sayı mı, surat mı?) kullanıcıya **tek soru** sor, sonra devam et.
- Dosya adı: ASCII, küçük harf (`göz` → `goz.yaml`, `gelmek` → `gel.yaml`).
  Fiiller kök hâliyle yazılır. Anlam ayrımı gerekirse sonek ekle (`yuz-sayi.yaml`).
- Temel söz varlığı → `sozluk/temel/`. Diğerleri konuya göre
  (`sozluk/doga/`, `sozluk/aile/` …); klasör yoksa oluştur.

## 2. Araştır

Kaynakları **kaynak sözlüğünden** seç: [`kaynaklar/KAYNAKLAR.md`](../../../kaynaklar/KAYNAKLAR.md).
Her dil ve her ihtiyaç için hangi kaynağın kullanılacağını oradan bul:

```bash
python3 araclar/kaynaklar.py --ara <dil kodu>     # ör. --ara chv, --ara kaz
python3 araclar/kaynaklar.py --ara odunc          # ihtiyaç: ana_turkce, bicim, agiz, tarihi, odunc, ...
```

Temel sıra:

1. **Ana Türkçe ve torun biçimler:** Wiktionary Ana Türkçe maddesi (`wiktionary-ana-turkce`,
   ham metin `?action=raw`, yönlendirmeleri izle), ardından StarLing (`starling`).
2. **Bağımsız ikinci kaynak:** Her kelimede en az bir kaynak Wiktionary dışından olsun.
   Temel kavramlarda Savelyev & Robbeets (`savelyev-turkic`) ve Dybo 2013 (`dybo-2013`),
   etimolojide ESTJa (`estja`), Clauson (`clauson`).
3. **Çuvaşça:** Ünal 2026 (`unal-2026`) ile miras/ödünç denetimi. Sibirya dillerinde
   Moğolca ödünç şüphesi için Khabtagaeva (`khabtagaeva`) ve ILCAA Moğolca listesi (`turkbv`).
4. **Tarihî tanıklar:** Türik Bitig ve Wilkens (Eski Türkçe), DLT (Karahanlıca), Grønbech
   (`gronbech-kuman`) ve Codex Cumanicus (Kuman), Tarama Sözlüğü (Eski Anadolu),
   Akvius/Boeschoten (Çağatay). Clauson archive.org'da tam metin (`clauson`).
5. **Ağızlar ve küçük diller:** Derleme Sözlüğü (Türkiye ağızları), dil sözlükleri,
   ELAR ve atlaslar (küçük Sibirya dilleri).

Erişim ipuçları: GitHub depolarını `raw.githubusercontent.com/<sahip>/<depo>/<dal>/<yol>`
üzerinden oku (HTML sayfaları bu ortamda 403). TDK Güncel Türkçe Sözlük JSON verir:
`https://sozluk.gov.tr/gts?ara=<kelime>`. Wikimedia 429 verirse istekler arasında bekle.
Her kaydın `dogrulama` alanı son denetimin sonucunu ve çalışan erişim yolunu yazar.

Kullanılan her kaynağı kökün `kaynak` alanına kimliğiyle yaz (ör. `wiktionary-ana-turkce;
savelyev-turkic`). Bir kaynak bu ortamdan erişilemiyorsa (`KAYNAKLAR.md`'de ✗), kullanıcıya
hangi adresin izin listesine eklenmesi gerektiğini söyle. Yeni ve işe yarar bir kaynak
bulursan `kaynaklar/kaynaklar.yaml`'a ekle ve dizini yenile.

**Alttan yukarı çalış.** Her dil için önce ağızlara bak (`agac.yaml`'da dilin
altındaki ağızlar), sonra yazı diline. Örneğin Türkiye Türkçesinde TDK *Derleme
Sözlüğü* ve ağız çalışmalarından Ege, Rumeli, Doğu Karadeniz… ağızlarının
kullandığı biçimleri al. Yazı dilinin biçimi dilin kendi koduna (`tur`), ağız
biçimleri ağız kodlarına (`tur-ege`) yazılır. Ağız verisi bulunamazsa sadece
yazı dili girilir; bu geçerlidir.

Kurallar:

- **Uydurma.** Emin olmadığın bir dili boş bırak. Boş bırakılan dil "veri yok"
  sayılır ve hesaptan çıkar. Yanlış veri ise sonucu bozar.
- Bir biçim **başka bir Türk dilinden ödünçse** (ör. Çuvaşçaya Tatarcadan
  geçmiş), biçimi `{ bicim: ..., odunc: tat }` olarak yaz. Bu, Hedef 2'de (kök
  yaşı) sahte kanıtı önler. Özellikle **Çuvaşça** biçimlerine dikkat et: miras
  kelime Oğur ses kurallarını taşır (Ortak Türkçe *z* → *r*, *ş* → *l*).
  Mirası kesinse `miras: true` yaz.
- Bir dilin o kavram için kullandığı kelime **alıntıysa**, o kelimeyi de ayrı bir
  kök olarak `koken: alıntı:<dil>` ile gir. Bu, "günlük kullanım" bilgisidir ve
  seçilmez.
- Aynı dilde birden çok kelime varsa hepsini gir ve `tercih` ver
  (1 asıl, 0.5 ikincil, 0.25 nadir/eskimiş/anlamı kaymış).
- Aynı kökten gelen biçimleri **tek kökte** topla (ses denklikleri: t/d, ş/s/l
  (Çuvaşça), -ğ/-w/-u/-v, z/r (Çuvaşça), y/c/ç/j/s/ʒ başlangıcı…). Bağlantı
  tartışmalıysa ayrı kök yap ve `not` yaz.
- Bilim insanlarının yeniden kurduğu Ana Türkçe biçim biliniyorsa (ör. StarLing,
  Wiktionary) kökün `ana_turkce` alanına yaz (ör. `ana_turkce: "*tāš"`).
- Kiril, Arap ve diğer yazılardaki biçimleri ILKELER.md §7'deki çalışma yazımına aktar.
- Tarihî tanıklarda kelime bulunamadıysa `tarihi_yok` listesine yaz. Hiç
  bakılmadıysa hiçbir yere yazma.
- Kaynakları kök düzeyinde `kaynak` alanına yaz. Tek bir biçim için özel bir
  kaynak varsa `{ bicim: ..., kaynak: ... }` biçiminde yaz.

## 3. Dosyayı yaz

Şablon: [`sablon.yaml`](sablon.yaml). `dogrulandi: false` olarak bırak.
`true` yapmak kullanıcının ya da onun gösterdiği bir kaynağın kararıdır.

## 4. Puanla ve kontrol et

```bash
python3 araclar/puanla.py <dosya_adı>
```

Hata veriyorsa düzelt (genellikle yanlış dil kodu).

## 5. Raporla (Türkçe, kısa)

1. **Sonuç:** alttan yukarı her birleşimde ne çıktığı (önemli ağızlar → dil →
   dal → kol → en tepe), anlaşılırlıkta en az anlayan kol, canlandırma uyarısı
   varsa o. Çıktı için `--derinlik 3` ya da `--agizlar` kullan.
2. **Tablo:** dil → biçim (alıntılar işaretli).
3. **Belirsizlikler:** boş bırakılan diller, şüpheli biçimler, tartışmalı kök
   bağlantıları.
4. **Üç hedef:** her adayın üç ölçüsü (köprü puanı ve en az anlayan büyük
   topluluk, kök yaşı, anlayan kişi sayısı) ve her hedefin seçimi. Ayrışıyorsa
   nedenini bir cümleyle açıkla. "Ödünç olabilir" uyarıları varsa belirt.
5. **Karar gerektirenler:** kullanıcıya sorulacak en fazla 2–3 nokta.

## 6. Kaydet

`KARSILASTIRMA.md` dosyasını yenile
(`python3 araclar/puanla.py --karsilastir --md > KARSILASTIRMA.md`).
Kullanıcının çalışma branch'ine commit et ve push et. Commit mesajı:
`sozluk: <kavram> eklendi` (güncellemede `güncellendi`).
