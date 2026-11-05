---
title: Hackers target French blood service fridges following supermarket attacks —
  Russia-aligned hackers claim intrusions are just to expose bad security
source_url: https://www.tomshardware.com/tech-industry/cyber-security/blood-banks-in-france-hit-by-temperature-raising-attacks-on-fridges-purported-hackers-claim-attacks-are-about-cybersecurity-not-malice
source_site: Tom's Hardware
source_slug: toms-hardware
description: Following the string of cyberattacks on supermarket freezers, blood banks
  in France were recently attacked.
image: https://cdn.mos.cms.futurecdn.net/CBTggBn4DkiVQJcprjXc-2048-80.jpg
published: '2026-11-05T00:00:00Z'
scraped_at: '2026-11-05T17:21:17Z'
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
people:
- Bruno Ferreira
- Burgundy-Franche-Comté
- Tom
locations:
- Copeland
- Dixell
- France
organisations:
- Coolworld
- Copeland/Dixell
- Danfoss
- EFS
- French Health Ministry
- Get Tom's Hardware
- Google News
- PC
- Telegram
- Tom's Hardware
- Z-Pentest
---

![Blood bank](https://cdn.mos.cms.futurecdn.net/CBTggBn4DkiVQJcprjXc-1920-80.jpg)

European fridges are *so hot* right now. Right on the heels of repeated cyberattacks on supermarket freezers, a fresh wave of attacks has hit units used by France's blood service (EFS). Thankfully, no biomaterials were lost, as the attack triggered the EFS' alerts, prompting staff to move the affected goods to proper storage.

![Nvidia](https://cdn.mos.cms.futurecdn.net/z53fPgXjpKHTpeGv3RHpqj-1200-80.png)

The French Health Ministry said that the situation is being closely monitored and that no assets were lost. The attack seemed focused on refrigeration units at three sites, with Burgundy-Franche-Comté reportedly among them. The EFS' communiqué says the intrusion was on a service provider, which some outlets are reporting as Coolworld.

Coolworld has posted a notice stating that the incident was due to "remote monitoring software" used in its systems, pinning the cause on "a component from a third-party supplier." There are no technical details available yet, so it's not yet clear if the hackers found internet-reachable equipment, as they did with the supermarket attacks.

It's possible that Coolworld keeps the controllers inside its own network and that malfeasants had to first gain entry to said network. However, it's worth noting that it was the EFS' monitoring and alarm system that noticed something was up — not the vendor's.

We don't know which brand of refrigerator controllers Coolworld uses, but the ongoing attacks seem to be happening on a per-vendor basis. Danfoss is the most-mentioned name — particularly, but not only, in the recent Nov. 1 - 2 attacks. Copeland/Dixell controllers were named in the Oct. 13 - 14 attacks.

A Danfoss datasheet recommends that its controllers are installed with "appropriately configured firewalls and secure LAN," and not "on any public or non secure network." That's not saying much, as punching holes in a firewall is nearly the same as having the unit directly reachable. The firm did issue a recent support bulletin clearly stating that the units should be installed with a VPN, but that document only appeared in October 2026. We couldn't find previous mention of this advice in our searches.

The manuals for the Copeland/Dixell controller units that were hit in earlier attacks advise installers to map ports 80 (web) and 22 (Secure Shell) to the internet so that the units can be reachable from the outside, suggesting a VPN only as an option. The firm has since published a security advisory recommending that the units only be reachable from inside a VPN. This was published Oct. 14, after the first wave of attacks.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Many news outlets claim to have seen materials — namely, in now-deleted Telegram posts — in which Russia-aligned hacking groups Noname057(16) and Z-Pentest are claiming responsibility for the attacks. Z-Pentest reportedly posted 2,500 lines of Danfoss code, but none of these alleged materials have been published. The purported hackers claim the attacks are about highlighting bad cybersecurity practices.

It's tempting to once again bring up AI agents as vehicles of cyber-destruction, but the reality is that, just like what happened with PHP, most of the time all bots are actually doing is revealing shoddy security practices and/or copious amounts of technological debt.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G-140-80.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.

* are just to expose bad security  
  no or you wouldnt cause damages (especially targeting blood which is finite and critical for some people to survive)  
    
  if you WERE only about showing bad security you'd msg them about it and show them you can do stuff at a specific time on a non critical thing so they can see it happen but also fix issue before causes a larger issue. Reply
