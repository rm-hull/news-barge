---
title: The privacy workaround prevents Windows from tracking you
source_url: https://www.techradar.com/pro/this-vpn-firm-has-created-a-way-to-stop-microsofts-hidden-tracking-tool-on-windows-although-it-will-break-some-key-cloud-services
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-09T16:49:48Z'
published: '2026-08-09T00:00:00Z'
description: A VPN company just found a way to block Microsoft's hidden Windows tracker
  without touching your internet connection
image: https://cdn.mos.cms.futurecdn.net/gqcnvTaWX8TaWF4LSNsEMj-970-80.jpg
---

![boss coworker spying on worker screen pc](https://cdn.mos.cms.futurecdn.net/gqcnvTaWX8TaWF4LSNsEMj.jpg) 

- **deGDID wipes cached tracking keys straight from the Windows registry permanently**
- **The script blocks Microsoft's DeviceAdd endpoint from ever seeing your device again**
- **Some Microsoft account and login services like login.live.com and account verification break once deGDID runs**

Windscribe has built an open source script called deGDID to strip a persistent tracking identifier from Windows systems entirely.

The tool targets Microsoft's Global Device Identifier, a permanent marker that operates beneath the network layer where VPNs function.

Its release follows a federal case in which the identifier reportedly helped the FBI locate an alleged hacker.

## How the script operates

The free script runs through PowerShell with administrator privileges and is available for download directly from GitHub.

It offers four execution flags that control its behaviour, starting with a read-only -Status check to confirm whether a GDID is active.

A -Status -Redact option generates diagnostic logs with the identifier hidden for safer sharing, while -Protect performs the core function.

This flag purges cached GDID keys from the registry and then modifies Access Control Lists and registry permissions to stop Windows from reissuing them.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

It further puts up a firewall against the internal DeviceAdd endpoint, cutting off Microsoft identity services from recognizing the machine as registered at all.

A fourth flag, —Unprotect, lets users reverse the process and restore default settings if needed.

Testing on a Windows 11 machine confirmed the script functioned as described, with the -Status flag revealing several cached identifiers before removal.

No new GDID appeared even after a system restart, though the trade-offs became apparent almost immediately afterward.

Account verification through login.live.com stopped working across every browser tested, while login.microsoftonline.com continued functioning without issue.

Some Microsoft applications returned connection errors, though online games and other software kept working normally throughout testing.

Users should still keep antivirus and endpoint protection active since deGDID addresses tracking rather than malicious software.

## Limitations of the workaround

Windscribe acknowledges that keys already stored on Microsoft's servers cannot be deleted, meaning the company retains indefinite access to previously collected data.

The script also refuses to run on managed systems or domain-joined accounts, restricting its use to individual unmanaged machines.

Windows currently offers no built-in method for disabling GDID, and the identifier persists across IP addresses regardless of any VPN tunneling applied.

"We tried the script on a Windows 11 computer, and it worked as intended," the company noted in its documentation of the testing process.

Windscribe describes deGDID as an ongoing research effort that will keep evolving as more details about the identifier's mechanics come to light.

The broken services represent a real cost for users weighing whether the privacy trade-off justifies losing certain Microsoft account functions.

Given that server-side keys remain permanently accessible to Microsoft, this script functions as a partial fix rather than a complete solution.

Via Tom's Hardware

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Efosa Udinmwen](https://cdn.mos.cms.futurecdn.net/nwRLdPUNG4rWu4Y6nthHDV.png)

Efosa has been writing about technology for over 7 years, initially driven by curiosity but now fueled by a strong passion for the field. He holds both a Master's and a PhD in sciences, which provided him with a solid foundation in analytical thinking.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
