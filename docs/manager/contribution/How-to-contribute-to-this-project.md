---
title: How to contribute to this project
---

<div markdown="1">

# How to contribute to this project

!!! info "Written for Hiddify Manager v14.5"
    The development steps below follow the project’s own [DEVELOPMENT.md](https://github.com/hiddify/Hiddify-Manager/blob/dev/DEVELOPMENT.md) and [CONTRIBUTING.md](https://github.com/hiddify/Hiddify-Manager/blob/dev/CONTRIBUTING.md). If they differ from this page, those files are right.

Hiddify Manager is free and open source, and its users help build it. You do not need to be a programmer to help.

## Ways to help without code { #ways-to-help-without-code }

<div class="hi-grid c2">
<a class="hi-card" href="https://github.com/hiddify/Hiddify-Manager/issues"><span class="hi-ic pink"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M20 8h-2.81c-.45-.8-1.07-1.5-1.82-2L17 4.41 15.59 3l-2.17 2.17a6.002 6.002 0 0 0-2.83 0L8.41 3 7 4.41 8.62 6c-.75.5-1.36 1.21-1.81 2H4v2h2.09c-.06.33-.09.66-.09 1v1H4v2h2v1c0 .34.03.67.09 1H4v2h2.81A5.988 5.988 0 0 0 15 20.18c.91-.52 1.67-1.28 2.19-2.18H20v-2h-2.09c.06-.33.09-.66.09-1v-1h2v-2h-2v-1c0-.34-.03-.67-.09-1H20V8m-4 7a4 4 0 0 1-4 4 4 4 0 0 1-4-4v-4a4 4 0 0 1 4-4 4 4 0 0 1 4 4v4m-2-5v2h-4v-2h4m-4 4h4v2h-4v-2Z"/></svg></span><span class="tx"><b>Report a bug or an idea</b><small>Open an issue on GitHub: your version (top of the panel), what you did, what you expected and what happened, with logs or pictures. Hide your IPs, domains and links.</small></span></a>
<a class="hi-card" href="https://github.com/hiddify/Hiddify-Panel/tree/dev/hiddifypanel/translations.i18n"><span class="hi-ic "><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="m12.87 15.07-2.54-2.51.03-.03A17.52 17.52 0 0 0 14.07 6H17V4h-7V2H8v2H1v2h11.17C11.5 7.92 10.44 9.75 9 11.35 8.07 10.32 7.3 9.19 6.69 8h-2c.73 1.63 1.73 3.17 2.98 4.56l-5.09 5.02L4 19l5-5 3.11 3.11.76-2.04M18.5 10h-2L12 22h2l1.12-3h4.75L21 22h2l-4.5-12m-2.62 7 1.62-4.33L19.12 17h-3.24Z"/></svg></span><span class="tx"><b>Translate the panel</b><small>The texts are in <code>translations.i18n/&lt;language&gt;.json</code> in the Hiddify-Panel repository. Fix or add them and send a pull request.</small></span></a>
<a class="hi-card" href="https://github.com/hiddify/hiddify.com"><span class="hi-ic green"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M8 12h8v2H8v-2m2 8H6V4h7v5h5v3.1l2-2V8l-6-6H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h4v-2m-2-2h4.1l.9-.9V16H8v2m12.2-5c.1 0 .3.1.4.2l1.3 1.3c.2.2.2.6 0 .8l-1 1-2.1-2.1 1-1c.1-.1.2-.2.4-.2m0 3.9L14.1 23H12v-2.1l6.1-6.1 2.1 2.1Z"/></svg></span><span class="tx"><b>Improve this website</b><small>The pencil button at the top of each page opens it on GitHub. Fix a mistake or add a guide.</small></span></a>
<a class="hi-card" href="https://www.youtube.com/@hiddify"><span class="hi-ic amber"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 8H4a2 2 0 0 0-2 2v4a2 2 0 0 0 2 2h1v4a1 1 0 0 0 1 1h2a1 1 0 0 0 1-1v-4h3l5 4V4l-5 4m3 7.6L13 14H4v-4h9l2-1.6v7.2m6.5-3.6c0 1.71-.96 3.26-2.5 4V8c1.53.75 2.5 2.3 2.5 4Z"/></svg></span><span class="tx"><b>Spread the word</b><small>Tell others about Hiddify, make videos and guides, and answer users’ questions.</small></span></a>
</div>

For other help (development, services), email [hiddify@gmail.com](mailto:hiddify@gmail.com).

## The repositories { #the-repositories }

Hiddify Manager is built from three repositories. Work on the `dev` branch in each.

<div class="hi-grid c3">
<a class="hi-card" href="https://github.com/hiddify/Hiddify-Manager"><span class="hi-ic logo"><img src="/assets/logos/github.svg" alt=""></span><span class="tx"><b>Hiddify-Manager</b><small>Install scripts, services and systemd units. Installed in <code>/opt/hiddify-manager</code>.</small></span></a>
<a class="hi-card" href="https://github.com/hiddify/Hiddify-Panel"><span class="hi-ic logo"><img src="/assets/logos/github.svg" alt=""></span><span class="tx"><b>Hiddify-Panel</b><small>The panel: Flask API, admin UI (<code>admin_v2</code>, Vue), config templates, certificates and translations. A submodule in <code>services/panel/src</code>.</small></span></a>
<a class="hi-card" href="https://github.com/hiddify/hiddify-user-front"><span class="hi-ic logo"><img src="/assets/logos/github.svg" alt=""></span><span class="tx"><b>hiddify-user-front</b><small>The user page (React). A submodule of the panel.</small></span></a>
</div>

## Set up a development server { #set-up-a-development-server }

Work on a Linux server or VM (preferably Ubuntu 24.04 or 26.04), as root. A development machine **is** a Hiddify server: the code lives where an installed Hiddify lives.

```bash
sudo -i
git clone --recurse-submodules -b dev https://github.com/hiddify/Hiddify-Manager.git /opt/hiddify-manager
cd /opt/hiddify-manager
make build
git -C services/panel/src checkout dev
```

`make build` installs everything (MySQL, Redis, HAProxy, Xray, the Hiddify core, the panel, …) in place. Then open `/opt/hiddify-manager` in VS Code (on a remote server, with the *Remote - SSH* extension). `.vscode/launch.json` has the run configurations.

### Day to day

- After changing the panel’s Python code, only restart the panel: `systemctl restart hiddify-panel`
- The **Admin V2 Dev (Flask + Vite)** configuration in VS Code runs the panel with the debugger and the admin UI with live reload.
- After changing a template or settings, click **Apply now** in the panel or run: `make apply`
- `data/` (server state) and `generated/` (configs the panel builds) are not in git. Never edit or commit them.
- Tests are in `services/panel/tests` (pytest). DEVELOPMENT.md shows how to run them.

## Send your change { #send-your-change }

1. On GitHub, **Fork** the repository you changed (the button at the top of the repository page).
2. Make a new branch from `dev`, commit, and push it to your fork. If you changed both repositories, commit the panel first.
3. Write the commit message in the [Conventional Commits](https://www.conventionalcommits.org/) style, because the changelog is built from it. For example:

    ```text
    fix: show the right expiry date on the user page
    feat: add a Reality SNI scanner
    ```

4. Open a **pull request** to the main repository’s `dev` branch. Describe the problem, your change and how you tested it, and add pictures for visual changes.

### New to git?

<div class="hi-grid c3">
<a class="hi-card" href="https://git-scm.com/book/en/v2"><span class="hi-ic "><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="m19 1-5 5v11l5-4.5V1m2 4v13.5c-1.1-.35-2.3-.5-3.5-.5-1.7 0-4.15.65-5.5 1.5V6c-1.45-1.1-3.55-1.5-5.5-1.5-1.95 0-4.05.4-5.5 1.5v14.65c0 .25.25.5.5.5.1 0 .15-.05.25-.05C3.1 20.45 5.05 20 6.5 20c1.95 0 4.05.4 5.5 1.5 1.35-.85 3.8-1.5 5.5-1.5 1.65 0 3.35.3 4.75 1.05.1.05.15.05.25.05.25 0 .5-.25.5-.5V6c-.6-.45-1.25-.75-2-1M10 18.41C8.75 18.09 7.5 18 6.5 18c-1.06 0-2.32.19-3.5.5V7.13c.91-.4 2.14-.63 3.5-.63 1.36 0 2.59.23 3.5.63v11.28Z"/></svg></span><span class="tx"><b>The free Pro Git book</b><small>Git from zero</small></span></a>
<a class="hi-card" href="https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks"><span class="hi-ic logo"><img src="/assets/logos/github.svg" alt=""></span><span class="tx"><b>Forks and pull requests</b><small>GitHub’s own step-by-step guide</small></span></a>
<a class="hi-card" href="https://git-scm.com/downloads"><span class="hi-ic green"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M13 5v6h1.17L12 13.17 9.83 11H11V5h2m2-2H9v6H5l7 7 7-7h-4V3m4 15H5v2h14v-2Z"/></svg></span><span class="tx"><b>Download git</b><small>git-scm.com</small></span></a>
</div>

## Related articles

<div class="hi-related" markdown="1">

- [Using the Hiddify Manager API](/manager/contribution/How-to-use-API-in-HiddifyManager-project/)
- [![](/assets/hiddify-app-logo.svg) Contribute to the Hiddify app](/app/How-to-contribute-to-this-project/)

</div>

</div>
