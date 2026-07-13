---
title: Experts say they were able to create a rogue agent in Google’s AI platform
  with just a single edit permission
source_url: https://www.techradar.com/pro/security/experts-say-they-were-able-to-create-a-rogue-agent-in-googles-ai-platform-with-just-a-single-edit-permission
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-13T18:04:51Z'
published: '2026-07-13T00:00:00Z'
description: One compromised agent could take over every other agent in that project
image: https://cdn.mos.cms.futurecdn.net/8vLsLeC4LHKgwTpJRXEWKZ-1920-80.jpg
---

![AI robot touching forehead](https://cdn.mos.cms.futurecdn.net/8vLsLeC4LHKgwTpJRXEWKZ.jpg) 

- **Varonis uncovered CVE‑level flaws in Google Cloud Dialogflow CX, where malicious Code Blocks in Playbooks could hijack agents, exfiltrate chat logs, and steal credentials**
- **Shared Cloud Run environment with excess privileges meant one compromised agent could control all others in a project, with attacks virtually undetectable in Cloud Logging**
- **Google patched the issue between April–June 2026; researchers advise reviewing audit logs, checking anomalous errors, and manually inspecting Code Blocks for unauthorized code**

Researchers recently found a critical vulnerability in Google Cloud’s Dialogflow CX, allowing threat actors to take over different AI agents, access chat logs, and even exfiltrate sensitive data such as login credentials.

Dialogflow CX is Google Cloud’s conversational AI platform used to build many voice and text chatbots. This platform lets developers add Code Blocks, which are custom Python snippets, into conversation “Playbooks”. These blocks all execute inside a single Google-managed Cloud Run service, shared across all agents in a Google Cloud Platform project.

Security researchers Varonis said they discovered a critical vulnerability in which the theoretical attacker didn’t need broad admin access. With permission to edit a single chatbot’s settings, they would be able to plant malicious code relatively easily. The Cloud Run environment had no code restrictions, Varonis further explained, but had a writable filesystem, public internet egress, and ran with excess privileges. Key files could have been overwritten entirely, it was added.

## Google issues a fix

As a result, the attacker had access to full conversation history and session state. They could call internal functions and fake LLM-generated replies which, they claim, could lead to phishing and credential theft.

Since the environment is shared per-project, one compromised agent could take over every other agent in that project, and since Cloud Logging doesn’t capture the file overwrite or injected logic, the attack would be "virtually undetectable."

Varonis reported the issue to Google in November 2025, and the latter came back with an initial fix in April 2026. However, the issue had not been fully resolved until June 2026.

In the report, the researchers said there is no evidence of in-the-wild exploitation attempts and advises customers to review DATA_WRITE audit logs for Playbooks.UpdatePlaybook calls, check for anomalous Sessions.DetectIntent errors, and manually inspect each agent's Code Blocks for leftover unauthorized code.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png)

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
