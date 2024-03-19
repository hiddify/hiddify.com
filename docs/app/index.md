---
description: Welcome to the wiki page for Hiddify App.
title: App Guide
weight: -1
comments: false
---

# :material-home: HiddifyApp Guide
Hiddify-Next is a client based on [Sing-box](https://github.com/SagerNet/sing-box) that serves as a universal proxy tool-chain which offers a wide range of features and protocols. The appropriate and detailed information are accessible [here](https://github.com/hiddify/hiddify-next/blob/main/README.md). This page contains tutorial guides related to this project.

## HiddifyApp

<div class="absolute -z-40 h-full max-h-[800px] w-full max-w-[700px] bg-blue-200 opacity-30 mix-blend-multiply blur-3xl filter md:left-0 md:animate-blob"></div>
<div class="animation-delay-2000 animat absolute -z-40 h-full max-h-[800px] w-full max-w-[700px] bg-indigo-300 opacity-30 mix-blend-multiply blur-3xl filter md:right-[5%] md:animate-blob"></div>

<div class="card-item mt-4 flex gap-16 rounded-xl border border-gray-500  p-8 backdrop-blur-xl backdrop-filter max-w-[800px] max-h-[451] w-full h-full relative mx-auto my-20 flex-col lg:flex-row">
<div class="max-w-[552px]">
    <img src="/assets/image-197.png" alt="image" class="rounded-xl">

    <ul class="my-4 list-disc text-secondary ml-5">
    <li>
        <a href="/app/How-to-install-Hiddify-app/" target="_blank">How to install HiddifyNext app</a>
    </li>
    <li>
        <a href="/app/How-to-use-Hiddify-app/" target="_blank">How to use HiddifyNext app</a>
    </li>
    <li>
        <a href="/app/How-to-use-UDP-Turn-Relay/" target="_blank">How to use UDP Turn Relay</a>
    </li>
    <li>
        <a href="/app/How-to-contribute-to-this-project/" target="_blank">How to contribute to this project</a>
    </li>
    <li>
        <a href="/app/URL-Scheme/" target="_blank">URL scehme in HiddifyApp</a>
    </li>
    </ul>

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
