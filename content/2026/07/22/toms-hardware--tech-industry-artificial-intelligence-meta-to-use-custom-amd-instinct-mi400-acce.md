---
title: Meta to use custom AMD Instinct MI400 accelerators with 144GB of HBM4 for select
  workloads, report claims — could dramatically reduce cost at the expense of versatility
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/meta-to-use-custom-amd-instinct-mi400-accelerators-with-144gb-of-hbm4-for-select-workloads-report-claims-could-dramatically-reduce-cost-at-the-expense-of-versatility
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-22T14:18:48Z'
published: '2026-07-22T00:00:00Z'
description: 1/3 the memory, optimized for recommendation systems.
image: https://cdn.mos.cms.futurecdn.net/vPpRcPenPjPyrz7q4vs6BP-2000-80.jpg
---

![Meta logo](https://cdn.mos.cms.futurecdn.net/vPpRcPenPjPyrz7q4vs6BP.jpg) 

AMD's custom Instinct MI450-based AI accelerator for Meta will use three times less memory than the fully-fledged Instinct MI455X and will be optimized primarily for recommendation systems operated by Facebook and other social platforms, according to SemiAnalysis. If the report is accurate, it is reasonable to expect Meta to keep using Nvidia hardware for training frontier AI models and running inference.

 ![A hand holding the Ryzen 7 9850X3D.](https://cdn.mos.cms.futurecdn.net/Xh2MupWrRjJPiLLuopmKRB.jpg) 


The custom Instinct MI455X for Meta will carry 144GB of HBM4 memory using six 8-Hi packages, whereas the full-blown Instinct MI455X will be equipped with 432 GB of HBM4 memory, according to *SemiAnalysis*. In addition, the part will reportedly offer 'significant decreases in compute.' The new design will offer a more competitive bandwidth-per-dollar ratio for recommendation systems, but will not be optimized for training of frontier AI models or running inference, the report claims.

Cutting compute performance and reducing HBM4 capacity from 432GB to 144GB should dramatically reduce the bill of materials, as HBM4 is exceptionally expensive. Furthermore, the reduction would cut the package size of the custom Instinct MI450-series accelerator for Meta, which is another way to reduce BOM costs. By using custom cut-down Instinct MI450-series accelerators instead of fully-fledged models, Meta can potentially save tens of millions of dollars.

As added bonuses, these custom Instinct MI450-series accelerators will also consume significantly less power when running recommendation workloads without significantly reducing performance. Also, such accelerators can offer better CPU/GPU balance for recommendation systems, according to *SemiAnalysis*. If Meta runs these accelerators primarily on recommendation workloads for their entire useful lives, the custom design could deliver substantially better total-cost-of-ownership.

However, such cutting down has many disadvantages. The biggest problem is loss of versatility. The reductions in both compute and HBM make it less attractive for LLM training and inference. The standard Instinct MI455X has 432 GB of HBM4 and 19.6 TB/s of bandwidth, which is particularly beneficial for large-scale training and inference. By contrast, the 144 GB capacity may be particularly restrictive for modern LLM training and inference.

In addition, there is also an interchangeability problem. A general-purpose Instinct MI455X can be reassigned from recommendation workloads to training, inference, or other workloads. Meta's specialized version is less attractive outside its intended workload. If Meta's compute demand shifts toward model training and LLM inference, it may find itself sitting on a huge installed base of accelerators optimized for a different workload mix.

As a result, for Meta's model training and inference workloads, the alternative to Meta's cut-down custom MI400 would likely be full-fat AMD Instinct MI455X systems or Nvidia's high-end platforms. Meanwhile, Nvidia has chances to become an obvious beneficiary because Meta already operates massive Nvidia infrastructure. The irony in that Meta customized an AMD accelerator to reduce costs and optimize recommendation systems, but that specialization could force its frontier AI division to buy more general-purpose accelerators — potentially from Nvidia — anyway.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

When AMD and Meta inked an agreement under which the former will supply the latter with 6 GW of Instinct AI accelerators over the next five years, they did disclose that at least some of them will be custom accelerators, including custom accelerators based on the Instinct MI450 design. As it seems now, these custom AI accelerators will only be used for select workloads, not a broad set of workloads.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Anton Shilov](https://cdn.mos.cms.futurecdn.net/uMZ5kNphxA2Ut6whdLaSQV.png)

Anton Shilov is a contributing writer at Tom’s Hardware. Over the past couple of decades, he has covered everything from CPUs and GPUs to supercomputers and from modern process technologies and latest fab tools to high-tech industry trends.
