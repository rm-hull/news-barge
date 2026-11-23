---
title: 'Sovereign AI: stop mapping, start proving'
source_url: https://www.techradar.com/pro/sovereign-ai-stop-mapping-start-proving
source_site: TechRadar UK
source_slug: techradar-uk
description: Sovereignty is proven mobility, not just data location
image: https://cdn.mos.cms.futurecdn.net/gMavKmnr8ZGuzV56Abc7DM-2560-80.jpg
published: '2026-11-23T00:00:00Z'
scraped_at: '2026-11-23T12:21:19Z'
categories:
- Technology & Software
- Business & Entrepreneurship
people: []
locations:
- AI
- Britain
- Europe
- UK
organisations:
- AI
- Amazon
- CTO
- Center for New American Security
- Competition and Markets Authority
- DORA
- EMEA & LATAM
- EU
- Future plc
- Microsoft
- Neocloud
- NetApp
- OpenAI
- Prudential Regulation Authority
- Stargate UK
- TechRadar Pro
- TechRadarPro
- VP Solutions Engineering
---

![A digital representation of the globe with digital lines connecting parts of it, below binary figures](https://cdn.mos.cms.futurecdn.net/gMavKmnr8ZGuzV56Abc7DM-1920-80.jpg)
![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png)

Ask most IT leaders where their sovereign AI strategy starts, and the answer is usually a location. If the data sits inside the UK, or inside a particular cloud region, control is assumed and the compliance box gets ticked. It's a reasonable starting point, but it shouldn’t be the end of the journey.

Location matters. Regulated industries cannot ignore residency requirements. But treat sovereignty as geography, and you create new limits just as AI workloads become more spread out. This is why 62% of European organizations are seeking sovereign solutions in response to geopolitical uncertainty.

CTO and VP Solutions Engineering, EMEA & LATAM at NetApp.

An enterprise might train a model in one environment, infer in another, and keep its most sensitive data on premises throughout. That's controlled choice: deciding where data lives, where compute runs, and how the two connect without ever losing governance.

## If it can't move, it isn't sovereign

Moving data and workloads is not simple. The deeper a system depends on a provider's native services, the harder that becomes.

Mobility isn't a default; it has to be built in and tested. Without that, sovereignty becomes another constraint. An architecture designed only for residency can struggle when business changes or new regulation arrives. The more useful framing is flexibility under control. Organizations should be able to decide where a given workload runs based on performance, cost, risk, and compliance, while keeping a coherent view of the data, the model, and the decision trail.

This is one reason we're seeing the emergence of Neocloud providers across Europe. They are built for AI workloads, around the assumption that organizations need advanced AI infrastructure without losing control of where data resides and how it moves. Britain has seen just how quickly the capacity promised in one place can slip. Stargate UK demonstrated this: announced with up to 8,000 GPUs via Nscale, it was paused by OpenAI in April over energy costs and regulation.

And the dependencies do not stop at where compute is hosted. The Center for New American Security looked at 184 government-backed AI projects around the world and found most still depend on at least one foreign tech partner. Building your own data center to avoid relying on a foreign cloud provider doesn't remove that reliance. It just moves it somewhere else, maybe the chips, maybe the servers, maybe the software underneath.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

True sovereignty isn't about doing everything yourself. It's about knowing where you still rely on someone else, and being able to prove you can manage that, instead of pretending it’s not needed.

## The hidden cost of every extra copy

An organization can meet a residency requirement and still create a new problem: data may need to be copied into each environment where it is used. Every additional copy brings its own storage costs, lifecycle decisions and governance burden. I call this the “copy tax”. At petabyte scale, the multiplier matters more than the unit price.

The risk of dependency is not new. A shared platform can simplify operations and offer attractive economics, but it can also make an organization increasingly reliant on one provider. If ownership, licensing or commercial priorities change, leaving may prove slower and more expensive than expected.

The same risk applies to AI estates built around a provider’s native storage format, with potentially much larger datasets to move. The UK’s Competition and Markets Authority has highlighted a related challenge in the cloud market, concluding that egress fees and technical barriers discourage customers from switching. Microsoft and Amazon have since set out voluntary actions on egress charges and interoperability.

Meeting a residency requirement is important, but it does not by itself show that an organization has meaningful choice. The better test is whether you can move a production dataset to another environment, maintain appropriate governance and protection, and demonstrate how long the move takes and what disruption it causes.

That calls for a consistent data layer across environments, so governance and protection remain in place as data moves. The aim is not to eliminate every copy, but to ensure that any copy is necessary, governed, and manageable. Therefore, moving data does not mean losing control of it.

## Assertion is no longer enough

Since DORA came into force in January 2025, financial institutions within its scope have faced greater scrutiny over whether they can recover from a segregated copy and, if necessary, exit a provider. Although DORA is EU law, the regulation also matters to UK firms with operations in the EU.

The Prudential Regulation Authority has expected UK banks and insurers to maintain tested exit plans for material outsourcing since 2022, with the most up-to-date iteration effective March 2027. An exit path that exists only on paper doesn't count. A firm must be able to show where sensitive data is held, how it is protected, and whether operations can be restored from an immutable, segregated copy.

Object storage alone is not a ransomware safeguard; recent large-scale retail incidents have underlined the consequences of gaps in recovery planning. Demonstrating these controls can support both regulatory confidence and business agility. When any one of them is missing, the organization eventually pays for it later, in narrower choices or slower response to change. AI is making these trade-offs harder to ignore because workloads that once lived in a single environment now span multiple locations and trust domains.

## The takeaway for IT teams building AI infrastructure now

None of this means sovereignty is a box you can never tick. It simply means it's a capability you must keep proving, not a status you declare once. As AI workloads multiply across on-premise cloud and neocloud environments, the organisations under least pressure won't be the ones with the tidiest data map. They'll be the ones that prove a production dataset can move, recover, and stay governed wherever it ends up.

For IT and infrastructure leaders evaluating AI platforms today, that's the real due diligence question to ask any vendor: not just where does our data live, but can we prove we could move it and would anything break if we did?

Sovereignty should provide flexibility under control, not simply put a pin on a map.

*This article was produced as part of* * TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:* * [https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)
