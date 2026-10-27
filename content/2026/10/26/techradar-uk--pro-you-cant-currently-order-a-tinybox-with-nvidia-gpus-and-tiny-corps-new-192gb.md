---
title: You can't currently order a Tinybox with Nvidia GPUs — and Tiny Corp's new
  192GB six-GPU AMD build just got $3,000 pricier
source_url: https://www.techradar.com/pro/you-cant-currently-order-a-tinybox-with-nvidia-gpus-and-tiny-corps-new-192gb-six-gpu-amd-build-just-got-usd3-000-pricier
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-27T00:24:16Z'
published: '2026-10-26T00:00:00Z'
description: All change, and a new price
image: https://cdn.mos.cms.futurecdn.net/UXUoBz2xYzpVLMMrg7S6Te-1920-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Jeff Fisher
locations:
- Taipei
- US
organisations:
- AMD
- Blackwell
- FAQ
- GPU
- Nvidia
- StinceBuilt
- TechRadar Pro
- The Register
- Tiny Corp
- Tinybox
- Tom's Hardware
- TweakTown
---

![The Tinybox workstation pictured](https://cdn.mos.cms.futurecdn.net/UXUoBz2xYzpVLMMrg7S6Te-1920-80.jpg)

* **Tiny Corp's Tinybox configurator is now AMD-only, after a new commit titled "rip nvidia" removed every Nvidia option and the Tinybox Pro**
* **The six-GPU, 192GB Radeon AI Pro R9700 build rose from $19,000 to $22,000, and a lower-end four-card, 128GB version now starts at $17,000**
* **For those wanting Nvidia only, a $91,000 tinybox green v2 with four RTX Pro 6000 cards is still listed in the company's Shopify storefront, about 40% above the $65,000 it charged in May**

When TechRadar Pro covered Tiny Corp's relaunched Tinybox on October 13 2026, the headline figure was $11,000 for a server-grade workstation pairing a 32-core AMD EPYC processor and DDR4 memory with four Radeon RX 9070 XT graphics cards.

Less than two weeks on, that configuration is still listed at the same price, but what surrounds it has changed considerably.

Tiny Corp's online configurator is now AMD-only, according to the configurator itself and the public commit history of its website; the RTX 5090 options disappeared on October 11, and the $19,000 RTX 6000 was marked out of stock on October 21, while those thinking this was just a temporary setback were greeted by a commit titled "rip nvidia" that deleted every remaining Nvidia option, along with the $32,000 tinybox pro platform.

## AMD GPUs galore?

The AMD side has moved in the opposite direction: Tiny Corp added a six-GPU build based on AMD's Radeon AI Pro R9700, with 192GB of GPU memory, on October 13. It raised each card from $2,000 to $2,500 on October 23 and added a four-card version the next day.

The cheapest six-card build, the "tinybox red flash" preset that the configurator now opens on, has gone from $19,000 to $22,000. The other two presets ship with no GPUs, described as "Bring your own GPUs."

The new Tinybox launched on October 8 with a short GPU list: four RX 9070 XT cards at $1,000 each, or one or two RTX 6000 cards at $19,000 apiece. RTX 5090 options at $8,000 per card were added a day later and were gone by October 11, removed in a commit with the message "rtx5090s aren't made anymore."

Nvidia disputes this, however: at an event in Taipei, Nvidia's Jeff Fisher said that despite a seemingly massive shortage of the chip on multiple US storefronts, "it has not been discontinued."

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Fisher's comments followed a leak claiming Nvidia would divert its GB202 silicon to RTX Pro cards, and a warning from custom PC maker StinceBuilt that "Retail GPU pricing is expected to climb significantly," as we reported on October 12.

Tiny Corp's list included Nvidia's 96GB RTX Pro 6000 Blackwell workstation card, and its price has followed a curve similar to the RTX 5090 on consumer storefronts. It launched at $8,565 in March 2025, reached $13,250 on Nvidia's own marketplace by June, according to Tom's Hardware, and hit $16,000 there in August, per TweakTown.

Nvidia hasn't completely disappeared from Tiny Corp's storefront; The company's Shopify store, still linked from its FAQ, lists a tinybox green v2 with four RTX Pro 6000 Blackwell cards and 384GB of GPU memory at $91,000, made to order in two to eight weeks.

The website's own history shows Tiny Corp listing the same configuration at $65,000 as recently as May, which puts the current price about 40% higher. The store also still lists the $32,000 Tinybox Pro, but its description tells buyers to use a configurator that no longer offers it, suggesting potential orders may not be processed.

There is some irony here: in 2024, Tiny Corp put its AMD-based box on hold over unstable firmware and launched an Nvidia version, telling customers, "If you want 'it just works,' buy green," as The Register reported. The October 24 commit scrubbed green from the configurator right down to its stylesheet, deleting the green preset label and Nvidia's accent color.

Each R9700 carries 32GB of GDDR6 with 640GB/s of bandwidth and a 300W board power rating, according to AMD, so six of them provide 192GB and 3,840GB/s in aggregate.

Tiny Corp caps each card at 225W in the six-card build, and the arithmetic suggests why: six cards at their full rating could draw up to 1,800W on their own, more than the Tinybox's 1,700W power supply, while the cap brings them down to 1,350W. The four-card build has no cap, so the same math applies: four cards at 300W total 1,200W.

The price rise is steep, but not completely unwarranted. Partner versions of the card were listed between $1,244 and $1,277 when it first went on sale in July 2025; AMD later set a $1,299 retail price, and one buyer's guide recorded street prices of roughly $1,400 to $1,900 when it rechecked them in September. At $2,500 per card, Tiny Corp now charges nearly double the official price.

Despite using an older 'G4' configuration locked to PCI-E 4.0 speeds, DDR4 memory, and an older 32-core EPYC CPU, the configuration can, when you plug in the maximum number of configurable GPUs and memory, cost as much as $25,000 without any RAID configuration memory whatsoever.

That is a long way from the first Tinybox, a $15,000 box of six Radeon RX 7900 XTX cards that drew 583 preorders in 2024. The FAQ still says the goal is to "commoditize the petaflop and enable AI for everyone."

The configurator now offers that through three AMD GPU options and no Nvidia ones, while a $91,000 Nvidia box sits in the shop, but it is unclear if such orders will be honored. Whether that reflects Nvidia's supply squeeze, the years Tiny Corp has spent building its own AMD software stack, or both, a two-word commit message doesn't convey well enough, one way or another.
