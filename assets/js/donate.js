/* Donation page: one-tap copy of a wallet address, and show/hide its QR code. */
(function () {
  function fallback(text) {
    var t = document.createElement('textarea');
    t.value = text; t.setAttribute('readonly', ''); t.style.position = 'fixed'; t.style.opacity = '0';
    document.body.appendChild(t); t.select();
    try { document.execCommand('copy'); } finally { document.body.removeChild(t); }
  }
  function copy(text) {
    if (navigator.clipboard && window.isSecureContext)
      return navigator.clipboard.writeText(text).catch(function () { fallback(text); });
    fallback(text);
    return Promise.resolve();
  }
  document.addEventListener('click', function (e) {
    var b = e.target.closest('.hi-dn-cp');
    if (b) {
      var label = b.querySelector('span'), was = b.dataset.was || label.textContent;
      b.dataset.was = was;
      copy(b.dataset.copy).then(function () {
        b.classList.add('ok'); label.textContent = b.dataset.done;
        clearTimeout(b._t); b._t = setTimeout(function () { b.classList.remove('ok'); label.textContent = was; }, 2200);
      });
      return;
    }
    var q = e.target.closest('.hi-dn-qrb');
    if (q) {
      var box = q.closest('.hi-dn-w').querySelector('.hi-dn-qr'), l = q.querySelector('span'), open = box.hidden;
      q.dataset.show = q.dataset.show || l.textContent;
      box.hidden = !open; q.setAttribute('aria-expanded', open ? 'true' : 'false');
      l.textContent = open ? q.dataset.hide : q.dataset.show;
    }
  });
})();
