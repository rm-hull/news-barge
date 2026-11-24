---
title: Meta Muse can be hacked to access user private chats using just a single malicious
  web page
source_url: https://www.techradar.com/pro/security/meta-muse-can-be-hacked-to-access-user-private-chats-using-just-a-single-malicious-web-page
source_site: TechRadar UK
source_slug: techradar-uk
description: Researchers found a chain of flaws that could be exploited
image: https://cdn.mos.cms.futurecdn.net/7JHgomMZui7pUWLxTnysHM-1920-80.png
published: '2026-11-24T00:00:00Z'
scraped_at: '2026-11-24T02:10:43Z'
categories:
- Technology & Software
people:
- Muse
locations: []
organisations:
- Meta
- Muse AI
- NebuSec
- Sentinel
- TechRadar Pro
---

![Meta Muse for Small Business](https://cdn.mos.cms.futurecdn.net/7JHgomMZui7pUWLxTnysHM-1920-80.png)

* **Researchers found a chain of vulnerabilities in Meta’s Muse AI assistant that could expose conversations, stored memories, and cloud credentials**
* **A crafted webpage enabled code execution, security-control bypasses, and potential access to sensitive user data**
* **Meta patched all reported issues before disclosure, with no evidence the flaws were exploited in the wild**

Meta’s Muse AI assistant could have been broken into using a chain of vulnerabilities, experts have warmed.

There, malicious actors could have exfiltrated all private conversations and stored memories, bypass security controls, and even exfiltrate credentials stored on the cloud machine running the AI assistant.

Security researchers NebuSec found a way to break into Muse and published an in-depth report detailing their findings. The researchers said they responsibly disclosed their research to Meta, which plugged all of the discovered holes by the time of publication.

## What is Muse and how was it breached?

Muse is a cloud-hosted personal AI assistant designed to carry out tasks on users’ behalf, by interacting with online accounts and services they connect it with. The tool operates inside a dedicated virtual machine (VM) for each user, with several security measures designed to prevent the assistant from accessing information and resources beyond its intended permissions.

One of these measures is a credential management system designed to keep authentication details away from the agent itself. Another one is called Sentinel - a service that monitors outgoing traffic. Now, NebuSec says they found a way to bypass these protections and to do that, all they needed was a specially crafted webpage.

To generate PDFs and documents, muse uses the Chromium browser (the same one upon which Chrome, Edge, and many others are built). By getting the assistant to export a malicious webpage, the researchers managed to achieve code execution inside its runtime environment. Then, they leveraged a previously discovered weakness in the way Sentinel handles outgoing requests, which allowed them to extract conversation history and stored memories, and send them all to an external server - without the victim knowing, or giving consent, to anything.

This same attack also allowed them to modify everything the user had stored with Muse, including conversation history. In other words, they could change what the users had told Muse to remember about them.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Finally, using an automated exploit generation framework, NebuSec developed Linux kernel exploits that allowed them to escape the agent’s runtime container and obtain root privileges on the underlying user VM. That gave them access to login credentials and other sensitive resources that were otherwise inaccessible to Muse.

It also bypassed Sentinel’s restrictions, meaning the researchers were allowed to send outgoing network communications.

## What can companies do?

This was all done in a contained environment, though. There were no reports of the flaws being actually abused in the wild, and since Meta patched it server-side, chances are, there will never be any. It’s also worth mentioning that the compromise remained limited to the individual user’s virtual machine - the researchers did not demonstrate pivoting to the underlying hypervisor host or accessing any other users’ environments.

Businesses and individuals are connecting AI agents to more and more services - emails, calendars, social media accounts - without setting up proper guardrails or, in many cases, even understanding what’s at stake. Cybercriminals, on the other hand, know very well how to take advantage of it.

"This access makes agents useful. But it also makes them attractive targets,” NebuSec explains.

The researchers warned that security measures must account for what happens when an attacker manages to compromise parts of an AI platform: "Security controls must do more than prevent unauthorized actions by the agent itself,” they said. “They must also protect the credentials and information the agent can access if one of its underlying components is compromised."

NebuSec reported all their findings to Meta, and the company apparently patched all of the exploits that were discovered. It did not publicly disclose, or acknowledge, any of it, though.

*Via* * The Hacker News*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
