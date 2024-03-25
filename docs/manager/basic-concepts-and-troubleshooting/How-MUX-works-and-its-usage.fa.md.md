---
title: کاربرد و نحوه عملکرد MUX 
---

<div dir="rtl" markdown="1">

# کاربرد و نحوه عملکرد MUX
## MUX چیست؟
Multiplexing که معمولاً به عنوان MUX شناخته می شود، به عنوان یک جزء حیاتی در پروتکل های VPN (شبکه خصوصی مجازی) عمل می‌کند و امکان انتقال همزمان جریان های داده‌های متعدد را از طریق یک کانال ارتباطی واحد فراهم می کند. در حوزه VPN ها، مالتی‌پلکس نقشی اساسی در بهینه سازی انتقال داده ایفا می‌کند. با تعریف مجموعه‌ای از جریان‌ها برای MUX در پروتکل VPN، جلساتی برای تسهیل عبور همه ترافیک از طریق این جریان‌ها ایجاد می‌شوند. این رویکرد نه تنها فرآیند انتقال را ساده می‌کند، بلکه اقدامات امنیتی را با پنهان کردن الگوهای انتقال افزایش می‌دهد، بنابراین رهگیری یا دستکاری داده ها را برای نهادهای غیرمجاز چالش برانگیزتر می کند.

## پروتکل‌های MUX
ماکس عموما از ۳ کتابخانه برای مالتی‌پلکس کردن استفاده می‌کند که به ترتیب توضیحات مختصری درباره هر کدام ارائه می‌گردد:
#### SMUX
Smux (Simple MUltipleXing) یک کتابخانه مالتی پلکسی برای Golang است. برای ارائه قابلیت اطمینان و سفارش، مانند TCP یا KCP، به یک اتصال اساسی متکی است و مالتی پلکسی جریان محور را فراهم می کند. هدف اصلی این کتابخانه قدرت مدیریت اتصال برای kcp-go است.

#### YAMUX

#### H2MUX
































</div>