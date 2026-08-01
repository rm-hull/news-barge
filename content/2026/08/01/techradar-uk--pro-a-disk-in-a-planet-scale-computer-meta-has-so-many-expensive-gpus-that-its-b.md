---
title: Meta slashes AI loading times from hours to minutes after rebuilding storage
source_url: https://www.techradar.com/pro/a-disk-in-a-planet-scale-computer-meta-has-so-many-expensive-gpus-that-its-buying-ssds-to-kill-idle-time
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-01T21:06:33Z'
published: '2026-08-01T00:00:00Z'
description: Meta is buying more SSDs because idle AI GPUs are becoming even more
  expensive than premium flash storage itself today
image: https://cdn.mos.cms.futurecdn.net/mK7KLzPXizP5EMdAqToXe3-1920-80.png
---

![Meta Muse Spark](https://cdn.mos.cms.futurecdn.net/mK7KLzPXizP5EMdAqToXe3.png) 

- **Meta rebuilt storage systems after slow data repeatedly stalled expensive AI GPUs**
- **SSD caching dramatically reduced AI dataset loading times from hours to minutes**
- **Meta replaced complex metadata lookups with a faster unified storage architecture**

Meta says storage systems have failed to keep pace with AI computing power, creating delays that leave costly GPUs waiting instead of processing workloads efficiently.

According to the company's engineers, storage bottlenecks remain a major cause of GPU stalls, increasing operating costs while slowing research progress and extending development timelines.

To address those delays, Meta redesigned its storage architecture, arguing that faster movement of data can unlock greater value from expensive AI hardware investments.

## Meta rebuilds storage architecture to keep GPUs working

Meta's engineers explained that the company operates hundreds of exabyte-scale storage clusters supporting Facebook, Instagram, Reality Labs, Meta AI, advertising systems, databases, and internal data warehouses.

Those services rely on a foundational storage layer called Tectonic, which manages object storage, file systems, block devices, and data placement across HDDs and SSDs.

The company has increasingly shifted from traditional file storage toward BLOB storage because massive AI datasets require unified access methods with significantly higher performance.

When GPU servers request information from storage, repeated metadata lookups across several layers create latency that interrupts AI training pipelines and delays overall processing.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Meta responded by rebuilding the metadata subsystem into a unified schema backed by ZippyDB while allowing clients to retrieve data directly from storage servers.

Instead of routing every transfer through application servers, the redesigned software uses an embedded client capable of streaming information directly from the Tectonic storage layer.

To support distributed AI deployments, Meta placed regional BLOB-storage systems beside GPU clusters, reducing delays associated with transferring information across distant infrastructure.

It introduced distributed caching using unused GPU host memory, producing an average cache hit rate of 80%, while metadata became accessible within 1 to 2 ms.

The engineers further added hedged reads alongside dynamic concurrency controls, stating that "the new BLOB-storage stack is now capable of serving AI workloads without causing GPU stalls."

## SSD caching cuts hours from AI data ingestion

Meta examined lengthy delays experienced before AI training even began, when researchers transferred enormous dataset snapshots from BLOB storage into regional GPU facilities.

Instead of loading every dataset directly from slower storage drives, Meta created multiple cache layers that keep frequently used data much closer to GPU servers.

That approach introduced multiple caching layers, using GPU memory as L1, SSDs inside GPU hosts as L2, and regional flash-backed BLOB storage as L3.

Traditional HDD storage remained the authoritative data source, while faster cache layers supplied frequently requested information before slower disks became necessary during processing.

Meta’s redesign produced sharp gains in ingestion speed, cutting a previous 150-minute loading process down to just 10 minutes.

A separate job that once required 89 hours to complete now finishes in just over three hours from start to finish.

Citrini analyst Jukan notes that high-capacity storage has traditionally been judged mainly by its cost per terabyte of capacity alone.

He argues that idle GPU time can outweigh any savings gained from cheaper storage if data arrives too slowly each day.

This suggests that the cost of flash storage is economically rational whenever eliminating idle time costs more than the flash itself each hour.

Via *Blocks and Files*

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Efosa Udinmwen](https://cdn.mos.cms.futurecdn.net/nwRLdPUNG4rWu4Y6nthHDV.png)

Efosa has been writing about technology for over 7 years, initially driven by curiosity but now fueled by a strong passion for the field. He holds both a Master's and a PhD in sciences, which provided him with a solid foundation in analytical thinking.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
