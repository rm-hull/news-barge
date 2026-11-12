---
title: AI's infrastructure boom is standing on porcelain legs
source_url: https://www.techradar.com/pro/ais-infrastructure-boom-is-standing-on-porcelain-legs
source_site: TechRadar UK
source_slug: techradar-uk
description: Why AI agents are straining data infrastructure
image: https://cdn.mos.cms.futurecdn.net/h8ZQHernNUVpnGYX7QnxVM-2560-80.jpg
published: '2026-11-12T00:00:00Z'
scraped_at: '2026-11-12T19:53:23Z'
categories:
- Technology & Software
- Business & Entrepreneurship
people: []
locations:
- AI
organisations:
- Amazon S3
- Amazon Web Services
- An AI
- Apache Iceberg
- Apache Parquet
- Future plc
- SereneDB
- TechRadar Pro
- TechRadarPro
---

![The letters AI in a box in the middle of a vast digital room divided by beams of line](https://cdn.mos.cms.futurecdn.net/h8ZQHernNUVpnGYX7QnxVM-1920-80.jpg)
![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png)

AI may look seamless at the surface, but underneath, search and analytics are still pulling in different directions.

There is an image I keep returning to when I think about AI infrastructure – an elephant standing on porcelain legs. The systems being built above the data layer are getting heavier and more ambitious, while the foundations beneath them receive far less attention. Investors and technology companies talk about AI infrastructure constantly, but they usually mean chips, models, and the applications built on top of them.

But AI infrastructure is more than that. Every one of those applications depends on a less fashionable layer underneath – the systems that find, retrieve, and analyze its data.

Co-Founder and CEO of SereneDB.

In many businesses, search and analytics still live in separate systems. One finds relevant information in documents and other unstructured data. The other calculates, compares, and identifies patterns. Pipelines copy and synchronize information between them, while engineers keep the systems working together.

Separating search from analytics was not a foolish design choice. The split became the status quo because it suited the questions, hardware, and users of the time. Now, however, natural-language interfaces and AI agents are exposing the cracks.

A person asks one ordinary question, but the infrastructure may have to turn it into several searches, a retrieval job, and a separate analytical query before it can produce an answer. Did AI create this problem? No. But it has made it much harder to ignore…

## One question becomes several jobs

An AI agent can turn one human request into several smaller machine queries before returning an answer. The agent may search for different parts of the request separately, rank the results, and decide whether it has enough evidence to continue. What feels like one action to the user can therefore generate repeated database work.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Some requests only require retrieval. Others ask the system to find evidence and calculate with it. The moment a task needs both, the distinction between search and analytics becomes visible: one system locates the relevant material, while another may be asked to aggregate values or identify a pattern.

Natural language does not respect the way the database industry has divided itself. People do not separate ‘find the relevant documents’ from ‘calculate what they mean’ when they ask a colleague for an answer. Agents do not either. They translate a single intention into whatever sequence of searches and calculations is required.

The extra database activity matters even before we imagine an agent swarm – a group of AI agents working in parallel on parts of a larger task. One apparently simple prompt can already create more database work than the user sees. Every hand-off between systems adds latency, cost, and another place where context can be lost.

## Search and analytics grew up apart

AI agents expose these hand-offs because search systems and analytical databases developed separately. Search engines are designed to find relevant information in messy text, logs, and documents, even when the user cannot describe the answer precisely. Analytical databases are built to work with structured data – aggregating large datasets, joining records, calculating averages, and identifying trends.

The separation between search and analytics made sense when businesses mostly asked one system to find information and another to calculate with it. It becomes a problem when a single question needs both.

Search may identify the right set of documents, but another system is often needed to crunch the numbers inside them. Analytical tools can calculate quickly, but they generally work best when the user already knows where the relevant data sits and how it is structured.

To combine search with analytics, businesses build extra copies of data, extraction and transformation pipelines, synchronization jobs, and application code. Vector search can add another specialized system to the chain. Data engineers then spend time maintaining that plumbing, not because the plumbing creates value of its own, but because the underlying jobs remain separated.

Some search and analytical products are already crossing into the other field. Even so, many businesses still run separate systems and maintain the infrastructure that connects them.

## Separate systems create costs today

Maintaining separate search and analytics systems means paying for extra copies of data, the pipelines between them, and the engineers who keep everything working. Search indexes need to be refreshed as source data changes. Analytical stores may hold another version of the same information, while vector search can introduce another specialist layer.

The exact architecture varies, but each additional copy consumes storage, every synchronization job needs monitoring, and every hand-off creates another place where data can fall out of date or a query can slow down. Those costs exist before AI agents increase query volumes. Agents make them harder to overlook because one user action may trigger several operations across the same chain of systems.

## Open formats change the economics

One way to reduce that duplication is to keep the underlying data in object storage and use open formats so different tools can work with it. In practice, the data might sit in Amazon S3, the object storage service from Amazon Web Services, as Apache Parquet files organized into tables with Apache Iceberg.

This approach separates storage from the databases and servers that process the data. Search and analytics tools can work from the same underlying information instead of requiring a complete copy inside every product. An index and a computing layer are still needed, and some workloads will continue to justify specialized systems, but duplication no longer has to be the default.

Across the industry, search and analytics are beginning to converge as businesses gain more control over where their data lives. When a new workload appears, they can use the same underlying data instead of automatically adding another database, another copy, and another pipeline.

## More agents will increase the pressure

Reducing duplicated data and pipelines will become more valuable as businesses give AI agents more work. Vast, concurrent agent swarms are not yet an everyday production reality, but agents are already changing database workloads. One natural-language request can become several underlying database operations, and an agent can repeat that process continuously, without the working hours or pauses that shape human use.

As agents handle more work, query volumes may begin to follow software activity rather than employee headcount. The first signs of that extra demand are unlikely to be a sudden database collapse. They are more likely to appear as queues, slower responses, timeouts, rising infrastructure bills, and greater pressure on the pipelines between systems.

Businesses do not need to assume that swarms are imminent to justify reviewing the data layer. Duplicated infrastructure and operational costs already exist. More agents would increase both.

## The status quo is the real competitor

A simpler data layer still has to beat infrastructure that businesses already know and trust. Legacy is often used as an insult, but I mean it more literally – the established status quo. Existing systems became dominant because they solved important problems and, in many cases, continue to solve them well.

Businesses should not rip out working infrastructure simply because AI is fashionable. They should ask more practical questions. How many complete systems hold versions of the same data? How many pipelines exist only to move information between them? How long does it take to answer a question that combines unstructured evidence with numerical analysis? How much specialist time is spent keeping that route operational?

If the answers remain simple and economical, the current architecture may be perfectly adequate. If every new AI feature requires another store, another copy, and another layer of glue, the foundation deserves closer attention.

The elephant is getting heavier, and its legs deserve the same attention as everything being built above them. Changing those foundations, however, will not be easy. There is no fiercer competitor than the status quo.

*This article was produced as part of* * TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:* * [https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)
