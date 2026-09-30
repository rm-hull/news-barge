---
title: Hackers host fake ChatGPT model on its official website — but really it's just
  malware
source_url: https://www.techradar.com/pro/security/hackers-host-fake-chatgpt-model-on-its-official-website-but-really-its-just-malware
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-30T18:10:24Z'
published: '2026-09-30T00:00:00Z'
description: A fake model leading to a fake CAPTCHA
image: https://cdn.mos.cms.futurecdn.net/SSrgDUXsJwUVxtvheg4YCM-2560-80.jpg
categories:
- Technology & Software
people:
- Huntress
locations: []
organisations:
- AI
- GPT
- Google Sites
- Huntress
- OpenAI
- RAT
- SOC
- TechRadar Pro
- URL
---

![A close up of ChatGPT on a phone, with the OpenAI logo in the background of the photo](https://cdn.mos.cms.futurecdn.net/SSrgDUXsJwUVxtvheg4YCM-1920-80.jpg)

* **Attackers abused custom ChatGPT bots and Google Sites to deliver ClickFix malware**
* **Fake troubleshooting prompts tricked victims into executing malicious commands**
* **Campaign shows trusted AI platforms increasingly leveraged in social engineering attacks**

Criminals are using custom GPTs in combination with Google services to deliver a ClickFix attack to their targets and deploy dangerous malware that can control the victim’s camera and microphone, experts have warned.

A new campaign was recently spotted by security researchers Huntress, and as soon as it was shut down, a new one popped up within days.

## Abusingn legitimate services

At the center of the scam is a ChatGPT feature called “Custom GPT”. This is a version of the AI tool that a user can configure for a specific purpose, so instead of starting every conversation with a blank AI, users can create their own one, with a set of instructions, knowledge and files, and different tools and capabilities. But perhaps most importantly, they can create one with unique names, personalities, and conversation starters.

A custom GPT is hosted on ChatGPT.com, so when a user navigates to one via a link in an email or an instant message, they have no reason to be suspicious, since the URL starts with “chatgpt.com”.

In this case, unidentified hackers created a custom GPT which they named “Plus 5.6”. OpenAI names their models “GPT-3.5”, “GPT-5 Pro”, and similar, so “Plus 5.6” definitely sounds like something OpenAI might use, especially for users who don’t really keep tabs on the progress in the AI industry. This GPT was told to display a single message, regardless of the prompt. That message is “We’re currently experiencing limited availability on the primary domain”, followed by instructions to navigate to a “backup domain”.

This backup domain is hosted on Google Sites. In itself, Sites is a legitimate service for people who want to build websites without needing to know how to code. In this case, it is also likely used to appear legitimate, although those with an eye for detail might wonder why would OpenAI use Google when it would be perfectly capable of creating a backup domain itself and have it redirect automatically.

Navigating to this “backup domain” shows the attackers’ true intentions: the site displays a fake Cloudflare CAPTCHA check, asking the visitor to copy and paste a piece of code into the Windows Run program. This is the typical ClickFix attack: the victim is shown a fake problem, and immediately shown a solution.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## Deploying a RAT

The “solution” leads to the downloading and running of a Remote Access Trojan (RAT) Huntress calls “@input”. This payload gives attackers almost full control of the infected Windows computer, showing them the victim’s screen, and letting them operate the device remotely. They can switch on the webcam, microphone, and system audio to watch and listen.

They can search through every file on the computer, including the contents of documents, to find valuable information, but before doing any of that, they can take stock of the machine, checking what security software is installed, what programs are running, and how the device connects to a wider network.

The malware can also download and run additional components and separate strains. In fact, in most cases Huntress investigated, it did exactly that - without the victims noticing a thing. To remain out of sight, @input contacts its operators through encrypted lookouts that blend into ordinary web traffic, the researchers said. They also added that the tool appears to be part of a well-maintained, professionally run framework.

Huntress says the campaign impacted “dozens” of users, with the company’s SOC responding to “at least 40” incidents stemming from the specific Google Sites domain involved in this attack. The researchers reached out to OpenAI, which helped take down the custom GPT on September 25. However, a new one emerged two days later.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
