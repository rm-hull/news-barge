---
title: Overlocker uses vibecoded BIOS modification to target Intel's non-K overclocking
  restrictions — attempts to revive ASRock's discontinued SkyOC technology
source_url: https://www.tomshardware.com/uk/pc-components/cpus/overlocker-uses-vibecoded-bios-modification-to-target-intels-non-k-overclocking-restrictions-attempts-to-revive-asrocks-discontinued-skyoc-technology
source_site: Tom's Hardware
source_slug: toms-hardware
description: ASRock discontinued SkyOC following Intel's efforts to block non-K CPU
  overclocking, but an enthusiast is now using AI to see if the old workaround can
  be adapted for newer platforms.
image: https://cdn.mos.cms.futurecdn.net/upv5CLs6eZgME2q4v4v9MX-1920-80.jpg
published: '2026-11-16T00:00:00Z'
scraped_at: '2026-11-17T03:47:23Z'
categories:
- Technology & Software
- Hardware
people:
- Fomdoo
- Kunal Khullar
- Tom
locations:
- AI
- SkyOC
organisations:
- AI
- ASRock
- Admin
- BCLK
- CPU
- Chat-GPT Astra
- Google News
- Intel
- SkyOC
- Skylake
- Tom’s Hardware
---

![ASRock Z170 motherboards](https://cdn.mos.cms.futurecdn.net/upv5CLs6eZgME2q4v4v9MX-1920-80.jpg)

In an attempt to resurrect ASRock's discontinued SkyOC overclocking feature, an enthusiast has vibe-coded a motherboard BIOS using AI, potentially bringing non-K CPU overclocking to modern Intel CPUs. According to a post on X, Hardware 360º used Chat-GPT Astra to decompile and compare two versions of an ASRock BIOS, one released with SkyOC and another with the feature disabled. The AI reportedly identified the code responsible for enabling the overclocking workaround and modified it to create a BIOS ready for implementation on a compatible motherboard. Unfortunately, it remains to be seen whether the modified firmware can restore SkyOC on modern Intel platforms, as the workaround is yet to be fully tested.

For context, Intel offers multiplier-based overclocking only on its unlocked K-series processors like the Core i9-14900K and the newer Core Ultra 270K Plus. Non-K models have locked multipliers, which restrict users from pushing CPU frequencies. However, there’s another way to raise the speed of a processor by pushing the base clock itself. The base clock, or BCLK, typically runs at 100 MHz and works alongside the CPU multiplier to determine its operating frequency. For example, raising the base clock speed of a CPU to 105 MHz increases the clock speed by 5%. The only downside is that BCLK adjustments can also affect the entire motherboard, including memory and PCIe-based components, thereby potentially causing system instability.

ASRock's SkyOC technology, which was introduced for Intel's Skylake processors in 2016, allowed users to overclock locked non-K CPUs through BCLK adjustments. Certain motherboards also featured independent clock generators, allowing CPU clock adjustments without affecting the rest of the system. Intel was not particularly pleased with the workaround, and ASRock eventually had to remove SkyOC from its motherboards via BIOS updates. Additionally, Intel introduced microcode changes to prevent non-K overclocking.

The current experiment revisits that workaround by identifying the original BIOS code and adapting it for modern motherboards. Hardware 360º claims Intel's restrictions include a mechanism that triggers a shutdown when BCLK exceeds 103 MHz, and that SkyOC originally worked around this by tricking the processor with a false report of the actual BCLK value.

Finding the original code for SkyOC does not necessarily mean it can be successfully ported to a modern motherboard BIOS. Newer Intel processors use different firmware, microcode, and clock-management mechanisms, which would make adapting the workaround considerably more complicated. Flashing modified motherboard firmware also comes with its own set of risks, including the possibility of rendering the board completely unusable. Nevertheless, it is interesting to see how AI-assisted reverse engineering can help gain access to BIOS modifications that would otherwise require a considerable amount of effort.



*Download the Tom's Hardware app for up-to-the-minute updates on* * iOS* * and* * Android**. Also follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Kunal Khullar](https://cdn.mos.cms.futurecdn.net/NDK3ae3zDxAx2BJnMXxBJV-140-80.jpg)

Kunal Khullar is a contributing writer at Tom’s Hardware. He is a long time technology journalist and reviewer specializing in PC components and peripherals, and welcomes any and every question around building a PC.

* Fomdoo said:You'd have to have an insane level of trust in AI to install a vibe coded bios firmware.If it were purely vibe-coded, yes. However, the part about de-compiling and then porting over just the bits involved in SkyOC sounds to me like it could work. The person doing it hopefully understands enough to roughly verify the scope of the modifications going into the new BIOS.  
    
  That said, I'm surprised this was reported before it was even verified working. It's only news if it actually works. Reply
* Admin said:ASRock discontinued SkyOC following Intel's efforts to block non-K CPU overclocking, but an enthusiast is now using AI to see if the old workaround can be adapted for newer platforms.  
    
  **Overlocker uses vibecoded BIOS modification to target Intel's non-K overclocking restrictions : Read more** I didn't know Toms Hardware was going into sewing! Nice overlocker home headline! PC hardware mustn't be maintaining the interest like sewing! 🤣🤣🤣
  Reply
