---
title: New AI-to-AI technique replaces human 'bottleneck' with an AI 'modem'
source_url: https://www.techradar.com/pro/china-publishes-landmark-paper-on-ai-to-ai-technique-that-kicks-human-bottleneck-out-of-the-loop-and-replaces-us-with-an-ai-modem-c2c-brainwave-direct-connection-achieves-150-boost-in-inference-speed
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-25T04:48:41Z'
published: '2026-09-25T00:00:00Z'
description: AI models can now skip the conversation entirely and exchange internal
  information directly, changing how multi-model systems communicate.
categories:
- Technology & Software
- Business & Entrepreneurship
image: https://cdn.mos.cms.futurecdn.net/D9SxF3hiMTwj2qrLfLCYk-2121-80.jpg
locations: []
people: []
organisations:
- C2C
- Fuser
- TechRadar Pro
- Tsinghua University
---

![Hologram of the artificial intelligence robot showing up from binary code](https://cdn.mos.cms.futurecdn.net/D9SxF3hiMTwj2qrLfLCYk.jpg)

* **Cache-to-Cache lets separate AI models exchange internal information without generating text**
* **A learned Fuser converts one model’s internal data for another**
* **C2C uses selective gating to control which layers receive information**

Researchers from Tsinghua University have published a paper describing a technique that lets separate AI models exchange information without producing any text.

The method, called Cache-to-Cache (C2C), has already been accepted at ICLR 2026 and ships with open-source code available to developers.

It targets a specific inefficiency present whenever multiple language models work together inside a shared pipeline.

## Skipping words entirely

When two AI models cooperate today, one has to turn its thinking into written sentences before the other can read them.

That writing step takes real computing time and throws away small details buried inside the first model's raw thinking process.

Every AI model keeps a working memory of everything it has processed so far, known technically as a cache.

C2C skips typed language entirely by letting one model pass that working memory straight into a second model's memory bank.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

A small assistance program called a Fuser handles this handoff, reshaping and rotating the information so the second model can actually use it.

Different AI models store their memories using completely different internal layouts, sizes, and structures from one another.

Simply dumping one model's raw memory into another would likely confuse it or cause its answers to fall apart.

To prevent that, C2C includes a smart filter that decides which pieces of incoming memory are worth absorbing immediately.

Some internal layers accept the new information right away, while other layers keep reasoning independently without any outside interference.

According to the researchers, this setup makes AI models run between 100% and 150% faster during shared collaborative tasks.

That upper figure works out to roughly two and a half times quicker than the usual back-and-forth typing process.

The team also reports accuracy gains as high as 14.2% when models work together instead of operating entirely alone.

Compared against older setups where models still communicate through typed text, accuracy reportedly improved by 3.1% to 5.4%.

## Why does this method have limits

This approach currently works only with open-weight models, since it requires direct access to a model's internal cache and layer structure.

Most popular AI tools, the kind ordinary people chat with online, hide those internal details completely from outside users.

That means everyday apps like certain chatbots cannot use this shortcut unless their own creators build it in privately.

Nobody outside these companies currently knows for certain whether anyone has started using a similar method internally.

The research team argues that typed language has always slowed machines down since it forces them to think like humans do.

That argument deserves some caution, since the same team that built the system also ran every test proving it works well.

Whether this speeds things up as much as claimed will depend on other external testing of the system.

![Google logo on a black background next to text reading &#039;Click to follow TechRadar&#039;](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg)
