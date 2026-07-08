---
title: Arrest and extradition of Scattered Spider hacker shines light on how Windows
  telemetry GDIDs can identify and track users — Microsoft device identifier is just
  one digital fingerprint in a software world rife with them
source_url: https://www.tomshardware.com/tech-industry/cyber-security/arrest-and-extradition-of-scattered-spider-hacker-shines-light-on-how-windows-telemetry-gdids-can-identify-users-microsoft-device-identifier-is-just-one-digital-fingerprint-in-a-software-world-rife-with-them
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-08T14:49:54Z'
published: '2026-07-08T00:00:00Z'
description: A harsh lesson on Windows telemetry, protecting online anonymity, and
  misinformation about defensive measures.
image: https://cdn.mos.cms.futurecdn.net/wqqUyuiXEd3qQNnhnBSYcQ-2121-80.jpg
---

![Digital fingerprint](https://cdn.mos.cms.futurecdn.net/wqqUyuiXEd3qQNnhnBSYcQ.jpg) 

The Internet is buzzing over news that 19-year-old Estonian "hacker" Peter Stokes got nabbed by the authorities and extradited to the U.S. on digital crime charges, mostly thanks to Microsoft Windows' built-in telemetry. The FBI seemingly subpoenaed Microsoft, which coughed up telemetry logs that contained both Stokes' GDID (Global Device Identifier) and websites he visited using his main Windows machine.

The existence of GDID isn't new by itself, as Windows telemetry's data collection has been extensively analyzed and reported on. It's also been known, and publicly explained by Microsoft, that the extended telemetry modes (Full/Optional instead of Required/Basic) can upload lists of URLs analyzed by SmartScreen and Defender, together with the GDID. In fact, using the Edge browser in this setup can even send every visited URL. The court documents do not reveal which exact mechanism triggered the telemetry upload, though.

This data collection has long been the source of heated debate and general public disgust. Even though the data is genuinely useful and necessary for debugging (by Microsoft or systems administrators in enterprise environments), the fact that it comes enabled by default in Windows Home and Professional editions is questionable. The fact that those versions don't have a simple, user-facing "Off" switch to fully disable telemetry also adds insult to injury.

The Peter Stokes arrest appears to be the first public case where these Windows GDIDs were both used as a tracking identifier and contained telemetry data including some of the URLs the defendant visited. The case also prompted a renewed analysis of the GDID by a security researcher that you might want to look into. From what we can ascertain, it's likely Stokes had his Windows telemetry set to Optional/Full, as Required/Basic doesn't appear to transmit URLs by default.

Using the telemetry GDID, the FBI easily connected the dashing rogue to his ngrokaccount, because he used that tool in the same session in which he accessed his Facebook and Snapchat accounts. The agents also established a link between travel records, a New York IP address, and a rental at the Empire Hotel, likely facilitated by the photos Stokes posted of his hotel room. The criminal mastermind was equally sneaky (read: not) in his visit to Thailand.

As many hackers do, he enjoyed some time off playing an obscure game, in this case Ubisoft's Growtopia, shortly before accessing his Apple logins, as well as the aforementioned Facebook and Snapchat logins over the following weeks. Besides Microsoft, Google and Apple also collaborated on the hunting effort, with Google linking Stokes' phishing phone number to the same exact IP address and date where he created the ngrok account. Ever the stealthy craftsman, Stokes had created the ngrok account using the same GMail address connected to a second phone number where he made phishing calls from.

While it's easy and arguably quite necessary to hoist pitchforks at Microsoft for collecting detailed information about billions of computers by default, security professionals will be quick to remind users that Windows' telemetry is merely one of the many ways to track a user. Even if not by malice, a lot of software simply *requires* GDID-like identifiers for things like tracking usage, subscription and licensing limitations, activation requests, and hardware detection. And every company behind such software can be subpoenaed by authorities, as exemplified in Stokes' case by Microsoft, Google, Apple, ngrok, and others. Even privacy-oriented services like Proton are careful enough to describe what they can and cannot reveal to authorities under a court order.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

If you're wondering the steps Stokes took to cover his tracks, though, you'd be looking at a small list. He did route his connections through a VPN hosted at servers from Tzulo along with the developer-oriented ngrok tunneling service and teleport.sh. Unfortunately, the modern digital world allows for many forms of identification, and hiding one's source IP address is merely one of them.

Using a VPN is recommended for digital anonymity, but it's merely the first of many necessary steps and can even backfire when not set up carefully. If misconfigured, a VPN may allow certain applications and operating system features to talk to the outside world using the original IP instead of the hidden one. Plus, the VPN will not stop the operating system or any application from sending out identifying information to begin with.

Perhaps more worryingly still, modern-day device and user fingerprinting is far more insidious and hard to counter. For example, plain web browsers are notorious leakers of personal information, as data-harvesting companies can weaponize features like TLS levels, HTML5 Canvas functionality, the fonts list, and even Widevine DRM in a combination that uniquely identifies a visitor. Stokes now has plenty of time to read up on the EFF's surveillance self-defense guides and get acquainted with the scripts at the Privacy Is Sexy website.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.
