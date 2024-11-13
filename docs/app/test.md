<div class="platform-grid">
    <a id="btn-android" href="#" onclick="showButtons('android')" class="platform-button">
        <img src="/assets/platforms/android.svg" alt="Android">
    </a>
    <a id="btn-ios" href="#" onclick="showButtons('ios')" class="platform-button">
        <img src="/assets/platforms/apple.svg" alt="iOS">
    </a>
    <a id="btn-windows" href="#" onclick="showButtons('windows')" class="platform-button">
        <img src="/assets/platforms/windows.svg" alt="Windows">
    </a>
    <a id="btn-macos" href="#" onclick="showButtons('macos')" class="platform-button">
        <img src="/assets/platforms/mac.svg" alt="macOS">
    </a>
    <a id="btn-linux" href="#" onclick="showButtons('linux')" class="platform-button">
        <img src="/assets/platforms/linux.svg" alt="Linux">
    </a>
</div>

<div class="button-container" id="download-buttons"></div>

<style>
.button-container {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-top: 20px;
}
.md-button {
    padding: 10px 20px;
    margin: 5px;
    text-align: center;
    border: 1px solid #ddd;
    border-radius: 5px;
    text-decoration: none;
    font-weight: bold;
}
</style>

<script>
// Detect OS and display relevant buttons
document.addEventListener("DOMContentLoaded", function () {
    const os = getOS();
    showButtons(os);
});

function getOS() {
    const platform = navigator.platform.toLowerCase();
    if (platform.includes("win")) return "windows";
    if (platform.includes("mac")) return "macos";
    if (platform.includes("linux")) return "linux";
    if (/iphone|ipad|ipod/.test(navigator.userAgent.toLowerCase())) return "ios";
    if (/android/.test(navigator.userAgent.toLowerCase())) return "android";
    return "windows"; // default if unknown
}

function showButtons(platform) {
    const container = document.getElementById("download-buttons");
    container.innerHTML = ""; // Clear previous buttons

    let buttonsHTML = "";
    if (platform === "windows") {
        buttonsHTML = `
            <a href="https://microsoft.com/store" class="md-button md-button--primary" onclick="showDownloading(this)">Microsoft Store</a>
            <a href="https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Windows-Setup-x64.exe" class="md-button md-button--primary" onclick="showDownloading(this)">Download EXE</a>
            <a href="https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Windows-Portable.zip" class="md-button md-button--primary" onclick="showDownloading(this)">Portable Version</a>
        `;
    } else if (platform === "ios") {
        buttonsHTML = `
            <a href="https://apps.apple.com/us/app/hiddify-proxy-vpn/id6596777532?platform=iphone" class="md-button md-button--primary" onclick="showDownloading(this)">App Store</a>
        `;
    } else if (platform === "android") {
        buttonsHTML = `
            <a href="https://play.google.com/store/apps/details?id=app.hiddify.com" class="md-button md-button--primary" onclick="showDownloading(this)">Google Play</a>
            <a href="https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Android.apk" class="md-button md-button--primary" onclick="showDownloading(this)">Download APK</a>
            <a href="https://github.com/hiddify/hiddify-app/releases" class="md-button md-button--primary" onclick="showDownloading(this)">Other APKs</a>
        `;
    } else if (platform === "macos") {
        buttonsHTML = `
            <a href="https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-MacOS.dmg" class="md-button md-button--primary" onclick="showDownloading(this)">Download DMG</a>
            <a href="https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-MacOS.pkg" class="md-button md-button--primary" onclick="showDownloading(this)">Download PKG</a>
        `;
    } else if (platform === "linux") {
        buttonsHTML = `
            <a href="https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Linux-x64.AppImage" class="md-button md-button--primary" onclick="showDownloading(this)">AppImage</a>
            <a href="https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Linux.deb" class="md-button md-button--primary" onclick="showDownloading(this)">Deb Package</a>
            <a href="https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Linux.rpm" class="md-button md-button--primary" onclick="showDownloading(this)">RPM Package</a>
        `;
    }

    container.innerHTML = buttonsHTML;
}

// Function to show "Downloading..." text when a download button is clicked
function showDownloading(button) {
    button.innerText = "Downloading...";
}
</script>
