---
title: This Halloween, make sure your sensitive data Is wearing a mask
source_url: https://www.techradar.com/pro/this-halloween-make-sure-your-sensitive-data-is-wearing-a-mask
source_site: TechRadar UK
source_slug: techradar-uk
description: Protecting sensitive data as AI access expands
image: https://cdn.mos.cms.futurecdn.net/mfPaYGQmks2VALWFFBnSej-2000-80.jpg
published: '2026-11-02T00:00:00Z'
scraped_at: '2026-11-02T11:00:05Z'
categories:
- Technology & Software
people: []
locations:
- AI
organisations:
- AI
- DSPM
- Future plc
- TechRadar Pro
- TechRadarPro
- Thales
---

![A robot hand touching a locked digital shield blocking a human from accessing data](https://cdn.mos.cms.futurecdn.net/mfPaYGQmks2VALWFFBnSej-1920-80.jpg)
![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png)

If you work in cybersecurity for long enough, you learn that we really love an analogy or a metaphor and come October you can barely move for talk of security nightmares, cyber monsters and threats lurking in the shadows.

I enjoy a good analogy as much as anyone, but there’s one Halloween comparison I don't hear very often. And, for data security at least, I think it might be the most useful one right now: the mask.

A mask doesn't make what's underneath disappear. It simply means you don't have to reveal its true identity to everyone who encounters it, and that’s what we’re trying to achieve with sensitive data.

VP of Data Security Products at cybersecurity company Thales.

Developers need data to test applications, analysts need it to find patterns, and AI tools and agents increasingly need access to enterprise information to do useful work. But needing to use this data isn't necessarily the same as needing to see every sensitive value it contains.

That's precisely where data masking comes in. By replacing sensitive information with realistic but unusable values, organizations can preserve the usefulness of data without unnecessarily exposing what's underneath.

With AI dramatically increasing where data can travel, who can find it and what can act upon it, that distinction is becoming much more important.

## A disguise with a serious purpose

At its core, data masking replaces sensitive information with realistic but unusable values. The resulting dataset can retain characteristics necessary for development, testing, analytics and other business processes without unnecessarily exposing the sensitive information underneath. Think of it as a Halloween costume with a security purpose; the data can still show up to the party without revealing its true identity.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

That distinction matters because protecting data shouldn't simply mean preventing people from using it. Modern businesses depend upon being able to analyze, test against and increasingly train or ground AI systems in enterprise information. Instead, the question should be: does this person, application or AI system actually need the original sensitive value to perform this task?

A developer testing an application may need representative customer data, for example, but not necessarily genuine customer identities. An analytics workload may need to preserve relationships and patterns without revealing every account number or personal identifier.

If the real value isn't required, exposing it creates risk without creating corresponding business value.

Masking removes that unnecessary exposure. Depending on the use case, organizations can also use techniques including tokenization and encryption. The important principle is to match protection to how the information needs to be used rather than defaulting to exposing raw sensitive data.

## You can't mask what you can't find

There is an obvious complication: before deciding what should wear a mask, businesses need to know where their sensitive information is.

That remains surprisingly difficult.

The 2026 Thales Data Threat Report found only 34% of surveyed organizations had complete knowledge of where their data was stored. Only 39% said they could classify all of it. Meanwhile, the average organization reported using seven different tools for data protection and monitoring.

Cloud infrastructure compounds the problem. Information can be copied into data lakes, SaaS platforms, development environments and backups. Unstructured documents can contain sensitive information nobody realized was there. Applications created years after the data was collected can suddenly gain access to it.

AI makes that visibility problem considerably more consequential because finding information is precisely what these systems are becoming very good at.

This is where data security posture management (DSPM) becomes important. Rather than treating data security purely as a question of defending infrastructure, DSPM starts with the data itself: discovering and classifying sensitive information and understanding where it resides, who or what can access it, how it is being used and whether its protection is appropriate.

Once an organization identifies unnecessarily exposed sensitive data, it can decide whether access should be removed, restricted or protected using controls such as masking, tokenization or encryption.

## AI data: trick or treat?

This becomes particularly important as businesses progress from experimenting with generative AI towards embedding AI into everyday operations.

AI applications need data. Agents may need considerably more of it because they are designed not simply to generate content but to retrieve information, make decisions and potentially take actions across different systems.

The security implications are already becoming visible. The same research found 61% of organizations reported their AI applications were being targeted by attackers, with sensitive data the leading target. Rapid change within the AI ecosystem was also the most commonly cited AI security risk.

The important question, however, isn't simply whether AI can be secured. Organizations also need to ask a more fundamental question:

## What data are we allowing AI to see in the first place?

Giving an AI application access to a database shouldn't automatically mean giving it access to every raw sensitive value contained within it. The same least-privilege principle used for human identities can be applied to data: expose what is necessary for the task and protect what isn't.

That could mean masking personal information before it reaches development and testing environments. It could mean tokenizing particularly sensitive values used by an application. It could mean encrypting information and tightly controlling which identities can decrypt it. And in some circumstances, it should mean preventing an AI system from accessing a dataset altogether.

## Don't make AI security harder than it needs to be

There is a tendency to treat AI security as an entirely new discipline requiring entirely new answers.

Some risks certainly are new. But one of the most useful things organizations can do is apply established data-security principles to this new environment.

Know where sensitive data resides. Understand its context. Minimize unnecessary access. Protect the underlying value according to how it needs to be used. And continually reassess those decisions as applications and AI systems change.

AI may dramatically increase how much value organizations can extract from their data. It doesn't follow that every system extracting that value needs to see everything underneath.

Halloween only comes around once a year. For sensitive data, however, having the option to wear a convincing mask year-round is becoming a non-negotiable.

*This article was produced as part of* * TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:* * [https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)
