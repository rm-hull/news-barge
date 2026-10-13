---
title: Microsoft CEO Satya Nadella wants your PC to become 'an infinite software factory'
  in final blow to the app store concept — but I'm afraid businesses won't bite the
  AI apple
source_url: https://www.techradar.com/pro/satya-nadella-wants-your-pc-to-become-an-infinite-software-factory-in-final-blow-to-the-app-store-concept-but-im-afraid-businesses-wont-bite-the-ai-apple
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-13T06:47:34Z'
published: '2026-10-12T00:00:00Z'
description: Microsoft wants every employee building apps with Copilot
image: https://cdn.mos.cms.futurecdn.net/6bfb10cc526d296d87da9aa41e7ed3b3-420-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Anushree Verma
- Bill Gates
- Brandon Thomas
- Jared Spataro
- Pavan Davuluri
- Satya Nadella
locations:
- Azure
- Nadella
organisations:
- AI at Work
- Anthropic
- CIOs
- CISOs
- Command Line
- Dataiku
- Frontier
- Gartner
- GitHub Copilot
- Harris Poll
- Hybrid Intelligence
- MAI-Code-1.1 Flash
- Microsoft Execution Containers
- NVIDIA RTX Spark
- Nadella
- Nvidia
- RTX Spark
- Retool
- Surface Laptop Ultra
- TechRadar Pro
- Windows and Devices
---

![Satya Nadella](https://cdn.mos.cms.futurecdn.net/6bfb10cc526d296d87da9aa41e7ed3b3-420-80.jpg)

* **Microsoft CEO Satya Nadella says Copilot Code and local AI make every Windows PC an infinite software factory with no cloud token spend**
* **Rather than killing app stores, Microsoft is moving app hosting into Copilot, while IT leaders stay wary of citizen-built tools**
* **Microsoft's own engineers say local inference doesn't make sessions offline, and the routing ships later this month**

Microsoft CEO Satya Nadella has a new pitch for the Windows PC, and it targets one of the most lucrative ideas in consumer tech.

In a post on X summarizing Microsoft's recent Windows and Surface event, Nadella told followers they no longer have to settle for whatever an app store happens to stock, because Copilot can now build the software they need on the desktop without spending any cloud tokens.

He wrote this idea without mincing any words, saying, "Your PC becomes an infinite software factory."

> Today marks a new chapter for Windows, as we bring unmetered intelligence to every desk and every home, and make every PC a place where agents can work securely on your behalf. Some highlights of what we announced: • MAI-Code-1.1 Flash: 137B parameter coding model w/ 256K context window, which is now optimized to run on your PC! • GitHub Copilot now hands off work to local models like MAI-Code-1.1 Flash, helping projects cost a lot less without sacrificing quality. • With Hybrid Intelligence, Copilot can now take action directly on the PC and keep sensitive work on your device. • And with Code in Copilot, you can essentially build any software you need on your desktop, without any cloud token spend, and it’s just super at it. You’re no longer limited to what’s in an app store! Your PC becomes an infinite software factory. • Security is foundational to all this, which is why we are also bringing together Windows and Agent 365 so agents can work within secure boundaries on-device, including MXC a local sandbox for agent execution. Windows becomes your secure agent box! • All this comes to life on a new generation of devices, like Surface Laptop Ultra, powered by NVIDIA RTX Spark. Can’t wait to see what you build with all this.October 7, 2026

## From Gates' factory to your desk?

The narrative is a striking line from the head of a company that sells more software than almost anyone.

But read Microsoft's own engineering documentation for the same launch, and the infinite factory starts to look rather finite: it runs best on a $5,899 laptop, it still reaches into the cloud, and the businesses Microsoft most needs to convince have spent the past year telling researchers they are worried about exactly this kind of thing.

More importantly, the factory metaphor is not new for Nadella: In a 2025 staff memo, he recalled that Bill Gates had envisioned "not just a software company, but a software factory," and argued the AI era demanded a rethink.

At a recent customer gathering, the CEO said Microsoft had progressed from code assistance through agentic coding "to software factory all within one year," and he now wants customers to open software factories of their own, spending more with Microsoft along the way.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The October 7 2026 launch builds on this ambition: a Windows Experience Blog post by Windows and Devices chief Pavan Davuluri describes hybrid intelligence, in which Copilot reads local files with permission, acts across Windows, and hands work to on-device models.

Copilot's Code experience builds an app, dashboard, or workflow from a plain-language description, and on Windows, Microsoft says it can produce native apps from one prompt. Jared Spataro, Microsoft's chief marketing officer for AI at Work, argued that building such tools is becoming "as basic a skill as writing a memo or modeling a budget."

The engine underneath is MAI-Code-1.1 Flash, Microsoft's in-house 137-billion-parameter coding model, which Nadella's post said is now optimized to run on a PC. There is a catch, however: despite Microsoft painting it as a situation where consumers are finding their AI needs "outpacing what their cloud budgets can support."

Microsoft's own engineers are more grounded about what the process entails, saying GitHub Copilot's automatic mode decides task by task whether work runs locally or in the cloud, and one diagram caption is blunt: "local inference does not make the session offline."

That routing doesn't ship until the end of October 2026; the hybrid Copilot features reach Copilot+ PCs over the coming months, and Code is rolling out first through Microsoft's Frontier early-access program. This is interesting, but somewhat predictable, because Nadella's approach, as stated, would cannibalize Microsoft's token-based business model.

An approach that routes harder tasks back to the Azure cloud makes far more sense by conserving compute where possible while still putting Microsoft's cloud compute at the center of things.

The hardware is another factor that one might be overlooking here: according to the Command Line post, the on-device version of MAI-Code-1.1 Flash is quantized down to 53GB, roughly an 80% reduction from the cloud model, and peaked at 75.5GB of memory at full context on Microsoft's test machine, a Surface Laptop Ultra built on Nvidia's RTX Spark.

That matters because eight Surface Laptop Ultra configurations are in play; only one has more than 64GB of memory, per TweakTown: the 128GB model at $5,899, which costs $3300 more than the base model and isn't available to purchase yet, meaning that potential users can't really test out how well it does compared to cloud-based solutions at a time when all performance-related figures come from Microsoft.

## The death of modern enterprise software? Not yet

Despite the hardware limitations in play, it might indicate a death sentence in the making for most basic enterprise-level software solutions, even as more ambitious ports have already been in play: Developer Brandon Thomas, for one, has just released seven open source Adobe Creative Cloud alternatives that he says he built with Anthropic's Claude Opus 5.5, declaring that "software is over."

His own roadmap, however, puts the Photoshop stand-in at roughly a quarter to a third of what a professional needs for daily work. Building software has become cheap. Building software someone can depend on has not.

The bigger issue will be enterprise IT, which will, I suspect, keep the gates closed for now; enterprises don't just buy features; they buy someone to call when it breaks, a patch schedule, an audit trail, and a vendor that carries liability.

Getting an open-source or AI-assisted app someone designed with zero liability in tow that could break things, create security risks, and may not come with future software updates that resolve either issue.

The survey data points the same way: a June 2026 Retool study of 307 CTOs, CIOs, and CISOs found 93% concerned about vibe-coded tools reaching production, though Retool sells an internal-tools platform pitched as the governed alternative.

A Harris Poll survey for Dataiku of 600 CIOs found 81% worried that citizen-built AI could expose sensitive data, and over half had already discovered unsanctioned AI in their organizations.

Gartner, meanwhile, predicts that over 40% of agentic AI projects will be scrapped by the end of 2027, with analyst Anushree Verma describing many as "mostly driven by hype and are often misapplied."

Microsoft's own launch materials quietly concede the same, even taking measures to ensure that agents do not run rogue while building software or solutions on-device.

The Command Line post admits Copilot's built-in file tools are policy-checked inside the app rather than isolated by the operating system, and GitHub requires Business and Enterprise administrators to enable a policy before staff can use MAI-Code-1.1 Flash at all, while Microsoft Execution Containers, which are now generally available, allow IT to define what agents can read, modify, or execute.

The real test for Nadella's factory isn't individuals with a $5,899 laptop and a tolerance for alpha software, but businesses willing to take the risk and trust Microsoft's safeguards. Until then, one could assume the AI factory narrative will continue to run well below its advertised potential.
