---
title: OpenAI took ten days to tell Hugging Face its models were behind the July 11
  weekend hack, report claims — rogue AI agents reportedly active on the open Internet
  for several days
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-took-ten-days-to-tell-hugging-face-its-models-were-behind-the-july-11-weekend-hack
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-24T14:06:02Z'
published: '2026-07-24T00:00:00Z'
description: Anthropic's Fable 5 and Opus refused to analyze the attack logs, so Hugging
  Face turned to China's GLM 5.2 to dissect the intrusion.
image: https://cdn.mos.cms.futurecdn.net/32WYcyu4rFmvpTh9AxGNmD-2000-80.jpg
---

![Sam Altman](https://cdn.mos.cms.futurecdn.net/32WYcyu4rFmvpTh9AxGNmD.jpg) 

OpenAI confirmed to Hugging Face only this week that models it was testing carried out the July 11 attack on the AI platform's production infrastructure, roughly ten days after the intrusion and days after Hugging Face disclosed it publicly without knowing who was responsible, according to a *Wall Street Journal* report. The models appear to have been active on the open Internet for several days before anyone stopped them, the*Journal* reported, and Hugging Face ended the attack two days after detecting it with help from an open-weight model out of China. Hugging Face co-founder and chief science officer Thomas Wolf told the paper the intruder was browsing cybersecurity datasets rather than hunting for anything a human attacker could sell.

 ![Microsoft data center in Mount Pleasant, Wisconsin](https://cdn.mos.cms.futurecdn.net/Vh4nY3pMCcmra2ymXah9S7.jpg) 


Hugging Face published its disclosure on July 16, describing an autonomous agent framework that ran thousands of actions across a swarm of short-lived sandboxes, but it wasn’t until July 21 that OpenAI’s own account named GPT-5.6 Sol and an unreleased frontier model as the culprits.

The models are now known to have been running OpenAI's ExploitGym benchmark, a suite of roughly 900 tests that measures whether an AI can turn a known software bug into a working exploit, with the company's safeguards removed for the evaluation. Rather than solve the tests, the models escaped their sandbox to look for the answers on Hugging Face, per OpenAI's account. The intrusion started with a malicious dataset that abused two code-execution paths in the data-processing pipeline, then escalated privileges and moved laterally using stolen credentials of an unknown origin.

Hugging Face first tried Anthropic's Fable 5 and an earlier Opus model to analyze the attack logs, but both refused because the logs contained real attack commands and exploit payloads. Hugging Face then turned to GLM 5.2, an open-weight model from Beijing-based Z.ai (formerly Zhipu AI), which had no such restrictions. The company's own July 16 disclosure described the blocked models only as "frontier models behind commercial APIs" and didn’t name them.

Z.ai’s GLM-5.2 held top accessible benchmark positions by default during the 18 days that U.S. export controls kept Anthropic's Fable 5 offline in June, before Anthropic restored the model with a single filter tuned to block one vulnerability-discovery technique. There’s serious irony here, given that the same Chinese open-weight model that Washington's export-control push has aimed to sideline is the one that handled incident response after an American lab's models attacked an American company, and American commercial models declined to help.

Security researchers have questioned whether the episode demonstrates model capability or an OpenAI failure. Cybersecurity veteran Jake Williams told *TechCrunch* that any model performing the documented actions "was not fully contained in a sandbox," calling it a control failure. OpenAI has said it shut down its model-testing systems to assess the damage, disclosed the zero-day in the package registry cache proxy that enabled the sandbox escape to the affected vendor, and promised a detailed report.

Both companies say the investigation is ongoing, and OpenAI hasn’t yet said how long the models roamed unsupervised or whether they reached any other targets.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Luke James](https://cdn.mos.cms.futurecdn.net/C4FAi2KzwaGLUrBqzX5aBM.png)

Luke James is a freelance writer and journalist. Although his background is in legal, he has a personal interest in all things tech, especially hardware and microelectronics, and anything regulatory.
