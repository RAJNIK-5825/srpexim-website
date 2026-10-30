/* SRP Exim - small helper script (menu + quotation form) */
(function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  var form = document.getElementById('quote-form');
  if (!form) return;
  var status = document.getElementById('form-status');
  var EMAIL = 'srpexim2025@gmail.com';

  function show(kind, text) {
    status.className = 'status show ' + kind;
    status.textContent = text;
  }

  function mailtoLink() {
    var d = new FormData(form);
    var lines = [];
    form.querySelectorAll('[name]').forEach(function (el) {
      if (el.name.charAt(0) === '_' || !el.labels || !el.labels[0]) return;
      var label = el.labels[0].textContent.replace('*', '').trim();
      lines.push(label + ': ' + (d.get(el.name) || ''));
    });
    var subject = 'Quotation request - SRP Exim website';
    return 'mailto:' + EMAIL + '?subject=' + encodeURIComponent(subject) +
      '&body=' + encodeURIComponent(lines.join('\n'));
  }

  function useMailto() {
    window.location.href = mailtoLink();
    show('ok', form.dataset.mailto);
  }

  document.getElementById('mailto-btn').addEventListener('click', function () {
    if (form.reportValidity()) useMailto();
  });

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var action = form.getAttribute('action') || '';
    // FORMSPREE_ID not filled in yet -> use the email fallback
    if (action.indexOf('FORMSPREE_ID') !== -1) { useMailto(); return; }
    var btn = form.querySelector('button[type=submit]');
    btn.disabled = true;
    fetch(action, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } })
      .then(function (r) {
        if (!r.ok) throw new Error('bad status');
        form.reset();
        show('ok', form.dataset.ok);
      })
      .catch(function () {
        show('err', form.dataset.err);
        window.location.href = mailtoLink();
      })
      .then(function () { btn.disabled = false; });
  });
})();
