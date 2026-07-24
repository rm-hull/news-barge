---
title: Nvidia's latest trick for cooling its data center hardware is... hot water?
  'Hot liquid cooling' is warmer than a hot tub, but apparently does the job pretty
  well
source_url: https://www.techradar.com/pro/nvidias-latest-trick-for-cooling-its-data-center-hardware-is-hot-water-hot-liquid-cooling-is-warmer-than-a-hot-tub-but-apparently-does-the-job-pretty-well
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-24T03:36:32Z'
published: '2026-07-23T00:00:00Z'
description: A fine-tuned cooling mechanism
image: https://cdn.mos.cms.futurecdn.net/P8gY25WHfpAuxs8W7zQkGL-1200-80.jpg
---

![AI infrastructure by Nvidia](https://cdn.mos.cms.futurecdn.net/P8gY25WHfpAuxs8W7zQkGL.jpg) 

- **Nvidia's Rubin-generation AI servers run coolant that is often hotter than a hot tub as it enters a closed loop at up to 45°C and leaves at around 55°C, with no performance penalty in tow**
- **The principle leveraged here is that of a temperature gradient with server chips still running hotter than the coolant, allowing heat transfer to occur seamlessly**
- **The approach allows Nvidia to roughly conserve 2.6 million gallons per megawatt annually to near zero and could save a 50MW site over $4 million a year in cost**

Nvidia's Rubin generation is the first of its kind in multiple ways, but the one that sticks out possibly is the fact that it is 100% liquid cooled, implementing it as a core design feature at a platform level with every single chip and networking component covered by a closed loop.

The reference design by Nvidia aims to allow for AI factories that effectively consume zero water by implementing a closed loop circuit that does not leverage evaporative water cooling 99% of the time.

The approach goes a step further by potentially eliminating industrial chiller plants from the equation by using liquid cooling where the temperature is as much as 45 degrees Celsius for coolant entering the system and approximately 55 degrees Celsius while exiting it.

## A numbers game for a data center that crunches them at an industrial level

Nvidia's approach is not the first of its kind in terms of thermal design or implementation; however, IBM beat it by 16 years, using 60-degree coolant to cool its prototype supercomputer at ETH Zurich.

The premise was the same: a much lower carbon footprint, significantly lower power consumption, and a loop that is filled once and left alone. What Nvidia adds is scale — its Vera Rubin-based DSX design extends the approach across an entire facility rather than a single machine.

"The NVIDIA DSX reference design for AI factories has zero water consumption — we have eliminated massive amounts of power usage and pretty much all water usage," said Ali Heydari, Nvidia's director of data center cooling and infrastructure.

The coolant is a 3:1 water-to-propylene-glycol mix, and it pulls heat away from chips running far hotter than the coolant itself with ease.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The savings are not only water-based: industrial chiller plants cut their energy costs by roughly 4% for every degree they raise their operating temperature, and Nvidia estimates that a 50-megawatt hyperscale facility could save over $4 million annually in cooling-related energy and water costs by adopting its design.

With cooling historically accounting for as much as 40% of a data center's total power bill, Nvidia's approach is ambitious, but it is one that should pay for itself quickly — eliminating server fans altogether while allowing chillers to run only where necessary, and at considerably lower power than a loop demanding colder coolant.

It must be noted that DSX is a reference design: a set of best practices for building an AI factory, not a census of what the industry has actually built, where many designs still consume very large amounts of water even as AI data centers continue to pop up in drought-affected regions of the US.

Nvidia might seem to be championing a "greener" AI data center for the future, at least in its own designs, but that is only part of the story — and the part it leaves out is a little less flattering. Nvidia did not adopt hot-water cooling because it is elegant, or green, or clever, though it is all three. It adopted it because its accelerators became so power-dense that moving air across them was no longer physically viable, and once you are committed to liquid cooling, running it hot is simply the efficient way to do it.

The sustainability win is real, and it is a consequence of a thermal problem Nvidia created for itself by building the most power-dense chips in the industry. Hot water isn't the trick. It's the bill coming due, paid in the most efficient currency available.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Rahim Amir](https://cdn.mos.cms.futurecdn.net/9xKZFBamtEZKSChRvywbPB.png)

Rahim Amir is a UAE-based tech writer who enjoys building PCs as much as he enjoys writing about them. He has been professionally writing about PC hardware since 2023, focusing on buyer’s guides, hardware reviews, and sponsored content and features related to tech.

Having built hundreds of gaming PCs and being an avid gamer in his spare time, Rahim tends to have stronger opinions about hardware than most. This is particularly on display when he gets his way with powerful, but minimalistic RGB builds even as Small Form Factor (SFF) PCs come a close second.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
