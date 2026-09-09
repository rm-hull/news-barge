---
title: FBI, NSA warn Chinese AI companies like DeepSeek and Alibaba are reportedly
  carrying out 'industrial-scale' distillation campaigns to boost their models
source_url: https://www.techradar.com/pro/security/fbi-nsa-warn-chinese-ai-companies-like-deepseek-and-alibaba-are-reportedly-carrying-out-industrial-scale-distillation-campaigns-to-boost-their-models
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-09T19:15:17Z'
published: '2026-09-09T00:00:00Z'
description: Attackers are teaching their models by asking GPT and Claude millions
  of questions
image: https://cdn.mos.cms.futurecdn.net/cWc9CWu3UHCubh8PtKXmVS-1920-80.jpg
---

![ChatGPT vs Gemini comparison](https://cdn.mos.cms.futurecdn.net/cWc9CWu3UHCubh8PtKXmVS.jpg) 

- **CISA, NSA, FBI warn Chinese AI firms of industrial‑scale knowledge distillation**
- **Companies like DeepSeek, Moonshot, Alibaba allegedly extracted billions of tokens from US frontier models**
- **Advisory urges detection of malicious prompts, deceptive responses to distillation, and cross‑provider intelligence sharing**

Chinese AI companies’ core development strategy is to steal proprietary functionalities and capabilities from their US counterparts, law enforcement agencies have warned.

The US Cybersecurity and Infrastructure Security Agency (CISA) has published a new security advisory, drafted jointly with the National Security Agency (NSA) and the Federal Bureau of Investigation (FBI), warning American AI companies about an ongoing “aggressive, malicious, and targeted distillation activities at an industrial scale,” and sharing recommended mitigation steps.

## Knowledge distillation

IBM defines knowledge distillation as a “machine learning technique that aims to transfer the learnings of a large pre-trained model, the ‘teacher model,’ to a smaller ‘student model’.” It is used in deep learning as a form of model compression and knowledge transfer, it added, particularly for massive deep neural networks.

So, knowledge distillation is not illegal or malicious, per se. Its goal is to train a more compact model to mimic a larger, more complex one. In the security advisory, the agencies stress it is “recognized as a legitimate and useful technique in AI research,” but add that China-based AI companies are using it in ill will.

In other words, the agencies claim that instead of spending months and millions developing new capabilities for their models, the Chinese are simply sending huge numbers of carefully designed questions to US models and extracting the answers.

## Which companies are engaged in knowledge distillation?

Apparently, all companies worth anything. DeepSeek, Moonshot AI, Alibaba, MiniMax, StepFun, and Z.AI all allegedly “extracted billions of tokens across millions of exchanges/requests from US frontier AI models, including variants of Claude, GPT, Gemini, and Grok, since at least late 2024.” CISA also stressed that this was likely done with the awareness of the Chinese government. It hasn’t outright said, “with its blessing”, although it could be read between the lines.

The advisory shares a thorough list of all the models that were being trained, as well as all the models being taken advantage of.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

On the Chinese side, they include DeepSeek R1 and V3 models, Moonshot’s Kimi-K2 and Kimi-K3 models, and MiniMax’s M2 model. On the US side, they start with earlier models such as GPT-4, Claude 3.7, and Gemini 2.5 Flash Preview, all the way to Claude Fable 5, GPT-5, and similar.

When done in good faith, knowledge distillation is not illegal. However, the report says the companies routed the requests through multiple accounts, different API access points, multiple cloud providers, third-party AI aggregators, proxy services and “transfer stations”, as well as premium subscriptions shared between developers, all in an attempt to work around defenders trying to disrupt the process.

“This represents systematic extraction of proprietary functionalities and capabilities threatening U.S. technological leadership. Addressing industrial-scale distillation merits a coordinated response across the AI ecosystem, including effective information-sharing, spanning the U.S. Government, private industry, and allied nations,” the agencies concluded.

## What US companies should be doing

To defend their intellectual property (and thus remain ahead of Chinese competing models) US AI companies should implement comprehensive detection and mitigation, the agencies said. That means hunting for anomalous and malicious prompts, accounts, networks, and behaviors. Furthermore, they should monitor subscription-to-usage ratios, immediate maximum usage from new accounts, and enterprise-scale throughput patterns.

The second step is to “deploy targeted response changes”: “Subtly alter responses for suspected malicious distillation attempts to attenuate the payoffs to companies conducting industrial-scale distillation campaigns.” In other words, AI companies should make sure their products lie when they spot they were being distilled for knowledge.

Finally, US AI firms should set up cross-organization intelligence sharing, correlating activity across model providers, cloud platforms, and API aggregators.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
