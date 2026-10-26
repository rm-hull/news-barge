---
title: Lack of staff and funding likely led to the recent PHP security snafu; project
  has only one full-time employee, but that's just the tip of the iceberg — a dreary
  situation caused by services running old versions with no support
source_url: https://www.tomshardware.com/tech-industry/cyber-security/lack-of-funding-likely-led-to-the-recent-php-security-snafu-but-thats-just-the-tip-of-the-iceberg-a-dreary-situation-caused-by-services-running-old-versions-with-no-support
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-26T12:54:40Z'
published: '2026-10-26T00:00:00Z'
description: Never underestimate the power of complacency, the destroyer of internets.
image: https://cdn.mos.cms.futurecdn.net/treU54HC35g9uxgWUT2cYD-1920-80.png
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
people:
- Bruno Ferreira
- Elizabeth Barron
locations: []
organisations:
- AI
- Chainguard
- Get Tom's Hardware
- PC
- PHP Foundation
- PHP2Shell
- Reuters
- Tom's Hardware
---

![PHP vulnerability](https://cdn.mos.cms.futurecdn.net/treU54HC35g9uxgWUT2cYD-1920-80.png)

The AI-powered inrush of software vulnerability reports over the last year has shined a light on how many critical pieces of open-source software are chronically underfunded. The latest victim is PHP, the scripting language powering about 71% of websites, making the news due to a critical remote code execution vulnerability. The PHP Foundation, which develops and oversees the language, reportedly counts only one full-time person and 14 "mostly part-time" contractors. That's bad enough, but the real problem goes far deeper thanks to the internet's lazy development practices and systems administration.

In an interview with *Reuters*, the PHP Foundation's Executive Director Elizabeth Barron spells it out clearly: she's the only full-time person on staff, and works with the contractors' help. Pertaining to the software itself, the team's job is to develop and maintain the PHP core, including taking care of security fixes. The core team accepts contributions from the world at large, in an arrangement not too dissimilar to Linux kernel development — except that project is far better-manned, with many full-time contributors and company-employed developers.

Naturally, the PHP foundation collaborates with other companies and many cybersecurity firms, but the dev team was stretched thin even before the increase in security vulnerabilities with the help of countless AI agents. Barron does note that there was no reported exploitation of PHP2Shell before the security fix came out.

But the lack of a higher funding level likely led to the "structural failure" to address the underlying vulnerability in a timely manner, as the out-of-memory condition (OOM) that eventually led to the 2026 exploits was originally discovered in 2024. Given how widespread PHP is, and how many third-party extensions there are, the work on fixing the OOM problem "stalled and restarted repeatedly over months." It didn't help that the Chainguard security firm broke the PHP2Shell embargo too early by accident.

Even still, the team is thankful for the money it has, as "without the Foundation’s funding it would have been impossible to have multiple people work on this issue full time, eventually through weekends and around the clock to coordinate and communicate with other involved parties." One would hope that this latest incident releases the purse strings of more companies that make their living off of PHP.

And yet, this failing is far larger than just bugs in the core language, which, notably, were only one point update away. In theory, any server running the current 8.x brand of the software *should* be upgraded in minutes with the released patches, but reality was far different, as websites went down for hours or days out of fear of exploitation.

The **real** problem reared its ugly head: nearly 73% of PHP installations were running versions well past their end-of-life (EOL) date, meaning that obtaining fixes is now far harder. Many professionals who worked with the language, including yours truly, had spent decades warning of this reckoning, even considering many Linux distributions were backporting fixes.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Many of these servers were still running PHP 7, a version that was completely EOL'd *four years ago*, with many years of advance warning, and that originally came out in late 2015, almost* eleven* years back. If that doesn't sound silly enough, let it sink in that around 7.7% of PHP sites were still running version 5.x, which first saw the light of day 22 years ago in 2005, and saw the final sunset in 2018. It's safe to say that everyone had plenty of time to prepare.

To further illustrate the ridiculousness of collective complacency: the jump from PHP 5 to 7 and then from 7 to 8 required changing sections of website code, but the vast majority of said changes are simple to find and apply, and even before AI, there were already automated code-patching tools around. A couple years ago I mapped them all out for a PHP 5-to-8 codebase conversion myself.

Most of the alterations were about dropping support for ancient functions and libraries, which themselves had had long-standing warnings of incoming deprecation. Not a lot of core language features underwent modification, and a lot of convenient syntax was added to help clarify fiddly, error-prone code, too. That the overall situation got to this point beggars belief and illustrates how complacency, laziness, and cost-cutting are a far bigger force than a cadre of AI bots digging for flaws.

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G-140-80.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.

* PHP7 to PHP8 is a major version change that is not fully backwards compatible. So it is understandable that people did not upgrade, preferring to run already written and debugged code with PHP7.Reply
