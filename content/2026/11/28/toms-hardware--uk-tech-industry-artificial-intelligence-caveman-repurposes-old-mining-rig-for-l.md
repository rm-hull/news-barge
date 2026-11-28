---
title: Caveman repurposes old mining rig for local AI, pools 72GB VRAM across mismatched
  GPUs — PCIe x1 slot hits just 10% load while running a 120B model
source_url: https://www.tomshardware.com/uk/tech-industry/artificial-intelligence/caveman-repurposes-old-mining-rig-for-local-ai-pools-72gb-vram-across-mismatched-gpus-pcie-x1-slot-hits-just-10-percent-load-while-running-a-120b-model
source_site: Tom's Hardware
source_slug: toms-hardware
description: Caveman employs mining rig for local AI, finds a PCIe x1 slot is more
  than enough — link only 10% busy even when using multiple cards
image: https://cdn.mos.cms.futurecdn.net/kqVBuGYgUcKMkyHTYZKSNC-1080-80.jpg
published: '2026-11-28T00:00:00Z'
scraped_at: '2026-11-28T15:29:02Z'
categories:
- Technology & Software
- Hardware
people:
- Bruno Ferreira
locations: []
organisations:
- AI
- CMP
- CPU
- Caveman Tech
- Get Tom's Hardware
- NVIDIA
- PC
- PCIe
- Quadro
- Tom's Hardware
---

![Nine graphics cards with bare aluminum heatsinks in an open black mining rig case](https://cdn.mos.cms.futurecdn.net/kqVBuGYgUcKMkyHTYZKSNC-1080-80.jpg)

Given that GPUs with any sizable amount of VRAM or horsepower are now made of unobtainium, enthusiasts looking to run LLMs locally try all sorts of tricks to use larger models. True to their moniker, X user Caveman Tech combined wildly different cards in the same rig, but not in the usual manner. They brought back a forgotten relic: a mining rig with PCIe x1 slots. Much to their surprise, the setup worked far better than it had any right to.

For their first trick, Tech used a Quadro RTX 4000 all on its own on the PCIe x1 slot, as opposed to the standard x16 connector. Running Qwen3-8B yielded the same 56 tokens/s output speed as before, with the only drawback being a longer model load at eight seconds — but unless you're running several models, you'll want to keep it in VRAM anyway. A number of software and hardware tweaks yielded even better results, upping tok/s to 96.

> 🚨 We just discovered that a PCIe x1 mining riser does NOT slow down local AI. I took a Quadro RTX 4000, jammed it in an x1 slot on my mining rig, and tested it like crazy. The result breaks what everyone assumes about x1 risers. 🤯 ⚡ Qwen3 8B: 56 tokens/sec. The same speed as a full x16 slot. ⚡ While it's writing, the x1 link carries just a few KB per second. It's basically asleep. ⚡ The only cost: 8 seconds to load the model. That's it. Then we went hunting for hidden boosts 🔍 🔥 +24% speed in long chats by switching one memory setting (f16 KV cache) 🔥 1.75x total output: 4 requests at once = 96 tok/s 🔥 +7% tokens per watt by capping it at 110 W 🔥 A 65,000-token conversation squeezed into 8 GB And the twist: NVIDIA locks memory overclocking on this Quadro. The driver allows exactly 0 MHz. 🔒 Every result answer-checked, every number measured. That old mining rig full of x1 risers? It's an AI rig now. 🔥November 25, 2026

This result alone is contrary to the general *zeitgeist* that says low-bandwidth slots are not useful for AI work. Much like many comments, you're probably thinking that while the setup is serviceable, the true test comes when using multiple GPUs at once that need to talk to each other, so Caveman Tech obliged.

The second setup involved three cards in what can be described as a staggeringly asymmetric configuration: a CMP 170HX with 64 GB of VRAM on the primary PCIe x16 slot, the aforementioned Quadro 4000 (8 GB) on x1. The chosen model was now GPT-OSS-120B, and the pooled VRAM totaled 72 GB.

As a slap back to the naysayers, this configuration held up surprisingly well, as it turns out that with layer splitting (wherein the harness splits the model's layers across several GPUs), even the PCIe x1 link was only 10% busy. In this setup, cards only transmit the calculation results between them, not model weights.

The overall token generation speed dropped from 121 tok/s to 91 tok/s, likely due to the raw performance difference between the 170HX and the other two cards. As a point of comparison, letting the model spill to system RAM yielded only 52 token/s, less than half the original speed.

> You said x1 breaks once cards have to talk to each other. Fair. So I tested it. 🧪 Rig: CMP 170HX 64GB, Quadro RTX 4000 on x1, GTX 1660 on x4. No P2P, so every byte between cards goes through the CPU. 📊 gpt-oss-120b: • 1 card (170HX): 121 tok/s • Split onto the x1 card (layer split): 92 tok/s. The x1 link sat under 10% busy • Same split, tensor mode (cards talk every layer): 101 tok/s writing, but prompt reading drops to 671 (from 1,113) with x1 ~45% busy • Spill to CPU RAM instead: 52 tok/s So you're half right 👇 ✅ Generation: x1 holds up even when cards talk every layer ❌ Prompt processing in tensor split: that's where x1 hurts ✅ A second card on x1 still beats spilling to RAM by 1.8x Next: a device-order trick I think wins most of that gap back. Testing it. 👀November 25, 2026

Caveman Tech did try an aggressive configuration in tensor mode, wherein all cards handle a portion of all layers, and only weights and the KV cache are split between them. That did bump the output to 101 tok/s, but prompt *reading* fell from the original 1,113 tok/s to 671, with the PCIe link 45% busy.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

The conclusions are useful and straightforward: with judicious configuration, adding a card on a x1 link on a cheap mining rig is a perfectly reasonable way to expand the available VRAM, letting one use larger, smarter models that would be otherwise slow or downright impractical to run if they had to resort to system memory. It'd be interesting to see experiments with more than one GPU on x1 slots, as *in theory* the same conclusion should still hold.

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G-140-80.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.
