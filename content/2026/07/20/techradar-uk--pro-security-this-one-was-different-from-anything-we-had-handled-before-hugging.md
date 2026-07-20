---
title: '''This one was different from anything we had handled before'': Hugging Face
  confirms it was hit by cyberattack powered by an AI agent'
source_url: https://www.techradar.com/pro/security/this-one-was-different-from-anything-we-had-handled-before-hugging-face-confirms-it-was-hit-by-cyberattack-powered-by-an-ai-agent
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-20T18:13:35Z'
published: '2026-07-20T00:00:00Z'
description: There's a new twist to the old code injection attack
image: https://cdn.mos.cms.futurecdn.net/6t9Lsf3QWte55CdyiDs97L-2560-80.jpg
---

![A robot's hand typing on a laptop keyboard](https://cdn.mos.cms.futurecdn.net/6t9Lsf3QWte55CdyiDs97L.jpg) 

- **Hugging Face discloses cyberattack where malicious code hidden in a dataset exploited flaws in its systems, enabling privilege escalation and credential theft**
- **The incident was unique in being orchestrated end‑to‑end by an autonomous AI agent, which launched thousands of short‑lived sandboxes and migrated C2 infrastructure across public services**
- **No customer data or public models were tampered with, but the attack highlights the emerging “agentic attacker” scenario long predicted by the industry**

Hugging Face, one of the biggest platforms for artificial intelligence (AI) and machine learning (ML), disclosed recently suffering a cyberattack supercharged by an AI agent.

“This one was different from anything we had handled before in one important way: it was driven, end to end, by an autonomous AI agent system - and we detected and dissected it largely with AI of our own,” Hugging Face explained in its announcement, noting that the attackers hid malicious code inside a dataset, which they then uploaded to the platform.

When Hugging Face’s automated systems processed that dataset, they exploited two software flaws which allowed the attackers’ code to run on one of the company’s servers.

## Orchestrated by an autonomous AI agent

This twist to the classic code injection attack allowed the attackers to expand their privileges and gain more control over the system, steal authentication credentials to access Hugging Face’s cloud infrastructure, and pivot to other internal systems.

But carrying the attack out mostly with an AI agent is what made this incident unique, Hugging Face explained.

Instead of a human threat actor typing commands, Hugging Face believes the attack was orchestrated by an AI-powered autonomous agent which, entirely on its own, decided which systems to probe, which vulnerabilities to exploit, which credentials to steal, and how to move laterally throughout the compromised infrastructure.

“The campaign was run by an autonomous agent framework (appearing to be built on an agentic security-research harness - used LLM still not known) executing many thousands of individual actions across a swarm of short-lived sandboxes, with self-migrating command-and-control staged on public services,” Hugging Face explained. “This matches the "agentic attacker" scenario the industry has been forecasting.”

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

In other words, the agent kept launching thousands of temporary computing environments, making it extremely hard to stop the attack (since there isn’t a single machine to block). At the same time, the infrastructure controlling the malware kept moving, likely by using legitimate public cloud or online services. Therefore, when the defenders blocked one control server, the attacks would simply come from another.

Currently there is no evidence of tampering with customer data, public user-facing models, or Spaces.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
