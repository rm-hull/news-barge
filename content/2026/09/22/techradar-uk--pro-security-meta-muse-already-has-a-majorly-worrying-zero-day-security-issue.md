---
title: Meta Muse already has a majorly worrying zero-day security issue
source_url: https://www.techradar.com/pro/security/meta-muse-already-has-a-majorly-worrying-zero-day-security-issue
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-22T13:24:07Z'
published: '2026-09-22T00:00:00Z'
description: The company has been informed, but is yet to comment, or issue a patch
categories:
- Technology & Software
- Business & Entrepreneurship
image: https://cdn.mos.cms.futurecdn.net/n2dFzA7TpfgKDWytxEnzX4-1920-80.jpg
locations:
- Bosnia and Herzegovina
- Sarajevo
people:
- Patrick Wardle
- Sead
organisations:
- Al Jazeera Balkans
- Ars Technica
- Artificial Intelligence
- Google News
- Meta Muse AI
- Objective-See
- Represent Communications
- TechRadar Pro
---

![Meta Muse AI agent](https://cdn.mos.cms.futurecdn.net/n2dFzA7TpfgKDWytxEnzX4.jpg)

* **Researcher Patrick Wardle finds zero‑day in Meta’s new Muse AI assistant,**
* **Dubbed not‑a‑mused, the exploit requires local compromise, voice dictation, and app integrations; attackers can hijack tokens and exfiltrate data**
* **Meta has been informed but no patch yet; flaw highlights risks of AI assistants with broad permissions**

Meta’s new Artificial Intelligence (AI) assistant Muse reportedly carried a zero-day vulnerability that allowed attackers to gain access to people’s apps, such as WhatsApp or email.

However, it’s not as straightforward as your usual zero-day - to exploit it, simply deploying malware will not suffice. Certain features need to be enabled, and certain integrations established before the bug could be leveraged.

## Not-a-mused

A little background, for context: Meta recently released Muse, describing it as an assistant that can “book appointments, fill out forms, and handle customer service.” It says the tool, available exclusively for the Mac ecosystem for now, “proactively takes tasks off your plate” and makes purchases, generates images, and creates documents.

To do that, however, it needs to connect to apps such as email, WhatsApp, calendar, or social media accounts - and this connection is the first prerequisite needed to exploit the flaw.

The second prerequisite is voice dictation. The vulnerability was found in the way Muse handles commands received via voice, meaning the attacker must piggyback onto voice commands in order to escalate privileges and access other apps and their content.

Now for the flaw itself. It was discovered by security researcher Patrick Wardle, founder of nonprofit Objective-See. He named it “not-a-mused” and says it hides in an undocumented setting called endo\_voyager\_dictation\_endpoint. When a user narrates a voice command, that instruction is sent and processed in the cloud, where Meta can log it. This setting allows the user to change which endpoint receives the dictation.

Which brings us to the third prerequisite. The threat actor must have local access to be able to change this setting in the first place. In other words, the device must already be compromised in some way, either via remote monitoring and management tools, or via low-level malware (or with physical access).

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

For the sake of the report, let’s say that a theoretical user checks all the right boxes - they’re running a compromised machine and are talking to Muse that’s already connected to other productivity apps. Instead of reaching Meta’s endpoints, the voice commands are first sent to attacker-controlled infrastructure, where the AI assistant, together with the instructions, also sends authentication tokens for the tool.

If the attacker reacts fast enough, they can grab the token and access their target’s AI tool. If it’s connected to other apps, such as WhatsApp or calendar, they can simply prompt it to extract whatever sensitive information is found inside.

Not-a-mused is therefore a combination of data exfiltration and privilege escalation.

## Ironing out the kinks

“We can manipulate the agent and leverage its privileges to do whatever we want,” Wardle told *Ars Technica*.

“So instead of us having to write a very comprehensive Mac malware stealer, we can just leverage the AI assistant itself.” Wardle said he has developed several proof-of-concept attacks that do things like writing malicious files to disk and snapping pictures, in many cases with no indication to even an alert user.

Meta has been informed, but is yet to comment, or issue a patch.

AI assistants are all the rage nowadays. They’ve turned elaborate answer machines into tools that can complete assignments, even more complex ones. They can book flights and restaurant tables, make purchases, schedule and reschedule calls and meetings, and more. However, to do that, these tools need extensive permissions - something the security community is warning of.

While they’re not openly speaking against it, they are advising caution. There are many stories of AI agents either going rogue, or simply being tricked by malicious actors. For example, a hidden prompt in a phishing email can trick an AI agent tasked with summarizing the message into exfiltrating all .PDF documents from the victim’s inbox.

In the early days of agentic AI, there were reports of assistants simply deleting people’s inboxes.

Assistants are likely here to stay, but there are still quite a few kinks to iron before they can hit the mainstream.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png)

![Google logo on a black background next to text reading &#039;Click to follow TechRadar&#039;](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg)

***Follow TechRadar on Google News***and** add us as a preferred source** * to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
