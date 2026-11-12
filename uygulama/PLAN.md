# Uygulama planı: bitig.codeloves.me

Projeyi (ortak Türk dili, dört hedef, kaynak sözlüğü, tanıklı sözlük) herkese açık
bir web sitesi olarak yayınlama planı. Henüz kod yok; aşamalar en altta.

## 1. Kararlar (2026-11-12)

| Konu | Karar |
|---|---|
| Erişim | **Herkese açık, giriş yok.** Site yalnız okur; düzenleme yok |
| Veri | Bu depo (`dil`, yeni adıyla `bitig`) hem kaynak veriyi hem **üretilmiş çıktıları** tutar. Sözlük sayfaları depoda Markdown olarak üretilir; site bunları gösterir |
| Uygulamalar | `my-euglena-apps` altında: `bitig-web`, `bitig-api`, `bitig-worker` |
| Çalışma biçimi | Euglena **host'unda tutulmaz**; her servis kendi `net_server`'ıyla ayrı çalışır |
| Dağıtım | Mevcut docker compose'a (`external-services`) servis girdileri olarak |
| MongoDB | Mevcut Mongo, aynı kimlik bilgileri (`MONGO_URI`) |
| Blob | Azurite (`external-services`, port 10010); ileride Azure Blob tek satır değişikliği |
| Alan adı | `bitig.codeloves.me` |

## 2. Akış

```
 bitig deposu (GitHub)                         my-euglena-apps
 ─────────────────────                         ───────────────
 YAML veri ──python3 araclar/yayinla.py──▶ cikti/ (Markdown + site.json)
                                                 │ git (commit edilir)
                                                 ▼
                                  bitig-worker  ── 5 dk'da bir git fetch
                                     │  yeni commit varsa:
                                     │  cikti/'yı okur → Mongo (sayfalar, arama)
                                     │                 → Azurite (commit'e göre anlık görüntü)
                                     ▼
                                  bitig-api  ── sayfa, gezinti, arama (salt okunur)
                                     ▲
 tarayıcı ── bitig.codeloves.me ── kapı ── bitig-web (wasm: Markdown → sayfa)
```

- **Hesap ve üretim depoda kalır.**
  - Python araçları (puanla, sozluk, kaynaklar) Markdown'ı ve `site.json`'ı
    üretir ve bunlar commit edilir.
  - Servislerde Python yoktur; worker yalnız dosya okur.
  - Depoda görülen ile sitede görülen hep aynıdır.
- **Yayın commit'e bağlıdır.**
  - Worker yeni bir commit'in bütün çıktısını Mongo'ya yazar, sonra tek bir
    işaretçiyi (`yayin.commit`) çevirir.
  - Okuyucu hiçbir zaman yarım yayın görmez.
  - Eski commit'lerin anlık görüntüleri Azurite'te kalır.

## 3. Depoda (bitig) yapılacaklar: çıktılar

`python3 araclar/yayinla.py` tek komutla bütün çıktıyı üretir:

| Çıktı | Bugün | Yapılacak |
|---|---|---|
| `sozluk/kok/<kök>.md` | var (`sozluk.py --yaz`) | — |
| `sozluk/SOZLUK.md` | var | — |
| `sozluk/temel/<kavram>.md` | **yok** | Kavram sayfası: dört hedefin seçimi, adaylar ve ölçüleri, alttan yukarı ağaç, dil tablosu |
| `KARSILASTIRMA.md`, `AGIRLIKLAR.md`, `kaynaklar/KAYNAKLAR.md` | var | — |
| `cikti/site.json` | **yok** | Gezinti, sayfa listesi (yol, başlık, tür, güncelleme), arama dizini (kavram, kök, biçimler, diller, kaynaklar), commit bilgisi |

Ayrıca bir denetim eklenir: `yayinla.py --denetle`, çıktılar eskiyse hata verir.
İleride bir GitHub Actions adımı da aynısını yapabilir. Böylece veri değişip
sayfası yenilenmeyen commit kalmaz.

Markdown sayfaları sitenin içeriğidir. Sayfalar arası bağlantılar göreli
yazılır (`../temel/ben.md`); site bunları kendi yollarına çevirir.

## 4. Uygulamalar (my-euglena-apps)

| Uygulama | Tür | Organeller | Görevi |
|---|---|---|---|
| **bitig-worker** | native, ayrı | `net_server` (sağlık), `timer`, `git`, `fs`, `mongodb`, `azure_blob`, `json`, `strings`, `arrays`, `env`, `console` | Depoyu çeker, `cikti/site.json` ve Markdown'ları Mongo'ya ve Azurite'e yazar, yayını çevirir |
| **bitig-api** | native, ayrı | `net_server`, `mongodb`, `json`, `strings`, `arrays`, `env`, `console` | `Gezinti`, `Sayfa { yol }`, `Ara { sorgu }`, `Ozet`, `Saglik`, `WhatCanIDo` |
| **bitig-web** | `runtime: web` (wasm) | `dom`, `net_client` (api), `router`, `storage`, `timer`, `json`, `strings`, `arrays`; genler `palette` | Markdown'ı sayfaya çevirir; yan gezinti, arama, kök sayfasında zaman çizelgesi düzeni, açık/koyu tema |

Kimlik yok: `jwt` ve `auth` kaydı gerekmez. API yalnız okuma parçacıkları
sunar; yazan tek şey worker'dır ve o da yalnız Mongo'ya yazar.

**Markdown işleme:**
- `docs-api`/`docs-web` bunu eski biçimde (`server.so`/`sap`) yapıyordu.
- Yazıma geçmeden önce güncel Code sürümünde bir `markdown` modülü olup
  olmadığına `organelle-web` kataloğundan bakılır.
  - Varsa worker, Markdown'ı yayın sırasında bir kez sayfa yapısına
    çevirip Mongo'ya yazar.
  - Yoksa bitig-web'de küçük bir gen yazılır: başlıklar, tablolar,
    bağlantılar, listeler ve vurgu yeterlidir.

## 5. Veri (MongoDB, veritabanı `bitig`)

| Koleksiyon | İçerik |
|---|---|
| `yayinlar` | Her içe aktarılan commit: sha, tarih, sayfa sayısı, durum |
| `yayin` | Tek belge: şu an sunulan commit |
| `sayfalar` | `{ commit, yol, baslik, tur, md, (yapı), guncelleme }` |
| `arama` | `{ commit, terim, tur, yol, ozet }`: kavramlar, kökler, biçimler, diller, kaynaklar |
| `gezinti` | `{ commit, agac }` |

Eski commit'lerin belgeleri son N yayından sonra silinir; anlık görüntüleri
Azurite'te kalır.

**Azurite** konteyneri `bitig`: `<commit>/cikti/site.json` ve
`<commit>/<yol>.md`. Bu bir yedektir; Mongo bozulursa yayın oradan yeniden
kurulur.

## 6. Dağıtım

- **İmajlar:**
  - Her native servis için `euglena build --release`; `init --service`
    Dockerfile'ı (debian:trixie-slim, root olmayan kullanıcı, tek ikili).
  - bitig-web için `web/` klasörü (wasm + `host.mjs` + `index.html`).
- **Mevcut compose'a girdiler:** `bitig-api`, `bitig-worker`, `bitig-kapi`.
  - Mongo ve Azurite ile aynı ağda.
  - Mevcut `MONGO_URI` kullanılır; Azurite bağlantı dizesi compose ağındaki
    adla verilir.
- **Kapı (`bitig-kapi`, Caddy):**
  - `web/` klasörünü sunar ve `/api/bitig` isteklerini bitig-api'ye iletir.
  - Tek origin olduğu için tarayıcı tarafında `BITIG_API_URL=/api/bitig`
    kullanılır.
- **Yayın:** Cloudflare tüneli → `bitig.codeloves.me` → `bitig-kapi`. Bu,
  `apps.codeloves.me`'nin host kuralından ayrıdır.
- **Worker'ın depo kopyası:** bir volume'da tutulur. Depo herkese açıksa
  kimlik gerekmez; özel kalacaksa salt okuma bir deploy anahtarı gerekir.

`.env.example` (her servisin yanında):

```
MONGO_URI=mongodb://…            # mevcut
BITIG_DB_NAME=bitig
AZURE_BLOB_CONNECTION_STRING=…   # Azurite
BITIG_BLOB_CONTAINER=bitig
BITIG_REPO_URL=https://github.com/codelovesme/bitig
BITIG_REPO_BRANCH=main
BITIG_REPO_DIR=/data/bitig
BITIG_API_HOST=0.0.0.0  BITIG_API_PORT=8960
BITIG_WORKER_HOST=0.0.0.0 BITIG_WORKER_PORT=8961
BITIG_API_URL=/api/bitig         # bitig-web
```

## 7. Aşamalar

| Aşama | Nerede | Teslim | Bitti sayılması için |
|---|---|---|---|
| **0. Çıktılar** | bitig | `araclar/yayinla.py`, kavram Markdown sayfaları, `cikti/site.json`, `--denetle` | Tek komut bütün çıktıyı üretiyor; denetim eski çıktıyı yakalıyor |
| **1. Worker + API** | my-euglena-apps | bitig-worker (git → Mongo + Azurite, yayın işaretçisi), bitig-api (okuma parçacıkları), fixture'lar | `curl -d '{"_class":"Sayfa","yol":"sozluk/kok/ben"}'` sayfayı döndürüyor |
| **2. Web** | my-euglena-apps | bitig-web: gezinti, sayfa, arama, kök zaman çizelgesi, tema | Gerçek tarayıcıda "ben" kök sayfası ve "ben" kavram sayfası |
| **3. Yayın** | external-services + tünel | Dockerfile'lar, compose girdileri, Caddy, Cloudflare tüneli | `https://bitig.codeloves.me` açık; yeni bir commit 5 dakika içinde sitede |
| **4. Sonra** | ikisi | Yüzyıl kaydırıcılı harita, kapsam panosu grafikleri, kaynak denetim raporu | — |

## 8. Açık noktalar

- **Depo adı.** `dil` → `bitig`. GitHub'da sahibinin yapması gerekir
  (Settings → Rename). Eski adres yönlendirmeye devam eder. Ardından
  belgelerdeki adlar güncellenir.
- **Depo görünürlüğü.** Herkese açıksa worker kimliksiz çeker; özelse deploy
  anahtarı gerekir.
- **Telif.** Altaica'dan okunan PDF'ler sitede sunulmaz; site yalnız künye ve
  özgün adresi gösterir. Depoya PDF konmaz.
- **Araç zinciri.** Code ve Euglena bu bulut ortamında kurulu değil. Uygulamalar
  my-euglena-apps'in AGENTS.md'sindeki gibi senin makinende derlenir; ya da
  ortama sürüm dosyalarına erişim eklenir.
