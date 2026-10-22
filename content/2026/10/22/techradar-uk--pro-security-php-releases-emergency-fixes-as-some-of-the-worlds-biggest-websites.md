---
title: PHP releases emergency fixes as some of the world's biggest websites say they
  were targeted by hackers
source_url: https://www.techradar.com/pro/security/php-releases-emergency-fixes-as-some-of-the-worlds-biggest-websites-say-they-were-targeted-by-hackers
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-22T11:46:25Z'
published: '2026-10-22T00:00:00Z'
description: The php2shell bug is being actively exploited
image: https://cdn.mos.cms.futurecdn.net/B73DML5s9XT2asace74Gnd-1920-80.jpg
categories:
- Technology & Software
people:
- Dane Knecht
- Florian Roth
locations:
- Europe
organisations:
- Admins
- BleepingComputer
- CTO
- Cloudflare
- Head of Research at Nextron Systems
- LTS
- PHP
- Reuters
- TechRadar Pro
- VirusTotal
---

![A close-up of an interent search bar with &#039;http://ww&#039; visible](https://cdn.mos.cms.futurecdn.net/B73DML5s9XT2asace74Gnd-1920-80.jpg)

* **PHP released fixes for two critical remote code execution flaws and urged immediate patching**
* **Security researchers and Cloudflare reported early exploitation attempts before patches became available**
* **Millions of internet-facing PHP installations may be at risk, especially unsupported legacy versions**

PHP has released patches for two critical remote code execution (RCE) vulnerabilities and “strongly encouraged” all users to apply them as soon as possible, as hackers are starting to abuse the flaws in real-life attacks.

PHP issued a new security advisory saying it addressed CVE-2026-109618 and CVE-2026-109619 with a patch. The former is an out-of-memory handling bug, while the latter is a use-after-free memory error. Both were assigned a severity score of 9.2/10 (critical).

The vulnerabilities were addressed in PHP versions 8.5.12, 8.4.27, 8.3.36, and 8.2.35. Users can download the versions from PHP’s downloads pages, with Windows source and binaries being on the same page. Linux distributions and LTS vendors received the patches in advance, it was said, so users should check with their vendors for updated packages.

## Shaking the internet’s foundations

PHP is among the most popular programming languages for websites and web applications in the world, so when remote code execution zero-days are found, it’s a big deal.

PHP was supposed to work on a solution in silence, not to give cybercriminals a head start on exploitation. However, information about the vulnerabilities leaked on the internet two days in advance, causing serious panic, and according to *Reuters* multiple government, healthcare, and education websites across Europe decided to temporarily shut down to prevent being targeted.

Different sources made different claims. For example, Florian Roth, Head of Research at Nextron Systems, said both flaws would be given a 10/10 severity score, which did not happen. He also said only PHP 8 would be patched, which turned out to be true, despite other sources claiming PHP down to version 5 being fixed.

This, too, is a huge deal, since it’s safe to say that millions of websites are running older, end-of-life PHP versions, and could now be targeted with relative ease. Citing VirusTotal, *BleepingComputer* said more than 5.1 million PHP hosts are currently exposed online, with some 3.8 million having at least one port open.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

According to PHP, “all PHP installations serving web requests, including PHP-FPM, Apache with mod\_php, php-cgi, FrankenPHP and LiteSpeed,” are at risk.“We consider the risk highest for mod\_php, with a demonstrated exploit where an unauthenticated request can trigger the attack before any application code runs.”

## Unsupported versions

PHP 8.1 and older will not be fixed, so if you’re running any of those versions, you’re in danger. Cloudflare’s CTO, Dane Knecht, said the company is “seeing early attacks emerging” and is updating mitigations as new vectors show up. This was a few hours before PHP released the fixes. “Given the severity of these vulnerabilities, the PHP security team provided minimal source-backports for PHP 7.4, PHP 8.0, and PHP 8.1 to help people building from source or without access to an LTS vendor,” PHP added.

The safest play here is to update PHP. For those that cannot do that immediately, PHP recommends a few mitigations, but stresses that these are not a complete solution. For the out-of-memory flaw, the maintainers recommend setting memory limits appropriately, and restricting the size of incoming requests, including file uploads, to reduce the risk of memory-related attacks. Admins can use container limits to prevent a vulnerable worker from affecting the wider system, it was said.

For the use-after-free one, PHP says admins can disable session upload progress tracking and turn on fatal-error backtraces (on PHP 8.5). They should also fix application errors that could trigger crashes or timeouts and avoid outdated settings that generate error messages before the app is fully initialized.

*Via* * BleepingComputer*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
