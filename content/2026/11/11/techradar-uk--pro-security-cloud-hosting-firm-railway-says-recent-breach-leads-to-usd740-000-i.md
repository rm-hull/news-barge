---
title: Cloud hosting firm Railway says recent breach leads to $740,000 in fraudulent
  AI charges
source_url: https://www.techradar.com/pro/security/cloud-hosting-firm-railway-says-recent-breach-leads-to-usd740-000-in-fraudulent-ai-charges
source_site: TechRadar UK
source_slug: techradar-uk
description: A zero-day in a cloud provider's infrastructure granted attackers access
  to paid AI models
image: https://cdn.mos.cms.futurecdn.net/j5YMwZuuKnvAXLyKBEmDrb-970-80.jpg
published: '2026-11-11T00:00:00Z'
scraped_at: '2026-11-11T19:36:42Z'
categories:
- Technology & Software
- Business & Entrepreneurship
people: []
locations:
- Railway
- US
organisations:
- AI
- API
- ARTEX
- Railway
- TechRadar Pro
- Temporal
- Wiz
---

![A digital themed isometric showing a neon padlock in the foreground, and a technological diagram of a processor logic board in the background.](https://cdn.mos.cms.futurecdn.net/j5YMwZuuKnvAXLyKBEmDrb-970-80.jpg)

* **Attackers exploited a zero-day in Railway’s build infrastructure to steal customer AI API keys and cloud credentials**
* **Stolen keys fueled roughly $740,000 in unauthorized AI usage, likely supporting large-scale model training and automation**
* **Railway spent 26 hours battling AI-assisted attackers before containing the intrusion and rotating credentials**

US-based cloud hosting company Railway said threat actors abused a previously unknown vulnerability to break in, steal user credentials, and rake up hundreds of thousands of dollars in unauthorized AI usage.

The company managed to throw out the criminals and harden its infrastructure, but not before witnessing an epic 26-hour bot-versus-bot battle.

## Railway gets attacked

At its core, Railway is a cloud hosting company, but one designed primarily for developers to build, deploy, and run applications without having to manage much of the underlying infrastructure.

Its key services include running websites and APIs, hosting databases and deploying PostgreSQL and MySQL, connecting GitHub repositories and deploying new code automatically, and handling containers, networking and resource allocation.

Similar to other cloud providers, its build infrastructure uses a multi-tenant architecture, meaning a single device hosts multiple builds which should, in theory, be in full isolation from each other on the same virtual machine.

Many of its customers are developers and businesses using AI services, with API keys stored as environment variables on the platform. This allows the hosted applications to communicate with AI models more easily.

Now, in an incident report, Railway said unidentified threat actors used a zero-day vulnerability in its build infrastructure to “partially escape filesystem isolation” and read some of the files stored on the host virtual machines. In these files were apparently credentials the build servers use to authenticate to a subset of internal systems.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

“After they acquired this credential, the attacker attempted but initially failed to use it in a variety of systems,” the report stated. However, they eventually realized the credential allowed access to Temporal, the company’s internal task management system. There they found a copy of Railway’s internal codebase in which they discovered a misconfigured authentication mechanism that allowed them to nab temporary cloud credentials.

With these, they accessed other internal systems, including credentials needed to access a production database with encrypted customer environment variables, as well as information on how to decrypt them.

## API keys for AI services

The attackers were apparently mostly interested in API keys of businesses using AI services. Using the keys, they were able to access paid AI services, leaving the victims to pick up the tab.

And quite the tab it was - roughly $740,000 charged for using coding agents and AI training pipelines. Railway believes whoever obtained the keys likely sold them on the black market, possibly to support model distillation.

Model distillation is when a smaller AI model is trained to imitate the capabilities and responses of a larger, more powerful model. This is usually done by sending a large number of queries to the original model, and using whatever it returns as training data for the smaller ones. Although it is impossible to prove, many analysts believe this is how Chinese models are able to compete with US ones.

Railway estimates environment variables of up to 100,000 customer workspaces could have been decrypted during the incident, but stresses the number represents an upper limit rather than a confirmed number of compromised accounts.

The company said the attack started on October 20 at roughly 07:28 UTC, and ended at 09:24 UTC on October 21, some 26 hours later. During that time the engineers, working in shifts, saw the attacker probing many potential routes in parallel, as Railway was hardening them, also in parallel. “The escalating situation became a contest of agent speed, with Railway defending against abliterated models and a harness similar to ARTEX, according to Wiz,” it said in the report.

Railway said it has since closed the exploited vulnerabilities, rebuilt affected infrastructure, and rotated compromised credentials. It is also working with AI providers to refund fraudulent charges, promising to cover losses that the providers refuse to reimburse.

*Via* * BleepingComputer*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
