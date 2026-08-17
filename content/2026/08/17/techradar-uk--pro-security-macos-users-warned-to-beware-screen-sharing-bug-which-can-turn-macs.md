---
title: MacOS users warned to beware screen-sharing bug which can turn Macs into cryptomining
  slaves
source_url: https://www.techradar.com/pro/security/macos-users-warned-to-beware-screen-sharing-bug-which-can-turn-macs-into-cryptomining-slaves
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-17T16:40:31Z'
published: '2026-08-17T00:00:00Z'
description: Apple patches critical-severity flaw in Screen Sharing
image: https://cdn.mos.cms.futurecdn.net/5HfdStguEjjwWA3HyeKfCZ-1920-80.jpg
---

![The Apple Mac Pro on a desk.](https://cdn.mos.cms.futurecdn.net/5HfdStguEjjwWA3HyeKfCZ.jpg) 

- **CVE‑2026‑65400 macOS Screen Sharing flaw exploited for cryptojacking within days of disclosure**
- **Attackers gained root via exposed port 5900 and deployed Monero miners using XMRig**
- **Apple patched in Sequoia 15.7.9, Sonoma 14.8.9, Tahoe 26.6.1; users urged to update immediately**

Less than a week after being publicly disclosed, a macOS vulnerability plaguing Screen Sharing was observed as being used in cryptojacking attacks.

Alfredo Pesoli, a security researcher from Bynario, discovered an authentication issue in macOS Screen Sharing and reported it to Apple. Screen Sharing is a built-in macOS tool that allows users to remotely connect, and use, another Mac device. It is similar to third-party tools such as AnyDesk or TeamViewer and comes in rather handy for IT teams accessing Macs stored in closets or used by remote and home-working employees.

The bug allows a remote attacker to bypass authentication and gain access to a vulnerable Mac device without valid credentials. It apparently stems from a logic issue in the Screen Sharing server’s authentication process, affecting systems where the service is exposed to the internet.

## The Netherlands issue a warning

Soon after disclosure, Apple released an out-of-bound fix, signaling that this is, indeed, a dangerous vulnerability. “Apple does not ship an update out of band unless something is critical,” security researchers Calif said in their technical writeup. The National Vulnerability Database (NVD) assigned it an identifier - CVE-2026-65400 - and gave it a severity rating of 9.6/10 (critical).

Approximately at the same time the patch was released, the flaw was also showcased at the 2026 Black Hat conference, with a video demonstration was made public a few days later.

Apple said it fixed it with improved state management, addressing the bug in macOS Sequoia 15.7.9, macOS Sonoma 14.8.9, macOS Tahoe 26.6.1.

Now, less than a week after the disclosure, researchers are saying the bug is being leveraged in actual cyberattacks, with Dutch security officials being first to react

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

“The NCSC has received a report showing that active abuse of this vulnerability has been observed on several systems on which port 5900 was accessible from the internet,” the Netherlands National Cyber Security Centrum (NCSC) said in a machine-translated report. “In all these cases, root access was gained on the affected system and a Monero crypto miner was placed.”

## Why Monero?

Monero is considered an “altcoin” - a cryptocurrency built as an alternative to Bitcoin. It is one of the oldest active altcoins out there, having been launched more than 12 years ago. Most cryptocurrencies rarely live through a single four-year bitcoin cycle but Monero, just like Ethereum, Litecoin, Solana, and a handful of others, endures.

It is similar to Bitcoin because it, too, can be “mined” (unlike Ethereum, for example). It differs on the privacy front. Unlike Bitcoin, whose transactions are recorded on a public ledger and can often be traced, Monero is designed to obscure the sender, recipient, and the amount of transactions. This privacy feature has, unfortunately, also attracted criminals.

Another key feature that made crooks choose Monero for their cryptojackers is the fact that the altcoin uses a proof-of-work (mining) algorithm optimized for general-purpose CPUs, making mining relatively profitable on ordinary servers, desktops, and cloud machines.

Although it was not specifically stated, it is safe to assume that in this incident, the attackers were deploying XMRig. It is, by far, the most popular cryptojacker and one that mines primarily Monero (its ticker is XMR).

## How to stay safe

The best way to go about it is to install the patch Apple just released. This effectively plugs the hole and makes the device secure. Those who are unable to deploy the patch immediately should block Screen Sharing and enable it only when it is actually needed and used. To do that, users can go to System Settings > General > Sharing and toggle the Screen Sharing switch off.

Finally, it is worth mentioning that the NCSC stressed the crooks could only exploit the flaw when the target device’s port 5900 is exposed to the internet. Therefore, setting routers and firewalls to block the port can also work, although we’d only recommend it as a last resort. Installing the patch is still the best way to go.

Right now, no groups claimed responsibility for this attack, and there is no evidence it is being used for anything else. In theory, though, it can also be used for data exfiltration, malware deployment, and possibly even ransomware attacks.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
