---
title: VPN provider built a script to block Microsoft's hidden GDID tracking on Windows
  — Windscribe's "deGDID" erases existing identifiers and blocks new ones from being
  created
source_url: https://www.tomshardware.com/software/windows/vpn-provider-windscribe-has-built-a-script-to-block-microsofts-persistent-gdid-tracking-on-windows-degdid-erases-existing-identifiers-and-blocks-new-ones-from-being-created
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-06T14:32:30Z'
published: '2026-08-06T00:00:00Z'
description: But there's a (small) downside.
image: https://cdn.mos.cms.futurecdn.net/A3bqjPsbEd6W9WtTAebSpJ-1920-80.jpg
---

![Windows 11](https://cdn.mos.cms.futurecdn.net/A3bqjPsbEd6W9WtTAebSpJ.jpg) 

Last month, we covered a federal criminal case in which Microsoft's Global Device Identifier (GDID) helped the FBI catch an alleged hacker. Despite the noble cause, the implications of a persistent tracker built into Windows became difficult to ignore, and it was enough of a tipping point to convince Windscribe to do something about it. The VPN company has created an open-source project and script called "deGDID" that aims to strip GDID off your PC — but does so at the cost of breaking some Microsoft cloud services.

 ![A hand holding the Ryzen 7 9850X3D.](https://cdn.mos.cms.futurecdn.net/Xh2MupWrRjJPiLLuopmKRB.jpg) 


You can find the script on GitHub and run it via PowerShell with admin privileges. It's completely free and works in a very straightforward manner. There are three main execution flags that dictate how deGDID operates: *–Status*, which is read-only and tells you if a GDID is active on your rig;*–Status –Redact*, which generates logs with the GDID redacted so users can share diagnostic data more confidently; and*–Protect*, which completely wipes the GDID and prevents the creation of new ones.

![Running the deGDID script](https://cdn.mos.cms.futurecdn.net/orE8jHz2MDuNryRPQUaF8T-1171-80.png) 

![Running the deGDID script](https://cdn.mos.cms.futurecdn.net/mZBhYTLVnCoqLnabMeoJ5T-1171-80.png) 

![Running the deGDID script](https://cdn.mos.cms.futurecdn.net/orE8jHz2MDuNryRPQUaF8T-1171-80.png) 

![Running the deGDID script](https://cdn.mos.cms.futurecdn.net/mZBhYTLVnCoqLnabMeoJ5T-1171-80.png) 

A fourth flag, *–Unprotect*, allows you to reverse the script in case you need to revert back to the default state. But*–Protect* is the one worth discussing. First, the script looks for server-issued GDID keys in the registry, where they remain cached, and purges them all. This is something you can do manually as well. In fact, Windscribe tried it on a virtual machine, but the GDID keys are silently re-minted in the background upon a reboot or whenever Windows contacts Microsoft servers again.

To close this loop, the script then modifies the ACLs (Access Control Lists) and registry permissions to prevent the OS from fetching and subsequently trying to remint the GDID keys. It puts up a firewall against the internal *DeviceAdd* endpoint, which completely cuts off Microsoft identity services from even seeing this as a registered Windows PC. This one-two punch completes the process, and the existing GDID keys are not only wiped, but the possibility of new ones being created is put to bed as well.

 ![Running the deGDID script](https://cdn.mos.cms.futurecdn.net/CQByWvD5yg4sXMqyHoWz3T.png) 


Keep in mind that old keys that are already server-side cannot be removed; Microsoft has access to them indefinitely. This script also only works on unmanaged systems with admin accounts. If you're part of an organization or domain, deGDID will refuse to run. More importantly, though, since it blocks Microsoft's *DeviceAdd* pipeline, some core Windows services will break because they'll fail to authenticate your Microsoft account.

The reason deGDID is even needed in the first place is that Windows has no native toggle to turn off GDID. It exists as a permanent device ID that can track you without your consent. It works across IP addresses since it sits beneath the layer where VPNs operate, so no amount of network tunneling can obfuscate it. This can explain why Windscribe was compelled to create deGDID — to combat a potentially invasive system that has the power to wreak havoc in the wrong hands.

 ![Microsoft online services degraded after running the deGDID script](https://cdn.mos.cms.futurecdn.net/dmaZB6d2RqkZfDhpWtPMLR.png) 


We tried the script on a Windows 11 computer, and it worked as intended. Running the *–Status* flag showed multiple cached GDIDs that were then removed by the*–Protect* flag, and a new GDID didn't show up even after restarting. As expected, some Microsoft apps freaked out and returned connection errors. Account verification through *login.live.com* was also blocked across all browsers, though*login.microsoftonline.com* still worked. Online games and other apps continued to behave normally as well.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Windscribe says deGDID is a research project, and it will continue to evolve as more information about how GDID works is uncovered. For now, the fact that it can make core Microsoft services and features fail might be too much of a tradeoff for some. The script also doesn't promise to kill every GDID instance, and Microsoft already has your previous keys, so this is certainly not an ideal solution — but it's a good start to the fight against hidden trackers.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Hassam Nasir](https://cdn.mos.cms.futurecdn.net/SxxNFHt95eGK37mKPhJpdZ.jpg)

Hassam Nasir is a die-hard hardware enthusiast with years of experience as a tech editor and writer, focusing on detailed CPU comparisons and general hardware news. When he’s not working, you’ll find him bending tubes for his ever-evolving custom water-loop gaming rig or benchmarking the latest CPUs and GPUs just for fun.

- 
Reply
 I read that and went "pfft. Don't threaten me with a good time." Making it more difficult for Microslop to store your data is always a bonusRabohinf said:" . . . cost of breaking some Microsoft cloud services."
 
 Cost? That's a benefit!
