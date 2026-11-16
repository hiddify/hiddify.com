// Guide pages (docs/manager, docs/app), built by tools/guide_page.py.
(function () {
  // ---- "New" / "Updated" badges ---------------------------------------------------------------
  // Each article link has data-k (its path), data-n (date added) and data-u (date of its last real
  // update). The browser remembers, in localStorage (it is never sent to the server), which version
  // of each article this reader has been shown:
  // - a version the reader has not been shown gets a badge: for a returning reader, every article
  //   added or updated since their last visit, however long ago that was; for a first visit, the
  //   ones from the last FIRST_VISIT_DAYS days;
  // - once shown, the badge stays for SHOW_DAYS days, or until the reader opens the article;
  // - the article gets a badge again only when it is updated again.
  var KEY = "hiddify-guide-seen", FIRST_VISIT_DAYS = 60, SHOW_DAYS = 3, DAY = 864e5;

  function load() {
    try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) { return {}; }
  }
  function save(st) {
    try { localStorage.setItem(KEY, JSON.stringify(st)); } catch (e) { /* private mode: no badges kept */ }
  }

  function badges() {
    var root = document.querySelector(".hg");
    if (!root || root.dataset.badges) return;
    root.dataset.badges = "1";
    var st = load(), now = Date.now(), today = new Date(now).toISOString().slice(0, 10);
    st.seen = st.seen || {};
    var since = st.last || new Date(now - FIRST_VISIT_DAYS * DAY).toISOString().slice(0, 10);
    root.querySelectorAll("a[data-k]").forEach(function (a) {
      var k = a.dataset.k, upd = a.dataset.u && a.dataset.u > a.dataset.n,
          ver = upd ? a.dataset.u : a.dataset.n, s = st.seen[k], show = false;
      if (s && s.v === ver) {
        show = !s.o && now - s.t < SHOW_DAYS * DAY;            // already shown: a few days, until opened
      } else if (ver > since || (s && s.v < ver)) {
        show = true;                                            // a version this reader has not been shown
        st.seen[k] = { v: ver, t: now };
      }
      if (!show) return;
      var b = document.createElement("span");
      b.className = upd ? "hg-badge hg-upd" : "hg-badge hg-new";
      b.textContent = upd ? root.dataset.lUpd : root.dataset.lNew;
      b.title = ver;
      a.after(b);
      a.addEventListener("click", function () {
        var cur = load(); cur.seen = cur.seen || {};
        cur.seen[k] = { v: ver, t: now, o: 1 }; save(cur);
      });
    });
    st.last = today;
    // forget articles that were last shown more than two years ago
    Object.keys(st.seen).forEach(function (k) { if (now - st.seen[k].t > 730 * DAY) delete st.seen[k]; });
    save(st);
  }

  // ---- video rows: the arrows scroll by one screen -------------------------------------------
  function arrows() {
    document.querySelectorAll(".hg-videos").forEach(function (box) {
      var row = box.querySelector(".hg-vrow");
      if (!row || box.dataset.ready) return;
      box.dataset.ready = "1";
      var rtl = getComputedStyle(row).direction === "rtl";
      function step(dir) { row.scrollBy({ left: dir * row.clientWidth * 0.9 * (rtl ? -1 : 1), behavior: "smooth" }); }
      function update() {
        var max = row.scrollWidth - row.clientWidth, pos = Math.abs(row.scrollLeft);
        box.classList.toggle("hg-noscroll", max < 4);
        box.querySelector(".hg-prev").disabled = pos < 4;
        box.querySelector(".hg-next").disabled = pos > max - 4;
      }
      box.querySelector(".hg-prev").addEventListener("click", function () { step(-1); });
      box.querySelector(".hg-next").addEventListener("click", function () { step(1); });
      row.addEventListener("scroll", update, { passive: true });
      window.addEventListener("resize", update);
      update();
    });
  }

  // ---- opened from search (#video-<id>): bring that video into view and make it pulse --------
  function target() {
    // #video-<id> (link to the heading) or ?v=<id> (a video result in the search)
    var h = decodeURIComponent(location.hash || ""), v = new URLSearchParams(location.search).get("v");
    var key = h.indexOf("#video-") === 0 ? h.slice(1) : (v ? "video-" + v : "");
    if (!key) return;
    var t = document.getElementById(key);
    var card = t && t.closest(".hg-v");
    if (!card) return;
    var d = card.closest("details");
    if (d) d.open = true;
    // after the theme's own jump to the anchor: centre the card in its row, then in the window
    setTimeout(function () {
      var row = card.closest(".hg-vrow");
      if (row) {
        var cr = card.getBoundingClientRect(), rr = row.getBoundingClientRect();
        row.style.scrollSnapType = "none";
        row.scrollLeft += (cr.left + cr.width / 2) - (rr.left + rr.width / 2);
        setTimeout(function () { row.style.scrollSnapType = ""; }, 400);
      }
      var r = card.getBoundingClientRect();
      window.scrollTo(0, r.top + window.scrollY - Math.max(70, (window.innerHeight - r.height) / 2));
      card.classList.remove("hg-v-target"); void card.offsetWidth; card.classList.add("hg-v-target");
    }, 700);
  }

  function init() { badges(); arrows(); target(); }
  window.addEventListener("hashchange", target);
  if (window.document$) document$.subscribe(init); else document.addEventListener("DOMContentLoaded", init);
})();
