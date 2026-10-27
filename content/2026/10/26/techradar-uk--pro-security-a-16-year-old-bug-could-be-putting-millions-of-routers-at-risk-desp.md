---
title: A 16-year-old bug could be putting millions of routers at risk — despite Broadcom
  saying it patched the issue years ago
source_url: https://www.techradar.com/pro/security/a-16-year-old-bug-could-be-putting-millions-of-routers-at-risk-despite-broadcom-saying-it-patched-the-issue-years-ago
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-27T00:23:59Z'
published: '2026-10-26T00:00:00Z'
description: Broadcom says it fixed this 16-year-old Wi-Fi flaw in 2018, but the fix
  never reached the routers, and attackers in range need no password
image: https://cdn.mos.cms.futurecdn.net/S2k99RTyJJhGbDwQRHUsyg-970-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Broadcom
- Quentin Kaiser
locations:
- Russia
organisations:
- AI
- APT28
- Broadcom
- CVE Numbering Authority
- Codex
- Cybernews
- FBI
- ISP
- Kaiser
- OpenAI
- Orange Belgium
- TechRadar Pro
- WPS Monitor
---

![An abstract image of digital security.](https://cdn.mos.cms.futurecdn.net/S2k99RTyJJhGbDwQRHUsyg-970-80.jpg)

* **A Broadcom WPS flaw dating back to at least 2010 lets attackers within Wi-Fi range run code on routers without the password**
* **Broadcom told the researcher it replaced the code from 2018, but declined to assign a CVE, calling the software obsolete**
* **Changing your Wi-Fi password won't help, and disabling WPS may not either; firmware updates or replacement are the fix**

A flaw in Broadcom's Wi-Fi software dating back to at least 2010 lets anyone within radio range take over a vulnerable router without its password, and the fix Broadcom says it shipped years ago never reached many routers that need it.

Security researcher Quentin Kaiser presented the bug at the recent Hexacon event alongside a detailed write-up, naming it 'WPSplinter', a name he admits to disliking; with no CVE assigned, it is the only label the flaw has.

The bug sits in Broadcom's legacy WPS Monitor, the component that handles Wi-Fi Protected Setup, the push-button pairing feature found on many home routers. When WPS messages arrive in fragments, the software stitches them back together without checking that the result fits in the memory set aside for it.

## No password, no pairing, no problem?

According to Kaiser's public documentation page, an attacker can reach that code over the air before any pairing completes, so no PIN, no button press and no network key are required. The upshot: anyone in range can read the router's memory and run code on it. Unlike the WPS PIN brute-forcing attacks of the early 2010s, the weakness is in Broadcom's code, not the protocol itself.

On an Askey TCG3000 gateway supplied by Orange Belgium, Kaiser's code pulled the Wi-Fi password from the router's storage and sent it over the air; he then used it to join the network. On a Sagemcom-built Proximus BBOX3V+, he opened a remote shell running entirely over Wi-Fi frames. He says the attack works at long range, though he has not published a distance. His summary: "you can get a root shell from across the street" on a significant share of Belgian routers.

Kaiser reported the flaw to Broadcom in July 2026, starting a 90-day disclosure clock. On July 28, Broadcom replied that a patch was available and told him to contact affected manufacturers. By Kaiser's account, the company also said it had known about the bug since 2018, had heard about it from others, and had been replacing WPS Monitor with the open-source hostapd since then.

Broadcom's official position is that this was fixed years ago. The real question is what that fix amounted to. Kaiser says the 2018 patch to the old code was incomplete and went out silently, and that Broadcom's real answer was a newer software kit that drops the vulnerable component altogether, which only helps if device makers migrate.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

On Broadcom's older eCos-based chips (BCM3380, BCM3383 and BCM33834) there is no migration path, making this what Kaiser calls a forever day: a flaw that will never be fixed. Linux-based BCM3390, BCM63xx, BCM65xx and BCM68xx hardware can be fixed, but only if each manufacturer does the porting work, sometimes for products years out of support. Broadcom has issued no public advisory, and its position is known only through Kaiser's account of their correspondence.

Broadcom also declined to request a CVE, telling Kaiser the software was obsolete and outside its support window, and refused to share the notice it says it sent manufacturers. Because Broadcom is itself a CVE Numbering Authority, it effectively decides whether flaws in its own products get an identifier.

Because the attack happens before any login, changing your Wi-Fi password does nothing. Turning off WPS in the router's settings may not help either, as Kaiser's documentation warns: "A settings toggle may not remove or fully disable the vulnerable parser." The exception appears to be an ISP disabling WPS centrally, but it is unclear as to how many will follow through.

For everyone else, the real fix is a firmware update from your ISP or router maker, or, for older eCos-based hardware, an outright replacement. Users renting their gateway need to ask their providers whether its firmware still includes Broadcom's legacy WPS code.

Kaiser credits AI with cutting the work from months to under a week, and Cybernews reports he used OpenAI's Codex agent. That cuts both ways: attackers have the same tools, and Kaiser argues that hard-to-monitor, over-the-air access like this is ideal for targeted operations, such as Russia's APT28 reaching a target through a neighboring organization's Wi-Fi, or Midnight Blizzard hijacking hotel Wi-Fi login portals to infect travelers.

Broadcom chips were also at the center of the Kr00k Wi-Fi flaw in 2020, though device makers have since issued a CVE and patches. Unsupported routers tend to become someone else's infrastructure, as the FBI warned in May 2025.

Kaiser joked that at 16 years old, the bug is now old enough to order a beer at a Belgian bar. Broadcom currently considers the code retired, but the underlying hardware still runs in thousands of households as well as commercial places to date.
