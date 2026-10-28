---
title: Watch out — that Microsoft Teams chat might be hackers impersonating your IT
  support
source_url: https://www.techradar.com/pro/security/watch-out-that-microsoft-teams-chat-might-be-hackers-impersonating-your-it-support
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-28T05:33:17Z'
published: '2026-10-27T00:00:00Z'
description: Crooks are messaging victims via Teams and offering IT support
image: https://cdn.mos.cms.futurecdn.net/JnkKiUetccxhjSuwFcdUPc-970-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Arctic Wolf
- Ethan
- Liam
- Scott
locations: []
organisations:
- AnyDesk
- Arctic Wolf
- IT Service Desk
- Microsoft Teams
- RMM
- ScreenConnect
- TechRadar Pro
---

![Microsoft Teams](https://cdn.mos.cms.futurecdn.net/JnkKiUetccxhjSuwFcdUPc-970-80.jpg)

* **Attackers flood inboxes with spam, then impersonate IT support through Microsoft Teams messages and calls**
* **Victims are tricked into sharing remote access via Quick Assist, AnyDesk, or ScreenConnect**
* **Researchers observed 400+ incidents, warning default Teams federation settings enable the social-engineering campaign**

Cybersecurity researchers Arctic Wolf have warned of an ongoing, widespread hacking campaign that includes an email inbox flooded with spam messages, a Teams account impersonating IT support, and the use of absolutely legitimate, everyday software.

The goal seems to be persistent access, possibly in preparation of a subsequent malware or ransomware infection.

## How the attack plays out

In its report, Arctic Wolf said it observed the same pattern in more than 400 cases. It starts with the victim - an employee in the target company - receiving hundreds, possibly thousands of spam emails in a very short timeframe, so their inbox gets absolutely flooded with junk, burying any and all meaningful, valuable emails under a mountain of trash.

A few moments later, that same person gets a Teams message from a user that, by all accounts, looks legitimate: their name clearly states “IT Service Desk”, and sometimes even has a first name next to it (something along the lines of Liam, Ethan, or Scott). They tell the victim they’ve been made aware of the problems they’re having with their email (as the IT department should) and offer a solution.

To solve the problem, they need hands-on access to the victim’s keyboard, usually through a legitimate remote monitoring and management tool like AnyDesk or ScreenConnect.

Obviously, this is all a ruse to get the victim to hand over access to their device. The same entity sent both the spam emails and the Teams messages. Sometimes, they even call the victim through Teams, rather than send a message - to make the entire ordeal even more believable.

Arctic Wolf says the key enabler of the whole scheme is the fact that Microsoft Teams ships with external access (federation) turned on by default. That means that, unless the actual IT team changed the default settings in Teams, every employee can receive messages from anyone else with a Microsoft 365 account, even if they belong to an entirely different tenant (dedicated environment within Microsoft's cloud services). Unfortunately, this is not a bug, it’s an entirely legitimate feature that threat actors happily exploit:

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

“This is the feature attackers most frequently abuse,” Arctic Wolf says. “This activity does not exploit any known Teams vulnerability; it abuses a legitimate, default-on collaboration capability.”

## Lock down your Teams

To make matters worse, when they ask for hands-on access, they don’t ask the victim to install any special software. In most cases, they just ask them to bring up Quick Assist, a tool that’s built directly into Windows, signed by Microsoft, and thus requires no installation. All victims need to do is send over a six-digit code and they’ve handed over the keys to the kingdom.

What happens after that is anyone’s guess. The researchers saw the attackers then installing a commercial RMM tool such as AnyDesk or ScreenConnect to gain a separate control channel, and make sure they retain access even if the Quick Assist one is revoked. They would then map out the target IT network and do as much reconnaissance as possible, likely in preparation of a ransomware or malware attack.

Defending against these kinds of attacks starts with locking the proverbial doors on Teams. “Most organizations have no legitimate need for open, any-tenant external chat,” Arctic Wolf says. “Per Microsoft’s guidance in Manage external meetings and chat with people and organizations using Microsoft identities, move from “allow all” to an allow-list of trusted organizations.”

The second crucial step is educating the employees. Everyone should be made aware of the fact that just because a message came from Teams, it doesn’t mean it’s legitimate. Same goes for an audio call, or an email.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
