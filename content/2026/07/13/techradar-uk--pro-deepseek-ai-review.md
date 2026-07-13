---
title: DeepSeek AI review
source_url: https://www.techradar.com/pro/deepseek-ai-review
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-13T11:26:17Z'
published: '2026-07-13T00:00:00Z'
description: Powerful AI at rock-bottom prices, with caveats
image: https://cdn.mos.cms.futurecdn.net/UxJbax8rRj575zbGmzK4AP-1376-80.jpg
---

### TechRadar Verdict

DeepSeek is hard to ignore on price and performance alone. Its V4 models punch well above their cost bracket, and the free chat app is capable enough to hold its own against paid competitors. But for any business handling sensitive data, the privacy and security picture is murky enough to give serious pause.

#### Pros

- +Free chat, no query limits 
- +Extremely cheap API pricing 
- +Open-weight models available 

#### Cons

- -Data stored on Chinese servers 
- -Known security vulnerabilities 
- -Content censorship on sensitive topics 

Why you can trust TechRadar

DeepSeek landed like a thunderclap in January 2025, when its R1 reasoning model briefly dethroned ChatGPT as the most downloaded free app on the iOS App Store in the United States. Built by a Hangzhou-based AI lab backed by Chinese hedge fund High-Flyer, it claimed to match frontier AI performance at a fraction of the development cost. That claim sent Nvidia's stock tumbling 17% in a single session and sparked a global conversation about who was actually winning the AI race.

Since then, DeepSeek has grown to roughly 97 million monthly active users and released multiple model generations, most recently the V4 family in April 2026. Its API pricing stands out: the V4 Flash model starts at $0.14 per million input tokens, cheaper than most "lite" tier models from OpenAI and Google yet competitive on coding, math, and reasoning benchmarks. The open-weight licensing under MIT also means teams can self-host the models and sidestep per-token costs entirely at scale.

We've been reviewing B2B software at TechRadar Pro since 2012, with AI platforms among our most active coverage areas in recent years. Our AI tools roundup, vibe coding guide for 2026, and explainers on OpenClaw and Moltbook give you a sense of the tools we track. DeepSeek is one of the more polarizing platforms we've tested: impressive in many ways, but not without significant red flags.

## What is DeepSeek?

DeepSeek is an AI chat platform and API service developed by Hangzhou DeepSeek Artificial Intelligence Co., Ltd., a Chinese company founded in 2023 and funded by the quant hedge fund High-Flyer. It offers a free web and mobile chat interface at chat.deepseek.com alongside a paid developer API, both powered by the same underlying model family.

The platform runs on DeepSeek's own large language models, specifically V4 Flash and V4 Pro, both using a Mixture-of-Experts (MoE) architecture. Only a subset of each model's parameters activates per token, which keeps inference costs low without shrinking the model's overall knowledge base.

V4 Pro has 1.6 trillion total parameters but only 49 billion active at inference. V4 Flash runs 284 billion total with 13 billion active, making it significantly faster and cheaper without sacrificing much on everyday tasks.

Developers, researchers, and cost-conscious businesses are the natural audience. The free chat tier suits individuals and small teams exploring the tool, while the API's aggressive pricing makes it attractive for anyone building AI-powered applications at scale.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## DeepSeek: At a glance

| 
 | 
 | 
| Underlying model(s) | DeepSeek V4 Flash (284B total / 13B active params) and V4 Pro (1.6T total / 49B active params), both MoE-based | 
| Best for | Coding assistance, mathematical reasoning, document analysis, budget API use | 
| Distinguishing functions | 1M token context, thinking/non-thinking modes, prompt caching, open weights (MIT) | 
| UI features | Web chat and iOS/Android apps with web search toggle, file upload (PDF, DOCX, TXT), Expert Mode and Instant Mode | 
| Subscription costs | Free (chat app, unlimited queries); no paid chat subscription tiers | 
| API pricing | Pay-per-token; new accounts receive 5M free tokens valid 30 days; V4 Flash at $0.14 / $0.28 per 1M tokens (input/output); V4 Pro at $1.74 / $3.48 standard, with promotional discounts available | 

### Buy it if…

- **You need a cheap, capable coding or reasoning API.** V4 Flash at $0.14 per million input tokens is among the most affordable frontier-adjacent APIs available, and its benchmark results on coding and math hold up well against more expensive competitors.
- **You want open weights for self-hosted deployment.** Both V4 models are released under MIT license on Hugging Face, giving teams the option to run the model on their own infrastructure and eliminate per-token costs entirely for high-volume workloads.
- **You're doing non-sensitive exploratory work.** For individual researchers, students, or developers prototyping non-confidential projects, the free chat app offers web search, file uploads, and a 1M token context window at zero cost.

### Don't buy it if…

- **Your work involves confidential or regulated data.** All user data is stored on servers in mainland China, subject to Chinese law, which permits government access without user consent. Multiple governments have banned DeepSeek from official devices for exactly this reason.
- **You need consistent responses on sensitive topics.** DeepSeek avoids certain politically sensitive subjects, particularly around Chinese domestic affairs. That content filtering can produce evasive or incomplete outputs on topics that other platforms handle straightforwardly.
- **You're in a GDPR-regulated region.** Italy's data protection authority blocked DeepSeek outright in January 2025 after the company provided what regulators called a "completely insufficient" response to data practice inquiries.

## My time with DeepSeek

I tested DeepSeek's chat app and API across a range of tasks: code generation, document summarization, long-form reasoning, and general Q&A. On raw capability, the V4 models impressed me. Code outputs were clean and well-structured, long document summaries were accurate, and the one-million-token context window handled full-length PDF ingestion without complaint.

The thinking mode, accessible via Expert Mode in the chat UI, added visible chain-of-thought reasoning that proved useful for multi-step problems rather than theatrical.

What gave me pause was everything outside the model itself. Certain politically sensitive prompts returned conspicuously vague or deflective answers — the kind of behavior that wouldn't be acceptable in a professional context where consistent and complete information matters. I also found that the chat interface lacks the memory and personalization features you'd find in ChatGPT or Claude.

Value for money on the API side is difficult to argue with. A production app with well-structured prompts benefits substantially from the caching discount: cached input tokens cost just $0.014 per million for V4 Flash, a 90% reduction. For high-volume, low-sensitivity workloads, that arithmetic is compelling.

## DeepSeek: Features

DeepSeek's core chat feature set covers the bases you'd expect: text generation, code writing and debugging, document summarization, mathematical reasoning, and web search. The web search integration is a manual toggle rather than always-on, which keeps responses faster by default but requires you to switch it on when real-time information matters. File uploads support PDF, DOCX, and TXT formats, with the model able to summarize and answer questions based on the uploaded content.

The standout capability is the 1M token context window introduced with V4, up from 128K in the previous generation. That's a meaningful jump for anyone analyzing long contracts, codebases, or research documents in a single session. Most competitors at comparable price points max out at 128K to 200K tokens.

V4 Flash covers both thinking and non-thinking modes, so you don't need to switch between separate models depending on task complexity. Non-thinking handles fast general responses; thinking adds structured multi-step reasoning for harder problems. That flexibility matters more than it sounds when you're toggling between casual tasks and complex analysis in the same workflow.

Where DeepSeek falls short is multimodal support. The platform does not currently support image generation or image understanding in the web app, putting it behind ChatGPT, Claude, and Gemini on that front. Agentic capabilities are available in the V4 Preview but remain early-stage compared to dedicated agentic platforms.

## DeepSeek: User experience

The chat interface at chat.deepseek.com is straightforward and fast to get started with. Signing up requires only an email address from a global provider like Gmail or Yahoo, and the default experience drops you straight into a conversation window. The distinction between Expert Mode (thinking-enabled, slower) and Instant Mode (faster, non-thinking) is surfaced clearly at the top of the interface, and mobile apps on iOS and Android mirror the web experience with file upload and web search included.

The learning curve is shallow for casual use. Switching between thinking and non-thinking modes takes one click, and the file upload workflow is drag-and-drop simple.

The API experience is less forgiving for first-time integrators. Unlike the chat app, the API is stateless, meaning every call must include the full conversation history in the messages array. DeepSeek's documentation covers this clearly, but it catches developers accustomed to managed conversation state elsewhere off guard.

## DeepSeek: Customer support

Support options for free chat users are limited to a Discord community server and an email channel for API service inquiries ([api-service@deepseek.com](mailto:api-service@deepseek.com)). Community responses on Discord can be prompt, but they depend on other users rather than official staff. There is no live chat or phone support.

API customers have slightly more recourse through direct email support, though response times vary. The official documentation at api-docs.deepseek.com is thorough and well-organized, covering model details, pricing, rate limits, and code examples in both Python and curl. For developers comfortable with self-service documentation, it's adequate.

 ![DeepSeek V3](https://cdn.mos.cms.futurecdn.net/fSXaMc6TyjLbyZqxCqFvJF.png) 


## DeepSeek: Pricing

- **Chat app is free with no query limits.** The web and mobile apps give you unlimited access to V4 Flash and V4 Pro at no cost, including web search, file uploads, and the full context window.
- **New API accounts receive 5M free tokens**, valid for 30 days, giving developers a zero-cost window to prototype and test.
- **API billing is pay-as-you-go.** V4 Flash costs $0.14 per million input tokens and $0.28 per million output tokens. V4 Pro runs $1.74 and $3.48 respectively at standard rates, with promotional discounts periodically dropping those to $0.435 and $0.87. Cached input tokens cost one-tenth of the standard input rate on both models.

The free chat tier is generous by any measure. Unlimited queries with a 1M context window puts it ahead of most free-tier competitors in raw access terms, and there's no paid chat subscription to worry about. Power users who need more control either stick with the free app or pay per token via the API.

On the API side, DeepSeek makes a strong case for developers managing costs at scale. Off-peak pricing discounts of up to 75% are available during 16:30–00:30 UTC, giving teams with flexible scheduling another cost lever. For production apps with well-structured prompts sharing a common system context, effective input costs can drop well below $0.02 per million tokens with caching applied.

## DeepSeek: alternatives you should consider

- **ChatGPT (OpenAI):** The most capable all-around AI platform, with image understanding, voice, and memory. API pricing is higher, but US-based data residency and enterprise data agreements make it a safer choice for sensitive business workloads.
- **Claude (Anthropic):** Particularly strong for long-form writing and document analysis, with comparable context windows and clearer data handling policies. Claude Pro starts at $20/month for individual users.
- **Gemini (Google):** Tightly integrated with Google Workspace and built for multimodal work across text, image, and video. Gemini 2.5 Flash offers competitive API pricing with no Chinese data jurisdiction concerns.

## How I tested DeepSeek

- Used the free web app for code generation, document summarization, mathematical reasoning, multi-turn Q&A, and file analysis, covering both Instant Mode and Expert Mode across each task type.
- Ran API calls across varying prompt sizes to verify context window behavior, caching discounts, and response consistency, following DeepSeek's own temperature guidance for different task types.
- Cross-referenced DeepSeek's official privacy policy, third-party security research from NowSecure and SecurityScorecard, and regulatory actions from Italy, Australia, South Korea, and US government bodies to build a complete picture of the data risk profile.

Beyond hands-on testing, I reviewed DeepSeek's official API documentation, the V4 technical report published on Hugging Face, and benchmark data from the April 2026 release. Pricing figures were sourced directly from the official DeepSeek API documentation and corroborated against third-party tracking services.

![Ritoban Mukherjee](https://cdn.mos.cms.futurecdn.net/cD9joj4H54xYmooW8re3vU.png)

Ritoban Mukherjee is a tech and innovations journalist from West Bengal, India. These days, most of his work revolves around B2B software, such as AI website builders, VoIP platforms, and CRMs, among other things. He has also been published on Tom's Guide, Creative Bloq, IT Pro, Gizmodo, Quartz, and Mental Floss.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
