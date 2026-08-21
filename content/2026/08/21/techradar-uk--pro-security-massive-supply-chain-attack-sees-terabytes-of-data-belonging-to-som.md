---
title: Massive supply-chain attack sees terabytes of data belonging to some of the
  world’s biggest and most sensitive organizations leaked online
source_url: https://www.techradar.com/pro/security/massive-supply-chain-attack-sees-terabytes-of-data-belonging-to-some-of-the-worlds-biggest-and-most-sensitive-organizations-leaked-online
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-21T04:52:10Z'
published: '2026-08-21T00:00:00Z'
description: 'The LiteLLM breach needed no exploit: install the package, and a poisoned
  security scanner had already handed your cloud keys away'
image: https://cdn.mos.cms.futurecdn.net/Dtd9CSn6K6jfEdpnzch4zj-2121-80.jpg
---

![Security padlock and circuit board to protect data](https://cdn.mos.cms.futurecdn.net/Dtd9CSn6K6jfEdpnzch4zj.jpg) 

- **More than 2,500 organizations, including Cisco, Samsung, AWS, Airbus U.S. Space & Defense, Thales, and the London Stock Exchange Group, have credentials harvested during a supply-chain attack on LiteLLM**
- **LiteLLM was not directly hacked by the hacking group TeamPCP, which found their way in thanks to a compromised build of an open-source security scanner**
- **Some of the credentials still work, nearly five months after the original breach, indicating that there is still a persistent security risk until they are changed**

Security firms CloudSEK and Hudson Rock have claimed more than 2,500 organizations have had credentials harvested in a supply-chain attack on LiteLLM.

LiteLLM, an open source gateway which translates API calls for over 100 large language models into a single OpenAI-compatible format, was not directly compromised in the attack, as hackers targeted a known vulnerability in Aqua Security's Trivy.

The list included many large and critical service providers, including but not limited to Cisco, Samsung, Salesforce, and Amazon Web Services, as well as Airbus U.S. Space & Defense, Thales Group, Deutsche Bahn, Munich Re, and the London Stock Exchange Group.

## An attack that is still a concern nearly five months later

The original attack occurred on March 24 2026 and was spearheaded by a financially motivated hacking group called TeamPCP, which compromised Trivy, an open source security tool that scans for vulnerabilities.

The modified package, which was subsequently downloaded and 'invited' in by LiteLLM without checking its ID- an automated process that essentially allowed a poisoned version of the trusted tool in- gained server administrator privileges and then installed a stealer.

The stealer compromised credentials and secrets far more valuable than corporate data, including Cloud keys, SSH keys, Kubernetes tokens, environment variables, repository and package-publishing tokens, and AI provider keys.

These are arguably worse from a security standpoint than a singular breach because of both the scale of the attack and the fact that hackers now had a 'key' to many security doors rather than having to run exploits to get there.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The victim-scale research done by CloudSEK was further corroborated the following day by Hudson Rock, and it painted a grim picture of what was still an outstanding issue nearly 5 months after the original attack.

The irony is that some of the credentials still work: Independent researcher Kevin Beaumont said some of the compromised keys were still valid after he tested them, even as the impacted organization insisted it had 'rotated' those keys to new ones.

CloudSEK's figures indicate 2,500-plus companies and 434,000 CI/CD pipelines were compromised, while Hudson Rock has released a 153 GB archive of the exfiltrated material after examining a 195 TB file it had obtained. Both firms are running domain-lookup tools so organizations can check their own exposure online.

Whether these revelations lead organizations to double-check their use of AI tools in multiple mission-critical instances that could compromise not only customer data but their own trade secrets down the line remains to be seen.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Rahim Amir](https://cdn.mos.cms.futurecdn.net/9xKZFBamtEZKSChRvywbPB.png)

Rahim Amir is a UAE-based tech writer who enjoys building PCs as much as he enjoys writing about them. He has been professionally writing about PC hardware since 2023, focusing on buyer’s guides, hardware reviews, and sponsored content and features related to tech.

Having built hundreds of gaming PCs and being an avid gamer in his spare time, Rahim tends to have stronger opinions about hardware than most. This is particularly on display when he gets his way with powerful, but minimalistic RGB builds even as Small Form Factor (SFF) PCs come a close second.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
