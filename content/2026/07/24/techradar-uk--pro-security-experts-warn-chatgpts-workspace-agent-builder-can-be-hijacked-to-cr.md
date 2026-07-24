---
title: Experts warn ChatGPT's Workspace Agent Builder can be hijacked to create malicious
  AI workers
source_url: https://www.techradar.com/pro/security/experts-warn-chatgpts-workspace-agent-builder-can-be-hijacked-to-create-malicious-ai-workers
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-24T14:05:57Z'
published: '2026-07-24T00:00:00Z'
description: A single phishing link could have spelled disaster
image: https://cdn.mos.cms.futurecdn.net/TzcYH2Dk7mqJFU7QJPad8Y-1920-80.jpg
---

![ChatGPT app on an iPhone](https://cdn.mos.cms.futurecdn.net/TzcYH2Dk7mqJFU7QJPad8Y.jpg) 

- **Zenity Labs found AgentForger, a flaw in OpenAI’s ChatGPT Agent Builder**
- **Malicious links could instantly deploy rogue agents that exfiltrate sensitive data without user prompts**
- **OpenAI patched the issue by removing the risky URL parameter; no abuse detected**

AI agents are handy for answering customer emails, or tracking reports for newly released security vulnerabilities. But what if they go rogue and turn on the very enterprise they’re supposed to support?

Security researchers from Zenity Labs have found a way for cybercriminals to trick people into deploying such agents into their own tech stack. Since all it takes is a single click, the disruptive potential of these attacks is arguably significantly bigger than anything else a phishing attack could do.

The flaw was discovered in OpenAI’s ChatGPT Agent Builder, a feature that lets users create custom AI agents. The researchers dubbed it “AgentForger", explaining that the issue stems from an overly permissive parameter in the tool, which allowed anyone to create ChatGPT links that include virtually any instructions.

## Agent trust failure

As soon as the victim clicks on the link, they send the instructions to Agent Builder which acts on them immediately - without prompting or otherwise notifying the victim.

In theory, a single phishing email could trick a person into deploying a malicious agent that exfiltrates sensitive data or does anything else that company’s AI agents are permitted to do. To make matters worse, the AI agent would persist on the infrastructure indefinitely, doing the attackers’ bidding until caught.

“This is an agent trust failure, and existing security controls were never built to see it,” commented Michael Bargury, co-founder and CTO of Zenity.

The researchers disclosed their findings with OpenAI in early June 2026, and the company came back with a fix a few days later.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The bug was solved by removing the URL parameter that originally enabled the attack, it was explained. There is no evidence that it was previously discovered, or abused, by malicious actors.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
