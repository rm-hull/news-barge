---
title: Express AI review
source_url: https://www.techradar.com/pro/express-ai-review
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-13T11:26:34Z'
published: '2026-07-13T00:00:00Z'
description: AI chat with a genuine privacy promise
image: https://cdn.mos.cms.futurecdn.net/vTJ8n5zZZa3EycskbLUuAZ-1376-80.jpg
---

### TechRadar Verdict

Express AI is one of the few AI platforms that backs its privacy claims with an independent audit. It won't replace a standalone AI subscription for power users, but privacy-conscious professionals who already use ExpressVPN will find genuine value here.

#### Pros

- +Zero-access architecture 
- +Five models in one 
- +Audited by Cure53 

#### Cons

- -Pro subscription required 
- -No API access 
- -Credit limits may frustrate power users 

Why you can trust TechRadar

Express AI, launched on March 31, 2026, is ExpressVPN's attempt to answer a question many AI users haven't thought to ask: who can read your chats? The platform offers access to five AI models inside a confidential computing environment, where prompts and outputs are cryptographically isolated from everyone, including ExpressVPN itself. That's a bold claim in a category where privacy policies tend to be long on language and short on enforcement.

The platform comes bundled with ExpressVPN's Pro plan at no additional cost, positioning it alongside the company's password manager, secure mail, and identity protection tools. I've been covering AI platforms and business software for TechRadar Pro for years, including our 2026 buying guide for vibe coders and our guides on OpenClaw and Moltbook.

For this review, I spent time using Express AI across a range of everyday tasks: drafting, summarising documents, and reasoning through technical problems, to see how it holds up against better-known AI platforms.

## What is Express AI?

Express AI is a multi-model AI chat platform built by ExpressVPN and accessible at app.expressai.com. At launch, it offers access to five general-purpose AI models, each selected for a different task type. What separates it from platforms like ChatGPT or Claude isn't the model lineup, but the underlying architecture: every interaction runs inside a confidential computing environment where encryption keys are generated inside the hardware itself, mathematically isolating conversations from cloud providers, model operators, and ExpressVPN.

The platform targets professionals and individuals who routinely share sensitive information in their AI chats, such as financial questions, work documents, and personal communications, and want guarantees that their data won't be retained or used to train future models. It's particularly well-suited to users already in the ExpressVPN ecosystem, since access is tied to the Pro subscription.

Privacy claims in the AI space are easy to make and hard to verify, which is why ExpressVPN commissioned an independent audit from Cure53, a German cybersecurity firm known for rigorous assessments. The pre-launch review, conducted in February and March 2026, covered penetration testing, source code inspection, and analysis of the platform's cryptography and key management. Cure53 confirmed that Express AI processes user interactions within confidential computing enclaves and found no unresolved vulnerabilities at launch.

## Express AI: At a glance

| 
 | 
 | 
| Underlying model(s) | Five open-weight models: GPT OSS 120B, DeepSeek R1 Distill 32B, Qwen2.5-VL 32B, Qwen3.5 35B-A3B, and Nemotron 12B | 
| Best for | Privacy-conscious professionals, sensitive document analysis, multi-model comparison | 
| Distinguishing functions | Confidential computing, Ghost Mode, encrypted vault, side-by-side model comparison, zero data retention | 
| UI features | Clean chat interface with per-model selection, credit tracker, file upload support | 
| Subscription costs | Included with ExpressVPN Pro; no standalone free plan | 
| API pricing | No public API access available at launch | 

### Buy it if…

- **You share sensitive information with AI tools.** If your prompts routinely include personal, financial, or professional details, Express AI's zero-access architecture offers a layer of protection that mainstream platforms don't.
- **You want multiple models without multiple subscriptions.** The platform bundles five models covering everyday writing, document analysis, and coding in one interface, which reduces the cost and friction of juggling several accounts.

### Don't buy it if…

- **You're not already an ExpressVPN subscriber.** Access requires a Pro plan, so you'd be paying for a full VPN suite alongside the AI platform. That's poor value if you only want an AI chatbot.
- **You need API access or developer-level control.** Express AI has no public API at launch, which makes it a non-starter for developers building on top of AI models.

## My time with Express AI

The interface is spare and deliberately uncomplicated. You select a model, type your prompt, and get a response. There's no sidebar full of tools or settings buried three menus deep. I found the model-switching to be the most useful feature in practice: running the same prompt through DeepSeek R1 Distill 32B for a reasoning-heavy task and then Qwen2.5-VL 32B for document analysis took seconds rather than the tab-switching juggle that typically comes with using multiple platforms.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Ghost Mode worked as described: conversations disappeared after the session ended with no residual trace in the history panel. The encrypted vault stores past conversations behind a user-set password, which means chat history isn't accessible server-side, though a forgotten password loses the history permanently. That's a reasonable trade-off for the privacy guarantee, but it's something to keep in mind for anyone who relies on conversation history for workflow continuity.

One honest caveat: I couldn't independently verify the confidential computing claims beyond what Cure53 has stated in its public report. I'm taking the audit at face value, just as most users will. The 500 daily credits at one credit per prompt felt adequate for my testing but could frustrate users running long, iterative research sessions.

## Express AI: Features

Express AI launches with five open-weight models rather than building proprietary ones from scratch. GPT OSS 120B handles everyday writing and reasoning; DeepSeek R1 Distill 32B is the pick for multi-step logic and research analysis; Qwen2.5-VL 32B reads and extracts data from images and documents; Qwen3.5 35B-A3B targets coding and complex prompts; and Nemotron 12B from NVIDIA handles technical and math-heavy workloads. In practice, having these in one interface means you can match the model to the task without maintaining separate accounts or API keys.

The side-by-side comparison tool is a standout. You can run the same prompt across multiple models simultaneously to compare outputs, which is especially useful when deciding which model to lean on for a recurring task type. Few standalone AI platforms offer this natively.

Ghost Mode and the encrypted vault address the two main categories of privacy risk. Ghost Mode auto-deletes conversations after each session, leaving no stored record at all. The vault stores history under user-controlled encryption: only the password set by the user can decrypt it, and neither ExpressVPN nor the model providers can access it. These aren't marketing claims; Cure53's February and March 2026 audit verified both mechanisms before launch.

File uploads are capped at 50 MB per file. The 2 GB of secure storage included with the Pro plan is sufficient for most document analysis tasks. I uploaded PDFs and images without friction, and Qwen2.5-VL 32B handled the analysis accurately in my testing. There's also a transparent credit tracker, which shows remaining daily usage clearly rather than burying it in account settings.

What's missing, at least at launch, is agentic capability. Express AI doesn't support tool use, web browsing, or multi-step autonomous tasks. It's a chat interface, and a deliberate one. For users who want AI agents to run workflows or integrate with external services, they'll need to look elsewhere. The no-API position also limits Express AI's appeal to developers, which may narrow the platform's audience more than ExpressVPN intends.

## Express AI: User experience

The interface prioritises simplicity, which suits the platform's core audience. New users can start a conversation in under a minute. There's no onboarding tutorial or feature demo, but the layout is intuitive enough that most users won't need one. The Ghost Mode toggle and model selector are front and centre, so the two features that define the platform don't require hunting through menus.

In terms of design, it reads closer to a focused productivity tool than a full AI platform. That restraint works in its favour for privacy-conscious users who don't want complexity, but it may feel bare to anyone coming from ChatGPT or Claude's more feature-dense interfaces. ExpressVPN has described Express AI as part of a broader privacy ecosystem, suggesting the product will expand, but the launch version makes no concessions to power users hoping for immediate depth.

## Express AI: Customer support

Express AI inherits ExpressVPN's customer support infrastructure, which includes 24/7 live chat via the main ExpressVPN site. Response times in my experience have been fast, typically under two minutes for live chat. Support agents are familiar with the VPN suite but may have limited depth on Express AI-specific technical queries, given how recently the platform launched.

The support documentation for Express AI is currently thin. The knowledge base covers setup and billing questions, but more detailed guidance on model selection, credit usage, and the encrypted vault is sparse. Given that this is a new product, that's understandable, but users who run into edge cases may find the documentation less helpful than they'd expect.

 ![Express AI user interface](https://cdn.mos.cms.futurecdn.net/qfJWzSC2JPRoFyAzaAhRZG.png) 


## Express AI: Pricing

- **Included with ExpressVPN Pro.** Express AI is available at no additional cost to Pro subscribers, which makes it the most accessible pricing model for existing users.
- **Pro plan starts at $7.49/month** on a 2-year commitment, rising to $8.99/month on a 1-year plan and $19.99/month month-to-month.
- **No standalone or free tier**. There is no way to access Express AI without an active ExpressVPN Pro subscription.

The pricing is simple once you accept that Express AI is a bundled benefit rather than a standalone product. Pro subscribers get 500 daily credits, 2 GB of encrypted storage, and access to all five models alongside ExpressVPN's other features. For users who already pay for a Pro plan, Express AI costs nothing extra.

For users who don't need a VPN, the value proposition is murkier. The Pro plan at $19.99/month is competitive with some standalone AI subscriptions — ChatGPT Plus costs $20/month, for example — but you're paying for a VPN suite first and an AI platform second. ExpressVPN hasn't announced a standalone plan for Express AI, so that decision point will remain for the foreseeable future.

## Express AI: alternatives you should consider

- **ChatGPT (OpenAI):** The most widely used AI platform, with broader model access, API support, and agentic capabilities, but no confidential computing or zero-access architecture.
- **Claude (Anthropic):** A strong alternative for writing and reasoning tasks, with competitive privacy policies, though prompts may be reviewed for safety and model improvement purposes.
- **Lumo (Proton):** A privacy-oriented alternative from the makers of ProtonMail, worth watching as it develops its AI toolset for privacy-focused users.

## How I tested Express AI

- Used Express AI for drafting, summarising, and answering research questions across multiple sessions to assess model quality and response consistency.
- Uploaded PDFs and images to test the Qwen2.5-VL 32B model's ability to extract data and answer questions about uploaded content.
- Tested Ghost Mode, the encrypted vault setup, and credit tracking to confirm they behaved as described in the official documentation and Cure53 audit summary.

For this review, I used Express AI as a day-to-day tool across a three-day period, testing each of the five models for their stated use cases and comparing the experience against mainstream AI platforms I use regularly. I reviewed ExpressVPN's official product documentation, the public summary of the Cure53 audit, and third-party coverage from the March 2026 launch to verify the platform's privacy claims and pricing.

![Ritoban Mukherjee](https://cdn.mos.cms.futurecdn.net/cD9joj4H54xYmooW8re3vU.png)

Ritoban Mukherjee is a tech and innovations journalist from West Bengal, India. These days, most of his work revolves around B2B software, such as AI website builders, VoIP platforms, and CRMs, among other things. He has also been published on Tom's Guide, Creative Bloq, IT Pro, Gizmodo, Quartz, and Mental Floss.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
