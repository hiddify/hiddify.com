# Time Zone Leak

A time zone leak occurs when the time obtained from the browser differs from the time zone of your VPN.

## How to Test for a Time Zone Leak
You can check for time zone leaks using the website [webbrowsertools.com](https://webbrowsertools.com/timezone/). This site uses six different methods to assess the time zone. The last method (aggressive) is particularly effective in accurately identifying the browser's time zone.

As shown in the image below, without using an extension, a simple JavaScript code run by the site can detect the Iran time zone, which can expose you if it differs from your VPN's time zone.

![timezone](https://github.com/user-attachments/assets/d9eee13e-b903-4977-ba05-e8707671f2dd)

Another method is using the browser's console. You can find your browser's time zone with the following code snippet in the console:
```
console.log(Intl.DateTimeFormat().resolvedOptions().timeZone);
```
![timezone2](https://github.com/user-attachments/assets/61a3c169-32f0-47e9-b468-c37e1e1d4a4a)

## Preventing Time Zone Leaks
To prevent time zone leaks, two methods are recommended.

### 1. Using the NoScript Extension
With this extension in [Chrome](https://chromewebstore.google.com/detail/noscript/doojmbjmlfjjnbmnoijecmcbfeoakpjm) and [Firefox](https://addons.mozilla.org/addon/noscript/), JavaScript code execution in the browser is blocked, preventing websites from accessing your time zone.

![timezone3](https://github.com/user-attachments/assets/2238af19-619d-42ad-a7dc-b6bb7a07e0dd)

However, using this extension can have some drawbacks. Some sites may not display all their features properly, so use this extension with that in mind.

### 2. Using the Spoof Timezone Extension
With this extension in [Chrome](https://chromewebstore.google.com/detail/spoof-timezone/kcabmhnajflfolhelachlflngdbfhboe?hl=en) and [Firefox](https://addons.mozilla.org/en-US/firefox/addon/spoof-timezone/), you can reduce time zone leaks effectively. There are two modes for using this extension:
- **Mode 1: Greenwich Mean Time (GMT)**  
  If you don't change the extension settings, it will default to GMT as the system time.
- **Mode 2: System Time Matching VPN IP**  
  To set this mode, right-click on the extension, select *Options* from the menu, and check the box for *Automatically update timezone based on my IP address*. To apply the changes, right-click on the extension and select *Update Timezone from IP* to match the VPN's IP. Every time you switch VPN servers, you’ll need to repeat this last step to update the time zone according to the new IP.

![timezone4](https://github.com/user-attachments/assets/dce0eaef-40a3-4079-92f4-4067ea2bbce9)


Note that the mentioned website uses six methods to retrieve the browser's time zone. The sixth method is particularly strict. As shown in the image below, even when using the Spoof Timezone extension, your time zone may still be revealed. However, the NoScript extension completely disables this capability.

![timezone5](https://github.com/user-attachments/assets/f168398e-5073-4ec3-9994-a83bf53b7cb7)
