---
title: Jailbroken PS5s can now run local AI models at over 100+ tokens per second
  — fork of PS5LM goes native, hijacks the CPU, and accesses the GPU and more RAM
source_url: https://www.tomshardware.com/video-games/playstation/jailbroken-ps5s-can-now-run-local-ai-models-at-over-100-tokens-per-second-fork-of-ps5lm-goes-native-and-accesses-gpu-and-more-ram
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-16T11:17:44Z'
published: '2026-10-16T00:00:00Z'
description: You can even chat with the LLM remotely from other devices.
image: https://cdn.mos.cms.futurecdn.net/p6RKS3uArE9EvG6rNBgPYb-970-80.jpg
categories:
- Technology & Software
- Hardware
people:
- Jhet Borja
- Tom
locations: []
organisations:
- AI LLMs
- AdIllustrious7246
- CPU
- GPU
- Gemma
- GiB LLM
- GitHub
- Google News
- Llama
- PS5
- PS5LM
- RADV
- RAM
- Reddit
- Vulkan
---

![One Year of Xbox Series X and PS5](https://cdn.mos.cms.futurecdn.net/p6RKS3uArE9EvG6rNBgPYb-970-80.jpg)

The list of things a jailbroken PS5 can do gets longer, as Reddit user u/AdIllustrious7246 posted his fork of PS5LM, a llama.cpp port on the PS5 to run AI LLMs locally, with a massive improvement, allowing PS5LM to run natively on the PS5 and utilize the GPU to run bigger AI models such as Qwen3.8-27B at 20 tokens per second.

GitHub user cobanov posted their unofficial port of llama.cpp on Reddit 14 days ago to enable jailbroken PS5s to run AI chat models locally and offline. cobanov’s version, according to u/AdIllustrious7246, runs as a payload on the CPU, limiting it to 6 GiB of memory. Running it as a payload is basically hijacking the CPU, inserting the LLM into its instructions alongside the home screen and system services; however, RAM access is limited to about 6.25 GiB because holding more would freeze the home screen. cobanov did this just to get the llama.cpp running as soon as possible, but eventually wanted to utilize the GPU so it could run larger models; however, it seems that u/AdIllustrious7246 beat him to it with his fork.

u/AdIllustrious7246 utilized PS5\_Vulkan, a port of the RADV graphics driver that allows instructions to be sent to the PS5 GPU. Normally, the PS5 GPU would be locked down and cannot be accessed like a PC GPU, despite being an AMD GPU. PS5\_Vulkan is one of the projects that made plenty of homebrew projects possible by opening up what could be done on the GPU, including making it run LLMs.

Now that llama.cpp runs natively on the PS5, fully utilizing the GPU and opening up more RAM to be used, u/AdIllustrious7246 was able to run a 27B parameter model on it at 20 tokens per second, and smaller models like Gemma 4 E4B and Llama 3.2 3B at 61 and 124 tokens per second, respectively. Previously, the large 6.8 GiB LLM would make the system freeze and crash due to the CPU bottleneck, but GPUs are much better at processing LLMs, which is why GPU and RAM prices are insane these days.

Running it on the GPU allowed for much faster token output, and running natively allowed it to use more RAM, up to 11.4 GiB, according to u/AdIllustrious7246. Not only did the developer run the app natively, but they also gave it a dashboard, showing useful data such as live token-per-second generation, GPU and CPU use, power draw, temperatures, and how the memory splits between the model and KV cache. They also made it work with llama.cpp’s web UI, allowing users to chat with the LLM from other local devices using a browser.

While this is an impressive feat, allowing the PS5 to run as an AI assistant when it’s not used for gaming, commenters are getting flashbacks to the crypto mining GPU crisis. This is unlikely, however, as we already have an ongoing GPU and RAM crisis thanks to the demands of large AI data centers, and the PS5 doesn’t exactly have the fastest GPU or the most RAM.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Jhet Borja](https://cdn.mos.cms.futurecdn.net/niBNJTDN6c99Ri7HD5zNZ8-140-80.png)

Jhet Borja is a serial hobbyist who was taking apart toys from childhood and sketching inventions. He now loves doing DIY projects ranging from designing custom 3D-printed parts, building PCs and keyboards, all the way to woodworking. If he's not getting his hands dirty, he's probably brainstorming his next project.
