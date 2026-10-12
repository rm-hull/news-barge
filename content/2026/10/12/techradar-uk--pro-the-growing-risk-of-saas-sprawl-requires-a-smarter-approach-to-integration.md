---
title: The growing risk of SaaS sprawl requires a smarter approach to integration
source_url: https://www.techradar.com/pro/the-growing-risk-of-saas-sprawl-requires-a-smarter-approach-to-integration
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-12T18:59:54Z'
published: '2026-10-12T00:00:00Z'
description: SaaS sprawl expands attack surfaces, demanding increased security visibility
image: https://cdn.mos.cms.futurecdn.net/JpXukHGqkZ8gapEzDQNqRW-1920-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people: []
locations:
- Flowise
organisations:
- AI
- Future plc
- GitHub
- OAuth
- Obsidian Security
- SaaS
- Salesforce
- ServiceNow
- TechRadar Pro
- TechRadarPro
---

![Concept art representing cybersecurity principles](https://cdn.mos.cms.futurecdn.net/JpXukHGqkZ8gapEzDQNqRW-1920-80.jpg)
![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png)

As organizations race to adopt SaaS applications and AI-powered tools, shadow integration has become a more dangerous and often overlooked entry point for modern breaches. Every new application introduces its own identities, roles, and permissions, while every third-party integration creates another trusted pathway into enterprise systems.

There may already be hundreds of agents currently inside the average enterprise, and these deployments are not slowing down. Employees routinely authorize third-party OAuth applications that gain persistent access to business-critical systems, often with broad permissions that remain long after they're needed. At the same time, AI agents and automated workflows are being embedded into critical SaaS platforms like Salesforce, ServiceNow, Workday, and Slack.

CEO of Obsidian Security.

Each new connection expands the attack surface, yet few organizations have a complete understanding of how these trusted relationships interact, and cyber criminals have noticed. In fact, SaaS breaches have increased by 300%. These identities often operate with elevated privileges, which makes them attractive targets if compromised.

The threat landscape is expanding faster than traditional security models can track. Without simple, trusted controls that can instantly govern SaaS applications and AI agents, organizations are left with systems that can access sensitive data, interact with business systems and take actions on users’ behalf.

To mitigate the threats, security leaders must be able to know at any moment, which third-party apps are connected to their environment, what those connections can reach, and whether they're behaving normally, rather than finding out after a security incident.

## Where SaaS innovation creates security risk

As SaaS sprawl grows, IT teams are dealing with fragmented signals across hundreds of applications, making it difficult to understand what’s connected and where access actually lies.

This threat landscape is expanding rapidly. With projections of over one billion agents in enterprise environments by 2028, organizations are deploying these tools faster than any manual review process. As agents gain access to business systems and integrations, traditional approaches to managing permissions and access are no longer sufficient.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Low-code, no-code and AI platforms are making it easier for anyone to build and deploy autonomous agents, often without security or oversight built in. These agents can inherit real access to business systems and data, while organizations still lack a consistent way to discover them, trace their privileges and enforce guardrails across the SaaS environment.

Recent security incidents illustrate this evolving threat. For example, Obsidian Security disclosed a one-click remote code execution vulnerability in Flowise (CVE-2026-40933), an open-source platform for building AI agents and LLM workflows with more than 52,000 GitHub stars.

The research found that an attacker could fully compromise a server by persuading an authorized user to import a malicious chatflow. The risk includes a combination of multiple factors: a trusted user importing a shared workflow, permissions that allowed custom MCP configurations, the ability to launch external processes, and access to connected credentials, APIs, databases, and cloud services. Together, they created a path to full environment compromise.

Traditional solutions don't discover these integrations, can't evaluate their permissions, and have no visibility into the cross-app activity that happens between connected systems. But that’s increasingly how attackers are escalating access and moving laterally.

## The role of visibility across SaaS ecosystems

To maintain the speed of innovation while keeping a security-first approach, IT teams need visibility across users, applications, OAuth grants and permissions so they can understand risk as it changes, not after an action has already taken place. They need to be able to answer questions such as, “Who still has admin rights across multiple apps?” or “Which inactive accounts still have effective access?”.

This is where approaches such as knowledge graphs can offer a different way to understand SaaS risk. A knowledge graph connects entities such as people, accounts, tokens and resources, showing how they relate to one another and revealing context that might otherwise be missed.

Rather than forcing every SaaS application into a standardized permission model, it captures how users, roles, permissions and integrations actually interact across systems, allowing security teams to understand who has access, what they can reach and how that access was granted.

With that foundation, security becomes adaptive rather than restrictive. High-risk or unusual integrations can be automatically flagged or constrained based on factors such as agent behavior or access patterns, while trusted activity can move forward with minimal friction. This allows IT teams to maintain strong control over the SaaS environment without slowing down legitimate business activity.

OAuth and API integrations make this visibility even more important. They can access large amounts of data and connect directly to critical systems, often without the same oversight applied to human users. Traditional tools such as SIEMs and CASBs can struggle to capture this risk because they were largely designed around human activity and security events.

But SaaS risk increasingly lives in the relationships between users, applications, permissions and integrations. A dormant administrative account may appear harmless until it is connected to an overprivileged OAuth integration or an AI workflow that inherits unnecessary access.

The future of SaaS security won't be defined by collecting more alerts or deploying more point solutions. It will be defined by bringing evidence to show where guardrails are needed, who has access, what they can reach, how that access was granted, and how those relationships change over time. Ultimately, the leaders that can turn this visibility into informed control will be best positioned to embrace SaaS and AI innovation for the business.

*This article was produced as part of* * TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:* * [https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)
