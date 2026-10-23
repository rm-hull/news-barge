---
title: Your data is in Europe. Your technology still isn’t sovereign
source_url: https://www.techradar.com/pro/your-data-is-in-europe-your-technology-still-isnt-sovereign
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-23T11:36:12Z'
published: '2026-10-23T00:00:00Z'
description: Technical autonomy is harder than server geography - but much more important
image: https://cdn.mos.cms.futurecdn.net/zwBWPNAfpJdnNkfJY3wUKM-2560-80.jpg
categories:
- Technology & Software
people: []
locations:
- Frankfurt
- New York
- Paris
- US
- United States
organisations:
- AI
- Anthropic
- Cycloid
- EU
- Future plc
- GDPR
- IDP
- Internal Developer Platform
- TechRadar Pro
- TechRadarPro
---

![A data center in a blue light](https://cdn.mos.cms.futurecdn.net/zwBWPNAfpJdnNkfJY3wUKM-1920-80.jpg)
![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png)

On 12 June, thousands of organizations discovered an uncomfortable truth about the AI tools they had started building into their businesses. They didn’t have control over it.

The US government issued an export-control directive affecting two Anthropic models. Anthropic responded by disabling them for every customer. The restrictions were later lifted, but that is hardly reassuring. Access disappeared and then reappeared because of decisions customers neither made nor controlled.

Founder of Cycloid.

It’s a wake-up call that many claimed that they had after the Cloudflare outage… or the CrowdStrike outage… or Meta’s… or AWS’… or so on… And yet we were met with predictable surprise amongst an industry that has been so afraid of having potentially uncomfortable conversations around digital sovereignty.

We often talk about data-center locations, regional availability and compliance certificates. We discuss whether the server sits in York or New York, then congratulate ourselves for making a sovereign choice.

But if a foreign government can remove your service, an outage can take down your entire business, a vendor can change your operating model or a proprietary API makes migration economically impossible, the location of the server is almost beside the point.

## Data residency is a comfort blanket

Putting a server in Paris does not magically make your architecture French. The server is only one part of the system and it may not even be the most important part. Sovereignty is about control over the complete operational chain. That includes the infrastructure, of course, but also the tools used to provision it, access it, deploy software to it and keep it running.

A business can satisfy its data-residency requirements while remaining completely dependent on foreign technology. A compliance box is checked and the organization believes it has reduced its risk because the data has moved, but the levers governing that data remain in somebody else’s hands.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The control plane matters. The developer tooling matters. The source-code platform, identity provider, orchestrator and AI assistant all matter. If any one of them becomes an immovable dependency, the organization is less sovereign than it thinks.

As an industry, we have focused on the physical location of servers because it is easy to understand. Technical autonomy is much harder, and it requires organizations to examine dependencies they have spent years pretending are somebody else’s problem.

## Enterprises are stuck in a legal sandwich

If technical lock-in wasn’t bad enough, the legal situation makes it worse. Modern enterprises increasingly find themselves trapped in a legal sandwich, caught between rules that apply simultaneously but do not always point in the same direction.

Weave Intelligence demonstrates the example of the friction between the US CLOUD Act and the EU’s GDPR.

The CLOUD Act can require US-based technology companies to disclose data under their control, even when that data is stored outside the United States. GDPR, meanwhile, places strict conditions on transfers of European personal data to third countries and access by foreign authorities.

This creates an obvious problem for a European company using a US-owned technology provider. The data might be sitting in Frankfurt, but the company operating the service can still be subject to US law. If it receives a valid demand from the US authorities, the provider may face obligations in one jurisdiction that create serious legal and regulatory risks in another.

This is not just a US-EU issue of course, but rather an example of where residency is often second to complex legal definitions of data ownership. And whilst enterprises cannot solve this international law through architecture, they can stop making the problem worse by building every critical workflow around one provider, one jurisdiction and one set of proprietary services.

The legal sandwich becomes much harder to swallow when there is no realistic way to change what is inside it.

## If you cannot leave, you are not sovereign

Digital sovereignty means retaining the practical ability to change provider, jurisdiction or deployment model without bringing the business to a halt.

Managed services allow teams to build quickly without worrying about every part of the underlying infrastructure. But each provider-specific service creates another dependency, and each dependency makes the exit door slightly smaller. This is the genius, and the true cost of the hyperscaler.

The test is very straightforward. If your provider disappeared tomorrow, could your teams continue building and operating software?

If the answer exists only in a 40-page exit-strategy document that nobody has tested, the answer is no. A genuine exit strategy must be executable and the business must be able to shift workloads, change providers or bring critical capabilities on premises without redesigning how every development team works.

## Own the layer between developers and infrastructure

To achieve genuine technical autonomy, organizations must decouple software delivery from the infrastructure underneath it. This is the strategic role of the Internal Developer Platform.

An IDP provides a consistent layer between development teams and the different environments where their software runs. Developers follow the same golden paths to build, test and deploy, whether the destination is a local cloud provider, a global hyperscaler or an on-premise environment.

The infrastructure can change without forcing every developer to change how they work. More importantly, the organization retains control over the workflows that keep software moving. Deployment logic, policies, configurations and operational knowledge are not welded to one infrastructure vendor.

This turns portability from a paragraph in a risk document into a capability that can be exercised and tested. Organizations can move workloads between environments during normal operations, identify the dependencies that remain and address them before a crisis arrives.

## Stop claiming sovereignty. Prove it.

Real sovereignty has to be designed, tested and maintained. Organizations should regularly move workloads between environments, test whether critical tools can run independently and expose the dependencies hiding behind their architecture diagrams.

Because the first time you test your sovereignty should not be during an outage, a legal dispute or a geopolitical crisis.

*This article was produced as part of* * TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:* * [https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)
