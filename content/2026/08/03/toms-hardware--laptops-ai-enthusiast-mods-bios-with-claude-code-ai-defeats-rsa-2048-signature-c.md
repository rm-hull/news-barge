---
title: AI enthusiast unlocks and mods BIOS with Claude Code — AI defeats RSA-2048
  signature checks and unlocks 55 hidden settings
source_url: https://www.tomshardware.com/laptops/ai-enthusiast-mods-bios-with-claude-code-ai-defeats-rsa-2048-signature-checks-and-unlocks-55-hidden-settings
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-03T15:11:36Z'
published: '2026-08-03T00:00:00Z'
description: A new way to stop locked laptops from becoming eWaste is always welcome.
image: https://cdn.mos.cms.futurecdn.net/Hx78fhhCWi4XR9Yrf9bJcA-1920-80.jpg
---

![HP OmniBook X Flip 14](https://cdn.mos.cms.futurecdn.net/Hx78fhhCWi4XR9Yrf9bJcA.jpg) 

BIOS-locked laptops are sometimes sold at bargain prices due to the operational restrictions this kind of firmware security puts on the device. Can AI tools be used to bypass this security measure? The answer looks like a yes, as Reddit_2049 on the Claude AI subreddit recently shared the process that successfully unlocked their HP 15-dw1036ne.

A new owner of a BIOS-locked laptop will typically not be able to bypass a password or PIN at startup, nor be able to adjust any BIOS settings. It depends on what kind of lock has been implemented. There was a time when removing the CMOS could reset the BIOS and break these chains, but for a long time, laptop makers have had far stronger security.

The particular laptop model with a BIOS lock to bypass by the Redditor was the HP 15-dw1036ne, a 10th-gen Intel processor-packing laptop from the turn of the decade. This looks like a consumer laptop, so we reckon it will have had a power-on password set by the previous owner, which somehow didn’t get communicated to Reddit_2049 through the used/recycled electronics ownership chain. However, it isn’t explicitly stated what kind of BIOS lock faced the Redditor, so it could have been a BIOS admin lock. These locks aren’t as stringent or formidable as those possible with HP’s commercial laptops, which can even tie BIOS locks to the system TPM…

Back to the HP 15-dw1036ne unlock process, and it came with BIOS version F.68. The Redditor had access to a CH341A chip flasher and code disassembly tools, but said the system would throw up a ‘BIOS Corruption Detected’ message if any modification was detected. That’s a check that makes hacking it all the more difficult. This is where Claude Code stepped in.

Looking for previous examples and details of someone successfully unlocking this specific HP laptop’s BIOS was fruitless. So, Reddit_2049 asked Claude Code to pick through their backup BIOS dump and try to unlock it. Long story short, it worked.

 ![BIOS flashing hardware](https://cdn.mos.cms.futurecdn.net/N4vT8JVg5aSruR3s6V23w5.jpg) 


## Three levels of patches

The Redditor shared a few technical details about the three levels of patches that were required to unlock the BIOS. These include: finding the RSA-2048 DXE-FV signature check bypass, and 55 hidden setup fields, as well as revealing advanced BIOS configuration tabs. But most important to know is that Claude Code wrangled these bits and bytes, so Reddit_2049 now has a fully open BIOS on their HP laptop.

A Python script that completes the whole process on this particular HP laptop is shared at the bottom of the Reddit post. This will back up your current BIOS, implement all three patches, and leave your HP 15-dw1036ne unlocked.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Please be warned that this script might not work with your laptop, even if it's an HP, even if it’s a 15-dw1036ne, or even if there are other differences like board revision. However, this example shows that laptops with locked BIOS access/features and no specific known bypass method can now be fully unlocked thanks to AI.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Mark Tyson](https://cdn.mos.cms.futurecdn.net/56vqMYLDaKRHPhHZgbADFR.jpg)

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.
