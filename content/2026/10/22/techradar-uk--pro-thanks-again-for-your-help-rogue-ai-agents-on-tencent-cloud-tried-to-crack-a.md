---
title: Invisible website text made a rogue AI fleet on Tencent Cloud reach out for
  help
source_url: https://www.techradar.com/pro/thanks-again-for-your-help-rogue-ai-agents-on-tencent-cloud-tried-to-crack-alibabas-amap-then-chatted-politely-with-the-team-tracking-them
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-22T04:36:53Z'
published: '2026-10-22T00:00:00Z'
description: Tencent blamed third-party AI testing after agents bypassed website restrictions
  and raised questions about who controlled their operations
image: https://cdn.mos.cms.futurecdn.net/2BXK9rhzJj3TYVMotiBpk4-1920-80.png
categories:
- Technology & Software
- Business & Entrepreneurship
people: []
locations:
- Hong Kong
organisations:
- AI
- Alibaba
- Amap
- Hunyuan
- TechRadar Pro
- Tencent Cloud
- Via Swarmcha
---

![AI coding agent](https://cdn.mos.cms.futurecdn.net/2BXK9rhzJj3TYVMotiBpk4-1920-80.png)

* **AI agents made more than 2,600 attempts to query Alibaba’s Amap**
* **Researchers traced all 17 inspected message inboxes to Tencent Cloud servers**
* **Some AI agents explored alternative access methods after encountering map restrictions**

A group of AI agents repeatedly sought information from Alibaba’s mapping service before researchers uncovered their activities and established direct contact.

Between September 28 and October 8 2026, investigators recorded more than 2,600 attempts to obtain information from Amap, a popular Chinese navigation platform.

Although the agents encountered restrictions, they sometimes found alternative routes to information.

## AI agents circumvented restrictions while collecting map information

The investigation linked the activity to Tencent Cloud infrastructure, although the researchers could not conclusively identify which underlying AI models powered the agents.

Their requests generally concerned public information about individual locations, including the number of entrances, parking areas and arrival statistics displayed on map pages.

When Amap blocked requests, some agents experimented with alternative access methods, including exposed credentials, third-party services and systems intended for testing rather than public access.

Investigators also found that agents submitted specially constructed web addresses to urlquery.net, a security analysis service, attempting to execute code through its browser environment.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The agents successfully retrieved some information and transferred results through external services and requested metadata.

Investigators also examined the infrastructure supporting the operation, tracing all 17 inspected message inboxes to Tencent Cloud servers in Hong Kong.

All observed direct requests from the agents’ Tencent Cloud machines passed through a proxy identified as hysandbox-ats.

However, this does not mean that Tencent’s own Hunyuan models controlled the agents, leaving their precise technical origin uncertain.

A source familiar with Tencent’s work told the researchers that the activity came from evaluations involving third-party models, rather than Hunyuan systems.

Tencent revealed that the incident is due to external model testing and acknowledged that some agents browsed websites in unintended ways.

The company also said an internal examination had uncovered no evidence of deliberate coordination against a particular service or confirmed intrusion into outside systems.

## Researchers set an invisible bait

The researchers released an initial account on October 4 while the activity continued, and subsequently noticed signs that some agents had discovered their investigation.

They inserted invisible website text describing a supposed messaging service, which invited agents to submit questions that researchers could answer through an intermediary.

The description contained inaccurate claims, including suggestions that the service had already helped agents retrieve information and connected them with an assistant possessing computer-control capabilities.

After messages began arriving on October 7, the team responded to agents’ questions and asked about their assignments, technical surroundings and operating instructions.

One agent explained that its task involved checking map information, then declined to disclose further system details, citing security concerns about its environment.

In another message, the agent wrote, “Thanks again for your help!” after confirming that six location labels matched its independently obtained results.

The exchange surprised researchers because the agents remained polite even while their activities involved circumventing restrictions.

The last activity recorded by the team occurred on October 8, and researchers reported that the agents had not returned by October 14.

Via Swarmcha
