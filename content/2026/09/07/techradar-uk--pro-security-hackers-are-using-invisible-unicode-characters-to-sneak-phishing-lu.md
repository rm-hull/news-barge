---
title: Hackers are using 'invisible' Unicode characters to sneak phishing lures into
  emails
source_url: https://www.techradar.com/pro/security/hackers-are-using-invisible-unicode-characters-to-sneak-phishing-lures-into-emails
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-07T14:14:56Z'
published: '2026-09-07T00:00:00Z'
description: Technique used in prompt injection attacks has made it into phishing
image: https://cdn.mos.cms.futurecdn.net/rsstAB5QjUqoXwXYPEgT7d-1920-80.jpg
---

![Phishing](https://cdn.mos.cms.futurecdn.net/rsstAB5QjUqoXwXYPEgT7d.jpg) 

- **Microsoft reports phishing campaign using ASCII smuggling to bypass spam filters**
- **Attackers insert invisible characters into keywords, tricking filters and AI agents**
- **Defenders should normalize Unicode tags and flag unexpected invisible code points as suspicious**

Cybercriminals are using the “ASCII smuggling” technique to make sure phishing emails pass security filters and land in people’s inboxes, experts have warned.

ASCII is a character encoding standard that turns characters and words humans can read into numeric values that computers can understand. It can also be used to create characters that aren’t even displayed on the screen (essentially “invisible” ones) but can still be read by the machine.

In a new report, security researchers from Microsoft found crooks are abusing this fact to distribute phishing emails. Most email providers offer solutions that filter out spam emails. These filters look for certain keywords and phrases, such as “funding”, “credit”, “loan”, and similar, and automatically send such emails to the spam folder.

## Ongoing campaign

By adding a set of invisible characters in the middle of these keywords, the attackers can break them apart and thus “confuse” the filters.

While the human sees the word “funding” in their email, the security solution is seeing something like “fun[a long string of characters]ding”. This technique has been adopted from prompt injection attacks, where crooks would use ASCII smuggling to deliver malicious and invisible prompts in the emails.

Therefore, when a victim asks their AI agent to summarize the email, it ends up working on a prompt that could be anything from extracting sensitive data, to deploying malware.

Microsoft is saying the campaign has been ongoing for months, and while it peaked in February 2026 with more than 2.3 million emails every day, and has been in decline ever since, it remains active to this day. In early February, Microsoft observed a cluster of almost 150 sender domains, all themed around finance. These domains accounted for almost all (96%) of all the spam emails Defender for Office 365 flagged under ASCII smuggling.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Defending sounds relatively simple, though. IT teams should normalize Unicode tag characters and other invisible code points before applying any keyword detection. They should also consider all unexpected tag-block characters as suspicious.

*Via**BleepingComputer*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
