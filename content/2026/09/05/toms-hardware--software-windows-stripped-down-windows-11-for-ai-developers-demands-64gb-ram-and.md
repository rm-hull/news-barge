---
title: Stripped-down Windows 11 for AI developers demands 64GB RAM and insane 250
  GB/s bandwidth — Project Zenith will debut on AMD's flagship Ryzen AI Halo platform
source_url: https://www.tomshardware.com/software/windows/stripped-down-windows-11-for-ai-developers-demands-64gb-ram-and-insane-250-gb-s-bandwidth-project-zenith-will-debut-on-amds-flagship-ryzen-ai-halo-platform
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-05T18:13:43Z'
published: '2026-09-05T00:00:00Z'
description: This version of Windows 11 will let developers code right out of the
  box.
image: https://cdn.mos.cms.futurecdn.net/gouCtmSHKJJLP8CP9BpbQ3-2560-80.jpg
---

![AMD Ryzen AI Halo](https://cdn.mos.cms.futurecdn.net/gouCtmSHKJJLP8CP9BpbQ3.jpg) 

Microsoft just released another version of Windows 11 designed for developers, dubbed Project Zenith. According to the Windows Blogs, this operating system is optimized for developer workflows and will first become available on the AMD Ryzen AI Halo, Team Red’s direct answer to the Nvidia DGX Spark, although it will also arrive on more devices from Microsoft’s OEM and other silicon partners soon. Redmond calls Project Zenith “a ready-to-code distraction-free Windows experience on developer-class devices with 64 GB+ unified memory and 250+ GB/s memory bandwidth,” claiming that “developers can jump right in.”

 ![HBM3E vs HBM4](https://cdn.mos.cms.futurecdn.net/xi79WuWDZXzix4Fc7sXNMn.png) 


It comes with pre-installed tools like Visual Studio Code, GitHub Copilot, PowerToys, WinAppCLI, Windows Dev Skills, Intelligent Terminal, PowerShell 7, Git, GitHub CLI, AzureCLI, Core Utils, Oh My Posh, Python 3.14+, uv, NVM, Node 24+, WSL 2+ Ubuntu, and .NET 10. Aside from that, Microsoft said it pre-configures Windows 11 so developers don’t have to dig through the settings menus of various apps to configure them for their needs.

It’s primarily designed for AI developers, especially since the devices it’s installed on are designed to run 30B+ parameter models locally and without meters. The company also made it more secure for developing and running agents, deploying features such as OS-enforced identity, containment through Microsoft Execution Containers (MXC), and enterprise-grade manageability for agents.

Project Zenith is Microsoft’s response to the AI token crisis, which has caused costs to spiral out of control, especially as agents use 1000x more tokens compared to standard AI. While frontier models would still be available on the cloud, AI developers could run everything else locally through devices like this, powered by this version of Windows 11. This should help AI developers keep using their agents without feeling the bite of tokenized billing, which is especially crucial for those working in smaller organizations or experimenting at home.

One big tradeoff with Project Zenith, though, is that it’s only available on expensive devices, at least for the moment. The AMD Ryzen AI Halo, with its AMD Ryzen AI Max+ 395 processor, 128GB LPDDR5x-8000 RAM, 2TB SSD, and integrated Radeon 8060S graphics, costs $3,999.99 on Micro Center. Even if Microsoft eventually makes Project Zenith available for separate purchase and installable on other mini-PCs, the 64 GB+ unified memory requirement will be a major roadblock, especially with skyrocketing RAM prices driven by the AI boom.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Jowi Morales](https://cdn.mos.cms.futurecdn.net/gM7E2WSDg2wgCFoaDPz9yK.jpg) 

Jowi Morales is a tech enthusiast with years of experience working in the industry. He’s been writing with several tech publications since 2021, where he’s been interested in tech hardware and consumer electronics.

- 
ReplyOne big tradeoff with Project Zenith, though, is that it’s only available on expensive devices, at least for the moment. The AMD Ryzen AI Halo, with its AMD Ryzen AI Max+ 395 processor, 128GB LPDDR5x-8000 RAM, 2TB SSD, and integrated Radeon 8060S graphics, costs $3,999.99 on Micro Center. Even if Microsoft eventually makes Project Zenith available for separate purchase and installable on other mini-PCs, the 64 GB+ unified memory requirement will be a major roadblock, especially with skyrocketing RAM prices driven by the AI boom. Who pays for Windows? I'm sure it will be hacked to work on any x86 device with any amount of RAM very quickly. But the real question is if you would want to. It might be usable with 32 GB, which some Strix Halo devices ship with, but if the point is running 30B models, you might want to follow the recommendation.
 
 The**minimum viable unified memory** for running**30B** parameter LLMs locally in 2026 is**32GB** for standard usage, though**64GB** is recommended for stable performance with larger context windows.
 
 While**16GB** systems can technically run heavily quantized (Q2/Q3) 30B models, performance is significantly degraded.**32GB** allows for smoother operation of 4-bit quantized (Q4_K_M) models, which require approximately**18–20GB** of memory for weights plus overhead. To support practical context lengths (e.g., 8K+ tokens) without severe swapping or latency,**64GB** of unified memory is considered the ideal baseline for 30B-class models.
- 
Reply
 If this and all of its additions is profitable, paying for it is a no brainer.usertests said:Who pays for Windows?
 
 Same with an architect paying for AutoCad.
 Or a professional photog paying for Photoshop/Lightroom.
 etc, etc, etc.
 
If a tool brings you more profit/income than some other tool, paying for it is not a hard pill to swallow.
