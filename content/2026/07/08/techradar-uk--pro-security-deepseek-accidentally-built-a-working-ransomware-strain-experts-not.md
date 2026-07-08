---
title: DeepSeek designed a browser attack that steals photos without installing any
  app
source_url: https://www.techradar.com/pro/security/deepseek-accidentally-built-a-working-ransomware-strain-experts-note-what-we-are-witnessing-is-a-fundamental-shift-in-how-novel-cyber-attacks-are-born
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-08T03:41:02Z'
published: '2026-07-08T00:00:00Z'
description: Chrome browsers on Android are quietly exposed to a ransomware trick
  AI figured out alone
image: https://cdn.mos.cms.futurecdn.net/FMwRmCw7wxB7F6AQgqzqnX-1920-80.jpg
---

![DeepSeek](https://cdn.mos.cms.futurecdn.net/FMwRmCw7wxB7F6AQgqzqnX.jpg) 

- **DeepSeek connected a theoretical browser flaw to a working attack chain**
- **The ransomware sample targets Android's photo folder through a fake permission prompt**
- **Check Point classified 1,383 DeepSeek-linked files as malicious or dangerous**

A Chinese AI model accidentally stumbled into a working ransomware technique while trying to satisfy an unrealistic, broad prompt.

New findings from Check Point Research say the DeepSeek-generated sample connected a theoretical browser risk to a functioning attack method, requiring no exploit, no app installation, and no real technical skill from the attacker.

It targets Android's photo storage through a legitimate browser feature called the File System Access API, disguised as a simple AI photo-enhancing tool.

## How the attack actually works

The technique abuses Android's DCIM folder, which typically holds years of personal photos, scanned identification documents, and banking screenshots.

Victims grant access through a single permission prompt disguised as an AI-powered photo enhancer, unaware they are handing over control of an entire directory.

Check Point's dataset included nearly 3,000 files attributed to DeepSeek, and researchers classified 1,383 of them as malicious or dangerous using VirusTotal and static analysis methods.

The team found a sample implementing a dangerous browser-native technique which has never been observed before in real-world attacks.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The sample, nicknamed InfernoGrabber 9000, was incomplete, yet testing showed it required little additional effort to become fully functional.

“Very little effort is needed. Low-level expertise is sufficient. You don't need to be a sophisticated cybercriminal or advanced persistent threat group,” said Pedro Drimel Neto, malware analysis team leader at Check Point

“In fact, we've already observed evidence of actual threat actors attempting this attack using straightforward LLM prompts.”

## Why this marks a turning point

"What we are witnessing is a fundamental shift in how novel cyber attacks are born. For the first time, we have evidence that an AI model can independently reason across legitimate platform features," said Eli Smadja, Head of Research at Check Point

This represents a major shift in how novel cyber-attacks are discovered and developed.

However, the underlying browser risk is not entirely new. A 2023 USENIX Security paper examined how the File System Access API could theoretically enable ransomware.

What changed, according to Check Point, is that DeepSeek connected these previously theoretical ideas into a realistic, working attack chain without human guidance.

When researchers tested the same concept using the latest DeepSeek V4 model, it refused direct ransomware requests but complied once explicit terms were removed.

Comparable testing against other LLMs produced only refusals or heavily constrained, browser-safe implementations lacking the same file-access capability.

Check Point ultimately built a working proof of concept, successfully encrypting photos on Android devices running Chrome 148, confirming the danger extends well beyond a single flawed sample.

Organizations embedding AI into their workflows must now treat every browser permission prompt as a genuine security decision rather than a routine click.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Efosa Udinmwen](https://cdn.mos.cms.futurecdn.net/nwRLdPUNG4rWu4Y6nthHDV.png)

Efosa has been writing about technology for over 7 years, initially driven by curiosity but now fueled by a strong passion for the field. He holds both a Master's and a PhD in sciences, which provided him with a solid foundation in analytical thinking.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
