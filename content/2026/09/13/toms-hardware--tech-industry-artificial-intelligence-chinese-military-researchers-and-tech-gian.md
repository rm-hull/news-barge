---
title: Chinese military researchers and tech giants caught using Claude — US frontier
  model coded 16 air-defense suppression tools targeting Taiwan, drafted anti-torpedo
  specs, and fed 151 million training queries to Alibaba
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/chinese-military-researchers-and-tech-giants-caught-using-claude-us-frontier-model-coded-16-air-defense-suppression-tools-targeting-taiwan-drafted-anti-torpedo-specs-and-fed-151-million-training-queries-to-alibaba
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-13T13:18:48Z'
published: '2026-09-13T00:00:00Z'
description: Is imitation the sincerest form of flattery?
image: https://cdn.mos.cms.futurecdn.net/vnqdtRupVqWHAik43ZWctH-1920-80.jpg
---

![Micron](https://cdn.mos.cms.futurecdn.net/vnqdtRupVqWHAik43ZWctH.jpg) 

While China claims to have advanced AI models that may well compete against those developed in the U.S., for some reason, hundreds of China-linked agents allegedly used Anthropic for at least five different programs: two military, two surveillance, and one aimed at distilling Claude's capabilities, according to Anthropic's September 2026 threat report.

## Two military programs

One China-based actor used Claude to draft a fire-control specification for an anti-torpedo fire-control system (the core logic that determines when and where an anti-torpedo weapon should engage an incoming threat), test the potential system against U.S. Navy anti-torpedo and anti-submarine systems based on public knowledge about these programs, and prep a 200+ page technical proposal for a potential client. While the actor disguised itself as an OEM in the U.S. defense sector, Anthropic believes that the actor was associated with a Chinese defense manufacturer seeking to develop a system for the People's Liberation Army Navy.

Another China-based defense and military-industrial researcher used Claude to develop about 16 software modules for electronic warfare and suppression of enemy air defenses. The software analyzed radars, SAM sites, command posts, and communications nodes and prioritized targets. At one point, the default scenario contained 12 targets in Taiwan, including Patriot and Tien Kung batteries, air bases, an early-warning radar, and a command bunker. Interestingly, Anthropic claims that account metadata and content caught by its safeguards 'indicated the actor was linked to PRC research institutions, including the PLA Academy of Military Sciences,' though it does not outright say that Claude was used by the PLA.

Given China's considerable AI capabilities — which may still lag behind those of the United States in some areas (more on this later) — it is striking that two Chinese military-related projects relied on Anthropic's Claude. Given the Chinese-language prompts and other account-level evidence identified by Anthropic, plausible deniability hardly seems to have been the primary reason for choosing Claude over domestic alternatives. More likely, Claude was simply better or more convenient for these particular engineering workflows, particularly coding, reasoning, and agentic tasks. There may also have been another advantage: U.S. frontier models are trained on enormous amounts of English-language material and could therefore have particularly extensive knowledge of publicly available information about American military technologies and systems.

Given China's major AI prowess (which may well fall short of American, but still be quite capable), it is interesting to see two Chinese military projects using Anthropic AI. Given Chinese IP addresses and Chinese language prompts detected by Anthropic, plausible deniability is certainly not the main reason for using Claude instead of using domestic tools (more on this later). Apparently, Claude was better or more convenient for these particular engineering workflows (coding => reasoning => agentic) than whatever models the actors could readily access. Furthermore, after all, U.S. frontier models were trained mostly on English-language materials, and they may have way more information about American military capability than Chinese spy channels have ever gotten (we are speculating, of course).

## Significant surveillance activities

Anthropic also disrupted China-linked surveillance operations related to Uyghurs outside of China, perhaps because similar operations are already in place in the Xinjiang Uyghur Autonomous Region. One China government-linked actor used Claude to infiltrate Uyghur armed groups in Syria and surveil Uyghur diaspora activists and media, while posing as an Arabic-speaking 'expert' consultant.

Once the agent had infiltrated the said groups, Claude helped process information collected from more than a hundred WhatsApp groups and dozens of Telegram channels, identify people across platforms, map social networks, and reveal potential recruitment targets considered vulnerable because of financial problems, family separation, or ideological disillusionment with the new Syrian government.

The actor also singled out individuals with relatives remaining in Xinjiang, while Claude helped draft deceptive approaches in local dialects, locate people and organizations, translate conversations in real time, and evaluate the credibility of recruitment messages. The same operation targeted diaspora journalists, particularly Uyghur Post, with coordinated mass-reporting and bot-amplification campaigns.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

## Stealing from Anthropic

Perhaps the most ironic thing about Anthropic's findings is that Chinese entities steal from the company. While reported broadly in 2024 – 2025, it does not stop Chinese entities from using distillation, the main way to 'steal' an AI model's capabilities without obtaining the model itself.

Anthropic says several major Chinese AI developers conducted industrial-scale distillation campaigns designed to extract Claude's reasoning and other capabilities and reproduce them in their own models. The largest one allegedly came from Alibaba, whose operators generated more than 151 million Claude exchanges between May and July 2026. At one point, this approached 3 million requests per day through thousands of fraudulent accounts. Anthropic says the harvested chain-of-thought data helped train Qwen 3.x, particularly for reasoning, coding, agentic software engineering, kernel development, and long-horizon tasks, according to Anthropic.

Alibaba is far from alone, as Anthropic accuses DeepSeek, Xiaomi, Zhipu/Z.ai, and others of similar campaigns. Techniques they have allegedly used span from proxy networks and fraudulent accounts to disguising the secret entity all the way to forwarding their own customers' requests to Claude and purchasing harvested Claude conversations from third parties. DeepSeek alone allegedly generated more than 12.1 million exchanges in 14 days, while Xiaomi generated more than 400,000.

Anthropic defines this activity as distillation: covertly extracting a frontier model's answers and then replicating the knowledge at a fraction of the compute, time, and cost required to develop them in-house.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Anton Shilov](https://cdn.mos.cms.futurecdn.net/uMZ5kNphxA2Ut6whdLaSQV.png) 

Anton Shilov is a contributing writer at Tom’s Hardware. Over the past couple of decades, he has covered everything from CPUs and GPUs to supercomputers and from modern process technologies and latest fab tools to high-tech industry trends.
