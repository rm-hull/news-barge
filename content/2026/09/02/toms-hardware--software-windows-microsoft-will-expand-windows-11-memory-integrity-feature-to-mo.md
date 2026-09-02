---
title: Microsoft will expand Windows 11 Memory Integrity feature to more PCs starting
  in October — security feature reduces gaming performance on some systems
source_url: https://www.tomshardware.com/software/windows/microsoft-will-expand-windows-11-memory-integrity-feature-to-more-pcs-starting-in-october-security-feature-reduces-gaming-performance-on-some-systems
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-02T19:22:10Z'
published: '2026-09-02T00:00:00Z'
description: PCs that already have Memory Integrity deliberately disabled will retain
  their existing configuration
image: https://cdn.mos.cms.futurecdn.net/A3bqjPsbEd6W9WtTAebSpJ-1920-80.jpg
---

![Windows 11](https://cdn.mos.cms.futurecdn.net/A3bqjPsbEd6W9WtTAebSpJ.jpg) 

Microsoft will begin automatically enabling its Memory Integrity security feature on a broader range of eligible Windows PCs through quality updates starting in October 2026, extending the kernel-level protection to more existing devices by default. In a September 1 blog post, Microsoft said the rollout will provide stronger protection for more devices against attacks targeting the Windows kernel, while PCs that already have Memory Integrity deliberately disabled will retain their existing configuration.

“Windows quality updates will begin enabling memory integrity protection on eligible devices,” Microsoft said. The updates will also enable Virtualization-based Security (VBS) where required, which provides the isolated environment underlying Memory Integrity. Before making the change, Windows will automatically assess each device using what Microsoft describes as readiness signals covering its hardware capabilities, compatibility, and performance.

The October rollout is basically an expansion of Microsoft’s existing default-enablement policy. Memory Integrity is already switched on by default on clean Windows 11 installations that meet Microsoft’s hardware requirements, as well as on Secured-core PCs. Current requirements include an 8th Gen or newer Intel processor for Windows 11 22H2, an AMD Zen 2 or newer processor, at least 8GB of RAM on x64 systems, an SSD of at least 64GB, compatible drivers, and enabled hardware virtualization. Automatic activation under that policy applies to clean installations and not upgrades of existing devices.

Memory Integrity — also known as Hypervisor-Protected Code Integrity (HVCI) — has existed since the Windows 10 era and was originally released as part of Microsoft’s Device Guard security technology. It uses VBS and the Windows hypervisor to move kernel-mode code-integrity checks into an isolated environment, helping prevent malicious or untrusted code and drivers from executing in the Windows kernel. Windows 10 generally left the protection optional outside configurations such as S mode, while Windows 11 made it more of a default security feature on compatible new installations.

The feature comes with a performance wrinkle familiar to PC gamers, leading many gamers to disable it. Microsoft acknowledged in 2022 that Memory Integrity and Virtual Machine Platform could affect gaming performance on some Windows 11 configurations, and advised gamers prioritizing performance that they could temporarily disable these protections while playing, warning that doing so reduces security. The company’s own gaming guidance subsequently continued to recommend temporarily disabling Memory Integrity and VMP where they interfere with gaming performance.

The security feature’s impact on performance depends on the hardware. Microsoft says Memory Integrity performs better on newer processors with hardware features designed to accelerate the required isolation, while older CPUs relying on software emulation can experience a larger performance hit. Driver compatibility can also prevent activation, with Microsoft documenting issues ranging from malfunctioning software to incompatible gaming anti-cheat solutions.

For most users, the October change requires no action. Eligible PCs will be evaluated and updated automatically, while administrator policies and previous user choices remain in place. Microsoft specifically says systems where Memory Integrity has already been disabled “won’t be automatically changed by this rollout,” leaving gamers and other users who previously opted out in control of the setting.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Etiido Uko](https://cdn.mos.cms.futurecdn.net/BBrMt7jWtSo2Dc3iKoroyD.jpg) 

Etiido Uko is a news contributor for Tom's Hardware covering the latest updates in big tech and the PC industry. He is a mechanical engineer and senior technical writer with over nine years of experience in documentation and reporting. He is deeply passionate about all things engineering and technology, and is an expert in gadgets, manufacturing, robotics, automotive, and aerospace.

- 
Reduce gaming performance eh? *This is me looking at SteamOS* Reply
 
 In other thoughts, I hope further integrity pushes lead to Microsoft kicking kernel level anti-cheat solutions to the curb.
 
 Less is more when it comes to true security of people's personal PII data.
 
 Admin said:PCs that already have Memory Integrity deliberately disabled will retain their existing configuration
 For now. But that statement has an expiration date. Microsoft has long since weaponized Windows Update in order to force people into Edge, Bing, start men advertisements, AI/Copilot junk nobody wants, and other settings people are setting but then later discovering, it was reverted back. Windows Update has become one of the most despised systems within the OS because of all this.
 
Microsoft is a bully. Bullies are gonna bully. That's just what they do that's just what Microsoft is. A shark is a shark, a mosquito is a mosquito. They do the things you predict they are going to do. It is in their nature.
- 
Reply
 The “I don’t like kernel level anticheat” crowd are funny. Especially when they’re running 10 RGB softwares which all have ring 0 accessezst036 said:Reduce gaming performance eh? *This is me looking at SteamOS*
 
 In other thoughts, I hope further integrity pushes lead to Microsoft kicking kernel level anti-cheat solutions to the curb.
 
 Less is more when it comes to true security of people's personal PII data.
 
 
 
 For now. But that statement has an expiration date. Microsoft has long since weaponized Windows Update in order to force people into Edge, Bing, start men advertisements, AI/Copilot junk nobody wants, and other settings people are setting but then later discovering, it was reverted back. Windows Update has become one of the most despised systems within the OS because of all this.
 
Microsoft is a bully. Bullies are gonna bully. That's just what they do that's just what Microsoft is. A shark is a shark, a mosquito is a mosquito. They do the things you predict they are going to do. It is in their nature.
