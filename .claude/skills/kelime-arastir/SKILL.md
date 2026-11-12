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

Web araştırması yap (WebSearch / web-fetch). Kaynak önceliği:

1. **Wiktionary'deki Ana Türkçe (Proto-Turkic) maddeleri**, ör.
   `Reconstruction:Proto-Turkic/tāš`. Torun dilleri listeler ve iyi bir başlangıçtır.
2. **StarLing Türk etimoloji veritabanı** (starling.rinet.ru): yaşayan dillerdeki
   biçimler ve Sevortyan/Räsänen göndermeleri.
3. Clauson (EDPT), Kâşgarlı Mahmud (DLT), TDK *Karşılaştırmalı Türk Lehçeleri
   Sözlüğü*.
4. Her dilin kendi sözlüğü (Wiktionary'deki dil maddeleri dahil).

**Alttan yukarı çalış.** Her dil için önce ağızlara bak (`agac.yaml`'da dilin
altındaki ağızlar), sonra yazı diline. Örneğin Türkiye Türkçesinde TDK *Derleme
Sözlüğü* ve ağız çalışmalarından Ege, Rumeli, Doğu Karadeniz… ağızlarının
kullandığı biçimleri al. Yazı dilinin biçimi dilin kendi koduna (`tur`), ağız
biçimleri ağız kodlarına (`tur-ege`) yazılır. Ağız verisi bulunamazsa sadece
yazı dili girilir; bu geçerlidir.

Kurallar:

- **Uydurma.** Emin olmadığın bir dili boş bırak. Boş bırakılan dil "veri yok"
  sayılır ve hesaptan çıkar. Yanlış veri ise sonucu bozar.
- Bir dilin o kavram için kullandığı kelime **alıntıysa**, o kelimeyi de ayrı bir
  kök olarak `koken: alıntı:<dil>` ile gir. Bu, "günlük kullanım" bilgisidir ve
  seçilmez.
- Aynı dilde birden çok kelime varsa hepsini gir ve `tercih` ver
  (1 asıl, 0.5 ikincil, 0.25 nadir/eskimiş/anlamı kaymış).
- Aynı kökten gelen biçimleri **tek kökte** topla (ses denklikleri: t/d, ş/s/l
  (Çuvaşça), -ğ/-w/-u/-v, z/r (Çuvaşça), y/c/ç/j/s/ʒ başlangıcı…). Bağlantı
  tartışmalıysa ayrı kök yap ve `not` yaz.
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
4. **Karar gerektirenler:** kullanıcıya sorulacak en fazla 2–3 nokta.

## 6. Kaydet

Kullanıcının çalışma branch'ine commit et ve push et. Commit mesajı:
`sozluk: <kavram> eklendi` (güncellemede `güncellendi`).
