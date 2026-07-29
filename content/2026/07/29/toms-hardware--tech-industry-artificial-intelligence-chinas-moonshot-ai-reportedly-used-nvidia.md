---
title: China's Moonshot AI reportedly used Nvidia Blackwell chips for training Kimi
  K3 — company circumvented both U.S. export and Chinese import controls to acquire
  compute
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/chinas-moonshot-ai-reportedly-used-nvidia-blackwell-chips-for-training-kimi-k3-company-circumvented-both-u-s-export-and-chinese-import-controls-to-acquire-compute
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-29T10:48:17Z'
published: '2026-07-29T00:00:00Z'
description: The US gov't says Moonshot has purchased Blackwell systems and rented
  time on foreign clouds to help it train models.
image: https://cdn.mos.cms.futurecdn.net/smfS6N7aideSB7eA7JSz2H-1920-80.jpg
---

![Nvidia Blackwell Ultra server stack.](https://cdn.mos.cms.futurecdn.net/smfS6N7aideSB7eA7JSz2H.jpg) 

Keeping the upper hand in the AI arms race has become a vital goal for both the U.S. and China, and Nvidia's Blackwell AI chips are one of many flashpoints in that fight. The US government bars their sale to Chinese firms, while Chinese policies block their import as the country tries to spin up an advanced AI chip industry of its own.

But as we've discussed multiple times and then some more, Chinese AI firms are quite creative with workarounds for these restrictive policies. That's the case of Moonshot AI, which has reportedly made good use of Blackwell for training the recently released Kimi K3 frontier-level model, and is seemingly looking to obtain additional access in preparation for Kimi K4.

*The Information* says "people with knowledge of the matter" told it that Moonshot employed two Chinese firms that have Blackwell chips in their respective datacenters despite the bilateral restrictions we mentioned. Given that those chips are scarce enough right now even when obtained legitimately, it's unsurprising that neither firm had enough of them on hand to let Moonshot train K3. This reportedly forced Moonshot to figure out how to join multiple eight-chip Blackwell servers together and across datacenters in order to harness the necessary computing power.

The report also mentions "a researcher at a major Chinese tech firm who works on model training" as stating that Kimi K3 has "started a new round of arms race" in the country's AI industry. They further added that training frontier models is difficult or impossible with the promising but slowly developed homegrown chips. By that source's account, Chinese AI accelerators remain a generation or two behind Nvidia's current offerings and are reportedly several months in backorder.

For inference work, Moonshot reportedly relies on Nvidia's China-market HGX H20, a last-gen chip that isn't blocked by trade laws on either side of the Pacific. The firm recomends setups with at least 64 H20 GPUs for running Kimi K3. Those requirements, combined with that frontier model's desirability, meant that Moonshot quickly ran out of computing capacity to run K3 and currently has subscriptions on a waiting list. Given it's an open-weight model, and that its weights were released this week, many other inference providers are serving it, perhaps alleviating that bottleneck.

Meanwhile, White House Director Michael Kratsios claimed last week in a tweet that that Moonshot AI both "acquired GB300-equipped servers and has accessed GB300s in Thailand." While buying Blackwell chips is illegal, renting them is apparently fair game, at least until the proposed Remote Access Security Act takes effect. That law is designed to prevent the rental loophole by treating remote access as an export event. There's no telling exactly how the U.S. would enforce this law across other jurisdictions, though.

At any rate, the Department of Commerce is formally investigating if Chinese firms are accessing advanced U.S. chips like Blackwell GPUs, and that's likely to be an ongoing point of contention as the war for frontier model supremacy continues.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

In China, it's an open secret that many of the country's high-level own or have access to Blackwell and other advanced chips, but despite all the trade restrictions and pushing the usage of local-made chips, the CCP has seemingly yet to crack down on said AI players. Some have theorized that the turning of this blind eye is intentional so Chinese firms like Moonshot can catch up to the likes of Anthropic and OpenAI.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.
