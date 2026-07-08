---
title: Experts warn of the first documented case of 'agentic ransomware
source_url: https://www.techradar.com/pro/security/experts-warn-of-the-first-documented-case-of-agentic-ransomware-dangerous-jadepuffer-attack-run-entirely-by-an-llm
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-08T21:20:20Z'
published: '2026-07-08T00:00:00Z'
description: An LLM-based ransomware attack has been detected by researchers, and
  is notable for losing the data it encrypted...
image: https://cdn.mos.cms.futurecdn.net/GJ8T4oA8G7TYJwTEhkwJAF-2560-80.jpg
---

![Representational image of a cybercriminal](https://cdn.mos.cms.futurecdn.net/GJ8T4oA8G7TYJwTEhkwJAF.jpg) 

- **The first agentic ransomware attack has been dubbed JADEPUFFER by researchers at Sysdig**
- **Threat exploited a known vulnerability, adapted to obstacles, and targeted an Alibaba Nacos**
- **Unfortunately for victims, paying up means nothing, as JADEPUFFER fails to back up the data**

Has ransomware become self-aware? Sysdig researchers have analyzed an attack on an internet-facing Langflow instance, and discovered what they believe to be the first ransomware infection driven not by a human, but by AI.

As the attack progressed via a vulnerability, it accessed a server, removed data, overcame challenges, and phoned home regularly – all controlled not by a remote operator, but by a large language model (LLM).

Dubbed “JADEPUFFER” the attack seems to point to the direction of travel for extortion-based cybercrime -- if not for the entire sector, then certainly for the cybercrime-as-a-service (CaaS) market. As highlighted in Sysdig’s conclusion: “It’s a marker of where extortion tradecraft is heading.”

## Fully autonomous hack

Using a code-injection attack on a Langflow deployment, Sysdig reported that the attack was fully automated, and after exploiting the vulnerability (CVE-2025-3248) JADEPUFFER sought out credentials for LLM providers, databases cloud platforms, and cryptocurrency wallets.

It also harvested data from the Langflow instance’s Postgres database, and committed various acts of destruction before the intended Alibaba Nacos (Naming and Configuration Service) and connected MySQL database were reached.

At this point, the ransomware demand was issued, with 1,342 Nacos configuration items encrypted and crucial database tables dropped. What is interesting about this is that random encryption was applied, but no backup was made and no key or report was created – so even if the ransom was paid, the data would remain unrecovered.

(Langflow fixed the vulnerability in April 2025, so this attack could have been avoided if the instance had been patched. Ironically, Langflow is also an AI platform, providing low-code solutions to build and deploy chatbots, agents, and advanced workflows using artificial intelligence.)

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## A new phase in cybersecurity

Security researchers have been on the lookout for Agentic Threat Actors (ATAs) for a while now, so the arrival of JADEPUFFER is not completely unexpected. Its arrival essentially means that anyone can create and operate a ransomware (or other cyberthreat) operation, relying on intelligent prompts and low-effort, fully automated testing in the wild, from which the LLM can learn and improve.

If this does indeed represent the dawning of a new age of cybersecurity, it isn’t all bad news. This incident has demonstrated how LLM-based attacks can be detected.

It used historical vulnerabilities, for example, but the most interesting thing about it is that this attempt was pretty verbose. The Sysdig team noticed that when JADEPUFFER was presented with obstacles to its primary aim, it adapted and shared its rationale.

While this narration is common among LLMs, other threats don’t do this, which offers an advantage for detecting LLM-based threats like JADEPUFFER and the variants which will inevitably appear.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Christian Cawley](https://cdn.mos.cms.futurecdn.net/zBDYnjPnB2XPvhKbYX9Kuc.png)

Christian Cawley has extensive experience as a writer and editor in consumer electronics, IT and entertainment media. He has contributed to TechRadar since 2017 and has been published in Computer Weekly, Linux Format, ComputerActive, and other publications.

He currently heads up the team at smart home website Matter Alpha, and writes about retro gaming at Gaming Retro.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
