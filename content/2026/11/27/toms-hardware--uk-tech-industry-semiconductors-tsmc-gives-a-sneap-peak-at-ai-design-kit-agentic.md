---
title: 'TSMC gives a sneap peak at AI Design Kit: Agentic AI with foundry expertise'
source_url: https://www.tomshardware.com/uk/tech-industry/semiconductors/tsmc-gives-a-sneap-peak-at-ai-design-kit-agentic-ai-with-foundry-expertise
source_site: Tom's Hardware
source_slug: toms-hardware
description: TSMC's ADK promises to cut accelerate chip development as nodes get more
  complex.
image: https://cdn.mos.cms.futurecdn.net/zr4jtQdQr2Ewa8sDbKneqF-1920-80.jpg
published: '2026-11-27T00:00:00Z'
scraped_at: '2026-11-27T21:10:57Z'
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
people:
- Anton Shilov
- Aveek Sarkar
- Tom
locations:
- Munich
organisations:
- A14
- AI
- APR
- Cadence
- Get Tom's Hardware
- Google News
- HP
- Head of Ecosystem and Alliance Management
- Implementation Agent
- InnoStack
- PPA
- Siemens EDA
- Synopsys
- TSMC ADK
- Tom’s Hardware
---

![TSMC](https://cdn.mos.cms.futurecdn.net/zr4jtQdQr2Ewa8sDbKneqF-1920-80.jpg)

The semiconductor industry is in a paradoxical situation these days. On the one hand, AI drives demand for the leading-edge nodes from both established players and new entrants, with everyone trying to accelerate the development cycle. On the other hand, leading-edge nodes become more complex, which increases entry barriers and stretches design cycles. While the challenge seems to be insoluble, it looks like TSMC has found a solution.

![TSMC](https://cdn.mos.cms.futurecdn.net/CyPMwuEMStxBmu4HuDQyoF-1200-80.jpg)

At its 2026 Europe OIP Ecosystem Workshop in Munich, TSMC this week unveiled its AI Design Kit (ADK), a collection of process-specific technical information, implementation guidelines, and design methodologies that enables AI agents to automate and optimize chip development flows.

The ADK complements the foundry's traditional process design kits (PDKs) and enables AI agents to use TSMC's process-specific expertise, knowledge of electronic design automation (EDA) tools, and customers' proprietary design methodologies to automate physical implementation and optimization of chips. Ultimately, the initiative aims to reduce development cycles, improve design productivity, and simplify adoption of TSMC's advanced process technologies.

"The ADK complements our traditional PDK, and it brings in capabilities to augment the EDA and other design flows," said Aveek Sarkar, Head of Ecosystem and Alliance Management at TSMC. "Our goal with these agentic flows is to bring in the technology-specific learning we have at TSMC and layer that with your orchestration layer, with your design expertise, and to support the next generation of EDA or design flows and methodologies that you have."

## Why AI?

While every new fabrication process from TSMC offers advantages in terms of power, performance, and area (PPA), it also considerably increases design complexity. Compared to TSMC's N5-derived manufacturing technologies (including various N4 nodes), the number of design rules has increased by 2.3X with N3P, 3.1X with N2P, and 3.6X with A14 (the first node to be supported by the ADK).

Meanwhile, the number of available standard library cells has increased by 2.8X, 5X, and 4.6X, respectively. Add to that a greater number of metallization stack options and plenty of EDA tool settings, and the number of possible design configurations becomes massive. As a result, conventional design optimization methodologies approach their productivity limits, according to TSMC. At the same time, some of TSMC's customers want to reduce their chip development cycles from 18 months to 12 months, Sarkar said.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Technology | N5/N4P | N3P | N2P NanoFlex | A14 NanoFlex Pro |
| Library | HD, HP | HD, HP, UHP | HD, HP, UHP + Boost Cells | HD, HP + Boost Cells |
| Cell Count | 1.0x | 2.8x | 5.0x | 4.6x |
| Rule Count | 1.0x | 2.3x | 3.1x | 3.6x |

Usage of agentic AI could help chip developers to explore more design configurations within shorter timeframes, achieve more favorable PPA results from advanced process technologies, and potentially improve manufacturability and yields by implementing more extensive physical design optimization. Furthermore, it could reduce the amount of engineering work required to adopt a new fabrication process for a new design.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

"AI is bringing a significant benefit: faster design cycles, more verification coverage, faster time to closure," Sarkar said.

## Do physical implementation faster

TSMC's early-phase AI Design Kit incorporates process-specific information, such as metal pitches, standard cell heights, routing track patterns, library cell naming conventions, and implementation guidelines, according to slides demonstrated at the event.

![TSMC](https://cdn.mos.cms.futurecdn.net/QcPPrRVftvHzU436GGrRrF-1200-80.jpg)

With the ADK, EDA agents — such as Cadence's InnoStack or Synopsys's Implementation Agent — can use a simple natural-language prompt and a large language model (LLM) to automatically generate a qualified automatic placement and routing (APR) reference flow for TSMC's A14 process technology. Such a flow includes project setup, library cell usage, placement and routing optimization, routing track and power grid creation, and wide-wire configuration. Traditionally, engineers could spend weeks on preparation of such scripts, but now APR scripts could be prepped with a natural language prompt, though TSMC did not disclose the actual time it takes to prep them (probably because it depends on design complexity and goals).

"Instead of spending weeks preparing APR scripts, EDA agents can take a simple prompt from users and the TSMC ADK and use a generative model to deliver a qualified APR reference flow," a spokesperson from TSMC said at the stage.

For more sophisticated design tasks, TSMC proposes an orchestration agent that resides at the customer's site and combines three sources of knowledge with clear ownership:

* Proprietary in-house design know-how, constraints, guidelines, and customized flow;
* Specialized EDA agents that know how to use EDA tools and their capabilities;
* TSMC's ADK that provides design reference package and technology-specific information on top of what EDA agent and tools know.

The orchestrator coordinates agents responsible for design diagnostics, power grid implementation, timing closure, design rule checks, and congestion mitigation. These agents analyze EDA tool output and automatically adjust parameters for subsequent iterations across floorplanning, placement, clock tree synthesis, routing, sign-off, and engineering change orders (ECOs). Such a methodology enables continuous design optimization 24/7 with less human intervention.

"The orchestrator then directs these agents to analyze the output of EDA tools and automatically adjust the settings for the next iteration across floorplan, placement, CTS, routing, sign-off, and ECO," the spokesman said. "This agentic AI flow drives the iterative design process 24/7, minimizing the turnaround time and maximizing productivity."

## Complement, not replace

For now, TSMC's ADK primarily addresses physical implementation rather than chip architecture or logic design. The company has not demonstrated an autonomous design flow that takes a chip from an architectural specification to tape-out without human intervention. Nor has TSMC disclosed quantified PPA improvements, actual reductions in development cycles, or a commercial availability timeframe for its ADK.

It is noteworthy that TSMC's ADK neither replaces conventional PDKs nor substitutes for advanced AI-enabled EDA software from Cadence, Synopsys, Siemens EDA, or other developers. Instead, it provides process-specific knowledge that enables AI agents to make more informed decisions, while the actual physical implementation, simulation, optimization, and verification tasks remain the domain of specialized EDA tools. Thus, chip developers cannot use the ADK independently of traditional EDA infrastructure.

## Strategic importance

For TSMC, the ADK could accelerate adoption of its latest fabrication processes, as customers could adapt their design methodologies to new nodes faster. Smaller fabless chip developers could also gain access to sophisticated physical design methodologies without the need to develop expertise comparable to that of prominent chip developers entirely in-house. Meanwhile, EDA and IP providers could benefit from closer integration of their products into process-specific design flows, whereas contract chip designers could offer shorter development times for their customers without significant additional investments.

There is also a potential customer lock-in aspect. While TSMC's proposed architecture preserves customers' ownership of proprietary design knowledge, extensive integration of foundry-specific physical design enablement collateral, EDA agents, and internal orchestration systems could make migration to another foundry harder and generally less likely as chipmakers get more accustomed to TSMC ADK (which is an exclusive capability for now and will remain an exclusive offering for a while). In effect, TSMC's competitive advantages will extend well beyond its process technologies, production capabilities, and conventional design ecosystem to include intelligence that emphasizes its customers' chip development methodologies.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Anton Shilov](https://cdn.mos.cms.futurecdn.net/uMZ5kNphxA2Ut6whdLaSQV-140-80.png)

Anton Shilov is a contributing writer at Tom’s Hardware. Over the past couple of decades, he has covered everything from CPUs and GPUs to supercomputers and from modern process technologies and latest fab tools to high-tech industry trends.
