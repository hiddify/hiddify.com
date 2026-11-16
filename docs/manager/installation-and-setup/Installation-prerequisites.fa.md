---
title: پیش‌نیازهای نصب
weight: -82
---

<div dir="rtl" markdown=1>

# پیش‌نیازهای نصب

قبل از [نصب هیدیفای‌منیجر](/fa/manager/installation-and-setup/guide/) این پنج چیز را آماده کنید. روی هر کدام بزنید تا توضیحش را ببینید.

<div class="hi-grid c5">
<a class="hi-tile" href="#vps"><span class="hi-ic "><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M4 1h16a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1m0 8h16a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1v-4a1 1 0 0 1 1-1m0 8h16a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1v-4a1 1 0 0 1 1-1M9 5h1V3H9v2m0 8h1v-2H9v2m0 8h1v-2H9v2M5 3v2h2V3H5m0 8v2h2v-2H5m0 8v2h2v-2H5Z"/></svg></span><span class="n">۱</span><b>سرور مجازی</b><small>یک VPS اجاره‌ای</small></a>
<a class="hi-tile" href="#resources"><span class="hi-ic green"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M17 17H7V7h10m4 4V9h-2V7a2 2 0 0 0-2-2h-2V3h-2v2h-2V3H9v2H7c-1.11 0-2 .89-2 2v2H3v2h2v2H3v2h2v2a2 2 0 0 0 2 2h2v2h2v-2h2v2h2v-2h2a2 2 0 0 0 2-2v-2h2v-2h-2v-2m-6 2h-2v-2h2m2-2H9v6h6V9Z"/></svg></span><span class="n">۲</span><b>منابع سرور</b><small>۱ گیگ رم کافی است</small></a>
<a class="hi-tile" href="#os"><span class="hi-ic amber"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M14.62 8.35c-.42.28-1.75 1.04-1.95 1.19-.39.31-.75.29-1.14-.01-.2-.16-1.53-.92-1.95-1.19-.48-.31-.45-.7.08-.92 1.64-.69 3.28-.64 4.91.03.49.21.51.6.05.9m7.22 7.28c-.93-2.09-2.2-3.99-3.84-5.66a4.31 4.31 0 0 1-1.06-1.88c-.1-.33-.17-.67-.24-1.01-.2-.88-.29-1.78-.7-2.61-.73-1.58-2-2.4-3.84-2.47-1.81.05-3.16.81-3.95 2.4-.21.43-.36.88-.46 1.34-.17.76-.32 1.55-.5 2.32-.15.65-.45 1.21-.96 1.71-1.61 1.57-2.9 3.37-3.88 5.35-.14.29-.28.58-.37.88-.19.66.29 1.12.99.96.44-.09.88-.18 1.3-.31.41-.15.57-.05.67.35.65 2.15 2.07 3.66 4.24 4.5 4.12 1.56 8.93-.66 9.97-4.58.07-.27.17-.37.47-.27.46.14.93.24 1.4.35.49.09.85-.16.92-.64.03-.26-.06-.49-.16-.73"/></svg></span><span class="n">۳</span><b>سیستم‌عامل</b><small>اوبونتو ۲۶ یا ۲۴</small></a>
<a class="hi-tile" href="#ports"><span class="hi-ic pink"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M4 1c-1.11 0-2 .89-2 2v4c0 1.11.89 2 2 2H1v2h12V9h-3c1.11 0 2-.89 2-2V3c0-1.11-.89-2-2-2H4m0 2h6v4H4V3M3 13v7h7v-2H5v-5H3m11 0c-1.11 0-2 .89-2 2v4c0 1.11.89 2 2 2h-3v2h12v-2h-3c1.11 0 2-.89 2-2v-4c0-1.11-.89-2-2-2h-6m0 2h6v4h-6v-4Z"/></svg></span><span class="n">۴</span><b>پورت‌ها</b><small>۸۰ و ۴۴۳ آزاد</small></a>
<a class="hi-tile" href="#ssh"><span class="hi-ic "><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M13 19v-3h8v3h-8m-4.5-6L2.47 7h4.24l4.96 4.95c.58.59.58 1.55 0 2.12L6.74 19H2.5l6-6Z"/></svg></span><span class="n">۵</span><b>دسترسی SSH</b><small>برای اجرای دستور</small></a>
</div>

## ۱. سرور مجازی (VPS) { #vps }

**VPS** یا سرور مجازی، کامپیوتری در یک دیتاسنتر است که اجاره می‌کنید و از طریق اینترنت کنترلش می‌کنید. یکی از این راه‌ها را برای خریدش انتخاب کنید:

<div class="hi-grid" style="grid-template-columns:1fr">
<a class="hi-card " href="https://www.google.com/search?q=buy+cheap+and+good+quality+vps+server"><span class="hi-ic "><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M20 8H4V6h16m0 12H4v-6h16m0-8H4c-1.11 0-2 .89-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2Z"/></svg></span><span class="tx"><b>کارت اعتباری یا پرداخت واسط</b><small>مستقیم از دیتاسنترهای معروف دنیا؛ معمولاً ارزان‌ترین راه.</small></span></a>
<a class="hi-card " href="https://www.google.com/search?q=purchase+vps+via+crypto"><span class="hi-ic amber"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M14.24 10.56c-.31 1.24-2.24.61-2.84.44l.55-2.18c.62.18 2.61.44 2.29 1.74m-3.11 1.56-.6 2.41c.74.19 3.03.92 3.37-.44.36-1.42-2.03-1.79-2.77-1.97m10.57 2.3c-1.34 5.36-6.76 8.62-12.12 7.28C4.22 20.36.963 14.94 2.3 9.58A9.996 9.996 0 0 1 14.42 2.3c5.35 1.34 8.61 6.76 7.28 12.12m-7.49-6.37.45-1.8-1.1-.25-.44 1.73c-.29-.07-.58-.14-.88-.2l.44-1.77-1.09-.26-.45 1.79c-.24-.06-.48-.11-.7-.17l-1.51-.38-.3 1.17s.82.19.8.2c.45.11.53.39.51.64l-1.23 4.93c-.05.14-.21.32-.5.27.01.01-.8-.2-.8-.2L6.87 15l1.42.36c.27.07.53.14.79.2l-.46 1.82 1.1.28.45-1.81c.3.08.59.15.87.23l-.45 1.79 1.1.28.46-1.82c1.85.35 3.27.21 3.85-1.48.5-1.35 0-2.15-1-2.66.72-.19 1.26-.64 1.41-1.62.2-1.33-.82-2.04-2.2-2.52Z"/></svg></span><span class="tx"><b>رمزارز</b><small>خیلی از ارائه‌دهنده‌ها رمزارز قبول می‌کنند.</small></span></a>
<a class="hi-card " href="https://www.google.com/search?q=%D8%AE%D8%B1%DB%8C%D8%AF+%D8%B3%D8%B1%D9%88%D8%B1+%D9%85%D8%AC%D8%A7%D8%B2%DB%8C"><span class="hi-ic green"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M5.06 3c-.43 0-.84.14-1.22.42s-.6.64-.7 1.08L2.11 8.91c-.25 1.09-.05 2.04.61 2.86l.28.28V19c0 .5.2 1 .61 1.39S4.5 21 5 21h14c.5 0 1-.2 1.39-.61S21 19.5 21 19v-6.95l.28-.28c.66-.82.86-1.77.61-2.86L20.86 4.5c-.13-.44-.36-.8-.73-1.08A1.88 1.88 0 0 0 18.94 3H5.06m13.83 1.97 1.08 4.41c.09.43 0 .82-.28 1.17-.25.31-.56.45-.94.45-.31 0-.58-.1-.8-.34-.22-.23-.34-.5-.37-.82L16.97 5l1.92-.03M5.06 5h1.97l-.61 4.84C6.3 10.63 5.91 11 5.25 11c-.41 0-.72-.14-.94-.45-.28-.35-.37-.74-.28-1.17L5.06 5m3.99 0H11v4.7c0 .35-.11.65-.36.92-.25.26-.56.38-.94.38-.34 0-.63-.12-.86-.41S8.5 10 8.5 9.66V9.5L9.05 5M13 5h1.95l.55 4.5c.08.42 0 .77-.29 1.07-.26.3-.6.43-1.01.43-.31 0-.59-.12-.84-.38A1.29 1.29 0 0 1 13 9.7V5m-5.55 7.05c.63.62 1.41.95 2.35.95.84 0 1.58-.33 2.2-.95.69.62 1.45.95 2.3.95.87 0 1.62-.33 2.25-.95.56.62 1.31.95 2.25.95h.23v6H5v-6h.25c.91 0 1.64-.33 2.2-.95Z"/></svg></span><span class="tx"><b>ارائه‌دهنده‌های ایرانی</b><small>اگر در ایران هستید و پرداخت خارجی ندارید.</small></span></a>
</div>

برای پرداخت با کارت خارجی می‌توانید از [سایت‌های پرداخت واسط](https://www.google.com/search?q=%D9%BE%D8%B1%D8%AF%D8%A7%D8%AE%D8%AA+%D9%81%D8%A7%DA%A9%D8%AA%D9%88%D8%B1+%D8%AE%D8%A7%D8%B1%D8%AC%DB%8C) کمک بگیرید.

<div class="hi-cta-wrap"><a class="hi-cta" href="https://github.com/hiddify/awesome-freedom/blob/main/vps-providers.md"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M3 5h6v6H3V5m2 2v2h2V7H5m6 0h10v2H11V7m0 8h10v2H11v-2m-6 5-3.5-3.5 1.41-1.41L5 17.17l4.59-4.58L11 14l-6 6Z"/></svg>فهرست ارائه‌دهنده‌های پیشنهادی ما</a></div>

در این فهرست، ارائه‌دهنده‌هایی که رمزارز قبول می‌کنند مشخص شده‌اند. برای چند ارائه‌دهنده راهنمای نصب قدم‌به‌قدم هم داریم: [Hetzner](/fa/manager/installation-and-setup/Quick-installation-on-Hetzner-Servers/)، [Vultr](/fa/manager/installation-and-setup/Quick-installation-on-Vultr-Servers/)، [OVH](/fa/manager/installation-and-setup/Quick-Installation-on-OVH-Servers/)، [Oracle Cloud](/fa/manager/installation-and-setup/Quick-Installation-on-Oracle-Cloud/)، [Azure](/fa/manager/installation-and-setup/Quick-Installation-on-Microsoft-Azure/).

## ۲. منابع سرور { #resources }

حداقل پیشنهادی:

<div class="hi-grid c3">
<div class="hi-stat"><span class="hi-ic green"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M17 17H7V7h10m4 4V9h-2V7a2 2 0 0 0-2-2h-2V3h-2v2h-2V3H9v2H7c-1.11 0-2 .89-2 2v2H3v2h2v2H3v2h2v2a2 2 0 0 0 2 2h2v2h2v-2h2v2h2v-2h2a2 2 0 0 0 2-2v-2h2v-2h-2v-2m-6 2h-2v-2h2m2-2H9v6h6V9Z"/></svg></span><span><b>۱ گیگابایت</b><small>رم</small></span></div>
<div class="hi-stat"><span class="hi-ic "><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M6 4h12v1h3v2h-3v2h3v2h-3v2h3v2h-3v2h3v2h-3v1H6v-1H3v-2h3v-2H3v-2h3v-2H3V9h3V7H3V5h3V4m5 11v3h1v-3h-1m2 0v3h1v-3h-1m2 0v3h1v-3h-1Z"/></svg></span><span><b>۱ هسته</b><small>CPU</small></span></div>
<div class="hi-stat"><span class="hi-ic amber"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M6 2h12a2 2 0 0 1 2 2v16a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2m6 2a6 6 0 0 0-6 6c0 3.31 2.69 6 6.1 6l-.88-2.23a1.01 1.01 0 0 1 .37-1.37l.86-.5a1.01 1.01 0 0 1 1.37.37l1.92 2.42A5.977 5.977 0 0 0 18 10a6 6 0 0 0-6-6m0 5a1 1 0 0 1 1 1 1 1 0 0 1-1 1 1 1 0 0 1-1-1 1 1 0 0 1 1-1m-5 9a1 1 0 0 0-1 1 1 1 0 0 0 1 1 1 1 0 0 0 1-1 1 1 0 0 0-1-1m5.09-4.73 2.49 6.31 2.59-1.5-4.22-5.31-.86.5Z"/></svg></span><span><b>۱۰ گیگابایت</b><small>فضای دیسک</small></span></div>
</div>

اگر رم سرور کم باشد، نصب‌کننده در طول نصب یک فضای swap موقت (بخشی از دیسک که مثل رم اضافه استفاده می‌شود) می‌سازد.

## ۳. سیستم‌عامل { #os }

سیستم‌عامل سرور باید **اوبونتو** باشد. اوبونتو یکی از نسخه‌های معروف لینوکس است و موقع ساختن سرور، در پنل ارائه‌دهنده انتخابش می‌کنید. بهترین انتخاب **اوبونتو ۲۶.۰۴** یا **۲۴.۰۴** است. اوبونتو ۲۲.۰۴ هنوز کار می‌کند، ولی فقط وقتی سراغش بروید که ارائه‌دهنده نسخهٔ جدیدتری ندارد.

<div class="hi-chips">
<span class="hi-chip ok"><img src="/assets/logos/ubuntu.svg" alt="">Ubuntu 26.04 · پیشنهادی</span>
<span class="hi-chip ok"><img src="/assets/logos/ubuntu.svg" alt="">Ubuntu 24.04 · پیشنهادی</span>
<span class="hi-chip"><img src="/assets/logos/ubuntu.svg" alt="">Ubuntu 22.04 · آخرین انتخاب</span>
<span class="hi-chip no">Ubuntu 20.04</span>
<span class="hi-chip no">Debian · CentOS</span>
</div>

<div class="hi-chips">
<span class="hi-chip"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M6 4h12v1h3v2h-3v2h3v2h-3v2h3v2h-3v2h3v2h-3v1H6v-1H3v-2h3v-2H3v-2h3v-2H3V9h3V7H3V5h3V4m5 11v3h1v-3h-1m2 0v3h1v-3h-1m2 0v3h1v-3h-1Z"/></svg> amd64 (x86_64)</span>
<span class="hi-chip"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M6 4h12v1h3v2h-3v2h3v2h-3v2h3v2h-3v2h3v2h-3v1H6v-1H3v-2h3v-2H3v-2h3v-2H3V9h3V7H3V5h3V4m5 11v3h1v-3h-1m2 0v3h1v-3h-1m2 0v3h1v-3h-1Z"/></svg> arm64</span>
</div>

یک سرور تازه انتخاب کنید که چیز دیگری روی آن نصب نشده باشد.

## ۴. پورت‌ها { #ports }

هیدیفای‌منیجر به پورت‌های **80** و **443** نیاز دارد و هیچ برنامهٔ دیگری روی سرور نباید از آن‌ها استفاده کند. اگر ارائه‌دهندهٔ سرور فایروال جداگانه دارد، دست‌کم این پورت‌ها را باز کنید:

<div class="hi-chips">
<span class="hi-chip"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M13 19v-3h8v3h-8m-4.5-6L2.47 7h4.24l4.96 4.95c.58.59.58 1.55 0 2.12L6.74 19H2.5l6-6Z"/></svg> <code>22</code> SSH</span>
<span class="hi-chip"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M16.36 14c.08-.66.14-1.32.14-2 0-.68-.06-1.34-.14-2h3.38c.16.64.26 1.31.26 2s-.1 1.36-.26 2m-5.15 5.56c.6-1.11 1.06-2.31 1.38-3.56h2.95a8.03 8.03 0 0 1-4.33 3.56M14.34 14H9.66c-.1-.66-.16-1.32-.16-2 0-.68.06-1.35.16-2h4.68c.09.65.16 1.32.16 2 0 .68-.07 1.34-.16 2M12 19.96c-.83-1.2-1.5-2.53-1.91-3.96h3.82c-.41 1.43-1.08 2.76-1.91 3.96M8 8H5.08A7.923 7.923 0 0 1 9.4 4.44C8.8 5.55 8.35 6.75 8 8m-2.92 8H8c.35 1.25.8 2.45 1.4 3.56A8.008 8.008 0 0 1 5.08 16m-.82-2C4.1 13.36 4 12.69 4 12s.1-1.36.26-2h3.38c-.08.66-.14 1.32-.14 2 0 .68.06 1.34.14 2M12 4.03c.83 1.2 1.5 2.54 1.91 3.97h-3.82c.41-1.43 1.08-2.77 1.91-3.97M18.92 8h-2.95a15.65 15.65 0 0 0-1.38-3.56c1.84.63 3.37 1.9 4.33 3.56M12 2C6.47 2 2 6.5 2 12a10 10 0 0 0 10 10 10 10 0 0 0 10-10A10 10 0 0 0 12 2Z"/></svg> <code>80</code> HTTP</span>
<span class="hi-chip"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 17a2 2 0 0 1-2-2c0-1.11.89-2 2-2a2 2 0 0 1 2 2 2 2 0 0 1-2 2m6 3V10H6v10h12m0-12a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V10c0-1.11.89-2 2-2h1V6a5 5 0 0 1 5-5 5 5 0 0 1 5 5v2h1m-6-5a3 3 0 0 0-3 3v2h6V6a3 3 0 0 0-3-3Z"/></svg> <code>443</code> HTTPS</span>
</div>

## ۵. دسترسی SSH { #ssh }

برای اجرای دستور نصب باید از طریق SSH به سرور وصل شوید. اگر تا حالا این کار را نکرده‌اید، از اینجا شروع کنید:

<div class="hi-grid" style="grid-template-columns:1fr">
<a class="hi-card big" href="/fa/manager/installation-and-setup/How-to-connect-to-server-via-SSH/"><span class="hi-ic "><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M13 19v-3h8v3h-8m-4.5-6L2.47 7h4.24l4.96 4.95c.58.59.58 1.55 0 2.12L6.74 19H2.5l6-6Z"/></svg></span><span class="tx"><b>آموزش اتصال به سرور با SSH</b><small>قدم‌به‌قدم از ویندوز، مک، لینوکس و گوشی.</small></span></a>
</div>

بعد از نصب، این دو کار دسترسی SSH را امن‌تر می‌کنند:

<div class="hi-grid c2">
<a class="hi-card " href="/fa/manager/basic-concepts-and-troubleshooting/Disable-SSH-Password-Authentication/"><span class="hi-ic green"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M22 18v4h-4v-3h-3v-3h-3l-2.26-2.26c-.55.17-1.13.26-1.74.26a6 6 0 0 1-6-6 6 6 0 0 1 6-6 6 6 0 0 1 6 6c0 .61-.09 1.19-.26 1.74L22 18M7 5a2 2 0 0 0-2 2 2 2 0 0 0 2 2 2 2 0 0 0 2-2 2 2 0 0 0-2-2Z"/></svg></span><span class="tx"><b>ورود با کلید به‌جای رمز</b><small>ورود با رمز عبور را غیرفعال کنید.</small></span></a>
<a class="hi-card " href="/fa/manager/basic-concepts-and-troubleshooting/How-to-change-SSH-port-on-your-server/"><span class="hi-ic pink"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M21 11c0 5.55-3.84 10.74-9 12-5.16-1.26-9-6.45-9-12V5l9-4 9 4v6m-9 10c3.75-1 7-5.46 7-9.78V6.3l-7-3.12L5 6.3v4.92C5 15.54 8.25 20 12 21m2.8-10V9.5C14.8 8.1 13.4 7 12 7S9.2 8.1 9.2 9.5V11c-.6 0-1.2.6-1.2 1.2v3.5c0 .7.6 1.3 1.2 1.3h5.5c.7 0 1.3-.6 1.3-1.2v-3.5c0-.7-.6-1.3-1.2-1.3m-1.3 0h-3V9.5c0-.8.7-1.3 1.5-1.3s1.5.5 1.5 1.3V11Z"/></svg></span><span class="tx"><b>تغییر پورت SSH</b><small>پورت ۲۲ را به یک پورت دیگر ببرید.</small></span></a>
</div>

<div class="hi-cta-wrap"><a class="hi-cta" href="/fa/manager/installation-and-setup/guide/"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="m13.13 22.19-1.63-3.83c1.57-.58 3.04-1.36 4.4-2.27l-2.77 6.1M5.64 12.5l-3.83-1.63 6.1-2.77C7 9.46 6.22 10.93 5.64 12.5M19.22 4c.28 0 .53 0 .74.05.17 1.39-.02 4.25-3.3 7.53-1.7 1.71-3.73 3.02-6.01 3.89l-2.15-2.1c.92-2.31 2.23-4.34 3.92-6.03C15.18 4.58 17.64 4 19.22 4m0-2c-1.98 0-4.98.69-8.22 3.93-2.19 2.19-3.5 4.6-4.35 6.71-.28.75-.09 1.57.46 2.13l2.13 2.12c.38.38.89.61 1.42.61.23 0 .47-.06.7-.15A19.1 19.1 0 0 0 18.07 13c5.66-5.66 3.54-10.61 3.54-10.61S20.7 2 19.22 2m-4.68 7.46c-.78-.78-.78-2.05 0-2.83s2.05-.78 2.83 0c.77.78.78 2.05 0 2.83-.78.78-2.05.78-2.83 0m-5.66 7.07-1.41-1.41 1.41 1.41M6.24 22l3.64-3.64c-.34-.09-.67-.24-.97-.45L4.83 22h1.41M2 22h1.41l4.77-4.76-1.42-1.41L2 20.59V22m0-2.83 4.09-4.08c-.21-.3-.36-.62-.45-.97L2 17.76v1.41Z"/></svg>همه آماده است؟ برویم سراغ نصب</a></div>

## مقاله‌های مرتبط

<div class="hi-related" markdown="1">

- [اتصال به سرور با SSH](/fa/manager/installation-and-setup/How-to-connect-to-server-via-SSH/)
- [راهنمای نصب اصلی](/fa/manager/installation-and-setup/guide/)
- [ثبت دامنه و تنظیمات بعد از نصب](/fa/manager/installation-and-setup/Guide-for-setting-up-the-domain-and-finalizing-the-installation/)
- [نصب نسخه‌های مختلف](/fa/manager/installation-and-setup/How-to-install-different-versions-of-Hiddify-Manager/)

</div>

</div>
