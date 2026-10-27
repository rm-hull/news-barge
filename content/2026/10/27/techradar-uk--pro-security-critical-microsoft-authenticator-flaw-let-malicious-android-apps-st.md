---
title: Critical Microsoft Authenticator flaw let malicious Android apps steal access
  to your precious accounts
source_url: https://www.techradar.com/pro/security/critical-microsoft-authenticator-flaw-let-malicious-android-apps-steal-access-to-your-precious-accounts
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-27T15:31:59Z'
published: '2026-10-27T00:00:00Z'
description: Authenticator was granting session tokens left and right
image: https://cdn.mos.cms.futurecdn.net/vAk5oh4pWzGeSY7xpMFAwR-2560-80.jpg
categories:
- Technology & Software
- Personal Finance & Investing
people: []
locations:
- Enclave
organisations:
- APK
- Enclave
- Google Play Store
- Microsoft Authenticator
- Microsoft Security Response Center
- Microsoft Teams
- TechRadar Pro
- URI
- Voila
---

![Futuristic biometric authentication technology concept. Man is touching a fingerprint scan with icons of secured access, data protection, network cyber security in digital interface.](https://cdn.mos.cms.futurecdn.net/vAk5oh4pWzGeSY7xpMFAwR-1920-80.jpg)

* **A critical Microsoft Authenticator flaw let rogue Android apps steal Microsoft session tokens without user interaction**
* **Attackers could impersonate trusted Microsoft apps and access emails, Teams data, calendars, and files**
* **Microsoft patched the bug and urges Android users to update Authenticator immediately**

A critical vulnerability in the Microsoft Authenticator app for Android allowed malicious apps to obtain session tokens for pretty much any Microsoft app and hand them over to the attackers.

Unlike other Android malware, this one did not require extensive permissions, the victims did not need to approve the login process, and the attackers did not need to know their victim’s login credentials.

Found by researchers at Enclave, the vulnerability, now tracked as CVE\_2026-80097, is fixed and Microsoft is urging all users to update their Authenticator app as soon as possible.

## What is Authenticator and how was it abused?

Authenticator is Microsoft’s two-factor authentication (2FA) app. Besides users, it also allows other apps to authenticate, giving them session tokens that grant them access to the users’ Microsoft work account and associated data. In practice, it means that a legitimate app such as Microsoft Teams can log into a user’s work account through Authenticator.

Enclave's security researchers set out to test how secure this process was. In an experiment, which they detailed on this link, they used an Android device that was logged into a Microsoft service and had the Authenticator app installed. Nothing less - nothing more.

Then, they installed a third app that was not malicious by any usual Android standards - it did not ask for extensive permissions, it did not contact a shady third-party server, and it did not try to exfiltrate any data.

What it did do, however, was pretend to be a legitimate Microsoft Teams app. As such, it asked Authenticator to, well, authenticate it, and grant it access to the data.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

To do that, it provided the necessary data: proper package name, client ID, and redirect URI. Authenticator confirmed the data was real and granted the app the token. Voila - the researchers were given access to emails, Teams chat messages, calendars, and were also allowed to modify and send messages, alter files, calendar entries, send chat messages, and even manage certain authentication methods (create or delete passkeys).

## A controlled experiment

How, you might ask? Apparently, Authenticator was just checking if the data the app provided was real - not the nature of the app providing the data itself. In other words, any app could have said “Hey, I’m Teams, give me a session token”, and would receive it.

The worst part is that this was all being done in the background. The researchers did not have to confirm the app’s login attempt, nor were they notified of it to begin with.

“We found that an unprivileged Android app with zero permissions could impersonate any installed Microsoft first-party app and have the Microsoft Authenticator broker hand it that app's tokens,” they said. This is a big deal, since asking for extensive permissions is the number one way to spot malicious Android apps.

Luckily for everyone involved, Enclave did not spot this attack in the wild and instead created it in a controlled environment. There is no evidence anyone tried anything similar in the wild, but now that the news is out, chances are they'll try. Therefore, it is vital all Authenticator users update their apps as soon as possible.

The silver lining in this report is that the malicious app still needs to land on the target Android device somehow. These apps likely won’t make it into the Google Play Store, and as long as users refrain from downloading shady .APK files from unvetted app stores, they should be fine.

Enclave reported the vulnerability to the Microsoft Security Response Center, which confirmed the issue and released a fix. It said that Microsoft Authenticator for Android versions earlier than 6.2606.4246 are affected and stressed that users should update to version 6.2606.4246 or later through the Google Play Store.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
