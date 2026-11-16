// The site writes some Persian words one way only (tools/fa_spelling.py, keep the two lists alike).
// A reader may type another spelling: the search box changes it to the site's spelling as they type,
// before the search runs, so «کلودفلر» finds the pages that write «کلادفلر».
(function () {
  var B = "(^|[^؀-ۿ‌])";
  var RULES = [
    ["کلودفلر|کلود فلر|کلاودفلر|کلود‌فلر", "کلادفلر"],
    ["ریالیتی|ریلیتی|رئالیتی", "ریالتی"],
    ["پراکسی", "پروکسی"],
    ["هایدیفای", "هیدیفای"],
    ["هیدیفای منیجر", "هیدیفای‌منیجر"],
    ["بروزرسانی|به روز رسانی|به‌روز رسانی|به روزرسانی", "به‌روزرسانی"],
    ["نرم افزار", "نرم‌افزار"],
    ["آیپی|آی پی|ایپی", "آی‌پی"],
    ["تانل", "تونل"],
    ["ورکرز", "ورکر"],
    // search only (not a site spelling): the search has no Persian plural, so «ویدیوهای» would not find «ویدیو»
    ["ویدیوهای|ویدیوها|ویدئوهای|ویدئوها|ویدئو", "ویدیو"]
  ].map(function (r) { return [new RegExp(B + "(?:" + r[0] + ")", "g"), "$1" + r[1]]; });

  document.addEventListener("input", function (e) {
    var el = e.target;
    if (!el || !el.matches || !el.matches(".md-search__input")) return;
    var v = el.value, w = v;
    RULES.forEach(function (r) { w = w.replace(r[0], r[1]); });
    if (w !== v) {
      var end = el.selectionEnd === v.length;
      el.value = w;
      if (end) el.setSelectionRange(w.length, w.length);
    }
  }, true);   // capture: runs before the search reads the box
})();
