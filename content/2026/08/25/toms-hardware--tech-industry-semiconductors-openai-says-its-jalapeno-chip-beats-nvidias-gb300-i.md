---
title: OpenAI’s 700W Jalapeño ASIC outpaces 1,400W Nvidia flagship GPU — claims up
  to 1.9x throughput per kilowatt and 3.6x lower latency, co-developed with Broadcom
source_url: https://www.tomshardware.com/tech-industry/semiconductors/openai-says-its-jalapeno-chip-beats-nvidias-gb300-in-first-published-benchmarks
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-25T20:41:11Z'
published: '2026-08-25T00:00:00Z'
description: Nvidia's Vera Rubin wasn't in the comparison.
image: https://cdn.mos.cms.futurecdn.net/3Bym5bRSoc2XYC2CRstQM3-2560-80.jpg
---

![OpenAI Jalapeño](https://cdn.mos.cms.futurecdn.net/3Bym5bRSoc2XYC2CRstQM3.jpg) 

Just over one week after Nvidia agreed to backstop up to $105 billion in financing for its data centers, OpenAI arrived at Hot Chips on Tuesday with benchmarks claiming its first in-house chip beats Nvidia's GB300. Jalapeño, the inference ASIC OpenAI co-developed with Broadcom, delivered 1.5 times to 1.9 times more throughput per kilowatt and 1.7 times to 3.6 times lower end-to-end latency than Nvidia's GB200 and GB300 rack systems on *SemiAnalysis's* public InferenceX suite, with a 700W part going up against accelerators rated at 1,200W and 1,400W. OpenAI plans to begin deploying the chip in its own data centers later this year.

The tests covered three open models: GPT-OSS 120B, DeepSeek R1 670B, and Moonshot AI's 1-trillion-parameter Kimi K2.5, with OpenAI reporting its widest leads at low-latency operating points, where it claims 8.6 times to 104.3 times more throughput per kilowatt at the GB300's fastest previous time-between-tokens settings.

 ![OpenAI says its Jalape&ntilde;o chip beats Nvidia's GB300 in first published benchmarks](https://cdn.mos.cms.futurecdn.net/YAiAHyxKfYYYbPvLf5CTA6.png) 


OpenAI normalized the results to each accelerator's published package TDP, though it said Jalapeño's measured sustained power stayed at or below 550W in testing. An appendix comparison using all-in utility power per accelerator, 1.18kW for Jalapeño against 2.55kW for the GB300, produces narrower gaps, as does pitting Jalapeño against a GB300 running multi-token prediction, where the peak efficiency lead shrinks to roughly 1.5 times.

Jalapeño wasn't tested against Vera Rubin, the Nvidia platform that's slated to power the first gigawatt of Nvidia systems OpenAI agreed to deploy in the second half of 2026. The chip also doesn't train models, the workload where Nvidia's hardware remains unchallenged. In addition, the major comparisons ran Jalapeño's single-token prediction against GB300 configurations doing the same, even though Nvidia deployments commonly use multi-token prediction in production. *SemiAnalysis*, which said it ran InferenceX with OpenAI engineers in the company's lab, described the part as "beating every Nvidia, AMD, and Google chip we have been able to test."

Each Jalapeño package, unveiled in June after a nine-month RTL-to-tapeout cycle, pairs its compute die with six HBM4 stacks, totaling 216 GiB at 15.4 TB/s. The GB300 carries 288GB of HBM3E at a 1,400W rating, so per watt of rated power, OpenAI's chip packs roughly 50% more memory. The company's Hot Chips presentation states that the main bottleneck its architecture targets is exposing aggregate HBM bandwidth, not adding more of it.

That memory is of course the tightest commodity in the semiconductor industry. Samsung, SK hynix, and Micron have sold their HBM capacity through 2027, a shortage so severe that Nvidia is reportedly testing cut-down Rubin Ultra configurations with as little as 192GB, and SK hynix CEO Kwak Noh-jung has warned that 2027 will be the worst year of the crunch. Micron told the same Hot Chips conference on August 23 that HBM consumes roughly three times the wafer area of DDR5 for equivalent capacity, a penalty that widens with each generation. Scaling Jalapeño across the 10GW deployment agreement that OpenAI signed with Broadcom last October would make the company a substantial new claimant to HBM4 supply, which Nvidia currently dominates through multi-year allocation deals with SK hynix.

A second-generation chip is approaching tapeout, expected within months, according to *Bloomberg*, and concept work on a third generation is underway. The first part reportedly uses a TSMC 3nm-class process, keeping OpenAI in the same wafer, memory, and advanced packaging queues as Blackwell and Rubin for the foreseeable future.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

OpenAI is procuring those inputs while deepening its financial dependence on the company it just benchmarked. On August 17, Nvidia agreed to provide up to $105 billion in financing for an OpenAI-leased data center campus in Ohio. "Nvidia is a really good partner, and we continue to need a lot of Nvidia," Richard Ho, OpenAI's vice president of hardware, told *Bloomberg* in an interview following the announcement.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Luke James](https://cdn.mos.cms.futurecdn.net/C4FAi2KzwaGLUrBqzX5aBM.png)

Luke James is a freelance writer and journalist. Although his background is in legal, he has a personal interest in all things tech, especially hardware and microelectronics, and anything regulatory.
