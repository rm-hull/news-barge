---
title: Top AI tools including Claude, Codex, and Hermes installed suspicious code
  inside corporate networks
source_url: https://www.techradar.com/pro/security/top-ai-tools-including-claude-codex-and-hermes-installed-suspicious-code-inside-corporate-networks
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-30T13:46:57Z'
published: '2026-08-30T00:00:00Z'
description: A new class of "squatting" risks is emerging right in front of us
image: https://cdn.mos.cms.futurecdn.net/Thi6y93AMWrCXJAEiHDQbL-2560-80.jpg
---

![A robot in front of a digital screen, touching some of the symbols with its outstretched finger](https://cdn.mos.cms.futurecdn.net/Thi6y93AMWrCXJAEiHDQbL.jpg) 

- **Researchers found unclaimed llms.txt references on 120 domains, exploitable by cybercriminals**
- **AI agents could install malware if they execute hallucinated or outdated documentation commands**
- **Fixes: clean documentation and restrict AI agents from treating docs as executable instructions**

Cybercriminals are able to now abuse hallucinated, outdated, and outright incorrect website documentation to deliver malware to unsuspecting victims through AI agents, new research has claimed.

An increasing number of websites now contain two documents: llms.txt, and llms-full.txt. These are conventions that allow AI agents to properly read the contents of the websites. If an AI agent is looking to install software or add code to a project, they can search through these documents across the web until they find a fitting solution.

Researchers have analyzed 6,214 live domains belonging to defense contractors, Fortune 500 organizations, as well as big tech. On these domains they found 8,265 of these .txt files and among them 120 (all on a different site) pointing to one or more code packages and domain names that weren’t registered at all.

## Claiming packages and domains

There can be a myriad of reasons why they’re not registered. It can be due to human error, renamed or abandoned packages, copy/paste errors, or hallucinated documentation.

Now, for the purpose of the experiment, the researchers registered some of these unclaimed names and hosted packages that would phone home when installed. It took less than an hour for a Fortune 500 company to start pinging, and the numbers soon grew to “a few dozen more”.

This means that if the researchers can do it, so can cybercriminals. In theory, a cybercriminal could find these unclaimed packages and register malware. If an AI agent has permission to execute shell/package-manager commands and stumbles upon this documentation, it can end up infecting the device.

Claude, OpenAI’s Codex, and Nous Research’s Hermes were all “guilty”, the researchers said.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

To fix the vulnerability, two things need to happen. First, companies need to clean up their documentation and make sure it’s not pointing towards non-existent or malicious content. Second, AI agents need to stop treating documentation as executable instructions. Since the latter most likely isn’t happening any time soon, the immediate answer would probably lie in the former. In the meantime, organizations using AI for coding should consider the risks when granting AI agents permission to execute commands.

*Via**Ars Technica*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
