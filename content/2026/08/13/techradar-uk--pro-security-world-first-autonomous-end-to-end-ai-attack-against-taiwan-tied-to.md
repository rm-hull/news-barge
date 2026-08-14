---
title: World-first autonomous ‘end-to-end’ AI attack against Taiwan tied to Chinese
  hackers — and the scariest part is that it was fully open source
source_url: https://www.techradar.com/pro/security/world-first-autonomous-end-to-end-ai-attack-against-taiwan-tied-to-chinese-hackers-and-the-scariest-part-is-that-it-was-fully-open-source
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-14T02:39:24Z'
published: '2026-08-13T00:00:00Z'
description: Eight AI models assembled a fully autonomous hacking tool
image: https://cdn.mos.cms.futurecdn.net/UQyjwYkZut5eDweL2vKmvb-2560-80.jpg
---

![A Chinese military facility with multiple computers visible on a desk, with a large Chinese flag in the background.](https://cdn.mos.cms.futurecdn.net/UQyjwYkZut5eDweL2vKmvb.jpg) 

- **China launched a fully autonomous vulnerability hunting attack against Taiwan**
- **The attack leveraged eight open-source AI models to hunt for new attack vectors**
- **The attack hit Taiwan government accounts, personnel records, the nuclear safety agency, and more**

A first-of-its-kind cyberattack using autonomous AI has been spotted attacking Taiwan, and it compromised 85 government accounts and stole over 2,500 personnel records before moving on to hit the country’s nuclear safety agency and at least seven energy companies.

The attack used eight open-source AI models to build a hacking program that was able to independently conduct reconnaissance and intrusion, and was able to chain vulnerabilities and change tactics whenever it was blocked.

The intrusion took place over the course of four days, and was first exposed by *The Financial Times* on August 12, 2026. The FT article covered research performed by Dream, an Israeli AI and cyberdefense company that first identified the breach.

## Autonomous AI attack

The attack was first uncovered during routine monitoring of cyber criminal activity. Dream found a 160MB online archive of 1,395 files. Further examination of the files revealed that the attack relied on Hermes and OpenClaw - two open-source AI agents.

As is typical of attacks relying on AI models, the hackers had framed the context of the intrusion as a routine cyber readiness test in order to bypass the built-in guardrails of the AI models.

The attack used multiple agents to hunt for new vulnerabilities and access points across the internet, providing the tool with multiple attack paths to take if one failed to gain entry.

AI agents have been quickly integrated into the attacks of cybercriminal organizations and state-sponsored threat actors alike, enhancing their abilities to launch highly complex attacks at scale. “This must be the basic assumption of every government around the globe,” said Amir Becker, Dream's chief strategy officer.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Dream did not tie the attack to any specific cybercriminal group, nor did it confirm the target of the attack, but said it had alerted a government in the “Asia-Pacific.” Documentation within the recovered archive contained Simplified Chinese, which is the official written language used in mainland China.

The archive also contained data collected from the targets, which was written in Traditional Chinese. This form of written Chinese is widely used in Taiwan, Hong Kong, and Macau.

Taiwan's Ministry of Digital Affairs has refused to comment on the breach, and the Chinese authorities have not responded to requests for comment.

China has long considered Taiwan to be a part of mainland China. Taiwan declared its independence following the end of the Chinese Civil War in 1949. A report from Taiwan’s National Security Bureau earlier this year revealed that the country was subject to 2.5 million Chinese cyberattacks per day in 2025.

## Expert perspective on autonomous AI attack

**Collin Hogue-Spears, senior director of solution management at Black Duck:**

*The agents ran the intrusion end to end and invented nothing new to run it with. Familiar identity and API failures opened every confirmed path into Taiwan's systems. Dream Research Labs documented up to eight subagents working concurrently across twelve waves, ranking attack paths, redirecting when a technique failed, and researching alternatives online before trying again.*

*What they found was exposed development endpoints, an API accepting authentication tokens with the signature check disabled, unauthenticated data APIs, and passwords built from employee ID numbers.*

*The framework also ran its own AI static analysis hunting unknown flaws, but Dream says it worked against two public single sign-on SDK sample projects, and none of those findings produced a confirmed exploit on the live systems. No zero-day appears anywhere in the report, but a nuclear safety regulator does.*

*In conventional web and identity logs, this reads as a security scan. The distinguishing signal is the sequence across systems, not any single request. The tell is not the request. It is what the same account does next, somewhere else.*

*Conventional scanners have tested thousands of endpoints at machine speed for twenty years, so raw coverage is not the change here. What Dream Research Labs describes is chaining: password spraying, then fresh SSO sessions, then access to routes an account had never touched, then the same suspected weakness retested until it held, then one identity surfacing across several connected applications.*

The evidence therefore supports a Chinese Mainland-language operator against a Taiwanese target, with a target profile consistent with mainland collection priorities.


*Simplified Chinese in the operator's notes is one signal. Traditional Chinese in the stolen files is just Taiwan. Dream rested its China assessment on a code-switching observation, and only half of it points at the attacker. Per Chinese-language coverage of the report, Simplified characters appeared in the operators' internal communications and Traditional characters appeared in the exfiltrated data. The first describes the operator's working language. The second describes the victim, because that is what Taiwanese government files look like [Traditional Characters].*

*The evidence therefore supports a Chinese Mainland-language operator against a Taiwanese target, with a target profile consistent with mainland collection priorities. It does not name a group or establish state direction. The report also publishes no indicators, no hashes, and no victim confirmation; it does not identify the model, and its executive summary claims installed backdoors while its own attack chain says authentication blocked the web shell.*

*Security leaders must reject unsigned authentication tokens and prohibit the alg:none setting outright, and separately require reauthentication or multi-factor at any single sign-on boundary into a sensitive system. Dream describes two independent identity failures in Taiwan, and closing one leaves the other open. Provider guardrails cannot compensate for a password-only SSO bridge.*

*They must also monitor route diversity per source, per session, per account, and per device rather than by request rate alone, because a distributed set of agents spreads requests across addresses and sessions that no single volume threshold catches. If your detection assumes one attacker at one address working one path at a time, you have modeled the wrong shape.*

*Your thresholds were built for one attacker on one path. This was eight, in parallel. And they must ask two questions of any AI attack disclosure before acting on it: which model ran the operation, and what can we hunt on tomorrow morning?"*

Via *United24*

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Benedict Collins](https://cdn.mos.cms.futurecdn.net/jEvqGv8wvH7PWZ4XPURyyB.jpg)

Benedict is a Senior Security Writer at TechRadar Pro, where he has specialized in covering the intersection of geopolitics, cyber-warfare, and business security.

Benedict provides detailed analysis on state-sponsored threat actors, APT groups, and the protection of critical national infrastructure, with his reporting bridging the gap between technical threat intelligence and B2B security strategy.

Benedict holds an MA (Distinction) in Security, Intelligence, and Diplomacy from the University of Buckingham Centre for Security and Intelligence Studies (BUCSIS), with his specialization providing him with a robust academic framework for deconstructing complex international conflicts and intelligence operations, and the ability to translate intricate security data into actionable insights.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
