---
title: Modern software is built on the backs of low-paid maintainers, opening the
  door to potential threats — report details critically underfunded projects that
  remain understaffed or unfunded
source_url: https://www.tomshardware.com/tech-industry/cyber-security/modern-software-is-built-on-the-backs-of-low-paid-maintainers-opening-the-door-to-potential-threats-report-details-critically-underfunded-projects-that-remain-understaffed-or-unfunded
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-20T14:20:25Z'
published: '2026-10-20T00:00:00Z'
description: Modern computing remains vulnerable to the low bus factor of many open-source
  projects — continued lack of funding and manpower for voluntary-maintained infrastructure
  makes for a perennial threat
image: https://cdn.mos.cms.futurecdn.net/zAKMPdMzn6uvTf3sxZsDgA-1920-80.jpg
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
people:
- Bash
- Bruno Ferreira
- Chet Ramey
- D.R. Commander aka DRC
- Daniel Stenberg
- Denis Pushkarev
- Dirk Lemstra
- Nick Wellnhofer
- Paul Eggert
locations:
- Behdad Esfahbod
- Germany
- HarfBuzz
- Middle Eastern
organisations:
- AI
- Apache Log4j
- Dropbox
- Esfahbod
- FFmpeg
- ImageMagick
- Libjpeg-turbo
- Libxml2
- Open Collective
- PC
- SQLite
- Sovereign Tech Agency
- Tom's Hardware
- UCLA
- WhatsApp
---

![Boxes stacked on top of one another](https://cdn.mos.cms.futurecdn.net/zAKMPdMzn6uvTf3sxZsDgA-1920-80.jpg)

Modern computing systems and devices typically require pieces of crucial open-source software, typically maintained by unpaid or low-paid volunteers. Recently, a report collated a list of critical open-source projects, noting which of them are chronically underfunded and/or understaffed. The information is sobering: 11 out of 23 of the listed projects currently only have one or two maintainers, and funding is generally scarce and sometimes nonexistent.

The Data Drop's report on open-source maintainers identifies that having only one or two sets of eyes on critical pieces of software means that sooner or later something breaks — and it tends to do so in spectacular fashion, given its ubiquity. So, what happens when these projects, which are widely used across software, go underfunded or understaffed?

## Lessons from the past

In 2014, the same year as Heartbleed, Shellshock made waves: a vulnerability in the Bash shell that's present in Linux, macOS, and Unix-type systems. The problem was traced back to a line of code present since 1989, displaying how even software that's thought to have all the bugs hammered out of it can still fall prey to attacks. A quick look at Bash's commit history shows it's almost exclusively maintained by Chet Ramey.

In 2016, ImageMagick was exploited, providing attackers with remote code execution. This library is used for image manipulation across a wide range of software, in webpages, mobile apps, and more. A 2020 analysis revealed that hundreds of security issues had been found over the years in its extensive codebase. Nearly every code contribution in the past couple of years has been done by an individual named Dirk Lemstra.

Contemporary examples include 2021's Log4Shell exploit, a critical vulnerability in the Apache Log4j logging library used in millions of servers. The libwebp image-handling library saw a zero-day vulnerability in 2023, and the xz compression library used across Linux and iOS was compromised in 2024.

## Thankless work

Key points in the report mention specific repos, which might be under threat. Somewhat unsurprisingly, the low number of overall maintainers and the unpaid nature of the work make it unattractive to perform.

The main time-zone file used across Linux-based operating systems is maintained pro bono by Paul Eggert, a UCLA teacher. Core-js, a piece of support software that lets new JavaScript work in old browsers and is estimated by the author to be used in half of the busiest websites in the world, is handled by Denis Pushkarev. He once had to endure criticism from the community because he added a command-line message to the library's installer asking for help or a job.

The HarfBuzz library developed by Behdad Esfahbod is a cornerstone in ligatures and text shaping in Middle Eastern languages. In those writings, a letter changes shape and/or orientation according to what's around it. Esfahbod handles that vast majority of the project's code, and doesn't mention public or corporate funding.

Libjpeg-turbo handles JPEG images on Android, Firefox, LibreOffice, and every Chromium-based browser. It's kept ship-shape by D.R. Commander aka DRC, who occasionally is contracted for library-specific work, though at arguably modest values of "3-4 figures rather than 6 or 7." Libxml2, just like the label says, handles XML reading and writing across numerous applications and operating systems. Nick Wellnhofer, the original maintainer, stepped down in September 2025, after years of work with little income.

The SQLite project provides a one-file database that's exceedingly easy to integrate into most software, instead of complicated, resource-heavy databases, while still retaining standard SQL language and accouterments. Thanks to its ease of use, it found its way into an astonishing number of applications. Examples include WhatsApp, Dropbox, Android, Windows, and all major browsers.

The project estimates that there are about a trillion instances of SQLite in use. Just four people keep this critical project together, and they've gone to the length of removing their names and photos from the project's page, as "there are a lot of crazy people in the world who might misuse that information." The project is funded by the offering paid support via the founder's company, though there's no word on effective income, especially when it presumably needs to feed four mouths.

## Funding is there, but scarce

It's not all doom and gloom, though. Take curl (the software), for example. Almost every developer has used it, thanks to its URL-fetching abilities and extensive scripting options. The project was started by Daniel Stenberg, who is now paid to work full-time on it. The team has now grown to 11 and has received funding through Open Collective and Germany's Sovereign Tech Agency, among others.

Likely due to the lessons learned from their past respective debacles, both the Log4j and OpenSSL projects are likewise funded by the Sovereign Tech Agency, as are the FFmpeg video file handler and the OpenSSH secure shell software that's ubiquitous in Linux servers.

All things considered, it's easy to argue that the critical importance of all the aforementioned software merits sizable investments from industry players, especially those whose commercial products benefit the most from the community's efforts. Plus, even if the firms feel no moral obligation to contribute, in the day and age where AI agents are finding exploitable vulnerabilities in hours, donations to these open-source projects could also be considered investments.

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G-140-80.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.
