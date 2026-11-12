// Bitig — tema düğmesi ve tarayıcıda arama (varlik/arama.json).
(function () {
  var kok = document.getElementById('ara').dataset.kok || '';

  // tema: sistem tercihi + elle seçim (localStorage, yoksa da çalışır)
  document.querySelector('.tema').addEventListener('click', function () {
    var el = document.documentElement;
    var koyu = el.dataset.theme ? el.dataset.theme === 'dark'
      : window.matchMedia('(prefers-color-scheme: dark)').matches;
    el.dataset.theme = koyu ? 'light' : 'dark';
    try { localStorage.setItem('bitig-tema', el.dataset.theme); } catch (e) {}
  });

  // arama
  var girdi = document.getElementById('ara');
  var liste = document.getElementById('ara-sonuc');
  var veri = null, secili = -1;
  var TURLER = { kavram: 'kavram', kok: 'kök', kaynak: 'kaynak', dil: 'dil' };
  var ONCELIK = { kavram: 0, kok: 1, dil: 2, kaynak: 3 };

  function katla(s) {
    return (s || '').toLocaleLowerCase('tr')
      .replace(/[çc]/g, 'c').replace(/[ğg]/g, 'g').replace(/[ıi̇i]/g, 'i').replace(/[öo]/g, 'o')
      .replace(/[şs]/g, 's').replace(/[üu]/g, 'u').replace(/[äəe]/g, 'e').replace(/[âa]/g, 'a')
      .normalize('NFD').replace(/[̀-ͯ]/g, '');
  }
  function yukle() {
    if (veri) return Promise.resolve(veri);
    return fetch(kok + 'varlik/arama.json').then(function (r) { return r.json(); }).then(function (d) {
      veri = d.map(function (a) {
        a._ad = katla(a.ad); a._diger = katla([a.alt, a.ozet].concat(a.anahtar || []).join(' '));
        return a;
      });
      return veri;
    });
  }
  // küçük puan önce: tam ad, tam biçim, ad başı, adın içi, öteki alanlar; eşitlikte kavram > kök > dil > kaynak
  function puan(a, q) {
    var p = -1;
    if (a._ad === q) p = 0;
    else if ((a.anahtar || []).some(function (k) { return katla(k) === q; })) p = 1;
    else if (a._ad.indexOf(q) === 0) p = 2;
    else if (a._ad.indexOf(q) >= 0) p = 3;
    else if (a._diger.indexOf(q) >= 0) p = 4;
    return p < 0 ? -1 : p * 10 + ONCELIK[a.t];
  }
  function esc(s) {
    return String(s || '').replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; });
  }
  function goster(sonuc) {
    secili = -1;
    if (!sonuc.length) { liste.innerHTML = '<li><a>Sonuç yok</a></li>'; liste.hidden = false; return; }
    liste.innerHTML = sonuc.map(function (a, i) {
      return '<li role="option" id="s' + i + '"><a href="' + esc(kok + a.yol) + '"><span class="t">' + TURLER[a.t] +
        '</span><b>' + esc(a.ad) + '</b>' + (a.alt ? ' <span>· ' + esc(a.alt) + '</span>' : '') +
        '<small>' + esc(a.ozet) + '</small></a></li>';
    }).join('');
    liste.hidden = false;
  }
  girdi.addEventListener('input', function () {
    var q = katla(girdi.value.trim());
    if (q.length < 2) { liste.hidden = true; return; }
    yukle().then(function (d) {
      var s = d.map(function (a) { return [puan(a, q), a]; })
        .filter(function (x) { return x[0] >= 0; })
        .sort(function (x, y) { return x[0] - y[0]; })
        .slice(0, 12).map(function (x) { return x[1]; });
      goster(s);
    });
  });
  girdi.addEventListener('keydown', function (e) {
    var ogeler = liste.querySelectorAll('li[role=option]');
    if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
      e.preventDefault();
      if (!ogeler.length) return;
      secili = (secili + (e.key === 'ArrowDown' ? 1 : -1) + ogeler.length) % ogeler.length;
      ogeler.forEach(function (o, i) { o.setAttribute('aria-selected', i === secili); });
    } else if (e.key === 'Enter') {
      var o = ogeler[secili < 0 ? 0 : secili];
      if (o && o.querySelector('a')) window.location = o.querySelector('a').href;
    } else if (e.key === 'Escape') {
      liste.hidden = true;
    }
  });
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.ara')) liste.hidden = true;
  });
})();
