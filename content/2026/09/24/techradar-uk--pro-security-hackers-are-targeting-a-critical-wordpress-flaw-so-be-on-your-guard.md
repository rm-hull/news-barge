---
title: Hackers are targeting a critical WordPress flaw, so be on your guard
source_url: https://www.techradar.com/pro/security/hackers-are-targeting-a-critical-wordpress-flaw-so-be-on-your-guard
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-24T16:43:44Z'
published: '2026-09-24T00:00:00Z'
description: Mitigations and a patch are already available, so update now
categories:
- Technology & Software
image: https://cdn.mos.cms.futurecdn.net/7NLZKWEKmFLJVAH4nubeaX-970-80.jpg
locations: []
people:
- Patchstack
- Robert Ressl
organisations:
- CVE
- Docker
- National Vulnerability Database
- Patchstack
- RCE
- TechRadar Pro
- WordPress
---

![WordPress logo on mobile](https://cdn.mos.cms.futurecdn.net/7NLZKWEKmFLJVAH4nubeaX.jpg)

* **WordPress Core flaw CVE‑2026‑87902 (path traversal, 8.1 severity) enables PHP file inclusion and possible RCE**
* **Patch released in v7.1.2 and backported to 4.7+; exploitation began within hours, now widespread**
* **Admins must urgently update; interim mitigations include blocking traversal sequences and disabling risky ARP/PHP settings**

Hackers are actively exploiting a high severity vulnerability in WordPress that can lead to full website takeover, researchers are saying. A patch is available, and WordPress users are urged to upgrade immediately or risk losing access to their assets.

Discovered by security researcher Robert Ressl, the vulnerability in question is tracked as CVE-2026-87902. It is an 8.1/10 (high severity) unauthenticated path traversal flaw affecting WordPress Core. According to WordPress itself, as well as the National Vulnerability Database, the bug can lead to local PHP file inclusion and, in certain scenarios, remote code execution (RCE).

"An unauthenticated attacker can make get\_page\_template() page-template resolution include a chosen readable local .php file outside the active theme directories," it was said in the official security advisory.

## Achieving RCE

WordPress is the world’s number one website hosting and builder platform, powering more than half of all websites active on the internet right now. However, that doesn’t mean all of them are susceptible to RCE. Only websites ticking these boxes are at risk:

Sites with parent or child themes that have a top-level directory with a name starting with ‘page-’ (for example, ‘page-templates).

Threat actors must target a local .PHP file that exists and is readable by the web server

The web server account must be able to read the included file (for example, pearcmd.php, if PHP’s register\_argc\_argv setting is active)

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

WordPress said that both the official PHP image for Docker, and the default cPanel configuration, are affected (users must be running a PHP version before 8.5, though).

The issue was fixed in version 7.1.2, which is now available for download. Fixes were also backported to older versions up to 4.7. Releases before 4.8 are not supported, it was said, and will not be getting a fix.

## Attacking vulnerable websites

Wordpress security company Patchstack said the first exploitation attempts started roughly five hours after the patch was released, and these were primarily reconnaissance efforts. In the hours to follow, malicious activity increased tenfold, it was said, as crooks started attempting to deliver malicious payloads to vulnerable websites, as well.

“When this post first went up, every request we had seen was reconnaissance against harmless core files,” Patchstack said. “That is no longer true. Attackers are now including pearcmd.php and using it to write PHP files to disk, and public scanning tooling for this CVE is in circulation.”

At first, Patchstack said the attacks were coming from a handful of IP addresses, and advised website admins to simply block them. However, the attacks have now become rather widespread, meaning blocking individual addresses is no longer a viable strategy. They urge everyone to apply the patch without delay:

“The first evening came from a small cluster of addresses. It is now spread across a few hundred, so blocklisting individual sources is not a strategy. The heaviest talkers at the time of writing:

43.250.53.42

180.251.159.243

195.178.110.247

107.189.14.87

45.61.184.170

92.246.130.76

The file write attempts specifically come from a much smaller subset of those addresses, which is the usual pattern of a few operators acting on results that a much larger scanning population produced.”

Those that cannot update immediately should reject traversal sequences in the pagename parameter, Patchstack added. A real page slug never contains one, they added, meaning it can be blocked without affecting normal traffic. Furthermore, disabling register\_argc\_argv does not fix the inclusion but it does break the pearcmd chain, which is the difference between an information leak and code execution.

*Via* * BleepingComputer*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png)

![Google logo on a black background next to text reading &#039;Click to follow TechRadar&#039;](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg)
