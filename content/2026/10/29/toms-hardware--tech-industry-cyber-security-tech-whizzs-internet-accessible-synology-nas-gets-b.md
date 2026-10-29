---
title: Tech whiz's internet-accessible Synology NAS gets bit by ransomware attack
  from 18-month-old remote code execution flaw — security updates neglected in a series
  of catastrophic errors
source_url: https://www.tomshardware.com/tech-industry/cyber-security/tech-whizzs-internet-accessible-synology-nas-gets-bit-by-ransomware-attack-from-18-month-old-remote-code-execution-flaw-security-updates-neglected-in-a-series-of-catastrophic-errors
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-29T18:33:21Z'
published: '2026-10-29T00:00:00Z'
description: In their defense, Synology's misleading update policies didn't help.
image: https://cdn.mos.cms.futurecdn.net/NiKV4fsALJWHimTDyVLD9o-1082-80.png
categories:
- Technology & Software
- Hardware
people:
- Bruno Ferreira
- Hwang
- NakamuraHwang
- Tom
locations: []
organisations:
- DSM
- Google News
- NAS
- PC
- Reddit
- Synology
- Tom's Hardware
---

![Synology](https://cdn.mos.cms.futurecdn.net/NiKV4fsALJWHimTDyVLD9o-1082-80.png)

Systems administrators are among the first to point out lax security policies in other companies' or people's setups. Sometimes, they are the ones who get bitten by not taking the same advice they will so readily dispense. Such is the tale of Reddit user NakamuraHwang, who had files on their Synology DS918+ NAS encrypted by a ransomware attack after making a series of unforced errors.

Hwang appears to be quite technically proficient and provided a detailed write-up of the situation. The key points, however, are that the unit in question (a) had its web interface exposed to the internet and (b) was roughly 18 months out-of-date with security patches. Just like the recent PHP snafu has adeptly shown, complacency is a far worse enemy than an army of AI bots.

The tech has a 3-2-1 backup setup, so they seemingly didn't lose any data. They attached the disks to a Proxmox machine for further inspection — Synology's DSM operating system uses mdraid underneath, so you can take the disks to another box and mount them there. Investigation of logs and the operating system files revealed that the attack was likely performed by abusing the CVE-2024-10441 remote code execution vulnerability, revealed a year and a half ago.

As most any other sysadmin will tell you, it's never advisable to expose devices directly to the internet without some layer of protection in between, chiefly but not only a VPN or an SSH tunnel. Tailscale, for instance, makes having a VPN fairly painless these days, and its free plan covers most home installations.

Synology had published its own advisory regarding the exploit, but that's where the NAS' behavior regarding updates complicates matters. According to multiple comments on the thread and in other forums, the UI will happily tell you that your device is up to date, all while there are critical security updates that need to be manually installed. The manual for DSM indicates that units from 2025 onwards have automatic updates, apparently implying that those of previous makes need to be configured so.

Furthermore, Synology apparently doesn't have a direct channel to warn its customers of critical security vulnerabilities —a simple e-mail notification would suffice. Although the firm is seemingly shifting away from consumer gear, it still sells small units that regular users might buy, and it's not reasonable to expect them to even be aware of security bulletins. Plus, package updates like the patch for the PHP2Shell vulnerability have to be installed separately, too.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G-140-80.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.

* "it says it is up to date"  
    
  Who wouldn't feel unsafe after months, let alone years without security updates?  
    
  One of my old cellphones hasn't had an update in years and I'm fully aware that it's an unsafe device (so I treat it as such), even though the manufacturer says that "it is up to date".  
    
  If automatic updates aren't working on your device, check manually (and there were plenty of updates), else search for alternatives because your device is not safe. Reply
* palladin9479 said:Exposing any admin interface to the web is a very VERY bad idea. That admin interface being an application web page makes it a ludicrously irresponsible bad idea.What exactly do you mean by admin interface on an application web page? I have access to google admin console at work through a google webpage. Does that count in your book as something 'ludicrously irresponsible'? Reply
* Worth checking UPnP on the router too. Synology can open ports on its own through it, so some people end up with the admin page exposed without ever forwarding anything themselves. If you need remote access, a VPN like Tailscale or WireGuard is the easy way around it.Reply
