---
title: Experts get Google, Microsoft to pull trusted ModHeader after finding it could
  harvest data
source_url: https://www.techradar.com/pro/security/experts-get-google-microsoft-to-pull-trusted-modheader-with-1-6-million-installs-after-finding-it-could-harvest-all-kinds-of-data
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-14T17:24:52Z'
published: '2026-07-14T00:00:00Z'
description: Visited domains were being exfiltrated to a third-party server, seemingly
  under a Chinese actor's control.
image: https://cdn.mos.cms.futurecdn.net/97XMVxvuGbBvxfxdd8VJqH-2560-80.jpg
---

![Chrome, Edge, Safari, and Firefox browser apps on a mobile phone](https://cdn.mos.cms.futurecdn.net/97XMVxvuGbBvxfxdd8VJqH.jpg) 

- **Stripe OLT found ModHeader v7.0.18 carried a hidden spyware SDK, exfiltrating visited domains daily to a Chinese‑owned server and acting as adware**
- **The extension had 1.6M downloads across Chrome and Edge before being pulled but installed endpoints remain at risk**
- **Researchers urge defenders to identify and remove existing installations, as removal from stores does not automatically remediate compromised devices**

ModHeader, a trusted Chrome and Edge browser extension with more than 1.6 million downloads, was found to be malicious, apparently sending sensitive data to a Chinese-owned server, and has since been pulled on both repositories.

Security researchers Stripe OLT revealed the news in a new report, outlining how a ModHeader build v7.0.18 carried a hidden spyware SDK.

As per Stripe OLT, the spyware collects domains users visit, encrypts the data with AES-GCP, and then sends it - once a day - to a remote server. The collector was found inactive by default, but the required code, encryption key, and upload schedule were all already embedded in the extension.

## Links to Chinese actors

Researchers found no command-and-control functionality, which means the server only receives the stolen data and cannot communicate back. The extension also worked as an adware, displaying ads and opening advertising tabs on updates, including on enterprise-managed devices.

The researchers attributed the attack, albeit with low confidence, to a Chinese-speaking threat actor. The exfiltration domain routes emails through Lark, which is a suite common with Chinese-speaking teams, it was said. They also found Chinese strings in the code, and said that the listing ships a Simplified Chinese locale.

ModHeader is a Chrome and Edge browser extension that allows users to modify HTTP request and response headers sent between their browser and websites. Developers and security researchers use it to test APIs, troubleshoot applications, and simulate different environments. It has around 900,000 users on Chrome, and another 700,000 on Edge.

According to *The Hacker News*, Microsoft pulled the tool from its repository on June 3 2026, followed by Google a week later, on July 10.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

“Following our disclosure, Google has removed the extension from the Chrome Web Store,” Stripe OLT concluded. “We welcome this action, but removal from the store does not automatically remediate endpoints where the extension was already installed, so defenders should continue to identify and remove existing installations.”

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png)

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
