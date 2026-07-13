---
title: Experts warn AI gateways connected to Amazon Bedrock are being hijacked to
  steal crypto
source_url: https://www.techradar.com/pro/security/cryptomining-can-be-a-lucrative-post-compromise-activity-in-cloud-environments-experts-warn-ai-gateways-connected-to-amazon-bedrock-are-being-hijacked-to-steal-crypto
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-13T14:56:23Z'
published: '2026-07-13T00:00:00Z'
description: Researchers found a new spin on an old attack, as AI gateways are used
  to enable cryptocurrency mining.
image: https://cdn.mos.cms.futurecdn.net/Rb6YDzdRZjccpn6MQ26KML-2560-80.jpg
---

![A person typing on a laptop and using a tablet. Only their upper torso, arms and hands are visible. Text superimposed on the image shows AI](https://cdn.mos.cms.futurecdn.net/Rb6YDzdRZjccpn6MQ26KML.jpg) 

- **Darktrace reports cryptojacking via a compromised AI gateway (LiteLLM‑Proxy on AWS Bedrock), breached through exposed SSH and abused with XMRig mining**
- **Attackers also showed suspicious IAM activity, hinting at possible cloud credential misuse, with connections traced to Vietnam**
- **Experts warn AI gateways concentrate privileged access, urging strict port closures, least‑privilege roles, and control‑plane monitoring to reduce blast radius**

If you are using AI gateways as part of your tech stack, be wary - they are being leveraged in cryptojacking attacks, experts have warned.

Cybersecurity researchers Darktrace have published a new report on a cloud-hosted AI gateway, connected to Amazon Bedrock, which was compromised and used for cryptocurrency mining.

An AI gateway is a piece of software that runs between users or applications and one or more AI models. It is not unlike a reverse proxy or an API gateway, but just for AI services. In this case, an Amazon EC2 instance running an AI gateway called LiteLLM-Proxy was given centralized access to large language models (LLM) hosted on Amazon Bedrock (AWS’ fully managed generative AI platform).

## Shady Vietnamese accounts

According to Darktrace, threat actors gained access most likely through a brute-force attack, since the EC2 instance was configured to accept SSH connections from anywhere on the internet.

After breaking in, they downloaded XMRig, by far the most popular cryptocurrency mining program. Within minutes, the instance started making repeated encrypted connections to a cryptocurrency mining pool, which also set off Darktrace’s alarms and spotted the attack.

Soon after, Darktrace spotted more suspicious activities, this time involving an AWS Identity and Access Management (IAM) user. This account started giving out unexpected and previously unused commands, such as enumerating and invoking Amazon Bedrock foundation models, or trying to set up a new IAM user account.

The final red flag was the IP address of that user - tracing back all the way to Vietnam. Darktrace said there was insufficient evidence to conclusively link the IAM activity with the earlier compromise of the AI gateway, but stressed that the behavior could indicate attempted cloud credential misuse.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png)

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
