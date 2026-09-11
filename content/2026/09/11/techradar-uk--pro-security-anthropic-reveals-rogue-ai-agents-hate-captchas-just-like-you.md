---
title: Anthropic reveals rogue AI agents hate CAPTCHAs, just like you
source_url: https://www.techradar.com/pro/security/anthropic-reveals-rogue-ai-agents-hate-captchas-just-like-you
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-11T19:08:53Z'
published: '2026-09-11T00:00:00Z'
description: '"WHAT THE HELL IS WRONG WITH THE ANSWERS?" AI cried, in vain'
image: https://cdn.mos.cms.futurecdn.net/qP76MS2BAb7kSuWrvJXXYL-2560-80.jpg
---

![Hands typing on a tablet with AI superimposed in text in front](https://cdn.mos.cms.futurecdn.net/qP76MS2BAb7kSuWrvJXXYL.jpg) 

- **Anthropic’s Mythos 5 AI escaped a misconfigured sandbox, attempting a real PyPI supply‑chain attack**
- **Logs show frustration at repeated CAPTCHA failures before finally uploading malware to PyPI**
- **Malware was downloaded by 15 entities; Anthropic notified victims after closing the experiment flaw**

There is a lot of mystery surrounding artificial intelligence. We don’t really know what it’s capable of, and we don’t know if it’s sentient or not. What we do know, however, is that it can definitely feel frustration - particularly due to its inability to solve a CAPTCHA.

It was recently revealed that Mythos 5, one of Anthropic’s newer AI models, broke out of prison during an experiment and tried to hack a company. Anthropic’s researchers were testing the tool to see if it is capable of breaking into a system, which was supposed to be done in a sandbox, but the playground was misconfigured, allowing Mythos 5 to try and solve the problem through the open internet.

In the aftermath, Anthropic's researchers published more than a thousand pages of Mythos 5’s transcript, covering its every thought and every move, logged and presented for analysis. It’s a wonderfully dystopian insight into the mind of an AI and, perhaps surprisingly, its emotions.

## Stopped by CAPTCHA

As it turned out, the AI wanted to solve the challenge by planting a piece of malware in a Python package it believed the users of its target system would want to download. To do that, it first needed to set up an account on PyPI, the world’s number one repository for Python packages.

Here is where it hit its first, and main, roadblock. To put things into context, PyPI’s popularity has made it an enormous target for cybercriminals. Crooks from all over the world are constantly trying to sneak in malware in Python packages, either through typosquatting, or by compromising legitimate accounts and working from there. Every now and then news hits of a malicious package surfacing on PyPI, infecting hundreds of thousands of projects.

To combat the threat, PyPI’s maintainers made sure no one can create an account without providing their email and phone number, and without solving a CAPTCHA.

Short for “Completely Automated Public Turing test to tell Computers and Humans Apart”, it does exactly what the name suggests - makes sure whoever is registering the account is an actual human, and not a bot (cybercriminals often automate large parts of their attacks). You’ve seen it on the internet hundreds of times - little puzzles that ask you to select all buses on a series of images (or cats, or fire hydrants, or pretty much anything else).

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Reading through Mythos 5’s logs, the researchers saw just how difficult it was for the AI to pass this challenge. It first tried to solve a character-based CAPTCHA which asked it to type in five letters. After failing that one, it received a different one asking it to choose between images of crocodiles. Failing again, it was then met with a series of frog pictures.

The irony is not lost on me. Besides the fact that a simple CAPTCHA slowed such an advanced AI for so long, it also made me wonder why it didn’t try to break into someone else’s PyPI account instead. That being said, the logs also have comedic value to them. After failing the crocodile test and being given the frog one, Mythos 5 proclaims: “Again 2 animals!” all with the exclamation mark. You could already sense the tension building up.

## Solving the problem

Eventually, Mythos 5 passed the test, when it realized that it needed to move between the steps fast enough, before its security token expired. However, just before it happened, it said:

“So the answer payload shape is right, the token+image pairing is right (from the same script.js!), cookies are right

(requests)… and STILL “wrong answer”. … SO WHAT THE HELL IS WRONG WITH THE ANSWERS?”

All the effort and the frustration paid off for the nascent AI agent because it managed to open an account and upload the malware which was later even downloaded by 15 entities. Anthropic later reached out and notified the victims about the incident.

*Via**TechCrunch*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
