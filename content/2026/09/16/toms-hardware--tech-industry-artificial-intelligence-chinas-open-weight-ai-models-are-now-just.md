---
title: China's open-weight AI models are now just 4 months behind frontier US offerings,
  Mozilla report claims — models still lag in some benchmarks but are drastically
  cheaper to use
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/chinas-open-weight-ai-models-are-now-just-4-months-behind-frontier-us-offerings-mozilla-report-claims-models-still-lag-in-some-benchmarks-but-are-drastically-cheaper-to-use
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-16T13:27:02Z'
published: '2026-09-16T00:00:00Z'
description: Behind, but at a fraction of the price
image: https://cdn.mos.cms.futurecdn.net/QGnsfcy2NbHpJXXmvjHVJk-2000-80.jpg
---

![Z.ai](https://cdn.mos.cms.futurecdn.net/QGnsfcy2NbHpJXXmvjHVJk.jpg) 

Mozilla has published version 1.1 of its __State of Open Source AI report__ on Sept. 15 using data current to Sept. 1, revealing that many of the best Chinese open-weight AI models are closing the gap with U.S. frontier offerings. The best open model trailed the closed leader on the Artificial Analysis Intelligence Index by three points at 60% of the price and two points behind Claude Fable 5 at 30%. Mozilla’s fit on METR task-horizon data puts the open-closed gap at around 4.4 months, in line with Epoch AI’s four-month estimate.

 ![Microsoft data center in Mount Pleasant, Wisconsin](https://cdn.mos.cms.futurecdn.net/Vh4nY3pMCcmra2ymXah9S7.jpg) 


Mozilla is the nonprofit behind the Firefox web browser, and its report is a recurring assessment first published on __July 14__ on the Mozilla blog. It’s built on a Mozilla/SlashData survey of roughly 1,400 developers along with OpenRouter traffic data and third-party benchmark indices. Mozilla is an advocate for open models, and __TIME__ reported on July 14 that Raffi Krikorian, Mozilla’s chief technology officer, described the report as partly advocacy. “Open weights” in this context means downloadable weights rather than training data or code. The report counts 16 notable open releases, but none delivers the data recipe required by the Open Source Initiative’s definition.

The four-month figure rests on METR, which is a research nonprofit that scores models by the length of task, in human working time, they complete half the time. By Mozilla’s fitted estimate, closed models handle tasks that take human experts 8 to 12 hours. Open models reach that about four months later, with open capability doubling every 3.9 months versus 5.5 for closed, by Mozilla’s computation. Mozilla also charted vals.ai’s Terminal-Bench 2.1 results, which run every model through the same harness, or software layer that offers a model its tools. On that board, Z.ai’s GLM-5.2 scored within a point of Claude Opus 4.7 and about four points behind Opus 4.8, at less than one-fifth the cost per test. On OpenRouter, a marketplace that routes developer traffic to hundreds of models, Mozilla counted eight of the top ten models by August token volume as open weights, seven of them Chinese-built. Nevertheless, closed providers took 96% of model-layer revenue on OpenRouter from May–September 2025, the __Linux Foundation__ reported. “We see the decision to pay for closed [models] as workload-specific rather than organization-specific,” Krikorian told Ars Technica in an email.

 ![Mozilla chart of the best open-weight model score at each hardware tier.](https://cdn.mos.cms.futurecdn.net/ExsxWrUXoBVvTYXeppQoaf.png) 


One caveat is that the four-month gap and the 30% token price figure are measured API to API on hosted endpoints and at list price. The report’s own hardware chart puts the best open model that fits one server at 52.6 and the best on one GPU at 40. The drop from the top is 10 and 23 points, respectively, a larger gap than the reported four months. Kimi K3’s native MXFP4 checkpoint runs about 1.56TB across 96 shards, and Mozilla’s serving configuration lists 64 or more accelerators, while __vLLM calls for__ at least eight GB300 GPUs, with multiple nodes for production traffic. The report describes this as open but not runnable by most who hold it, and __Tom’s Hardware put the memory need near 1.5TB in July__. One example exception is Thinking Machines’ Inkling-Small model, under the Apache 2.0 license, whose NVFP4 version fits one B300 at a 180GB floor.

The report’s data stops at Sept. 1. Since then, Artificial Analysis has moved its index to v4.3 with a different evaluation set. The live board has Claude Fable 5.1 at 53 on its highest effort setting with Kimi K3 at 44, not comparable to the v4.1.1 numbers Mozilla plotted. vals.ai’s Terminal-Bench 2.1 board, updated Sept. 11, is now led by GPT-6 Astra at 87.27% with Fable 5.1 at 85.02%. Mozilla’s own chart caption reads: “the gap resets every release cycle.” K3 also carries an allegation detailed in the __Sept. 8 NSA/CISA/FBI joint advisory__ (AA26-251A). The claim, which Mozilla’s report states as “asserted, and unshown,” is that Moonshot extracted Claude Fable 5 data to train K3 through distillation, the practice of training one model on another model’s outputs. On __July 17__, Artificial Analysis had K3 at 57 versus Fable 5’s 60, while on Sept. 1, Mozilla had it two points back.

  


Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Shane Downing](https://cdn.mos.cms.futurecdn.net/Zosi9VrDytS9FkgJiHvc69.png) 

Shane Downing is a Freelance Reviewer for Tom’s Hardware US, covering consumer storage hardware.
