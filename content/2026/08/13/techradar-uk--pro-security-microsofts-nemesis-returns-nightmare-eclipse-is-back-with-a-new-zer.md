---
title: 'Microsoft''s nemesis returns: Nightmare Eclipse is back with a new zero day
  which could be bad news for Windows users'
source_url: https://www.techradar.com/pro/security/microsofts-nemesis-returns-nightmare-eclipse-is-back-with-a-new-zero-day-which-could-be-bad-news-for-windows-users
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-13T17:08:57Z'
published: '2026-08-13T00:00:00Z'
description: It's the tenth zero-day the disgruntled researcher has disclosed
image: https://cdn.mos.cms.futurecdn.net/iGi8rqmXBTK3ZPbi4ExzfW-2000-80.jpg
---

![Fingertip pressing keyboard key with Windows logo on it](https://cdn.mos.cms.futurecdn.net/iGi8rqmXBTK3ZPbi4ExzfW.jpg) 

- **Nightmare Eclipse discloses ShieldBreak, a new Windows privilege‑escalation zero‑day**
- **Flaw bypasses a recent patch and works on fully updated Windows 11 systems**
- **Researcher’s ongoing exploit spree leaves multiple Windows vulnerabilities still unpatched**

Nightmare Eclipse has struck again! The notorious zero-day researcher with a Microsoft grudge disclosed its latest vulnerability, and just as in previous instances, they picked their timing and released their research hours after Microsoft published its August Patch Tuesday cumulative update in order to maximize the hurt.

The newest flaw is called ShieldBreak, and is described as a local escalation of privilege vulnerability that allows threat actors to gain SYSTEM-level privileges on vulnerable systems. Speaking of vulnerable systems, the list is rather long because it includes all versions of Windows 11, including those with the latest security patches.

“The PoC was tested in the latest version of windows 11 25h2 (+Canary channel) and windows server 2025, the PoC also have a 100% success rate,” Nightmare Eclipse said on their GitHub account. “Please note that Windows 10 (and respective server editions) are not currently supported, they are however vulnerable to ShieldBreak as well.”

## A bypass for the RoguePlanet fix

The mysterious attacker also said that the bug was actually a bypass for the patch Microsoft issued to fix their earlier work, called RoguePlanet.

“Microsoft has failed to properly patch the RoguePlanet vulnerability CVE-2026-50656, this PoC demonstrates a full patch bypass,” the GitHub read entry.

Microsoft, on the other hand, responded in pure enterprise fashion, sharing a boilerplate statement that it was “investigating” and that it “supports coordinated vulnerability disclosure”.

In response to an enquiry by *The Register*, a company spokesperson said Microsoft "is aware of the reported vulnerability and is actively investigating the validity and potential applicability of these claims."

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

"Microsoft is committed to investigating security issues and updating impacted products to protect customers as soon as possible,” the statement reads. “Importantly, we support coordinated vulnerability disclosure, an industry standard that protects customers and supports the research community by ensuring their findings are thoroughly investigated and addressed before being made public."

## A hacker on a mission

Together with ShieldBreak, the number of disclosed Windows vulnerabilities and exploits now counts 10. Nightmare Eclipse’s campaign began in April 2026, when they demonstrated BlueHammer, a Windows Defender local privilege-escalation flaw that gives low-privileged users SYSTEM-level access. The researcher claimed BlueHammer, now tracked as CVE-2026-33825, was previously reported to Microsoft, but the company allegedly mishandled the disclosure.

Just before publishing the work, they said “someone violated our agreement and left me homeless with nothing. They knew this will happen and they still stabbed me in the back anyways, this is their decision not mine.”

At first, Microsoft took a tough stance, calling the public release “never justifiable” and even warning that it might pursue legal cases against people who put customers at risk.

The community interpreted this statement as a threat of legal action against Nightmare Eclipse, which triggered a backlash. Microsoft later backed away, saying “to be clear about our approach to legal matters, we have no intention to pursue action against individuals conducting or publishing their security research.”

In the meantime, Nightmare Eclipse (also known as Chaotic Eclipse) went on a full-blown rampage. They released RedSun and UnDefend (both targeting Defender), YellowKey (a BitLocker bypass), GreenPlasma (a CTFMON-based privilege-escalation flaw), MiniPlasma (a regression of a vulnerability Microsoft had originally fixed in 2020), RoguePlanet (another Defender privilege-escalation bug), GreatXML (a BitLocker/Windows Recovery Environment bypass), LegacyHive (a Windows User Profile Service privilege-escalation flaw), and now ShieldBreak.

BlueHammer was fixed in April, RedSun and UnDefend in May, and YellowKey, GreenPlasma, and MiniPlasma, in June. RoguePlanet was patched in July, while LegacyHive, GreatXML, and ShieldBreak, remain unpatched.

It is also worth mentioning that not all of Nightmare Eclipse’s releases were equally complete or reproducible by third parties. For GreenPlasma, independent researchers said it contained the vulnerability but turning it into a reliable working exploit required significant additional technical work. Some of the early Defender exploits were also apparently difficult to reproduce, mostly because they relied on delicate race conditions and very specific sequences of Windows components.

ShieldBreak, however, seems to be more dangerous in that respect. Speaking to *The Register*, security researcher Kevin Beaumont confirmed it as working: “I've tried it, it works on latest Windows 11,” he told the publication.

He also said that while ShieldBreak was described as a bypass for the RoguePlanet fix, the two flaws actually operated quite differently.

“RoguePlanet was a filesystem race condition vuln that uses virtual disks and NT native file manipulation to trick quarantine process into overwriting system files,” Beaumont explained. “ShieldBreak user-mode callback hook to change file contents during a Defender cloud-hydration scan via cfapi (Cloud Filter API).”

No one knows how much ammunition Nightmare Eclipse still has, but we will certainly be paying attention to them in the hours after next month’s Patch Tuesday, as well.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
