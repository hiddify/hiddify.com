// Shorten raw badge values: data-format="compact" (120 604 -> 121K), data-format="rating" (4.44191 -> 4.4)
function formatBadge(img, svg) {
    const format = img.dataset.format;
    if (!format) return;
    svg.querySelectorAll("text").forEach(text => {
        let value = text.textContent;
        if (format === "compact") {
            const number = Number(value.replace(/\D/g, ""));
            if (!number) return;
            value = new Intl.NumberFormat("en", { notation: "compact", maximumFractionDigits: 0 }).format(number);
        } else if (format === "rating") {
            value = value.replace(/\d+\.\d+/, rating => Number(rating).toFixed(1));
        }
        text.textContent = value;
        text.removeAttribute("textLength"); // shields stretches text to its original width otherwise
    });

    // shrink the badge to the new text so it stays centered (shields draws text at scale(.1))
    const text = svg.querySelector('g[text-anchor="middle"] text');
    const textWidth = text && text.getComputedTextLength() / 10;
    if (!textWidth) return;
    const center = text.x.baseVal[0].value / 10;
    const width = textWidth + 10;
    svg.setAttribute("viewBox", `${center - width / 2} 0 ${width} 20`);
    svg.setAttribute("width", width);
}

document.addEventListener("DOMContentLoaded", function () {
    // Check if there's a hash in the URL
    if (window.location.hash) {
        const hash = window.location.hash;

        // Use a timeout to ensure the scrolling happens after the content is loaded
        setTimeout(() => {
            const targetElement = document.querySelector(hash);
            if (targetElement) {
                // Calculate the target position minus 100 pixels
                const offsetTop = targetElement.getBoundingClientRect().top + window.scrollY - 100;

                window.scrollTo({ top: offsetTop, behavior: 'smooth' });
            }
        }, 500); 
    }

    SVGInject(document.querySelectorAll("img"), { afterInject: formatBadge });

document.getElementById('show-protocols-app').addEventListener('click', function(event) {
  event.preventDefault(); // Prevent page jump
  const hiddenFeatures = document.querySelector('#show-protocols-app + .hidden-features');
  hiddenFeatures.style.display = hiddenFeatures.style.display === 'none' ? 'inline' : 'none';
});

document.getElementById('show-protocols-manager').addEventListener('click', function(event) {
  event.preventDefault(); // Prevent page jump
  const hiddenFeatures = document.querySelector('#show-protocols-manager + .hidden-features');
  hiddenFeatures.style.display = hiddenFeatures.style.display === 'none' ? 'inline' : 'none';
});



    
    if (document.getElementById('show-protocols')){
    document.getElementById('show-protocols').addEventListener('click', function(e) {
        e.preventDefault();
        const hiddenFeatures = document.querySelector('.hidden-features');
        hiddenFeatures.style.display = hiddenFeatures.style.display === 'none' ? 'inline' : 'none';
      });
    }

      const platformButtons = document.querySelectorAll('.platform-button');
      const downloadButton = document.getElementById('download-button');
      
      platformButtons.forEach(button => {
        button.addEventListener('click', () => {
            Swal.fire({title: "Downloading", icon:"info"});
          platformButtons.forEach(btn => btn.classList.remove('selected'));
          button.classList.add('selected');
          const platform = button.dataset.platform;
          downloadButton.textContent = `${downloadButton.dataset.prefix} ${platform}`;
          downloadButton.href = button.attributes['href'].value;
        });
      });
      const installButton = document.getElementById("install-btn");

var btnid = "btn-windows";
if (window.navigator.userAgent.indexOf("Windows") != -1) btnid = "btn-windows";
else if (window.navigator.userAgent.indexOf("Mac") != -1) btnid = "btn-ios";
else if (window.navigator.userAgent.indexOf("iPhone") != -1) btnid = "btn-ios";
else if (window.navigator.userAgent.indexOf("iPad") != -1) btnid = "btn-ios";
else if (window.navigator.userAgent.indexOf("Android") != -1) btnid = "btn-android";
else if (window.navigator.userAgent.indexOf("X11") != -1) btnid = "btn-linux";
else if (window.navigator.userAgent.indexOf("Linux") != -1) btnid = "btn-linux";
button=document.getElementById(btnid);
if (button && downloadButton){
  platformButtons.forEach(btn => btn.classList.remove('selected'));
  button.classList.add('selected');

  downloadButton.textContent = `${downloadButton.dataset.prefix} ${button.dataset.platform}`;
  downloadButton.href = button.attributes['href'].value;
}
});




