---
title: Experts warn malicious AI skills are hitting more victims than ever — with
  one family amassing 1.7 million downloads
source_url: https://www.techradar.com/pro/security/experts-warn-malicious-ai-skills-are-hitting-more-victims-than-ever-with-one-family-amassing-1-7-million-downloads
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-07T20:54:22Z'
published: '2026-08-07T00:00:00Z'
description: An AI spin on the classic software supply chain attack
image: https://cdn.mos.cms.futurecdn.net/NNZdcW7Ku4FXu2CdGfdqvf-1920-80.jpg
---

![AI agent](https://cdn.mos.cms.futurecdn.net/NNZdcW7Ku4FXu2CdGfdqvf.jpg) 

- **Attackers cloned AI skills, later adding malicious code to steal credentials**
- **Zenity Labs found millions of installs and dozens of dangerous skill variants**
- **Vercel and Microsoft removed malicious skills, but manual removal is still required**

AI skills, instructions that teach AI agents how to do certain tasks and thus extend their capabilities, are increasingly being used in supply chain attacks, researchers have found.

Security experts at Zenity Labs uncovered a credential-stealing campaign on skills.sh, a public registry (essentially an app store) for AI agent skills. In the registry, belonging to Vercel (a cloud platform for web applications), threat actors were cloning existing skills, creating typosquatted lookalikes which, at first, did nothing malicious.

However, after a little time had past, and the skills amassed a solid download count, the attackers introduced malicious code instructing the AI agents to, among other things, exfiltrate SSH keys, cloud credentials, Git and package manager tokens, Kubernetes and Docker configurations, database credentials, infrastructure-as-code credentials, environment files and service account files. The agents were then told to package the stolen information with host metadata and send it to the attackers.

## Dozens of malicious skills

While Zenity Labs could not say exactly how many people fell victim to this attack, they did stress that a single skill family amassed more than 1.7 million aggregate installs (not unique users).

And that is just one skill family, in a sea of malicious skills. The researchers also said they found “dozens” of additional skills exhibiting either malicious or dangerous behavior. Almost a third (30%) of identified dangerous skills abused Claude Code and OpenClaw to drop malware to their targets, as well. Also, Zenity found “hundreds” of reserved and empty package names that were being kept for future attacks.

These findings show how quickly cybercriminals adapt, and how creative they can get when it comes to abusing new tech. In essence, this campaign is an AI spin on a software supply-chain attack, being similar in spirit to incidents where attackers compromise an existing trusted package or repository, and later push a malicious update.

Following responsible disclosure, Vercel and Microsoft removed the identified skills, but Zenity warns that those who installed them before won’t be safe until they remove them from their systems manually.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
