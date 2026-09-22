---
title: Apple weighs its first server since the Xserve, and as always, Nvidia may hold
  the key
source_url: https://www.techradar.com/pro/apple-weighs-its-first-server-since-the-xserve-and-as-always-nvidia-may-hold-the-key
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-22T22:55:21Z'
published: '2026-09-22T00:00:00Z'
description: Apple is reportedly exploring an M8 Ultra AI server for 2029
categories:
- Technology & Software
- Business & Entrepreneurship
image: https://cdn.mos.cms.futurecdn.net/D9pZcgdPinp5ty7pPDjKeY-1920-80.png
---

![Nvidia](https://cdn.mos.cms.futurecdn.net/D9pZcgdPinp5ty7pPDjKeY.png)

* **Reports claim Apple is weighing an as-yet-unapproved enterprise AI server with two or four M8 Ultra chips, targeting 2029**
* **Apple is considering using Nvidia's NVLink Fusion to link the chips, with Thunderbolt-based Mac clustering falling short of data center bandwidth requirements**
* **The move comes as demand continues to be a key driver for Apple's higher-end Macs, with AI firms buying Mac minis and Mac Studios in bulk, even as Apple has turned enterprise buyers away**

Apple has been working on plans for an enterprise AI server built on its own silicon with an interesting twist: it is seeking Nvidia's help on the networking front to make it work.

A report by *The Information* claims Apple is considering two configurations: one with two of its future M8 Ultra chips and a larger one with four, aimed at businesses that want to run AI inference on their own hardware rather than in a public cloud.

The timeline, however, is long and loose, with a potential launch in 2029, though the same report cautions that the project could be canceled before then, with neither the server nor any Nvidia arrangement finalized at the time of writing.

## A market that Apple previously walked away from

If it ships, the machine would be Apple's first purpose-built server since the Xserve, which Apple announced it would discontinue in November 2010 and stopped selling at the end of January 2011.

Steve Jobs's explanation, in an email to a reader of French site MacGeneration, reported by *MacRumors* at the time, was blunt: "Hardly anyone was buying them." Gartner's data backed up that claim with an estimated 10,000 units being sold per quarter, a relatively low number for the tech giant whose numbers normally ran in the hundreds of thousands or millions for most of its other products.

Apple's suggested replacements to users were server configurations of the Mac mini and Mac Pro, desktops running server software rather than rack hardware. If the 2029 launch materializes, it would mean Apple's reversal would see it enter the server market 18 years after the Xserve stopped being sold.

This time, however, feels different: The Information has reported that OpenAI bought tens of thousands of Mac minis and Mac Studios to train AI agents through reinforcement learning, and that Anthropic has rented Mac minis through Amazon Web Services, as per Ars Technica.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## Getting caught off guard by AI-centric demand

Apple reportedly was caught off guard by the AI-driven rush for its hardware, with no enterprise AI strategy, no business engineering team in place, and no specific developer relations staff to manage those orders. As a result, it also turned away businesses asking to buy access to its Private Cloud Compute infrastructure.

The project reportedly had a powerful sponsor: Apple's now-CEO John Ternus, when he ran Apple's hardware engineering team. However, shortages plagued it, leading many users to opt for Nvidia's DGX Spark and AMD's Ryzen AI Halo as viable alternatives.

The focus, however, remains on Apple's ability to interconnect a large number of chips or dies together: its current flagship, the M5 Ultra that ships in the new Mac Studio on September 22 2026, is Apple's first quad-die design, stitched together inside one package by the company's UltraFusion bridge, with up to 512GB of unified memory and 1.2TB/s of bandwidth, which users often stack for on-device AI needs.

A data center-esque, server-grade offering, however, would require considerably more power under the hood to meet its AI needs, which would also depend on how fast the interconnect between chips is; Apple's current limitation is Thunderbolt 5 speeds, which offer up to 10GB/s (or 80Gb/s) bidirectionally.

For context, Nvidia says the sixth-generation NVLink, available through NVLink Fusion, connects up to 72 accelerators at 3.6TB/s each. Comparing total two-way bandwidth, that is roughly 240 times a single Thunderbolt 5 connection's one-way capability of up to 15GB/s (or 120Gb/s).

Apple's own marketing hints at what that gap costs: It says four clustered Mac Studios deliver up to three times the inference performance of one, suggesting it already makes scaling tradeoffs of nearly 25% when linking devices.

This could explain why Nvidia is in the conversation at all: proven tech that could help Apple scale its AI server ambitions without the performance overhead it currently already has, at a time when its silicon would be even more powerful, might just be a no-brainer for the Cupertino-based giant.

![Google logo on a black background next to text reading &#039;Click to follow TechRadar&#039;](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg)

***Follow TechRadar on Google News***and** add us as a preferred source** * to get our expert news, reviews, and opinion in your feeds.*

![Rahim Amir](https://cdn.mos.cms.futurecdn.net/9xKZFBamtEZKSChRvywbPB.png)

Rahim Amir is a UAE-based tech writer who enjoys building PCs as much as he enjoys writing about them. He has been professionally writing about PC hardware since 2023, focusing on buyer’s guides, hardware reviews, and sponsored content and features related to tech.

Having built hundreds of gaming PCs and being an avid gamer in his spare time, Rahim tends to have stronger opinions about hardware than most. This is particularly on display when he gets his way with powerful, but minimalistic RGB builds even as Small Form Factor (SFF) PCs come a close second.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
