---
title: Anthropic warns of self-replicating AI worm threat that doesn't need data centers
  to self-improve and spread — current deployment is impractical but could become
  a worry as tech improves
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-warns-of-self-replicating-ai-worm-threat-that-doesnt-need-data-centers-to-self-improve-and-spread-current-deployment-is-impractical-but-could-become-a-worry-as-tech-improves
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-13T16:57:02Z'
published: '2026-10-13T00:00:00Z'
description: The threat is real, but still in the future, at least for now.
image: https://cdn.mos.cms.futurecdn.net/E8iSMKgnW5PaeepdDQjS4W-2000-80.jpg
categories:
- Technology & Software
- Hardware
people:
- Auxityne
- Dorito
- Ian Malcolm
- Tom
- Zak Killian
locations:
- Android Debug Bridge
organisations:
- ADB
- AGI
- AI
- AIs
- AMD
- Android TV
- Anthropic
- Apple Silicon Macs
- Frontier Red Team
- GLM-5.2
- Gemma4-26B-A4B
- Get Tom's Hardware
- Google Cloud
- Google News
- Google TPU
- HotHardware
- MI300X
- NVIDIA Jetson Nano
- PC
- Qwen3.5-9B
- The Tech Report
- Tom's Hardware
- Xeon
- Zak
---

![AI](https://cdn.mos.cms.futurecdn.net/E8iSMKgnW5PaeepdDQjS4W-1920-80.jpg)

Anthropic's Frontier Red Team has demonstrated two components of a potential AI-powered worm that, if key issues with the practical implementation are resolved, could spread across consumer devices including inexpensive Android TV boxes and smart appliances, hypothetically without relying on datacenter infrastructure. The experiments show that AI agents can configure inference across different hardware platforms and orchestrate replication across a network. There are still some serious limitations, though, particularly around the gap between the capabilities of today's models versus the hardware constraints of potential targets.

In its October 12 report, titled "AI models may be capable of self-replicating without access to a datacenter," Anthropic examines a potential class of malware called a weight-based replicator. Rather than distributing conventional executable code, it would propagate AI model weights alongside the software infrastructure needed to run inference on compromised devices, and it's not pure theory, either.

The researchers demonstrated that Qwen3.5-9B can establish an inference server on eight of nine tested hardware types, spanning NVIDIA Jetson Nano devices, Apple Silicon Macs, Xeon servers, a Google TPU, AMD's MI300X, and at least one PC with an RTX 4090, among others. They also ran Gemma4-26B-A4B across 15 off-brand Android TV boxes costing approximately $55 each, achieving a combined generation rate of 0.39 tokens per second.

Anthropic also tested whether a model could orchestrate replication across a network. The experiment used eight Google Cloud nodes running Android 15 emulators. A seeded agent propagated between nodes through an unauthenticated Android Debug Bridge (ADB) port, transferring files and establishing an inference server on each target. GLM-5.2, a titanic model with 744 billion parameters over 1TB in size, completed the replication sequence across all eight nodes in four of five trials, reaching seven nodes in the remaining trial.

![Self replicating AI](https://cdn.mos.cms.futurecdn.net/vuaLXdWSGw2MGixDapgCSb-896-80.jpg)

No other tested open-weight model was able to complete the sequence at all without orchestration from GLM-5.2, and they weren't able to meaningfully ask a larger model for help, either, despite being equipped with the capability. Naturally, GLM-5.2 wasn't actually replicating itself onto smart TV boxes; instead, it established an inference server for the much smaller Llama 3.1 8B on each target. GLM-5.2 ran on a separate inference server because the emulated nodes couldn't handle the larger model.

In other words, Anthropic demonstrated that a very large, externally hosted model can orchestrate a simplified replication sequence across machines with deliberately exposed ADB interfaces, and it showed that small models can set up inference, but it absolutely hasn't proven that a small model can independently replicate itself across consumer hardware. That distinction, admittedly fine, is nevertheless pretty important when the entire premise is that small models could soon spread without relying on datacenter infrastructure.

The experiments expose a central constraint of the research: models capable of reliably completing the replication sequence aren't currently small enough to run on inexpensive target devices, while models that fit within those devices' memory budgets, despite being capable of setting up inference, still can't reliably complete the entire process. This gap between the intelligence needed for reliable replication and the maximum model size that target hardware can support means that this threat model isn't really applicable right now, but Anthropic warns that gap could narrow, and potentially soon.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Self replicating AI](https://cdn.mos.cms.futurecdn.net/pgTFKYv8NF3TbkVzVa3SVd-917-80.jpg)

Using historical improvements in general AI capability (measured through the Epoch Capabilities Index), Anthropic projects that a model within the 30-billion-parameter class could reach the necessary capability level by the end of 2026. But once again, that's a hypothetical, and it still doesn't address the substantial efficiency problem.

Based on measured inference performance and the token requirements of its setup experiments, Anthropic estimates that establishing an inference environment would take approximately 28–51 hours for Qwen3.5-9B and 71–150 hours for Gemma4-26B-A4B at the observed throughput of its cheap Android TV boxes, and it’s worth noting that the boxes it used are configurations with 4GB of RAM, a relative luxury among these cheap set-top boxes. A model-driven replicator could take days to establish an inference environment on a new host, whereas conventional malware can execute its payload within seconds when its assumptions about the target hold. A conventional worm can spread to tens of thousands of vulnerable targets in minutes.

Model weights also impose substantial bandwidth and storage costs. Anthropic acknowledges that compromised hosts could download weights from external repositories rather than receiving them directly from an infected device, and that not every compromised machine would need to host a model. Nevertheless, distributing multi-gigabyte payloads and maintaining communication between machines running a sharded model would generate tremendous network traffic, making the activity very easy to detect.

Anthropic estimates that a hypothetical fleet comparable in size to the infamous Kimwolf botnet, which infected more than two million devices at its peak, could support approximately 133,000 instances of Gemma4-26B-A4B if every 15 devices collectively hosted one model. At the measured throughput (which benefits considerably from LAN latency), Anthropic says that such a fleet would provide roughly 40 Hopper H100-equivalents of inference capacity.

This is a very messy comparison that takes significant liberties with the data, but even at that it must be said that it's not particularly intimidating. We're talking about two million infected devices that must remain infected and operable for months (or years; infecting 2 million devices would take around 6,300 agent-years even with the fastest 28-hour stand-up speed) to produce less AI inference throughput than a few blades of previous-generation GPUs.

Anthropic notes that a real replicator could exploit other types of hardware, deploy different models across heterogeneous devices, and avoid loading model weights onto every compromised host. Those possibilities certainly complicate the comparison, but arguably they complicate it beyond the bounds of this discussion.

![Self replicating AI](https://cdn.mos.cms.futurecdn.net/BXJHcBfPxPr6yt6bFXUb7f-864-80.jpg)

The research does identify a meaningful security concern: AI agents could make malware more adaptable to unfamiliar environments and reduce the amount of target-specific engineering required. A hybrid approach, combining conventional code for routine operations with AI-driven reasoning when unexpected conditions arise, could offer some of those benefits without requiring every compromised device to run an inference engine continuously. This is definitely concerning, but we've already seen AI agents using frontier intelligence write their own code to compromise secured systems, so that specific angle on this research isn't exactly groundbreaking.

Anthropic's experiments are useful in that they provide evidence that autonomous software configuration and simplified network replication are increasingly feasible, but turning those capabilities into a materially more dangerous class of malware will take improvements in model reliability, hardware compatibility, deployment efficiency, and the ability to overcome real-world security controls, which the firm didn’t test. There’s a ton of data and some interesting findings not discussed here in the actual paper, so if you’re interested in the research you should go check it out.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Zak Killian](https://cdn.mos.cms.futurecdn.net/yonJziSpjzVFahKcUonJvi-140-80.jpg)

Zak is a freelance contributor to Tom's Hardware with decades of PC benchmarking experience who has also written for HotHardware and The Tech Report. A modern-day Renaissance man, he may not be an expert on anything, but he knows just a little about nearly everything.

* This reads like the kind of thing we were warned about via movies starring a buff Austrian guy and games starring a girl who wears a Dorito chip on her ear. I also immediately think of a rather well-known Ian Malcolm quote.  
    
  Are we really ready for science fiction to become science non-fiction regarding AI? People constantly try to downplay that this sort of thing can and does happen with other tech. I'm mildly worried that Anthropic has already created and lost control of some sort of AI worm given how cavalier the biggest companies have been about racing towards AGI at any cost. Reply
* hotaru251 said:sad that the current internet will eventually likely need purged and replaced due to stuff liek that occurringLOL, how are you going to purge it and what are you going to replace it with?  
    
  This is Pandora's Box stuff. There's no going back to how things used to be.  
    
  Auxityne said:"And the only way you can protect yourselves from our hypothetical apocalypse worm is by giving us tons of money!"Even that won't do it. Nobody can guarantee this won't happen. Perhaps they will take the antivirus route and have "guardian" AIs that actively watch for & try to block rouge or other malicious AIs...  
    
  Somewhat paradoxically, this*could* be at least*delayed* if investors stopped pumping money into this sector, forcing them to slow down!
  Reply
