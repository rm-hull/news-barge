---
title: Epic introduces an improved version of anti-cheat for Linux — strict TPM 2.0
  and Secure Boot rules spark open-source pushback, but finally allow Linux gamers
  to play Fortnite
source_url: https://www.tomshardware.com/video-games/pc-gaming/epic-introduces-an-improved-version-of-anti-cheat-for-linux-eac-linux-v2-will-finally-allow-linux-gamers-to-play-fortnite
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-16T16:39:53Z'
published: '2026-10-16T00:00:00Z'
description: Are all these requirements worth it just to play a few competitive titles?
image: https://cdn.mos.cms.futurecdn.net/TuUrJ7mPPTzDMN7HfGCwiA-1920-80.jpg
categories:
- Technology & Software
- Hardware
- Video Gaming
people:
- Jowi Morales
- Tom
- Witcher
locations: []
organisations:
- EAC Linux V2
- GOG
- Google News
- IOMMU
- Input-Output Memory Management Unit
- Jowi Morales
- Kernel Lockdown Integrity Mode
- Kernel Modules
- Kexec Disabled
- Linux Mint
- No. Anti-get-paid-stuff-for-free
- Proton
- Secure Boot
- Signed Kernel
- Ubuntu
- Wine
---

![Fortnite Splash Squadron Set](https://cdn.mos.cms.futurecdn.net/TuUrJ7mPPTzDMN7HfGCwiA-1920-80.jpg)

Epic Games says that it’s working on an update for its anti-cheat solution for Linux that would close the gap in capabilities with the Windows version of Easy Anti-Cheat. The company said that EAC Linux V2 will use existing Linux features to make it easier for distribution maintainers to meet these requirements by default, which should allow more Linux gamers to play competitive titles without needing to make changes to their current setup, but with the trade-off of forced adherence to certain security measures that the Linux community often avoids.

EAC Linux V2 currently has the following requirements: Signed Kernel and Kernel Modules, TPM 2.0, Secure Boot, Measured Boot, Input-Output Memory Management Unit (IOMMU), Kernel Lockdown Integrity Mode, Kexec Disabled, and Linux Security Module BPF. The company says that it expects to iterate on these requirements over time, and that it’s looking to work with developers and distribution maintainers to refine these requirements. Using these features means that EAC Linux V2 will not need a kernel driver like the Windows implementation of anti-cheat, although it may require some distro maintainers to effect a configuration change to work with EAC Linux V2.

As for Linux players using an EAC-Linux-V2-compatible game and distro, they need to install an anti-cheat systemd service that only runs alongside a protected game. Once they quit the protected title, the anti-cheat service would also end its process. Some of the distros the EAC Linux V2 recognizes signing keys from include Ubuntu, Linux Mint, Fedora, Bazzite, and Debian, among others, meaning gamers already using these would be able to play protected games provided that their machine also meets all other requirements.

Even though Epic is trying to reach as many Linux gamers as possible, these features will likely not be well received by the community. Some Linux users don’t trust big tech, and it is often one of the reasons why they switched over to the open-source platform in the first place. Enforcing these requirements just to play a single game would go against the ethos of having full control of one’s hardware and software, which is one challenge the anti-cheat systems working on Linux must deal with. Epic does offer some compromises, like allowing multiple boot options so that Linux gamers can still maintain their preferred configuration when they do not intend to play a protected title. But the fact that something with this many stringent requirements is installed on their system may not sit well with many users.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Jowi Morales](https://cdn.mos.cms.futurecdn.net/gM7E2WSDg2wgCFoaDPz9yK-140-80.jpg)

Jowi Morales is a tech enthusiast with years of experience working in the industry. He’s been writing with several tech publications since 2021, where he’s been interested in tech hardware and consumer electronics.

* What do Witcher and Cyberpunk games have in common, except obviously being made by the same studio?  
  Both are in top 20 of best-selling games of all time and both \*completely\* lack any DRM from the day 1 (at least if purchased on GOG web-site). And they play well on Linux with Wine and Proton.  
    
  Is there a piracy of such games? Yes, but it did not impede them in any way.  
    
  If publisher treats customers right good things happen. Reply
* Anti-cheat? No. Anti-get-paid-stuff-for-free is more like it. The current crop of anti-cheat solutions is all about protecting that DLC monetization store. I like seeing the Linux compatibility spread, but I don't like what EAC is protecting given the ridiculous greed of the biggest gaming industry participants.Reply
