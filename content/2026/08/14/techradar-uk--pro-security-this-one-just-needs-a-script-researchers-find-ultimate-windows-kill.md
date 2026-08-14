---
title: '''This one just needs a script'': Researchers find ultimate Windows kill switch
  which can disable antivirus with almost no user interaction'
source_url: https://www.techradar.com/pro/security/this-one-just-needs-a-script-researchers-find-ultimate-windows-kill-switch-which-can-disable-antivirus-with-almost-no-user-interaction
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-14T17:04:47Z'
published: '2026-08-14T00:00:00Z'
description: Microsoft fixes issue, so update now or be at risk
image: https://cdn.mos.cms.futurecdn.net/iGi8rqmXBTK3ZPbi4ExzfW-2000-80.jpg
---

![Fingertip pressing keyboard key with Windows logo on it](https://cdn.mos.cms.futurecdn.net/iGi8rqmXBTK3ZPbi4ExzfW.jpg) 

- **Researchers uncovered “Download more RAM” flaw in consumer DDR4/DDR5 memory**
- **Attack bypassed Windows VBS and HVCI, disabling antivirus and protections**
- **Microsoft patched CVE‑2026‑23670; tools now help enable memory write protection**

Microsoft has recently fixed a vulnerability that allowed threat actors to bypass advanced security measures, disable antivirus software, and expose the target device to full system takeover.

All of this, it seems, could have been possible with a very simple script, and a single click from the victim’s side.

Luckily, the vulnerability was discovered by white hat hackers, reported to Microsoft and remedied before falling into the wrong hands.

## Download more RAM

During the 2026 USENIX Security Symposium, security researchers from the University of Birmingham and Durham University presented a discovery they called “Download more RAM”.

According to the researchers, some consumer memory chips (DDR4 and DDR5 DIMM) allowed software to alter the configuration reports it sends to the motherboard. In practice, it means that a threat actor could instruct the RAM chip to tell the computer it was bigger than it actually was, making the device “think” it has twice as much RAM memory as it actually has.

The researchers then established that this phantom extra memory can serve as an alias for real memory locations, granting them the ability to both read, and modify, memory allocations that should be under the processor’s, and Windows’ protection.

This window let them work around both Virtualization-based Security (VBS) and Hypervisor-Enforced Code Integrity (HVCI).

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

VBS, first introduced with Windows 10, is a security feature that uses hardware virtualization to isolate critical security functions from the OS, while HVCI uses virtualization to make sure only trusted and verified code can run in the Windows kernel.

The researchers also used the flaw to disable both antivirus and endpoint detection and response (EDR) software, re-introduce older, vulnerable drivers, compromise corporate systems under lockdown, and bypass kernel-level game anti-cheat protections.

The worst part is that this entire process can be chained together into a one-click script. In theory, if a victim is served this script as a file and they run it, they would trigger a chain of events that includes creating memory aliases, rebooting the computer, and disabling security protections.

"Our work exploits the fact that all processes share the same memory to bypass Windows' strongest security guarantees,” said Professor Tom Chothia, from the University of Birmingham. “Previous attacks of this kind needed a screwdriver and physical access to the machine. This one just needs a script. That changes who can carry it out and how far it can spread."

## Who is vulnerable and how to stay safe

The attack surface is rather large, as well. The researchers analyzed the market and found three major manufacturers (Corsair, G.Skill, and ADATA) shipping at least one consumer memory product line in which the configuration chip was left entirely unprotected. Together, these vendors make up more than half (55%) of the high-performance consumer memory market and more than 70% of the gaming market (this doesn’t mean that 55% of the high-performance market is vulnerable - many devices are running other modules, too).

Modules from Crucial, Kingston and HyperX, and some G.Skill lines, were found to use partial write protection, but still enough to keep the device secure.

Before publishing their work, the researchers disclosed their findings to Microsoft, who quickly addressed it. The bug is now tracked as CVE-2026-23670, and is described on the National Vulnerability Database (NVD) as an “untrusted pointer dereference in Windows Virtualization-Based Security (VBS) Enclave” which “allows an authorized attacker to bypass a security feature locally.”

The bug was given a severity score of 5.7/10 (medium), and was fixed as part of the April 2026 Patch Tuesday cumulative update. Therefore, systems with Secure Boot running should be protected against this vulnerability.

Corsair added a feature to its iCue tools that lets users retroactively enable write protection on their memory modules. There is also a free tool called HWinfo with the same functionality, the researchers said, stressing that it mitigates the issue on non-Corsair models. Also, some motherboards offer a BIOS setting to block writes to memory configuration chips, which users can enable as an interim measure.

“The ‘Download More RAM’ attack demonstrates once more the importance of understanding systems, especially in terms of security guarantees. If a lower layer can become compromised, it puts the full system at risk,” said Dr Marius Muench, from the University of Birmingham.

“Windows makes a strong promise: that even an attacker with administrator rights can't touch the secure kernel. We found that promise rests on the assumption that your memory is telling the truth about itself - on a lot of the memory people actually buy, it doesn't have to."

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
