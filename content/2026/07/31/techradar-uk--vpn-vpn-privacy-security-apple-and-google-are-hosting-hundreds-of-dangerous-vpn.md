---
title: Apple and Google are hosting hundreds of dangerous VPN links — here is why
  your device is at risk
source_url: https://www.techradar.com/vpn/vpn-privacy-security/apple-and-google-are-hosting-hundreds-of-dangerous-vpn-links-here-is-why-your-device-is-at-risk
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-31T17:49:46Z'
published: '2026-07-31T00:00:00Z'
description: Our audit of over 4,000 VPN apps has uncovered that it doesn't take much
  for dangerous links to make their way onto store listings
image: https://cdn.mos.cms.futurecdn.net/VWHaco2FMgMv8k4qipihwP-2000-80.jpg
---

![Phone showing Google Play Store next to hand holding phone with warnings on it](https://cdn.mos.cms.futurecdn.net/VWHaco2FMgMv8k4qipihwP.jpg) 

When you download an app from the Apple App Store or Google Play Store, you assume the environment is heavily moderated and entirely safe. Unfortunately, we recently completed an audit of mobile VPNs that reveals significant privacy and security risks.

Our evaluation identified apps on both app stores that put visitors at risk of unencrypted traffic, hidden redirects, and active scareware.

The best VPNs will invest heavily in bug bounties and secure, authenticated web infrastructure. But there are a significant number of mobile VPN apps that leave you exposed to phishing and malware before you even install the app.

## Insecure protocols and obscured links

The biggest concern we found surrounds encryption enforcement. We found that **339 Android links (5.3%)** and**188 iOS links (6.8%)** use plain, unencrypted HTTP instead of secure HTTPS. This includes massively popular apps like**Oryx VPN**(which boasts over 1 million downloads) and** Stealth Shield VPN**.

### So what?

Clicking a plain HTTP link allows network eavesdroppers or **man-in-the-middle (MitM) attackers** to intercept, manipulate, or inject malicious content into the traffic between you and the developer's site.

But the security holes don't stop at missing encryption. The audit uncovered several other severely obscured URL formats being approved, such as:

- **URL Shorteners:** Multiple store listings rely on shorteners like-*shorturl.at* and the Yandex-based-*clck.ru*. This deliberately conceals the final destination domain, making it impossible for users or automated URL security scanners to evaluate link safety prior to clicking.
- **Raw IP Addresses:** Some listings use raw numerical IP addresses instead of domain names. This bypasses domain-based web filtering, SSL certificate validation, and public DNS reputation systems, effectively making connection security impossible to verify.
- **Direct PDF Links:** We found privacy policies pointing directly to downloadable PDF files (13 on iOS, 1 on Android). PDF documents can execute embedded JavaScript, trigger automated local file downloads, or easily exploit PDF reader vulnerabilities on your device.

## Active threats: scareware and malicious redirects

The most alarming discovery is that clicking a link on an official Apple or Google store page can lead to active cyber threats.

When developers abandon their apps, their official web domains often expire. It seems that actors are actively purchasing these expired domains specifically to exploit the existing app store traffic. In fact, our audit verified multiple active store listings containing domains that now host fake antivirus popups and ad redirects.

Users who trust these official app store links are tricked into viewing fake security warnings. These scareware popups are explicitly designed to coerce panicked users into downloading genuine malware to "fix" a fabricated virus.

In other instances, store links point to totally irrelevant and unvetted environments. Official links were found pointing to deleted Twitter handles, empty Facebook and Instagram pages, payment portals like Cashpay Iraq, and even Chinese opera sites.

Directing users to external messaging platforms like Telegram or abandoned social accounts bypasses web security standards entirely, exposing users to unmoderated third-party chat environments and severe impersonation risks.

## How to protect yourself

Its important that, regardless of inbuilt measures, consumers take matters into their own hands to some extent to navigate these listings safely. Always inspect link targets closely before blindly tapping on a developer website.

You should verify that the destination uses a secure HTTPS connection, and remain on high alert for obscured formats like raw numerical IP addresses or randomized link shorteners that conceal the true domain.

Furthermore, you should actively decline unexpected PDF downloads. Avoid opening direct PDF links from store pages, as these files may contain embedded JavaScript or exploit reader vulnerabilities. If tapping a privacy policy suddenly prompts an automatic file execution or download, block it immediately.

Finally, if an official app store link leads to a virus warning or requests system scanning permissions, recognize that it is a fabricated scareware scam designed to coerce you into downloading malware. Do not click anything on the page; close your browser tabs immediately to protect your device.

## The bottom line

Gaps in outbound link verification across the App Store and Google Play Store mean active security threats and unencrypted traffic can still slip onto mobile VPN product pages.

When we approached Apple and Google on our findings, Apple declined to comment on the record. Instead, we were pointed towards its safety guidelines and app review processes. A Google Spokesperson did comment, saying, "We are looking into this. When made aware of an app that violates our policies, we will review the apps in question and take appropriate action."

We also reached out to both Oryx VPN and Stealth Shield VPN, neither of which has returned to us with a response at the time of publication.

Ultimately, the lesson is that you must apply the same strict web security precautions inside official app stores as you would when navigating the open web.

![Rene Millman](https://cdn.mos.cms.futurecdn.net/DXDNjzRkphApxN8f5SooCA.png)

Rene Millman is a seasoned technology journalist whose work has appeared in The Guardian, the Financial Times, Computer Weekly, and IT Pro. With over two decades of experience as a reporter and editor, he specializes in making complex topics like cybersecurity, VPNs, and enterprise software accessible and engaging.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
