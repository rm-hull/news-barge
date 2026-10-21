---
title: Website admins across the world bracing for impact following major PHP flaw
  reveal
source_url: https://www.techradar.com/pro/security/website-admins-across-the-world-bracing-for-impact-following-major-php-flaw-reveal
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-21T17:12:23Z'
published: '2026-10-21T00:00:00Z'
description: PHP notifies the community of two critical RCE flaws
image: https://cdn.mos.cms.futurecdn.net/pL5rBKGq88cnoqgdJgCXGS-2560-80.jpg
categories:
- Technology & Software
people:
- Benjamin Harris
- Florian Roth
locations: []
organisations:
- ANNOUNCE
- BleepingComputer
- Hacker News
- Head of Research at Nextron Systems
- PHP 8
- RCE
- TechRadar Pro
---

![Cloud, networking and internet](https://cdn.mos.cms.futurecdn.net/pL5rBKGq88cnoqgdJgCXGS-1920-80.jpg)

* **PHP discloses two critical remote code execution vulnerabilities that could enable website takeover and data theft**
* **Details leaked before patch release, prompting an early security advisory and urgent upgrade warning**
* **Researchers confirmed the flaws are real, with widespread impact expected across multiple PHP versions**

PHP, arguably the most popular programming language for websites and web applications in the world, contains two critical-level vulnerabilities that could expose countless sites to remote code execution (RCE) attacks, the provider has revealed.

The flaws could lead to website takeovers, data theft, malicious redirects, and a whole swathe of similarly sinister situations.

## Security rush hour

PHP published a new security advisory, giving admins a “heads up” on an incoming patch.

“The PHP security team would like to give advance notice of an upcoming security release,” the advisory reads.

“It is scheduled for Wednesday, 21 October 2026 at 14:00 UTC. It addresses two critical vulnerabilities, both rated CVSS v4.0 9.2. All PHP users are encouraged to prepare now so they can upgrade as soon as the release is available. We reserve the right to release earlier should details of either vulnerability become public, or should evidence of active exploitation appear in the wild.Full details, affected versions, and the fixed versions will be published with the release.”

If you’re thinking the announcement is rather unorthodox and that PHP might as well just released the patch - you’re absolutely right. The problem is that someone spilled the beans on the vulnerabilities before the official embargo was lifted, having the cybersecurity community scrambling for answers.

That ‘someone’ is a person with an alias ‘petecooper’, who published a new post on Y Combinator’s Hacker News forum earlier this week. In the post, they claimed PHP would disclose two remote code execution bugs on October 22 2026.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The post has since been deleted so we couldn’t independently verify it, but *BleepingComputer* says the post claimed the bugs carried CVSS scores of 10.0 and affected PHP versions dating back to PHP 5.

The post also labeled the bugs as CVE-2026-109618 and CVE-2026-109619, which was subsequently confirmed. Therefore, the only thing that’s wrong is the CVSS score which seems to be 9.2, not 10.0.

Among the people who knew about the flaw and the upcoming patch were watchTowr, and Florian Roth, Head of Research at Nextron Systems.

The embargo on the news was set for October 20, with the patch due a day later, on October 21. However, yesterday Roth posted on X, saying “Okay, since the news is already out: an RCE vulnerability in PHP core, CVSS 10.0. Further details are scheduled for release on October 20. Only PHP 8 will receive patches.”

## Leaking the zero-days

This forced PHP’s hand, not just to release the advisory, but also to send a notice to its ANNOUNCE mailing list, according to *BleepingComputer*.

Security researchers watchTowr confirmed the news, saying the bugs are tracked as CVE-2026-109618 and CVE-2026-109619, and that the duo is being nicknamed “php2shell” by the community. Obviously, technical details are being withheld to protect users, but most likely affect PHP versions 5, 6, 7, and 8.

"In the last hour, two remote code execution vulnerabilities in PHP have been leaked. These vulnerabilities were previously scheduled under embargo and due for release on Thursday at 11 am ET," watchTowr CEO Benjamin Harris told *BleepingComputer*.

"While we are not able to share technical information at this point for obvious reasons, given the sensitivity, we can confirm that these vulnerabilities are indeed real. Both of them are CVSS10 and are understood to affect PHP versions 5, 6, 7, and 8."

The researchers also told the publication they managed to successfully reproduce CVE-2026-109618, confirming the flaws actually work. Good news is, there are still no confirmed reports of the flaws being used as zero-days in the wild.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
