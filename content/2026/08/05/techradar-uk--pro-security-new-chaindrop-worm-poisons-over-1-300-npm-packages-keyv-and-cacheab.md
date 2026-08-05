---
title: New ChainDrop worm poisons over 1,300 npm packages, Keyv and Cacheable among
  those hit
source_url: https://www.techradar.com/pro/security/new-chaindrop-worm-poisons-over-1-300-npm-packages-keyv-and-cacheable-among-those-hit
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-05T14:28:58Z'
published: '2026-08-05T00:00:00Z'
description: Another Shai-Hulud variant hits npm packages
image: https://cdn.mos.cms.futurecdn.net/x4SmwpYXk8yGgDmYCVeckL-2560-80.jpg
---

![A hand about to touch a phone. Superimposed on top of it is a pink triangle with exclamation mark inside it. Behind it is a computer display with code on it](https://cdn.mos.cms.futurecdn.net/x4SmwpYXk8yGgDmYCVeckL.jpg) 

- **Aikido researchers uncovers ChainDrop, a Shai‑Hulud variant infecting 1,300+ npm packages with an infostealer**
- **Attackers compromised GitHub accounts tied to popular libraries (Keyv, Cacheable, flat‑cache, file‑entry‑cache) and pushed tainted releases with 2B monthly downloads**
- **Malware exfiltrates developer/cloud credentials and secrets to a public GitHub repo; admins should treat affected systems as compromised even after removal**

Another Shai-Hulud variant has been discovered in the wild, infecting more than 1,300 npm packages with an infostealer.

Security researchers Aikido reported finding “at least 868 packages (across 1381 versions) that have been compromised by the worm.”

Shai-Hulud is a self-propagating supply chain malware that targets software developers by compromising open-source packages and CI/CD pipelines. It steals credentials, API keys, and access tokens and then uses those stolen secrets to publish additional malicious packages.

## What to do in case of an infection

In May 2026, actors claiming to be associated with the TeamPCP group publicly released the Shai-Hulud worm's source code, saying they were “open sourcing the carnage” and inviting other threat actors to adopt and modify the code. Since then, there were multiple copycat campaigns and variants, including this one which Aikido dubbed ‘ChainDrop’.

Aikido said the attackers compromised the GitHub account of the person maintaining Keyv and Cacheable, widely used open source JavaScript libraries for caching data in Node.js applications. From there, they were able to move into other popular utilities such as flat-cache and file-entry-cache, as well as packages associated with organizations such as Deliveroo, Ornikar, OneReach, Picsart, Qlik, and ServiceTitan.

The malware was pushed directly into the projects’ main branches, and then generated additional package releases. The compromised packages have a combined 2 billion monthly downloads.

Aikido says the infostealer grabs developer and cloud credentials, encrypts them, and then sends them to a public GitHub repository called “Shai-Hulud: Here We Go Again.”

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

It also steals local configuration files, GitHub PATs, workflow tokens, and other ghp_, gho_, and ghs_ tokens, certain npm tokens, GitHub Actions secrets, AWS credentials, Kubernetes secrets, and more.

The researchers are saying system admins who installed a tainted package should treat their developer workstation or CI/CD runner as compromised, even if they removed the package.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
