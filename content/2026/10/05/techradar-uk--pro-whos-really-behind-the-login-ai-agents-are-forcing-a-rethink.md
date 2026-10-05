---
title: Who's really behind the login? AI agents are forcing a rethink
source_url: https://www.techradar.com/pro/whos-really-behind-the-login-ai-agents-are-forcing-a-rethink
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-05T14:28:43Z'
published: '2026-10-05T00:00:00Z'
description: AI agents are exposing gaps in digital trust
image: https://cdn.mos.cms.futurecdn.net/6t9Lsf3QWte55CdyiDs97L-2560-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people: []
locations:
- UK
organisations:
- AI
- DVS Trust Framework
- Digidentity
- Digital Verification Services
- Future plc
- TechRadar Pro
- TechRadarPro
---

![A robot&#039;s hand typing on a laptop keyboard](https://cdn.mos.cms.futurecdn.net/6t9Lsf3QWte55CdyiDs97L-1920-80.jpg)
![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png)

Digital trust has rested on the simple assumption that behind every login or decision, there is a person. Passwords and multi-factor authentication were built to confirm that whoever was asking had the right access.

They were never built to answer a question that AI agents are now making unavoidable: not just whether you can get in, or even who you are, but who authorized you to act, what exactly you can do, and for how long.

Break it down, and there are really three separate checks. Authentication: can you access this? Identity: who are you? Authority: who authorized you to do this, what can you do, and for how long? Most of today's infrastructure was built to answer the first two. Agents are what make the third one impossible to ignore, and it's where the interesting problem now sits.

Country Manager at Digidentity.

AI agents are completing transactions and handling admin tasks that used to require a person, often with minimal oversight. Many of the systems checking who's on the other end of a request weren't built to tell a person from an agent, or a legitimate agent from an unauthorized one. They confirm that someone, or increasingly something, holds the right credentials, not whether it has authority for the action it's taking.

The UK has spent the past couple of years building the infrastructure to answer the identity part of this equation. The Data (Use and Access) Act has put Digital Verification Services (DVS) on statutory footing.

Some use cases are going further still, introducing mandatory identity verification for directors and people with significant control. That's progress. But as agents start acting more inside business workflows, a second question is emerging that this infrastructure wasn't designed to answer: not who someone is, but who is acting, and with what authority.

## Identity is only the first check

For businesses, proving a person's identity has always gone hand in hand with checking what they are authorized to do. Take an employee approving a payment on a company's behalf: the organization relying on that action needs to know not just who they are, but whether they're currently entitled to do it. Financial services and healthcare already layer eligibility and role checks on top of identity verification, because identity alone doesn't tell you what someone is allowed to do.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

AI agents make that distinction unavoidable everywhere else, too. Identifying the agent behind a request doesn't show who authorized the action or whether it falls within the permission originally granted. The infrastructure built so far is much stronger on identity verification than on applying delegated authority, and that gap will widen as more of what businesses do is offloaded to agents.

## Minimum necessary authority

The same discipline that good identity design applies to documents should apply to authority: ask for, and grant, only what a transaction actually needs. An agent completing a task should be able to prove it holds a specific, limited mandate for that task, not standing access to everything behind it.

Broad, standing access is easier to build, but it means a single compromised or mis-scoped agent can do far more damage than a narrowly scoped one ever could.

## Preparing for delegation

So how should businesses actually close this gap? The starting point isn't a new verification step. It's moving that check earlier, so authority is confirmed before an agent acts rather than discovered after something's gone wrong. An organization should give an agent a specific, limited job rather than a copy of a person's own access, and keep a clear record of who granted that authority and when it can be pulled.

For any agentic action, a business should be able to answer five questions: Who, or what, is acting? Who authorized it? What can it do? Under what constraints? And is that authority still valid? It's a simple test, but it's a useful one, and it maps closely onto the ‘on-behalf-of’ (or OBO) delegation models already used in identity standards, which is a promising foundation to build on rather than starting from scratch.

Without those answers, a mis-scoped agent could quietly approve a payment it was never meant to touch. Waiting for a regulator to define the standard first only leaves that exposure open for longer.

## Where the framework needs to catch up

The government's role here too is to extend what already exists rather than build new infrastructure from scratch. The DVS Trust Framework already recognizes delegated authority when a person acts on behalf of somebody else or an organization. What it doesn't yet address is how that same principle should apply when the delegate is software, and the UK now needs to work out how its existing delegated-authority thinking extends to that case.

Whatever shape that takes, an agent needs to be able to present a machine-verifiable mandate: who authorized it, what it can do, under what constraints, for how long, and whether that authority is still valid. Digital wallets are one plausible home for that mandate, sitting alongside a person's or organization's verified credentials so it can be checked or revoked.

They're not the only answer, but they point at the kind of infrastructure this problem needs, and the UK has a narrow window to work it out before agent deployments outpace the systems meant to govern them.

With the Data (Use and Access) Act, the DVS Trust Framework is already laying much of the groundwork for secure, reusable digital identity, the UK has an opportunity to get ahead of this shift, extending principles it has already established rather than inventing new ones.

In the near future, trust online will no longer depend on whether something can pass a login. It will depend on whether we can prove who, or what, is really acting behind the screen, on whose authority, and for how long.

*This article was produced as part of* * TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:* * [https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)
