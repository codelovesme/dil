# Kaynak sözlüğü

> Bu dosya `python3 araclar/kaynaklar.py > kaynaklar/KAYNAKLAR.md` komutuyla [`kaynaklar.yaml`](kaynaklar.yaml) dosyasından üretilir; elle düzenlemeyin.

Toplam **168 kaynak**. Her kayıtta: ne işe yaradığı, adresi, kapsadığı diller, nasıl kullanılacağı, erişim türü, güvenilirlik ve bu ortamdan erişilip erişilemediği.

- **Güven:** yüksek = hakemli ya da uzman eseri; orta = derlenmiş ya da topluluk ürünü; düşük = küçük liste ya da kaba tahmin.
- **Ortam:** ✓ bu oturumun ağ izni olan adres; ✗ izin listesine eklenmesi gerekir (bkz. [Erişim](#bu-ortamdan-erisim)).
- **Durum:** 82 kaynak bu ortamdan açılıp denetlendi, 72 kaynak aramada görüldü, 14 kaynak basılı. Son denetimin sonucu her kaydın **Doğrulama** satırında.
- **Hızlı arama:** `python3 araclar/kaynaklar.py --ara <dil kodu ya da ihtiyaç>` (ör. `--ara chv`, `--ara odunc`).

## İhtiyaca göre

### Ana Türkçe kuruluşu ve etimoloji

- [Brahmi, Tibet, Soğd ve Phags-pa harfli Eski Türkçe](#yabanci-yazili-eski-turkce) — kısmen, güven: yüksek, ortam: ✓
- [Clauson — An Etymological Dictionary of Pre-Thirteenth-Century Turkish (1972)](#clauson) — kısmen, güven: yüksek, ortam: ✓
- [Doerfer — Türkische und mongolische Elemente im Neupersischen (TMEN, 1963-75)](#doerfer-tmen) — kısmen, güven: yüksek, ortam: ✓
- [Dybo — Этимологический словарь базисной лексики тюркских языков (2013, ЭСТЯ ek cilt 9)](#dybo-2013) — açık, güven: yüksek, ortam: ✓
- [Eski Türkçedeki ödünç katmanları üzerine makaleler (Moğolca, Samoyedce, Kitanca)](#eski-turkce-odunc-katmanlari) — açık, güven: yüksek, ortam: ✓
- [Göttingen Bilimler Akademisi — Altuigurisches Wörterbuch projesi](#gottingen-altuygur) — açık, güven: yüksek, ortam: ✗
- [Halaçça — Doerfer, Khalaj Materials (1971) ve Doerfer & Tezcan, Wörterbuch des Chaladsch (1980)](#halacca) — basılı, güven: yüksek
- [Rahmatullayev — O'zbek tilining etimologik lug'ati](#ozbek-etimoloji) — basılı, güven: yüksek
- [Räsänen — Versuch eines etymologischen Wörterbuchs der Türksprachen (1969)](#rasanen) — kısmen, güven: yüksek, ortam: ✓
- [Róna-Tas & Berta — West Old Turkic (Macarcadaki Türkçe ödünçler) veri seti](#ronatas-bati-eski-turkce) — açık, güven: yüksek, ortam: ✓
- [Savelyev & Robbeets — Turkic Basic Vocabularies (lexibank/savelyevturkic)](#savelyev-turkic) — açık, güven: yüksek, ortam: ✓
- [Sovetskaya Tyurkologiya dergisi arşivi (Azerbaycan Cumhurbaşkanlığı Kütüphanesi, TurkLib)](#sovet-turkologiya) — açık, güven: yüksek, ortam: ✗
- [StarLing — Türk etimoloji veritabanı (Starostin, Dybo, Mudrak)](#starling) — açık, güven: yüksek, ortam: ✓
- [TDK Sözlükleri (Güncel Türkçe, Derleme, Tarama, Köken Bilgisi…)](#tdk-portal) — açık, güven: yüksek, ortam: ✓
- [Tatarintsev — Tuvacanın etimolojik sözlüğü (2000-)](#tatarintsev-tuvaca) — açık, güven: yüksek, ortam: ✓
- [Tataristan Bilimler Akademisi — Tatarca sözlükler (Süzlek)](#tatar-akademi-sozluk) — açık, güven: yüksek, ortam: ✗
- [Tietze — Tarihî ve Etimolojik Türkiye Türkçesi Lugatı (TÜBA)](#tietze) — basılı, güven: yüksek
- [Wilkens — Handwörterbuch des Altuigurischen (2021)](#wilkens-eski-uygurca) — açık, güven: yüksek, ortam: ✓
- [Çin kaynaklarındaki Eski Türkçe kelimeler (Ligeti 1950, Kasai, Vovin & McCraw)](#cin-transkripsiyonlari) — açık, güven: yüksek, ortam: ✓
- [Çuvaşça etimoloji sözlükleri (Yegorov 1964, Fedotov 1996, Zolotnitski 1875, Paasonen)](#cuvasca-etimoloji) — açık, güven: yüksek, ortam: ✓
- [Ünal — A Compendium of Common Turkic–Chuvash Lexical Correspondences with Proto-Turkic Reconstructions (2026)](#unal-2026) — açık, güven: yüksek, ortam: ✓
- [Сравнительно-историческая грамматика тюркских языков (Tenishev, 1984–2006)](#tenishev) — basılı, güven: yüksek
- [Этимологический словарь тюркских языков (ЭСТЯ, Sevortyan ve devamı)](#estja) — kısmen, güven: yüksek, ortam: ✓
- [Etymological Dictionary of the Altaic Languages (Starostin, Dybo, Mudrak 2003)](#edal) — basılı, güven: orta
- [Monumenta Altaica — Türkoloji e-kütüphanesi](#altaica-kutuphane) — açık, güven: orta, ortam: ✓
- [Nişanyan Sözlük — Çağdaş Türkçenin Etimolojisi](#nisanyan) — kısmen, güven: orta, ortam: ✓
- [Robbeets vd. 2021 — Triangulation (Transeurasian) veri seti](#robbeets-2021) — açık, güven: orta, ortam: ✗
- [Sino-Platonic Papers 325 — Proto-Turkic consonants](#proto-turkic-unsuzler) — açık, güven: orta, ortam: ✗
- [Toharca ile Türkçe temasları (CEToM, Carling & Pinault, Róna-Tas 1974)](#toharca) — kısmen, güven: orta, ortam: ✓
- [Türkmence etimoloji ve açıklamalı sözlükler (Atanyýazow; Türkmen diliniň düşündirişli sözlügi)](#turkmen-etimoloji) — basılı, güven: orta
- [Wiktionary — About Proto-Turkic (yazım ve kuruluş kuralları)](#wiktionary-hakkinda) — açık, güven: orta, ortam: ✓
- [Wiktionary — Ana Türkçe (Proto-Turkic) maddeleri](#wiktionary-ana-turkce) — açık, güven: orta, ortam: ✓
- [kaikki.org — Wiktionary'nin makinece okunabilir hâli (wiktextract)](#kaikki) — açık, güven: orta, ortam: ✓
- [Vámbéry — Etymologisches Wörterbuch der turko-tatarischen Sprachen (1878)](#vambery-1878) — açık, güven: düşük, ortam: ✓

### Yaşayan dillerde biçim toplama

- [Alişina 1994 — Tobol-İrtış ağzı (Sibirya Tatarcası) ve Tümen Üniversitesi e-kitaplığı](#sibirya-tatar-agiz) — açık, güven: yüksek, ortam: ✗
- [Azerbaycanca kaynaklar (Azərbaycan dilinin izahlı lüğəti, dilcilik.az)](#azerbaycan-kaynaklari) — kısmen, güven: yüksek, ortam: ✗
- [Aşmarin — Thesaurus Linguae Tschuvaschorum (17 cilt)](#cuvasca-asmarin) — basılı, güven: yüksek
- [Dybo — Этимологический словарь базисной лексики тюркских языков (2013, ЭСТЯ ek cilt 9)](#dybo-2013) — açık, güven: yüksek, ortam: ✓
- [ELAR — Endangered Languages Archive](#elar) — kısmen, güven: yüksek, ortam: ✗
- [Grønbech — Kuman Lehçesi Sözlüğü (Codex Cumanicus sözlüğü, Türkçe çeviri)](#gronbech-kuman) — açık, güven: yüksek, ortam: ✓
- [Halaçça — Doerfer, Khalaj Materials (1971) ve Doerfer & Tezcan, Wörterbuch des Chaladsch (1980)](#halacca) — basılı, güven: yüksek
- [ILCAA Turkic Basic Vocabulary (Tokyo Yabancı Diller Üniversitesi)](#turkbv) — açık, güven: yüksek, ortam: ✗
- [ILCAA çevrim içi kaynak portalı (Tokyo)](#ilcaa-kaynaklari) — açık, güven: yüksek, ortam: ✗
- [Karayca — Karaim Multi Dictionary (Csató & Nathan) ve KRPS 1974](#karay-sozluk) — kısmen, güven: yüksek, ortam: ✗
- [Kazak Dili Ulusal Derlemi](#qazcorpus) — kısmen, güven: yüksek, ortam: ✗
- [Kaşkayca — Dolatkhah 2019, Qashqai Turkic (derlem tabanlı dilbilgisi)](#kaskayca) — basılı, güven: yüksek
- [Lexical copies in Khalaj — World Loanword Database (WOLD) katkısı](#wold-halac) — açık, güven: yüksek, ortam: ✗
- [NorthEuraLex](#northeuralex) — açık, güven: yüksek, ortam: ✓
- [O'zbek tilining izohli lug'ati — Özbekçe açıklamalı sözlük (yeni baskı)](#ozbek-izohli) — kısmen, güven: yüksek, ortam: ✗
- [Qazaq ädebï tiliniñ sözdigi — Kazak yazı dilinin 15 ciltlik sözlüğü (2011)](#kazak-15-cilt) — kısmen, güven: yüksek, ortam: ✗
- [RBA Sibirya Şubesi Filoloji Enstitüsü (Novosibirsk) — dergiler ve e-kitaplık](#nsc-filoloji) — açık, güven: yüksek, ortam: ✗
- [Radloff — Versuch eines Wörterbuches der Türk-Dialecte (1893-1911, 4 cilt)](#radloff) — açık, güven: yüksek, ortam: ✓
- [Rusça açıklamalı standart sözlükler (Yudahin, Gagavuzca 1973, Karaçay-Malkarca 1989, Hakasça, Sahaca 1972)](#sovyet-iki-dilli-sozlukler) — açık, güven: yüksek, ortam: ✓
- [Salarca — Dwyer'in çalışmaları ve DoBeS Salar projesi](#salarca) — kısmen, güven: yüksek, ortam: ✗
- [Savelyev & Robbeets — Turkic Basic Vocabularies (lexibank/savelyevturkic)](#savelyev-turkic) — açık, güven: yüksek, ortam: ✓
- [Sibirya ve Altay'ın eski ve küçük dil sözlükleri (Verbitski 1884, Pekarski, Tumaşeva, Rassadin, Lemskaya)](#sibirya-eski-sozlukler) — açık, güven: yüksek, ortam: ✓
- [StarLing — Türk etimoloji veritabanı (Starostin, Dybo, Mudrak)](#starling) — açık, güven: yüksek, ortam: ✓
- [TDK Sözlükleri (Güncel Türkçe, Derleme, Tarama, Köken Bilgisi…)](#tdk-portal) — açık, güven: yüksek, ortam: ✓
- [Tatar Ulusal Derlemi "Tugan Tel" ve Yazılı Tatarca Derlemi](#tugan-tel) — açık, güven: yüksek, ortam: ✗
- [Tataristan Bilimler Akademisi — Tatarca sözlükler (Süzlek)](#tatar-akademi-sozluk) — açık, güven: yüksek, ortam: ✗
- [el-sozduk.kg — Kırgızca sözlükler (Yudahin dahil)](#el-sozduk) — açık, güven: yüksek, ortam: ✗
- [Çin'deki küçük Türk dillerinin sözlükleri (Batı Yugurca, Salarca)](#cin-turk-dilleri) — basılı, güven: yüksek
- [Özbekçe kaynaklar (CTILD Indiana, Chicago CEERES)](#ozbek-kaynaklari) — açık, güven: yüksek, ortam: ✗
- [Этимологический словарь тюркских языков (ЭСТЯ, Sevortyan ve devamı)](#estja) — kısmen, güven: yüksek, ortam: ✓
- [Apertium — Türk dilleri çeviri çiftleri ve sözlükleri](#apertium) — açık, güven: orta, ortam: ✓
- [Budagov — Türk-Tatar lehçelerinin karşılaştırmalı sözlüğü (1869-71, 2 cilt)](#budagov) — açık, güven: orta, ortam: ✓
- [DergiPark](#dergipark) — açık, güven: orta, ortam: ✓
- [Elegant Lexicon — Turkic database (C. A. Straughn)](#elegant-lexicon) — açık, güven: orta, ortam: ✓
- [Kuzey, Sibirya ve Uzak Doğu yerli halkları etkileşimli atlası](#atlaskmns) — açık, güven: orta, ortam: ✗
- [Kırım Tatarcası Ulusal Derlemi ve sözlükleri](#kirim-tatar-derlem) — açık, güven: orta, ortam: ✗
- [Lexilogos — dil bazlı sözlük portalı](#lexilogos) — açık, güven: orta, ortam: ✗
- [Qamus — Türk Devletleri Parlamenter Asamblesi (TÜRKPA) karşılaştırmalı sözlüğü](#qamus) — kısmen, güven: orta, ortam: ✗
- [Sibirya Dilleri — Rusya Bilimler Akademisi Etnoloji Enstitüsü](#lingsib) — açık, güven: orta, ortam: ✗
- [Tatarca Ulusal Derlemi (corpus.tatar)](#tatar-derlem) — açık, güven: orta, ortam: ✗
- [Turkic Interlingua (TIL) — 22 Türk dili paralel derlemi](#til-mt) — açık, güven: orta, ortam: ✓
- [Tuvan Talking Dictionary (Swarthmore) ve Living Dictionaries](#tuva-sozluk) — açık, güven: orta, ortam: ✗
- [Türkmence etimoloji ve açıklamalı sözlükler (Atanyýazow; Türkmen diliniň düşündirişli sözlügi)](#turkmen-etimoloji) — basılı, güven: orta
- [Türkmence sözlükler (Webonary, Makul Sözlük, Ene dilim)](#turkmen-sozluk) — açık, güven: orta, ortam: ✗
- [Uluslararası Türk Akademisi — Türk dilleri terim sözlükleri](#turk-akademisi-terim) — kısmen, güven: orta, ortam: ✗
- [Wiktionary — Ana Türkçe (Proto-Turkic) maddeleri](#wiktionary-ana-turkce) — açık, güven: orta, ortam: ✓
- [Wiktionary — Türk dilleri Swadesh listeleri](#wiktionary-swadesh) — açık, güven: orta, ortam: ✓
- [YÖK Açık Bilim ve Tez Merkezi — Türkiye'deki lisansüstü tezler](#yok-acik-bilim) — kısmen, güven: orta, ortam: ✗
- [kaikki.org — Wiktionary'nin makinece okunabilir hâli (wiktextract)](#kaikki) — açık, güven: orta, ortam: ✓
- [neurotatarlar/tt-dictionaries — Tatarca sözlükler veri seti](#tatar-sozluk-veri) — açık, güven: orta, ortam: ✗
- [sakhatyla.ru — Sahaca-Rusça / Sahaca-İngilizce sözlük](#sakhatyla) — açık, güven: orta, ortam: ✗
- [sozdik.kz — Kazakça-Rusça / Rusça-Kazakça sözlük](#sozdik) — açık, güven: orta, ortam: ✗
- [til.im — Kumukça kitaplar ve sözlükler](#kumuk-kaynaklari) — açık, güven: orta, ortam: ✗
- [translate.chv.su — Çuvaşça-Rusça derlem, çeviri ve sözlük (Plotnikov)](#cuvasca-ceviri) — açık, güven: orta, ortam: ✗
- [Freelang kelime listeleri](#freelang) — açık, güven: düşük, ortam: ✗
- [Gagavuzca sözlükler](#gagavuzca) — kısmen, güven: düşük, ortam: ✗
- [PanLex](#panlex) — açık, güven: düşük, ortam: ✗
- [lehceler.com — Türk lehçeleri karşılaştırmalı sözlüğü](#lehceler-com) — açık, güven: düşük, ortam: ✗

### Ağız verisi

- [Alişina 1994 — Tobol-İrtış ağzı (Sibirya Tatarcası) ve Tümen Üniversitesi e-kitaplığı](#sibirya-tatar-agiz) — açık, güven: yüksek, ortam: ✗
- [Azerbaycanca kaynaklar (Azərbaycan dilinin izahlı lüğəti, dilcilik.az)](#azerbaycan-kaynaklari) — kısmen, güven: yüksek, ortam: ✗
- [Azərbaycan dilinin dialektoloji lüğəti (1999, 2003)](#azerbaycan-diyalekt) — açık, güven: yüksek, ortam: ✓
- [Aşmarin — Thesaurus Linguae Tschuvaschorum (17 cilt)](#cuvasca-asmarin) — basılı, güven: yüksek
- [Castrén 1857 (Koybal ve Karagas) ve Böhtlingk 1851 (Sahaca) — ilk bilimsel tanımlar](#castren-bohtlingk) — açık, güven: yüksek, ortam: ✓
- [ELAR — Endangered Languages Archive](#elar) — kısmen, güven: yüksek, ortam: ✗
- [Halaçça — Doerfer, Khalaj Materials (1971) ve Doerfer & Tezcan, Wörterbuch des Chaladsch (1980)](#halacca) — basılı, güven: yüksek
- [Karayca eski kayıtlar (Kowalski 1929 Trakay metinleri; KRPS 1974)](#karayca-eski-kayitlar) — açık, güven: yüksek, ortam: ✓
- [Karayca — Karaim Multi Dictionary (Csató & Nathan) ve KRPS 1974](#karay-sozluk) — kısmen, güven: yüksek, ortam: ✗
- [Kâşgarlı Mahmud — Dîvânu Lugâti't-Türk (Ercilasun & Akkoyunlu 2014, TDK)](#dlt) — açık, güven: yüksek, ortam: ✓
- [RBA Sibirya Şubesi Filoloji Enstitüsü (Novosibirsk) — dergiler ve e-kitaplık](#nsc-filoloji) — açık, güven: yüksek, ortam: ✗
- [Radloff — Versuch eines Wörterbuches der Türk-Dialecte (1893-1911, 4 cilt)](#radloff) — açık, güven: yüksek, ortam: ✓
- [Rusya Federasyonu Türk Ağızları Atlası (Dybo)](#rf-turk-agiz-atlasi) — kısmen, güven: yüksek, ortam: ✗
- [Sibirya ve Altay'ın eski ve küçük dil sözlükleri (Verbitski 1884, Pekarski, Tumaşeva, Rassadin, Lemskaya)](#sibirya-eski-sozlukler) — açık, güven: yüksek, ortam: ✓
- [Sovetskaya Tyurkologiya dergisi arşivi (Azerbaycan Cumhurbaşkanlığı Kütüphanesi, TurkLib)](#sovet-turkologiya) — açık, güven: yüksek, ortam: ✗
- [TDK Sözlükleri (Güncel Türkçe, Derleme, Tarama, Köken Bilgisi…)](#tdk-portal) — açık, güven: yüksek, ortam: ✓
- [Tataristan Bilimler Akademisi — Tatarca sözlükler (Süzlek)](#tatar-akademi-sozluk) — açık, güven: yüksek, ortam: ✗
- [Tietze — Tarihî ve Etimolojik Türkiye Türkçesi Lugatı (TÜBA)](#tietze) — basılı, güven: yüksek
- [Uluslararası Türk Lehçe Araştırmaları Dergisi (TÜRKLAD)](#turklad) — açık, güven: yüksek, ortam: ✓
- [WOWA — Word Order in Western Asia derlemi (Bamberg)](#wowa) — açık, güven: yüksek, ortam: ✗
- [Özbekçe kaynaklar (CTILD Indiana, Chicago CEERES)](#ozbek-kaynaklari) — açık, güven: yüksek, ortam: ✗
- [İbn Mühennâ Lügati (13.-14. yy; Battal 1934, TDK)](#ibn-muhenna) — açık, güven: yüksek, ortam: ✓
- [ASK REAL — Kore Altayistik Derneği saha araştırmaları (2003-2009)](#kore-ask-real) — kısmen, güven: orta, ortam: ✗
- [DergiPark](#dergipark) — açık, güven: orta, ortam: ✓
- [Klaproth — Asia Polyglotta (1823) ve Uygur dili ve yazısı üzerine (1812/1820)](#klaproth) — açık, güven: orta, ortam: ✓
- [Novye issledovaniya Tuvy (Tuva üzerine yeni araştırmalar) dergisi](#tuva-dergi) — açık, güven: orta, ortam: ✗
- [Pallas — Linguarum totius orbis vocabularia comparativa (1786-89)](#pallas-1787) — açık, güven: orta, ortam: ✓
- [Strahlenberg 1730 ve Witsen 1692 — Sibirya kelime listeleri (Almanca, Felemenkçe)](#strahlenberg-witsen) — açık, güven: orta, ortam: ✓
- [Türkmence etimoloji ve açıklamalı sözlükler (Atanyýazow; Türkmen diliniň düşündirişli sözlügi)](#turkmen-etimoloji) — basılı, güven: orta
- [YÖK Açık Bilim ve Tez Merkezi — Türkiye'deki lisansüstü tezler](#yok-acik-bilim) — kısmen, güven: orta, ortam: ✗

### Tarihî tanık biçimleri

- [19. yy Osmanlıca sözlükleri (Kieffer & Bianchi 1835, Zenker 1866-76, Redhouse 1890)](#osmanlica-batili-sozlukler) — açık, güven: yüksek, ortam: ✓
- [BBAW Turfan Araştırmaları — Eski Uygurca metinler ve sayısal arşiv](#turfan-bbaw) — açık, güven: yüksek, ortam: ✗
- [Bizans kaynaklarında Türkçe (Moravcsik, Byzantinoturcica II; Macartney 1944)](#bizans-kaynaklari) — kısmen, güven: yüksek, ortam: ✓
- [Boeschoten — A Dictionary of Early Middle Turkic (Brill 2022)](#boeschoten) — ücretli, güven: yüksek, ortam: ✗
- [Brahmi, Tibet, Soğd ve Phags-pa harfli Eski Türkçe](#yabanci-yazili-eski-turkce) — kısmen, güven: yüksek, ortam: ✓
- [Bulġatü'l-Müştâk ve ed-Dürretü'l-Mudiyye (Zajączkowski 1958-1969, Fransızca)](#bulgat-durre) — açık, güven: yüksek, ortam: ✓
- [Castrén 1857 (Koybal ve Karagas) ve Böhtlingk 1851 (Sahaca) — ilk bilimsel tanımlar](#castren-bohtlingk) — açık, güven: yüksek, ortam: ✓
- [Clauson — An Etymological Dictionary of Pre-Thirteenth-Century Turkish (1972)](#clauson) — kısmen, güven: yüksek, ortam: ✓
- [Codex Cumanicus (çevrim içi baskılar)](#codex-cumanicus) — açık, güven: yüksek, ortam: ✗
- [Doerfer — Türkische und mongolische Elemente im Neupersischen (TMEN, 1963-75)](#doerfer-tmen) — kısmen, güven: yüksek, ortam: ✓
- [Ebû Hayyân — Kitâbü'l-İdrâk li-Lisâni'l-Etrâk (1312-13)](#kitab-idrak) — açık, güven: yüksek, ortam: ✓
- [Erdal 1993 — Die Sprache der wolgabolgarischen Inschriften](#erdal-volga-bulgar) — basılı, güven: yüksek
- [Ermeni harfli Kıpçakça (Garkavets 2010; Tryjarski 1968-72)](#ermeni-kipcak) — açık, güven: yüksek, ortam: ✓
- [Gaochang Guan Yiyu / Zazi — Ming dönemi Uygurca-Çince sözlük (15.-16. yy)](#gaochang-yiyu) — açık, güven: yüksek, ortam: ✓
- [Grønbech — Kuman Lehçesi Sözlüğü (Codex Cumanicus sözlüğü, Türkçe çeviri)](#gronbech-kuman) — açık, güven: yüksek, ortam: ✓
- [Göttingen Bilimler Akademisi — Altuigurisches Wörterbuch projesi](#gottingen-altuygur) — açık, güven: yüksek, ortam: ✗
- [Hazarca kalıntıları (Golden 1980 Khazar Studies; İbranice yazışma)](#hazarca) — basılı, güven: yüksek
- [Hotanca kaynaklarda Türkçe (Bailey 1939-55, Emmerick & Róna-Tas 1992, Hovdhaugen 1971)](#hotanca-turkce) — açık, güven: yüksek, ortam: ✓
- [Houtsma 1894 — Ein türkisch-arabisches Glossar (Leiden yazması, 1245)](#houtsma-leiden) — açık, güven: yüksek, ortam: ✓
- [KOHD — Almanya'daki Eski Uygurca el yazmaları kataloğu](#kohd-eski-uygurca) — açık, güven: yüksek, ortam: ✗
- [Karayca eski kayıtlar (Kowalski 1929 Trakay metinleri; KRPS 1974)](#karayca-eski-kayitlar) — açık, güven: yüksek, ortam: ✓
- [Kâşgarlı Mahmud — Dîvânu Lugâti't-Türk (Ercilasun & Akkoyunlu 2014, TDK)](#dlt) — açık, güven: yüksek, ortam: ✓
- [Meninski 1680 ve Latin harfli Osmanlıca (Megiser 1612, Molino 1641)](#meninski-transkripsiyon) — açık, güven: yüksek, ortam: ✓
- [Mirza Mehdi Han — Senglâh (1759-60; Clauson 1960 tıpkıbasım)](#senglah) — basılı, güven: yüksek
- [Moğolistan'daki Türk yazıtları (Battulga 2005; Moriyasu & Ochir 1999, Japonca-Moğolca)](#mogolistan-yazitlari) — açık, güven: yüksek, ortam: ✓
- [Moğolların Gizli Tarihi (13. yy) dizinleri (Kuribayashi 2009, Haenisch 1939)](#gizli-tarih) — açık, güven: yüksek, ortam: ✓
- [Nadjip 1979 — XIV. yüzyıl Türk dillerinin tarihî-karşılaştırmalı sözlüğü (Rusça)](#najip-xiv) — açık, güven: yüksek, ortam: ✓
- [Pelliot — Notes on Marco Polo (1959-73)](#pelliot-marco-polo) — kısmen, güven: yüksek, ortam: ✓
- [Radloff — Versuch eines Wörterbuches der Türk-Dialecte (1893-1911, 4 cilt)](#radloff) — açık, güven: yüksek, ortam: ✓
- [Rasûlî Altı Dilli Sözlük — The King's Dictionary (Golden 2000)](#rasulid-hexaglot) — kısmen, güven: yüksek, ortam: ✓
- [Róna-Tas & Berta — West Old Turkic (Macarcadaki Türkçe ödünçler) veri seti](#ronatas-bati-eski-turkce) — açık, güven: yüksek, ortam: ✓
- [Sibirya ve Altay'ın eski ve küçük dil sözlükleri (Verbitski 1884, Pekarski, Tumaşeva, Rassadin, Lemskaya)](#sibirya-eski-sozlukler) — açık, güven: yüksek, ortam: ✓
- [TDK Sözlükleri (Güncel Türkçe, Derleme, Tarama, Köken Bilgisi…)](#tdk-portal) — açık, güven: yüksek, ortam: ✓
- [Tietze — Tarihî ve Etimolojik Türkiye Türkçesi Lugatı (TÜBA)](#tietze) — basılı, güven: yüksek
- [Toparlı, Vural, Karaatlı — Kıpçak Türkçesi Sözlüğü (TDK 2007)](#toparli-kipcak) — kısmen, güven: yüksek, ortam: ✓
- [Turfan metinlerinin ilk yayınları (Müller, Uigurica 1908-31; Bang & Gabain, TTT ve dizini)](#turfan-ilk-yayinlar) — açık, güven: yüksek, ortam: ✓
- [Tâli' İmânî Herevî — Bedâyi'ü'l-Lugat (Borovkov 1961, tıpkıbasım ve Rusça)](#bedayi-lugat) — açık, güven: yüksek, ortam: ✓
- [VATEC — İslam öncesi Eski Türkçe metinlerin elektronik derlemi (Frankfurt)](#vatec) — açık, güven: yüksek, ortam: ✗
- [Wilkens — Handwörterbuch des Altuigurischen (2021)](#wilkens-eski-uygurca) — açık, güven: yüksek, ortam: ✓
- [Wuti Qingwen Jian — Beş Dilli Ayna (18. yy; Mançu-Tibet-Moğol-Çağatay-Çince)](#bes-dilli-ayna) — basılı, güven: yüksek
- [Zemahşerî — Mukaddimetü'l-Edeb (1137; Harezm Türkçesi ve Moğolca aralık çevirileri)](#mukaddimet-edeb) — açık, güven: yüksek, ortam: ✓
- [et-Tuhfetü'z-Zekiyye fi'l-Lügati't-Türkiyye (14. yy; Atalay 1945, TDK)](#tuhfe-zekiyye) — açık, güven: yüksek, ortam: ✓
- [Çin kaynaklarındaki Eski Türkçe kelimeler (Ligeti 1950, Kasai, Vovin & McCraw)](#cin-transkripsiyonlari) — açık, güven: yüksek, ortam: ✓
- [Çuvaşça etimoloji sözlükleri (Yegorov 1964, Fedotov 1996, Zolotnitski 1875, Paasonen)](#cuvasca-etimoloji) — açık, güven: yüksek, ortam: ✓
- [İbn Mühennâ Lügati (13.-14. yy; Battal 1934, TDK)](#ibn-muhenna) — açık, güven: yüksek, ortam: ✓
- [Древнетюркский словарь (1969)](#dts) — kısmen, güven: yüksek, ortam: ✓
- [Abuşka — Çağatayca-Osmanlıca sözlük (16. yy; Vámbéry 1862, Atalay 1970)](#abuska) — açık, güven: orta, ortam: ✓
- [Akvius — çevrim içi Çağatayca sözlük](#akvius-cagatayca) — açık, güven: orta, ortam: ✗
- [Arapça ve Farsça coğrafya eserleri (Hudûdü'l-Âlem 982; Minorsky 1937)](#arap-fars-cografyacilar) — açık, güven: orta, ortam: ✓
- [Avrupa'da basılan Çağatayca sözlükler (Vámbéry 1867, Pavet de Courteille 1870, Kúnos 1902)](#cagatay-batili-sozlukler) — açık, güven: orta, ortam: ✓
- [Bahşayiş Lügati — Eski Oğuzca Sözlük (Turan)](#bahsayis) — açık, güven: orta, ortam: ✓
- [Budagov — Türk-Tatar lehçelerinin karşılaştırmalı sözlüğü (1869-71, 2 cilt)](#budagov) — açık, güven: orta, ortam: ✓
- [Chaghatay tilining izahliq lughiti (Uygurca açıklamalı Çağatayca sözlük)](#cagatay-izahli) — açık, güven: orta, ortam: ✓
- [Eski İran dilleriyle temas (Harmatta 1972 Irano-Turcica; Sims-Williams, Baktrça adlar)](#iran-turk-temasi) — kısmen, güven: orta, ortam: ✓
- [Karamanlıca — Rum harfli Türkçe (Salaville & Dalleggio, Anatoli gazetesi)](#karamanlica) — açık, güven: orta, ortam: ✗
- [Klaproth — Asia Polyglotta (1823) ve Uygur dili ve yazısı üzerine (1812/1820)](#klaproth) — açık, güven: orta, ortam: ✓
- [Komşu dillerdeki Türkçe ödünçler (Miklosich 1884, Şipova 1976, Škaljić 1966)](#komsu-dillerde-turkce) — açık, güven: orta, ortam: ✓
- [Pallas — Linguarum totius orbis vocabularia comparativa (1786-89)](#pallas-1787) — açık, güven: orta, ortam: ✓
- [Strahlenberg 1730 ve Witsen 1692 — Sibirya kelime listeleri (Almanca, Felemenkçe)](#strahlenberg-witsen) — açık, güven: orta, ortam: ✓
- [Tibetçe kaynaklarda Türkler (OTDO, Pelliot tibétain 1283)](#tibet-kaynaklari) — açık, güven: orta, ortam: ✗
- [Türik Bitig — Eski Türkçe yazıtlar ve metinler portalı](#turik-bitig) — açık, güven: orta, ortam: ✓
- [Türk ülkelerinde yayımlanmış Eski Türkçe sözlükler (Azerbaycan 1992, Uygur 1989)](#eski-turkce-yerel-sozlukler) — açık, güven: orta, ortam: ✓
- [Wiktionary — Ana Türkçe (Proto-Turkic) maddeleri](#wiktionary-ana-turkce) — açık, güven: orta, ortam: ✓
- [Yedisu'daki Süryani harfli Nesturi mezar taşları (Chwolson 1890)](#suryani-yazitlar) — açık, güven: orta, ortam: ✓
- [YÖK Açık Bilim ve Tez Merkezi — Türkiye'deki lisansüstü tezler](#yok-acik-bilim) — kısmen, güven: orta, ortam: ✗

### Ödünç ve miras ayrımı (özellikle Çuvaşça)

- [19. yy Osmanlıca sözlükleri (Kieffer & Bianchi 1835, Zenker 1866-76, Redhouse 1890)](#osmanlica-batili-sozlukler) — açık, güven: yüksek, ortam: ✓
- [Abaev — Osetçenin tarihî-etimolojik sözlüğü (1958-95, 4 cilt)](#abaev-osetce) — basılı, güven: yüksek
- [Arapça ve Farsça kaynak sözlükler (Lane, Steingass) — ödünç sınaması](#arapca-farsca-sozlukler) — açık, güven: yüksek, ortam: ✓
- [Aşmarin — Thesaurus Linguae Tschuvaschorum (17 cilt)](#cuvasca-asmarin) — basılı, güven: yüksek
- [Doerfer — Türkische und mongolische Elemente im Neupersischen (TMEN, 1963-75)](#doerfer-tmen) — kısmen, güven: yüksek, ortam: ✓
- [Erdal 1993 — Die Sprache der wolgabolgarischen Inschriften](#erdal-volga-bulgar) — basılı, güven: yüksek
- [Eski Türkçedeki ödünç katmanları üzerine makaleler (Moğolca, Samoyedce, Kitanca)](#eski-turkce-odunc-katmanlari) — açık, güven: yüksek, ortam: ✓
- [Houtsma 1894 — Ein türkisch-arabisches Glossar (Leiden yazması, 1245)](#houtsma-leiden) — açık, güven: yüksek, ortam: ✓
- [Khabtagaeva — Sibirya Türk dillerinde Moğolca ödünçler](#khabtagaeva) — basılı, güven: yüksek
- [Lexical copies in Khalaj — World Loanword Database (WOLD) katkısı](#wold-halac) — açık, güven: yüksek, ortam: ✗
- [Moğol dilleri karşılaştırmalı ve etimolojik sözlükleri (Sun Zhu 1990; Sanjeev vd. 2015-18; Sühbaatar)](#mogolca-etimoloji) — açık, güven: yüksek, ortam: ✓
- [Moğolca sözlükler (Kowalewski 1844-49, Lessing 1960, Bawden, Büyük Akademik Moğolca-Rusça)](#mogolca-sozlukler) — açık, güven: yüksek, ortam: ✓
- [Moğolların Gizli Tarihi (13. yy) dizinleri (Kuribayashi 2009, Haenisch 1939)](#gizli-tarih) — açık, güven: yüksek, ortam: ✓
- [Pelliot — Notes on Marco Polo (1959-73)](#pelliot-marco-polo) — kısmen, güven: yüksek, ortam: ✓
- [Rahmatullayev — O'zbek tilining etimologik lug'ati](#ozbek-etimoloji) — basılı, güven: yüksek
- [Rasûlî Altı Dilli Sözlük — The King's Dictionary (Golden 2000)](#rasulid-hexaglot) — kısmen, güven: yüksek, ortam: ✓
- [Róna-Tas & Berta — West Old Turkic (Macarcadaki Türkçe ödünçler) veri seti](#ronatas-bati-eski-turkce) — açık, güven: yüksek, ortam: ✓
- [Savelyev & Robbeets — Turkic Basic Vocabularies (lexibank/savelyevturkic)](#savelyev-turkic) — açık, güven: yüksek, ortam: ✓
- [Soğdca ödünçler (Gharib 1995 sözlüğü, Ayazlı 2020, Wilkens 2021)](#sogdca) — kısmen, güven: yüksek, ortam: ✓
- [Studia Etymologica Cracoviensia (Krakov, 1996-2015) ve Stachowski'nin çalışmaları](#studia-etymologica-cracoviensia) — açık, güven: yüksek, ortam: ✗
- [Tatarintsev — Tuvacanın etimolojik sözlüğü (2000-)](#tatarintsev-tuvaca) — açık, güven: yüksek, ortam: ✓
- [Tunguz-Mançu dilleri karşılaştırmalı sözlüğü (Tsintsius 1975-77) ve Evenkçe sözlük](#tunguzca) — açık, güven: yüksek, ortam: ✓
- [Wuti Qingwen Jian — Beş Dilli Ayna (18. yy; Mançu-Tibet-Moğol-Çağatay-Çince)](#bes-dilli-ayna) — basılı, güven: yüksek
- [Zemahşerî — Mukaddimetü'l-Edeb (1137; Harezm Türkçesi ve Moğolca aralık çevirileri)](#mukaddimet-edeb) — açık, güven: yüksek, ortam: ✓
- [Çin'deki küçük Türk dillerinin sözlükleri (Batı Yugurca, Salarca)](#cin-turk-dilleri) — basılı, güven: yüksek
- [Çuvaşça etimoloji sözlükleri (Yegorov 1964, Fedotov 1996, Zolotnitski 1875, Paasonen)](#cuvasca-etimoloji) — açık, güven: yüksek, ortam: ✓
- [Ünal — A Compendium of Common Turkic–Chuvash Lexical Correspondences with Proto-Turkic Reconstructions (2026)](#unal-2026) — açık, güven: yüksek, ortam: ✓
- [Doğu Yugurca (Moğol dili) - Moğolca - Çince sözlük](#dogu-yugur-sozluk) — açık, güven: orta, ortam: ✓
- [Eski İran dilleriyle temas (Harmatta 1972 Irano-Turcica; Sims-Williams, Baktrça adlar)](#iran-turk-temasi) — kısmen, güven: orta, ortam: ✓
- [Komşu dillerdeki Türkçe ödünçler (Miklosich 1884, Şipova 1976, Škaljić 1966)](#komsu-dillerde-turkce) — açık, güven: orta, ortam: ✓
- [Nişanyan Sözlük — Çağdaş Türkçenin Etimolojisi](#nisanyan) — kısmen, güven: orta, ortam: ✓
- [Toharca ile Türkçe temasları (CEToM, Carling & Pinault, Róna-Tas 1974)](#toharca) — kısmen, güven: orta, ortam: ✓

### Örgü: benzerlik ve anlaşılırlık değerleri

- [Baidildinova vd. 2026 — Quantifying mutual intelligibility gradients in Turkic languages (SCiL)](#scil-2026) — açık, güven: yüksek, ortam: ✓
- [ILCAA Turkic Basic Vocabulary (Tokyo Yabancı Diller Üniversitesi)](#turkbv) — açık, güven: yüksek, ortam: ✗
- [Iran Atlas — İran'ın Dil Atlası (Anonby vd.)](#iran-dil-atlasi) — açık, güven: yüksek, ortam: ✗
- [NorthEuraLex](#northeuralex) — açık, güven: yüksek, ortam: ✓
- [Rusya Federasyonu Türk Ağızları Atlası (Dybo)](#rf-turk-agiz-atlasi) — kısmen, güven: yüksek, ortam: ✗
- [Salehi & Neysani 2017 — Azerbaycan Türkçesinin Türkiye Türkçesi konuşurlarınca anlaşılırlığı](#salehi-2017) — kısmen, güven: yüksek, ortam: ✗
- [Savelyev & Robbeets — Turkic Basic Vocabularies (lexibank/savelyevturkic)](#savelyev-turkic) — açık, güven: yüksek, ortam: ✓
- [ASJP Database (Automated Similarity Judgment Program)](#asjp) — açık, güven: orta, ortam: ✓
- [En sık 1000 kelime açısından modern Türk dilleri (Türkiye, Azerbaycan, Kazak, Kırgız, Özbek)](#en-sik-1000) — açık, güven: orta, ortam: ✗

### Sınıflandırma (soy ağacı)

- [Glottolog](#glottolog) — açık, güven: yüksek, ortam: ✓
- [Iran Atlas — İran'ın Dil Atlası (Anonby vd.)](#iran-dil-atlasi) — açık, güven: yüksek, ortam: ✗
- [Johanson & Csató (ed.) — The Turkic Languages (2. baskı, 2021)](#johanson-csato) — ücretli, güven: yüksek, ortam: ✗
- [Sibirya Dilleri — Rusya Bilimler Akademisi Etnoloji Enstitüsü](#lingsib) — açık, güven: orta, ortam: ✗
- [Wikipedia — List of Turkic languages](#wikipedia-turk-dilleri) — açık, güven: düşük, ortam: ✗

### Konuşur sayısı ve canlılık

- [Iran Atlas — İran'ın Dil Atlası (Anonby vd.)](#iran-dil-atlasi) — açık, güven: yüksek, ortam: ✗
- [Endangered Languages Project](#elp) — açık, güven: orta, ortam: ✗
- [Ethnologue](#ethnologue) — ücretli, güven: orta, ortam: ✗
- [Kuzey, Sibirya ve Uzak Doğu yerli halkları etkileşimli atlası](#atlaskmns) — açık, güven: orta, ortam: ✗
- [Novye issledovaniya Tuvy (Tuva üzerine yeni araştırmalar) dergisi](#tuva-dergi) — açık, güven: orta, ortam: ✗
- [Rosstat — 2021 Rusya nüfus sayımı dil tabloları](#rosstat-2021) — açık, güven: orta, ortam: ✗
- [Sibirya Dilleri — Rusya Bilimler Akademisi Etnoloji Enstitüsü](#lingsib) — açık, güven: orta, ortam: ✗
- [UNESCO World Atlas of Languages](#unesco-wal) — açık, güven: orta, ortam: ✗
- [Joshua Project](#joshua-project) — açık, güven: düşük, ortam: ✗
- [Wikipedia — List of Turkic languages](#wikipedia-turk-dilleri) — açık, güven: düşük, ortam: ✗

### Sıklık listeleri ve kavram listeleri

- [Concepticon — kavram listeleri veritabanı](#concepticon) — açık, güven: yüksek, ortam: ✓
- [Dybo — Этимологический словарь базисной лексики тюркских языков (2013, ЭСТЯ ek cilt 9)](#dybo-2013) — açık, güven: yüksek, ortam: ✓
- [Kazak Dili Ulusal Derlemi](#qazcorpus) — kısmen, güven: yüksek, ortam: ✗
- [Tatar Ulusal Derlemi "Tugan Tel" ve Yazılı Tatarca Derlemi](#tugan-tel) — açık, güven: yüksek, ortam: ✗
- [Türkçe Ulusal Derlemi (TNC) ve Türkçe Sıklık Sözlüğü](#tnc) — kısmen, güven: yüksek, ortam: ✗
- [En sık 1000 kelime açısından modern Türk dilleri (Türkiye, Azerbaycan, Kazak, Kırgız, Özbek)](#en-sik-1000) — açık, güven: orta, ortam: ✗
- [Kırım Tatarcası Ulusal Derlemi ve sözlükleri](#kirim-tatar-derlem) — açık, güven: orta, ortam: ✗
- [Leipzig Corpora Collection — kelime sıklık listeleri](#leipzig-corpora) — açık, güven: orta, ortam: ✗
- [OpenSubtitles tabanlı sıklık listeleri (hermitdave/FrequencyWords, orgtre/top-open-subtitles-sentences)](#opensubtitles-siklik) — açık, güven: orta, ortam: ✓
- [Pallas — Linguarum totius orbis vocabularia comparativa (1786-89)](#pallas-1787) — açık, güven: orta, ortam: ✓
- [Sketch Engine — Turkic web corpora](#sketch-engine-turk) — ücretli, güven: orta, ortam: ✗
- [Tatarca Ulusal Derlemi (corpus.tatar)](#tatar-derlem) — açık, güven: orta, ortam: ✗
- [Turkic Interlingua (TIL) — 22 Türk dili paralel derlemi](#til-mt) — açık, güven: orta, ortam: ✓
- [Wiktionary — Türk dilleri Swadesh listeleri](#wiktionary-swadesh) — açık, güven: orta, ortam: ✓
- [translate.chv.su — Çuvaşça-Rusça derlem, çeviri ve sözlük (Plotnikov)](#cuvasca-ceviri) — açık, güven: orta, ortam: ✗

### Ses denklikleri

- [Brahmi, Tibet, Soğd ve Phags-pa harfli Eski Türkçe](#yabanci-yazili-eski-turkce) — kısmen, güven: yüksek, ortam: ✓
- [Castrén 1857 (Koybal ve Karagas) ve Böhtlingk 1851 (Sahaca) — ilk bilimsel tanımlar](#castren-bohtlingk) — açık, güven: yüksek, ortam: ✓
- [Ermeni harfli Kıpçakça (Garkavets 2010; Tryjarski 1968-72)](#ermeni-kipcak) — açık, güven: yüksek, ortam: ✓
- [Gaochang Guan Yiyu / Zazi — Ming dönemi Uygurca-Çince sözlük (15.-16. yy)](#gaochang-yiyu) — açık, güven: yüksek, ortam: ✓
- [Hotanca kaynaklarda Türkçe (Bailey 1939-55, Emmerick & Róna-Tas 1992, Hovdhaugen 1971)](#hotanca-turkce) — açık, güven: yüksek, ortam: ✓
- [ILCAA Turkic Basic Vocabulary (Tokyo Yabancı Diller Üniversitesi)](#turkbv) — açık, güven: yüksek, ortam: ✗
- [Johanson & Csató (ed.) — The Turkic Languages (2. baskı, 2021)](#johanson-csato) — ücretli, güven: yüksek, ortam: ✗
- [Meninski 1680 ve Latin harfli Osmanlıca (Megiser 1612, Molino 1641)](#meninski-transkripsiyon) — açık, güven: yüksek, ortam: ✓
- [Sovetskaya Tyurkologiya dergisi arşivi (Azerbaycan Cumhurbaşkanlığı Kütüphanesi, TurkLib)](#sovet-turkologiya) — açık, güven: yüksek, ortam: ✗
- [StarLing — Türk etimoloji veritabanı (Starostin, Dybo, Mudrak)](#starling) — açık, güven: yüksek, ortam: ✓
- [Çin kaynaklarındaki Eski Türkçe kelimeler (Ligeti 1950, Kasai, Vovin & McCraw)](#cin-transkripsiyonlari) — açık, güven: yüksek, ortam: ✓
- [Ünal — A Compendium of Common Turkic–Chuvash Lexical Correspondences with Proto-Turkic Reconstructions (2026)](#unal-2026) — açık, güven: yüksek, ortam: ✓
- [Сравнительно-историческая грамматика тюркских языков (Tenishev, 1984–2006)](#tenishev) — basılı, güven: yüksek
- [Этимологический словарь тюркских языков (ЭСТЯ, Sevortyan ve devamı)](#estja) — kısmen, güven: yüksek, ortam: ✓
- [ASK REAL — Kore Altayistik Derneği saha araştırmaları (2003-2009)](#kore-ask-real) — kısmen, güven: orta, ortam: ✗
- [Karamanlıca — Rum harfli Türkçe (Salaville & Dalleggio, Anatoli gazetesi)](#karamanlica) — açık, güven: orta, ortam: ✗
- [Monumenta Altaica — Türkoloji e-kütüphanesi](#altaica-kutuphane) — açık, güven: orta, ortam: ✓
- [Sino-Platonic Papers 325 — Proto-Turkic consonants](#proto-turkic-unsuzler) — açık, güven: orta, ortam: ✗
- [Wiktionary — About Proto-Turkic (yazım ve kuruluş kuralları)](#wiktionary-hakkinda) — açık, güven: orta, ortam: ✓

### Ortak alfabe ve yazım

- [Ortak Türk Alfabesi (Türk Devletleri Teşkilatı, 2024)](#ortak-turk-alfabesi) — açık, güven: yüksek, ortam: ✗
- [TurkicNLP — Türk dilleri için doğal dil işleme araç takımı](#turkicnlp) — açık, güven: orta, ortam: ✗

### Dilbilgisi (Aşama 3)

- [Ebû Hayyân — Kitâbü'l-İdrâk li-Lisâni'l-Etrâk (1312-13)](#kitab-idrak) — açık, güven: yüksek, ortam: ✓
- [Grambank](#grambank) — açık, güven: yüksek, ortam: ✗
- [Johanson & Csató (ed.) — The Turkic Languages (2. baskı, 2021)](#johanson-csato) — ücretli, güven: yüksek, ortam: ✗
- [Kaşkayca — Dolatkhah 2019, Qashqai Turkic (derlem tabanlı dilbilgisi)](#kaskayca) — basılı, güven: yüksek
- [WOWA — Word Order in Western Asia derlemi (Bamberg)](#wowa) — açık, güven: yüksek, ortam: ✗
- [Сравнительно-историческая грамматика тюркских языков (Tenishev, 1984–2006)](#tenishev) — basılı, güven: yüksek
- [til.im — Kumukça kitaplar ve sözlükler](#kumuk-kaynaklari) — açık, güven: orta, ortam: ✗

### Toplu, makinece okunabilir veri

- [Concepticon — kavram listeleri veritabanı](#concepticon) — açık, güven: yüksek, ortam: ✓
- [NorthEuraLex](#northeuralex) — açık, güven: yüksek, ortam: ✓
- [Radloff — Versuch eines Wörterbuches der Türk-Dialecte (1893-1911, 4 cilt)](#radloff) — açık, güven: yüksek, ortam: ✓
- [Savelyev & Robbeets — Turkic Basic Vocabularies (lexibank/savelyevturkic)](#savelyev-turkic) — açık, güven: yüksek, ortam: ✓
- [ASJP Database (Automated Similarity Judgment Program)](#asjp) — açık, güven: orta, ortam: ✓
- [Apertium — Türk dilleri çeviri çiftleri ve sözlükleri](#apertium) — açık, güven: orta, ortam: ✓
- [Elegant Lexicon — Turkic database (C. A. Straughn)](#elegant-lexicon) — açık, güven: orta, ortam: ✓
- [Leipzig Corpora Collection — kelime sıklık listeleri](#leipzig-corpora) — açık, güven: orta, ortam: ✗
- [Robbeets vd. 2021 — Triangulation (Transeurasian) veri seti](#robbeets-2021) — açık, güven: orta, ortam: ✗
- [Turkic Interlingua (TIL) — 22 Türk dili paralel derlemi](#til-mt) — açık, güven: orta, ortam: ✓
- [TurkicNLP — Türk dilleri için doğal dil işleme araç takımı](#turkicnlp) — açık, güven: orta, ortam: ✗
- [kaikki.org — Wiktionary'nin makinece okunabilir hâli (wiktextract)](#kaikki) — açık, güven: orta, ortam: ✓
- [neurotatarlar/tt-dictionaries — Tatarca sözlükler veri seti](#tatar-sozluk-veri) — açık, güven: orta, ortam: ✗
- [PanLex](#panlex) — açık, güven: düşük, ortam: ✗

### Makaleler ve bibliyografya

- [Azerbaycanca kaynaklar (Azərbaycan dilinin izahlı lüğəti, dilcilik.az)](#azerbaycan-kaynaklari) — kısmen, güven: yüksek, ortam: ✗
- [Glottolog](#glottolog) — açık, güven: yüksek, ortam: ✓
- [Göttingen Bilimler Akademisi — Altuigurisches Wörterbuch projesi](#gottingen-altuygur) — açık, güven: yüksek, ortam: ✗
- [ILCAA çevrim içi kaynak portalı (Tokyo)](#ilcaa-kaynaklari) — açık, güven: yüksek, ortam: ✗
- [KOHD — Almanya'daki Eski Uygurca el yazmaları kataloğu](#kohd-eski-uygurca) — açık, güven: yüksek, ortam: ✗
- [RBA Sibirya Şubesi Filoloji Enstitüsü (Novosibirsk) — dergiler ve e-kitaplık](#nsc-filoloji) — açık, güven: yüksek, ortam: ✗
- [Sovetskaya Tyurkologiya dergisi arşivi (Azerbaycan Cumhurbaşkanlığı Kütüphanesi, TurkLib)](#sovet-turkologiya) — açık, güven: yüksek, ortam: ✗
- [Studia Etymologica Cracoviensia (Krakov, 1996-2015) ve Stachowski'nin çalışmaları](#studia-etymologica-cracoviensia) — açık, güven: yüksek, ortam: ✗
- [Türk Dili Araştırmaları Yıllığı — Belleten](#tdk-belleten) — açık, güven: yüksek, ortam: ✗
- [Uluslararası Türk Lehçe Araştırmaları Dergisi (TÜRKLAD)](#turklad) — açık, güven: yüksek, ortam: ✓
- [DergiPark](#dergipark) — açık, güven: orta, ortam: ✓
- [Endangered Languages Project](#elp) — açık, güven: orta, ortam: ✗
- [Monumenta Altaica — Türkoloji e-kütüphanesi](#altaica-kutuphane) — açık, güven: orta, ortam: ✓
- [Novye issledovaniya Tuvy (Tuva üzerine yeni araştırmalar) dergisi](#tuva-dergi) — açık, güven: orta, ortam: ✗
- [YÖK Açık Bilim ve Tez Merkezi — Türkiye'deki lisansüstü tezler](#yok-acik-bilim) — kısmen, güven: orta, ortam: ✗
- [Vámbéry — Etymologisches Wörterbuch der turko-tatarischen Sprachen (1878)](#vambery-1878) — açık, güven: düşük, ortam: ✓

## Dile göre

Yalnızca o dili **özellikle** kapsayan kaynaklar. Bütün diller için geçerli kaynaklar (Wiktionary, StarLing, ESTJa, Savelyev vb.) her dil için ayrıca kullanılabilir.

| Dil | Kaynaklar |
|---|---|
| Çuvaşça (`chv`) | [cuvasca-asmarin](#cuvasca-asmarin), [northeuralex](#northeuralex), [ronatas-bati-eski-turkce](#ronatas-bati-eski-turkce), [cuvasca-etimoloji](#cuvasca-etimoloji), [unal-2026](#unal-2026), [kore-ask-real](#kore-ask-real), [apertium](#apertium), [rosstat-2021](#rosstat-2021), [strahlenberg-witsen](#strahlenberg-witsen), [cuvasca-ceviri](#cuvasca-ceviri) |
| Halaçça (`klj`) | [halacca](#halacca), [iran-dil-atlasi](#iran-dil-atlasi), [wold-halac](#wold-halac), [elegant-lexicon](#elegant-lexicon), [freelang](#freelang) |
| Türkiye Türkçesi (`tur`) | [osmanlica-batili-sozlukler](#osmanlica-batili-sozlukler), [scil-2026](#scil-2026), [meninski-transkripsiyon](#meninski-transkripsiyon), [northeuralex](#northeuralex), [salehi-2017](#salehi-2017), [tdk-portal](#tdk-portal), [tietze](#tietze), [tnc](#tnc), [wowa](#wowa), [apertium](#apertium), [en-sik-1000](#en-sik-1000), [karamanlica](#karamanlica), [komsu-dillerde-turkce](#komsu-dillerde-turkce), [leipzig-corpora](#leipzig-corpora), [lexilogos](#lexilogos), [nisanyan](#nisanyan), [opensubtitles-siklik](#opensubtitles-siklik), [qamus](#qamus), [sketch-engine-turk](#sketch-engine-turk), [turk-akademisi-terim](#turk-akademisi-terim), [lehceler-com](#lehceler-com) |
| Gagavuzca (`gag`) | [sovyet-iki-dilli-sozlukler](#sovyet-iki-dilli-sozlukler), [kore-ask-real](#kore-ask-real), [freelang](#freelang), [gagavuzca](#gagavuzca) |
| Balkan Gagavuz Türkçesi (`bgx`) | *özel kaynak bulunamadı* |
| Azerbaycan Türkçesi (`aze`) | [azerbaycan-kaynaklari](#azerbaycan-kaynaklari), [azerbaycan-diyalekt](#azerbaycan-diyalekt), [scil-2026](#scil-2026), [iran-dil-atlasi](#iran-dil-atlasi), [northeuralex](#northeuralex), [salehi-2017](#salehi-2017), [wowa](#wowa), [apertium](#apertium), [elegant-lexicon](#elegant-lexicon), [en-sik-1000](#en-sik-1000), [leipzig-corpora](#leipzig-corpora), [lexilogos](#lexilogos), [qamus](#qamus), [sketch-engine-turk](#sketch-engine-turk), [turk-akademisi-terim](#turk-akademisi-terim), [freelang](#freelang), [lehceler-com](#lehceler-com) |
| Irak Türkmencesi (Kerkük) (`kerkuk`) | *özel kaynak bulunamadı* |
| Kaşkayca (`qxq`) | [iran-dil-atlasi](#iran-dil-atlasi), [kaskayca](#kaskayca), [wowa](#wowa), [elegant-lexicon](#elegant-lexicon) |
| Türkmence (`tuk`) | [sovyet-iki-dilli-sozlukler](#sovyet-iki-dilli-sozlukler), [apertium](#apertium), [leipzig-corpora](#leipzig-corpora), [lexilogos](#lexilogos), [qamus](#qamus), [sketch-engine-turk](#sketch-engine-turk), [turkmen-etimoloji](#turkmen-etimoloji), [turkmen-sozluk](#turkmen-sozluk), [turk-akademisi-terim](#turk-akademisi-terim), [freelang](#freelang), [lehceler-com](#lehceler-com) |
| Horasan Türkçesi (`kmz`) | [iran-dil-atlasi](#iran-dil-atlasi), [elegant-lexicon](#elegant-lexicon) |
| Salarca (`slr`) | [salarca](#salarca), [cin-turk-dilleri](#cin-turk-dilleri), [kore-ask-real](#kore-ask-real) |
| Tatarca (`tat`) | [northeuralex](#northeuralex), [rf-turk-agiz-atlasi](#rf-turk-agiz-atlasi), [tugan-tel](#tugan-tel), [tatar-akademi-sozluk](#tatar-akademi-sozluk), [apertium](#apertium), [komsu-dillerde-turkce](#komsu-dillerde-turkce), [leipzig-corpora](#leipzig-corpora), [lexilogos](#lexilogos), [qamus](#qamus), [rosstat-2021](#rosstat-2021), [strahlenberg-witsen](#strahlenberg-witsen), [tatar-derlem](#tatar-derlem), [turk-akademisi-terim](#turk-akademisi-terim), [tatar-sozluk-veri](#tatar-sozluk-veri), [lehceler-com](#lehceler-com) |
| Başkurtça (`bak`) | [northeuralex](#northeuralex), [rf-turk-agiz-atlasi](#rf-turk-agiz-atlasi), [sovyet-iki-dilli-sozlukler](#sovyet-iki-dilli-sozlukler), [apertium](#apertium), [leipzig-corpora](#leipzig-corpora), [qamus](#qamus), [rosstat-2021](#rosstat-2021), [strahlenberg-witsen](#strahlenberg-witsen), [turk-akademisi-terim](#turk-akademisi-terim), [lehceler-com](#lehceler-com) |
| Kırım Tatarcası (`crh`) | [sovyet-iki-dilli-sozlukler](#sovyet-iki-dilli-sozlukler), [apertium](#apertium), [komsu-dillerde-turkce](#komsu-dillerde-turkce), [kirim-tatar-derlem](#kirim-tatar-derlem), [lexilogos](#lexilogos) |
| Karayca (`kdr`) | [karayca-eski-kayitlar](#karayca-eski-kayitlar), [karay-sozluk](#karay-sozluk), [kore-ask-real](#kore-ask-real) |
| Kırımçakça (`jct`) | *özel kaynak bulunamadı* |
| Urumca (`uum`) | [kore-ask-real](#kore-ask-real) |
| Kumukça (`kum`) | [apertium](#apertium), [rosstat-2021](#rosstat-2021), [kumuk-kaynaklari](#kumuk-kaynaklari), [freelang](#freelang) |
| Karaçay-Malkarca (`krc`) | [abaev-osetce](#abaev-osetce), [sovyet-iki-dilli-sozlukler](#sovyet-iki-dilli-sozlukler), [rosstat-2021](#rosstat-2021) |
| Kazakça (`kaz`) | [scil-2026](#scil-2026), [qazcorpus](#qazcorpus), [northeuralex](#northeuralex), [kazak-15-cilt](#kazak-15-cilt), [apertium](#apertium), [en-sik-1000](#en-sik-1000), [leipzig-corpora](#leipzig-corpora), [lexilogos](#lexilogos), [opensubtitles-siklik](#opensubtitles-siklik), [qamus](#qamus), [sketch-engine-turk](#sketch-engine-turk), [turk-akademisi-terim](#turk-akademisi-terim), [sozdik](#sozdik), [lehceler-com](#lehceler-com) |
| Karakalpakça (`kaa`) | [apertium](#apertium) |
| Nogayca (`nog`) | [apertium](#apertium), [rosstat-2021](#rosstat-2021), [freelang](#freelang) |
| Sibirya Tatarcası (`sty`) | [sibirya-tatar-agiz](#sibirya-tatar-agiz), [nsc-filoloji](#nsc-filoloji), [sibirya-eski-sozlukler](#sibirya-eski-sozlukler), [rosstat-2021](#rosstat-2021), [strahlenberg-witsen](#strahlenberg-witsen) |
| Kırgızca (`kir`) | [scil-2026](#scil-2026), [northeuralex](#northeuralex), [sovyet-iki-dilli-sozlukler](#sovyet-iki-dilli-sozlukler), [el-sozduk](#el-sozduk), [apertium](#apertium), [en-sik-1000](#en-sik-1000), [leipzig-corpora](#leipzig-corpora), [lexilogos](#lexilogos), [qamus](#qamus), [sketch-engine-turk](#sketch-engine-turk), [turk-akademisi-terim](#turk-akademisi-terim), [lehceler-com](#lehceler-com) |
| Güney Altayca (`alt`) | [elar](#elar), [khabtagaeva](#khabtagaeva), [nsc-filoloji](#nsc-filoloji), [rf-turk-agiz-atlasi](#rf-turk-agiz-atlasi), [sibirya-eski-sozlukler](#sibirya-eski-sozlukler), [kore-ask-real](#kore-ask-real), [rosstat-2021](#rosstat-2021) |
| Özbekçe (`uzb`) | [scil-2026](#scil-2026), [northeuralex](#northeuralex), [ozbek-izohli](#ozbek-izohli), [ozbek-etimoloji](#ozbek-etimoloji), [ozbek-kaynaklari](#ozbek-kaynaklari), [apertium](#apertium), [en-sik-1000](#en-sik-1000), [leipzig-corpora](#leipzig-corpora), [lexilogos](#lexilogos), [qamus](#qamus), [sketch-engine-turk](#sketch-engine-turk), [turk-akademisi-terim](#turk-akademisi-terim), [lehceler-com](#lehceler-com) |
| Uygurca (`uig`) | [scil-2026](#scil-2026), [sovyet-iki-dilli-sozlukler](#sovyet-iki-dilli-sozlukler), [bes-dilli-ayna](#bes-dilli-ayna), [apertium](#apertium), [cagatay-izahli](#cagatay-izahli), [leipzig-corpora](#leipzig-corpora), [lexilogos](#lexilogos), [qamus](#qamus), [turk-akademisi-terim](#turk-akademisi-terim), [freelang](#freelang), [lehceler-com](#lehceler-com) |
| İli Türkçesi (`ili`) | *özel kaynak bulunamadı* |
| Sahaca (Yakutça) (`sah`) | [castren-bohtlingk](#castren-bohtlingk), [khabtagaeva](#khabtagaeva), [northeuralex](#northeuralex), [nsc-filoloji](#nsc-filoloji), [sovyet-iki-dilli-sozlukler](#sovyet-iki-dilli-sozlukler), [sibirya-eski-sozlukler](#sibirya-eski-sozlukler), [tunguzca](#tunguzca), [kore-ask-real](#kore-ask-real), [apertium](#apertium), [rosstat-2021](#rosstat-2021), [strahlenberg-witsen](#strahlenberg-witsen), [sakhatyla](#sakhatyla) |
| Dolganca (`dlg`) | [tunguzca](#tunguzca), [kore-ask-real](#kore-ask-real), [rosstat-2021](#rosstat-2021) |
| Sarı Uygurca (`ybe`) | [elar](#elar), [cin-turk-dilleri](#cin-turk-dilleri), [kore-ask-real](#kore-ask-real), [dogu-yugur-sozluk](#dogu-yugur-sozluk) |
| Tuvaca (`tyv`) | [khabtagaeva](#khabtagaeva), [nsc-filoloji](#nsc-filoloji), [tatarintsev-tuvaca](#tatarintsev-tuvaca), [kore-ask-real](#kore-ask-real), [apertium](#apertium), [tuva-dergi](#tuva-dergi), [rosstat-2021](#rosstat-2021), [tuva-sozluk](#tuva-sozluk), [freelang](#freelang) |
| Tofaca (`kim`) | [castren-bohtlingk](#castren-bohtlingk), [elar](#elar), [khabtagaeva](#khabtagaeva), [nsc-filoloji](#nsc-filoloji), [sibirya-eski-sozlukler](#sibirya-eski-sozlukler), [tuva-dergi](#tuva-dergi), [rosstat-2021](#rosstat-2021), [lingsib](#lingsib), [tuva-sozluk](#tuva-sozluk) |
| Duhaca (Tsaatan) (`duha`) | [tuva-dergi](#tuva-dergi) |
| Soyotça (`soyot`) | [sibirya-eski-sozlukler](#sibirya-eski-sozlukler), [atlaskmns](#atlaskmns), [tuva-dergi](#tuva-dergi), [rosstat-2021](#rosstat-2021), [lingsib](#lingsib) |
| Hakasça (`kjh`) | [castren-bohtlingk](#castren-bohtlingk), [khabtagaeva](#khabtagaeva), [northeuralex](#northeuralex), [nsc-filoloji](#nsc-filoloji), [rf-turk-agiz-atlasi](#rf-turk-agiz-atlasi), [sovyet-iki-dilli-sozlukler](#sovyet-iki-dilli-sozlukler), [kore-ask-real](#kore-ask-real), [rosstat-2021](#rosstat-2021), [strahlenberg-witsen](#strahlenberg-witsen), [freelang](#freelang) |
| Şorca (`cjs`) | [nsc-filoloji](#nsc-filoloji), [rf-turk-agiz-atlasi](#rf-turk-agiz-atlasi), [sibirya-eski-sozlukler](#sibirya-eski-sozlukler), [kore-ask-real](#kore-ask-real), [atlaskmns](#atlaskmns), [rosstat-2021](#rosstat-2021) |
| Çulımca (`clw`) | [elar](#elar), [nsc-filoloji](#nsc-filoloji), [rf-turk-agiz-atlasi](#rf-turk-agiz-atlasi), [sibirya-eski-sozlukler](#sibirya-eski-sozlukler), [kore-ask-real](#kore-ask-real), [atlaskmns](#atlaskmns), [rosstat-2021](#rosstat-2021), [tuva-sozluk](#tuva-sozluk) |
| Fuyu Kırgızcası (`fuyu`) | [cin-turk-dilleri](#cin-turk-dilleri), [kore-ask-real](#kore-ask-real) |
| Kuzey Altayca (`atv`) | [nsc-filoloji](#nsc-filoloji), [rf-turk-agiz-atlasi](#rf-turk-agiz-atlasi), [sibirya-eski-sozlukler](#sibirya-eski-sozlukler), [rosstat-2021](#rosstat-2021) |
| Eski Türkçe (Göktürk ve Uygur metinleri) (`otk`) | [turfan-bbaw](#turfan-bbaw), [bizans-kaynaklari](#bizans-kaynaklari), [yabanci-yazili-eski-turkce](#yabanci-yazili-eski-turkce), [clauson](#clauson), [eski-turkce-odunc-katmanlari](#eski-turkce-odunc-katmanlari), [gaochang-yiyu](#gaochang-yiyu), [gottingen-altuygur](#gottingen-altuygur), [hotanca-turkce](#hotanca-turkce), [kohd-eski-uygurca](#kohd-eski-uygurca), [mogolistan-yazitlari](#mogolistan-yazitlari), [sogdca](#sogdca), [turfan-ilk-yayinlar](#turfan-ilk-yayinlar), [vatec](#vatec), [wilkens-eski-uygurca](#wilkens-eski-uygurca), [cin-transkripsiyonlari](#cin-transkripsiyonlari), [dts](#dts), [arap-fars-cografyacilar](#arap-fars-cografyacilar), [iran-turk-temasi](#iran-turk-temasi), [tibet-kaynaklari](#tibet-kaynaklari), [toharca](#toharca), [turik-bitig](#turik-bitig), [eski-turkce-yerel-sozlukler](#eski-turkce-yerel-sozlukler) |
| Volga Bulgarcası (`xbo`) | [bizans-kaynaklari](#bizans-kaynaklari), [erdal-volga-bulgar](#erdal-volga-bulgar), [hazarca](#hazarca), [ronatas-bati-eski-turkce](#ronatas-bati-eski-turkce), [cuvasca-etimoloji](#cuvasca-etimoloji), [arap-fars-cografyacilar](#arap-fars-cografyacilar) |
| Karahanlıca (Dîvânu Lugâti't-Türk, Kutadgu Bilig) (`xqa`) | [boeschoten](#boeschoten), [clauson](#clauson), [dlt](#dlt), [dts](#dts), [suryani-yazitlar](#suryani-yazitlar) |
| Kuman-Kıpçakça (Codex Cumanicus, Memlük Kıpçakçası) (`qwm`) | [bizans-kaynaklari](#bizans-kaynaklari), [boeschoten](#boeschoten), [bulgat-durre](#bulgat-durre), [codex-cumanicus](#codex-cumanicus), [kitab-idrak](#kitab-idrak), [ermeni-kipcak](#ermeni-kipcak), [gronbech-kuman](#gronbech-kuman), [houtsma-leiden](#houtsma-leiden), [najip-xiv](#najip-xiv), [rasulid-hexaglot](#rasulid-hexaglot), [toparli-kipcak](#toparli-kipcak), [tuhfe-zekiyye](#tuhfe-zekiyye), [ibn-muhenna](#ibn-muhenna), [komsu-dillerde-turkce](#komsu-dillerde-turkce) |
| Eski Anadolu Türkçesi (`eski-anadolu`) | [meninski-transkripsiyon](#meninski-transkripsiyon), [rasulid-hexaglot](#rasulid-hexaglot), [tdk-portal](#tdk-portal), [tietze](#tietze), [bahsayis](#bahsayis), [karamanlica](#karamanlica) |
| Harezm Türkçesi ve Çağatayca (`chg`) | [boeschoten](#boeschoten), [gaochang-yiyu](#gaochang-yiyu), [senglah](#senglah), [najip-xiv](#najip-xiv), [bedayi-lugat](#bedayi-lugat), [bes-dilli-ayna](#bes-dilli-ayna), [mukaddimet-edeb](#mukaddimet-edeb), [ibn-muhenna](#ibn-muhenna), [abuska](#abuska), [akvius-cagatayca](#akvius-cagatayca), [cagatay-batili-sozlukler](#cagatay-batili-sozlukler), [cagatay-izahli](#cagatay-izahli) |

## Bütün kaynaklar

### Etimoloji ve karşılaştırmalı sözlükler

<a id="abaev-osetce"></a>
#### Abaev — Osetçenin tarihî-etimolojik sözlüğü (1958-95, 4 cilt)

<
https://search.worldcat.org/search?q=Abaev+istoriko-etimologicheskij+slovar+osetinskogo>

Karaçay-Malkarcadaki Osetçe (Alan) kökenli kelimeleri ve Osetçedeki Türkçe ödünçleri ayırmak için.

**Nasıl kullanılır:** Basılı (Rusça).

- **Diller:** Karaçay-Malkarca
- **İşe yaradığı yer:** Ödünç ve miras ayrımı (özellikle Çuvaşça)
- **Erişim:** basılı · **Biçim:** basili · **Güven:** yüksek · **Durum:** basılı · **Ortam:** —
- **Kimlik:** `abaev-osetce`

<a id="clauson"></a>
#### Clauson — An Etymological Dictionary of Pre-Thirteenth-Century Turkish (1972)

<
https://archive.org/details/sir-gerard-clauson-an-etymological-dictionary-of-pre-thirteenth-century-turkish->

13. yüzyıl öncesi Türkçenin (Eski Türkçe, Karahanlıca) temel etimoloji sözlüğü.

**Nasıl kullanılır:** Internet Archive'da tam tarama (PDF ve metin). Madde başları Clauson'un kendi sırasıyla dizili (ünsüz iskeletine göre). Bu yüzden önce ayrı dizin cildine (Szeged 1981, Studia Uralo-Altaica) ya da PDF'in metin aramasına bak.

- **Diller:** Eski Türkçe (Göktürk ve Uygur metinleri), Karahanlıca (Dîvânu Lugâti't-Türk, Kutadgu Bilig)
- **İşe yaradığı yer:** Ana Türkçe kuruluşu ve etimoloji, Tarihî tanık biçimleri
- **Erişim:** kısmen · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: eski adres (etymologicaldict00clau) 404 veriyordu; yeni archive.org kaydı açıldı (HTTP 200).
- **Kimlik:** `clauson`

<a id="doerfer-tmen"></a>
#### Doerfer — Türkische und mongolische Elemente im Neupersischen (TMEN, 1963-75)

<
https://altaica.ru/LIBRARY/runic/Doerfer_T%C3%BCrkische%20und%20mongolische%20Elemente%20im%20Neupersischen.%20Bd.%201_1963.pdf>

Farsçaya geçmiş Türkçe ve Moğolca kelimelerin 4 ciltlik etimolojik sözlüğü. Her kelimenin bütün Türk dillerindeki karşılıklarını tartışır; Türkçe mi Moğolca mı sorusunda temel başvuru.

**Nasıl kullanılır:** Almanca. Altaica'da 1. cilt doğrulandı; diğer ciltler aynı dizinde aranmalı.

- **Diller:** bütün diller
- **İşe yaradığı yer:** Ödünç ve miras ayrımı (özellikle Çuvaşça), Tarihî tanık biçimleri, Ana Türkçe kuruluşu ve etimoloji
- **Erişim:** kısmen · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: altaica 1. cilt PDF'i açıldı (HTTP 200/206).
- **Kimlik:** `doerfer-tmen`

<a id="dybo-2013"></a>
#### Dybo — Этимологический словарь базисной лексики тюркских языков (2013, ЭСТЯ ek cilt 9)

<https://altaica.ru/LIBRARY/turks/Дыбо_Этимологический%20словарь%20базисной%20лексики%20тюркских%20языков%202013.pdf>

Temel söz varlığının (Swadesh tipi) etimoloji sözlüğü; Aşama 1 için birebir.

**Nasıl kullanılır:** PDF; kavram bazında düzenlenmiş.

- **Diller:** bütün diller
- **İşe yaradığı yer:** Ana Türkçe kuruluşu ve etimoloji, Yaşayan dillerde biçim toplama, Sıklık listeleri ve kavram listeleri
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: PDF indirildi (HTTP 200, ~22 MB).
- **Kimlik:** `dybo-2013`

<a id="eski-turkce-odunc-katmanlari"></a>
#### Eski Türkçedeki ödünç katmanları üzerine makaleler (Moğolca, Samoyedce, Kitanca)

<
https://altaica.ru/LIBRARY/runic/Rybatzki_Classification%20of%20Old%20Turkic%20loanwords%20in%20Mongolic_2011.PDF>

Eski Türkçede Moğolca var mı, Moğolcadaki Eski Türkçe ödünçler, Samoyed-Ugor ve Kitan temasları.

**Nasıl kullanılır:** Clark 1977: https://altaica.ru/LIBRARY/runic/Clark_Mongol%20Elements%20in%20Old%20Turkic%20%28OCR%29_1977.pdf ; Doerfer 1992: https://altaica.ru/LIBRARY/runic/Doerfer_Mongolica%20im%20Altt%C3%BCrkischen_1992.pdf ; Doerfer 1993: https://altaica.ru/LIBRARY/runic/Doerfer_The%20Older%20Mongolian%20Layer%20in%20Ancient%20Turkic_1993.pdf ; Clauson 1960, Turk, Mongol, Tungus: https://altaica.ru/LIBRARY/runic/Clauson_Turk,%20Mongol,%20Tungus_1960.pdf ; Sinor: https://altaica.ru/LIBRARY/runic/Sinor_Samoyed%20and%20Ugric%20Elements%20in%20Old%20Turkic_1979-80.pdf ; Vovin 2013, Kitanca: https://altaica.ru/LIBRARY/runic/Vovin_Old%20Turkic%20Loanwords%20in%20the%20Khitan%20Language%20%28Fs%20Sertkaya,%20Yal%C4%B1m%20Kaya%20Bitigi%29_2013.pdf

- **Diller:** Eski Türkçe (Göktürk ve Uygur metinleri)
- **İşe yaradığı yer:** Ödünç ve miras ayrımı (özellikle Çuvaşça), Ana Türkçe kuruluşu ve etimoloji
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: yedi altaica PDF'i açıldı (HTTP 200/206).
- **Kimlik:** `eski-turkce-odunc-katmanlari`

<a id="khabtagaeva"></a>
#### Khabtagaeva — Sibirya Türk dillerinde Moğolca ödünçler

<https://search.worldcat.org/search?q=Khabtagaeva+Mongolic+elements+in+Tuvan>

Khabtagaeva 2009, Mongolic Elements in Tuvan (Harrassowitz) ve 2019, Language Contact in Siberia (Brill). Tuvaca ve komşularındaki Moğolca ödünçlerin katmanları.

**Nasıl kullanılır:** Basılı. Sibirya dillerinde bir biçimin Türkçe mi Moğolca ödünç mü olduğunu ayırmak için.

- **Diller:** Tuvaca, Sahaca (Yakutça), Güney Altayca, Hakasça, Tofaca
- **İşe yaradığı yer:** Ödünç ve miras ayrımı (özellikle Çuvaşça)
- **Erişim:** basılı · **Biçim:** basili · **Güven:** yüksek · **Durum:** basılı · **Ortam:** —
- **Kimlik:** `khabtagaeva`

<a id="mogolca-etimoloji"></a>
#### Moğol dilleri karşılaştırmalı ve etimolojik sözlükleri (Sun Zhu 1990; Sanjeev vd. 2015-18; Sühbaatar)

<https://altaica.ru/LIBRARY/mong/Sun_comparative_dict.pdf>

Bir kelimenin Moğol dillerinin hepsinde olup olmadığı ve Türkçeden mi geldiği. Sühbaatar'ın Moğolcadaki yabancı kelimeler sözlüğü Türkçe kökenlileri işaretler.

**Nasıl kullanılır:** Sun Zhu (Çince) PDF. Sühbaatar: https://altaica.ru/LIBRARY/Sukhebaatar_foreign_words.pdf ; Sanjeev, Orlovskaya, Şevernina etimolojik sözlüğü (Rusça, 3 cilt) book.ivran.ru'da.

- **Diller:** bütün diller
- **İşe yaradığı yer:** Ödünç ve miras ayrımı (özellikle Çuvaşça)
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: Sun Zhu ve Sühbaatar PDF'leri açıldı (HTTP 200/206).
- **Not:** book.ivran.ru bu ortamdan çözülemedi.
- **Kimlik:** `mogolca-etimoloji`

<a id="ozbek-etimoloji"></a>
#### Rahmatullayev — O'zbek tilining etimologik lug'ati

<https://search.worldcat.org/search?q=O%27zbek+tilining+etimologik+lug%27ati>

Özbekçenin etimoloji sözlüğü (Türkçe kökenli kelimeler, Farsça ve Arapça alıntılar ayrı ciltlerde; 2000–2009).

**Nasıl kullanılır:** Basılı; Özbekistan kütüphanelerinde elektronik kopyalar. Özbekçenin Farsça alıntılarını ayıklamak için.

- **Diller:** Özbekçe
- **İşe yaradığı yer:** Ana Türkçe kuruluşu ve etimoloji, Ödünç ve miras ayrımı (özellikle Çuvaşça)
- **Erişim:** basılı · **Biçim:** basili · **Güven:** yüksek · **Durum:** basılı · **Ortam:** —
- **Kimlik:** `ozbek-etimoloji`

<a id="rasanen"></a>
#### Räsänen — Versuch eines etymologischen Wörterbuchs der Türksprachen (1969)

<https://altaica.ru/LIBRARY/turks/Rasanen_VEWT%201969.pdf>

Türk dillerinin karşılaştırmalı etimoloji sözlüğü (Almanca).

**Nasıl kullanılır:** Altaica'da PDF. Ses tarihi için Räsänen 1949, Materialien zur Lautgeschichte: https://altaica.ru/LIBRARY/runic/R%C3%A4s%C3%A4nen_Materialien%20zur%20Lautgeschichte%20der%20t%C3%BCrkischen%20Sprachen_1949.pdf

- **Diller:** bütün diller
- **İşe yaradığı yer:** Ana Türkçe kuruluşu ve etimoloji
- **Erişim:** kısmen · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: iki altaica PDF'i açıldı (HTTP 200/206).
- **Kimlik:** `rasanen`

<a id="sogdca"></a>
#### Soğdca ödünçler (Gharib 1995 sözlüğü, Ayazlı 2020, Wilkens 2021)

<https://dergipark.org.tr/en/download/article-file/1180997>

Eski Uygurcadaki Soğdca kelimeler (din, ticaret, yazı terimleri). 'Ele' ilkesi için ödünç ayıklamaya yarar.

**Nasıl kullanılır:** Ayazlı 2020 (Uluslararası Eski Uygurca Araştırmaları Dergisi, Türkçe) DergiPark'tan iner. Gharib, Sogdian Dictionary (Tahran 1995) basılı. Wilkens 2021: bitig.ogu.edu.tr.

- **Diller:** Eski Türkçe (Göktürk ve Uygur metinleri)
- **İşe yaradığı yer:** Ödünç ve miras ayrımı (özellikle Çuvaşça)
- **Erişim:** kısmen · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: DergiPark PDF'i açıldı (HTTP 200/206).
- **Kimlik:** `sogdca`

<a id="starling"></a>
#### StarLing — Türk etimoloji veritabanı (Starostin, Dybo, Mudrak)

<https://starlingdb.org/>

Türk dilleri etimoloji veritabanı (turcet); Ana Türkçe kuruluşlar, dillerdeki biçimler, Sevortyan/Räsänen göndermeleri. EDAL'ın (2003) çalışma ortamı.

**Nasıl kullanılır:** Sorgu: https://starlingdb.org/cgi-bin/response.cgi?root=config&morpho=0&basename=\data\alt\turcet&first=1&text_meaning=<anlam>&method_meaning=exact Eski adres starling.rinet.ru buraya yönlendiriyor.

- **Diller:** bütün diller
- **İşe yaradığı yer:** Ana Türkçe kuruluşu ve etimoloji, Yaşayan dillerde biçim toplama, Ses denklikleri
- **Erişim:** açık · **Biçim:** web · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: ana sayfa açıldı (HTTP 200). Veritabanı sorguları (cgi-bin) zaman zaman 502/504 veriyor; sunucu tarafı sorun, birkaç dakika sonra yeniden dene. starling.rinet.ru eski adres.
- **Not:** Altay dil ailesi hipotezine dayanır: yalnızca Türk dilleri kısmı kullanılmalı.
- **Kimlik:** `starling`

<a id="tatarintsev-tuvaca"></a>
#### Tatarintsev — Tuvacanın etimolojik sözlüğü (2000-)

<
https://altaica.ru/LIBRARY/turks/%D0%A2%D0%B0%D1%82%D0%B0%D1%80%D0%B8%D0%BD%D1%86%D0%B5%D0%B2_%D0%AD%D1%82%D0%B8%D0%BC%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%87.%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C%20%D1%82%D1%83%D0%B2.%20%D1%8F%D0%B7._I%202000.pdf>

Tuvaca kelimelerin kökeni; Moğolca ödünçleri tek tek tartışır.

**Nasıl kullanılır:** Rusça PDF (altaica'da 1. ve 2. cilt).

- **Diller:** Tuvaca
- **İşe yaradığı yer:** Ana Türkçe kuruluşu ve etimoloji, Ödünç ve miras ayrımı (özellikle Çuvaşça)
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: 1. cilt PDF'i açıldı (HTTP 200/206).
- **Kimlik:** `tatarintsev-tuvaca`

<a id="tietze"></a>
#### Tietze — Tarihî ve Etimolojik Türkiye Türkçesi Lugatı (TÜBA)

<https://www.tuba.gov.tr>

~42.000 madde başı, 71.000 örnek cümle; Kıbrıs vb. ağız verisi de içerir.

**Nasıl kullanılır:** Basılı (TÜBA, çok ciltli).

- **Diller:** Türkiye Türkçesi, Eski Anadolu Türkçesi
- **İşe yaradığı yer:** Ana Türkçe kuruluşu ve etimoloji, Tarihî tanık biçimleri, Ağız verisi
- **Erişim:** basılı · **Biçim:** basili · **Güven:** yüksek · **Durum:** basılı · **Ortam:** —
- **Not:** Kıbrıs ağzı verileri üzerine bir inceleme: akmb.gov.tr (Emine Yılmaz). TÜBA'nın tanıtım PDF'i tuba.gov.tr/files/images/2020/tietze 10 cilt/ altında.
- **Kimlik:** `tietze`

<a id="tunguzca"></a>
#### Tunguz-Mançu dilleri karşılaştırmalı sözlüğü (Tsintsius 1975-77) ve Evenkçe sözlük

<https://altaica.ru/tms.php>

Sahaca ve Dolganca kelimelerin bir kısmı Evenkçe ve Evence kökenlidir; Tunguz kökenlileri ayırmak için.

**Nasıl kullanılır:** Altaica'da SSTMYa sorgu sayfası. Vasileviç Evenkçe sözlüğü: https://altaica.ru/LIBRARY/tungus/vasilevich_dict.pdf ; StarLing'de Tunguz etimoloji veritabanı da var.

- **Diller:** Sahaca (Yakutça), Dolganca
- **İşe yaradığı yer:** Ödünç ve miras ayrımı (özellikle Çuvaşça)
- **Erişim:** açık · **Biçim:** web · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: tms.php sayfası; Vasileviç PDF'i açıldı (HTTP 200/206).
- **Kimlik:** `tunguzca`

<a id="cuvasca-etimoloji"></a>
#### Çuvaşça etimoloji sözlükleri (Yegorov 1964, Fedotov 1996, Zolotnitski 1875, Paasonen)

<https://altaica.ru/LIBRARY/chuvash.pdf>

Çuvaşça kelimelerin kökeni: Ana Türkçe mirası, Tatarca, Marice ve Rusça ödünçler. Zolotnitski 1875 ve Paasonen'in (Macarca-Almanca) eski kayıtları bugünkünden önceki biçimleri verir.

**Nasıl kullanılır:** Fedotov: https://altaica.ru/LIBRARY/fedotov1.pdf ; Zolotnitski: https://altaica.ru/LIBRARY/turks/%D0%97%D0%BE%D0%BB%D0%BE%D1%82%D0%BD%D0%B8%D1%86%D0%BA%D0%B8%D0%B9_%D0%9A%D0%BE%D1%80%D0%BD%D0%B5%D0%B2%D0%BE%D0%B9%20%D1%87%D1%83%D0%B2%D0%B0%D1%88%D1%81%D0%BA%D0%BE-%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C%201875.pdf ; Paasonen: https://altaica.ru/LIBRARY/turks/Paasonen_Tschuwaschisches%20Worterverzeichnis%201974.pdf ; Volga bölgesi temasları için Agyagási 2019, Chuvash Historical Phonetics (Harrassowitz, basılı).

- **Diller:** Çuvaşça, Volga Bulgarcası
- **İşe yaradığı yer:** Ödünç ve miras ayrımı (özellikle Çuvaşça), Ana Türkçe kuruluşu ve etimoloji, Tarihî tanık biçimleri
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: dört altaica PDF'i açıldı (HTTP 200/206).
- **Kimlik:** `cuvasca-etimoloji`

<a id="unal-2026"></a>
#### Ünal — A Compendium of Common Turkic–Chuvash Lexical Correspondences with Proto-Turkic Reconstructions (2026)

<https://univerlag.uni-goettingen.de/handle/3/isbn-978-3-86395-657-8>

Ortak Türkçe ile Çuvaşça arasındaki ortak kökenli kelimelerin derlemesi, Ana Türkçe kuruluşlarıyla. Çuvaşçadaki miras/ödünç ayrımı ve Hedef 2 (kök yaşı) için en doğrudan kaynak.

**Nasıl kullanılır:** Göttingen Üniversitesi Yayınevi; OAPEN açık erişim kaydı var (DOI 10.17875/gup2025-2765).

- **Diller:** Çuvaşça, bütün diller
- **İşe yaradığı yer:** Ödünç ve miras ayrımı (özellikle Çuvaşça), Ana Türkçe kuruluşu ve etimoloji, Ses denklikleri
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: yayınevi sayfası açıldı (HTTP 200); PDF bağlantısı sayfada.
- **Kimlik:** `unal-2026`

<a id="estja"></a>
#### Этимологический словарь тюркских языков (ЭСТЯ, Sevortyan ve devamı)

<https://altaica.ru/LIBRARY/e_edtl.php>

Türk dillerinin en kapsamlı etimoloji sözlüğü. Cilt 1 (ünlüyle başlayanlar, 1974), 2 (B, 1978), 3 (V/G/D, 1980), 4-6 (Ž/Y, K, Q), 7 (L/M/N/P/S, 2003); 8. cilt hazırlanıyor.

**Nasıl kullanılır:** Altaica sayfasından cilt PDF'leri (ör. LIBRARY/ESTJA/estja1.pdf, LIBRARY/ESTJA/Estja7.pdf). Rusçadır; madde başları Türkçe köklerdir.

- **Diller:** bütün diller
- **İşe yaradığı yer:** Ana Türkçe kuruluşu ve etimoloji, Yaşayan dillerde biçim toplama, Ses denklikleri
- **Erişim:** kısmen · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: dizin sayfası açıldı (HTTP 200). Ciltler PDF olarak altaica.ru/LIBRARY/ESTJA/ altında (estja1.pdf … Estja7.pdf).
- **Not:** Taramaların telif durumu belirsiz.
- **Kimlik:** `estja`

<a id="iran-turk-temasi"></a>
#### Eski İran dilleriyle temas (Harmatta 1972 Irano-Turcica; Sims-Williams, Baktrça adlar)

<https://altaica.ru/LIBRARY/runic/Harmatta_Irano-Turcica_1972.pdf>

Baktrça belge ve sikkelerde (7.-8. yy) kağan, tarkan, tudun gibi Türkçe unvanlar ve adlar; Eski Türkçedeki İran kökenli kelimeler.

**Nasıl kullanılır:** Sims-Williams, Bactrian Personal Names (Avusturya Bilimler Akademisi 2010, basılı).

- **Diller:** Eski Türkçe (Göktürk ve Uygur metinleri)
- **İşe yaradığı yer:** Ödünç ve miras ayrımı (özellikle Çuvaşça), Tarihî tanık biçimleri
- **Erişim:** kısmen · **Biçim:** pdf · **Güven:** orta · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: altaica PDF'i açıldı (HTTP 200/206).
- **Kimlik:** `iran-turk-temasi`

<a id="edal"></a>
#### Etymological Dictionary of the Altaic Languages (Starostin, Dybo, Mudrak 2003)

<https://en.wikipedia.org/wiki/Etymological_Dictionary_of_the_Altaic_Languages>

3 cilt, ~2.800 etimoloji; miras ile ödünç ayrımı yapar.

**Nasıl kullanılır:** Verisi StarLing'de çevrim içi.

- **Diller:** bütün diller
- **İşe yaradığı yer:** Ana Türkçe kuruluşu ve etimoloji
- **Erişim:** basılı · **Biçim:** basili · **Güven:** orta · **Durum:** basılı · **Ortam:** —
- **Not:** Altay hipotezi tartışmalıdır; Türk içi kuruluşları güvenilir, Altay karşılaştırmaları değil.
- **Kimlik:** `edal`

<a id="komsu-dillerde-turkce"></a>
#### Komşu dillerdeki Türkçe ödünçler (Miklosich 1884, Şipova 1976, Škaljić 1966)

<https://archive.org/details/dietrkischenele00miklgoog>

Balkan ve Doğu Avrupa dillerine (Rumca, Arnavutça, Bulgarca, Sırpça, Rumence, Macarca, Lehçe, Rusça) geçmiş Türkçe kelimeler. Ödünç biçim çoğu zaman kaynak dilin eski telaffuzunu korur.

**Nasıl kullanılır:** Miklosich archive.org (Almanca). Rusçadaki Türkçe kelimeler: https://altaica.ru/LIBRARY/turks/%D0%A8%D0%B8%D0%BF%D0%BE%D0%B2%D0%B0_%D0%A1%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C%20%D1%82%D1%8E%D1%80%D0%BA%D0%B8%D0%B7%D0%BC%D0%BE%D0%B2%20%D0%B2%20%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%BC%20%D1%8F%D0%B7%D1%8B%D0%BA%D0%B5%201976.pdf ; Sırp-Hırvatça: Škaljić, Turcizmi (Sarajevo 1966, basılı); Rumence: Şăineanu 1900 (Fransızca).

- **Diller:** Türkiye Türkçesi, Kuman-Kıpçakça (Codex Cumanicus, Memlük Kıpçakçası), Kırım Tatarcası, Tatarca
- **İşe yaradığı yer:** Tarihî tanık biçimleri, Ödünç ve miras ayrımı (özellikle Çuvaşça)
- **Erişim:** açık · **Biçim:** pdf · **Güven:** orta · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: Miklosich archive.org kaydı; Şipova PDF'i açıldı (HTTP 200/206).
- **Kimlik:** `komsu-dillerde-turkce`

<a id="nisanyan"></a>
#### Nişanyan Sözlük — Çağdaş Türkçenin Etimolojisi

<https://www.nisanyansozluk.com>

Türkiye Türkçesi kelimelerinin kökeni, ilk tanıklıkları.

**Nasıl kullanılır:** Madde adresi /kelime/<kelime>.

- **Diller:** Türkiye Türkçesi
- **İşe yaradığı yer:** Ana Türkçe kuruluşu ve etimoloji, Ödünç ve miras ayrımı (özellikle Çuvaşça)
- **Erişim:** kısmen · **Biçim:** web · **Güven:** orta · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: açıldı (HTTP 200).
- **Not:** Türkçe etimolojide hızlı ilk bakış. Türk dilleri arası köken bağlantılarında tek başına kullanma; Clauson, ESTJa ya da Tietze ile denetle.
- **Kimlik:** `nisanyan`

<a id="toharca"></a>
#### Toharca ile Türkçe temasları (CEToM, Carling & Pinault, Róna-Tas 1974)

<
https://altaica.ru/LIBRARY/runic/R%C3%B3na-Tas_Tocharische%20Elemente%20in%20den%20altaischen%20Sprachen_1974.pdf>

Eski Türkçe ile Toharca arasındaki karşılıklı ödünçler; Ana Türkçenin çok eski temas katmanını ayırmak için.

**Nasıl kullanılır:** CEToM (cetom.univie.ac.at) metin veritabanı; Carling & Pinault, Toharca A sözlüğü (Harrassowitz 2023, çevrim içi De Gruyter 2025) ödünçlerin kaynağını gösterir; Toharca B için Adams 2013. Toharca 100 kelimelik liste StarLing'de: https://starlingdb.org/new100/txr.pdf

- **Diller:** Eski Türkçe (Göktürk ve Uygur metinleri)
- **İşe yaradığı yer:** Ödünç ve miras ayrımı (özellikle Çuvaşça), Ana Türkçe kuruluşu ve etimoloji
- **Erişim:** kısmen · **Biçim:** pdf · **Güven:** orta · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: altaica PDF'i açıldı (HTTP 200/206).
- **Not:** cetom.univie.ac.at bu ortamda izinli değil.
- **Kimlik:** `toharca`

<a id="turkmen-etimoloji"></a>
#### Türkmence etimoloji ve açıklamalı sözlükler (Atanyýazow; Türkmen diliniň düşündirişli sözlügi)

<https://search.worldcat.org/search?q=T%C3%BCrkmen+dilini%C5%88+s%C3%B6zl%C3%BCgi>

S. Atanyýazow'un Türkmence etimoloji ve ad sözlükleri; Türkmen diliniň düşündirişli sözlügi (2 cilt). Türkmence ağızlar için Türkmen diliniň dialektlerinin atlası.

**Nasıl kullanılır:** Basılı; Türkiye kütüphanelerinde Türkçe çevirileri de var.

- **Diller:** Türkmence
- **İşe yaradığı yer:** Ana Türkçe kuruluşu ve etimoloji, Yaşayan dillerde biçim toplama, Ağız verisi
- **Erişim:** basılı · **Biçim:** basili · **Güven:** orta · **Durum:** basılı · **Ortam:** —
- **Not:** Künyeler kütüphane kataloğundan denetlenmeli.
- **Kimlik:** `turkmen-etimoloji`

<a id="wiktionary-hakkinda"></a>
#### Wiktionary — About Proto-Turkic (yazım ve kuruluş kuralları)

<https://en.wiktionary.org/wiki/Wiktionary:About_Proto-Turkic>

Wiktionary'nin Ana Türkçe kuruluşlarında kullandığı yazım ve ses kuralları.

**Nasıl kullanılır:** Ana Türkçe biçimlerini (*bẹ, *tāĺ…) okumadan önce bakılır.

- **Diller:** bütün diller
- **İşe yaradığı yer:** Ana Türkçe kuruluşu ve etimoloji, Ses denklikleri
- **Erişim:** açık · **Biçim:** web · **Güven:** orta · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: Wikimedia hız sınırı (HTTP 429). Önceki denemede açılmıştı; ardışık isteklerde 1-2 saniye bekle, ya da kaikki dökümünü kullan.
- **Kimlik:** `wiktionary-hakkinda`

<a id="wiktionary-ana-turkce"></a>
#### Wiktionary — Ana Türkçe (Proto-Turkic) maddeleri

<https://en.wiktionary.org/wiki/Category:Proto-Turkic_lemmas>

Ana Türkçe yeniden kuruluşları ve her maddenin altında torun dillerdeki biçimler (30-40 dil), çekim tablosu, kaynakça (Clauson, ESTJa, Räsänen, DLT).

**Nasıl kullanılır:** Ham metin: https://en.wiktionary.org/wiki/Reconstruction:Proto-Turkic/<kök>?action=raw. Çoğu madde yönlendirmedir (ör. ben → be, sen → se); yönlendirmeyi izle. API'yi (w/api.php) sık çağırma: Wikimedia hız sınırı uyguluyor; istekler arasında bekle ve genel bir User-Agent kullan.

- **Diller:** bütün diller
- **İşe yaradığı yer:** Ana Türkçe kuruluşu ve etimoloji, Yaşayan dillerde biçim toplama, Tarihî tanık biçimleri
- **Erişim:** açık · **Biçim:** web · **Güven:** orta · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: kategori sayfası açıldı (HTTP 200). Madde ham metni ?action=raw ile alınıyor (ben, sen, o bu yolla araştırıldı).
- **Not:** Kaynakçası iyi ama topluluk ürünüdür; küçük diller ve ağızlar eksik olabilir.
- **Kimlik:** `wiktionary-ana-turkce`

<a id="vambery-1878"></a>
#### Vámbéry — Etymologisches Wörterbuch der turko-tatarischen Sprachen (1878)

<https://archive.org/details/etymologischesw00vmuoft>

İlk Türkçe etimoloji sözlüğü; kök aileleri. Bilim tarihi açısından önemli.

**Nasıl kullanılır:** Almanca, archive.org; aynı dosya altaica LIBRARY/turks altında.

- **Diller:** bütün diller
- **İşe yaradığı yer:** Ana Türkçe kuruluşu ve etimoloji, Makaleler ve bibliyografya
- **Erişim:** açık · **Biçim:** pdf · **Güven:** düşük · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: archive.org kaydı açıldı (HTTP 200/206).
- **Not:** Etimolojilerinin çoğu eskimiştir; yalnız biçim tanığı olarak kullanın.
- **Kimlik:** `vambery-1878`

### Karşılaştırmalı veri setleri

<a id="turkbv"></a>
#### ILCAA Turkic Basic Vocabulary (Tokyo Yabancı Diller Üniversitesi)

<https://turkbv.aa-ken.jp/>

Türk dillerinde temel söz varlığı listeleri, konuşur ses kayıtlarıyla. Aynı merkezin Moğolca karşılığı mongolicbv.aa-ken.jp; Moğolca ödünçleri ayırmak için yan yana kullanılabilir.

**Nasıl kullanılır:** Web arayüzünde kavram ya da dil seçilir. Kaynak portalı: online-resources.aa-ken.jp.

- **Diller:** bütün diller
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama, Örgü: benzerlik ve anlaşılırlık değerleri, Ses denklikleri
- **Erişim:** açık · **Biçim:** web · **Güven:** yüksek · **Durum:** aramada görüldü · **Ortam:** izinsiz (turkbv.aa-ken.jp)
- **Not:** Hangi dilleri kapsadığı ortama eklenip denetlenmeli (Japonca aramada bulundu).
- **Kimlik:** `turkbv`

<a id="wold-halac"></a>
#### Lexical copies in Khalaj — World Loanword Database (WOLD) katkısı

<https://openaccess.artvin.edu.tr/items/35435f9c-bcac-49af-9f4b-2066ad6a5cb9>

Halaççadaki ödünç kelimeler (Farsça, Azerbaycan Türkçesi…).

**Nasıl kullanılır:** Halaçça biçimlerinin miras mı ödünç mü olduğunu denetlemek için.

- **Diller:** Halaçça
- **İşe yaradığı yer:** Ödünç ve miras ayrımı (özellikle Çuvaşça), Yaşayan dillerde biçim toplama
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** aramada görüldü · **Ortam:** izinsiz (openaccess.artvin.edu.tr)
- **Kimlik:** `wold-halac`

<a id="northeuralex"></a>
#### NorthEuraLex

<https://lexibank.clld.org/contributions/northeuralex>

107 Kuzey Avrasya dilinde 1.016 kavram, IPA ile. Türk dillerinin bir kısmı dahil. Dellert vd. 2020, Language Resources and Evaluation 54.

**Nasıl kullanılır:** CLDF; Lexibank üzerinden indirilir.

- **Diller:** Türkiye Türkçesi, Azerbaycan Türkçesi, Kazakça, Özbekçe, Tatarca, Başkurtça, Çuvaşça, Sahaca (Yakutça), Hakasça, Kırgızca
- **İşe yaradığı yer:** Örgü: benzerlik ve anlaşılırlık değerleri, Toplu, makinece okunabilir veri, Yaşayan dillerde biçim toplama
- **Erişim:** açık · **Biçim:** csv · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: lexibank katkı sayfası açıldı (HTTP 200).
- **Not:** Kapsanan Türk dillerinin tam listesi doğrulanmadı.
- **Kimlik:** `northeuralex`

<a id="ronatas-bati-eski-turkce"></a>
#### Róna-Tas & Berta — West Old Turkic (Macarcadaki Türkçe ödünçler) veri seti

<https://github.com/LoanpyDataHub/ronataswestoldturkic>

Macarcaya Batı Eski Türkçeden (Oğur) geçmiş kelimeler. Oğur kolunun tarihî kanıtı olarak Hedef 2'ye ek tanık sağlar.

**Nasıl kullanılır:** Makinece okunabilir veri seti (CLDF). Ham dosyalar: https://raw.githubusercontent.com/LoanpyDataHub/ronataswestoldturkic/main/ (GitHub HTML sayfaları bu ortamda 403). Basılı eser: Róna-Tas & Berta 2011, West Old Turkic: Turkic Loanwords in Hungarian (Harrassowitz). Daha eski temel eser: Gombocz 1912, Die bulgarisch-türkischen Lehnwörter in der ungarischen Sprache.

- **Diller:** Çuvaşça, Volga Bulgarcası
- **İşe yaradığı yer:** Tarihî tanık biçimleri, Ödünç ve miras ayrımı (özellikle Çuvaşça), Ana Türkçe kuruluşu ve etimoloji
- **Erişim:** açık · **Biçim:** csv · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: README raw üzerinden okundu (HTTP 200).
- **Not:** Kitap ve önceki çalışmalar altaica'da: Róna-Tas & Berta 2011 Part II https://altaica.ru/LIBRARY/runic/R%C3%B3na-Tas,%20Berta_West%20Old%20Turkic.%20Turkic%20Loanwords%20in%20Hungarian.%20Part%20II_2011.pdf ; Németh 1965 ve Berta & Róna-Tas 2002 aynı dizinde; Erdal'ın eleştirisi: https://altaica.ru/LIBRARY/runic/Erdal_Review%20of%20R%C3%B3na-Tas,%20Berta,%20West%20Old%20Turkic.pdf
- **Kimlik:** `ronatas-bati-eski-turkce`

<a id="savelyev-turkic"></a>
#### Savelyev & Robbeets — Turkic Basic Vocabularies (lexibank/savelyevturkic)

<https://github.com/lexibank/savelyevturkic>

32 Türk dilinde 254 temel kavram (Leipzig-Jakarta + Jena 200). Her kelimenin akrabalık sınıfı ses denkliklerine göre belirlenmiş; açık ödünçler ayıklanmış. Savelyev & Robbeets 2020, Journal of Language Evolution 5(1).

**Nasıl kullanılır:** CLDF biçimi (cldf/forms.csv, cognates.csv, languages.csv). Bu ortamdan GitHub HTML sayfaları 403 verir; dosyaları ham adresten çek: https://raw.githubusercontent.com/lexibank/savelyevturkic/master/cldf/forms.csv. Zenodo sürümleri v1.0–v2.1. Örgüyü (ag.yaml) veriden hesaplamak ve kök yaşını denetlemek için birebir.

- **Diller:** bütün diller
- **İşe yaradığı yer:** Örgü: benzerlik ve anlaşılırlık değerleri, Toplu, makinece okunabilir veri, Yaşayan dillerde biçim toplama, Ana Türkçe kuruluşu ve etimoloji, Ödünç ve miras ayrımı (özellikle Çuvaşça)
- **Erişim:** açık · **Biçim:** csv · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: raw.githubusercontent.com üzerinden master dalı okundu (HTTP 200); 'main' dalı yok (404).
- **Not:** Biçimlerin her biri kendi kaynağına bağlı (sources.bib); 32 dilin listesi languages.csv'de.
- **Kimlik:** `savelyev-turkic`

<a id="asjp"></a>
#### ASJP Database (Automated Similarity Judgment Program)

<https://asjp.clld.org>

Dünyanın dilleri için 40 kavramlık kararlı kelime listeleri (sürüm 21, 2025); birçok Türk çeşidi (ör. OLD_TURKIC, QASHQAI_2).

**Nasıl kullanılır:** Dil sayfaları asjp.clld.org/languages/<AD>; toplu veri lexibank/asjp.

- **Diller:** bütün diller
- **İşe yaradığı yer:** Örgü: benzerlik ve anlaşılırlık değerleri, Toplu, makinece okunabilir veri
- **Erişim:** açık · **Biçim:** csv · **Güven:** orta · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: açıldı (HTTP 200). Dil sayfaları ör. asjp.clld.org/languages/QASHQAI_2, OLD_TURKIC, ILI_TURKI.
- **Kimlik:** `asjp`

<a id="apertium"></a>
#### Apertium — Türk dilleri çeviri çiftleri ve sözlükleri

<https://github.com/apertium>

Açık lisanslı tek dilli biçimbirim sözlükleri ve iki dilli sözlükler (.dix), ör. apertium-kaz-kir, apertium-kaz-tat.

**Nasıl kullanılır:** Depolardaki .dix dosyaları XML olarak okunur.

- **Diller:** Kazakça, Kırgızca, Tatarca, Başkurtça, Çuvaşça, Sahaca (Yakutça), Tuvaca, Kırım Tatarcası, Kumukça, Karakalpakça, Nogayca, Özbekçe, Uygurca, Türkiye Türkçesi, Azerbaycan Türkçesi, Türkmence
- **İşe yaradığı yer:** Toplu, makinece okunabilir veri, Yaşayan dillerde biçim toplama
- **Erişim:** açık · **Biçim:** git · **Güven:** orta · **Durum:** aramada görüldü · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: github.com HTML sayfası 403 (oturumun GitHub kapsamı). Depolardaki .dix dosyaları raw.githubusercontent.com/apertium/<depo>/master/ üzerinden okunabilir.
- **Not:** Liste örnektir; hangi çiftlerin bulunduğu depolardan doğrulanmalı.
- **Kimlik:** `apertium`

<a id="elegant-lexicon"></a>
#### Elegant Lexicon — Turkic database (C. A. Straughn)

<https://turkic.elegantlexicon.com>

~30.000 kayıtlık karşılaştırmalı Türk sözlüğü; 575 çekirdek kavram (uzun Swadesh listesi, Doerfer'in listeleri). İran'daki küçük Oğuz çeşitleri (Sonkor vb.) dahil.

**Nasıl kullanılır:** Biçim sayfaları ör. lxforms.php?lx=snq (dil kodu). Wiktionary'de kaynak olarak kullanılıyor.

- **Diller:** bütün diller, Kaşkayca, Azerbaycan Türkçesi, Horasan Türkçesi, Halaçça
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama, Toplu, makinece okunabilir veri
- **Erişim:** açık · **Biçim:** web · **Güven:** orta · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: açıldı (HTTP 200).
- **Kimlik:** `elegant-lexicon`

<a id="robbeets-2021"></a>
#### Robbeets vd. 2021 — Triangulation (Transeurasian) veri seti

<https://clics.clld.org/languages/1687>

Nature 2021 makalesinin temel söz varlığı verisi (CLDF; CLICS'te). Türk dillerinin eski biçimlerini Moğol, Tunguz, Kore ve Japon dilleriyle karşılaştırır.

**Nasıl kullanılır:** Ana Türkçe ötesine gitmek için değil, bir kökün Moğolca ile paylaşılıp paylaşılmadığını görmek için (ödünç şüphesi).

- **Diller:** bütün diller
- **İşe yaradığı yer:** Ana Türkçe kuruluşu ve etimoloji, Toplu, makinece okunabilir veri
- **Erişim:** açık · **Biçim:** csv · **Güven:** orta · **Durum:** aramada görüldü · **Ortam:** izinsiz (clics.clld.org)
- **Not:** Transeurasian (Altay) akrabalığı tartışmalıdır; Hedef 2 için kanıt sayılmaz.
- **Kimlik:** `robbeets-2021`

<a id="kaikki"></a>
#### kaikki.org — Wiktionary'nin makinece okunabilir hâli (wiktextract)

<https://kaikki.org/dictionary/rawdata.html>

İngilizce Wiktionary'nin bütün maddeleri JSON Lines biçiminde; dil bazında indirilebilir dosyalar.

**Nasıl kullanılır:** Tek tek sayfa çekmek yerine ilgili dillerin dosyası bir kez indirilip yerelde aranır. Wikimedia hız sınırı sorununu çözer.

- **Diller:** bütün diller
- **İşe yaradığı yer:** Toplu, makinece okunabilir veri, Yaşayan dillerde biçim toplama, Ana Türkçe kuruluşu ve etimoloji
- **Erişim:** açık · **Biçim:** json · **Güven:** orta · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: indirme sayfası açıldı (HTTP 200).
- **Not:** Türk dilleri kapsamı (2026-11): Türkçe, Azerbaycanca, Türkmence, Gagavuzca, Kazakça, Kırgızca, Tatarca, Başkurtça, Kırım Tatarcası, Karaçay-Malkarca, Kumukça, Nogayca, Karakalpakça, Özbekçe, Uygurca, Sahaca, Tuvaca, Hakasça, Altayca, Çuvaşça ve ayrıca Ana Türkçe, Eski Türkçe, Çağatayca. Küçük dillerin dosyaları birkaç yüz maddelik olabilir. Aynı veri wiktextract (PyPI) ile kendi dökümünden de üretilebilir.
- **Kimlik:** `kaikki`

<a id="tatar-sozluk-veri"></a>
#### neurotatarlar/tt-dictionaries — Tatarca sözlükler veri seti

<https://huggingface.co/datasets/neurotatarlar/tt-dictionaries>

Tatarca sözlüklerin makinece okunabilir dökümü (Hugging Face).

**Nasıl kullanılır:** README'de kaynak sözlükler ve lisans; dosyalar doğrudan indirilir.

- **Diller:** Tatarca
- **İşe yaradığı yer:** Toplu, makinece okunabilir veri, Yaşayan dillerde biçim toplama
- **Erişim:** açık · **Biçim:** json · **Güven:** orta · **Durum:** aramada görüldü · **Ortam:** izinsiz (huggingface.co)
- **Not:** huggingface.co bu ortamda izinli değil.
- **Kimlik:** `tatar-sozluk-veri`

<a id="panlex"></a>
#### PanLex

<https://dev.panlex.org/>

~9.000 dil çeşidinde 20 milyon sözcük birimi ve 1,1 milyar çeviri çifti.

**Nasıl kullanılır:** HTTP API ve aylık CSV/JSON/XML anlık görüntüler.

- **Diller:** bütün diller
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama, Toplu, makinece okunabilir veri
- **Erişim:** açık · **Biçim:** api · **Güven:** düşük · **Durum:** aramada görüldü · **Ortam:** izinsiz (dev.panlex.org)
- **Not:** Kaynakları karışık kalitede; tek başına kanıt sayılmamalı.
- **Kimlik:** `panlex`

### Kavram listeleri

<a id="concepticon"></a>
#### Concepticon — kavram listeleri veritabanı

<https://concepticon.clld.org>

Swadesh 100/207, Leipzig-Jakarta, ASJP, Savelyev-2020-254 gibi kavram listeleri ve ortak kavram kimlikleri.

**Nasıl kullanılır:** SIRA.md'deki kavramları ortak kimliklere bağlamak için; Zenodo'da indirilebilir sürümler.

- **Diller:** bütün diller
- **İşe yaradığı yer:** Sıklık listeleri ve kavram listeleri, Toplu, makinece okunabilir veri
- **Erişim:** açık · **Biçim:** csv · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: açıldı (HTTP 200, sürüm 3.4.1).
- **Kimlik:** `concepticon`

<a id="klaproth"></a>
#### Klaproth — Asia Polyglotta (1823) ve Uygur dili ve yazısı üzerine (1812/1820)

<https://archive.org/details/asiapolyglotta00klap>

Asya dillerinin kelime listeleri: Çuvaşça, Sahaca, Tofaca (Karagas), Hakas ağızları dahil. 1820 baskısında Uygurca kelime listesi var. Abel-Rémusat'ın Recherches sur les langues tartares (1820) de aynı dönemin Fransız çalışması.

**Nasıl kullanılır:** Uygurca: https://archive.org/details/bub_gb_jz9JAAAAcAAJ ; Rémusat: https://archive.org/details/bub_gb_tc4GAAAAQAAJ

- **Diller:** bütün diller
- **İşe yaradığı yer:** Tarihî tanık biçimleri, Ağız verisi
- **Erişim:** açık · **Biçim:** pdf · **Güven:** orta · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: üç archive.org kaydı açıldı (HTTP 200/206).
- **Kimlik:** `klaproth`

<a id="pallas-1787"></a>
#### Pallas — Linguarum totius orbis vocabularia comparativa (1786-89)

<https://archive.org/details/bub_gb_mPBLAAAAcAAJ>

II. Katerina'nın emriyle 200'ü aşkın dilde 285 kavramlık karşılaştırmalı liste (Kiril harfli). Pek çok Türk dili ve ağzının 18. yy'daki biçimini verir; temel kavramlar listemizle büyük ölçüde örtüşür.

**Nasıl kullanılır:** archive.org (1. cilt). Rusça baskı altaica'da: https://altaica.ru/LIBRARY/turks/%D0%9F%D0%B0%D0%BB%D0%BB%D0%B0%D1%81_%D0%A1%D1%80%D0%B0%D0%B2%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D0%B8%20%D0%B2%D1%81%D0%B5%D1%85%20%D1%8F%D0%B7%D1%8B%D0%BA%D0%BE%D0%B2%20%D0%B8%20%D0%BD%D0%B0%D1%80%D0%B5%D1%87%D0%B8%D0%B9_I%201787.pdf

- **Diller:** bütün diller
- **İşe yaradığı yer:** Tarihî tanık biçimleri, Ağız verisi, Sıklık listeleri ve kavram listeleri
- **Erişim:** açık · **Biçim:** pdf · **Güven:** orta · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: archive.org kaydı; altaica PDF'i açıldı (HTTP 200/206).
- **Kimlik:** `pallas-1787`

<a id="strahlenberg-witsen"></a>
#### Strahlenberg 1730 ve Witsen 1692 — Sibirya kelime listeleri (Almanca, Felemenkçe)

<https://archive.org/details/11064853bsb>

Poltava'da esir düşen İsveçli subay Strahlenberg'in 'Tabula polyglotta'sı ve Amsterdam belediye başkanı Witsen'in 'Noord en Oost Tartarye'si: Sibirya Türk dillerinin bilinen ilk kelime kayıtları.

**Nasıl kullanılır:** Strahlenberg archive.org (Almanca 1730); Witsen basılı ve Hollanda dijital kütüphanelerinde.

- **Diller:** Sahaca (Yakutça), Hakasça, Çuvaşça, Tatarca, Başkurtça, Sibirya Tatarcası
- **İşe yaradığı yer:** Tarihî tanık biçimleri, Ağız verisi
- **Erişim:** açık · **Biçim:** pdf · **Güven:** orta · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: Strahlenberg archive.org kaydı açıldı (HTTP 200/206).
- **Not:** Witsen archive.org'da bulunamadı; yazım Almanca ve Felemenkçe kulağına göre.
- **Kimlik:** `strahlenberg-witsen`

<a id="wiktionary-swadesh"></a>
#### Wiktionary — Türk dilleri Swadesh listeleri

<https://en.wiktionary.org/wiki/Appendix:Turkic_Swadesh_lists>

Ana Türkçe ve 25 dil için (Türkiye, Azerbaycan, Türkmen, Kumuk, Karaçay-Malkar, Kırım Tatar, Tatar, Sibirya Tatar, Başkurt, Kazak, Karakalpak, Nogay, Kırgız, Güney/Kuzey Altay, Şor, Eski Türkçe, Özbek, Uygur, Karahanlıca, Tuva, Hakas, Saha, Çuvaş) Swadesh listesi.

**Nasıl kullanılır:** Sayfa otomatik şablonla üretiliyor; tablo HTML'den okunur.

- **Diller:** bütün diller
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama, Sıklık listeleri ve kavram listeleri
- **Erişim:** açık · **Biçim:** web · **Güven:** orta · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: açıldı (HTTP 200, ~1 MB tek sayfa).
- **Kimlik:** `wiktionary-swadesh`

### Tarihî metinler ve sözlükler

<a id="turfan-bbaw"></a>
#### BBAW Turfan Araştırmaları — Eski Uygurca metinler ve sayısal arşiv

<https://turfan.bbaw.de/projekt-en.html>

Berlin-Brandenburg Bilimler Akademisi'nin Turfan koleksiyonu: Eski Uygurca el yazmalarının sayısal görüntüleri ve yayınları (IDP Berlin).

**Nasıl kullanılır:** Metin tanığını görmek için; kelime arama için Wilkens sözlüğü daha uygun.

- **Diller:** Eski Türkçe (Göktürk ve Uygur metinleri)
- **İşe yaradığı yer:** Tarihî tanık biçimleri
- **Erişim:** açık · **Biçim:** web · **Güven:** yüksek · **Durum:** aramada görüldü · **Ortam:** izinsiz (turfan.bbaw.de)
- **Not:** Almanca aramada bulundu.
- **Kimlik:** `turfan-bbaw`

<a id="bizans-kaynaklari"></a>
#### Bizans kaynaklarında Türkçe (Moravcsik, Byzantinoturcica II; Macartney 1944)

<
https://altaica.ru/LIBRARY/runic/Macartney_On%20the%20Greek%20Sources%20for%20the%20History%20of%20the%20Turks%20in%20the%20Sixth%20Century_1944.pdf>

Rumca kaynaklarda Hun, Bulgar, Hazar, Peçenek, Kuman ve Göktürk adları, unvanları ve kelimeleri. Moravcsik'in 2. cildi bunların tam dizinidir.

**Nasıl kullanılır:** Moravcsik 1958 (Berlin; De Gruyter yeniden basım) basılı ya da e-kitap.

- **Diller:** Eski Türkçe (Göktürk ve Uygur metinleri), Volga Bulgarcası, Kuman-Kıpçakça (Codex Cumanicus, Memlük Kıpçakçası)
- **İşe yaradığı yer:** Tarihî tanık biçimleri
- **Erişim:** kısmen · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: Macartney PDF'i açıldı (HTTP 200/206).
- **Kimlik:** `bizans-kaynaklari`

<a id="boeschoten"></a>
#### Boeschoten — A Dictionary of Early Middle Turkic (Brill 2022)

<https://www.degruyterbrill.com/document/isbn/9789004525191/html>

14. yüzyıl Doğu Türkçesi (geç Karahanlı, Harezm, Altın Orda, Memlük Kıpçakçası) söz varlığı.

**Nasıl kullanılır:** Ücretli; Akvius Çağatayca sözlüğü bu veriye dayanıyor.

- **Diller:** Harezm Türkçesi ve Çağatayca, Kuman-Kıpçakça (Codex Cumanicus, Memlük Kıpçakçası), Karahanlıca (Dîvânu Lugâti't-Türk, Kutadgu Bilig)
- **İşe yaradığı yer:** Tarihî tanık biçimleri
- **Erişim:** ücretli · **Biçim:** web · **Güven:** yüksek · **Durum:** aramada görüldü · **Ortam:** izinsiz (www.degruyterbrill.com)
- **Kimlik:** `boeschoten`

<a id="yabanci-yazili-eski-turkce"></a>
#### Brahmi, Tibet, Soğd ve Phags-pa harfli Eski Türkçe

<
https://altaica.ru/LIBRARY/runic/Zieme_Turkic%20Fragments%20in%20%27Phags-pa%20Script_1998.pdf>

Uygur harfinin göstermediği ünlü ayrımlarını (o/u, ö/ü, e/ä, uzun ünlüler) gösteren yabancı yazılı metinler. Ana Türkçe ünlülerini kurmakta ve Eski Türkçe okunuşu sınamakta kullanılır.

**Nasıl kullanılır:** Maue 1996 ve 2015, Alttürkische Handschriften: Dokumente in Brāhmī und tibetischer Schrift (VOHD, basılı); Soğd harfli Eski Türkçe: https://altaica.ru/LIBRARY/runic/Fedak%C3%A2r_Das%20Altt%C3%BCrkische%20in%20sogdischer%20Schrift%20%28%D0%B4%D1%80%D1%83%D0%B3%D0%B0%D1%8F%20%D1%81%D1%8A%D1%91%D0%BC%D0%BA%D0%B0%29.pdf ; Uygurcadaki Sanskritçe ödünçler: https://altaica.ru/LIBRARY/runic/Moerloose_Sanskrit%20Loan%20Words%20in%20Uighur.pdf

- **Diller:** Eski Türkçe (Göktürk ve Uygur metinleri)
- **İşe yaradığı yer:** Tarihî tanık biçimleri, Ses denklikleri, Ana Türkçe kuruluşu ve etimoloji
- **Erişim:** kısmen · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: üç altaica PDF'i açıldı (HTTP 200/206).
- **Not:** Maue ciltleri basılı (Steiner).
- **Kimlik:** `yabanci-yazili-eski-turkce`

<a id="bulgat-durre"></a>
#### Bulġatü'l-Müştâk ve ed-Dürretü'l-Mudiyye (Zajączkowski 1958-1969, Fransızca)

<
https://altaica.ru/LIBRARY/runic/Zaj%C4%85czkowski_Vocabulaire%20Arabe-Kiptchak,%20Bul%C4%A1at%20al-mu%E1%B9%A1t%C4%81q%20fi%20lu%C4%A1at%20at-turk%20wa-l-qif%C7%AF%C4%81q_1958.pdf>

İki Memlük Kıpçakçası sözlüğünün Lehçe-Fransızca baskıları (14.-15. yy).

**Nasıl kullanılır:** Dürre için: https://altaica.ru/LIBRARY/runic/Zaj%C4%85czkowski_Chapitres%20choisis%20du%20Vocabulaire%20arabe-kiptchak%20%27ad-Durrat%20al-mu%E1%B8%8D%C4%AB%E2%80%99a%20f%C4%AB-l-lu%C4%A1at%20at-turk%C4%ABya%27.%201_1965.pdf. Bulgat'ın Türkçe incelemesi: https://archive.org/details/kitabu-bulgatul-mustak-fi-lugatit-turk-wel-kifcak-uzerine-dil-incelemesi

- **Diller:** Kuman-Kıpçakça (Codex Cumanicus, Memlük Kıpçakçası)
- **İşe yaradığı yer:** Tarihî tanık biçimleri
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: altaica.ru'daki iki PDF; archive.org kaydı açıldı (HTTP 200/206).
- **Kimlik:** `bulgat-durre`

<a id="castren-bohtlingk"></a>
#### Castrén 1857 (Koybal ve Karagas) ve Böhtlingk 1851 (Sahaca) — ilk bilimsel tanımlar

<https://archive.org/details/malexandercastr01castgoog>

Finli Castrén'in Koybal (Hakas ağzı) ve Karagas (Tofaca) sözlükçesi; Böhtlingk'in Almanca Sahaca dilbilgisi ve sözlüğü.

**Nasıl kullanılır:** Böhtlingk: https://altaica.ru/LIBRARY/Bohtlingk_I.pdf ve https://altaica.ru/LIBRARY/Bohtlingk_II.pdf

- **Diller:** Hakasça, Tofaca, Sahaca (Yakutça)
- **İşe yaradığı yer:** Tarihî tanık biçimleri, Ağız verisi, Ses denklikleri
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: Castrén archive.org kaydı; Böhtlingk PDF'leri açıldı (HTTP 200/206).
- **Kimlik:** `castren-bohtlingk`

<a id="codex-cumanicus"></a>
#### Codex Cumanicus (çevrim içi baskılar)

<https://opendata.uni-halle.de/handle/1981185920/102379>

Kuman-Kıpçakça tanığı. Halle baskısı (kamu malı, PDF); Kuun 1880 baskısı (archive.org/details/codexcumanicusbi00kuunuoft) ve Ligeti'nin girişi (Hungaricana). Sözlük olarak Grønbech'in Kuman Lehçesi Sözlüğü (gronbech-kuman) daha kullanışlı.

**Nasıl kullanılır:** PDF'lerde kelime arama; Türkçe baskı (Argunşah & Güner) basılı.

- **Diller:** Kuman-Kıpçakça (Codex Cumanicus, Memlük Kıpçakçası)
- **İşe yaradığı yer:** Tarihî tanık biçimleri
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** aramada görüldü · **Ortam:** izinsiz (opendata.uni-halle.de)
- **Doğrulama:** 2026-11-12: Kuun 1880 baskısı archive.org'da açıldı (HTTP 200). Halle adresi bu ortamda izinli değil.
- **Kimlik:** `codex-cumanicus`

<a id="kitab-idrak"></a>
#### Ebû Hayyân — Kitâbü'l-İdrâk li-Lisâni'l-Etrâk (1312-13)

<https://archive.org/details/kitbalidrkllisnaltrk>

Kahire'de Arapça yazılmış Kıpçakça sözlük ve dilbilgisi; yer yer Türkmence (Oğuzca) farkları not eder.

**Nasıl kullanılır:** archive.org'da Arapça İstanbul baskısı. Türkçe çevirili baskı: Caferoğlu 1931 (basılı).

- **Diller:** Kuman-Kıpçakça (Codex Cumanicus, Memlük Kıpçakçası)
- **İşe yaradığı yer:** Tarihî tanık biçimleri, Dilbilgisi (Aşama 3)
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: archive.org kaydı açıldı (HTTP 200/206).
- **Kimlik:** `kitab-idrak`

<a id="erdal-volga-bulgar"></a>
#### Erdal 1993 — Die Sprache der wolgabolgarischen Inschriften

<https://openlibrary.org/search?q=wolgabolgarischen+Inschriften>

Volga Bulgarcası mezar taşı yazıtlarının dili; Oğur kolunun tarihî tanığı.

**Nasıl kullanılır:** Basılı; Wiktionary maddelerinde atıf yapılıyor.

- **Diller:** Volga Bulgarcası
- **İşe yaradığı yer:** Tarihî tanık biçimleri, Ödünç ve miras ayrımı (özellikle Çuvaşça)
- **Erişim:** basılı · **Biçim:** basili · **Güven:** yüksek · **Durum:** basılı · **Ortam:** —
- **Kimlik:** `erdal-volga-bulgar`

<a id="ermeni-kipcak"></a>
#### Ermeni harfli Kıpçakça (Garkavets 2010; Tryjarski 1968-72)

<
https://altaica.ru/LIBRARY/runic/%D0%93%D0%B0%D1%80%D0%BA%D0%B0%D0%B2%D0%B5%D1%86_%D0%9A%D1%8B%D0%BF%D1%87%D0%B0%D0%BA%D1%81%D0%BA%D0%BE%D0%B5%20%D0%BF%D0%B8%D1%81%D1%8C%D0%BC%D0%B5%D0%BD%D0%BD%D0%BE%D0%B5%20%D0%BD%D0%B0%D1%81%D0%BB%D0%B5%D0%B4%D0%B8%D0%B5.%20%D0%A2.%20III.%20%D0%9A%D1%8B%D0%BF%D1%87%D0%B0%D0%BA%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C%20%28%D0%B0%D1%80%D0%BC%D1%8F%D0%BD%D0%BE-%D0%BA%D1%8B%D0%BF%D1%87%D0%B0%D0%BA%D1%81%D0%BA%D0%B8%D0%B9%29_2010.pdf>

16.-17. yy'da Lviv ve Kamenets Ermenilerinin yazdığı Kıpçakça (dua, hukuk, kronik). Ermeni harfi ünlüleri açıkça gösterir.

**Nasıl kullanılır:** Garkavets'in Kıpçakça sözlüğü (Rusça): https://altaica.ru/LIBRARY/runic/%D0%93%D0%B0%D1%80%D0%BA%D0%B0%D0%B2%D0%B5%D1%86_%D0%9A%D1%8B%D0%BF%D1%87%D0%B0%D0%BA%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C.pdf ; Tryjarski, Dictionnaire arméno-kiptchak (Varşova, basılı).

- **Diller:** Kuman-Kıpçakça (Codex Cumanicus, Memlük Kıpçakçası)
- **İşe yaradığı yer:** Tarihî tanık biçimleri, Ses denklikleri
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: iki altaica PDF'i açıldı (HTTP 200/206).
- **Kimlik:** `ermeni-kipcak`

<a id="gaochang-yiyu"></a>
#### Gaochang Guan Yiyu / Zazi — Ming dönemi Uygurca-Çince sözlük (15.-16. yy)

<
https://altaica.ru/LIBRARY/runic/Hu%20Zhenhua,%20Huang%20Runhua%20%28eds.%29_Gaochang%20guan%20zazi%20%28%E9%AB%98%E6%98%8C%E9%A4%A8%E6%9D%82%E5%AD%97%29%20%28%D0%BD%D0%B0%20%D0%BA%D0%B8%D1%82%D0%B0%D0%B9%D1%81%D0%BA%D0%BE%D0%BC%29.pdf>

Ming sarayının çevirmen bürosunun Uygurca-Çince kelime listesi (Hua-yi yiyu dizisi). Her Türkçe kelimenin Çince karakterle okunuşu verilir; Eski Uygurca ile Çağatayca arasındaki dönemin tanığı.

**Nasıl kullanılır:** Hu & Huang 1984 (Çince). Ligeti'nin Fransızca ek sözlüğü: https://altaica.ru/LIBRARY/runic/Ligeti_Glossaire%20suppl%C3%A9mentaire%20au%20vocabulaire%20sino-ouigour%20du%20Bureau%20des%20traducteurs.%202_1969.pdf ; dizinin Moğolca kısmı için Kuribayashi 2003 dizini: https://altaica.ru/mong_monuments/Kuribayashi_Word-%20and%20Suffix-Index%20to%20Hua-yi%20Yi-yu%202003_OCR.pdf

- **Diller:** Eski Türkçe (Göktürk ve Uygur metinleri), Harezm Türkçesi ve Çağatayca
- **İşe yaradığı yer:** Tarihî tanık biçimleri, Ses denklikleri
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: üç altaica PDF'i açıldı (HTTP 200/206).
- **Kimlik:** `gaochang-yiyu`

<a id="gronbech-kuman"></a>
#### Grønbech — Kuman Lehçesi Sözlüğü (Codex Cumanicus sözlüğü, Türkçe çeviri)

<https://archive.org/details/k.-gronbech-kuman-lehcesi-sozlugu-codex-cumani-cus>

Codex Cumanicus'taki bütün Kumanca kelimelerin alfabetik sözlüğü (Grønbech 1942, Komanisches Wörterbuch; Türkçesi Kemal Aytaç, TDK 1992). Her kelimenin metindeki yazımları ve anlamı.

**Nasıl kullanılır:** archive.org taramasında madde başına göre ara. qwm tanığı için ilk bakılacak yer.

- **Diller:** Kuman-Kıpçakça (Codex Cumanicus, Memlük Kıpçakçası)
- **İşe yaradığı yer:** Tarihî tanık biçimleri, Yaşayan dillerde biçim toplama
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: archive.org kaydı açıldı (HTTP 200).
- **Kimlik:** `gronbech-kuman`

<a id="gottingen-altuygur"></a>
#### Göttingen Bilimler Akademisi — Altuigurisches Wörterbuch projesi

<
https://adw.d.sub.uni-goettingen.de/fileadmin/forschungsprojekte/altuigurisches_woerterbuch/dokumente/Gesamtbibliographie_JPL.pdf>

Büyük Eski Uygurca sözlük projesi (Wilkens, Ünal vd.). Bağlantı projenin Eski Uygurca genel kaynakçası; proje sayfasında yayınlar (ör. Ünal 2026) listelenir.

**Nasıl kullanılır:** Kaynakça PDF'i bir Eski Uygurca metnin yayınını bulmak için.

- **Diller:** Eski Türkçe (Göktürk ve Uygur metinleri)
- **İşe yaradığı yer:** Tarihî tanık biçimleri, Ana Türkçe kuruluşu ve etimoloji, Makaleler ve bibliyografya
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** aramada görüldü · **Ortam:** izinsiz (adw.d.sub.uni-goettingen.de)
- **Not:** Röhrborn'un Uigurisches Wörterbuch I-VI (1977-98) cildi altaica'da: https://altaica.ru/LIBRARY/turks/R%D3%A7hrborn_Uigurisches%20W%D3%A7rterbuch_I-VI%201977-1998.pdf (HTTP 206, 2026-11-12).
- **Kimlik:** `gottingen-altuygur`

<a id="hazarca"></a>
#### Hazarca kalıntıları (Golden 1980 Khazar Studies; İbranice yazışma)

<https://search.worldcat.org/search?q=Golden+Khazar+Studies>

İbranice, Arapça ve Rumca kaynaklarda geçen Hazar unvanları ve kelimeleri; Batı Eski Türkçe (Ogur) için seyrek tanık.

**Nasıl kullanılır:** Basılı (Budapeşte 1980).

- **Diller:** Volga Bulgarcası
- **İşe yaradığı yer:** Tarihî tanık biçimleri
- **Erişim:** basılı · **Biçim:** basili · **Güven:** yüksek · **Durum:** basılı · **Ortam:** —
- **Kimlik:** `hazarca`

<a id="hotanca-turkce"></a>
#### Hotanca kaynaklarda Türkçe (Bailey 1939-55, Emmerick & Róna-Tas 1992, Hovdhaugen 1971)

<https://altaica.ru/LIBRARY/runic/Bailey_A%20Turkish-Khotanese%20Vocabulary_1944.pdf>

10. yy'dan Brahmi harfiyle yazılmış Türkçe-Hotanca kelime listesi (bilinen en eski iki dilli Türkçe sözlüklerden). Brahmi yazısı ünlüleri ve ünlü uzunluğunu gösterdiği için ses tarihine değerli.

**Nasıl kullanılır:** Emmerick & Róna-Tas düzeltmesi: https://altaica.ru/LIBRARY/runic/Emmerick,%20R%C3%B3na-Tas_The%20Turkish-Khotanese%20Wordlist%20Revisited_1992.pdf ; Hovdhaugen: https://altaica.ru/LIBRARY/runic/Hovdhaugen_Turkish%20Words%20in%20Khotanese%20Texts.%20A%20Linguistic%20Analysis_1971.pdf ; Bailey, Turks in Khotanese texts: https://altaica.ru/LIBRARY/runic/Bailey_Turks%20in%20Khotanese%20Texts_1939.pdf

- **Diller:** Eski Türkçe (Göktürk ve Uygur metinleri)
- **İşe yaradığı yer:** Tarihî tanık biçimleri, Ses denklikleri
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: dört altaica PDF'i açıldı (HTTP 200/206).
- **Kimlik:** `hotanca-turkce`

<a id="houtsma-leiden"></a>
#### Houtsma 1894 — Ein türkisch-arabisches Glossar (Leiden yazması, 1245)

<https://archive.org/details/eintrkischarab00houtuoft>

Memlük Mısır'ında 1245'te yazılmış Arapça açıklamalı Türkçe sözlük; Kıpçakça ağırlıklı, Oğuzca biçimler de var. Elyazmasının Moğolca bölümü de var. En eski Kıpçak kayıtlarından biri.

**Nasıl kullanılır:** Almanca baskı, madde başları Arap harfli Türkçe ve Latin harfli okunuş. Aynı PDF altaica.ru'da: https://altaica.ru/LIBRARY/runic/Houtsma_Ein%20t%C3%BCrkisch-arabisches%20Glossar%20nach%20der%20Leidener%20Handschrift_1894.pdf. Moğolca kısmı için Poppe, Das mongolische Sprachmaterial einer Leidener Handschrift: https://altaica.ru/LIBRARY/POPPE/poppeleiden.pdf

- **Diller:** Kuman-Kıpçakça (Codex Cumanicus, Memlük Kıpçakçası)
- **İşe yaradığı yer:** Tarihî tanık biçimleri, Ödünç ve miras ayrımı (özellikle Çuvaşça)
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: archive.org kaydı; altaica.ru PDF'i; Poppe PDF'i açıldı (HTTP 200/206).
- **Kimlik:** `houtsma-leiden`

<a id="kohd-eski-uygurca"></a>
#### KOHD — Almanya'daki Eski Uygurca el yazmaları kataloğu

<
https://orient-kohd.dl.uni-leipzig.de/content/SpecFeatures_KOHD_OldUygur_ENG_20200120.pdf>

Katalogisierung der Orientalischen Handschriften in Deutschland: Eski Uygurca metin parçalarının ayrıntılı katalogları (VOHD serisi).

**Nasıl kullanılır:** Leipzig Üniversitesi veritabanı; metin parçasının yayın bilgisini bulmak için.

- **Diller:** Eski Türkçe (Göktürk ve Uygur metinleri)
- **İşe yaradığı yer:** Tarihî tanık biçimleri, Makaleler ve bibliyografya
- **Erişim:** açık · **Biçim:** web · **Güven:** yüksek · **Durum:** aramada görüldü · **Ortam:** izinsiz (orient-kohd.dl.uni-leipzig.de)
- **Kimlik:** `kohd-eski-uygurca`

<a id="karayca-eski-kayitlar"></a>
#### Karayca eski kayıtlar (Kowalski 1929 Trakay metinleri; KRPS 1974)

<https://archive.org/details/kpbc.umk.pl.Magazyn_316_11_244557>

Trakay ağzı metinleri ve Karayca-Lehçe sözlükçe; Karayca-Rusça-Lehçe sözlük (1974) üç ağzı ayırır.

**Nasıl kullanılır:** Kowalski archive.org (Lehçe-Almanca). KRPS basılı.

- **Diller:** Karayca
- **İşe yaradığı yer:** Tarihî tanık biçimleri, Ağız verisi
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: archive.org kaydı açıldı (HTTP 200/206).
- **Kimlik:** `karayca-eski-kayitlar`

<a id="dlt"></a>
#### Kâşgarlı Mahmud — Dîvânu Lugâti't-Türk (Ercilasun & Akkoyunlu 2014, TDK)

<https://archive.org/details/divan-1939>

11. yüzyıl; Karahanlıca tanığı. Oğuz, Kıpçak ve diğer boyların biçimlerini ayrı ayrı kaydeder (ör. Türk boylarında män, Oğuzlarda bän).

**Nasıl kullanılır:** Atalay'ın 1939-43 çevirisi archive.org'da; dizin cildi: https://altaica.ru/LIBRARY/runic/Atalay%20%28%C3%A7ev.%29_Divan%C3%BC%20L%C3%BCgat-it-T%C3%BCrk%20terc%C3%BCmesi.%20IV%20%28Endeks%29.pdf ; tıpkıbasım 1. cilt: https://altaica.ru/LIBRARY/runic/Ka%C5%9Fgarl%C4%B1%20Mahmud_Kit%C3%A2b-%C4%B1%20D%C3%AEv%C3%A2n-%C4%B1%20L%C3%BCgati%27t-T%C3%BCrk.%20Cilt%201%20%28%D1%84%D0%B0%D0%BA%D1%81%D0%B8%D0%BC%D0%B8%D0%BB%D0%B5%29.pdf ; İngilizce (Dankoff & Kelly): https://altaica.ru/LIBRARY/turks/Dankoff_Mahmud_1.pdf ; Rusça: https://altaica.ru/LIBRARY/turks/Mahmud_ru.pdf ; Kazakça: https://altaica.ru/LIBRARY/turks/Mahmud_kz1.pdf ; Türkçe dizin: https://altaica.ru/LIBRARY/turks/Mahmud_turkish_index.pdf. Ercilasun & Akkoyunlu 2014 (TDK) basılıdır.

- **Diller:** Karahanlıca (Dîvânu Lugâti't-Türk, Kutadgu Bilig)
- **İşe yaradığı yer:** Tarihî tanık biçimleri, Ağız verisi
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: Atalay archive.org kaydı; altaica'daki dizin, tıpkıbasım, İngilizce, Rusça, Kazakça ve Türkçe dizin PDF'leri açıldı (HTTP 200/206).
- **Kimlik:** `dlt`

<a id="meninski-transkripsiyon"></a>
#### Meninski 1680 ve Latin harfli Osmanlıca (Megiser 1612, Molino 1641)

<https://archive.org/details/bub_gb_7MBIAAAAcAAJ>

Meninski'nin Thesaurus'u 17. yy Osmanlıcasını Latin harfiyle ve okunuşuyla verir. Megiser ve Molino gibi 'transkripsiyonlu metinler' Arap harfinin göstermediği ünlüleri gösterir.

**Nasıl kullanılır:** archive.org (Viyana 1680). Molino ve diğer İtalyanca-Türkçe sözlükler üzerine: Kurtböke, Euralex 1994 (euralex.org); derlem çalışmaları DergiPark'ta 'transkripsiyonlu metinler' aramasıyla.

- **Diller:** Türkiye Türkçesi, Eski Anadolu Türkçesi
- **İşe yaradığı yer:** Tarihî tanık biçimleri, Ses denklikleri
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: archive.org kaydı açıldı (HTTP 200/206).
- **Kimlik:** `meninski-transkripsiyon`

<a id="senglah"></a>
#### Mirza Mehdi Han — Senglâh (1759-60; Clauson 1960 tıpkıbasım)

<https://search.worldcat.org/search?q=Sanglax+Clauson>

Farsça yazılmış en büyük Çağatayca sözlük; Clauson EDPT'de sık kullanır.

**Nasıl kullanılır:** Basılı (Gibb Memorial Series). Kütüphane kataloğundan.

- **Diller:** Harezm Türkçesi ve Çağatayca
- **İşe yaradığı yer:** Tarihî tanık biçimleri
- **Erişim:** basılı · **Biçim:** basili · **Güven:** yüksek · **Durum:** basılı · **Ortam:** —
- **Kimlik:** `senglah`

<a id="mogolistan-yazitlari"></a>
#### Moğolistan'daki Türk yazıtları (Battulga 2005; Moriyasu & Ochir 1999, Japonca-Moğolca)

<https://altaica.ru/LIBRARY/turks/Battulga_runic_inscriptions_in_Mongolia_2005.pdf>

Moğolistan'daki küçük runik yazıtların Moğolca yayını; Japon-Moğol ortak ekibinin 1996-98 saha raporu (Şine Usu, Sevrey vb.).

**Nasıl kullanılır:** Battulga PDF (Moğolca). Moriyasu & Ochir raporu Osaka Üniversitesi deposunda (ir.library.osaka-u.ac.jp, Mongol1-3.pdf).

- **Diller:** Eski Türkçe (Göktürk ve Uygur metinleri)
- **İşe yaradığı yer:** Tarihî tanık biçimleri
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: Battulga PDF'i açıldı (HTTP 200/206).
- **Not:** Osaka deposu bu ortamda izinli değil.
- **Kimlik:** `mogolistan-yazitlari`

<a id="gizli-tarih"></a>
#### Moğolların Gizli Tarihi (13. yy) dizinleri (Kuribayashi 2009, Haenisch 1939)

<
https://altaica.ru/SECRET/Kuribayashi_Word-Index%20to%20the%20SHM%20with%20Chinese%20Transcriptions%20and%20Glosses%202009_OCR.pdf>

Orta Moğolcanın ana metni. İçindeki Türkçe ödünçler, bir kelimenin 13. yy'da Moğolcaya geçmiş olduğunu (yani Türkçede daha eski olduğunu) gösterir.

**Nasıl kullanılır:** Haenisch sözlüğü: https://altaica.ru/LIBRARY/mong/Haenish%20GG%20worterbuch%201939.pdf ; Uygur-Moğol harfli anıtlar: https://altaica.ru/LIBRARY/Tumurtogoo_uighur2006.pdf

- **Diller:** bütün diller
- **İşe yaradığı yer:** Ödünç ve miras ayrımı (özellikle Çuvaşça), Tarihî tanık biçimleri
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: üç altaica PDF'i açıldı (HTTP 200/206).
- **Kimlik:** `gizli-tarih`

<a id="najip-xiv"></a>
#### Nadjip 1979 — XIV. yüzyıl Türk dillerinin tarihî-karşılaştırmalı sözlüğü (Rusça)

<
https://altaica.ru/LIBRARY/runic/%D0%9D%D0%B0%D0%B4%D0%B6%D0%B8%D0%BF_%D0%98%D1%81%D1%82%D0%BE%D1%80%D0%B8%D0%BA%D0%BE-%D1%81%D1%80%D0%B0%D0%B2%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C%20%D1%82%D1%8E%D1%80%D0%BA%D1%81%D0%BA%D0%B8%D1%85%20%D1%8F%D0%B7%D1%8B%D0%BA%D0%BE%D0%B2%20XIV%20%D0%B2%D0%B5%D0%BA%D0%B0.%20%D0%A2.%201_1979.djvu>

Altın Orda edebî dili (Kutb'un Hüsrev ü Şirin'i) üzerine kurulu; maddelerde Kıpçak ve Harezm biçimleri karşılaştırılır.

**Nasıl kullanılır:** DJVU (Rusça). Madde başları Arap harfinden Latin çeviriyazı.

- **Diller:** Kuman-Kıpçakça (Codex Cumanicus, Memlük Kıpçakçası), Harezm Türkçesi ve Çağatayca
- **İşe yaradığı yer:** Tarihî tanık biçimleri
- **Erişim:** açık · **Biçim:** djvu · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: altaica.ru DJVU'su açıldı (HTTP 200/206).
- **Kimlik:** `najip-xiv`

<a id="pelliot-marco-polo"></a>
#### Pelliot — Notes on Marco Polo (1959-73)

<https://archive.org/details/notesonmarcopolo0000paul>

Batı ve Doğu kaynaklarında geçen Türkçe ve Moğolca kelimelerin, adların uzun tartışmaları.

**Nasıl kullanılır:** archive.org ödünç kütüphanesi (oturum gerekir).

- **Diller:** bütün diller
- **İşe yaradığı yer:** Tarihî tanık biçimleri, Ödünç ve miras ayrımı (özellikle Çuvaşça)
- **Erişim:** kısmen · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: archive.org kaydı açıldı (HTTP 200/206).
- **Kimlik:** `pelliot-marco-polo`

<a id="rasulid-hexaglot"></a>
#### Rasûlî Altı Dilli Sözlük — The King's Dictionary (Golden 2000)

<
https://altaica.ru/LIBRARY/runic/Golden%20%28ed.%29_The%20King%27s%20Dictionary.%20The%20Ras%C5%ABlid%20Hexaglot%20%28%D1%84%D0%B0%D0%BA%D1%81%D0%B8%D0%BC%D0%B8%D0%BB%D0%B5%29_2000.pdf>

14. yy Yemen'inde Arapça-Farsça-Türkçe-Rumca-Ermenice-Moğolca kelime listeleri. Türkçe ile Moğolca karşılık yan yana: ödünç sınaması için.

**Nasıl kullanılır:** PDF tıpkıbasım ve İngilizce çeviri (Brill). Benzer çok dilli bir Memlük sözlüğü (İstanbul nüshası) altaica Arab/STAMBUL.RAR olarak duruyor.

- **Diller:** Kuman-Kıpçakça (Codex Cumanicus, Memlük Kıpçakçası), Eski Anadolu Türkçesi
- **İşe yaradığı yer:** Tarihî tanık biçimleri, Ödünç ve miras ayrımı (özellikle Çuvaşça)
- **Erişim:** kısmen · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: altaica.ru PDF'i açıldı (HTTP 200/206).
- **Kimlik:** `rasulid-hexaglot`

<a id="toparli-kipcak"></a>
#### Toparlı, Vural, Karaatlı — Kıpçak Türkçesi Sözlüğü (TDK 2007)

<
https://altaica.ru/LIBRARY/runic/Toparl%C4%B1,%20Vural,%20Karaatl%C4%B1_K%C4%B1p%C3%A7ak%20T%C3%BCrk%C3%A7esi%20S%C3%B6zl%C3%BC%C4%9F%C3%BC_2007.pdf>

Memlük Kıpçakçası kaynaklarının (İdrâk, Tuhfe, Bulgat, Kavânîn, Houtsma vb.) birleşik sözlüğü; her biçimin hangi eserde geçtiği gösterilir.

**Nasıl kullanılır:** qwm tanığı için önce buraya bakın, sonra kaynak esere inin. Aynı dosya altaica LIBRARY/turks altında da var.

- **Diller:** Kuman-Kıpçakça (Codex Cumanicus, Memlük Kıpçakçası)
- **İşe yaradığı yer:** Tarihî tanık biçimleri
- **Erişim:** kısmen · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: altaica.ru PDF'i açıldı (HTTP 200/206).
- **Not:** Basılı TDK yayını; altaica kopyasının telif durumu belirsiz, atıfta TDK baskısını gösterin.
- **Kimlik:** `toparli-kipcak`

<a id="turfan-ilk-yayinlar"></a>
#### Turfan metinlerinin ilk yayınları (Müller, Uigurica 1908-31; Bang & Gabain, TTT ve dizini)

<https://archive.org/details/Muller_uigurica>

Berlin Turfan derlemesinin ilk metin yayınları; Eski Uygurca kelimelerin ilk tanıkları.

**Nasıl kullanılır:** Bang & Gabain'in dizini (1931): https://altaica.ru/LIBRARY/runic/Bang,%20Gabain_Analytischer%20Index%20zu%20den%20f%C3%BCnf%20ersten%20St%C3%BCcken%20der%20T%C3%BCrkischen%20Turfan-Texte_1931.pdf

- **Diller:** Eski Türkçe (Göktürk ve Uygur metinleri)
- **İşe yaradığı yer:** Tarihî tanık biçimleri
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: archive.org kaydı; dizin PDF'i açıldı (HTTP 200/206).
- **Kimlik:** `turfan-ilk-yayinlar`

<a id="bedayi-lugat"></a>
#### Tâli' İmânî Herevî — Bedâyi'ü'l-Lugat (Borovkov 1961, tıpkıbasım ve Rusça)

<
https://altaica.ru/LIBRARY/runic/%D0%91%D0%BE%D1%80%D0%BE%D0%B2%D0%BA%D0%BE%D0%B2_%D0%91%D0%B0%D0%B4%C4%81%E2%80%99%D0%B8%E2%80%98%20%D0%B0%D0%BB-%D0%BB%D1%83%D2%93%D0%B0%D1%82.%20%D0%A1%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C%20%D0%A2%C4%81%D0%BB%D0%B8%E2%80%98%20%D0%98%D0%BC%C4%81%D0%BD%D0%B8%20%D0%93%D0%B5%D1%80%D0%B0%D1%82%D1%81%D0%BA%D0%BE%D0%B3%D0%BE%20%D0%BA%20%D1%81%D0%BE%D1%87%D0%B8%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F%D0%BC%20%D0%90%D0%BB%D0%B8%D1%88%D0%B5%D1%80%D0%B0%20%D0%9D%D0%B0%D0%B2%D0%BE%D0%B8_1961.pdf>

Nevayi'nin eserleri için Farsça açıklamalı Çağatayca sözlük.

**Nasıl kullanılır:** PDF; madde başları Arap harfli, Borovkov'un çeviriyazısı ve Rusça açıklama.

- **Diller:** Harezm Türkçesi ve Çağatayca
- **İşe yaradığı yer:** Tarihî tanık biçimleri
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: altaica.ru PDF'i açıldı (HTTP 200/206).
- **Kimlik:** `bedayi-lugat`

<a id="wilkens-eski-uygurca"></a>
#### Wilkens — Handwörterbuch des Altuigurischen (2021)

<https://directory.doabooks.org/handle/20.500.12854/72556>

Eski Uygurca metinlerin bütün söz varlığı; Almanca-Türkçe açıklamalı.

**Nasıl kullanılır:** Göttingen Üniversitesi Yayınevi, açık erişim PDF. Kayıt: DOAB; dosya: library.oapen.org/handle/20.500.12657/51341.

- **Diller:** Eski Türkçe (Göktürk ve Uygur metinleri)
- **İşe yaradığı yer:** Tarihî tanık biçimleri, Ana Türkçe kuruluşu ve etimoloji
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** aramada görüldü · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: DOAB ve OAPEN hız sınırı veriyor (HTTP 429). Aralıklı denenmeli; arama motorunda kayıt görüldü.
- **Kimlik:** `wilkens-eski-uygurca`

<a id="bes-dilli-ayna"></a>
#### Wuti Qingwen Jian — Beş Dilli Ayna (18. yy; Mançu-Tibet-Moğol-Çağatay-Çince)

<https://en.wikipedia.org/wiki/Pentaglot_Dictionary>

Qing sarayının 18.000 civarı kavramlık beş dilli sözlüğü. Çağatayca karşılıkların okunuşu Mançu harfiyle de yazılmıştır; aynı kavramın Moğolca karşılığı da yanında.

**Nasıl kullanılır:** Japonca dizinli baskı: Tamura vd. 1966-68 (Kyoto); Almanca: Fünfsprachenspiegel (Harrassowitz 2013). Basılı.

- **Diller:** Harezm Türkçesi ve Çağatayca, Uygurca
- **İşe yaradığı yer:** Tarihî tanık biçimleri, Ödünç ve miras ayrımı (özellikle Çuvaşça)
- **Erişim:** basılı · **Biçim:** basili · **Güven:** yüksek · **Durum:** aramada görüldü · **Ortam:** —
- **Doğrulama:** 2026-11-12: Wikipedia maddesi aramada görüldü; sayısal baskı bulunamadı.
- **Kimlik:** `bes-dilli-ayna`

<a id="mukaddimet-edeb"></a>
#### Zemahşerî — Mukaddimetü'l-Edeb (1137; Harezm Türkçesi ve Moğolca aralık çevirileri)

<https://altaica.ru/LIBRARY/POPPE/poppe_mukad.pdf>

Arapça sözlüğün sonraki elyazmalarına Harezm Türkçesi, Çağatayca ve Moğolca karşılıklar eklenmiş. Aynı kavramın Türkçe ve Moğolca karşılığını yan yana görmek Moğolca ödünçleri ayırmaya yarar.

**Nasıl kullanılır:** Poppe 1938 Moğolca sözlüğü (Rusça, PDF). Türkçe Harezm nüshası: Yüce 1993 (basılı). Bir elyazması: https://archive.org/details/McGillLibrary-rbsc_blackerwood_folioMSBWIvanow0218-16919

- **Diller:** Harezm Türkçesi ve Çağatayca
- **İşe yaradığı yer:** Tarihî tanık biçimleri, Ödünç ve miras ayrımı (özellikle Çuvaşça)
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: Poppe PDF'i; McGill elyazması kaydı açıldı (HTTP 200/206).
- **Kimlik:** `mukaddimet-edeb`

<a id="tuhfe-zekiyye"></a>
#### et-Tuhfetü'z-Zekiyye fi'l-Lügati't-Türkiyye (14. yy; Atalay 1945, TDK)

<
https://archive.org/details/et-tuhfetuz-zekiyyefil-lugatit-turkiyyeuzerinebirdilincelemesi>

Memlük Kıpçakçasının Arapça açıklamalı sözlüğü ve dilbilgisi.

**Nasıl kullanılır:** archive.org'daki dil incelemesi (Türkçe) sözlük dizinini içerir.

- **Diller:** Kuman-Kıpçakça (Codex Cumanicus, Memlük Kıpçakçası)
- **İşe yaradığı yer:** Tarihî tanık biçimleri
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: archive.org kaydı açıldı (HTTP 200/206).
- **Kimlik:** `tuhfe-zekiyye`

<a id="cin-transkripsiyonlari"></a>
#### Çin kaynaklarındaki Eski Türkçe kelimeler (Ligeti 1950, Kasai, Vovin & McCraw)

<
https://altaica.ru/LIBRARY/runic/Kasai_Die%20altt%C3%BCrkischen%20W%C3%B6rter%20der%20Natur%20und%20Gesellschaft%20in%20chinesischen%20Quellen%20%286.%20und%208.%20Jh.%29.pdf>

6.-8. yy Çin yıllıklarında Çince karakterlerle yazılmış Türkçe kelimeler. Göktürk yazıtlarından daha eski olabilen tanıklar; Erken Orta Çince okunuşuyla birlikte değerlendirilir.

**Nasıl kullanılır:** Ligeti, Mots de civilisation de Haute Asie en transcription chinoise: https://altaica.ru/LIBRARY/runic/Ligeti_Mots%20de%20civilisation%20de%20Haute%20Asie%20en%20transcription%20chinoise_1950.pdf ; Vovin & McCraw, akrabalık adları: https://altaica.ru/LIBRARY/runic/Vovin,%20McCraw_Old%20Turkic%20Kinship%20Terms%20in%20Early%20Middle%20Chinese.pdf ; Çin yıllıklarının Almanca çevirisi (Liu Mau-tsai 1958): https://altaica.ru/LIBRARY/runic/Liu%20Mau-tsai_Die%20chinesischen%20Nachrichten%20zur%20Geschichte%20der%20Ost-T%C3%BCrken%20%28T%27u-k%C3%BCe%29.pdf ; özgün metin: Zhou Shu 50 ve Sui Shu 84 (zh.wikisource.org).

- **Diller:** Eski Türkçe (Göktürk ve Uygur metinleri)
- **İşe yaradığı yer:** Tarihî tanık biçimleri, Ana Türkçe kuruluşu ve etimoloji, Ses denklikleri
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: dört altaica PDF'i açıldı (HTTP 200/206).
- **Not:** Çince transkripsiyonun yorumu tartışmalıdır; tek başına kök kanıtı sayılmaz, yazıt biçimiyle birlikte kullanın.
- **Kimlik:** `cin-transkripsiyonlari`

<a id="ibn-muhenna"></a>
#### İbn Mühennâ Lügati (13.-14. yy; Battal 1934, TDK)

<
https://altaica.ru/LIBRARY/runic/Battal_%C4%B0bn%C3%BC-M%C3%BChenn%C3%A2%20L%C3%BBgati_1934.pdf>

İlhanlı çevresinde yazılmış Arapça-Farsça-Türkçe-Moğolca sözlük. Türkçe bölümde 'Türkmen' (Oğuz) ve 'Türkistan Türkleri' biçimlerini ayrı ayrı verir; ağız ayrımı için değerli.

**Nasıl kullanılır:** Battal'ın Türkçe baskısı (PDF). Başka bir tarama: https://archive.org/details/Bn-MhennLgati

- **Diller:** Kuman-Kıpçakça (Codex Cumanicus, Memlük Kıpçakçası), Harezm Türkçesi ve Çağatayca
- **İşe yaradığı yer:** Tarihî tanık biçimleri, Ağız verisi
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: altaica.ru PDF'i; archive.org kaydı açıldı (HTTP 200/206).
- **Kimlik:** `ibn-muhenna`

<a id="dts"></a>
#### Древнетюркский словарь (1969)

<https://altaica.ru/LIBRARY/turks/dts.pdf>

Eski Türkçe ve Eski Uygurca sözlüğü (Nadelyaev vd., 676 s.).

**Nasıl kullanılır:** Altaica'da 80 MB PDF (1969 baskısı). Wiktionary'de DTS diye atıf yapılır.

- **Diller:** Eski Türkçe (Göktürk ve Uygur metinleri), Karahanlıca (Dîvânu Lugâti't-Türk, Kutadgu Bilig)
- **İşe yaradığı yer:** Tarihî tanık biçimleri
- **Erişim:** kısmen · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: altaica PDF'i açıldı (HTTP 200/206).
- **Kimlik:** `dts`

<a id="abuska"></a>
#### Abuşka — Çağatayca-Osmanlıca sözlük (16. yy; Vámbéry 1862, Atalay 1970)

<
https://altaica.ru/LIBRARY/runic/V%C3%A1mb%C3%A9ry_Abu%C5%A1ka.%20%C4%8Cagataisch-osmanisches%20W%C3%B6rterbuch_1862.pdf>

Ali Şir Nevayi'nin dilini Osmanlı okuruna açıklayan sözlük.

**Nasıl kullanılır:** Vámbéry'nin Almanca baskısı (PDF). Türkçe baskı (Atalay): https://archive.org/details/AbukaLgati

- **Diller:** Harezm Türkçesi ve Çağatayca
- **İşe yaradığı yer:** Tarihî tanık biçimleri
- **Erişim:** açık · **Biçim:** pdf · **Güven:** orta · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: altaica.ru PDF'i; archive.org kaydı açıldı (HTTP 200/206).
- **Kimlik:** `abuska`

<a id="akvius-cagatayca"></a>
#### Akvius — çevrim içi Çağatayca sözlük

<https://akvius-website.pages.dev/categories/languages/chaghatay/posts/chagatai-dictionary.html>

Boeschoten'in sözlüğüne dayanan, geliştirme aşamasındaki Çağatayca arama.

**Nasıl kullanılır:** Web arama. Ayrıca Şeyh Süleyman'ın Lügat-ı Çağatay transkripsiyonu YÖK Açık Bilim'de.

- **Diller:** Harezm Türkçesi ve Çağatayca
- **İşe yaradığı yer:** Tarihî tanık biçimleri
- **Erişim:** açık · **Biçim:** web · **Güven:** orta · **Durum:** aramada görüldü · **Ortam:** izinsiz (akvius-website.pages.dev)
- **Kimlik:** `akvius-cagatayca`

<a id="arap-fars-cografyacilar"></a>
#### Arapça ve Farsça coğrafya eserleri (Hudûdü'l-Âlem 982; Minorsky 1937)

<https://archive.org/details/in.ernet.dli.2015.281514>

Türk boylarının yurtları, adları ve bazı kelimeleri (Oğuz, Karluk, Kimek, Bulgar). İbn Fadlan'ın Volga seyahatnamesi de aynı türden.

**Nasıl kullanılır:** archive.org (İngilizce çeviri ve açıklamalar).

- **Diller:** Eski Türkçe (Göktürk ve Uygur metinleri), Volga Bulgarcası
- **İşe yaradığı yer:** Tarihî tanık biçimleri
- **Erişim:** açık · **Biçim:** pdf · **Güven:** orta · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: archive.org kaydı açıldı (HTTP 200/206).
- **Kimlik:** `arap-fars-cografyacilar`

<a id="cagatay-batili-sozlukler"></a>
#### Avrupa'da basılan Çağatayca sözlükler (Vámbéry 1867, Pavet de Courteille 1870, Kúnos 1902)

<https://archive.org/details/dictionnairetur00courgoog>

Pavet de Courteille'in Fransızca Dictionnaire turk-oriental'i, Vámbéry'nin Čagataische Sprachstudien'i ve Şeyh Süleyman Efendi'nin Lügat-i Çağatay'ının Kúnos tarafından Almancaya kısaltılmış baskısı.

**Nasıl kullanılır:** Vámbéry: https://archive.org/details/10522453bsb ; Kúnos: https://archive.org/details/ejxsulejmanefen00effogoog ; aynı eserler altaica LIBRARY/turks altında da var.

- **Diller:** Harezm Türkçesi ve Çağatayca
- **İşe yaradığı yer:** Tarihî tanık biçimleri
- **Erişim:** açık · **Biçim:** pdf · **Güven:** orta · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: üç archive.org kaydı; altaica kopyaları açıldı (HTTP 200/206).
- **Not:** 19. yy yayınları; okunuşlar zaman zaman Osmanlıcaya göre düzeltilmiş, dikkatli kullanın.
- **Kimlik:** `cagatay-batili-sozlukler`

<a id="bahsayis"></a>
#### Bahşayiş Lügati — Eski Oğuzca Sözlük (Turan)

<
https://altaica.ru/LIBRARY/runic/Turan_Bah%C5%9Fayi%C5%9F%20l%C3%BCgati.%20Eski%20O%C4%9Fuzca%20s%C3%B6zl%C3%BCk.pdf>

Eski Anadolu Türkçesi (Eski Oğuzca) metinlerinden derlenmiş sözlük.

**Nasıl kullanılır:** PDF (Türkçe).

- **Diller:** Eski Anadolu Türkçesi
- **İşe yaradığı yer:** Tarihî tanık biçimleri
- **Erişim:** açık · **Biçim:** pdf · **Güven:** orta · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: altaica.ru PDF'i açıldı (HTTP 200/206).
- **Kimlik:** `bahsayis`

<a id="cagatay-izahli"></a>
#### Chaghatay tilining izahliq lughiti (Uygurca açıklamalı Çağatayca sözlük)

<https://altaica.ru/LIBRARY/runic/Chaghatay%20tilining%20izahliq%20lughiti.%201.pdf>

Doğu Türkistan'da hazırlanmış, Uygurca açıklamalı Çağatayca sözlük.

**Nasıl kullanılır:** PDF, Arap harfli Uygurca.

- **Diller:** Harezm Türkçesi ve Çağatayca, Uygurca
- **İşe yaradığı yer:** Tarihî tanık biçimleri
- **Erişim:** açık · **Biçim:** pdf · **Güven:** orta · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: altaica.ru PDF'i açıldı (HTTP 200/206).
- **Kimlik:** `cagatay-izahli`

<a id="karamanlica"></a>
#### Karamanlıca — Rum harfli Türkçe (Salaville & Dalleggio, Anatoli gazetesi)

<https://iris.unive.it/bitstream/10278/5060883/1/EGLL%20Karamanlidika.pdf>

18.-20. yy'da Rum harfiyle basılmış Türkçe kitaplar ve gazeteler; ünlüleri ve konuşma dilini gösterir.

**Nasıl kullanılır:** Kappler'in ansiklopedi maddesi (PDF); kaynakça Salaville & Dalleggio (Fransızca). Anatoli gazetesinin 1888-94 sayıları Halle Üniversitesi deposunda; SALT Araştırma'da kitaplar.

- **Diller:** Türkiye Türkçesi, Eski Anadolu Türkçesi
- **İşe yaradığı yer:** Tarihî tanık biçimleri, Ses denklikleri
- **Erişim:** açık · **Biçim:** pdf · **Güven:** orta · **Durum:** aramada görüldü · **Ortam:** izinsiz (iris.unive.it)
- **Doğrulama:** 2026-11-12: aramada görüldü; sunucular bu ortamda izinli değil.
- **Kimlik:** `karamanlica`

<a id="tibet-kaynaklari"></a>
#### Tibetçe kaynaklarda Türkler (OTDO, Pelliot tibétain 1283)

<https://otdo.aa-ken.jp>

Eski Tibetçe belgelerde Dru-gu (Türk), Hor (Uygur) ve Karluk adları, unvanlar. 8. yy'da beş Uygur elçisinin kuzey kavimlerini anlatan raporu (PT 1283) Türk boy adlarını verir.

**Nasıl kullanılır:** OTDO (Tokyo Yabancı Dil. Üniv.) KWIC araması. Moriyasu 1980: https://altaica.ru/LIBRARY/runic/Moriyasu_La%20nouvelle%20interpr%C3%A9tation%20des%20mots%20Hor%20et%20Ho-yo-hor%20dans%20le%20manuscrit%20Pelliot%20tib%C3%A9tain%201283%20%28AOH%2034%29_1980.pdf ; Hoffmann 1950, Karluklar: https://altaica.ru/LIBRARY/runic/Hoffmann_Die%20Qarluq%20in%20der%20tibetischen%20Literatur_1950.pdf

- **Diller:** Eski Türkçe (Göktürk ve Uygur metinleri)
- **İşe yaradığı yer:** Tarihî tanık biçimleri
- **Erişim:** açık · **Biçim:** web · **Güven:** orta · **Durum:** aramada görüldü · **Ortam:** izinsiz (otdo.aa-ken.jp)
- **Doğrulama:** 2026-11-12: otdo.aa-ken.jp bu ortamda izinli değil; iki makale altaica.ru'dan açıldı (HTTP 206).
- **Kimlik:** `tibet-kaynaklari`

<a id="turik-bitig"></a>
#### Türik Bitig — Eski Türkçe yazıtlar ve metinler portalı

<https://bitig.kz/?lang=e>

300 metin (54 Orhon, 106 Yenisey, 15 Talas yazıtı, 38 Turfan el yazması), 2.353 kelimelik Eski Türkçe-Kazakça sözlük.

**Nasıl kullanılır:** Metin, çeviri ve sözlük arama.

- **Diller:** Eski Türkçe (Göktürk ve Uygur metinleri)
- **İşe yaradığı yer:** Tarihî tanık biçimleri
- **Erişim:** açık · **Biçim:** web · **Güven:** orta · **Durum:** aramada görüldü · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: bitig.kz izinli olduğu hâlde bağlantı yanıt vermedi (zaman aşımı). Eski adres bitig.org (ISAW AWOL dizininde arşivli).
- **Kimlik:** `turik-bitig`

<a id="eski-turkce-yerel-sozlukler"></a>
#### Türk ülkelerinde yayımlanmış Eski Türkçe sözlükler (Azerbaycan 1992, Uygur 1989)

<
https://altaica.ru/LIBRARY/runic/Q%C9%99dim%20t%C3%BCrk%20abid%C9%99l%C9%99rinin%20s%C3%B6zl%C3%BCy%C3%BC_1992.pdf>

Azerbaycanca açıklamalı runik yazıtlar sözlüğü ve Uygurca 'Qedimki Uyghur tili lughiti'.

**Nasıl kullanılır:** Uygurca: https://altaica.ru/LIBRARY/runic/Qedimki%20uy%C4%A1ur%20tili%20lu%C4%A1iti_1989.pdf ; Bayat & Alieva, Eski Türkçe sözlük: https://altaica.ru/LIBRARY/runic/Bayat,%20Alieva_Eski%20T%C3%BCrk%C3%A7e%20s%C3%B6zl%C3%BCk.pdf

- **Diller:** Eski Türkçe (Göktürk ve Uygur metinleri)
- **İşe yaradığı yer:** Tarihî tanık biçimleri
- **Erişim:** açık · **Biçim:** pdf · **Güven:** orta · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: üç altaica PDF'i açıldı (HTTP 200/206).
- **Kimlik:** `eski-turkce-yerel-sozlukler`

<a id="suryani-yazitlar"></a>
#### Yedisu'daki Süryani harfli Nesturi mezar taşları (Chwolson 1890)

<https://archive.org/details/chwolson_syrisch_nestorianische_grabinschriften>

13.-14. yy Hristiyan Türklerin Süryani harfli Türkçe mezar yazıtları ve takvim adları.

**Nasıl kullanılır:** archive.org (Almanca).

- **Diller:** Karahanlıca (Dîvânu Lugâti't-Türk, Kutadgu Bilig)
- **İşe yaradığı yer:** Tarihî tanık biçimleri
- **Erişim:** açık · **Biçim:** pdf · **Güven:** orta · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: archive.org kaydı açıldı (HTTP 200/206).
- **Kimlik:** `suryani-yazitlar`

### Dil sözlükleri

<a id="osmanlica-batili-sozlukler"></a>
#### 19. yy Osmanlıca sözlükleri (Kieffer & Bianchi 1835, Zenker 1866-76, Redhouse 1890)

<https://archive.org/details/redhouse-a-turkish-and-english-lexicon-1890>

Her kelimenin Türkçe, Arapça ya da Farsça olduğunu işaretleyen büyük sözlükler; 'Ele' ilkesinde Türkiye Türkçesinin ödünçlerini ayıklamak için.

**Nasıl kullanılır:** Zenker: https://archive.org/details/bub_gb_6wxFAAAAYAAJ ; Kieffer & Bianchi: https://archive.org/details/bub_gb_2gAUAAAAYAAJ

- **Diller:** Türkiye Türkçesi
- **İşe yaradığı yer:** Ödünç ve miras ayrımı (özellikle Çuvaşça), Tarihî tanık biçimleri
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: üç archive.org kaydı açıldı (HTTP 200/206).
- **Kimlik:** `osmanlica-batili-sozlukler`

<a id="arapca-farsca-sozlukler"></a>
#### Arapça ve Farsça kaynak sözlükler (Lane, Steingass) — ödünç sınaması

<https://archive.org/details/an-arabic-english-lexicon>

Bir Türkçe kelimenin Arapça ya da Farsça kökenli olup olmadığını denetlemek için ('Ele' ilkesi).

**Nasıl kullanılır:** Steingass: https://archive.org/details/comprehensiveper0000stei_d9o9 (ödünç kütüphanesi). Farsçadaki Türkçe ve Moğolca kelimeler için Doerfer TMEN.

- **Diller:** bütün diller
- **İşe yaradığı yer:** Ödünç ve miras ayrımı (özellikle Çuvaşça)
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: iki archive.org kaydı açıldı (HTTP 200/206).
- **Kimlik:** `arapca-farsca-sozlukler`

<a id="azerbaycan-kaynaklari"></a>
#### Azerbaycanca kaynaklar (Azərbaycan dilinin izahlı lüğəti, dilcilik.az)

<https://dilcilik.az>

Azərbaycan dilinin izahlı lüğəti (4 cilt, AMEA 2006) ve Azərbaycan dilinin dialektoloji lüğəti (ağız sözlüğü). dilcilik.az dilbilim kitaplığı; sözlük taramaları preslib.az koleksiyonunda.

**Nasıl kullanılır:** Ağız sözlüğü Azerbaycan ağızlarını (Güney, Afşar, Karapapak) doldurmak için.

- **Diller:** Azerbaycan Türkçesi, `aze-iran` (ağız)
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama, Ağız verisi, Makaleler ve bibliyografya
- **Erişim:** kısmen · **Biçim:** pdf · **Güven:** yüksek · **Durum:** aramada görüldü · **Ortam:** izinsiz (dilcilik.az)
- **Kimlik:** `azerbaycan-kaynaklari`

<a id="azerbaycan-diyalekt"></a>
#### Azərbaycan dilinin dialektoloji lüğəti (1999, 2003)

<
https://altaica.ru/LIBRARY/turks/Azerbaycan%20Dialektoloji%20Lugati.%20I%20cild%20A-L,%201999.pdf>

Azerbaycan Türkçesi ağız sözlüğü (iki cilt).

**Nasıl kullanılır:** II. cilt: https://altaica.ru/LIBRARY/turks/Azerbaycan%20Dialektoloji%20Lugati.%20II%20cild%20M-Z,%202003.pdf

- **Diller:** Azerbaycan Türkçesi
- **İşe yaradığı yer:** Ağız verisi
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: iki cilt PDF'i açıldı (HTTP 200/206).
- **Kimlik:** `azerbaycan-diyalekt`

<a id="cuvasca-asmarin"></a>
#### Aşmarin — Thesaurus Linguae Tschuvaschorum (17 cilt)

<https://openlibrary.org/works/OL3026013W>

17 ciltlik (1928–1950) büyük Çuvaşça sözlük, 54.000'den fazla madde; ağız biçimleri ve örnek cümleler dahil.

**Nasıl kullanılır:** Aranabilir PDF altaica'da: https://altaica.ru/LIBRARY/turks/Ashmarin_searchable_dict.pdf . Çuvaşistan Ulusal Kütüphanesi (nbchr.ru) 2014'te kelime dizinini elektronik olarak yayımladı.

- **Diller:** Çuvaşça
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama, Ağız verisi, Ödünç ve miras ayrımı (özellikle Çuvaşça)
- **Erişim:** basılı · **Biçim:** basili · **Güven:** yüksek · **Durum:** basılı · **Ortam:** —
- **Not:** Standart Çuvaşça yenilikçidir; ağız biçimleri Ana Türkçe için daha değerli olabilir. Rusça aramada: Ашмарин, Словарь чувашского языка.
- **Kimlik:** `cuvasca-asmarin`

<a id="halacca"></a>
#### Halaçça — Doerfer, Khalaj Materials (1971) ve Doerfer & Tezcan, Wörterbuch des Chaladsch (1980)

<https://www.routledge.com/Khalaj-Materials/Doerfer/p/book/9780700709151>

Halaççanın temel kaynakları; Talhab ağzından 319 kelimelik liste, Harrab ağzı sözlüğü.

**Nasıl kullanılır:** Doerfer & Tezcan, Wörterbuch des Chaladsch (1980) PDF: https://altaica.ru/LIBRARY/turks/Doerfer,Tezcan_Worterbuch%20des%20Chaladsch%201980.pdf ; Khalaj Materials basılı.

- **Diller:** Halaçça
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama, Ağız verisi, Ana Türkçe kuruluşu ve etimoloji
- **Erişim:** basılı · **Biçim:** basili · **Güven:** yüksek · **Durum:** basılı · **Ortam:** —
- **Doğrulama:** 2026-11-12: Doerfer & Tezcan PDF'i açıldı (HTTP 200/206).
- **Kimlik:** `halacca`

<a id="karay-sozluk"></a>
#### Karayca — Karaim Multi Dictionary (Csató & Nathan) ve KRPS 1974

<https://www.karaim.eu/en/language/researching-the-language/>

Çevrim içi Karayca-Rusça çok dilli sözlük. Basılı Karayca-Rusça-Lehçe Sözlük (1974): 17.400 kelime, üç ağzın tamamı (Trakay, Galiç, Kırım).

**Nasıl kullanılır:** Ağız kodlarını (kdr-trakay, kdr-galic, kdr-kirim) doldurmak için.

- **Diller:** Karayca
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama, Ağız verisi
- **Erişim:** kısmen · **Biçim:** web · **Güven:** yüksek · **Durum:** aramada görüldü · **Ortam:** izinsiz (www.karaim.eu)
- **Kimlik:** `karay-sozluk`

<a id="kaskayca"></a>
#### Kaşkayca — Dolatkhah 2019, Qashqai Turkic (derlem tabanlı dilbilgisi)

<https://glottolog.org/resource/reference/id/570614>

Açıklamalı Kaşkayca metinler ve dilbilgisi; ayrıca Mardani, Qašqayı sözlügü (Şiraz).

**Nasıl kullanılır:** Basılı (LINCOM).

- **Diller:** Kaşkayca
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama, Dilbilgisi (Aşama 3)
- **Erişim:** basılı · **Biçim:** basili · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** —
- **Doğrulama:** 2026-11-12: Glottolog künye sayfası açıldı (HTTP 200).
- **Kimlik:** `kaskayca`

<a id="mogolca-sozlukler"></a>
#### Moğolca sözlükler (Kowalewski 1844-49, Lessing 1960, Bawden, Büyük Akademik Moğolca-Rusça)

<https://altaica.ru/LIBRARY/mong/bamrs_full.pdf>

Bir Türkçe kelimenin Moğolcada da olup olmadığını görmek için. Kowalewski'nin üç dilli (Moğolca-Rusça-Fransızca) sözlüğü klasik yazı dilini, Lessing ve Bawden İngilizce açıklamalı.

**Nasıl kullanılır:** Kowalewski: https://archive.org/details/dictionnairemon00kovagoog ; Lessing: https://altaica.ru/LIBRARY/mong/Lessing.pdf ; Kalmukça: Ramstedt 1935 https://altaica.ru/LIBRARY/ramstedt/Ramstedt_Kalmykisches_Worterbuch.pdf ; tam liste: https://altaica.ru/mongolic_dictionaries.html

- **Diller:** bütün diller
- **İşe yaradığı yer:** Ödünç ve miras ayrımı (özellikle Çuvaşça)
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: BAMRS, Lessing, Ramstedt PDF'leri; Kowalewski archive.org kaydı açıldı (HTTP 200/206).
- **Kimlik:** `mogolca-sozlukler`

<a id="ozbek-izohli"></a>
#### O'zbek tilining izohli lug'ati — Özbekçe açıklamalı sözlük (yeni baskı)

<https://uza.uz/ar/posts/ozbek-tilining-izohli-lugati-taqdimoti-otkazildi_488895>

Özbekçenin açıklamalı sözlüğü (5 cilt 2006–2008; Bilimler Akademisi yeni baskısı tanıtıldı).

**Nasıl kullanılır:** Akademinin yayınlar sayfası academy.uz/en/page/pdf/nashrlar.

- **Diller:** Özbekçe
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama
- **Erişim:** kısmen · **Biçim:** pdf · **Güven:** yüksek · **Durum:** aramada görüldü · **Ortam:** izinsiz (uza.uz)
- **Not:** Özbekçe aramada bulundu.
- **Kimlik:** `ozbek-izohli`

<a id="kazak-15-cilt"></a>
#### Qazaq ädebï tiliniñ sözdigi — Kazak yazı dilinin 15 ciltlik sözlüğü (2011)

<
https://search.worldcat.org/search?q=%D2%9A%D0%B0%D0%B7%D0%B0%D2%9B+%D3%99%D0%B4%D0%B5%D0%B1%D0%B8+%D1%82%D1%96%D0%BB%D1%96%D0%BD%D1%96%D2%A3+%D1%81%D3%A9%D0%B7%D0%B4%D1%96%D0%B3%D1%96>

Kazakçanın en büyük açıklamalı sözlüğü (A. Baytursınulı Dilbilim Enstitüsü). Eskimiş ve bölgesel kelimeler işaretli.

**Nasıl kullanılır:** Çevrim içi sürümü sozdik.kz ve Kazakistan dil portallarında aranabilir.

- **Diller:** Kazakça
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama
- **Erişim:** kısmen · **Biçim:** basili · **Güven:** yüksek · **Durum:** aramada görüldü · **Ortam:** izinsiz (search.worldcat.org)
- **Kimlik:** `kazak-15-cilt`

<a id="radloff"></a>
#### Radloff — Versuch eines Wörterbuches der Türk-Dialecte (1893-1911, 4 cilt)

<https://altaica.ru/LIBRARY/Radlov/Radlov_dicI1.pdf>

19. yy sonunda bütün Türk dillerinden ve ağızlarından derlenmiş dev karşılaştırmalı sözlük (Rusça-Almanca). Her madde hangi dil veya ağızdan geldiğini gösterir; bugün kaybolmuş ağız biçimleri için eşsiz.

**Nasıl kullanılır:** Ciltler altaica'da LIBRARY/Radlov ve LIBRARY/turks altında (Radloff_v3p1.pdf … Radloff_v4p2.pdf). archive.org: https://archive.org/details/opytslovariatiu00radlgoog (cilt 1-3).

- **Diller:** bütün diller
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama, Ağız verisi, Tarihî tanık biçimleri, Toplu, makinece okunabilir veri
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: 1. ve 4. cilt PDF'leri; archive.org kaydı açıldı (HTTP 200/206).
- **Not:** Kiril harfli çeviriyazı Radloff'un kendi sistemiyle; ä, ï, ö, ü ayrımları dikkatle okunmalı.
- **Kimlik:** `radloff`

<a id="sovyet-iki-dilli-sozlukler"></a>
#### Rusça açıklamalı standart sözlükler (Yudahin, Gagavuzca 1973, Karaçay-Malkarca 1989, Hakasça, Sahaca 1972)

<https://altaica.ru/turkic_dictionaries.html>

Altaica'nın 28 Türk diline göre düzenlenmiş sözlük listesi; çoğu PDF olarak iner.

**Nasıl kullanılır:** Yudahin: https://altaica.ru/LIBRARY/yudahin/kyrgyz_dictionary1.pdf ; Gagavuzca: https://altaica.ru/LIBRARY/turks/%D0%93%D0%B0%D0%B3%D0%B0%D1%83%D0%B7%D1%81%D0%BA%D0%BE-%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE-%D0%BC%D0%BE%D0%BB%D0%B4%D0%B0%D0%B2%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C%201973.pdf ; Karaçay-Malkarca: https://altaica.ru/LIBRARY/turks/%D0%9A%D0%B0%D1%80%D0%B0%D1%87%D0%B0%D0%B5%D0%B2%D0%BE-%D0%B1%D0%B0%D0%BB%D0%BA%D0%B0%D1%80%D1%81%D0%BA%D0%BE-%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C%201989.djvu ; Hakasça: https://altaica.ru/LIBRARY/BASKAKOV/xakas_rus.pdf ; Sahaca: https://altaica.ru/LIBRARY/yakut/sleptsov_yakut_russian_dictionary_1972.pdf

- **Diller:** Kırgızca, Gagavuzca, Karaçay-Malkarca, Hakasça, Sahaca (Yakutça), Başkurtça, Kırım Tatarcası, Uygurca, Türkmence
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: liste sayfası ve beş sözlük açıldı (HTTP 200/206).
- **Kimlik:** `sovyet-iki-dilli-sozlukler`

<a id="sibirya-eski-sozlukler"></a>
#### Sibirya ve Altay'ın eski ve küçük dil sözlükleri (Verbitski 1884, Pekarski, Tumaşeva, Rassadin, Lemskaya)

<
https://altaica.ru/LIBRARY/turks/%D0%92%D0%B5%D1%80%D0%B1%D0%B8%D1%86%D0%BA%D0%B8%D0%B9_%D0%A1%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C%20%D0%B0%D0%BB%D1%82%D0%B0%D0%B9%D1%81%D0%BA.%20%D0%B8%20%D0%B0%D0%BB%D0%B0%D0%B4%D0%B0%D0%B3%D1%81%D0%BA%D0%BE%D0%B3%D0%BE%20%D0%BD%D0%B0%D1%80%D0%B5%D1%87%D0%B8%D0%B9%201884.pdf>

Verbitski'nin 1884 Altayca sözlüğü, Pekarski'nin büyük Sahaca sözlüğü, Tumaşeva'nın Sibirya Tatar ağızları sözlüğü (1992), Rassadin'in Tofaca ve Soyotça, Lemskaya'nın Çulımca-İngilizce sözlüğü (2024); Kumandı, Teleüt ve Şor sözlükleri.

**Nasıl kullanılır:** Pekarski: https://altaica.ru/LIBRARY/yakut/pekarsky_big_yakut_russian_dictionary_1959.pdf ; Tumaşeva: https://altaica.ru/LIBRARY/turks/%D0%A2%D1%83%D0%BC%D0%B0%D1%88%D0%B5%D0%B2%D0%B0_%D0%A1%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C%20%D0%B4%D0%B8%D0%B0%D0%BB%D0%B5%D0%BA%D1%82%D0%BE%D0%B2%20%D1%81%D0%B8%D0%B1%D0%B8%D1%80%D1%81%D0%BA%D0%B8%D1%85%20%D1%82%D0%B0%D1%82%D0%B0%D1%80%201992.djvu ; Tofaca: https://altaica.ru/LIBRARY/turks/%D0%A0%D0%B0%D1%81%D1%81%D0%B0%D0%B4%D0%B8%D0%BD_%D0%A2%D0%BE%D1%84.-%D1%80%D1%83%D1%81%D1%81%D0%BA.%20%D0%B8%20%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE-%D1%82%D0%BE%D1%84.%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C%202005.pdf ; Çulımca: https://altaica.ru/CORPUS/Chulym/chulym_dictionary.xhtml ; Kumandı: https://altaica.ru/LIBRARY/turks/%D0%9A%D1%83%D0%BC%D0%B0%D0%BD%D0%B4%D0%B8%D0%BD%D1%81%D0%BA%D0%BE-%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C%201995.pdf ; Teleüt: https://altaica.ru/LIBRARY/turks/%D0%A2%D0%B5%D0%BB%D0%B5%D1%83%D1%82%D1%81%D0%BA%D0%BE-%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C%201995.pdf ; Şor: https://altaica.ru/LIBRARY/turks/%D0%A8%D0%BE%D1%80%D1%81%D0%BA%D0%BE-%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9%20%D0%B8%20%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE-%D1%88%D0%BE%D1%80%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%BB%D0%BE%D0%B2%D0%B0%D1%80%D1%8C%201993.pdf

- **Diller:** Güney Altayca, Kuzey Altayca, Sahaca (Yakutça), Sibirya Tatarcası, Tofaca, Soyotça, Şorca, Çulımca
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama, Ağız verisi, Tarihî tanık biçimleri
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: sekiz altaica dosyası açıldı (HTTP 200/206).
- **Kimlik:** `sibirya-eski-sozlukler`

<a id="tdk-portal"></a>
#### TDK Sözlükleri (Güncel Türkçe, Derleme, Tarama, Köken Bilgisi…)

<https://sozluk.gov.tr>

TDK'nin bütün sözlükleri tek portalda: Güncel Türkçe Sözlük, Derleme Sözlüğü (Anadolu ağızları), Tanıklarıyla Tarama Sözlüğü (Eski Anadolu Türkçesi), Köken Bilgisi (etimoloji) Sözlüğü, terim sözlükleri.

**Nasıl kullanılır:** Belgelenmiş olmayan JSON ucu: https://sozluk.gov.tr/gts?ara=<kelime> (Güncel Türkçe Sözlük; dizi döner, bulunamazsa {"error": ...}). Diğer sözlükler sitenin içinde ayrı sayfalar (/ds Derleme, /ts Tarama, /etms Köken Bilgisi, /lehceler Karşılaştırmalı Türk Lehçeleri, /osmanlica, /bati, /ads). Bu sayfalar HTML uygulamasıdır; veriyi https://api.sozluk.gov.tr altındaki uçlardan çeker (uygulama kodunda görülen yollar: /gts-yeni/arama, /gts-yeni/maddeler-detay, /yeni-derleme, /koken-bilgisi, /lehceler). Hazır sarmalayıcı: tdk-py (Python). Derleme Sözlüğü ağız kodlarını (tur-ege, tur-erzurum…), Tarama Sözlüğü eski-anadolu tanığını, Lehçeler Sözlüğü 8 lehçede karşılıkları doldurmak için.

- **Diller:** Türkiye Türkçesi, Eski Anadolu Türkçesi
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama, Ağız verisi, Tarihî tanık biçimleri, Ana Türkçe kuruluşu ve etimoloji
- **Erişim:** açık · **Biçim:** api · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: gts JSON ucu çalışıyor (ör. ara=biz, HTTP 200). api.sozluk.gov.tr bu ortamda izinli değil; Derleme/Tarama/Köken uçları için ortama eklenmeli.
- **Kimlik:** `tdk-portal`

<a id="tatar-akademi-sozluk"></a>
#### Tataristan Bilimler Akademisi — Tatarca sözlükler (Süzlek)

<https://www.antat.ru/en/tatzet>

G. İbrahimov Dil, Edebiyat ve Sanat Enstitüsü'nün sözlükleri: Tatar teleneñ añlatmalı süzlege (açıklamalı), Tatar halık söyläşläre süzlege (ağız sözlüğü), Tatarca etimoloji sözlüğü (Ahmetyanov).

**Nasıl kullanılır:** Enstitünün çevrim içi sözlük hizmeti suzlek.antat.ru. Ağız sözlüğü Tatarca ağızlarını (Kazan, Mişer, Sibirya) ayırmak için.

- **Diller:** Tatarca
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama, Ağız verisi, Ana Türkçe kuruluşu ve etimoloji
- **Erişim:** açık · **Biçim:** web · **Güven:** yüksek · **Durum:** aramada görüldü · **Ortam:** izinsiz (www.antat.ru)
- **Kimlik:** `tatar-akademi-sozluk`

<a id="el-sozduk"></a>
#### el-sozduk.kg — Kırgızca sözlükler (Yudahin dahil)

<https://el-sozduk.kg>

Kırgızca-Rusça (Yudahin), Rusça-Kırgızca, İngilizce-Kırgızca sözlükler; açıklamalı sözlük ve deyimler (/frazeologizm/).

**Nasıl kullanılır:** Web arama. Ayrıca Kırgızca dil kaynakları listesi github.com/alexeyev/awesome-kyrgyz-nlp.

- **Diller:** Kırgızca
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama
- **Erişim:** açık · **Biçim:** web · **Güven:** yüksek · **Durum:** aramada görüldü · **Ortam:** izinsiz (el-sozduk.kg)
- **Kimlik:** `el-sozduk`

<a id="cin-turk-dilleri"></a>
#### Çin'deki küçük Türk dillerinin sözlükleri (Batı Yugurca, Salarca)

<
https://search.worldcat.org/search?q=%E8%A5%BF%E9%83%A8%E8%A3%95%E5%9B%BA%E6%B1%89%E8%AF%8D%E5%85%B8>

Lei Xuanchun 1992, Xibu Yugu-Han cidian (Batı Yugurca-Çince sözlük); Lin Lianyun 1992, Sala-Han Han-Sala cihui (Salarca-Çince söz varlığı); Chen Zongzhen'in Batı Yugurca incelemeleri. Fuyu Kırgızcası için Hu Zhenhua'nın çalışmaları.

**Nasıl kullanılır:** Basılı (Çince). Çince arama terimleri: 西部裕固汉词典, 撒拉汉汉撒拉词汇, 富裕柯尔克孜语. Moğolca ve Tibetçe ödünçlere dikkat.

- **Diller:** Sarı Uygurca, Salarca, Fuyu Kırgızcası
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama, Ödünç ve miras ayrımı (özellikle Çuvaşça)
- **Erişim:** basılı · **Biçim:** basili · **Güven:** yüksek · **Durum:** basılı · **Ortam:** —
- **Not:** Çince aramada bulundu.
- **Kimlik:** `cin-turk-dilleri`

<a id="ozbek-kaynaklari"></a>
#### Özbekçe kaynaklar (CTILD Indiana, Chicago CEERES)

<https://ctild.indiana.edu>

Indiana Üniversitesi CTILD: Özbekçe-İngilizce sözlük ve çoklu ortamlı Özbekçe Ağız Sözlüğü (uzb-karluk, uzb-kipcak, uzb-oguz ağızları için). Chicago: Zangori Kema ve Composite Uzbek-English Dictionary. Ayrıca O'zbek tilining izohli lug'ati'nin elektronik sürümü.

**Nasıl kullanılır:** Web arama.

- **Diller:** Özbekçe
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama, Ağız verisi
- **Erişim:** açık · **Biçim:** web · **Güven:** yüksek · **Durum:** aramada görüldü · **Ortam:** izinsiz (ctild.indiana.edu)
- **Kimlik:** `ozbek-kaynaklari`

<a id="budagov"></a>
#### Budagov — Türk-Tatar lehçelerinin karşılaştırmalı sözlüğü (1869-71, 2 cilt)

<https://altaica.ru/LIBRARY/turks/Budagov_SSTTN_1.pdf>

Rusça açıklamalı, Arap harfli madde başlarıyla Osmanlıca, Azerbaycanca, Tatarca, Çağatayca vb. karşılaştırması.

**Nasıl kullanılır:** Cilt 2: https://altaica.ru/LIBRARY/turks/Budagov_SSTTN_2.pdf

- **Diller:** bütün diller
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama, Tarihî tanık biçimleri
- **Erişim:** açık · **Biçim:** pdf · **Güven:** orta · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: 1. cilt PDF'i açıldı (HTTP 200/206).
- **Kimlik:** `budagov`

<a id="dogu-yugur-sozluk"></a>
#### Doğu Yugurca (Moğol dili) - Moğolca - Çince sözlük

<https://altaica.ru/LIBRARY/mong/jegun%20yugur%20dictionary.pdf>

Sarı Uygurca konuşurlarının komşusu olan Moğol dili Doğu Yugurcanın sözlüğü. Sarı Uygurcadaki Moğolca ödünçleri ayırmak için.

**Nasıl kullanılır:** PDF (Moğol harfli ve Çince).

- **Diller:** Sarı Uygurca
- **İşe yaradığı yer:** Ödünç ve miras ayrımı (özellikle Çuvaşça)
- **Erişim:** açık · **Biçim:** pdf · **Güven:** orta · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: altaica PDF'i açıldı (HTTP 200/206).
- **Kimlik:** `dogu-yugur-sozluk`

<a id="qamus"></a>
#### Qamus — Türk Devletleri Parlamenter Asamblesi (TÜRKPA) karşılaştırmalı sözlüğü

<https://www.dailysabah.com/politics/diplomacy/qanun-and-qamus-new-projects-to-bridge-turkic-language-law>

9 Türk dilinde karşılaştırmalı dijital sözlük projesi; Kubbealtı'nın Misalli Büyük Türkçe Sözlük'üyle bütünleşme.

**Nasıl kullanılır:** Çevrim içi adresi henüz doğrulanmadı.

- **Diller:** Türkiye Türkçesi, Azerbaycan Türkçesi, Kazakça, Kırgızca, Özbekçe, Türkmence, Başkurtça, Tatarca, Uygurca
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama
- **Erişim:** kısmen · **Biçim:** web · **Güven:** orta · **Durum:** aramada görüldü · **Ortam:** izinsiz (www.dailysabah.com)
- **Kimlik:** `qamus`

<a id="tuva-sozluk"></a>
#### Tuvan Talking Dictionary (Swarthmore) ve Living Dictionaries

<https://tuvan.swarthmore.edu/about/>

Sesli Tuvaca-İngilizce sözlük (Anderson & Harrison). Living Tongues'un livingdictionaries.app platformunda 120'den fazla sözlük var; Çulımca (Ös) ve Tofaca belgeleme projeleri.

**Nasıl kullanılır:** Web arama; Çulımca için livingtongues.org/os-chulym.

- **Diller:** Tuvaca, Çulımca, Tofaca
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama
- **Erişim:** açık · **Biçim:** web · **Güven:** orta · **Durum:** aramada görüldü · **Ortam:** izinsiz (tuvan.swarthmore.edu)
- **Kimlik:** `tuva-sozluk`

<a id="turkmen-sozluk"></a>
#### Türkmence sözlükler (Webonary, Makul Sözlük, Ene dilim)

<https://www.webonary.org/turkmen/>

Webonary Türkmence-İngilizce (Magtymguly Üniversitesi). makulsozluk.com (Türkmence-İngilizce-Rusça-Türkçe). Ene dilim (açıklamalı Türkmence).

**Nasıl kullanılır:** Web arama.

- **Diller:** Türkmence
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama
- **Erişim:** açık · **Biçim:** web · **Güven:** orta · **Durum:** aramada görüldü · **Ortam:** izinsiz (www.webonary.org)
- **Kimlik:** `turkmen-sozluk`

<a id="turk-akademisi-terim"></a>
#### Uluslararası Türk Akademisi — Türk dilleri terim sözlükleri

<https://turkicacademy.org/proekt/terminological-dictionaries-turkic-languages>

Tıp, ekonomi, askerlik, diplomasi, çevre gibi alanlarda ortak terim sözlükleri (2023'ten beri).

**Nasıl kullanılır:** Aşama 4 (konulara göre genişletme) için.

- **Diller:** Türkiye Türkçesi, Azerbaycan Türkçesi, Kazakça, Kırgızca, Özbekçe, Türkmence, Başkurtça, Tatarca, Uygurca
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama
- **Erişim:** kısmen · **Biçim:** web · **Güven:** orta · **Durum:** aramada görüldü · **Ortam:** izinsiz (turkicacademy.org)
- **Kimlik:** `turk-akademisi-terim`

<a id="sakhatyla"></a>
#### sakhatyla.ru — Sahaca-Rusça / Sahaca-İngilizce sözlük

<https://sakhatyla.ru>

Çevrim içi Saha sözlüğü; 15 ciltlik Büyük Açıklamalı Saha Sözlüğü sayısallaştırılıyor.

**Nasıl kullanılır:** Web arama.

- **Diller:** Sahaca (Yakutça)
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama
- **Erişim:** açık · **Biçim:** web · **Güven:** orta · **Durum:** aramada görüldü · **Ortam:** izinsiz (sakhatyla.ru)
- **Kimlik:** `sakhatyla`

<a id="sozdik"></a>
#### sozdik.kz — Kazakça-Rusça / Rusça-Kazakça sözlük

<https://sozdik.kz>

~92.000 madde (eski bir rakam).

**Nasıl kullanılır:** Web arama.

- **Diller:** Kazakça
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama
- **Erişim:** açık · **Biçim:** web · **Güven:** orta · **Durum:** aramada görüldü · **Ortam:** izinsiz (sozdik.kz)
- **Kimlik:** `sozdik`

<a id="freelang"></a>
#### Freelang kelime listeleri

<https://www.freelang.net/dictionary/>

Küçük İngilizce karşılıklı kelime listeleri (Halaçça 427, Hakasça ~1.220, Nogayca ~1.000 kelime…).

**Nasıl kullanılır:** Başka kaynak bulunamadığında son çare; tek başına kanıt değildir.

- **Diller:** Halaçça, Hakasça, Nogayca, Kumukça, Tuvaca, Gagavuzca, Uygurca, Azerbaycan Türkçesi, Türkmence
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama
- **Erişim:** açık · **Biçim:** web · **Güven:** düşük · **Durum:** aramada görüldü · **Ortam:** izinsiz (www.freelang.net)
- **Kimlik:** `freelang`

<a id="gagavuzca"></a>
#### Gagavuzca sözlükler

<https://www.freelang.net/dictionary/gagauz.php>

Gagavuzca-Rusça-Moldovaca akademik sözlük (basılı; Gaydarcı vd.), Rajki'nin Concise Gagauz-English Dictionary'si, Freelang listesi.

**Nasıl kullanılır:** Çevrim içi kapsamlı Gagavuzca sözlük bulunamadı.

- **Diller:** Gagavuzca
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama
- **Erişim:** kısmen · **Biçim:** web · **Güven:** düşük · **Durum:** aramada görüldü · **Ortam:** izinsiz (www.freelang.net)
- **Kimlik:** `gagavuzca`

<a id="lehceler-com"></a>
#### lehceler.com — Türk lehçeleri karşılaştırmalı sözlüğü

<http://www.lehceler.com/>

Türkiye Türkçesinden ana lehçelere kelime karşılıkları.

**Nasıl kullanılır:** Türkçe kelimeyle ara. Hızlı ilk tarama için; biçimleri bir dil sözlüğüyle denetle.

- **Diller:** Türkiye Türkçesi, Azerbaycan Türkçesi, Türkmence, Kazakça, Kırgızca, Özbekçe, Tatarca, Başkurtça, Uygurca
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama
- **Erişim:** açık · **Biçim:** web · **Güven:** düşük · **Durum:** aramada görüldü · **Ortam:** izinsiz (www.lehceler.com)
- **Kimlik:** `lehceler-com`

### Derlemler ve sıklık listeleri

<a id="qazcorpus"></a>
#### Kazak Dili Ulusal Derlemi

<https://qazcorpus.kz>

Dilbilim Enstitüsü, 2012'den beri; 12 alt derlem. qazcorpora.kz olarak da geçiyor.

**Nasıl kullanılır:** Web arama; erişim koşulları doğrulanmadı.

- **Diller:** Kazakça
- **İşe yaradığı yer:** Sıklık listeleri ve kavram listeleri, Yaşayan dillerde biçim toplama
- **Erişim:** kısmen · **Biçim:** web · **Güven:** yüksek · **Durum:** aramada görüldü · **Ortam:** izinsiz (qazcorpus.kz)
- **Kimlik:** `qazcorpus`

<a id="tugan-tel"></a>
#### Tatar Ulusal Derlemi "Tugan Tel" ve Yazılı Tatarca Derlemi

<https://tugantel.tatar>

180 milyonu aşkın kelime kullanımı (2019). Ayrıca Kazan Federal Üniversitesi derlemi corpus.tatar (indirilebilir sıklık listeleri).

**Nasıl kullanılır:** Web arama; sıklık listeleri https://www.corpus.tatar/en/statistics.

- **Diller:** Tatarca
- **İşe yaradığı yer:** Sıklık listeleri ve kavram listeleri, Yaşayan dillerde biçim toplama
- **Erişim:** açık · **Biçim:** web · **Güven:** yüksek · **Durum:** aramada görüldü · **Ortam:** izinsiz (tugantel.tatar)
- **Kimlik:** `tugan-tel`

<a id="tnc"></a>
#### Türkçe Ulusal Derlemi (TNC) ve Türkçe Sıklık Sözlüğü

<https://www.tnc.org.tr>

50 milyon kelimelik dengeli Türkçe derlemi (1990-2009); Aksan vd. 2012 Türkçe Sıklık Sözlüğü.

**Nasıl kullanılır:** Çalışma sırasını (SIRA.md) gerçek sıklığa göre düzeltmek için.

- **Diller:** Türkiye Türkçesi
- **İşe yaradığı yer:** Sıklık listeleri ve kavram listeleri
- **Erişim:** kısmen · **Biçim:** web · **Güven:** yüksek · **Durum:** aramada görüldü · **Ortam:** izinsiz (www.tnc.org.tr)
- **Kimlik:** `tnc`

<a id="vatec"></a>
#### VATEC — İslam öncesi Eski Türkçe metinlerin elektronik derlemi (Frankfurt)

<https://vatec2.fkidg1.uni-frankfurt.de/>

Yayımlanmış Eski Uygurca metinlerde kelime, ek ve yazım değişkeni araması.

**Nasıl kullanılır:** Web sorgu formları.

- **Diller:** Eski Türkçe (Göktürk ve Uygur metinleri)
- **İşe yaradığı yer:** Tarihî tanık biçimleri
- **Erişim:** açık · **Biçim:** web · **Güven:** yüksek · **Durum:** aramada görüldü · **Ortam:** izinsiz (vatec2.fkidg1.uni-frankfurt.de)
- **Doğrulama:** 2026-11-12: Frankfurt sunucusu bu ortamda izinli değil; aramada ve Turfan sitesinde görüldü.
- **Kimlik:** `vatec`

<a id="wowa"></a>
#### WOWA — Word Order in Western Asia derlemi (Bamberg)

<https://multicast.aspra.uni-bamberg.de/resources/wowa>

Batı Asya'nın az çalışılmış dillerinden açıklamalı konuşma metinleri; Oğuz kısmında Ankara, Erzurum, Tebriz, Kaşkay.

**Nasıl kullanılır:** Her alt veri seti ayrı indirilir (metadata PDF, metin); tüm derlem DOI 10.48564/unibafd-gyws0-g4218.

- **Diller:** Türkiye Türkçesi, `tur-erzurum` (ağız), `aze-iran` (ağız), Kaşkayca
- **İşe yaradığı yer:** Ağız verisi, Dilbilgisi (Aşama 3)
- **Erişim:** açık · **Biçim:** csv · **Güven:** yüksek · **Durum:** aramada görüldü · **Ortam:** izinsiz (multicast.aspra.uni-bamberg.de)
- **Kimlik:** `wowa`

<a id="kirim-tatar-derlem"></a>
#### Kırım Tatarcası Ulusal Derlemi ve sözlükleri

<https://ctcorpus.org/en/>

Kırım Tatarcası derlemi. Sözlük için ana-yurt.com (iki alfabe, Rusça) ve medeniye.org/en/lugat (durumu belirsiz).

**Nasıl kullanılır:** Web arama.

- **Diller:** Kırım Tatarcası
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama, Sıklık listeleri ve kavram listeleri
- **Erişim:** açık · **Biçim:** web · **Güven:** orta · **Durum:** aramada görüldü · **Ortam:** izinsiz (ctcorpus.org)
- **Kimlik:** `kirim-tatar-derlem`

<a id="leipzig-corpora"></a>
#### Leipzig Corpora Collection — kelime sıklık listeleri

<https://wortschatz.uni-leipzig.de/en/download>

Dil bazında derlemler ve sıklık listeleri (CC BY 4.0); ör. Özbekçe uzb_community_2017 (10,9 milyon kelime).

**Nasıl kullanılır:** Dil sayfaları curl.corpora.uni-leipzig.de/languages/<iso>.

- **Diller:** Özbekçe, Kazakça, Kırgızca, Tatarca, Azerbaycan Türkçesi, Türkiye Türkçesi, Başkurtça, Türkmence, Uygurca
- **İşe yaradığı yer:** Sıklık listeleri ve kavram listeleri, Toplu, makinece okunabilir veri
- **Erişim:** açık · **Biçim:** csv · **Güven:** orta · **Durum:** aramada görüldü · **Ortam:** izinsiz (wortschatz.uni-leipzig.de)
- **Not:** Dil sayfası ör. curl.corpora.uni-leipzig.de/languages/uzb. Özbekçe dışındaki dillerin dosyaları ayrıca doğrulanmalı.
- **Kimlik:** `leipzig-corpora`

<a id="opensubtitles-siklik"></a>
#### OpenSubtitles tabanlı sıklık listeleri (hermitdave/FrequencyWords, orgtre/top-open-subtitles-sentences)

<https://github.com/hermitdave/FrequencyWords>

Konuşma diline yakın sıklık listeleri (film altyazıları).

**Nasıl kullanılır:** Dil koduna göre dosyalar: https://raw.githubusercontent.com/hermitdave/FrequencyWords/master/content/2018/<kod>/<kod>_50k.txt (kelime ve sayı). Türkçe için tr, Kazakça için kk.

- **Diller:** Türkiye Türkçesi, Kazakça
- **İşe yaradığı yer:** Sıklık listeleri ve kavram listeleri
- **Erişim:** açık · **Biçim:** csv · **Güven:** orta · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: tr_50k.txt raw üzerinden indirildi (HTTP 200, ~700 KB).
- **Kimlik:** `opensubtitles-siklik`

<a id="sketch-engine-turk"></a>
#### Sketch Engine — Turkic web corpora

<https://www.sketchengine.eu/turkic-web-corpora/>

Web'den derlenmiş Türk dilleri derlemleri, sıklık listeleri.

**Nasıl kullanılır:** Ticari platform, deneme erişimi.

- **Diller:** Azerbaycan Türkçesi, Kazakça, Kırgızca, Özbekçe, Türkmence, Türkiye Türkçesi
- **İşe yaradığı yer:** Sıklık listeleri ve kavram listeleri
- **Erişim:** ücretli · **Biçim:** web · **Güven:** orta · **Durum:** aramada görüldü · **Ortam:** izinsiz (www.sketchengine.eu)
- **Kimlik:** `sketch-engine-turk`

<a id="tatar-derlem"></a>
#### Tatarca Ulusal Derlemi (corpus.tatar)

<https://www.corpus.tatar/en/statistics>

Kazan merkezli büyük Tatarca derlemi; sıklık istatistikleri. Tugan Tel'den (tugan-tel) ayrı bir derlem.

**Nasıl kullanılır:** search.corpus.tatar arayüzünde kelime ve sıklık arama.

- **Diller:** Tatarca
- **İşe yaradığı yer:** Sıklık listeleri ve kavram listeleri, Yaşayan dillerde biçim toplama
- **Erişim:** açık · **Biçim:** web · **Güven:** orta · **Durum:** aramada görüldü · **Ortam:** izinsiz (www.corpus.tatar)
- **Kimlik:** `tatar-derlem`

<a id="til-mt"></a>
#### Turkic Interlingua (TIL) — 22 Türk dili paralel derlemi

<https://github.com/turkic-interlingua/til-mt>

22 Türk dilinde 75 milyondan fazla cümle çifti (İngilizce, Rusça ve Türk dilleri arası), 400'den fazla çeviri yönü. Mirzakhalov vd. 2021.

**Nasıl kullanılır:** GitHub'dan veri ve modeller. Aynı cümlenin dillerdeki karşılıkları kelime sıklığı ve örnek için kullanılabilir.

- **Diller:** bütün diller
- **İşe yaradığı yer:** Toplu, makinece okunabilir veri, Sıklık listeleri ve kavram listeleri, Yaşayan dillerde biçim toplama
- **Erişim:** açık · **Biçim:** git · **Güven:** orta · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: README raw.githubusercontent.com/turkic-interlingua/til-mt/main/README.md üzerinden okundu (HTTP 200). GitHub HTML sayfası bu ortamda 403.
- **Kimlik:** `til-mt`

<a id="cuvasca-ceviri"></a>
#### translate.chv.su — Çuvaşça-Rusça derlem, çeviri ve sözlük (Plotnikov)

<https://ru.translate.chv.su>

Çuvaşça-Rusça paralel derlemi (~225.000 cümle çifti) üzerinde çeviri ve sözlük. Aynı geliştiricinin çevrim içi Çuvaşça sözlüğü.

**Nasıl kullanılır:** Kelimenin bugünkü kullanımını ve sıklığını görmek için.

- **Diller:** Çuvaşça
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama, Sıklık listeleri ve kavram listeleri
- **Erişim:** açık · **Biçim:** web · **Güven:** orta · **Durum:** aramada görüldü · **Ortam:** izinsiz (ru.translate.chv.su)
- **Not:** Rusça aramada bulundu.
- **Kimlik:** `cuvasca-ceviri`

### Küçük diller ve belgeleme

<a id="sibirya-tatar-agiz"></a>
#### Alişina 1994 — Tobol-İrtış ağzı (Sibirya Tatarcası) ve Tümen Üniversitesi e-kitaplığı

<
https://elib.utmn.ru/jspui/bitstream/ru-tsu/35717/1/Alishina_1994_Tobolo-Irtyshskii_dialekt.pdf>

Sibirya Tatarcasının Tobol-İrtış ağzının tanımı ve söz varlığı (Rusça). Tümen Devlet Üniversitesi deposunda (elib.utmn.ru) başka Sibirya Tatarcası çalışmaları da var.

**Nasıl kullanılır:** PDF. Sibirya Tatarcası (sty) ağız biçimleri için.

- **Diller:** Sibirya Tatarcası
- **İşe yaradığı yer:** Ağız verisi, Yaşayan dillerde biçim toplama
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** aramada görüldü · **Ortam:** izinsiz (elib.utmn.ru)
- **Kimlik:** `sibirya-tatar-agiz`

<a id="elar"></a>
#### ELAR — Endangered Languages Archive

<https://eldp.access.preservica.com/>

Tehlikedeki diller arşivi (550'den fazla dil). Tofaca (son konuşurlarla derlem), Çulımca (Melets ve Eushta), Sarı Uygurca (2024'ten beri), Teleüt (Güney Altay) koleksiyonları.

**Nasıl kullanılır:** Koleksiyon sayfaları (ör. dk0495, dk0337); kayıt ve metinler.

- **Diller:** Tofaca, Çulımca, Sarı Uygurca, Güney Altayca
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama, Ağız verisi
- **Erişim:** kısmen · **Biçim:** web · **Güven:** yüksek · **Durum:** aramada görüldü · **Ortam:** izinsiz (eldp.access.preservica.com)
- **Kimlik:** `elar`

<a id="rf-turk-agiz-atlasi"></a>
#### Rusya Federasyonu Türk Ağızları Atlası (Dybo)

<https://www.altaist.org/home/confessions/dybo-anna/the-atlas-of-the-turkic-dialects-in-the-russian-federation-some-results-and-problems/>

Rusya'daki Türk ağızlarının atlas projesi; Şor ve Çulım ağızları dahil.

**Nasıl kullanılır:** Sonuçlar makale ve sunumlarda; ağız kodlarını doldurmak için.

- **Diller:** Şorca, Çulımca, Tatarca, Başkurtça, Güney Altayca, Kuzey Altayca, Hakasça
- **İşe yaradığı yer:** Ağız verisi, Örgü: benzerlik ve anlaşılırlık değerleri
- **Erişim:** kısmen · **Biçim:** web · **Güven:** yüksek · **Durum:** aramada görüldü · **Ortam:** izinsiz (www.altaist.org)
- **Kimlik:** `rf-turk-agiz-atlasi`

<a id="salarca"></a>
#### Salarca — Dwyer'in çalışmaları ve DoBeS Salar projesi

<https://dobes.mpi.nl/project_data/salar/salar.pdf>

DoBeS belgeleme projesi; Salarca-Uygurca-Çince sözlük (2010, basılı); Yakup'un İli Salarcası sözlükçesi.

**Nasıl kullanılır:** PDF ve basılı eserler.

- **Diller:** Salarca
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama
- **Erişim:** kısmen · **Biçim:** pdf · **Güven:** yüksek · **Durum:** aramada görüldü · **Ortam:** izinsiz (dobes.mpi.nl)
- **Kimlik:** `salarca`

<a id="kore-ask-real"></a>
#### ASK REAL — Kore Altayistik Derneği saha araştırmaları (2003-2009)

<https://www.ardahan.edu.tr/cuaconference2014/upload/yong_song_li.pdf>

Seul Ulusal Üniversitesi merkezli ekibin tehlikedeki Türk dilleri saha çalışmaları (ses kayıtlı kelime listeleri).

**Nasıl kullanılır:** Yong Song Li'nin raporu (PDF); kayıtlar için ekiple iletişim gerekir.

- **Diller:** Şorca, Çuvaşça, Tuvaca, Sarı Uygurca, Gagavuzca, Urumca, Karayca, Çulımca, Salarca, Dolganca, Sahaca (Yakutça), Fuyu Kırgızcası, Hakasça, Güney Altayca
- **İşe yaradığı yer:** Ağız verisi, Ses denklikleri
- **Erişim:** kısmen · **Biçim:** pdf · **Güven:** orta · **Durum:** aramada görüldü · **Ortam:** izinsiz (www.ardahan.edu.tr)
- **Doğrulama:** 2026-11-12: aramada görüldü; sunucu bu ortamda izinli değil.
- **Kimlik:** `kore-ask-real`

<a id="elp"></a>
#### Endangered Languages Project

<https://www.endangeredlanguages.com>

Tehlikedeki diller için konuşur sayıları, bibliyografya, örnekler.

**Nasıl kullanılır:** Dil sayfaları.

- **Diller:** bütün diller
- **İşe yaradığı yer:** Konuşur sayısı ve canlılık, Makaleler ve bibliyografya
- **Erişim:** açık · **Biçim:** web · **Güven:** orta · **Durum:** aramada görüldü · **Ortam:** izinsiz (www.endangeredlanguages.com)
- **Kimlik:** `elp`

<a id="atlaskmns"></a>
#### Kuzey, Sibirya ve Uzak Doğu yerli halkları etkileşimli atlası

<https://www.atlaskmns.ru/page/en/index.html>

Soyotça, Şorca, Çulımca dil sayfaları; nüfus sayımı verisi ve uyarıları.

**Nasıl kullanılır:** Dil sayfaları (ör. lang_sojoty.html, lang_shorcy.html).

- **Diller:** Soyotça, Şorca, Çulımca
- **İşe yaradığı yer:** Konuşur sayısı ve canlılık, Yaşayan dillerde biçim toplama
- **Erişim:** açık · **Biçim:** web · **Güven:** orta · **Durum:** aramada görüldü · **Ortam:** izinsiz (www.atlaskmns.ru)
- **Kimlik:** `atlaskmns`

<a id="lingsib"></a>
#### Sibirya Dilleri — Rusya Bilimler Akademisi Etnoloji Enstitüsü

<https://lingsib.iea.ras.ru/en/languages/tofa.shtml>

Tofaca, Soyotça ve diğer Sibirya dilleri hakkında bilgi sayfaları.

**Nasıl kullanılır:** Web.

- **Diller:** Tofaca, Soyotça
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama, Konuşur sayısı ve canlılık, Sınıflandırma (soy ağacı)
- **Erişim:** açık · **Biçim:** web · **Güven:** orta · **Durum:** aramada görüldü · **Ortam:** izinsiz (lingsib.iea.ras.ru)
- **Kimlik:** `lingsib`

### Sınıflandırma ve el kitapları

<a id="glottolog"></a>
#### Glottolog

<https://glottolog.org/resource/languoid/id/turk1311>

Türk dillerinin sınıflandırması (turk1311), her dil ve alt grup için kaynakça. Johanson 2021 ve Tekin 1990'a göre alt sınıflandırma notları.

**Nasıl kullanılır:** Dil sayfaları ör. nucl1301 (Türkiye Türkçesi), sout2701 (Güney Altay).

- **Diller:** bütün diller
- **İşe yaradığı yer:** Sınıflandırma (soy ağacı), Makaleler ve bibliyografya
- **Erişim:** açık · **Biçim:** web · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: Türk dilleri sayfası açıldı (HTTP 200, Glottolog 5.4).
- **Kimlik:** `glottolog`

<a id="grambank"></a>
#### Grambank

<https://grambank.clld.org>

Dünya dilleri için dilbilgisel özellik veritabanı; Türk dilleri dahil.

**Nasıl kullanılır:** Dilbilgisi aşamasında ekleri ve yapıları karşılaştırmak için.

- **Diller:** bütün diller
- **İşe yaradığı yer:** Dilbilgisi (Aşama 3)
- **Erişim:** açık · **Biçim:** csv · **Güven:** yüksek · **Durum:** aramada görüldü · **Ortam:** izinsiz (grambank.clld.org)
- **Kimlik:** `grambank`

<a id="johanson-csato"></a>
#### Johanson & Csató (ed.) — The Turkic Languages (2. baskı, 2021)

<https://www.routledge.com>

Türk dillerinin standart el kitabı: sınıflandırma, ses tarihi, her dilin dilbilgisi.

**Nasıl kullanılır:** Basılı/ücretli.

- **Diller:** bütün diller
- **İşe yaradığı yer:** Sınıflandırma (soy ağacı), Ses denklikleri, Dilbilgisi (Aşama 3)
- **Erişim:** ücretli · **Biçim:** basili · **Güven:** yüksek · **Durum:** basılı · **Ortam:** izinsiz (www.routledge.com)
- **Kimlik:** `johanson-csato`

<a id="tenishev"></a>
#### Сравнительно-историческая грамматика тюркских языков (Tenishev, 1984–2006)

<https://search.worldcat.org/oclc/13008487>

Türk dillerinin karşılaştırmalı-tarihî dilbilgisi (ses, dilbilgisi, söz varlığı ciltleri).

**Nasıl kullanılır:** Basılı; bazı ciltler Altaica e-kütüphanesinde olabilir.

- **Diller:** bütün diller
- **İşe yaradığı yer:** Ses denklikleri, Dilbilgisi (Aşama 3), Ana Türkçe kuruluşu ve etimoloji
- **Erişim:** basılı · **Biçim:** basili · **Güven:** yüksek · **Durum:** basılı · **Ortam:** —
- **Kimlik:** `tenishev`

### Konuşur sayısı ve canlılık

<a id="iran-dil-atlasi"></a>
#### Iran Atlas — İran'ın Dil Atlası (Anonby vd.)

<https://iranatlas.net>

İran'da konuşulan dillerin ve ağızların haritası ve sınıflandırması; Azerbaycan Türkçesi, Kaşkayca, Horasan Türkçesi, Halaçça ve küçük Oğuz ağızlarının dağılımı.

**Nasıl kullanılır:** Harita ve belge sayfaları (Google Docs vekil sayfaları da var). Konuşur sayısı ve komşuluk (örgü) için.

- **Diller:** `aze-iran` (ağız), Kaşkayca, Horasan Türkçesi, Halaçça
- **İşe yaradığı yer:** Konuşur sayısı ve canlılık, Sınıflandırma (soy ağacı), Örgü: benzerlik ve anlaşılırlık değerleri
- **Erişim:** açık · **Biçim:** web · **Güven:** yüksek · **Durum:** aramada görüldü · **Ortam:** izinsiz (iranatlas.net)
- **Not:** Farsça aramada bulundu. Farsça sözlük sitesi abadis.ir Azerbaycanca karşılıklar için yardımcı olabilir (güven düşük).
- **Kimlik:** `iran-dil-atlasi`

<a id="ethnologue"></a>
#### Ethnologue

<https://www.ethnologue.com>

Konuşur sayıları ve dil durumu.

**Nasıl kullanılır:** Ücretli; Wikipedia ve Glottolog sık atıf yapar.

- **Diller:** bütün diller
- **İşe yaradığı yer:** Konuşur sayısı ve canlılık
- **Erişim:** ücretli · **Biçim:** web · **Güven:** orta · **Durum:** aramada görüldü · **Ortam:** izinsiz (www.ethnologue.com)
- **Not:** Tanım farklarına dikkat (ör. Balkan Gagavuz Türkçesi rakamı Türkiye Yörüklerini de sayıyor).
- **Kimlik:** `ethnologue`

<a id="rosstat-2021"></a>
#### Rosstat — 2021 Rusya nüfus sayımı dil tabloları

<https://rosstat.gov.ru>

Rusya'daki Türk dillerinin konuşur sayıları.

**Nasıl kullanılır:** Dikkat: Sayım yeterliliği ölçmüyor (en fazla üç "konuşulan" dil ve bir "ana dil"); yanıtsızlık arttı. Rakamlar aşağı ya da yukarı sapmış olabilir.

- **Diller:** Tatarca, Başkurtça, Çuvaşça, Sahaca (Yakutça), Tuvaca, Hakasça, Güney Altayca, Kuzey Altayca, Şorca, Tofaca, Soyotça, Dolganca, Kumukça, Karaçay-Malkarca, Nogayca, Sibirya Tatarcası, Çulımca
- **İşe yaradığı yer:** Konuşur sayısı ve canlılık
- **Erişim:** açık · **Biçim:** web · **Güven:** orta · **Durum:** aramada görüldü · **Ortam:** izinsiz (rosstat.gov.ru)
- **Kimlik:** `rosstat-2021`

<a id="unesco-wal"></a>
#### UNESCO World Atlas of Languages

<https://en.wal.unesco.org>

Dillerin durumu, canlılığı, tehlike düzeyi; ülke ve dile göre arama.

**Nasıl kullanılır:** Dil sayfaları (ör. Rusya'da Tatarca).

- **Diller:** bütün diller
- **İşe yaradığı yer:** Konuşur sayısı ve canlılık
- **Erişim:** açık · **Biçim:** web · **Güven:** orta · **Durum:** aramada görüldü · **Ortam:** izinsiz (en.wal.unesco.org)
- **Kimlik:** `unesco-wal`

<a id="joshua-project"></a>
#### Joshua Project

<https://joshuaproject.net>

Halk grupları ve dilleri için nüfus tahminleri (ör. Irak Türkmenleri, Horasan Türkleri).

**Nasıl kullanılır:** Başka kaynak yoksa kaba tahmin olarak.

- **Diller:** bütün diller
- **İşe yaradığı yer:** Konuşur sayısı ve canlılık
- **Erişim:** açık · **Biçim:** web · **Güven:** düşük · **Durum:** aramada görüldü · **Ortam:** izinsiz (joshuaproject.net)
- **Kimlik:** `joshua-project`

<a id="wikipedia-turk-dilleri"></a>
#### Wikipedia — List of Turkic languages

<https://en.wikipedia.org/wiki/List_of_Turkic_languages>

Türk dillerinin konuşur sayısı, tehlike durumu ve sınıflandırma özeti.

**Nasıl kullanılır:** İkincil kaynak; rakamların asıl kaynağına git.

- **Diller:** bütün diller
- **İşe yaradığı yer:** Konuşur sayısı ve canlılık, Sınıflandırma (soy ağacı)
- **Erişim:** açık · **Biçim:** web · **Güven:** düşük · **Durum:** aramada görüldü · **Ortam:** izinsiz (en.wikipedia.org)
- **Kimlik:** `wikipedia-turk-dilleri`

### Anlaşılırlık ve benzerlik çalışmaları

<a id="scil-2026"></a>
#### Baidildinova vd. 2026 — Quantifying mutual intelligibility gradients in Turkic languages (SCiL)

<https://aclanthology.org/2026.scil-main.41/>

Dil modelleriyle Türk dilleri arası aktarım. Kırgızcadan Kazakçaya aktarım tersinden güçlü; sözcük benzerliği, ses dizimi örtüşmesi ve soy uzaklığı en iyi öngörücüler.

**Nasıl kullanılır:** Örgüdeki yönlü anlaşılırlık değerlerini denetlemek için.

- **Diller:** Türkiye Türkçesi, Azerbaycan Türkçesi, Kazakça, Kırgızca, Özbekçe, Uygurca
- **İşe yaradığı yer:** Örgü: benzerlik ve anlaşılırlık değerleri
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: ACL Anthology sayfası ve PDF açıldı (HTTP 200).
- **Kimlik:** `scil-2026`

<a id="salehi-2017"></a>
#### Salehi & Neysani 2017 — Azerbaycan Türkçesinin Türkiye Türkçesi konuşurlarınca anlaşılırlığı

<
https://www.tandfonline.com/action/doSearch?AllField=Receptive+intelligibility+of+Turkish+to+Iranian-Azerbaijani+speakers>

Dinleyici deneyi; Türkiye-Azerbaycan anlaşılırlığı.

**Nasıl kullanılır:** Salehi & Neysani 2017, Receptive intelligibility of Turkish to Iranian-Azerbaijani speakers, Cogent Education 4(1). Künye SCiL 2026 makalesinin (scil-2026) kaynakçasında da var.

- **Diller:** Türkiye Türkçesi, Azerbaycan Türkçesi
- **İşe yaradığı yer:** Örgü: benzerlik ve anlaşılırlık değerleri
- **Erişim:** kısmen · **Biçim:** pdf · **Güven:** yüksek · **Durum:** aramada görüldü · **Ortam:** izinsiz (www.tandfonline.com)
- **Doğrulama:** 2026-11-12: eski adres makalenin kendisi değil SCiL 2026 PDF'iydi; dergi aramasına çevrildi. Makale bu ortamdan açılmadı.
- **Kimlik:** `salehi-2017`

<a id="en-sik-1000"></a>
#### En sık 1000 kelime açısından modern Türk dilleri (Türkiye, Azerbaycan, Kazak, Kırgız, Özbek)

<https://www.academia.edu/40960810>

~940 içerik kelimesi karşılaştırılmış; en sık 150'den fazla kelime beş dilde ortak.

**Nasıl kullanılır:** Ortak kelimelerin sıklığa göre dağılımı; SIRA.md için yararlı.

- **Diller:** Türkiye Türkçesi, Azerbaycan Türkçesi, Kazakça, Kırgızca, Özbekçe
- **İşe yaradığı yer:** Örgü: benzerlik ve anlaşılırlık değerleri, Sıklık listeleri ve kavram listeleri
- **Erişim:** açık · **Biçim:** pdf · **Güven:** orta · **Durum:** aramada görüldü · **Ortam:** izinsiz (www.academia.edu)
- **Kimlik:** `en-sik-1000`

### Ses bilgisi

<a id="proto-turkic-unsuzler"></a>
#### Sino-Platonic Papers 325 — Proto-Turkic consonants

<https://sino-platonic.org/complete/spp325_proto_Turkic_consonants.pdf>

Ana Türkçe ünsüzleri üzerine açık erişimli çalışma.

**Nasıl kullanılır:** Ses kuralları aşamasında başvuru.

- **Diller:** bütün diller
- **İşe yaradığı yer:** Ses denklikleri, Ana Türkçe kuruluşu ve etimoloji
- **Erişim:** açık · **Biçim:** pdf · **Güven:** orta · **Durum:** aramada görüldü · **Ortam:** izinsiz (sino-platonic.org)
- **Kimlik:** `proto-turkic-unsuzler`

### Yazım

<a id="ortak-turk-alfabesi"></a>
#### Ortak Türk Alfabesi (Türk Devletleri Teşkilatı, 2024)

<https://en.wikipedia.org/wiki/Common_Turkic_alphabet>

34 harf: A Ä B C Ç D E F G Ğ H I İ J K L M N Ñ O Ö P Q R S Ş T U Ü V W X Y Z. Bakü, Eylül 2024; Mayıs 2025 Budapeşte zirvesinde onaylandı. Her dil yalnızca kendi seslerine karşılık gelen harfleri kullanır.

**Nasıl kullanılır:** ILKELER §11 (Yazım) bu alfabeye bağlanmalı; çalışma yazımımız zaten çok yakın (ä, ñ, q, w, x).

- **Diller:** bütün diller
- **İşe yaradığı yer:** Ortak alfabe ve yazım
- **Erişim:** açık · **Biçim:** web · **Güven:** yüksek · **Durum:** aramada görüldü · **Ortam:** izinsiz (en.wikipedia.org)
- **Kimlik:** `ortak-turk-alfabesi`

### Portallar ve kütüphaneler

<a id="ilcaa-kaynaklari"></a>
#### ILCAA çevrim içi kaynak portalı (Tokyo)

<https://online-resources.aa-ken.jp/>

Asya ve Afrika dilleri üzerine çevrim içi sözlükler, temel söz varlığı listeleri ve derlemler; Türk dilleri kayıtları (turkbv) dahil.

**Nasıl kullanılır:** Dil adına göre ara.

- **Diller:** bütün diller
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama, Makaleler ve bibliyografya
- **Erişim:** açık · **Biçim:** web · **Güven:** yüksek · **Durum:** aramada görüldü · **Ortam:** izinsiz (online-resources.aa-ken.jp)
- **Not:** Japonca aramada bulundu.
- **Kimlik:** `ilcaa-kaynaklari`

<a id="lexilogos"></a>
#### Lexilogos — dil bazlı sözlük portalı

<https://www.lexilogos.com/english/turkish_dictionary.htm>

Her dil için çevrim içi sözlüklerin bağlantı listesi (ör. kazakh_dictionary.htm, tatar_crimean_dictionary.htm, turkmen_dictionary.htm, uyghur_dictionary.htm).

**Nasıl kullanılır:** Yeni bir dil için sözlük ararken ilk durak.

- **Diller:** Türkiye Türkçesi, Azerbaycan Türkçesi, Kazakça, Tatarca, Kırım Tatarcası, Türkmence, Uygurca, Kırgızca, Özbekçe
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama
- **Erişim:** açık · **Biçim:** web · **Güven:** orta · **Durum:** aramada görüldü · **Ortam:** izinsiz (www.lexilogos.com)
- **Kimlik:** `lexilogos`

<a id="altaica-kutuphane"></a>
#### Monumenta Altaica — Türkoloji e-kütüphanesi

<https://altaica.c4.starlingdb.org/e_turkic_books.html>

Türkoloji ve Altayistik kitaplarının PDF'leri (Poppe, Vladimirtsov, Karayca söz dizimi, Tenishev serisinin bazı ciltleri…). Altaica.ru ile aynı içerik.

**Nasıl kullanılır:** starlingdb.org alt alan adında olduğu için bu ortamdan erişilebilir olabilir.

- **Diller:** bütün diller
- **İşe yaradığı yer:** Makaleler ve bibliyografya, Ana Türkçe kuruluşu ve etimoloji, Ses denklikleri
- **Erişim:** açık · **Biçim:** pdf · **Güven:** orta · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: Türkoloji kitap listesi açıldı (HTTP 200). Aynı içerik altaica.ru/LIBRARY altında da var.
- **Not:** c4.starlingdb.org alt alan adı izin listesinde ayrıca yok; denenmeli.
- **Kimlik:** `altaica-kutuphane`

<a id="yok-acik-bilim"></a>
#### YÖK Açık Bilim ve Tez Merkezi — Türkiye'deki lisansüstü tezler

<https://acikbilim.yok.gov.tr>

Türkiye'de yazılmış tezler: Çağatayca lügatlerin çevriyazıları (Abuşka, Şeyh Süleyman Efendi, Bedâyiü'l-Lugat), ağız monografileri, lehçeler arası karşılaştırmalı sözlükler.

**Nasıl kullanılır:** Tez adına ya da konuya göre ara. Çağatayca (chg) ve Türkiye ağızları için zengin.

- **Diller:** bütün diller
- **İşe yaradığı yer:** Makaleler ve bibliyografya, Tarihî tanık biçimleri, Ağız verisi, Yaşayan dillerde biçim toplama
- **Erişim:** kısmen · **Biçim:** pdf · **Güven:** orta · **Durum:** aramada görüldü · **Ortam:** izinsiz (acikbilim.yok.gov.tr)
- **Kimlik:** `yok-acik-bilim`

<a id="kumuk-kaynaklari"></a>
#### til.im — Kumukça kitaplar ve sözlükler

<https://til.im>

Kumukça dil kitapları, sözlükler ve konuşma kılavuzları (Rusça arayüz); ör. Sovremennyy kumykskiy yazyk.

**Nasıl kullanılır:** Kitaplar bölümünde (knigi) sözlükleri ara.

- **Diller:** Kumukça
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama, Dilbilgisi (Aşama 3)
- **Erişim:** açık · **Biçim:** pdf · **Güven:** orta · **Durum:** aramada görüldü · **Ortam:** izinsiz (til.im)
- **Kimlik:** `kumuk-kaynaklari`

### Dergiler ve bibliyografya

<a id="nsc-filoloji"></a>
#### RBA Sibirya Şubesi Filoloji Enstitüsü (Novosibirsk) — dergiler ve e-kitaplık

<https://philology.nsc.ru/>

Sibirya Türk dilleri üzerine makaleler (Sibirskiy filologicheskiy zhurnal, Kritika i semiotika) ve sözlük taslakları; ör. Dobrinina'nın Altayca sözlüğü (fehu.philology.nsc.ru/elib/).

**Nasıl kullanılır:** PDF'ler fehu.philology.nsc.ru/journals/spj/pdf/<yıl_sayı>/<no>.pdf biçiminde. Rusça arama: алтайско-русский словарь, хакасско-русский словарь.

- **Diller:** Güney Altayca, Kuzey Altayca, Hakasça, Şorca, Çulımca, Tuvaca, Tofaca, Sahaca (Yakutça), Sibirya Tatarcası
- **İşe yaradığı yer:** Yaşayan dillerde biçim toplama, Ağız verisi, Makaleler ve bibliyografya
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** aramada görüldü · **Ortam:** izinsiz (philology.nsc.ru)
- **Kimlik:** `nsc-filoloji`

<a id="sovet-turkologiya"></a>
#### Sovetskaya Tyurkologiya dergisi arşivi (Azerbaycan Cumhurbaşkanlığı Kütüphanesi, TurkLib)

<https://files.preslib.az/projects/turklib/>

Sovyet Türkolojisinin ana dergisinin (1970–1991) taranmış sayıları: etimoloji, ses tarihi, ağız ve karşılaştırma makaleleri. Aynı kütüphanenin sözlük koleksiyonu: preslib.az/en/collections/ebooks/0eJYS7u.

**Nasıl kullanılır:** Sayılar jurnallar/sovet_turkologiya/sovtur_<yıl>_<sayı>.pdf biçiminde.

- **Diller:** bütün diller
- **İşe yaradığı yer:** Makaleler ve bibliyografya, Ana Türkçe kuruluşu ve etimoloji, Ses denklikleri, Ağız verisi
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** aramada görüldü · **Ortam:** izinsiz (files.preslib.az)
- **Not:** Azerbaycanca aramada bulundu.
- **Kimlik:** `sovet-turkologiya`

<a id="studia-etymologica-cracoviensia"></a>
#### Studia Etymologica Cracoviensia (Krakov, 1996-2015) ve Stachowski'nin çalışmaları

<https://ejournals.eu/en/journal/studia-etymologica-cracoviensia>

Etimolojiye adanmış dergi; Türk dillerindeki ödünçler üzerine çok makale var. Stachowski'nin Dolganca kelime hazinesi (1993) Dolganca kelimelerin kökenini tek tek verir.

**Nasıl kullanılır:** Arşiv açık erişim. Stachowski: https://altaica.ru/LIBRARY/turks/Stachowski_Dolganischer%20Wortschatz%201993.PDF

- **Diller:** bütün diller
- **İşe yaradığı yer:** Ödünç ve miras ayrımı (özellikle Çuvaşça), Makaleler ve bibliyografya
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** aramada görüldü · **Ortam:** izinsiz (ejournals.eu)
- **Doğrulama:** 2026-11-12: ejournals.eu izinli değil; Stachowski PDF'i altaica'dan açıldı (HTTP 206).
- **Kimlik:** `studia-etymologica-cracoviensia`

<a id="tdk-belleten"></a>
#### Türk Dili Araştırmaları Yıllığı — Belleten

<https://tdkbelleten.gov.tr>

TDK'nin hakemli, açık erişimli Türkoloji dergisi.

**Nasıl kullanılır:** Tam metin PDF'ler.

- **Diller:** bütün diller
- **İşe yaradığı yer:** Makaleler ve bibliyografya
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** aramada görüldü · **Ortam:** izinsiz (tdkbelleten.gov.tr)
- **Kimlik:** `tdk-belleten`

<a id="turklad"></a>
#### Uluslararası Türk Lehçe Araştırmaları Dergisi (TÜRKLAD)

<https://dergipark.org.tr/en/pub/turklad>

Türk lehçeleri ve ağızları üzerine hakemli, açık erişimli dergi (2017'den beri, CC BY-NC 4.0).

**Nasıl kullanılır:** DergiPark'ta arama.

- **Diller:** bütün diller
- **İşe yaradığı yer:** Makaleler ve bibliyografya, Ağız verisi
- **Erişim:** açık · **Biçim:** pdf · **Güven:** yüksek · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: açıldı (HTTP 200).
- **Kimlik:** `turklad`

<a id="dergipark"></a>
#### DergiPark

<https://dergipark.org.tr>

Türkiye'deki akademik dergilerin ortak platformu; ağız ve lehçe çalışmalarının çoğu burada.

**Nasıl kullanılır:** Kelime + ağız/lehçe adıyla arama (ör. "Ahıska ağzı sözlük").

- **Diller:** bütün diller
- **İşe yaradığı yer:** Makaleler ve bibliyografya, Ağız verisi, Yaşayan dillerde biçim toplama
- **Erişim:** açık · **Biçim:** pdf · **Güven:** orta · **Durum:** bu ortamdan açıldı · **Ortam:** izinli
- **Doğrulama:** 2026-11-12: açıldı (HTTP 200). Makale PDF'leri dergipark.org.tr/tr/download/article-file/<no> biçiminde doğrudan inebiliyor.
- **Kimlik:** `dergipark`

<a id="tuva-dergi"></a>
#### Novye issledovaniya Tuvy (Tuva üzerine yeni araştırmalar) dergisi

<https://nit.tuva.asia>

Tuvaca, Tuvaca ağızları (Moğolistan, Çin Tuvaları) ve Tofaca üzerine açık erişimli makaleler.

**Nasıl kullanılır:** Makale PDF'leri nit.tuva.asia/nit/article/download/<no>.

- **Diller:** Tuvaca, Tofaca, Duhaca (Tsaatan), Soyotça
- **İşe yaradığı yer:** Makaleler ve bibliyografya, Ağız verisi, Konuşur sayısı ve canlılık
- **Erişim:** açık · **Biçim:** pdf · **Güven:** orta · **Durum:** aramada görüldü · **Ortam:** izinsiz (nit.tuva.asia)
- **Kimlik:** `tuva-dergi`

### Araçlar

<a id="turkicnlp"></a>
#### TurkicNLP — Türk dilleri için doğal dil işleme araç takımı

<https://arxiv.org/html/2602.19174>

Türk dilleri için ortak araçlar: yazı çevirme (Kiril, Arap, Latin), biçimbirim çözümleme ve kaynak listesi (2026).

**Nasıl kullanılır:** Kiril ve Arap yazısındaki biçimleri çalışma yazımına aktarmak için yardımcı olabilir.

- **Diller:** bütün diller
- **İşe yaradığı yer:** Toplu, makinece okunabilir veri, Ortak alfabe ve yazım
- **Erişim:** açık · **Biçim:** git · **Güven:** orta · **Durum:** aramada görüldü · **Ortam:** izinsiz (arxiv.org)
- **Kimlik:** `turkicnlp`

<a id="bu-ortamdan-erisim"></a>
## Bu ortamdan erişim

Bu oturumun ortamında (**dil**) yalnızca şu adreslere izin var: `aclanthology.org`, `altaica.c4.starlingdb.org`, `altaica.ru`, `archive.org`, `asjp.clld.org`, `bitig.kz`, `concepticon.clld.org`, `dergipark.org.tr`, `directory.doabooks.org`, `en.wiktionary.org`, `github.com`, `glottolog.org`, `kaikki.org`, `lexibank.clld.org`, `library.oapen.org`, `raw.githubusercontent.com`, `sozluk.gov.tr`, `starling.rinet.ru`, `starlingdb.org`, `turkic.elegantlexicon.com`, `univerlag.uni-goettingen.de`, `www.nisanyansozluk.com`, `zenodo.org`.

Çevrim içi kaynakların ihtiyaç duyduğu, henüz izinli olmayan adresler (kaç kaynağın kullandığına göre). Bir kaynağı kullanmak gerektiğinde ilgili adres ortama eklenir.

| Adres | Kaynak sayısı | Kaynaklar |
|---|---:|---|
| `www.freelang.net` | 2 | `freelang`, `gagavuzca` |
| `en.wikipedia.org` | 2 | `wikipedia-turk-dilleri`, `ortak-turk-alfabesi` |
| `dev.panlex.org` | 1 | `panlex` |
| `openaccess.artvin.edu.tr` | 1 | `wold-halac` |
| `sino-platonic.org` | 1 | `proto-turkic-unsuzler` |
| `www.tnc.org.tr` | 1 | `tnc` |
| `multicast.aspra.uni-bamberg.de` | 1 | `wowa` |
| `www.degruyterbrill.com` | 1 | `boeschoten` |
| `opendata.uni-halle.de` | 1 | `codex-cumanicus` |
| `akvius-website.pages.dev` | 1 | `akvius-cagatayca` |
| `www.lexilogos.com` | 1 | `lexilogos` |
| `sozdik.kz` | 1 | `sozdik` |
| `qazcorpus.kz` | 1 | `qazcorpus` |
| `el-sozduk.kg` | 1 | `el-sozduk` |
| `tugantel.tatar` | 1 | `tugan-tel` |
| `sakhatyla.ru` | 1 | `sakhatyla` |
| `ctcorpus.org` | 1 | `kirim-tatar-derlem` |
| `www.karaim.eu` | 1 | `karay-sozluk` |
| `tuvan.swarthmore.edu` | 1 | `tuva-sozluk` |
| `www.webonary.org` | 1 | `turkmen-sozluk` |
| `ctild.indiana.edu` | 1 | `ozbek-kaynaklari` |
| `dobes.mpi.nl` | 1 | `salarca` |
| `eldp.access.preservica.com` | 1 | `elar` |
| `www.atlaskmns.ru` | 1 | `atlaskmns` |
| `lingsib.iea.ras.ru` | 1 | `lingsib` |
| `www.altaist.org` | 1 | `rf-turk-agiz-atlasi` |
| `www.endangeredlanguages.com` | 1 | `elp` |
| `www.routledge.com` | 1 | `johanson-csato` |
| `grambank.clld.org` | 1 | `grambank` |
| `en.wal.unesco.org` | 1 | `unesco-wal` |
| `rosstat.gov.ru` | 1 | `rosstat-2021` |
| `www.ethnologue.com` | 1 | `ethnologue` |
| `joshuaproject.net` | 1 | `joshua-project` |
| `www.tandfonline.com` | 1 | `salehi-2017` |
| `www.academia.edu` | 1 | `en-sik-1000` |
| `wortschatz.uni-leipzig.de` | 1 | `leipzig-corpora` |
| `www.sketchengine.eu` | 1 | `sketch-engine-turk` |
| `www.dailysabah.com` | 1 | `qamus` |
| `turkicacademy.org` | 1 | `turk-akademisi-terim` |
| `tdkbelleten.gov.tr` | 1 | `tdk-belleten` |
| `turkbv.aa-ken.jp` | 1 | `turkbv` |
| `www.lehceler.com` | 1 | `lehceler-com` |
| `www.antat.ru` | 1 | `tatar-akademi-sozluk` |
| `huggingface.co` | 1 | `tatar-sozluk-veri` |
| `www.corpus.tatar` | 1 | `tatar-derlem` |
| `ru.translate.chv.su` | 1 | `cuvasca-ceviri` |
| `til.im` | 1 | `kumuk-kaynaklari` |
| `philology.nsc.ru` | 1 | `nsc-filoloji` |
| `nit.tuva.asia` | 1 | `tuva-dergi` |
| `elib.utmn.ru` | 1 | `sibirya-tatar-agiz` |
| `files.preslib.az` | 1 | `sovet-turkologiya` |
| `dilcilik.az` | 1 | `azerbaycan-kaynaklari` |
| `search.worldcat.org` | 1 | `kazak-15-cilt` |
| `uza.uz` | 1 | `ozbek-izohli` |
| `iranatlas.net` | 1 | `iran-dil-atlasi` |
| `turfan.bbaw.de` | 1 | `turfan-bbaw` |
| `orient-kohd.dl.uni-leipzig.de` | 1 | `kohd-eski-uygurca` |
| `adw.d.sub.uni-goettingen.de` | 1 | `gottingen-altuygur` |
| `clics.clld.org` | 1 | `robbeets-2021` |
| `arxiv.org` | 1 | `turkicnlp` |
| `acikbilim.yok.gov.tr` | 1 | `yok-acik-bilim` |
| `online-resources.aa-ken.jp` | 1 | `ilcaa-kaynaklari` |
| `otdo.aa-ken.jp` | 1 | `tibet-kaynaklari` |
| `vatec2.fkidg1.uni-frankfurt.de` | 1 | `vatec` |
| `iris.unive.it` | 1 | `karamanlica` |
| `ejournals.eu` | 1 | `studia-etymologica-cracoviensia` |
| `www.ardahan.edu.tr` | 1 | `kore-ask-real` |

