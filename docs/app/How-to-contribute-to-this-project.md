---
title: How to contribute to this project
---

# How to contribute to the Hiddify app

The Hiddify app is open source: [github.com/hiddify/hiddify-app](https://github.com/hiddify/hiddify-app). You can help by reporting problems, translating, or changing the code. This page shows each way.

!!! info "Written for Hiddify app 5.9"
    The commands below match the repository as of version 5.9 (Flutter 3.38.5 or newer).

## Report a problem or suggest a feature

1. Search the [issues](https://github.com/hiddify/hiddify-app/issues?q=is%3Aissue), open and closed. If someone already reported it, add what you know there.
2. Otherwise open a [new issue](https://github.com/hiddify/hiddify-app/issues/new/choose) and pick **Bug report** or **Feature request**. Write the app version (**Settings › About**), your device and system, and the steps that cause the problem.
3. Add the logs. How to get them, and how to send a crash report from the app: [Logs and reporting a problem](Logs-and-reporting-a-problem.md). Remove your links, IPs and passwords before you post.

For a big change, open an issue first and agree on it with the maintainers, before you write code.

## Translate

The app's texts are in [`assets/translations`](https://github.com/hiddify/hiddify-app/tree/main/assets/translations): one file per language, such as `fa.i18n.json`. `en.i18n.json` is the base; every other file has the same keys.

- To fix a translation, edit the file of your language on GitHub (the pencil icon) and send the change as a pull request. GitHub makes the fork and the branch for you.
- Keep the keys, the `${…}` placeholders and the line breaks (`\n`) as they are; translate only the text.
- If you work locally, run `make translate` after editing to check the files and regenerate the code.

## Change the code

### 1. Get the code

1. On GitHub, open [hiddify/hiddify-app](https://github.com/hiddify/hiddify-app) and click **Fork**. This makes your own copy of the repository under your account.
2. Clone (download) your fork, and add the original repository as `upstream`:

```bash
git clone https://github.com/<your-username>/hiddify-app.git
cd hiddify-app
git remote add upstream https://github.com/hiddify/hiddify-app.git
```

### 2. Install the tools

- [Flutter](https://docs.flutter.dev/get-started/install) 3.38.5 or newer (`flutter --version` shows it), with its tools for your target: Android Studio and the Android SDK for Android; Xcode for iOS and macOS; Visual Studio with "Desktop development with C++" for Windows.
- `make`, `curl` and `tar`. On Debian or Ubuntu, `make linux-install-deps` installs what a Linux build needs.

### 3. Prepare a platform

Run the command for the platform you build for:

```bash
make android-prepare     # or: windows-prepare, linux-prepare, macos-prepare, ios-prepare
```

It runs `flutter pub get`, generates the code (`dart run build_runner build`) and the translations (`dart run slang`), and downloads the Hiddify Core library for that platform from the [hiddify-core releases](https://github.com/hiddify/hiddify-core/releases). Run it again after you switch branches.

While you work:

- after changing a model, provider or anything with generated code: `make gen`;
- after changing a translation file: `make translate`.

### 4. Run it

```bash
flutter devices           # lists phones, emulators and your computer
flutter run -d <device-id>
```

A release build for testing: `make android-release` (or `windows-release`, `linux-release`, `macos-release`).

### 5. Build the core yourself (optional)

Only needed if you change Hiddify Core too. The core is the `hiddify-core` submodule; it needs [Go](https://go.dev/dl/):

```bash
git config submodule.hiddify-core.url https://github.com/hiddify/hiddify-core.git   # if you have no SSH key on GitHub
git submodule update --init --recursive hiddify-core
make build-android-libs   # or: build-windows-libs, build-linux-libs, build-macos-libs, build-ios-libs
```

Changes to the core itself go to [hiddify-core](https://github.com/hiddify/hiddify-core) (and [hiddify-sing-box](https://github.com/hiddify/hiddify-sing-box)), as their own pull requests. Don't work around a core bug in the app: fix it in the core, or report it there.

### 6. Send your change

1. Start a branch from the latest code:

    ```bash
    git fetch upstream
    git switch -c fix/short-name upstream/main
    ```

2. Make one change per branch. Write commit messages in the [Conventional Commits](https://www.conventionalcommits.org/) style, for example `fix(home): keep the connect button disabled while stopping`.
3. Don't commit generated files (`*.g.dart`, `*.freezed.dart`, the generated translations in `lib/gen`), the downloaded core libraries, the `hiddify-core` submodule pointer, or any real link, IP or key.
4. Test on Android and on one desktop system.
5. Bring your branch up to date and push it to your fork:

    ```bash
    git fetch upstream
    git rebase upstream/main
    git push -u origin fix/short-name
    ```

6. On GitHub, open a **pull request** from your branch to `hiddify/hiddify-app`, base `main`. Say what was wrong, what you changed and how you tested it. For a change you can see, add before and after screenshots or short videos.

## Talk to the team

- [Hiddify group on Telegram](https://t.me/hiddify_board) and [channel](https://t.me/hiddify)
- Email: contribute@hiddify.com

## Related articles

- [Logs and reporting a problem in the Hiddify app](/app/Logs-and-reporting-a-problem/)
- [How to use the Hiddify app](/app/How-to-use-Hiddify-app/)
- [How to install the Hiddify app](/app/How-to-install-Hiddify-app/)
