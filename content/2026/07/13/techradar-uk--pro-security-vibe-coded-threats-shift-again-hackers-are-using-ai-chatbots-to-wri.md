---
title: Experts warn hackers are using AI chatbots to write malware using natural language
source_url: https://www.techradar.com/pro/security/vibe-coded-threats-shift-again-hackers-are-using-ai-chatbots-to-write-malware-using-natural-language
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-13T18:04:55Z'
published: '2026-07-13T00:00:00Z'
description: How do you spot an attack when signatures and behaviors can no longer
  be used?
image: https://cdn.mos.cms.futurecdn.net/G8QNviZt3KrDbfWVANJrNM-1920-80.jpg
---

![malware](https://cdn.mos.cms.futurecdn.net/G8QNviZt3KrDbfWVANJrNM.jpg) 

- **Huntress analyzed AI‑generated malware “Untitled1.ps1,” a noisy custom AD enumeration tool likely built by low‑skilled attackers using generative AI**
- **Attackers paired it with s5cmd for rapid data exfiltration and SharpShares.exe for share enumeration before being detected and removed**
- **Report warns AI “vibe coding” lowers barriers for cybercrime, producing unique payloads that evade signature‑based defenses, requiring behavioral analytics to catch attack lifecycles**

“Unsophisticated” cybercriminals can now easily write malicious code using Artificial Intelligence (AI) and run devastating data breach attacks with speed, forcing defenders to rethink their strategies, researchers have claimed.

Security experts Huntress thoroughly investigating a piece of AI-written malware, and explained how the bespoke, AI-generated payload was a “highly aggressive, noisy, custom-built AD enumeration tool.”

Since cybercriminals are generally careful not to make too much noise and to try and do their bidding without raising any alarms, the researchers hint this was the work of a low-skilled attacker.

## Significant challenge

The malware, labeled Untitled1.ps1, was designed to map the Active Directory environment and apparently, it did its job well. In the next step, the crooks deployed a legitimate high-speed command-line tool for Amazon S3 operations called s5cmd which, according to Huntress, is often used for data exfiltration.

Before being spotted and kicked out, the attackers also deployed a known enumeration tool called SharpShares.exe, filtering common administrative shares while hunting for further user-accessible data repositories.

The move from off-the-shelf frameworks to custom, bespoke AI tools is a “significant challenge” for the defenders, Huntress warns.

“Historically, AVs and EDR platforms have relied heavily on file hashes and static string signatures,” they say. “Vibe-coded scripts are inherently unique. Untitled1.ps1 has never existed before and will likely never be compiled in this exact configuration again.”

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

As a result, defenders must focus on the “fundamental behaviors of the attack lifecycle.” AI can change the code syntax, they’re saying, but cannot change the underlying mechanics of Active Directory enumeration.

“Vibe coding lowers the barrier to entry for cybercrime, allowing unsophisticated actors to generate highly capable, evasive tooling on the fly,” the researchers concluded. “While the code itself may be messy, over-engineered, and filled with AI hallmarks like left-behind comments, the threat it poses is very real. To combat this, defenders must abandon rigid, signature-based thinking and embrace behavioral analytics to catch the underlying actions that no LLM can hide.”

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png)

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
