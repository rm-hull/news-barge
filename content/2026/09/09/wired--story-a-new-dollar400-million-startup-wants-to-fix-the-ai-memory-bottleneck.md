---
title: A Stealth Startup Thinks It Just Hacked the Memory Shortage
source_url: https://www.wired.com/story/a-new-dollar400-million-startup-wants-to-fix-the-ai-memory-bottleneck/
source_site: Wired
source_slug: wired
scraped_at: '2026-09-09T19:15:37Z'
published: '2026-09-09T00:00:00Z'
description: Kepler Computing claims a new approach to chip design—and a proprietary
  material—can help end the supply bottlenecks that have sent memory prices surging.
image: https://media.wired.com/photos/6a99ec2e5d2ca173f400bbc3/191:100/w_1280,c_limit/00-kepler-wafer_memory_technology.jpg
---

An ambitious chip startup that has spent more than seven years quietly trying to redesign the architecture for computer memory has just come out of stealth mode and believes its new approach can help ease the global memory-chip shortage—provided it can produce its technology at scale.

Kepler Computing, a San Jose, California–based startup founded in 2018 by a team of physicists and computer scientists, says it has developed a new architecture for high-bandwidth memory (HBM) that directly addresses some of the chip supply bottlenecks that are constraining the computing market.

While chipmakers typically rely on expensive extreme ultraviolet lithography (EUV) to shrink the transistors on a chip, thereby packing more technology into the same amount of space, Kepler claims that its “3D stacking” approach and a proprietary new material allow it to increase density without relying on EUV at all—and it can work with existing semiconductor fabrication plants.

Kepler says it has made similar gains for the high-speed cache memory typically used in CPUs, GPUs, and XPUs. This so-called SRAM sits within the core of a chip die in order to cut down on data transfer times. HBM, by contrast, uses stacks of DRAM, which is a separate memory component of chips.

The company has raised $468 million in funding over the past few years from big-name backers. This includes GlobalFoundries, Intel Capital, AMD Ventures, the British investment fund Baillie Gifford, and Bill Gates, through his private Gates Frontier fund. In July, the US Department of Commerce committed to give Kepler up to $245 million to “develop in the US a new class of high-performance AI memory technology, enabled by innovative 3D and ferroelectric technologies.”

For now, much of Kepler’s testing is happening in Singapore, which is where GlobalFoundries—a manufacturing partner and investor of $50 million—has a facility. Over the past two years Kepler has been building out what it refers to as “mini fabs,” where it produces its memory chips in conjunction with Global Foundries’ 28-nanometer chips. (It has also been running tests in GlobalFoundries’ facilities in Burlington, Vermont.)

Kepler and its investors say the startup’s new approach to building memory chips couldn’t come at a better time. The global memory chip shortage has reaffirmed at least two realities about the market: Building new fabs is hugely expensive and painstaking, and the demands around certain kinds of memory tend to be cyclical. In a data-center-driven, AI-crazed world, HBM has become the memory du jour.

Some of the world’s leading memory makers, including SK Hynix and Micron, have been racing to build multibillion-dollar fabs in order to meet demand, wagering that even by the time those facilities are operational, the industry will still be looking for high-bandwidth memory.

“For a long time our thinking was that we’d work on SRAM first and then follow up with DRAM and HBM,” says Debo Olaosebikan, a Kepler Computing cofounder and its chief executive officer. “But with the launch of ChatGPT [in 2022] and the explosion of demand for an HBM alternative, we started working on our HBM road map. Now we’re making SRAM and HBM in parallel.”

“We didn’t go in thinking that this would be a replacement for DRAM or a replacement for SRAM,” says Srini Ananth, managing director at Intel Capital. “We figured the market would dictate that, and now you’re seeing a demand for both.”

In bypassing ultraviolet lithography, Kepler is one of a few tech startups working to avoid one of the major bottlenecks in semiconductor manufacturing. The startup claims it can produce SRAM that achieves the same density as 2-nanometer or 3-nanometer chips without having to invest in EUV.

“Kepler’s approach is at the sweet spot of our strategy,” says Ed Kaste, senior vice president of GlobalFoundries’ CMOS business. “It’s a new materials system, with multigenerational scaling potential, without having to build entirely new systems in the fab or invest in very expensive lithography equipment.”

## Material Impact

Kepler’s overarching pitch is that the accelerated computing market shouldn’t have to wait for brand-new memory fabs to be built in order to meet demand. Instead, new approaches to building memory within existing fabs can increase supply.

Their approach is twofold. In terms of improving HBM, Kepler says it has developed a novel 3D-manufacturing technique that fits more memory chips within a fixed footprint. The core compute can then sit closer to the memory, so the data travel between the two uses less energy. Their ultimate goal is to move data around in HBM with the amount of energy that’s comparable to SRAM, all while keeping HBM’s large capacity.

Kepler also says it has improved the density of SRAM using ferroelectrics, which can read and write data at lower voltages than the mechanisms typically used to process and store data in semiconductors. The startup did this by developing a new, low-voltage, composite material that works with this ferroelectric approach.

Sasi Manipatruni, a Kepler cofounder and its chief technology officer, says the Kepler team went through 35 iterations of composites before they landed on a material class that they thought would make memory chips easier and cheaper to make.

“Once we found a way to solve the physics problem—as in the physical limitations for HBM—we came up with a material innovation that helps with the amount of memory you can have between chips,” he says.

In its early build-outs with GlobalFoundries, Kepler says it was able to convert a fab into a “next-generation” fab in just eight months, compared to a typical 24-month timeframe.

“Out goal is to take the fabs and architectures already built, and push them to the limits of physics,” Olaosebikan says.

Basically Kepler is betting that any additional costs that come from new materials or retooling existing fabs would far outweigh the $20 billion to $40 billion it costs to build new ones and outfit them with equipment worth hundreds of millions of dollars.

## Waiting to Scale

Kepler Computing still has a long road ahead before it reaches full-scale production—assuming it gets there. To date, the company has run its technology on around 2,000 wafers. The startup says it’s planning to ship its first samples of HBM chips later this year, ramp up production out of Singapore next year, and start chip production in the US in 2028.

Kaste, the GlobalFoundries executive, says he’s confident that the “fundamental breakthroughs have happened. What remains is getting good results on thousands of wafers and millions of devices.”

He points out that one of the challenges with a material system like the one Kepler is using is that it includes iron in its composite. “Iron is a tough contaminant to introduce into a production facility. So Kepler’s solution has to run on dedicated equipment, or be fully encapsulated so that it can’t escape,” he says.

“The art is in keeping that material really well isolated through our production flow,” Kaste says.

Olaosebikan wouldn’t confirm the specific elements of the company’s composite material. “What I can say is, we’re using a small number of materials, and some of them aren’t what you’d typically find in mainstream ferroelectrics,” he says.

Kepler Computing isn’t the only startup looking to upend the semiconductor industry. Late last year, a well-funded startup called Substrate also made waves for its new approach to lithography, which uses nanoparticles to etch details onto advanced chips. Some industry analysts were skeptical of the startup’s ambitions, noting that it would be extremely difficult for Substrate to produce a large number of chips “that meet incredibly stringent specifications, on time and on budget,” as reported in Bloomberg.

Scale is a common challenge when attempting to innovate semiconductor manufacturing, whether with new processes, materials, or some combination of both. “The question is how to overcome all the limitations of contamination, different materials, and different tooling, in such a way that the resulting innovation can be used at scale and is worth the cost,” says Austin Lyons, a chip analyst for Creative Strategies, who was not briefed on Kepler’s innovation.

Proving out a new method for memory is one thing; meeting the historic demand for it will be another altogether.
