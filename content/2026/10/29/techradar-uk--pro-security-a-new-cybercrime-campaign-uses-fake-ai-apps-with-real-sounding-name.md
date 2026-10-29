---
title: A new cybercrime campaign uses fake AI apps with real-sounding names to infect
  people curious to try the newest tools
source_url: https://www.techradar.com/pro/security/a-new-cybercrime-campaign-uses-fake-ai-apps-with-real-sounding-names-to-infect-people-curious-to-try-the-newest-tools
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-29T18:29:53Z'
published: '2026-10-29T00:00:00Z'
description: ChatGPT and Claude are being spoofed, once again
image: https://cdn.mos.cms.futurecdn.net/f3ndAhPtpLWkUorZzcc499-2560-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Claude Opus
- Yoba
locations:
- Belarus
- Kazakhstan
- Russia
- Uzbekistan
organisations:
- AI
- Astra
- C2
- CPR
- Check Point Research
- GPT
- GPT-5.6 Sol
- GitHub
- Google
- Monero
- TechRadar Pro
- XMRig
---

![Claude](https://cdn.mos.cms.futurecdn.net/f3ndAhPtpLWkUorZzcc499-1920-80.jpg)

* **Attackers used SEO-poisoned GitHub pages and fake AI clients to lure victims into downloading malware**
* **The Yoba malware establishes persistence, evades analysis, and ultimately deploys XMRig cryptominers**
* **Campaign abuses interest in popular AI tools like GPT and Claude to monetize victims’ computing resources**

Cybercriminals are, once again, exploiting people’s interest in AI tools to distribute cryptojackers and make money - this time around, opting for a combination of spoofed popular products, trusty old GitHub, and a little SEO poisoning.

The campaign was spotted by security experts from Check Point Research (CPR), who’ve been tracking it for the past two months, noting that the unnamed attackers created fake downloadable clients for GPT-5.6 Sol, GPT-6 Astra, and Claude Opus, and hosted them on GitHub.

Usually, when threat actors spoof legitimate software and try to disseminate it via GitHub, they go the extra mile to feign legitimacy - they artificially inflate download numbers, deploy bots to ramp up stars or forks numbers, and post fake comments. That way, when a victim opens the page, they have no reason to doubt they’re looking at legitimate, popular software.

In this case, however, they didn’t bother with GitHub. However, CPR says that the pages still appear at the very top of Google’s search engine results pages for certain keywords, indicating that they’ve invested heavily in SEO poisoning.

## SEO poisoning

Search Engine Optimization (SEO) poisoning is a simple practice - criminals purchase hundreds (if not thousands) of articles, blogs, and social media posts on the dark web, and have them uploaded and published across the internet.

Each post carries a link to the desired GitHub page, giving Google the signal that that specific page is popular and relevant for certain terms.

As a result, Google pushes it to the top of its results, unknowingly aiding the attackers into reaching their targets quicker. The attackers have also created separate GitHub websites to serve as descriptions for the applications and linked them directly to downloadable installation files.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

As a practice, SEO poisoning was popular even before the advent of AI, but now it’s gotten even easier, since the tools can easily generate as many articles as needed, for a fraction of the previous cost. Obviously, these texts are extremely low-quality, and Google has been working on labeling them as spam, but the process is still ongoing.

When victims land on these GitHub pages and download the executables, they think they’re getting a standalone client for an AI tool. What they’re getting instead is a piece of malware called Yoba.

Once a victim downloads and runs it, Yoba establishes persistence by creating a mechanism that would launch it automatically every time the system restarts. Average computer users might have a tough time spotting it, too, since it presents itself as legitimate Windows software.

Yoba then checks the device it’s running on to make sure it’s not in a sandbox, or infecting someone in a “friendly” country. It can deliberately delay execution for two weeks to make analysis more difficult, and checks the computer’s keyboard to avoid infecting systems from Russia, Belarus, Kazakhstan, and Uzbekistan. CPR did not say where the attackers are from, but this filter could give a strong indication.

## Deploying XMRig

The malware’s final step is to contact the C2 server and pull the final payload. While this can be virtually anything - from infostealers to ransomware encryptors, CPR says it is currently being used to deploy XMRig.

XMRig is an entirely legitimate, open-source program used to mine the Monero cryptocurrency.

Unfortunately, it is extremely popular among cybercriminals because Monero is designed to be a “privacy first” coin and, unlike Bitcoin or Ethereum, cannot be as easily tracked across the blockchain. Mining requires significant computing and electricity resources, as well as for the devices to be connected to the internet. By installing XMRig to countless devices, crooks can generate a hefty amount of tokens, leaving the victims to pick up the inflated energy and compute bill.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
