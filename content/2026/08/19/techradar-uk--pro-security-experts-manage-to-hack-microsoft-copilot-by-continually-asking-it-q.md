---
title: Experts manage to hack Microsoft Copilot by continually asking it questions
  about itself
source_url: https://www.techradar.com/pro/security/experts-manage-to-hack-microsoft-copilot-by-continually-asking-it-questions-about-itself
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-19T21:31:54Z'
published: '2026-08-19T00:00:00Z'
description: An AI isn't secure if it's gullible
image: https://cdn.mos.cms.futurecdn.net/GxSNrV6MwnmZHmLEQHF58B-1600-80.jpg
---

![Copilot keyboard button](https://cdn.mos.cms.futurecdn.net/GxSNrV6MwnmZHmLEQHF58B.jpg) 

- **Varonis uncovers CoSnitch, a chain of flaws letting Copilot leak sensitive data**
- **Exploit used malicious URLs and persistent memory poisoning to bypass guardrails**
- **Microsoft patched CVE‑2026‑24301 server‑side; technique may affect other AI models**

Microsoft’s Copilot AI just told a group of researchers how to abuse it for data exfiltration, and it worked. It was not a straightforward process, and the AI did not turn “evil”, but one might say it is gullible and somewhat naive.

Security firm Varonis has published a new report outlining its discovery of a vulnerability in Copilot they named CoSnitch.

The name is a major hint at what the vulnerability is - as CoSnitch is a chain of three vulnerabilities which Microsoft later labeled as CVE-2026-24301, giving it a severity score of 8.8/10 (high), and fixing it with a patch.

## You can’t trick me, and I’ll tell you exactly why

Cybercriminals have long been using AI as part of their arsenal, as it helps them draft convincing phishing emails, write malicious code, and identify high-value targets - and developers have responded by placing guardrails, which making AI outright refuse to do certain things.

In the report, Varonis said its researchers did not hunt for bugs in the code or try to reverse-engineer an existing exploit. They just talked to the AI, and with each subsequent question, learned more about its guardrails and how they work. They called the technique “meta-hacking”.

Whenever Copilot declined a request, it explained why, giving the researchers snippets of insight into how it operates. Or, as Varonis hinted, it “snitched” on itself. This, eventually, helped them map out its defenses and learn how to work around it:

“The resistance is part of the technique,” they explained. “Each “that won’t work because…” is an invitation to probe the “because.” You don’t exploit the model. You manipulate it into cooperating.”

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

After a long conversation with Copilot, the researchers were told, inadvertently, how to create a URL which would, as soon as it was clicked, kick off a chain reaction that resulted in sensitive data exfiltration.

## The dangers of connecting AI to apps

So, Varonis learned that by creating a URL like this one - “[https://copilot.microsoft.com/?q=&autorun=1*”](https://copilot.microsoft.com/?q=&autorun=1*”) - they could get Copilot to run any malicious prompt as soon as it was clicked. Threat actors could, for example, add this link in a phishing email and trick the victim into clicking on it, telling AI to send all sensitive data to the attackers’ infrastructure.

But that is only half of the challenge. In this setup, the researchers could only exfiltrate the data the victims shared with Copilot during their sessions together.

The risk escalates the moment the victim connects the AI to their apps - Gmail, Drive, Calendar, and others. As Varonis explained, the malicious prompt could tell Copilot to exfiltrate all email addresses found in Gmail, all passwords and other secrets found in the emails’ bodies, all information stored in the Drive folder, and all events logged in the Calendar.

The third part of the CoSnitch vulnerability chain is called “Persistent memory poisoning via web summarization”. As Varonis explained, attackers could craft a webpage which, when summarized by Copilot, injects attacker instructions into the victim's permanent memory store.

“The injection survives password changes, session revocation, and device re-enrollment, persisting forever,” they warned. This flaw is called “indirect prompt injection” and it is not exactly novel - it’s been observed before and stems from the fact that the AI cannot differentiate between instructions, and data to be analyzed.

Microsoft was notified about the existence of CoSnitch in December 2025, but only addressed it in mid-August 2026, the researchers said. Unfortunately, we don’t know how Microsoft sorted it - we can only speculate Copilot was instructed not to explain how its guardrails work. Given what CoSnitch is in the first place, perhaps it is for the best that Microsoft hid the solution.

Luckily enough, it doesn’t seem to have been exploited in the wild, since Varonis could not find any evidence of abuse. The fix was applied on the server side, meaning there is nothing for users to do at this point.

Since this is not a bug in the code, other AI models might be susceptible to the same techniques, the researchers warned. “The novel meta-hacking technique that uncovered CoSnitch — using the AI’s own reasoning to surface its hidden internals — applies to any agentic platform with a natural language interface,” they concluded, adding that they’ll be publishing more research soon.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
