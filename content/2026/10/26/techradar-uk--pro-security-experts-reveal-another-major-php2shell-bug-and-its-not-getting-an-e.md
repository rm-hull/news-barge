---
title: Experts reveal another major PHP2Shell bug — and it's not getting an emergency
  patch this time
source_url: https://www.techradar.com/pro/security/experts-reveal-another-major-php2shell-bug-and-its-not-getting-an-emergency-patch-this-time
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-26T20:31:09Z'
published: '2026-10-26T00:00:00Z'
description: PHP2Shell bug can trigger remote code execution
image: https://cdn.mos.cms.futurecdn.net/x4SmwpYXk8yGgDmYCVeckL-2560-80.jpg
categories:
- Technology & Software
people:
- Yotam Perkal
locations:
- Europe
organisations:
- ASLR
- Amazon Web Services
- Chainguard
- PHP Security Team
- Pluto Security
- RCE
- TechRadar Pro
---

![A hand about to touch a phone. Superimposed on top of it is a pink triangle with exclamation mark inside it. Behind it is a computer display with code on it](https://cdn.mos.cms.futurecdn.net/x4SmwpYXk8yGgDmYCVeckL-1920-80.jpg)

* **PHP disclosed a new RCE vulnerability, but exploitation requires a rare and specific configuration setup**
* **Unlike php2shell, the flaw will be fixed in the next regular release rather than an emergency patch**
* **Researchers say php2shell attacks remain limited so far, though widespread patching is still urgently needed**

The PHP Security Team has discovered yet another remote code execution (RCE) vulnerability in the now-notorious programming code, but since the issue is not that easy to abuse, it won’t receive an out-of-bounds fix.

The organization recently published a new security advisory warning users about a session upload progress bug in PHP, tracked as CVE-2026-115560. In the advisory, the organization said the bug can only be abused “under an unusual combination of configuration and application code”.

“An application must set session.serialize\_handler to php\_binary or php\_serialize in its configuration and then switch it to php at runtime with ini\_set() before calling session\_start(). Session upload progress must also still be enabled. Applications that never change the serialize handler at runtime can keep the feature enabled,” the advisory reads.

So, unless your setup has these exact settings, you’re not at risk. The PHP Security Team also suggests users set session.upload\_progress.enabled=0 until the next regular bugfix release, to fully protect from this RCE vector, which they explained as “unlikely”. They also said this setting was listed as a mitigation for CVE-2026-109619, so users who applied it then should just keep it and do nothing else.

## PHP2Shell

CVE-2026-109619 is one of two critical-severity RCE vulnerabilities recently discovered and dubbed “php2shell”, the discovery of which caused widespread panic, since the implications were monumental, to put it mildly.

PHP is an extremely popular programming language used to build websites and web apps. Some analysts claim that roughly 70% of all websites on the internet are running PHP, including banking, education, healthcare, and government sites. It was revealed that the PHP Security Team was working on a fix for php2shell and that a handful of security organizations knew, or were involved in the work. The bugs allowed threat actors to take full control over the websites.

The organizations were told not to break the news until a patch was released, in order not to alert cybercriminals of the existence of the flaws. However, information somehow leaked, and Amazon Web Services’ team saw exploitation attempts four days before the patch was due.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

A few hours before the release, the CEO of security outfit Chainguard published container images containing fixes for the flaws, effectively breaking the embargo. The security community blamed him for what happened next - the number of attempted exploits grew to a few hundred, then a few thousands, then into the millions - all in a few hours following the release of the patch.

The PHP Security Team tried to mitigate the damage by issuing a “heads up” alert - telling IT teams to prepare and wait for the patch, which was scheduled for October 21.

## Saved by ASLR

This mass exploitation campaign - apparently launched by multiple threat actors - is what caused widespread panic. According to different sources, healthcare, government, and education companies across Europe preemptively shut down their websites as they waited for the fix. However, despite the seriousness of the flaw and the speed at which threat actors picked it up - very few breaches actually happened.

As it turns out - exploiting php2shell is not as easy as it seems, likely thanks to a feature called Address Space Layout Randomization (ASLR). This security feature randomly changes where a program’s code and data are stored in memory every time it runs, allegedly complicating things for the attackers:

“PHP2Shell doesn't seem trivial to exploit. I believe that part of the reason we’ve yet to see successful exploitation is that reliable code execution requires getting past ASLR, a memory protection that randomizes where code sits in memory,” said Yotam Perkal, Director of Security Research at Pluto Security. “That's hard to do remotely, and most of the public PoCs floating around (many of them vibe coded) simply don't work reliably on real systems.”

This is great news, but Perkal believes the best ASLR can do is buy security teams a little time: “I wouldn't count on it staying that way, though. Exploits will get better, and most PHP servers out there are still unpatched, so teams should patch and restart their PHP workers now. But compared with all the drama before and after the release, real-world exploitation so far looks pretty limited.”

*Via* * BleepingComputer*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
