---
title: Jailbroken PS4 runs 9-billion-parameter AI model at up to 43 tokens per second
  — open-source Garlic LLM bypasses drivers to talk directly to the 2013-era GPU
source_url: https://www.tomshardware.com/uk/video-games/playstation/jailbroken-ps4-runs-9-billion-parameter-ai-model-at-up-to-43-tokens-per-second-open-source-garlic-llm-bypasses-drivers-to-talk-directly-to-the-2013-era-gpu
source_site: Tom's Hardware
source_slug: toms-hardware
description: Garlic LLM runs Alibaba’s Qwen3.5-9B on a jailbroken PlayStation 4’s
  GPU, fully offline, at 31 to 39 tokens per second.
image: https://cdn.mos.cms.futurecdn.net/NiEzQj4gSZE2jaQaCMEuvG-1800-80.jpg
published: '2026-11-16T00:00:00Z'
scraped_at: '2026-11-16T19:36:43Z'
categories:
- Technology & Software
- Hardware
- Video Gaming
people:
- Shane Downing
- Tom
locations:
- Vulkan
organisations:
- AI
- AMD GPU
- AMD GPUs
- Alibaba
- CPU
- GCN
- GTA
- Garlic LLM
- Gemma
- Get Tom's Hardware
- GitHub
- GoldHEN
- Google News
- LLVM
- Llama
- Nvidia
- PC
- PS4
- PS5
- PS5LM
- Playstations
- RADV
- SFF
- Shane Downing
- Sony
- Tom’s Hardware
- Vulkan
- Xbox
---

![A black PlayStation 4 console lying flat with a DualShock 4 controller in front of it](https://cdn.mos.cms.futurecdn.net/NiEzQj4gSZE2jaQaCMEuvG-1800-80.jpg)

Developer Leonardo Alegría’s open-source project Garlic LLM lets a jailbroken PS4 run the 9-billion-parameter Qwen3.5-9B AI model offline on the console’s 2013-era GPU. The app talks to the GPU directly, and the model is shrunk to about 4.5GiB to fit in the console’s memory, running at 31 to 39 tokens per second.

The project, named after the memory the GPU reads directly — its sibling memory type is “Onion” — relies on a PS4 running GoldHEN, which is a homebrew enabler for exploited consoles. Garlic LLM is a free, single 5.66GB download, available on Hugging Face and installable through the PS4’s Package Installer, with about 6GB free needed, or 12GB if the package is first copied to the console’s internal disk. The developer tested it on a base/Slim PS4 on firmware 11.52.

![Garlic LLM chat screen on a PS4 showing a bulleted answer on why the sky is blue and sunsets are red](https://cdn.mos.cms.futurecdn.net/cSYh9cdshnXtQ5TtvLpAXG-1200-80.png)

It’s capable of voice conversation, with spoken replies in seven languages through the Chatterbox speech model and the chat model running at about 22 tokens per second. A held controller button also lets it take dictation with Nvidia’s Parakeet TDT 0.6B v3 speech-to-text model, which supports 25 European languages. Parakeet models also power local transcription and dictation apps such as Meetily and Hex. The main model is Alibaba’s small open-weight Qwen3.5-9B, which, at the claimed 31 to 39 tokens per second in text chat — the prompt and test method are not given — is usable on the console.

The closest comparison is the PS5LM fork, which runs llama.cpp as a native app on the PS5 and reaches the console’s AMD GPU through PS5\_Vulkan, a port of the RADV driver. The open-source llama.cpp is a widely used program for running language models locally, and RADV is the open-source driver that lets AMD GPUs run Vulkan, the graphics and compute API. On the PS4 there is no such driver layer for homebrew; Garlic LLM uses neither llama.cpp nor a Vulkan port, or so it would appear.

The model’s operations, such as matrix multiplies over 4-bit weights, are compute kernels written in OpenCL C and compiled with LLVM for AMD’s Graphics Core Next (GCN) architecture. The weights are kept in that “Garlic” memory, while the CPU side, in plain C, handles the tokenizer, the interface, text rendering, and audio. The pipeline runs from the prompt to the CPU tokenizer, then, for each token, a PM4 command buffer — the low-level commands a graphics driver would normally generate, which, in this case, the app builds itself — and the GCN kernels, before the token is displayed or spoken. The whole thing is built with the open-source OpenOrbis PS4 toolchain.

One immediate question is how you fit a 9-billion-parameter model in the console’s 8GB of memory, which the CPU and GPU share. At 8 bits per weight, you have one byte per parameter, meaning you’d need at least 9GB, with typically more than that required overall. Part of the answer is 4-bit (“Q4”) weights, which take half as much, although 3-bit (“Q3”) weights, at about 3.5 bits with scales, are used for the two largest matrices in each layer.

Using the combination gets you to about 4.5GiB, versus about 4.9GiB if it were all 4-bit. The attention, or KV, cache is also 4-bit, which lets a 16K-token context fit, in comparison to the model’s native 256K. The Parakeet dictation model adds 0.33GiB and the Chatterbox voice models 0.29GiB and 0.09GiB, for a grand total of 5.23GiB, or 5.62GB, which closely matches the 5.66GB package size.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

The next question is performance. Qwen3.5 comes with a multi-token prediction (MTP) head, and Garlic LLM uses it to draft up to two tokens ahead, with the full model verifying. This matches what the model was trained for, and the vLLM instructions on Alibaba’s model card use two speculative tokens. The project credits this for its chat speed on 2013 hardware.

Code also comes out faster with this setup, at up to 43 tokens per second. Also detailed is the default temperature, or model variability, which is 0.7 — Alibaba recommends 0.7 for general tasks with thinking off and 1.0 with it on — although the demo video uses 0, so it is predictable. At 35 tokens per second, the middle of the reported performance range, a 300-token answer takes under nine seconds. As a comparison, the PS5 ran the three-times-larger Qwen3.8-27B at about 20 tokens per second and the smaller Gemma 4 E4B and Llama 3.2 3B at 61 and 124, respectively, which is potentially quicker.

The PS4 Pro is “not tested yet,” but the developer is asking users for reports on GitHub. The PS5 is not supported as the app is written specifically for the PS4’s GPU and system software. The app itself contains no exploit, but GoldHEN is installed at the user’s own risk.



Follow Tom’s Hardware on Google News, or add us as a preferred source, to get our latest news, analysis, & reviews in your feeds.

![Shane Downing](https://cdn.mos.cms.futurecdn.net/Zosi9VrDytS9FkgJiHvc69-140-80.png)

Shane Downing is a Contributing Writer for Tom’s Hardware, covering consumer storage, PC hardware, and AI.

* I have to wonder if this is going to lead to people buying up Playstations the way they've been buying up GPUs. I'm going to laugh so hard if what Sony is claiming to be excitement over GTA 6 turns out to actually be jailbreakers wanting to run local AI on affordable hardware.Reply
* bigdragon said:I have to wonder if this is going to lead to people buying up Playstations the way they've been buying up GPUs. I'm going to laugh so hard if what Sony is claiming to be excitement over GTA 6 turns out to actually be jailbreakers wanting to run local AI on affordable hardware.I would only buy PS5/PS6/Xbox if they were fully jailbroken Linux-capable PCs, even if AI didn't exist.  
    
  I doubt AI will drive PS5 sales. It's kind of like an RX 6700 with 16 GB, but with less memory available if you need to run an operating system.  
    
  A used PS5 is around $400. You can get a used 7600 XT 16GB for around the same price which should be much better, especially with the PC having its own RAM. Or you go to $700 for an RTX 4060 Ti 16GB to crush it.  
    
  A PC adds cost, but you might be able to get it down to $200 or less. Main factors being the large case size needed, so no SFF office PCs permitted, and the appropriate power supply. Reply
