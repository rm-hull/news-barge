---
title: Could this be the end of BIOS-locked laptops? AI tweaker deploys Claude to
  unlock and change settings for good
source_url: https://www.techradar.com/pro/could-this-be-the-end-of-bios-locked-laptops-ai-tweaker-deploys-claude-to-unlock-and-change-settings-for-good
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-08T02:14:44Z'
published: '2026-08-07T00:00:00Z'
description: AI helps patch a signature check to always say "yes" on a specific HP
  laptop using a hardware flasher
image: https://cdn.mos.cms.futurecdn.net/g4rSJo2KyoM42vGic5MGrn-1920-80.png
---

![Anthropic Claude 4.5](https://cdn.mos.cms.futurecdn.net/g4rSJo2KyoM42vGic5MGrn.png) 

- **Redditor uses Claude Code to help reverse-engineer the firmware on an HP 15-dw1036ne, patching its signature check and exposing 55 hidden setup fields and four configuration tabs**
- **The laptop's RSA-2048 was not broken: the verification routine was patched to return success, a standard firmware-modding technique as per Community Notes**
- **The result is model- and version-specific, still requires physical access via a hardware flash programmer, and leaves the machine permanently more exposed to firmware implants in the future**

A Reddit user going by Reddit_2049 posted to r/ClaudeAI a claim that traveled fast: Claude Code had picked apart the firmware on their HP 15-dw1036ne and unlocked it, exposing 55 hidden setup fields and four previously invisible configuration tabs.

The move, though impressive, relies on a well-known BIOS modding approach: attacking the BIOS signature check so the BIOS always replies in the affirmative, effectively bypassing it altogether rather than throwing a potential firmware corruption error.

While it does have security implications, it also opens up a route to essentially 'rescue' locked or disabled laptops that would otherwise become e-waste.

## A solution to certain types of e-waste, enabled by AI

What Claude Code did to "unlock" the Redditor's laptop is not a new technique. It bypassed the firmware's integrity check (an RSA-2048 signature verification) by targeting not how the check was performed, but how its result was reported.

The cryptography remains untouched, as Community Notes on two of the larger viral posts about the story pointed out. What the episode does highlight is that on machines without hardware-rooted boot protection, the verification routine itself sits in modifiable firmware, which is the same repair specialists and modders have relied on for years.

Reddit_2049 ran the job through the standard firmware toolchain: Ghidra for disassembly, UEFITool for extracting firmware volumes, and Unicorn Engine to emulate the check outside the real machine. Claude Code assisted here rather than acting autonomously by stitching together the relevant parts for him. The techniques involved are well documented; what was not documented was this particular machine, and that is the gap the model closed.

That opens an interesting front, one that could help with e-waste, even if not every owner is equipped to open a laptop safely or use a hardware flash programmer. An LLM that can read disassembly and hold a firmware layout in its head compresses hours of specialist work, which means targets that were never worth anyone's time individually now might be.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Whether the approach travels is an interesting question, however. The author of the original post warns the script may not work even on superficially similar HP models, and anyone attempting it on different hardware would need a flash programmer on hand and a tolerance for bricking the machine: modified firmware also brings its own problems, including occasional stability issues.

Right-to-repair rules in the EU and several US states have been circling this territory without directly addressing firmware. Until they do, the position stands roughly where it did last week, except that reverse-engineering a specific machine's firmware has become considerably cheaper for everybody.

That could let owners keep using older, locked laptops that would otherwise become e-waste, at a time when consumers are already burdened by higher costs due to inflation and an AI spending spree by data centers affecting laptops and desktops alike.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Rahim Amir](https://cdn.mos.cms.futurecdn.net/9xKZFBamtEZKSChRvywbPB.png)

Rahim Amir is a UAE-based tech writer who enjoys building PCs as much as he enjoys writing about them. He has been professionally writing about PC hardware since 2023, focusing on buyer’s guides, hardware reviews, and sponsored content and features related to tech.

Having built hundreds of gaming PCs and being an avid gamer in his spare time, Rahim tends to have stronger opinions about hardware than most. This is particularly on display when he gets his way with powerful, but minimalistic RGB builds even as Small Form Factor (SFF) PCs come a close second.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
