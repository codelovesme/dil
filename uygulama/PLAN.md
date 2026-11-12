# Uygulama planı: dil, ayrı çalışan Euglena uygulamaları olarak

Bu belge projeyi (ortak Türk dili, dört hedef, kaynak sözlüğü, tanıklı sözlük) bir
**Linux servisi** olarak açmanın planıdır. Henüz kod yok; aşamalar en altta.

## 1. Amaç

- Bugün proje bir git deposu: YAML veriler ve Python araçları. Okumak için dosya
  açmak, hesap için komut çalıştırmak gerekiyor.
- Hedef: tarayıcıdan gezilen, aranan ve düzenlenen bir **uygulama**:
  - kavramlar ve dört hedefin sonucu,
  - kök sayfaları (zaman çizelgesi, diller, ileride harita),
  - kaynak sözlüğü, soy ağacı ve örgü,
  - kapsam panosu,
  - arka planda çalışan işler: kaynak denetimi, PDF indirme ve OCR, yeniden puanlama.
- **Euglena uygulamaları** olarak yazılır (`manifest.json` + `src/*.gene.code`),
  `my-euglena-apps`'teki api/web/worker kalıbıyla.
- Ama **Euglena host'unda tutulmaz**. Her servis kendi kapısını açar: `membrane`
  değil `net_server`. Kendi makinesinde ya da konteynerinde ayrı çalışan bir
  uygulamalar bütünüdür (`euglena init --service` kalıbı; bugünkü örneği
  `todo-worker`).

## 2. Bileşenler

```
               tarayıcı
                  │  https://dil.<alan>/
           ┌──────▼──────┐
           │  kapı (Caddy)│  web/ dosyalarını sunar, /api/<servis> → servis
           └──┬───────┬──┘
     /api/dil │       │ /api/is
     ┌────────▼──┐ ┌──▼─────────┐
     │  dil-api  │ │ dil-worker │  zamanlayıcı + iş kuyruğu
     │ net_server│ │ net_server │  process → python3 araclar/*.py, tesseract
     └──┬─────┬──┘ └──┬──────┬──┘
        │     │       │      │
   ┌────▼─┐ ┌─▼───────▼─┐  ┌─▼─────────────┐
   │MongoDB│ │ Blob depo │  │ dil deposu     │
   │  dil  │ │ (Azurite/ │  │ (git checkout: │
   └───────┘ │  Azure)   │  │ YAML + Python) │
             └───────────┘  └───────────────┘
```

| Uygulama | Tür | Organeller | Görevi |
|---|---|---|---|
| **dil-web** | `runtime: web` (wasm) | `dom`, `net_client` (api, is), `storage`, `router`, `timer`, `json`, `strings`, `arrays`; genler `palette`, `outbox` | Bütün ekranlar. Tek wasm modülü (`cart-web` kalıbı) |
| **dil-api** | native, kendi portunda | `net_server`, `mongodb`, `azure_blob`, `jwt`, `json`, `strings`, `arrays`, `math`, `time`, `env`, `console` | Okuma ve düzenleme. Mongo'daki hazır sonuçları sunar, düzenlemeleri kaydeder, işleri kuyruğa yazar |
| **dil-worker** | native, kendi portunda | `net_server`, `timer`, `mongodb`, `azure_blob`, `process`, `fs`, `git`, `http_client`, `json`, `strings`, `arrays`, `env`, `console` | İçe aktarma, puanlama, sözlük sayfaları, kaynak denetimi, PDF indirme, OCR, dışa aktarma |
| **kapı** | Caddy (ya da nginx) | — | Tek origin: `web/` + `/api/dil` → dil-api, `/api/is` → dil-worker |
| **MongoDB** | `external-services`'teki mevcut Mongo ya da compose'daki | — | `dil` veritabanı |
| **Blob depo** | Azurite (yerel), sonra Azure Blob | — | PDF'ler, OCR metinleri, üretilen sayfalar, dışa aktarımlar |

Host'ta tutulmadığı için şunlar bizim işimiz olur:

- kapı (Caddy),
- servislerin kendi `console` günlükleri,
- kendi süreç yönetimi (systemd ya da docker).

Manifestte `"hosted": "membrane"` stand-in'i tanımlarsak, ileride istenirse aynı
yapı host'a da alınabilir. Kapı organelin arkasında kalır; genler değişmez.

## 3. Hesaplama motoru: Python kalır, worker onu çağırır

Puanlama (`puanla.py`, ~900 satır) ve sözlük (`sozluk.py`) Python'da ve sık
değişiyor. Bunları baştan Code diline taşımak işin en riskli kısmı olur. Bu yüzden:

- **Aşama 1-3:** Worker, `process` organeliyle depo kopyasındaki Python
  araçlarını çalıştırır ve **JSON** çıktısını Mongo'ya yazar. Araçlara `--json`
  çıktısı eklenir. Yeni bir hesap yazılmaz; aynı kod hem komut satırında hem
  serviste çalışır.
- **Aşama 5 (isteğe bağlı):** Kurallar oturunca puanlama Code'a taşınır
  (`dil-motor` geni). O zamana kadar Python çıktısı Code çıktısının sınavı
  (fixture) olur.

API hesap yapmaz; worker'ın yazdığı hazır sonucu sunar. Bu yüzden hızlıdır ve
Python'un yavaşlığı kullanıcıya yansımaz.

## 4. Verinin asıl kaynağı: git mi, Mongo mu?

| | A: git asıl, Mongo okuma modeli (önerilen başlangıç) | B: Mongo asıl, git dışa aktarım |
|---|---|---|
| Düzenleme | Depoda (ben ya da sen), worker içe aktarır | Arayüzden; worker YAML'a döker ve commit eder |
| Geçmiş | git | Mongo'da sürümler + git yedeği (`backuper` kalıbı) |
| Risk | Arayüz yalnız okur | İki yönlü uyuşmazlık |

Önerim aşamalı:

- **Aşama 1-2:** A. Uygulama okur; veri bugünkü gibi depoda değişir.
- **Aşama 4:** Arayüzden düzenleme açılır. Bir düzenleme önce Mongo'daki
  `oneriler` koleksiyonuna düşer. Onaylanınca worker YAML'ı günceller,
  doğrulama araçlarını (`sozluk.py --denetle`, `kaynaklar.py`) çalıştırır,
  geçerse commit eder ve yeniden içe aktarır. Böylece git asıl kalır ve her
  değişiklik aynı denetimlerden geçer.

## 5. Veri modeli (MongoDB, veritabanı `dil`)

| Koleksiyon | Kaynak | İçerik |
|---|---|---|
| `diller` | `agac.yaml` | Düğümler: kod, ad, üst, tür (kol/dal/dil/ağız), konuşur, not |
| `baglar` | `ag.yaml` | Örgü: anlaşılırlık, ikinci dil, temas |
| `tanik_turleri` | `tarihi.yaml` | Tarihî tanık kodları, dönem, ağırlık |
| `hedefler` | `hedefler.yaml` | Dört hedefin ayarları ve sözlük durakları |
| `kaynaklar` | `kaynaklar/kaynaklar.yaml` | 168 kaynak, doğrulama ve yüzyıl alanlarıyla |
| `kavramlar` | `sozluk/temel/*.yaml` | Kavram, aday kökler, günlük biçimler |
| `kokler` | `sozluk/kok/*.yaml` | Sözlük maddesi ve bütün tanıklar |
| `sonuclar` | `puanla.py --json` | Kavram × hedef: seçim, alttan yukarı ağaç, adayların ölçüleri |
| `kapsam` | `sozluk.py --json` | Kök başına seviye, eksik duraklar ve diller |
| `isler` | worker | İş kuyruğu: tür, durum, girdi, çıktı, günlük, zaman |
| `dosyalar` | worker | Blob kayıtları: kaynak kimliği, adres, sha256, boyut, OCR durumu |
| `oneriler` | api (Aşama 4) | Arayüzden gelen düzenleme önerileri ve onay durumu |
| `ice_aktarimlar` | worker | Hangi git commit'inin içe aktarıldığı |

İçe aktarma tamdır ve tek bir işlemde yapılır: bir commit'in bütün verisi ya
yazılır ya hiç yazılmaz. `ice_aktarimlar` son geçerli commit'i tutar.

## 6. Blob depo

| Konteyner | İçerik |
|---|---|
| `kaynak-dosyalari` | İndirilen PDF ve DJVU dosyaları (altaica.ru vb.), sha256 adıyla |
| `ocr` | Sayfa sayfa OCR metinleri (tesseract tur/rus/eng) |
| `sayfalar` | Üretilen Markdown/HTML sözlük sayfaları, dışa aktarımlar |

Bir PDF bir kez indirilir; aynı dosya için yeniden indirme olmaz. Telif durumu
belirsiz kopyalar **yalnız iç kullanım** içindir: arayüz bunları herkese
sunmaz, yalnız künye ve özgün adresi gösterir.

## 7. API (dil-api)

Euglena kalıbı: `POST /api/dil` ile `{"_class": "...", …}` parçacıkları.

| Parçacık | Ne döner |
|---|---|
| `Ozet` | Sayılar: kavram, kök, tanık, kaynak; son içe aktarma |
| `Kavramlar { filtre }` / `Kavram { ad }` | Liste; tek kavram: dört hedefin seçimi, adaylar, alttan yukarı ağaç |
| `Kokler { filtre }` / `Kok { kok }` | Liste; tek madde: tanıklar (yüzyıla göre), kapsam, kaynakça |
| `Ara { sorgu }` | Kavram, kök, biçim ve kaynaklarda arama |
| `Kaynaklar { ihtiyac, dil }` / `Kaynak { kimlik }` | `kaynaklar.py --ara` karşılığı |
| `Agac` / `Ag` / `Agirliklar { hedef }` | Soy ağacı, örgü ve ağırlık tabloları |
| `Karsilastir` | KARSILASTIRMA.md karşılığı |
| `Kapsam` | SOZLUK.md karşılığı |
| `Oner { tur, veri }` | (Aşama 4, oturum gerekir) düzenleme önerisi |
| `Isler` / `Is { id }` | İşlerin durumu (okuma) |
| `WhatCanIDo` | Mike'ın sorabilmesi için yetenek listesi (`abilities` geni) |

## 8. Worker (dil-worker)

| İş | Tetik | Ne yapar |
|---|---|---|
| `IceAktar` | git'te yeni commit (5 dakikada bir `git fetch`) ya da elle | YAML → Mongo; ardından `Puanla` ve `SozlukYaz` |
| `Puanla` | `IceAktar` sonrası | `puanla.py --json` (bütün hedefler) → `sonuclar` |
| `SozlukYaz` | `IceAktar` sonrası | `sozluk.py --json` ve `--denetle` → `kapsam`; sayfalar → blob |
| `KaynakDenetle` | haftalık | Her kaynağın adresini dener, `dogrulama` sonucunu `kaynaklar`'a yazar (bugünkü elle yaptığımız denetim) |
| `Indir { kaynak, url }` | elle | PDF'i indirir → blob, sha256 → `dosyalar` |
| `Ocr { dosya, sayfalar, dil }` | `Indir` sonrası ya da elle | `pdftoppm` + `tesseract` → `ocr` konteyneri |
| `DisaAktar` (Aşama 4) | öneri onaylanınca | Mongo → YAML, denetim, commit, push |

İşler `isler` koleksiyonunda kuyruklanır. Worker kendi `timer`'ıyla sırayla alır,
aynı anda tek ağır iş çalıştırır, her adımın günlüğünü işe yazar.
`POST /api/is` ile `Baslat { tur, girdi }` ve `Durum` kabul eder (yönetici).

## 9. Arayüz (dil-web)

1. **Ana sayfa:** arama kutusu, özet sayılar, son eklenen kelimeler, çalışma
   sırası (`SIRA.md`).
2. **Kavram:** dört hedefin seçimi yan yana; adaylar ve üç ölçü; alttan yukarı
   ağaç (ağız → dil → dal → kol → tepe); dil tablosu (alıntılar işaretli);
   canlandırma uyarıları.
3. **Kök (sözlük maddesi):** zaman çizelgesi (yüzyıl ekseni), yabancı kayıtlar 🌍,
   yaşayan diller ve ağızlar, kapsam rozeti (Seviye 0-3), kaynakça. İleride
   yüzyıl kaydırıcılı harita (Glottolog koordinatları).
4. **Diller:** soy ağacı ve örgü görselleştirmesi, ağırlık tabloları.
5. **Kaynaklar:** ihtiyaca ve dile göre süzülebilen kaynak sözlüğü, doğrulama durumu.
6. **Karşılaştırma** ve **Kapsam panosu.**
7. **Yönetim** (oturumla): işler, öneriler ve onay, indirilen dosyalar.

## 10. Kimlik

Okuma herkese açıktır. Yazma (öneri, onay, iş başlatma) oturum ister. İki yol:

- **(a) Mevcut `auth`'u kullanmak (önerilen).** `dil-api` ve `dil-worker`,
  `JWT_PUBLIC_KEY` ile `auth`'un jetonunu doğrular, imzalayamaz. Ayrı çalışsa
  da kimlik tek kalır. `auth`'ta bir uygulama kaydı ve kurallar yazılır
  (`permissions_dil`).
- **(b) Kendi basit yönetici anahtarı.** `.env`'de bir yönetici jetonu.

## 11. Yapılandırma (`.env.example`)

```
MONGO_URI=mongodb://localhost:27017      DIL_DB_NAME=dil
AZURE_BLOB_CONNECTION_STRING=…            (yerelde Azurite)
DIL_API_HOST=127.0.0.1   DIL_API_PORT=8960
DIL_WORKER_HOST=127.0.0.1 DIL_WORKER_PORT=8961
DIL_REPO_DIR=/srv/dil/repo                (worker'ın git kopyası)
DIL_REPO_REMOTE=https://github.com/codelovesme/dil   DIL_REPO_BRANCH=main
JWT_PUBLIC_KEY=…                          (auth'un açık anahtarı)
DIL_API_URL=/api/dil   DIL_WORKER_URL=/api/is   (dil-web, tek origin)
```

Portlar mevcut düzenle çakışmaz: host 8899, web kabuğu 8923, todo 8892/8893,
Mongo 27017, LocalAI 8080.

## 12. Dağıtım

- **Derleme:** `euglena build --release`. Native servisler tek ikili dosya olur
  ve modüller içine bağlanır. Web için `euglena build --target wasm -o web/dil-web.wasm`.
- **İki seçenek:**
  - **systemd** (bugünkü `euglena-host` gibi): `dil-api`, `dil-worker`,
    `dil-kapi` kullanıcı birimleri.
  - **docker compose:** `init --service`'in Dockerfile'ı
    (debian:trixie-slim, root olmayan kullanıcı). Worker imajına
    `python3-yaml`, `poppler-utils`, `tesseract-ocr(-tur,-rus)` ve `git` eklenir.
    Compose'da Mongo, Azurite, Caddy ve üç servis yer alır.
- **Yayın:** Cloudflare tüneli → kapı. Bu, `apps.codeloves.me`'deki tek nginx
  kuralından bağımsızdır; ayrı bir alt alan adı olur, ör. `dil.codeloves.me`.

## 13. Depo yerleşimi

```
dil/
  uygulama/
    PLAN.md            bu belge
    dil-api/           manifest.json, src/*.gene.code, tests/, .env.example, Dockerfile
    dil-worker/        manifest.json, src/*.gene.code, tests/, .env.example, Dockerfile
    dil-web/           manifest.json, src/*.gene.code, web/, tests/
    kapi/Caddyfile
    compose.yaml
    systemd/*.service
  araclar/             Python motoru (+ --json çıktıları)
```

Uygulamalar verinin yanında, `dil` deposunda durur, çünkü worker aynı depoyu
çalıştırır. `my-euglena-apps`'in kurallarına (AGENTS.md) uyulur, ama oraya
taşınmaz.

## 14. Aşamalar

| Aşama | Teslim | Bitti sayılması için |
|---|---|---|
| **0. Hazırlık** | Python araçlarına `--json` (puanla: kavram × hedef × ağaç; sozluk: madde + kapsam; kaynaklar: liste). İçe aktarma şeması (`uygulama/sema.md`) | JSON çıktıları test edilmiş, şema yazılmış |
| **1. Okuma çekirdeği** | dil-worker `IceAktar` + `Puanla` + `SozlukYaz`; dil-api okuma parçacıkları; Mongo; fixture'lar | `curl` ile `Kavram {ad:"ben"}` dört hedefi döndürüyor |
| **2. Arayüz** | dil-web: ana sayfa, kavram, kök, kaynaklar, arama; kapı; yerelde compose | Tarayıcıda "ben" sayfası, zaman çizelgesiyle |
| **3. İşler ve dosyalar** | `KaynakDenetle`, `Indir`, `Ocr`; blob; yönetim ekranı (okuma) | Bir altaica PDF'i indirilip OCR'lanıyor, metni aranabiliyor |
| **4. Düzenleme** | Kimlik (auth jetonu), `oneriler`, onay, `DisaAktar` (YAML + denetim + commit) | Arayüzden eklenen bir tanık denetimlerden geçip commit oluyor |
| **5. Yayın ve olgunlaşma** | systemd/compose ile sunucuya kurulum, Cloudflare tüneli, yedek (`backuper`'a `dil` veritabanı), isteğe bağlı: puanlamanın Code'a taşınması, harita | `dil.<alan>` açık, gece yedeği alınıyor |

## 15. Riskler ve açık sorular

- **Code/Euglena araç zinciri bu bulut ortamında yok.** Yazmak burada
  yapılabilir, ama derleme ve test için `cdlvsm install code euglena` gerekir
  (GitHub sürüm dosyaları). Ağ izni gerekebilir; olmazsa derleme senin
  makinende yapılır.
- **`process` ile Python çağırmak** worker imajına Python koyar. Kabul edilebilir;
  Aşama 5'te kaldırılabilir.
- **Telif durumu belirsiz PDF'ler** yalnız iç kullanım içindir; herkese açık
  sunulmaz.
- **Karar bekleyenler:** kimlik yolu (a/b), dağıtım (systemd ya da compose),
  alan adı, Mongo (mevcut `external-services` mi, ayrı mı), Azure Blob mu yoksa
  şimdilik Azurite mi.
