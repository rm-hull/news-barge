---
title: A worrying ChatGPT bug let strangers read Gmail messages via a hidden cross-account
  channel
source_url: https://www.techradar.com/pro/security/a-worrying-chatgpt-bug-let-strangers-read-gmail-messages-via-a-hidden-cross-account-channel
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-09T19:14:55Z'
published: '2026-09-09T00:00:00Z'
description: Researchers say it's worth an investigation, in spite of caveats
image: https://cdn.mos.cms.futurecdn.net/PB5R692ChqyHSzKEtqDyYe-2560-80.jpg
---

![ChatGPT app](https://cdn.mos.cms.futurecdn.net/PB5R692ChqyHSzKEtqDyYe.jpg) 

- **Check Point Research exposed coerced insider flaw in ChatGPT’s agent architecture**
- **Containers shared metadata via internal service, enabling cross‑account prompt injection and data theft**
- **OpenAI closed the path, but CPR warns similar risks may exist in other AI platforms**

ChatGPT’s AI agents were allowed to pull sensitive data from one account shared with an entirely different account because, colloquially speaking, all agents used to walk down the same hallways, experts have warned.

A new report from security experts Check Point Research (CPR) dubbed the flaw “coerced insider”, since it revolves around persuading the agent instead of abusing a vulnerability.

## Coerced insider

When an AI agent is given a task that needs code execution, it handles that task in an isolated container which also sometimes needs to install software. To enable that, without giving containers direct internet access (which would be too risky), OpenAI routes those packages through an internal JFrog Artifactory instance. As a separate security contingency, containers from different accounts cannot talk between themselves.

However - they can reach the same internal service (our proverbial hallways), which exposes an item management feature that lets the containers attach text or binary properties to a repository item. As a result, any container can read back the properties written by any other container.

“Check Point Research confirmed the isolation gap directly: a property written from one account’s container was fully readable from a different account’s container moments later, with data too large for one property simply split into chunks and reassembled on the other end,” the researchers explained.

“The package delivery metadata effectively became a shared clipboard between containers that were supposed to be walled off from one another.”

From there, the exploit turns into your usual, off-the-shelf prompt injection. The only difference is that the malicious prompt is not delivered directly to the victim, but rather left in the hallways, and the results are not shared with the attackers directly, but rather left in those same proverbial hallways, too.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The attacker then delivers a prompt or a shared conversation that instructs the agent to check the same storage during its next ordinary reply. The agent checks, sees the malicious instructions, executes them, all the while replying to the victim’s question in the usual manner. The victim is oblivious to the fact that data theft is taking place in the background.

## What kind of information can be stolen?

But this is just half of the equation. How destructive this attack ends up being still depends on the amount of data being shared with the victim agent.

The bare minimum is the information shared while chatting to the agent. It then grows with every connected app: Gmail, Google Drive, Microsoft Teams, GitHub, and similar. “In Check Point Research’s demonstration, ChatGPT retrieved the victim’s email data through their connected Gmail account and delivered it to the attacker’s session, all within a single ordinary turn,” CPR stressed.

The good news is that you’ll likely never be exposed this way, at least not via ChatGPT. CPR says it disclosed the findings to OpenAI, who then confirmed that the specific internal Artifactory instance identified in the research has been commissioned. In other words, the hallways attack path has been closed.

The bad news is that this doesn’t automatically mean everyone’s safe. This particular path might be closed, but the architectural pattern behind the flaw could be present in other platforms, CPR warns.

“Any AI assistant that operates inside an organization’s trust boundary, holding credentials, running code, and reaching connected services, can become what Check Point Research calls a coerced insider,” the report states. “The model itself does not need to be malicious. It only needs to be persuaded, through text it was never meant to trust, to use access that was granted for entirely legitimate reasons.”

Going forward, businesses are advised to learn which AI tools their employees are using, and what those tools are connected to. Then, they should govern what AI tools and agents are allowed to do, treating all of their actions (not just output) as something that needs to be monitored.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
