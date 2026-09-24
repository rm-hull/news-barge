---
title: Someone got Nvidia Smooth Motion working on RTX 3000 series GPUs with some
  pretty simple changes — and given the component price crisis, I think Nvidia needs
  to start making this kind of thing official
source_url: https://www.techradar.com/computing/gpu/modders-do-what-nvidia-refuses-and-bring-new-features-to-older-gpus-and-its-time-team-green-admits-were-being-priced-out-of-new-graphics-cards
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-24T16:42:28Z'
published: '2026-09-24T00:00:00Z'
description: Nvidia's driver-level Frame Generation now works on RTX 3000 series GPUs,
  via a mod, and maybe it's time for Nvidia to work up official implementations.
categories:
- Technology & Software
image: https://cdn.mos.cms.futurecdn.net/WV5DuA3g6UyUMoqUhkVGA5-2000-80.jpg
locations: []
people: []
organisations:
- AMD Radeon
- Ada Lovelace
- Ampere GPU
- DLSS
- Frame Generation
- GeForce
- GitHub
- Multi-Frame Generation
- Nvidia Smooth Motion
- PC
- RAM
- Smooth Motion
- Team Green
- Wccftech
---

![An Nvidia RTX 3090 on a wooden table](https://cdn.mos.cms.futurecdn.net/WV5DuA3g6UyUMoqUhkVGA5.jpg)

* **Nvidia Smooth Motion has been modded onto RTX 3000 series GPUs**
* **The experimental mod allows driver-level frame generation in unsupported games**
* **Nvidia hasn't officially implemented this and other features on older RTX hardware yet**

Modders continue to find new ways to implement Nvidia's latest technologies on older hardware, and now it's been done with Team Green's driver-level frame generation.

As reported by Wccftech, Nvidia Smooth Motion has been unofficially made to work on RTX 3000 series GPUs, with a new NVSmooth30 mod available on GitHub, confirmed to work on an RTX 3050 laptop and an RTX 3080 desktop GPU.

Nvidia's Smooth Motion functionality is essentially identical to AMD's Fluid Motion Frames, meaning that it enables frame generation in games that don't have official support for it — a tool that is most useful for older games or games running in emulators.

The mod works by modifying Nvidia's driver-level frame generation DLL (Dynamic Link Library) file, labeled NvPresent64, bypassing the usual compatibility checks that would stop it from working on Ampere GPU hardware, aka RTX 3000 series GPUs. It also works by "conservative metadata retargeting" from Ada Lovelace (RTX 4000 series) and targets Ampere instead.

The creator says that all users need to do is place the DLL file into the relevant game's folder and use the Nvidia Profile Inspector app to enable Smooth Motion. The process is very simple, but this is an experimental project, so it runs the risk of game bugs and crashes, or potentially other issues — and *must* not be used in online games using anti-cheat (doing so could result in a ban).

## Gamers want new features, but new GPUs are unaffordable

![An Nvidia GeForce RTX 5070](https://cdn.mos.cms.futurecdn.net/FFvnBYVHaorTEVUnXAVyQS.jpg)

Nvidia has been quite impressive with its latest technologies, notably with DLSS 5 Neural Rendering (which I saw at Gamescom 2026), and Smooth Motion has been one of many over the last few years.

The GPU market is in complete disarray due to the RAM crisis, which means prices for GPUs for both AMD Radeon and Nvidia GeForce GPUs are way too high for most people to consider an upgrade. Features like Multi-Frame Generation, Dynamic Frame Generation, and Smooth Motion are those that PC users would love, but can't use on older hardware.

Sign up for breaking news, reviews, opinion, top tech deals, and more.

Modders have consistently proved that these features can be backported in some way, with some even going as far as porting DLSS 5 onto the RTX 4080 (despite the performance hit).

DLSS 5 Neural Rendering coming to older hardware in the immediate future is unrealistic — but Nvidia has previously told me that it does plan on adding backwards compatibility at *some* point, though it's likely to come to 4000-series models first, and then we'll have to hope for 3000-series later in the future, if it's even possible.

But it feels as though features such as Frame Generation, and specifically Smooth Motion, deserve backporting attention now more than ever, as users are stuck with older GPUs.

Doing so would put Team Green in the good books of many PC gamers, and keep players from relying on unofficial mods to achieve better performance and enjoy GeForce hardware to the fullest extent.

![Google logo on a black background next to text reading &#039;Click to follow TechRadar&#039;](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg)
