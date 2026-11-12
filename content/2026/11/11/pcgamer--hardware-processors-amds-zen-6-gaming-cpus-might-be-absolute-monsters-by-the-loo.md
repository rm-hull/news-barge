---
title: AMD has taken the wraps off its Zen 6 architecture—and your next gaming chip
  might be a monster
source_url: https://www.pcgamer.com/hardware/processors/amds-zen-6-gaming-cpus-might-be-absolute-monsters-by-the-looks-of-the-server-chips-and-theres-a-3d-v-cache-variant-to-keep-an-eye-on/
source_site: PC Gamer
source_slug: pcgamer
description: A tantalising tease.
image: https://cdn.mos.cms.futurecdn.net/rzParbRmcG9d7cPPxniue9-2560-80.jpg
published: '2026-11-11T00:00:00Z'
scraped_at: '2026-11-12T02:15:08Z'
categories:
- Technology & Software
people:
- Lisa Su
- Mercy
- Zen
locations:
- Nova Lake
- Techpowerup
- Venice
organisations:
- 18A-P
- 3D V-Cache
- AMD
- CPU
- EPYC
- Intel
- PC Gamer Circuit Breaker
- Ryzen
- TSMC
- Zen
---

![AMD Ryzen 7 9800X3D processor](https://cdn.mos.cms.futurecdn.net/rzParbRmcG9d7cPPxniue9-1920-80.jpg)

AMD has revealed a substantial amount of detail on its next-gen Zen 6 CPU architecture, in the form of a technical deep dive on its newly-unveiled EPYC "Venice" range of server chips.

These models will find themselves buried deep within data centers, but the Zen 6 architecture itself looks extremely promising for next-gen Ryzen desktop processors—and quite possibly, your next gaming CPU.

## AMD Zen 6 CPU architecture

Current Zen 5 CCDs with full-fat performance cores max out at eight cores per chiplet, but a single Zen 6 CCD, based on TSMC’s cutting-edge N2P node, is stuffed with 12 of the beasties—alongside 4 MB of L3 cache per core, the same as Zen 5. That adds up to a total of 48 MB of L3 cache per CCD, as opposed to the 32 MB you'd find on an 8-core Zen 5 chip (via Techpowerup).

A current gen Zen 5 CPU with more than eight cores has to spread them across two CCDs, which can result in latency as the two communicate with each other during multi-threaded tasks. With the upped core count per CCD, a 12-core Zen 6 chip would face no such performance penalty.

It's the "c" core counts that have received the biggest jump in density, though. These aren't the same as Intel's Efficiency cores, instead amounting to scaled down performance cores designed to take up less die space and spread the workload during heavily multi-threaded tasks.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AMD EPYC "Venice" - Zen 6 vs Zen 5 comparison |  |  |  |  |
| Row 0 - Cell 0 | **Zen 5c**|** Zen 6c**|** Zen 5**|** Zen 6** |
| **Cores per complex** | 16 | 32 | 8 | 12 |
| **L3 cache per core** | 2 MB | 4 MB | 4 MB | 4 MB |
| **L3 total per complex** | 32 MB | 128 MB | 32 MB | 48 MB |
| **Maximum frequency** | 3.7 GHz | 4.1 GHz | 5.0 GHz | 5.2 GHz |
| **Maximum cores** | 192 | 256 | 64 | 96 |

In the case of Zen 6c, 32 cores can be squeezed onto a single core complex, double that of a Zen 5 equivalent. The L3 cache per Zen 6c core has been upped, too, from 2 MB per core to 4 MB. That means a fully-stocked 32-core Zen 6c complex ends up with a stonking 128 MB of L3 cache to play with, quadruple that of a maxed-out Zen 5c version.

## Zen 6 speeds

In terms of clock speeds, the full-fat Zen 6 cores on a Venice server chip have a maximum clock frequency of 5.3 GHz, while the Zen 6c cores top out at 4.1 GHz. Rumours suggest the eventual Zen 6-based Ryzen desktop chips will top out much higher than that, potentially above 6 GHz, although we'll have to wait and see in that regard.

The PC Gamer Circuit Breaker newsletter breaks down the latest PC gaming tech, and finds you the best deals on the best products

AMD has also improved Zen 6's branch prediction, with optimized prediction tables and larger prediction queues, while the return address stack has also been buffed from 52 to 64 entries, alongside two branch predictions per cycle. In essence, Zen 6 should be better at anticipating instructions, and should also recover faster from errors. The reorder buffer, integer physical register, and operation cache sizes have been increased, too.

AMD claims up to a 27% increase in Zen 6's instructions per clock (IPC) performance compared to Zen 5 in certain server workloads. That's a pretty massive uplift, and could bode well for whatever consumer chips we end up receiving based around the architecture.

## 3D V-Cache

*Speaking of which,* I'd imagine many of you are curious about the addition of AMD's all-singing, all-dancing 3D V-Cache to this potent new design. Well, one of its new Venice chips is called the Venice-X 9006X SP7, and variants go all the way up to 96 cores with 1152 MB of L3 cache. That's 144 MB of L3 cache for every 12-core CCD, which works out at 48 MB of traditional cache alongside 96 MB of stacked 3D V-Cache.

![AMD Ryzen 7 9800X3D processor](https://cdn.mos.cms.futurecdn.net/UZf4p7JE3uqji82cC3Eqe9-1200-80.jpg)

To put that into perspective, the eight-core Ryzen 7 9800X3D (our best gaming CPU pick, no less) has 96 MB of L3 cache in total, with 64 MB being made up of 3D V-Cache. And that's a beastly gaming chip. Many games enjoy the benefits of all that cache sitting so close to the cores, so the prospect of a 12-core successor with 144 MB of L3 cache sitting on board is enough to give me the vapours.

And with no latency penalty between those cores in multithreaded loads, and a potentially hefty performance increase across the board? Mercy, that'd likely be a very impressive gaming chip.

As for when we might see Zen 6-based Ryzen desktop CPUs? Well, this launch is purely focussed on EPYC server implementations, which are beginning to ship now, so exact dates for consumer chips remain to be seen. It seems likely at this point that we might be looking at a first-half of 2027 release, although with everything going on at the moment and a new production process to contend with, all I can really do is speculate.

![AMD&#039;s Dr. Lisa Su on stage at the Advancing AI 2026 event, giving a keynote, discussing Zen 6 AMD Epyc Venice.](https://cdn.mos.cms.futurecdn.net/h3WffBZqLEKCyYMZBMjPB3-1200-80.jpg)

And while we're talking about new CPUs, there's always Intel's upcoming (and if you believe the rumours, even faster) Nova Lake chips to keep your eye on. Intel's first 18A-P client chips are reportedly on track for a CES 2027 reveal, which happens in January. It's been a while since we've seen a clash of the CPU titans, so keep your eyes peeled around that time.

Still, AMD's new architecture looks mightily impressive on paper. Given all the hubbub and bad news surrounding PC hardware this year, perhaps some new, ultra-speedy processors are a hope I can cling to going into 2027. Until I see the eventual pricing, I would imagine.

Aw. I made myself sad.

![AMD Ryzen 9 9800X3D processor](https://cdn.mos.cms.futurecdn.net/5ryUJb6snbbQMdpHJu7i8W-140-80.jpg)
