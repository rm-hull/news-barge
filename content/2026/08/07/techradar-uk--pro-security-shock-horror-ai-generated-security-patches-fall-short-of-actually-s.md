---
title: Shock horror — AI-generated security patches fall short of actually solving
  all the problems they were meant to fix
source_url: https://www.techradar.com/pro/security/shock-horror-ai-generated-security-patches-fall-short-of-actually-solving-all-the-problems-they-were-meant-to-fix
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-07T20:54:19Z'
published: '2026-08-07T00:00:00Z'
description: AI without oversight creates patches that rarely fix the issue entirely
image: https://cdn.mos.cms.futurecdn.net/TaxPLZc75WiicpmgZNzWzL-2560-80.jpg
---

![A woman out of focus in the background touches the word AI, lit up in glowing yellow light, in the foreground. The woman is wearing smart glasses](https://cdn.mos.cms.futurecdn.net/TaxPLZc75WiicpmgZNzWzL.jpg) 

- **Researchers tested AI-generated patches on six CVEs with poor success rates**
- **Many fixes failed, altered behavior, or introduced new vulnerabilities**
- **Guidance improved outcomes, leading to FLAWED evaluation harness release**

When using Generative Artificial Intelligence (GenAI) to fix vulnerabilities, security professionals are most of the time just robbing Peter to pay Paul, experts have warned.

Researchers from 1Passwords Off-by-1 Labs analyzed fixes proposed by two frontier models - ChatGPT 5.5 at “medium” effort, and Claude Opus 4.8 at “high” effort.

As an experiment, the researchers took six recently disclosed CVEs and produced 6,080 patches using two frontier, cyber-capable reasoning models. The results were underwhelming to say the least - of all the proposed patches, just a quarter (26%) fully resolved the issue.

## FLAWED work?

This obviously leaves plenty to be desired, as half (49.3%) of the patches failed to fix at least one existing exploit path. A fifth (20.1%) fixed the original issue but changed application behavior, while 2.3% introduced new security issues. Funny enough, 2.2% failed to fix the vulnerability while also introducing additional exploit paths, as well.

Even among the patches that might be considered (26% of clean ones and 20.1% of those that changed app behavior), more than a third were fragile and not entirely addressing the underlying problem.

The researchers created an acronym for automated LLM patches: FLAWED (Fix-Like Artifacts With Embedded Defects), and warned against letting AI work without human oversight: "The expected value of a fully LLM-generated, non-human-reviewed patch is a net-negative by a considerable margin."

Results drastically improved when the AI was given better context, the researchers further explained. Before working on any patch, human developers are usually given initial guidance. When AI is given proper guidance, its success rate rises to 65%. Incorrect guidance, on the other hand, drops the success rate down to 15.2%. The difference between humans and AI is that humans are better at catching misleading information and poor guidance.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

This doesn’t mean developers will, or should, abandon AI. Worst case scenario is that developers will spend more time reviewing AI-generated fixes which could increase cognitive load and still end up being net negative. Therefore, the researchers released a patch evaluation harness called FLAWED, which organizations can now use to determine the effectiveness of their AI-generated fixes.

*Via**The Register*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
