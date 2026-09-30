---
title: Geekbench 7 results suggest OpenAI’s dots agent runs on nine-core AMD EPYC
  VMs with nearly 10GB of memory — newest runs score about six times Meta Muse in
  multi-core
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/geekbench-7-results-suggest-openais-dots-agent-runs-on-nine-core-amd-epyc-vms-with-nearly-10gb-of-memory-newest-runs-score-about-six-times-meta-muse-in-multi-core
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-30T22:18:28Z'
published: '2026-09-30T00:00:00Z'
description: The 9,435 multi-core score posted on X was uploaded four days before
  the launch.
image: https://cdn.mos.cms.futurecdn.net/KTQc5i5yh9CnQxg4TVgKMF-2560-80.png
categories:
- Technology & Software
- Hardware
people:
- Maddie D. Reese
- Tibo
locations:
- DevDay
- Geekbench
organisations:
- 3D Slicer
- AMD EPYC Turin
- Astra
- Blender
- CPU
- Chromium
- Cursor
- FreeCAD
- GIMP
- Geekbench
- Get Tom's Hardware
- Godot
- Google News
- Grok Bot
- INIYSA
- Inkscape
- Kdenlive
- KiCad
- Meta
- Meta’s Muse
- OpenAI
- OpenSCAD
- ParaView
- QGIS
- Shane Downing
- SpaceXAI
- Tom’s Hardware
- Ubuntu
- VM
---

![OpenAI&#039;s dots wordmark in glowing multicolor letters above four plush dot characters, on a black background](https://cdn.mos.cms.futurecdn.net/KTQc5i5yh9CnQxg4TVgKMF-1920-80.png)

A pre-launch Geekbench 7 result, shared on X by INIYSA as one of OpenAI’s dots (it's answer to Meta's Muse), shows a multi-core score of 9,435, with indications of the hardware used by the new autonomous agent. The VM hardware appears to be a single nine-core slice of an AMD EPYC 9V74 with 9.73GB of memory, run on Ubuntu for the leak and Debian for post-launch runs. Our check of Geekbench 7’s public database found six runs on that configuration uploaded since launch, ranging from 1,512 to 1,614 single-core and 8,135 to 8,991 multi-core. Dots, powered by GPT-6 Astra, launched at OpenAI’s DevDay on Tuesday for Pro and Business Premium users.

OpenAI bills the autonomous agents as having “their own cloud computer, their own browser, and the apps you’ve connected” in its introduction. This is not a new concept: Cursor says its cloud agents get their own virtual machines; SpaceXAI says every Grok Bot shares one persistent cloud computer; and Meta’s Muse gives each agent a sandbox.   
Maddie D. Reese posted on X on launch day the apps her dot said came preloaded. The lineup includes Chromium, Blender, GIMP, Inkscape, Kdenlive, Godot, FreeCAD, OpenSCAD, KiCad, QGIS, ParaView, 3D Slicer, with Python, Node.js, and Git. In the same reply, the dot said its cloud computer runs “Debian Linux.”

> Fun note from Tibo at the closing q&a of DevDay:dots get their own Linux cloud computer, and that cloud computer comes preloaded with apps like Blender!I checked with my dot to get a fuller list of the preloaded apps and tools pic.twitter.com/JIt5VQiV2jSeptember 29, 2026

The post went up the evening of launch day, captioned “OpenAI dots Geekbench 7 Score,” with a screenshot showing a single-core score of 1,667 and multi-core of 9,435. The result in the screenshot shows that it was uploaded Sept. 25, or four days before the launch. The 9,435 is almost 5% higher than the post-launch best and about 10% higher than the median. The pre-launch run is potentially a bit of an outlier, but performance remains within the same ballpark. It is uncertain who ran the original benchmark.

Tom’s Hardware previously reported that rival Meta’s Muse runs on AMD EPYC Turin with two cores and 8GB per sandbox. The 10 Muse runs in Geekbench’s database have median scores of about 1,041 single-core and 1,394 multi-core. The dot’s post-launch runs, with median scores of 1,570 and about 8,550, put it at about 1.5x the single-core and 6x the multi-core score.

Some of this gap is accounted for by the nine-core vs. two-core configuration; the rest of the gap likely comes from a difference in clock speed, partially offset by Muse’s newer architecture. Geekbench lists a 2.6GHz base clock for the dot’s EPYC 9V74 against 1.5GHz for Muse’s EPYC 9D25.

Muse’s runs also report 7.75GB of memory. Our independent run for this article came back with a single-core score of 1,000 and a multi-core score of 1,433, in line with the other Muse runs.

Data center CPU demand for always-on agents has surged as high-core-count CPUs are needed at sustained load. It is unknown whether the dots, as tested, hold their cores while idle. Such agents are rising in popularity: Muse reportedly passed 500,000 daily active users, and SpaceXAI plans standalone Nvidia Vera CPUs for Grok’s agentic workloads. It may only be a matter of time before a new CPU arms race begins. OpenAI has already said that, in the future, users will be able to add more dots and “scale the output of each dot by ... increasing its speed.”

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.



*Follow* * Tom’s Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Shane Downing](https://cdn.mos.cms.futurecdn.net/Zosi9VrDytS9FkgJiHvc69-140-80.png)

Shane Downing is a Contributing Writer for Tom’s Hardware, covering consumer storage, PC hardware, and AI.
