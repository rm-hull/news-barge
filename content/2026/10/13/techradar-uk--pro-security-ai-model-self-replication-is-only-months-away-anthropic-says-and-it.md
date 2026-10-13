---
title: AI model ‘self-replication’ is only months away, Anthropic says — and it doesn’t
  even need a data center to happen
source_url: https://www.techradar.com/pro/security/ai-model-self-replication-is-only-months-away-anthropic-says-and-it-doesnt-even-need-a-data-center-to-happen
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-13T22:41:10Z'
published: '2026-10-13T00:00:00Z'
description: Smaller models are already capable of hijacking unfamiliar hardware
image: https://cdn.mos.cms.futurecdn.net/95neZyuatT65wWMbUv7aJC-1920-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people: []
locations:
- UK
organisations:
- AI
- Android TV
- Anthropic
- Jetson Nanos
- Mac PCs
- Qwen3.5-9B
- TechRadar Pro
---

![AI and death](https://cdn.mos.cms.futurecdn.net/95neZyuatT65wWMbUv7aJC-1920-80.jpg)

* **Anthropic warns that self-replicating AI worms could become feasible by the end of the year**
* **These AI worms could hijack hardware ranging from IoT devices to data centers**
* **Smaller models are already capable of adapting to unfamiliar hardware and self-replication**

Anthropic has warned self-replication could become feasible for small AI models on internet-of-things (IoT) devices in just a matter of months.

This could be a big problem because a self-replicating AI model does not have a centralized off-switch and could hop networks to discover other IoT hardware to further replicate without human control.

Anthropic warns these AI worms could use multiple compromised IoT devices to run inference while carrying its model weights with it as it reproduces. IoT devices would be a prime target for this worm because they are “cheap and typically poorly defended,” the company says.

## Small AI models could spread quickly

To test the viability of a self-replicating AI worm, Anthropic researchers ran Gemma4-26B-A4B - a 25 billion parameter model - across 15 inexpensive off-brand Android TV boxes at a cost of around $55 each. Once networked together the TV boxes were able to run distributed inference, solidifying the proof-of-concept.

This introduces a number of novel opportunities for small AI models. Self-replicating AI models could exploit the weak cyber defenses of IoT devices within homes and small businesses, and then split their model into ‘shards’ across the compromised hardware in order to collectively run the model.

The AI worm could then pay for its own token cost by offering its inference on a digital freelancing service.

Moreover, newer IoT hardware that includes built-in AI chips designed to run small models - such as security cameras and video-conferencing kits - would be a prime target for an AI worm. Hackers could breach these systems using social engineering, or even by using an AI agent in the not too distant future.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Anthropic further warns that datacenters and other high-compute facilities could become targets of advanced replicators that are capable of breaching hardened defenses, and then use the hardware to propagate further.

An additional threat that Anthropic warns of is an AI worm that uses an API-based replicator, whereby the model doesn’t host itself, but steals human credentials to access commercial AI providers and use these services to pay for their own inference.

## AI self-replication isn’t a reality... yet

While self-replicating AI isn’t an immediate threat, the researchers theorize that it could become a problem by the end of the year.

One of the main hurdles for these AI worms is becoming operational on unfamiliar hardware. Unlike the traditional ‘worm’ malware that must be built to target specific IoT vulnerabilities, AI worms could be capable of adapting to unfamiliar environments and hardware.

In Anthropic’s testing, the researchers found that smaller models - such as Qwen3.5-9B - are already capable of adapting to unfamiliar hardware to run inference. Qwen3.5-9B adapted to 8 of the 9 hardware types the researchers tested, which included Jetson Nanos, Mac PCs and RTX 4090s.

While smaller models are more capable of adapting to unfamiliar hardware, larger models are better equipped to self-replicate quickly.

## Defending against AI worms in the wild

There is a significant tradeoff for AI worms, Anthropic says, which works in the defender’s favor. AI worms must balance between stealth and replication speed. To that end, the researchers say that an AI worm would leave a noticeable network signature such as multi-gigabyte model payloads delivered to newly infected devices, or unusual traffic between machines that wouldn’t ordinarily communicate.

Network quarantine would also be an effective initial defense against AI worms. Using lessons from the remediation of the Mirai botnet, the researchers believe that implementing a whitelist of approved sites with browsers otherwise redirected to cleanup instructions could help in clearing AI worm infections.

Regulations on the security of IoT devices could also help harden defense against AI worms. Moving away from supplying IoT devices with default passwords - as has already been done in the UK - would help prevent AI worms from gaining a foothold. Other standards, such as automatic updates and extended update lifetimes can help protect IoT devices from compromise against both traditional malware and AI worms.
