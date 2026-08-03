---
title: Amazon warns AI is giving North Korean hackers a dangerous advantage
source_url: https://www.techradar.com/pro/security/amazon-flags-a-north-korean-hacker-group-as-being-behind-the-surge-in-open-source-supply-chain-attacks
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-03T21:17:15Z'
published: '2026-08-03T00:00:00Z'
description: Generative AI is helping North Korean hackers disguise malware inside
  trusted software used by millions of developers every week
image: https://cdn.mos.cms.futurecdn.net/kDLU9By5uaPPbwrbfEaZFJ-2560-80.jpg
---

![North Korean flag with a hooded hacker](https://cdn.mos.cms.futurecdn.net/kDLU9By5uaPPbwrbfEaZFJ.jpg) 

- **Amazon links multiple software supply chain attacks to one North Korean hacking group**
- **Generative AI enables convincing malware hidden inside trusted software packages at scale**
- **Attackers manipulated trusted maintainers before distributing compromised software updates to developers**

Amazon has linked a North Korean threat actor to several recent compromises of popular NPM software libraries.

A report from Amazon Threat Intelligence connected recent breaches of the axios, debug, chalk, and typo-crypto packages to a single group.

That group is tracked across the security community under names including SAPPHIRE SLEET, STARDUST CHOLLIMA, BlueNoroff, CageyChameleon, and Alluring Pisces.

## Attackers exploit trust to compromise widely used packages

In March 2025, the threat actor compromised the typo-crypto package through a trojanized file disguised as a legitimate dependency.

The same group later compromised debug and chalk in September 2025, then axios in March 2026.

Axios alone carries more than 100 million weekly downloads, making it one of the most widely used JavaScript libraries in existence today.

In each case, attackers socially engineered a trusted maintainer before publishing a malicious software update.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Any organization that automatically pulled the latest version of these packages received the compromised code without warning.

Wiz Research reported that roughly 1 in 10 cloud environments were affected within a two-hour window during the debug and chalk incident.

Amazon assesses the pattern as financially motivated, since compromising a small number of popular packages grants access to thousands of downstream environments simultaneously, far more efficient than targeting organizations individually.

Attackers have also shifted from single malicious packages toward fragmenting workflows across several ordinary-looking dependencies published separately over time.

## Generative AI introduces new risks for automated code review

Generative AI now allows attackers to produce coherent, well-commented code alongside convincing documentation and fabricated maintainer identities.

Because each malicious variant can be mutated, renamed, and re-encrypted, no single stable signature remains available for an antivirus or other detection tools to match.

Attackers have also begun exploiting slopsquatting, registering package names that AI coding assistants hallucinate during ordinary development work.

When a hallucinated package gets recommended by a coding assistant, an attacker who registered that name in advance can deliver malware directly.

Amazon warns that malicious packages are increasingly built to fool automated AI reviewers rather than only human analysts scanning code manually.

Hidden instructions embedded in comments, README files, or docstrings could manipulate AI scanners into approving dangerous code as safe.

Amazon Threat Intelligence and Amazon Inspector have observed that attackers split malicious workflows across multiple packages that each appear harmless individually.

Their malicious behaviour only emerges once separate components combine in the intended sequence during execution.

Amazon has invested in Amazon Inspector and its broader threat intelligence programs to help detect these evolving supply chain risks.

The company also joined the Linux Foundation's Akrites initiative and contributed $12.5 million toward defending open-source software from AI-driven attacks.

The shift toward AI-generated malware suggests traditional pattern matching alone may become less effective against evolving threats, including future ransomware campaigns using similar techniques.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Efosa Udinmwen](https://cdn.mos.cms.futurecdn.net/nwRLdPUNG4rWu4Y6nthHDV.png)

Efosa has been writing about technology for over 7 years, initially driven by curiosity but now fueled by a strong passion for the field. He holds both a Master's and a PhD in sciences, which provided him with a solid foundation in analytical thinking.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
