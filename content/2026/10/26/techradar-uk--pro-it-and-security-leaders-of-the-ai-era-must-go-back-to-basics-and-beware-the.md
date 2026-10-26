---
title: IT and security leaders of the AI era must go back to basics and beware the
  hype
source_url: https://www.techradar.com/pro/it-and-security-leaders-of-the-ai-era-must-go-back-to-basics-and-beware-the-hype
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-26T12:51:52Z'
published: '2026-10-26T00:00:00Z'
description: AI hype distracts from foundational identity security risks and controls
image: https://cdn.mos.cms.futurecdn.net/UjSNcAZ5SebctebKAMQNVF-2560-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Hey
locations:
- AI
organisations:
- AI
- AWS
- CIEM
- CIO
- CIOs
- CISO
- CISOs
- Capital One
- Cloud Infrastructure Entitlement Management
- DBIR
- Future plc
- Hugging Face
- NHI
- NHIs
- SVP Strategy
- Saviynt
- TechRadar Pro
- TechRadarPro
- Verizon
---

![Cybersecurity ensures data protection on internet. Data encryption, firewall, encrypted network, VPN, secure access and authentication defend against malware, hacking, cyber crime and digital threat](https://cdn.mos.cms.futurecdn.net/UjSNcAZ5SebctebKAMQNVF-1920-80.jpg)
![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png)

CISOs and CIOs should not just chase the latest hype around AI that can escape sandboxes and morphing security threats, but bet on tried and true ROI of identity security.

It’s demonstrably true that the information security scene is transforming as agentic AI accelerates operational speed and potentially exposes new attack surfaces. Most AI providers have reported their latest generation models are so powerful that they are capable of escaping sandboxes and hacking organizations. Regardless if you believe this is hype, truth or genius marketing, what matters is this: information security leaders should rigorously check the basics of their discipline.

SVP Strategy for Saviynt.

Yes, CISOs need to be ahead of the curve but this can’t be at the cost of dropping the ball on security and identity essentials. I say this because, all too often, even in sophisticated and otherwise mature enterprises, the latest breaches are still abusing the lack of essential controls, via credentials and permissions the agents should never have been able to reach.

And sometimes, thought leaders and experts attempting to understand and communicate rapid technology changes, are creating more confusion and distracting from first principles.

‘AI washing’ – the practice of overstating the importance of AI in a product, project or strategy – is real. We need to do more to demystify data security and separate hype from reality and place a higher value on specificity when we talk about risks.

## The identity challenge

The industry's instinct to frame this as an "AI security" problem is understandable, but it is not actionable. For CISOs trying to reduce real risk, the more precise frame is identity.

For an example of what I’m talking about, consider onboarding. When people join an organization, they are granted privileges based on their needs, seniority and roles. A major part of contemporary information security is about staying on top of identity management, but that’s not easy.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

In hypergrowth, companies hire very quickly. But IT leaders also need to stay abreast of many other people who need access to systems. These include freelancers, consultants, suppliers, auditors and work-experience temporary staff. That gap (unrevoked, over-permissioned, forgotten access) is exactly what autonomous AI agents exploited in the Hugging Face breach earlier this year.

The attack was novel. The underlying vulnerability was not. NHIs and human identities share the same failure mode: access granted, never reviewed, never revoked. That is the identity challenge, and it predates AI by decades.

## A complex puzzle

IT today is complicated. CIOs stay in their roles for between three and five years. CISOs (and security staff generally) are in high demand, and organizations understandably turn to outsourcers for help. It’s easy for basic management disciplines like maintaining identity hygiene to get lost in the mix, such are the comings and goings of personnel.

And things are getting harder. Who owns an AI identity? Not every enterprise employs an identity specialist, so who is in charge when the identity is non-human? The CIO? What about the CISO? HR? How does the chief risk officer fit in?

It’s easy for tasks to fall between gaps. And even if onboarding is immaculate, who is running offboarding and the impacts on identity? The consequences of that question going unanswered are well documented. Verizon's 2026 Data Breach Investigations Report found that exploitation of vulnerabilities has overtaken stolen credentials as the top initial access vector for the first time in 19 years.

But credentials still drove the privilege escalation and lateral movement that followed. A vulnerability opens the door; an unmanaged identity walks through the building unchallenged.

And in the agentic AI era, who will be in charge of managing those NHIs that often have extraordinarily high permissions and license to roam? The Hugging Face breach answered that question in practice: nobody was. One over-privileged, unmonitored non-human identity provided cluster-admin access across two environments the moment it was compromised.

The AI was the intruder. Vulnerabilities have surged as an entry point precisely because AI agents are now extraordinary zero-day discovery engines, finding in hours what took human attackers weeks. But identity remains the common denominator: had proper least-privilege, just-in-time access and NHI governance been in place, the breach would have been contained even after the vulnerability was exploited. You cannot patch your way out of an identity problem.

## Back to basics (and learning from the past)

If I think about a lot of the breaches I’ve seen, a lot of them relate to these seemingly obvious gaps that become chasms. It’s the left- behind orphan credentials, the ‘puppies with two owners’ and other grey areas that cause problems. ‘Hey. I thought you had this?’, people hear… when it’s too late.

To improve, we need to learn from the past, because we all know the famous quote (of uncertain authorship) about those who ignore history being condemned to repeat mistakes.

A relevant analogy here is cloud computing. Some of us lived through the datacenter wave, then the cloud wave hit. The Capital One breach of 2019 (over 100 million records exposed through a misconfigured AWS role) became the defining lesson of that era: cloud created vast new entitlement sprawl, and nobody was governing it. That breach, and others like it, drove the creation of Cloud Infrastructure Entitlement Management (CIEM) to bring least-privilege principles to cloud permissions at scale. AI is the current wave, and the pattern is similar.

Agents are being deployed with extraordinarily broad permissions, credentials are being embedded in pipelines without rotation or scoping, and ownership of who governs those entitlements is unclear. We will need the same focused response we built for the cloud. Not new acronyms, but the same rigorous application of least-privilege, just-in-time access, and entitlement governance, adapted to the new environment. And whatever wave follows AI will present the same challenge again. Identity is the constant.

Every wave reshapes the technology landscape, but the question of who (human or machine) has access to what, under what conditions, and for how long, never goes away. We just keep failing to answer it before the damage is done. If you weren't there, speak to a cloud veteran because so much of security today has to be about assembling teams of all talents. So use them and build consensus with clear allocation of who is responsible for what and a handover plan for when people leave or swap roles.

The current environment is replete with risks. Consider what AI has done to the act of building software: a non-coder like me can now spin up an app or deploy an agent in an afternoon. That is genuinely transformative, and dangerous. The population of people creating software that handles credentials, calls APIs, and interacts with production systems has exploded overnight, and most of them have never thought about identity hygiene in their lives.

Every time you use an LLM, you are storing credentials somewhere. As that population scales, so does the attack surface. We will see an avalanche of badly architected agents and apps built fast, deployed faster, and governed by nobody. It’s easy to offer up credentials to the world just as misconfigured AWS accounts led to major problems a couple of decades ago.

Today, everybody is excited about the abuses of agents running wild. These are hot stories, and yes, we should be concerned. But really, hackers are going to hack, just as they always have, and they will exploit any loopholes we offer up. The Verizon 2026 DBIR showed vulnerabilities are now the number one initial access vector, but identity is what converts a foothold into a catastrophe.

So many foundational security elements remain neglected like storing static credentials in plain sight. We can still do a lot more with Zero-Trust principles and enforcing least privilege to mitigate risks and reduce impacts. The tools exist and the discipline exists. CIEM was built precisely because the cloud created entitlement problems nobody had anticipated, and it worked, for organizations that adopted it seriously.

The same rigor applied to NHI governance and agentic AI today will determine whether the next wave of breach headlines features your organization or your competitor's. Let’s get the basics right and ensure we can walk at the same time as we try to run.

*This article was produced as part of* * TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:* * [https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)
