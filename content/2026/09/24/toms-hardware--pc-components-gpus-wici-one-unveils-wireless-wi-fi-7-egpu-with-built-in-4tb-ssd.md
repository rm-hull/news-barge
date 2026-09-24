---
title: New wireless Wi-Fi 7 external GPU enclosure comes with a built-in 4TB SSD for
  local AI — $1,999 box leverages WiFi 7 to present a remote card as local
source_url: https://www.tomshardware.com/pc-components/gpus/wici-one-unveils-wireless-wi-fi-7-egpu-with-built-in-4tb-ssd-for-local-ai-usd1-999-box-leverages-wifi-7-to-present-a-remote-card-as-local
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-24T13:32:03Z'
published: '2026-09-24T00:00:00Z'
description: There's onboard storage for keeping model weights, too.
categories:
- Technology & Software
- Hardware
image: https://cdn.mos.cms.futurecdn.net/TwwYe9MvcPiiF6eEoGsVRc-2553-80.png
---

![WiCi One external GPU](https://cdn.mos.cms.futurecdn.net/TwwYe9MvcPiiF6eEoGsVRc.png)

External GPUs (eGPU) have been tried time and again, and while they have found their niche among laptop users, they're not commonplace. Now that the AI craze is in full swing, more people are looking into owning a graphics card of some sort for the single purpose of running LLMs locally. The WiCi One is designed with that specific scenario in mind, but adds wireless connectivity, multi-device support, and onboard storage.

That list of words usually doesn't belong in the same sentence as GPUs, so it merits close inspection. First and foremost, the WiCi One leverages the WiFi 7 protocol to transmit data to and from the card. The firm says that client machines keep a GPU driver that makes the operating system think it's a graphics card just like any other, while in reality they'll be talking to the WiCi One over the network.

However, as WiCi explains in great detail, just blindly doing that would make for a terrible eGPU, as the standard communication between host and card is extremely chatty. That's not a problem with the sub-microsecond latency of PCIe 5.0, but would quickly turn even basic status querying operations into multi-second affairs. Large computations with lots of data shuffled back and forth could hypothetically take hours.

The company claims its driver software performs a great deal of data caching, deduplication, and compression, and is also very judicious about what type of hardware requests can be handled locally versus those that really do need to go over the airwaves.

This mode of operation and its corresponding separation of concerns bring several advantages: theoretically, the one GPU could be used on multiple machines. There are Python libraries for passing the WiCi One as any other GPU to LLMs, and also a standard HTTP API for network access, once again lending credence to the fact that multiple clients could use the WiCi One without any special configuration.

Running LLMs means shuffling a substantial amount of data back-and-forth, and contemporary models with a Mixture-of-Experts (MoE) architecture can run locally using an SSD as a fallback. WiCi took a clever approach and incorporated a 4 TB PCIe 5.0 SSD directly into the enclosure, in a bid to store model weights to both enable larger models and indirectly save on cross-network transfers.

WiCi also mentions that the card can also run games without modification, but doesn't elaborate on what kind of performance is expected. The documentation only ever mentions Vulkan and Direct3D, and hedges the fact that "[not] every API must be complete on day one." WiFi makes for a poor technology to underpin a real-time endeavor like pushing millions of polygons and textures in, and the resulting images out, in just 16.67ms for 60 FPS, so we'll venture that gamers will be best served with conventional eGPUs.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

The base spec comes with an RTX 5060 Ti 16 GB graphics card, and is slated for a 2026 Q4 preview, with no release date set in stone. WiCi plans to offer a variant with an RTX 5090 and its 32 GB of VRAM, albeit there's no word on when that will arrive, much less at which price — especially considering those cards alone are currently going for well over 7 grand, and have been spotted selling for far more.

The asking price for all this is $1,999 for early signups, and $2,599 otherwise, for the base spec. Those figures might sound steep, but they're actually fairly reasonable if the WiCi packaging and software stack deliver. A quick skim of Newegg puts an RTX 5060 Ti 16 GB graphics card at $800 or more, while an NVMe 4 TB PCIe 5.0 SSD is a little pricier at $850. Once you factor in a hypothetical $100 for a power supply and another $100 for the case, Wi-Fi card, and assorted bits and bobs, you're at $1,850 already.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.
