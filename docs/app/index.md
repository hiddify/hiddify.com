---
title: App
hide:
  # - navigation
  # - toc
  - feedback

weight: -19

---

# Hiddify App Guide

HiddifyApp is a client based on <a class="underline underline-offset-2"
  href="https://github.com/SagerNet/sing-box">Sing-box</a> that serves as a
universal proxy tool-chain which offers a wide
range
of features and protocols. The appropriate and detailed information are accessible <a
  class="underline underline-offset-2"
  href="https://github.com/hiddify/hiddify-next/blob/main/README.md">here</a>. This page
contains
tutorial guides related to this project.

<section class="flex flex-col gap-5 items-center justify-center py-10">
      <section
        class=" video-card  relative w-full md:max-w-[900px] rounded-3xl border-2 border-white bg-white bg-opacity-20 shadow-lg">

        <div class="flex flex-col md:flex-row h-full md:max-h-[450px]" id="section-1">
          <div class="px-8 py-8 w-full md:w-2/3">
            <img src="/assets/hiddify-app.png" class="md:max-h-[183px] rounded-xl w-full md:max-w-[326px] mb-5" />
            <div class="flex flex-col gap-2">
              <h1 class="text-primaryText title-font text-lg mb-3">Hiddify App</h1>
              <div class="flex items-center gap-2">
                <div>
                  <div class="h-2 w-2 rounded-full bg-[#455FE9]"></div>
                </div>
                <a href="/app/How-to-install-Hiddify-app/" target="_blank" class="text-secondaryText text-sm">How
                  to install HiddifyApp</a>
              </div>
              <div class="flex items-center gap-2">
                <div>
                  <div class="h-2 w-2 rounded-full bg-[#455FE9]"></div>
                </div>
                <a href="/app/How-to-use-Hiddify-app" target="_blank" class="text-secondaryText text-sm">How to use
                  HiddifyApp
                </a>
              </div>
              <div class="flex items-center gap-2">
                <div>
                  <div class="h-2 w-2 rounded-full bg-[#455FE9]"></div>
                </div>
                <a href="/app/HiddifyCli-guide/" target="_blank" class="text-secondaryText text-sm">How to use
                  HiddifyCli</a>
              </div>
              <div class="flex items-center gap-2">
                <div>
                  <div class="h-2 w-2 rounded-full bg-[#455FE9]"></div>
                </div>
                <a href="/app/How-to-use-UDP-Turn-Relay/" target="_blank" class="text-secondaryText text-sm">How to
                  use
                  UDP Turn Relay in HiddifyApp</a>
              </div>
              <div class="flex items-center gap-2">
                <div>
                  <div class="h-2 w-2 rounded-full bg-[#455FE9]"></div>
                </div>
                <a href="/app/How-to-contribute-to-this-project/" target="_blank"
                  class="text-secondaryText text-sm">How
                  to contribute to this project</a>
              </div>

              <div class="flex flex-col gap-2 md:hidden" id="section-content-1">
                <div class="flex items-center gap-2">
                  <div>
                    <div class="h-2 w-2 rounded-full bg-[#455FE9]"></div>
                  </div>
                  <a href="/app/URL-Scheme/" target="_blank" class="text-secondaryText text-sm">
                    URL scehme in HiddifyApp
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

    </section>
  

<script>
  
  function readMore(id) {
    const readMoreBtn = document.getElementById(`read-more-${id}`)
    const arrowIcon = document.getElementById(`arrow-${id}`)
    const hiddenContent = document.getElementById(`section-content-${id}`)
    const section = document.getElementById(`section-${id}`)
    const sectionBottom = document.getElementById(`section-bottom-${id}`)

    const btnText = readMoreBtn.getElementsByTagName('span')[0].innerText

    if (btnText.includes('more')) {
      readMoreBtn.getElementsByTagName('span')[0].innerText = 'Read less'
      hiddenContent.style.display = 'flex'
      sectionBottom.classList.remove('absolute')

      const content = document.getElementById(`section-content-${id}`)
      section.style.maxHeight = content.offsetHeight + 450 + 'px'
      arrowIcon.style.transform = "rotate(180deg)";
    } else {
      readMoreBtn.getElementsByTagName('span')[0].innerText = 'Read more'
      hiddenContent.style.display = 'none'
      section.style.maxHeight = 450 + 'px'
      arrowIcon.style.transform = "rotate(0deg)";
      sectionBottom.classList.add('absolute')
    }
  }
</script>
