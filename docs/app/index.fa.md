---
description: به ویکی هیدیفای خوش آمدید
title: راهنمای هیدیفای‌اپ
comments: false
weight: -1
---
# :material-home: راهنمای هیدیفای‌اپ
یک کلاینت مالتی‌پلتفرم مبتنی بر [سینگ‌باکس](https://github.com/SagerNet/sing-box) که به عنوان یک ابزار عمومی برای پروکسی عمل می‌کند و با دارا بودن قابلیت‌های فراوان از پروتکل‌های زیادی برا دور زدن محدودیت‌های اینترنتی پشتیبانی می‌کند. اطلاعات بیشتر و دقیق‌تر را در [اینجا](https://github.com/hiddify/hiddify-next/blob/main/README_fa.md) ملاحظه فرمایید. این صفحه شامل مطالب آموزشی مرتبط به این برنامه می‌باشد.

## هیدیفای‌اپ

<div class="absolute -z-40 h-full max-h-[800px] w-full max-w-[700px] bg-blue-200 opacity-30 mix-blend-multiply blur-3xl filter md:left-0 md:animate-blob"></div>
<div class="animation-delay-2000 animat absolute -z-40 h-full max-h-[800px] w-full max-w-[700px] bg-indigo-300 opacity-30 mix-blend-multiply blur-3xl filter md:right-[5%] md:animate-blob"></div>

<div class="card-item mt-4 flex gap-16 rounded-xl border border-gray-500  p-8 backdrop-blur-xl backdrop-filter max-w-[800px] max-h-[451] w-full h-full relative mx-auto my-20 flex-col lg:flex-row">
<div class="max-w-[552px]">
    <img src="/assets/image-197.png" alt="image" class="rounded-xl">

    <ul class="my-4 list-disc text-secondary ml-5">
    <li>
        <a href="/fa/app/How-to-install-Hiddify-app/" target="_blank">آموزش نصب هیدیفای‌اپ</a>
    </li>
    <li>
        <a href="/fa/app/How-to-use-Hiddify-app/" target="_blank">آموزش کار با هیدیفای‌اپ</a>
    </li>
    <li>
        <a href="/app/How-to-use-UDP-Turn-Relay/" target="_blank">آموزش استفاده از UDP Turn Relay</a>
    </li>
    <li>
        <a href="/app/How-to-contribute-to-this-project/" target="_blank">چگونه می‌توان در این پروژه همکاری نمود</a>
    </li>
    <li>
        <a href="/app/URL-Scheme/" target="_blank">ساختار لینک‌ها در هیدیفای‌اپ</a>
    </li>
    </ul>

</div>
<div class="lg:border-r lg:border-gray-500 lg:p-4 lg:mr-auto">
    <h4 class="text-md">ویدئوهای مرتبط</h4>
    <div class="flex gap-4 mt-4 flex-col lg:mr-2">
    <a href="https://www.youtube.com/watch?v=vUaA1AEUy1s" target="_blank">
        <img src="/assets/install_HiddifyApp.png" alt="image" class="rounded-xl w-[184px] h-[103px]">
    </a>
    <a href="https://www.youtube.com/watch?v=EjHjLQbC40E" target="_blank">
        <img src="/assets/Use_HiddifyApp.png" alt="image" class="rounded-xl w-[184px] h-[103px]">
    </a>
    <a href="https://www.youtube.com/watch?v=NtQ0bQlIRrYs" target="_blank">
        <img src="/assets/advanced_setting_HiddifyApp.jpg" alt="image" class="rounded-xl w-[184px] h-[103px]">
    </a>
    </div>
</div>


<script>
    function toggleShow() {
    var mobileHeader = document.getElementById("mobile-header");
    var showIcon = document.getElementById("show-icon");
    var hideIcon = document.getElementById("hide-icon");

    if (mobileHeader.classList.contains("hidden")) {
        mobileHeader.classList.remove("hidden");
        showIcon.classList.add("hidden");
        hideIcon.classList.remove("hidden");
    } else {
        mobileHeader.classList.add("hidden");
        showIcon.classList.remove("hidden");
        hideIcon.classList.add("hidden");
    }
    }

    var cardItems = document.querySelectorAll(".card-item");
    cardItems.forEach(function (item) {
    var show_more = item.querySelector("button");
    var contents = item.querySelector(".hidden");
    var read_more_par = item.querySelector(".read-more-par");

    if (show_more) {
        show_more.addEventListener("click", function () {
        contents.outerHTML = contents.innerHTML;
        read_more_par.outerHTML = "";
        });
    }
    });
</script>
