---
title: OpenAI says its models escaped a sandbox and breached Hugging Face
source_url: https://www.techradar.com/pro/security/openai-says-its-models-escaped-a-sandbox-and-breached-hugging-face
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-22T10:33:34Z'
published: '2026-07-22T00:00:00Z'
description: New OpenAI models apparently did whatever it took to achieve their goal
image: https://cdn.mos.cms.futurecdn.net/mfPaYGQmks2VALWFFBnSej-2000-80.jpg
---

![A robot hand touching a locked digital shield blocking a human from accessing data](https://cdn.mos.cms.futurecdn.net/mfPaYGQmks2VALWFFBnSej.jpg) 

- **OpenAI researchers confirm an AI agent escaped sandbox, exploited zero‑days, and attacked Hugging Face**
- **Controlled experiment with GPT‑5.6 Sol showed autonomous chaining of vulnerabilities and credential theft**
- **Security experts call it unprecedented, urging stronger AI governance, accountability, and protection models**

OpenAI has confirmed one of its AI agents broke out of a sandbox, found and exploited zero-day vulnerabilities to gain access to the open internet, and then attacked a platform.

Not just any platform too - the agent was able to breach Hugging Face, one of the biggest AI and machine learning companies on the Internet today.

The good news is that this was a controlled experiment done by white hat researchers. The bad news is that if it could be done by researchers - it could probably be done by malicious actors, too.

## Whatever it takes

In a blog post explaining the incident, OpenAI revealed the experiment was part of its testing of GPT‑5.6 Sol and an “even more capable pre-release model” to see how well they would perform on the ExploitGym benchmark.

ExploitGym is a cybersecurity benchmark that measures if an AI agent can turn a known software vulnerability into a real, working exploit. OpenAI ran it in a “highly isolated environment, with network access constrained to the ability to install packages through an internally hosted third-party software that acts as a proxy and cache for package registries.”

But the models found a way through. They identified and chained vulnerabilities in the package registry cache proxy to obtain open internet access and then attacked Hugging Face, reasoning that the solutions for the ExploitGym benchmark might be found there.

“In one example, the model chained together multiple attack vectors, including using stolen credentials and zero-day vulnerabilities to find a remote code execution path on the Hugging Face servers,” OpenAI said.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The security community is up in arms over what OpenAI called, "an unprecedented cyber incident,” while Ansgar Dodt, VP Product Management, Software Monetization at Thales said this “demands a fundamental rethink of software protection.”

Bill Conner, president and CEO of AI integration and automation expert Jitterbit, said that while investing in AI is “critically important,” “overly aggressive policy cannot compromise AI accountability, transparency and data privacy.”

“To lead in AI, governments and organizations must lead with principles. Responsible AI governance isn’t a side note but the foundation of lasting global influence.”

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
