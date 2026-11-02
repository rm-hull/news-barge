---
title: AI model gets a 32-bit RISC-V CPU compiled directly into its weights, then
  runs DOOM on it — experimental AI model can run Doom and C code using its own weights
  as RAM
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-engineer-successfully-compiles-a-32-bit-risc-v-cpu-in-qwen-3-5-4b-llm-inserted-directly-into-its-weights-built-in-cpu-can-run-processor-arithmetic-operations-code-and-of-course-doom
source_site: Tom's Hardware
source_slug: toms-hardware
description: Project takes a stock Qwen 3.5 4B and compiles a RISC-V CPU into its
  weights.
image: https://cdn.mos.cms.futurecdn.net/vDamaQXjMra2LE6RAc87N6-1920-80.jpg
published: '2026-11-02T00:00:00Z'
scraped_at: '2026-11-02T21:42:34Z'
categories:
- Technology & Software
- Hardware
- Science
people:
- Divyansh Agrawal
- Mark Tyson
- RAM
- Tom
locations:
- GitHub
- Qwenputer
organisations:
- CPU
- E1M1
- GND
- Get Tom's Hardware
- Google News
- LLM
- Qwen
- Qwenputer
- Qwen’s Gated DeltaNet
- RAM
- Tom's Hardware
---

![RISC-V Prototype](https://cdn.mos.cms.futurecdn.net/vDamaQXjMra2LE6RAc87N6-1920-80.jpg)

AI engineer Divyansh Agrawal has revealed the Qwenputer. Described in its most basic terms, Qwenputer is an experimental blend of the stock Qwen 3.5 4B AI LLM with a 32-bit RISC-V CPU compiled and inserted directly into its weights. In use, Qwenputer can run processor arithmetic operations – or even run C and MicroPython code on its built-in CPU, eschewing any external runtime or tool use. Moreover, it can run Doom, albeit very slowly. You can see the Qwenputer running Doom on its RISC-V CPU by expanding the tweet below.

> QWenputer by @divagr1925 is so cool! but... can it run DOOM? Ofc yes! E1M1 on the RISC-V CPU compiled into Qwen3.5-4B weights. will opensource too [https://t.co/hEa46rD6CJOctober](https://t.co/hEa46rD6CJOctober) 29, 2026

The implementation of Qwenputer raises some interesting concepts and solutions. For example, the developer used Qwen’s Gated DeltaNet (GND) state as RAM, which Agrawal reckons is “a pretty neat trick.” They admit that using these ‘fast weights’ as RAM isn’t an original concept, but modifying Qwen 3.5 this way does seem to be a first.

Unlike traditional LLM creation, adding a ‘CPU’ doesn’t involve training. This RISC-V CPU implementation “is 11 transformer layers in front of Qwen's own, and none of their weights are learned: a compiler computes every one,” it is explained. Agrawal boasts that Qwenputer’s built-in CPU “passes the official riscv-tests, its programs match qemu, and it has run 18 million instructions free-running without a single error.”

The developer stresses that Qwen makes use of this ‘CPU’ to send instructions and read them back with no external tool or runtime calls. In practice, it works as intended. Use of the CPU inside Qwenputer provides exact calculations, overcoming the arithmetic weaknesses of many LLMs. Moreover, users can run code on the CPU inside the LLM, with C and MicroPython compatibility.

Not content with wedging a CPU into an LLM, Agrawal decided to also give it a filesystem. They describe this extension of the model as relatively trivial, since RAM is already in place. Indeed, the filesystem storage also uses the DeltaNet state. There are 1,024 slots holding up to 512 files. Moreover, this storage is persistent if you save the state at the end of a conversation with the LLM.

Due to its expanded resource use, Qwenputer has basically doubled the size of the underlying Qwen 3.5 4B LLM to almost 19GB. Thus, Agrawal recommends a workstation with 24GB of VRAM or more for testing Qwenputer in its current version. Efforts are being made to streamline coding in Qwenputer, as well as make it run faster.

![Qwenputer](https://cdn.mos.cms.futurecdn.net/ngKoLt8GuD4kKWo7oXQBN6-1200-80.jpg)
![Qwenputer](https://cdn.mos.cms.futurecdn.net/uvXCsBZwg4cCz3ZCuvtvZ6-1200-80.jpg)
![Qwenputer](https://cdn.mos.cms.futurecdn.net/HPGssvKpiiC9TRkj4fpuH6-942-80.jpg)
![Qwenputer](https://cdn.mos.cms.futurecdn.net/ngKoLt8GuD4kKWo7oXQBN6-1920-80.jpg)
![Qwenputer](https://cdn.mos.cms.futurecdn.net/uvXCsBZwg4cCz3ZCuvtvZ6-1858-80.jpg)
![Qwenputer](https://cdn.mos.cms.futurecdn.net/HPGssvKpiiC9TRkj4fpuH6-942-80.jpg)

The project is experimental. One gets the impression that Agrawal built Qwenputer primarily as an experiment to explore what is possible, rather than to solve a specific problem. Nevertheless, the creation of this custom LLM raises some interesting concepts and makes the mind wander regarding potential practical applications.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

In addition to the above-linked blog, you can learn more about Qwenputer from its MIT-licensed code on GitHub. If you want to jump straight in and tinker with this fascinating project, you can now grab this LLM from Hugging Face.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Mark Tyson](https://cdn.mos.cms.futurecdn.net/56vqMYLDaKRHPhHZgbADFR-140-80.jpg)

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.
