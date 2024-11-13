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

<div class="button-container" id="download-buttons">
    <!-- Buttons will appear here based on selection -->
</div>

<script>
function showButtons(platform) {
    const container = document.getElementById("download-buttons");
    container.innerHTML = ""; // Clear previous buttons

    let buttonsHTML = "";
    if (platform === "windows") {
        buttonsHTML = `
            <a href="https://microsoft.com/store" class="md-button md-button--primary">Microsoft Store</a>
            <a href="https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Windows-Setup-x64.exe" class="md-button md-button--primary">Download EXE</a>
            <a href="https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Windows-Portable.zip" class="md-button md-button--primary">Portable Version</a>
        `;
    } else if (platform === "ios") {
        buttonsHTML = `
            <a href="https://apps.apple.com/us/app/hiddify-proxy-vpn/id6596777532?platform=iphone" class="md-button md-button--primary">App Store</a>
        `;
    } else if (platform === "android") {
        buttonsHTML = `
            <a href="https://play.google.com/store/apps/details?id=app.hiddify.com" class="md-button md-button--primary">Google Play</a>
            <a href="https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Android.apk" class="md-button md-button--primary">Download APK</a>
            <a href="https://github.com/hiddify/hiddify-app/releases" class="md-button md-button--primary">Other APKs</a>
        `;
    } else if (platform === "macos") {
        buttonsHTML = `
            <a href="https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-MacOS.dmg" class="md-button md-button--primary">Download DMG</a>
            <a href="https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-MacOS.pkg" class="md-button md-button--primary">Download PKG</a>
        `;
    } else if (platform === "linux") {
        buttonsHTML = `
            <a href="https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Linux-x64.AppImage" class="md-button md-button--primary">AppImage</a>
            <a href="https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Linux.deb" class="md-button md-button--primary">Deb Package</a>
            <a href="https://github.com/hiddify/hiddify-app/releases/latest/download/Hiddify-Linux.rpm" class="md-button md-button--primary">RPM Package</a>
        `;
    }

    container.innerHTML = buttonsHTML;
}
</script>
