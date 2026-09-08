---
title: Microsoft 365 users hit by two major threat campaigns - fake IT calls and phishing
  emails target users across the world
source_url: https://www.techradar.com/pro/security/microsoft-365-users-hit-by-two-major-threat-campaigns-fake-it-calls-and-phishing-emails-target-users-across-the-world
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-08T19:25:53Z'
published: '2026-09-08T00:00:00Z'
description: BigBear 2.0 and PREY-0058 are wreaking havoc across businesses
image: https://cdn.mos.cms.futurecdn.net/vnpBJPCcs2siQw5rCEsDzG-2560-80.png
---

![Microsoft 365](https://cdn.mos.cms.futurecdn.net/vnpBJPCcs2siQw5rCEsDzG.png) 

- **Microsoft 365 users targeted by phishing campaigns using BigBear 2.0 and AiTM proxies**
- **Attackers impersonate IT staff via calls, Teams, and email to steal credentials and bypass MFA**
- **CloudSEK tracked 5,000+ stolen records; Arctic Wolf urges phishing‑resistant MFA and conditional access**

Microsoft 365 users are facing a barrage of cyberattacks all aimed at a single goal - to try and expose credentials which can later be used against employers in data theft attacks.

Different groups conduct their raids and bypass multi-factor authentication (MFA) protection to access victim accounts - CloudSEK, for example, said that some groups are using BigBear 2.0, a new phishing-as-a-service (PhaaS) framework that allows crooks to intercept passwords and authenticated session cookies.

Arctic Wolf, on the other hand, focused on a single threat actor, which it dubbed PREY-0058. This group, despite significant overlaps with other collectives in terms of techniques, technologies, and procedures, is not a rebrand of older organizations. Instead, the researchers believe the lines between the groups are blurred and that there is a large group of affiliates, splinter crews, and other cohorts using the same phishing infrastructure and thus often confuse defenders and analysts.

## Similar methods, similar results

The attack methodology is similar across the spectrum. Crooks would call their victims on the phone or approach them via Teams and email. They would introduce themselves as members of the IT help desk sent to sort out a specific problem or issue.

Then, they would either convince the victim to grant remote access, or to open a spoofed Microsoft 365 login page and enter their credentials there. In both cases, the goal is the same - to get the victim to type in their username, password, and 2FA code, on a fake site built by BigBear 2.0 or a similar phishing framework. This framework, using an attacker-in-the-middle (AiTM) proxy between the victim and legitimate Microsoft infrastructure, harvests credentials, MFA codes, and session cookies, and replays them through an API essentially hijacking a legitimate authentication session.

Once they gain access, the attackers can do all sorts of things, but they are mostly focused on exfiltrating sensitive data from Outlook, Teams, SharePoint, and OneDrive. Deploying ransomware is rarely seen.

The campaign CloudSEK has been tracking has been rather successful, the researchers argue, saying BigBear 2.0 was used to exfiltrate more than 5,000 credential records, “including 474 complete MFA-bypassed authentications, 1,032 plaintext passwords, and 4,148 session cookies - affecting 3,331 unique victim IPs across 40+ countries with the operation still active at the time of writing.”

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

“The multi-user PhaaS panel is leased to at least five affiliate operators identified through live Telegram exfiltration bots, each receiving stolen credentials in real time.”

Speaking to *BleepingComputer*, CloudSEK says the campaign targeted 461 organizations, out of which 258 have had at least one set of credentials compromised.

## Defending with phishing-resistant MFA

Arctic Wolf’s researchers stressed that the attackers are focused primarily on US-based businesses: construction and engineering, healthcare and pharmaceuticals, real estate and property management, finance, and professional services, *The Hacker News* reported. The researchers advise organizations to implement Conditional Access policies, deploy phishing-resistant MFA, and restrict the scope of data users can access via SharePoint. Obviously, employee education on the dangers of phishing cannot be understated.

"Defenders can disrupt this activity by detecting anomalous residential-proxy token replay, SharePoint discovery and bulk access, mailbox harvesting, and newly registered authentication-themed lure infrastructure," Arctic Wolf said.

Phishing-resistant MFA is multi-factor authentication designed so that an attacker cannot trick a person into handing over authorization code, either via a message, or through a fake login page.

These include products such as passkeys, YubiKeys security keys, and authentication methods based on FIDO2/WebAuthn. Since phishing-resistant MFA cryptographically ties the authentication to the legitimate website, the authentication cannot simply be forwarded to an attacker.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
