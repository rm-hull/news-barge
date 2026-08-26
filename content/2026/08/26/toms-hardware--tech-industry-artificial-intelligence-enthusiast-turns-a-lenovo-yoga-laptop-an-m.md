---
title: Enthusiast turns a Lenovo Yoga laptop, an M.2 slot, and AMD Radeon RX 7900
  XT into 'the world's stupidest' desktop for local AI chatbots — M.2 franken-rig
  crippled by laptop DRAM swap
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/enthusiast-turns-a-lenovo-yoga-laptop-an-m-2-slot-and-amd-radeon-rx-7900-xt-into-the-worlds-stupidest-desktop-for-local-ai-chatbots-m-2-franken-rig-crippled-by-laptop-dram-swap
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-26T13:12:41Z'
published: '2026-08-26T00:00:00Z'
description: Predictably, they ended up regretting their life decisions, but it was
  seemingly a fun ride.
image: https://cdn.mos.cms.futurecdn.net/AnQTdsfDi6CsBxanpSjUtU-1080-80.png
---

![Lenovo Yoga with Radeon 7900 XT](https://cdn.mos.cms.futurecdn.net/AnQTdsfDi6CsBxanpSjUtU.png) 

About a month ago, techie Redditor Alternative-Panic69 (Panic) had the idea of acquiring a Radeon 7900 XT with 20 GB of VRAM for LLM use, a significant undertaking in their home country of India. They found one for $550, an excellent deal even by Western standards, and they were off to the races with Qwen and GLM in tow. Panic intended to use this card in a Lenovo M910Q desktop, but the machine wouldn't cooperate, so recently they turned to the next logical thing: a Lenovo Yoga laptop.

As Panic themselves put it, they took the "completely sane decision to perform surgery on [their] laptop." Armed with an ADT-Link PCIe external cable connector wired to the laptop's M.2 slot, a DeepCool PL750D power supply, and some quick bottom-panel removal, they managed to wire everything together in a manner that mostly worked.

With the M.2 slot now unavailable, the first challenge was having somewhere to boot from, a task accomplished by a USB SSD. Getting a picture with the main display hooked into the 7900 XT "worked beautifully", with Furmark doing 500 FPS at 1080p. This arrangement had to go, though, as the display framebuffer(s) were eating into precious VRAM necessary for the models, so the integrated graphics silicon was back to its original assignment.

Panic mused at how "[their] laptop was sitting there looking like it had been converted into a PCIe development board," but ended up having some harsh realizations about trying to wrangle fairly large LLMs (Qwen 35B A3B, GLM-4.7 Flash) exclusively on the GPU, all with a 128K-token context window.

Another Redditor pointed out that was a classical "pick two out of three" situation, and indeed that was the case, as Panic found that ultimately his laptop's memory (or lack thereof) proved to be a serious bottleneck. The large context window needed lots of associated data in RAM, and eventually the available DRAM was exhausted, and the laptop began using swap space, grinding performance to a halt, to the point where the GPU was "being idle, occasionally in bursts."

The story ends in somewhat predictable fashion: as interesting and visually striking this project was, they needed their laptop as an actual mobile device again, so they elected to buy the cheapest AM4 machine they could find to fit the Radeon 7900 XT and the power supply in. As Panic themselves said, "buying an old office tower would have been the sensible solution. I wasn't here to be sensible."

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.
