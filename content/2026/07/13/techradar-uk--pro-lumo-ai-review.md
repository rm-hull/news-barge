---
title: Lumo AI review
source_url: https://www.techradar.com/pro/lumo-ai-review
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-13T11:27:02Z'
published: '2026-07-13T00:00:00Z'
description: Privacy-first AI that keeps your secrets
image: https://cdn.mos.cms.futurecdn.net/x76vSjSQvt4QQ6v5wvUPAZ-1376-80.jpg
---

### TechRadar Verdict

Lumo delivers on its core promise: AI chat that not even Proton can read. Raw capability still trails frontier models, but for users handling sensitive work, that privacy guarantee is worth the trade-off.

#### Pros

- +Zero-access encryption 
- +No training on your data 
- +Ghost Mode for private sessions 

#### Cons

- -Weaker than frontier AI rivals 
- -Tight limits on free tier 
- -No image upload support 

Why you can trust TechRadar

Most AI assistants are built on a familiar arrangement: you get useful tools, the company gets your data. Lumo, launched by Swiss privacy company Proton in July 2025, refuses that deal entirely. Every conversation is protected by zero-access encryption, no logs are kept server-side, and your chats are never used to train the underlying models.

Lumo runs on a set of open-source large language models, including Mistral Small 3, OLMO 2 32B, and OpenHands 32B, with a routing layer that sends each query to the most appropriate model for the task. The client-side code is open source on GitHub and open to independent review. TIME named Lumo a Best Inventions 2025 special mention, recognizing the broader privacy architecture rather than raw AI performance.

TechRadar Pro has been reviewing business software since 2012. For more of our AI coverage, you can explore our AI tool roundup for 2026.

## What is Lumo?

Lumo is an AI chat assistant from Proton AG, the Swiss company behind Proton Mail and Proton VPN. It handles everyday tasks: drafting text, summarizing documents, answering questions, writing and debugging code, and translating between languages. Unlike most mainstream AI tools, Lumo is designed so that neither Proton nor any third party can access your conversation history.

The platform targets individuals and teams who work with sensitive information and cannot pass it to Big Tech services. Lawyers reviewing contracts, journalists protecting sources, healthcare workers discussing sensitive cases, and privacy-conscious professionals who object to their inputs being fed into model training pipelines are all natural fits. Proton launched Lumo for Business in October 2025 to serve team deployments with admin controls and multi-user management.

A Lumo API is in development according to Proton's spring 2026 product roadmap, which would let third-party platforms embed private AI chat into their own workflows. For now, Lumo is available on the web at lumo.proton.me, and through iOS and Android apps.

## Lumo: At a glance

| 
 | 
 | 
| Underlying model(s) | Routes across Mistral Small 3, OLMO 2 32B, OpenHands 32B, and Mistral Nemo based on task type | 
| Best for | Privacy-conscious users, professionals with sensitive workflows, existing Proton subscribers | 
| Distinguishing functions | Zero-access encryption, Ghost Mode, no-log policy, privacy-respecting web search | 
| UI features | Clean chat interface with dark mode (v1.2+), available on web, iOS, and Android | 
| Subscription costs | Free (limited prompts); Lumo Plus at $12.99/month or $119.88/year ($9.99/month effective) | 
| API pricing | API is in development; no public pricing structure published as of mid-2026 | 

### Buy it if…

- **You regularly handle confidential information.** Zero-access encryption means even Proton cannot read your saved chats, which matters enormously for legal, healthcare, or journalistic work that no mainstream rival can match.
- **You're already a Proton subscriber.** Proton Unlimited members get free access to Lumo's base tier at no additional cost, making it a natural addition to an existing encrypted workflow.
- **Your business needs GDPR-compliant AI.** Lumo is hosted on Proton's Swiss servers, subject to European data protection law, a real advantage for teams with regulatory obligations.

### Don't buy it if…

- **You need frontier-level AI output.** Lumo's open-source models are capable for everyday tasks, but they fall noticeably short of GPT-4o or Claude on complex reasoning and nuanced long-form writing.
- **Image analysis is part of your work.** As of mid-2026, Lumo does not support image uploads. If visual understanding matters to your workflow, you'll need a different tool.
- **You're a light user unwilling to pay.** The free tier's prompt limits create real friction for anything beyond occasional queries, and Lumo Plus is harder to justify if privacy isn't a top concern.

## My time with Lumo

You don't need an account to get started, just open a chat as a guest at lumo.proton.me and start typing immediately. There's a single text input, a web search toggle, and a Ghost Mode button for sessions you want to vanish when you close the window. I found the onboarding frictionless by any standard.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

For routine tasks like summarizing a PDF, drafting a short email, or explaining a technical concept, Lumo performed competently. Response times were reasonable throughout. Where I noticed the ceiling was in longer, more structured outputs: the model occasionally lost the thread in extended conversations, and answers on analytical questions felt thinner than comparable responses from Claude or ChatGPT Plus on the same prompts.

Ghost Mode is useful in practice and cleanly implemented. One click opens a session that leaves no trace on any server when you close it. That's a meaningful practical feature for sensitive queries, and I haven't seen any mainstream competitor offer it this simply.

## Lumo: Features

Lumo covers the standard AI assistant toolkit: document analysis, code writing and debugging, text translation, email drafting, brainstorming, and general Q&A. The routing system automatically directs coding queries to OpenHands 32B, general conversation to Mistral models, and deeper reasoning tasks to OLMO 2. You don't choose the model manually; Proton's routing logic decides what handles each query.

The privacy architecture is the main event. Zero-access encryption means saved chats are only decryptable on your own device with your password, and no server-side logs are kept. Your inputs are never used to train the underlying models, and the optional web search feature routes through privacy-respecting search engines rather than ad-supported services.

Lumo 1.1, released August 2025, upgraded the model stack and delivered meaningful speed improvements. Version 1.2 in October 2025 added dark mode, bug fixes, and basic chat personalization. Lumo for Business followed that same month at $11.99 per user per month (annual billing), adding team admin controls, usage management, and data handling aligned with GDPR, HIPAA, and CCPA.

The feature gaps are real. There's no image input, no voice mode, no plugin marketplace, and no memory system for personalized responses across sessions. For privacy-focused everyday use those absences are manageable, but power users comparing Lumo to ChatGPT's tool ecosystem or Claude's extended context handling will notice the difference.

## Lumo: User experience

The interface is minimal, fast, and easy to navigate. A new chat takes one click, history is searchable when signed in, and the settings panel is straightforward. Dark mode arrived in v1.2, and the mobile apps on iOS and Android closely mirror the web experience with no major feature gaps between platforms.

Customization options are sparse by design: no system prompt settings, no pinned model preferences, no memory configuration. The routing logic is entirely automated, and you largely have to trust Proton's judgment on which model handles what. Users who want fine-grained control will find that frustrating; those who just want to start typing will appreciate how quickly they can get going.

## Lumo: Customer support

Proton covers Lumo support through its help center at proton.me/support/lumo, which includes getting started guides, feature documentation, and troubleshooting articles. A community forum on Proton's user voice platform lets you submit and vote on feature requests. Account-based support tickets can be filed through the dashboard.

There's no live chat or phone support at any tier, which may cause issues for business users dealing with time-sensitive problems. Lumo for Business likely offers more direct support access, but Proton hasn't published detailed SLAs for that plan. For most users, the self-serve documentation is clear enough, but enterprise buyers should confirm escalation options before committing.

 ![Lumo AI by ProtonVPN](https://cdn.mos.cms.futurecdn.net/gLyVDNf4hjYZZQbbEoWTwE.png) 


## Lumo: Pricing

- **Free tier:** Guest access (no account required) with a limited number of prompts per session. A free Proton account unlocks encrypted chat history and more daily messages.
- **Lumo Plus:**$12.99/month, or $119.88/year ($9.99/month effective). Includes unlimited chats, document uploads, history search, priority response times, and access to all available models.
- **Lumo for Business:**$11.99 per user per month, billed annually. Adds team admin controls and compliance-ready data handling for GDPR, HIPAA, and CCPA.

The free tier is functional for sporadic use but constrained enough that the weekly prompt limit becomes friction quickly. At $12.99/month, Lumo Plus sits below ChatGPT Plus and Claude Pro (both $20/month), and the value calculation depends on how much the privacy guarantee matters to you. If you're primarily after output quality and don't mind where your data goes, there are more capable options at similar price points.

Proton Unlimited subscribers ($14.99/month or $9.99/month on annual billing) get free access to the base Lumo tier as part of their existing plan. Lumo is also bundled into the Proton Workspace Premium business plan alongside encrypted email, VPN, and cloud storage.

## Lumo alternatives you should consider

- **ChatGPT Plus ($20/month):** OpenAI's platform offers stronger reasoning, image analysis, voice mode, and a plugin ecosystem. The privacy trade-off is significant, but capability-wise it remains the field benchmark.
- **DuckAI (free):** Duck.ai routes queries through multiple AI models via privacy-respecting proxies and requires no account. Encryption depth is less thorough than Lumo's zero-access approach, but it's a capable free alternative for casual use.
- **Claude Pro ($20/month):** Anthropic's Claude handles long documents and nuanced writing particularly well. It offers no comparable encryption architecture, but output quality on complex tasks is a step above Lumo.

## How I tested Lumo

- Ran Lumo through document summarization, email drafting, code debugging, and general Q&A across multiple sessions to assess response quality and consistency.
- Tested Ghost Mode, web search with and without the toggle enabled, document uploads, and the iOS mobile app across both guest and signed-in access.
- Cross-referenced plans against Proton's official support documentation, product announcements, and other company material.

My testing spanned the web app and iOS client over several days. I compared output quality against Claude and ChatGPT Plus on identical prompts to gauge where Lumo sits in the current AI field. Privacy claims were assessed against publicly available documentation, open-source client code, and independent technical analysis.

![Ritoban Mukherjee](https://cdn.mos.cms.futurecdn.net/cD9joj4H54xYmooW8re3vU.png)

Ritoban Mukherjee is a tech and innovations journalist from West Bengal, India. These days, most of his work revolves around B2B software, such as AI website builders, VoIP platforms, and CRMs, among other things. He has also been published on Tom's Guide, Creative Bloq, IT Pro, Gizmodo, Quartz, and Mental Floss.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
