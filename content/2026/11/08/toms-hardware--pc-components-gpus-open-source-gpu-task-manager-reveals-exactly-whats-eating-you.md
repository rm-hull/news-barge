---
title: Open-source GPU task manager reveals exactly what's eating your VRAM — Microsoft
  VP's new GPU Taskman tool reveals every process using your GPU, how much memory
  each uses, and breaks down AI and LLM workloads
source_url: https://www.tomshardware.com/pc-components/gpus/open-source-gpu-task-manager-reveals-exactly-whats-eating-your-vram-microsoft-vps-new-gpu-taskman-tool-reveals-every-process-using-your-gpu-how-much-memory-each-uses-and-breaks-down-ai-and-llm-workloads
source_site: Tom's Hardware
source_slug: toms-hardware
description: A new open-source GitHub project called gputaskman has been released
  by Microsoft VP Scott Hanselman.
image: https://cdn.mos.cms.futurecdn.net/j6M4fBvsjExPSFtuP5xYyG-1920-80.jpg
published: '2026-11-08T00:00:00Z'
scraped_at: '2026-11-08T17:55:26Z'
categories:
- Technology & Software
- Hardware
people:
- Hanselman
- Mark Tyson
- Tom
locations:
- GitHub
- Hanselman
organisations:
- GPU Taskman
- GitHub
- Google News
- MIT
- Microsoft VP
- PRs
- Scott Hanselman
- Tom's Hardware
- Unigine Valley GPU
---

![gputaskman in action](https://cdn.mos.cms.futurecdn.net/j6M4fBvsjExPSFtuP5xYyG-1920-80.jpg)

Microsoft VP Scott Hanselman has revealed a new open-source GitHub project called gputaskman. The name neatly encapsulates the headline role of this tool, a GPU-focused task manager, but its scope might be broader than you expect. This new tool for Windows, Linux, and macOS can show per-process GPU usage, VRAM consumption, active runtimes, and many more stats. It also breaks out AI/LLM task-specific information.

> There's a lot going on in my GPU. I'm making a GPU Taskman to get insights to where my GPU memory is going. PRs welcome [https://t.co/6FwKqnFWDWNovember](https://t.co/6FwKqnFWDWNovember) 3, 2026

On social media, Hanselman snappily makes clear the technical itch that gputaskman was designed to scratch. “There's a lot going on in my GPU,” wrote the prominent public face of Microsoft's developer ecosystem. “I'm making a GPU Taskman to get insights to where my GPU memory is going.”

There are several example screenshots of GPU Taskman in use by the Microsoft VP. They clearly show the kinds of data that are presented in the terminal-like display that pops up in the tool. Hanselman’s tweet shows that the most VRAM-hungry app on his RTX 4080S system is the desktop windows manager. That is selected in the list, and more details are shown for this task at the bottom of the window. Also, we see AI/LLM apps consuming VRAM, and a few Windows staples.

![gputaskman in action](https://cdn.mos.cms.futurecdn.net/CJLAMoHHwMZL8chMPQ8k6H-1200-80.jpg)

In a GitHub-embedded image, we see what details are broken out when the llama-server.exe app is selected in the list. The bottom of the window breakdown reveals that Qwen3-0.6B is being used, and there’s a breakdown of its weights, the KV cache, the number of parameters, and more. Very informative.

As the Microsoft developer has made portable Windows downloads of the latest v0.3.0 release of gputaskman, I couldn’t resist giving it a spin. Upon launch, I found that no tasks were using the discrete GPU in my laptop… so I fired up ye olde Unigine Valley GPU benchmark to stir the RTX 4060 from its slumber. I note the live-streaming charts showing GPU load, VRAM use, temperature, and so on are more prominent in my screenshot than in Hanselman’s examples. Perhaps he screen-shotted a previous version of the tool.

![gputaskman in action](https://cdn.mos.cms.futurecdn.net/wi6yEzpHEwnvbN3qSJbG6H-1200-80.jpg)

There’s a lot more information about gputaskman, its inner workings, and even its source code, on the linked GitHub repository. Hanselman is sharing his “experimental software” tool under the permissive MIT license. Finally, in social media comments, he hints that expanded GPU monitoring capabilities could be coming to Windows as standard.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Mark Tyson](https://cdn.mos.cms.futurecdn.net/56vqMYLDaKRHPhHZgbADFR-140-80.jpg)

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.

* Hmm.  
    
  We have all of these task managers and process lists, yet can anybody actually identify the processes which go into feeding all of the OS-level advertisements?  
    
  I doubt Microsoft was nice enough to name it YourAnnoyingAdvertisements.exe. Reply
