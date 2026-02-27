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

    SVGInject(document.querySelectorAll("img"));

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




