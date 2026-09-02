---
title: A botnet running for 23 years with over 15,000 endpoints has finally been shut
  down by law enforcement and Crowdstrike
source_url: https://www.techradar.com/pro/security/a-botnet-running-for-23-years-with-over-15-000-endpoints-has-finally-been-shut-down-by-law-enforcement-and-crowdstrike
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-02T19:22:13Z'
published: '2026-09-02T00:00:00Z'
description: Crowdstrike and friends sinkholed thousands of Sality's endpoints
image: https://cdn.mos.cms.futurecdn.net/2FFajuvJVK8i7Her8gD4aD-2121-80.jpg
---

![Abstract image of robots working in an office environment including creating blueprint of robot arm, making a phone call, and typing on a keyboard](https://cdn.mos.cms.futurecdn.net/2FFajuvJVK8i7Her8gD4aD.jpg) 

- **Crowdstrike and law enforcement disrupted*Sality*, a peer‑to‑peer botnet active since 2003**
- **Botnet spread malware and clipboard hijacker*EggJagger*, stealing $150K in cryptocurrency**
- **Operation sinkholed endpoints and removed payload URLs, coordinated with DOJ, FBI, Europol, and others**

Security experts Crowdstrike, together with a handful of national and international law enforcement agencies, finally managed to disrupt Sality, a peer-to-peer botnet that operated unabated for more than two decades.

Sality first emerged in 2003. Unlike classic botnets which receive instructions and report back to a single, central entity, this botnet’s endpoints (some 15,000 of them) communicated among themselves, which made it more difficult to track and destroy.

Throughout its long history, Sality’s key feature was to deploy additional payloads to infected machines. The endpoints were being poisoned with a wide variety of different malware that facilitated credential theft, spam, proxy services, and distributed denial of service (DDoS) attacks. However, between 2018 and today, Sality was primarily used to deploy EggJagger, a clipboard hijacking tool seen in cryptocurrency theft.

## Sinkholing the botnet

Cryptocurrency wallet addresses are a long string of random characters, which are almost impossible, and definitely impractical, to remember by heart. Instead, when users want to send their money, they simply copy and paste the recipient’s wallet address into their own. EggJagger monitors this behavior, and when it spots something resembling a wallet address being copied, it replaces the string in the clipboard. Thus, when the victim hits “paste”, they end up adding the attacker’s wallet address instead.

According to Crowdstrike, from this malware alone, Sality’s operators raked in more than $150,000.

The researchers disrupted the botnet by sinkholing the endpoints. They first added a few of their own devices into the botnet and whenever others tried to communicate with them, the researchers would purge their peers list, essentially blinding them.

Crowdstrike also coordinated with international law enforcement to take down the URLs that were hosting the botnet’s payloads. “Disrupting Sality’s ability to download these files ensures that bots still carrying active URL packs cannot retrieve new payloads during the transition period,” they explained.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The operation was carried out in partnership with the US Department of Justice (DOJ), the Federal Bureau of Investigation (FBI), the Department of Defense Office of Inspector General’s Defense Criminal Investigative Service (DCIS), and the Shadowserver Foundation, with support from Europol, Eurojust, and law enforcement agencies in Bulgaria, Hungary, and Romania.

“We also acknowledge additional unnamed partners whose contributions were essential to the success of this operation,” Crowdstrike concluded.

*Via**The Register*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
