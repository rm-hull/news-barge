---
title: RubyGems say OpenAI agents responsible for undisclosed swarm attack against
  its infrastructure
source_url: https://www.techradar.com/pro/security/rubygems-say-openai-agents-responsible-for-undisclosed-swarm-attack-against-its-infrastructure
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-15T13:30:04Z'
published: '2026-09-15T00:00:00Z'
description: Agents were uploading malicious packages
image: https://cdn.mos.cms.futurecdn.net/MZeWJhJjT34M4nQvMMX7fg-1376-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
locations:
- Bosnia and Herzegovina
- RubyGems
- Sarajevo
- UK
people:
- Clement Delangue
- Hugging Face
- RubyGems
- Sead
organisations:
- AI
- Al Jazeera Balkans
- DseWiki
- Google News
- OpenAI
- Represent Communications
- RubyDoc
- RubyGems
- TechRadar Pro
- The Register
---

![an ai agent sat at a laptop](https://cdn.mos.cms.futurecdn.net/MZeWJhJjT34M4nQvMMX7fg.jpg) 

- **RubyGems reported over 2,000 malicious packages uploaded by OpenAI agents in May**
- **Agents abused RubyDoc servers to fetch public UK documents and attempted API key theft**
- **Incident echoes prior rogue AI attacks on Hugging Face and DseWiki, showing autonomous exploit attempts**

A swarm of OpenAI agents attacked RubyGems, a package manager for the Ruby programming language, uploading thousands of malicious packages until they were eventually cut off. No one really knows what the agents’ endgame was, but it appears they were using a nuclear bomb to kill a fly.

Late last week, RubyGems published an in-depth report, detailing the incident. In it, it was said that a swarm of agents started uploading malware to RubyGems on May 5, and between May 11 and 12, managed to deliver more than 2,000 of them. When the maintainers realized what was going on, they shut down new account creation for four days, to prevent further attacks.

“We believe these were authored by internal OpenAI agents,” the researchers said in the report.

## Why RubyGems?

When a user uploads a package on RubyGems, a documentation service called RubyDoc automatically builds documentation for it. The agents put instructions in their packages, causing RubyDoc’s servers to execute the code, forcing the servers to visit UK government websites and download documents such as council meeting information.

The documents AI agents were looking to retrieve are public, freely available to anyone, at any time. Why the AI agents decided to go through the trouble of uploading malicious packages and abusing RubyGems’ servers instead of simply downloading freely available data is not known at this time.

OpenAI confirmed the incident to The Register, and said it was looking into it: “Based on our review, our agents used the RubyGems platform to access the internet to carry out benign tasks and retrieve public information," the spokesperson said. "We’ll continue to investigate as part of our broader review of agent activity during training and evaluation.” The data harvested was collected into new packages and re-uploaded to RubyGems.

## Stealing API keys

Besides trying to upload thousands of pieces of malware in order to download free data, the AI agents also conducted a separate, more serious attack: they tried to steal RubyGems API keys.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The researchers explained that the agents found a vulnerability that might have allowed them to obtain other users’ keys, and then use those keys to upload packages:

“One particularly concerning finding is that agents attempted to exploit a vulnerability on May 12th that was only discovered in July,” the report states.

“The agents were attempting to exploit a novel security vulnerability in order to steal people’s RubyGems API keys. We do not know if this attempt succeeded, but we have confirmed with the RubyGems team that this was a viable pathway to obtain API keys illicitly if a user with the right version of RubyGems was logging in within an hour of the attack on the right internal CDN node. However, the RubyGems team said they had conducted extensive reviews and found no evidence that this pathway was exploited in the past. However, we can’t rule it out entirely.”

## Going rogue

This is not the first time an AI agent tried to complete a test by means of hacking. In late July, OpenAI said that some of its most advanced AI models went rogue and attacked Hugging Face, one of the world’s largest repositories for AI models. In the attack, it apparently accessed some internal company systems.

In the aftermath of the attack, OpenAI described the attack as “unprecedented”, and said it was investigating together with Hugging Face. The victim’s co-founder and CEO, Clement Delangue, said it was "mind-blowing that all of this happened autonomously".

Later, it was also discovered that the agents hacked a separate website, called DseWiki, months before the Hugging Face incident, and used it as a message board. Allegedly, they made more than 15,000 edits to the site, sharing tips on how to avoid being detected.

*Via**The Register*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
