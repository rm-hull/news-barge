---
title: Sanctioned Chinese supercomputer maker stripped of IO500 benchmark crown, Intel-powered
  Aurora retakes the lead — record-breaking ParaStor F9000 storage system doesn't
  meet reproducibility requirements
source_url: https://www.tomshardware.com/tech-industry/supercomputers/sanctioned-chinese-supercomputer-maker-stripped-of-io500-benchmark-crown-intel-powered-aurora-retakes-the-lead-record-breaking-parastor-f9000-storage-system-doesnt-meet-reproducibility-requirements
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-11T19:10:06Z'
published: '2026-09-11T00:00:00Z'
description: But it is still among the fastest storage subsystems in the world.
image: https://cdn.mos.cms.futurecdn.net/BZeKHbXtMSgJcRKR9H6zR-2000-80.png
---

![Server SSD installation](https://cdn.mos.cms.futurecdn.net/BZeKHbXtMSgJcRKR9H6zR.png) 

The IO500 Committee has removed storage subsystems based on Sugon's ParaStor F9000 all-flash storage systems from its Production IO500 list, as the system does not meet reproducibility requirements, which include sufficient architecture details and general availability, as noticed by Glenn K. Lockwood. The machines powered by ParaStor F9000 storage systems have been moved to the Research IO500 list and are still among the world's highest-performing storage devices; meanwhile, Intel's Aurora has retaken the top spot on the Production list.

"After further review, the Sugon ISC26 submission has been transferred from the Production List to the Research List, as it did not satisfy the criteria for the highest level of Reproducibility due to the lack of widely available architectural details and limited general availability of the file system," a statement by the IO500 Committee reads. "Accordingly, the previous #1 position on the Production and Production 10-Client lists (Argonne’s DAOS system) has been restored."

IO500 is essentially the storage counterpart to TOP500, but rather than ranking supercomputers by computational performance, it ranks HPC storage systems by their I/O performance in terms of overall bandwidth and I/O.

At ISC 2026, SCNet submitted two systems based on ParaStor storage software and ParaStor file system and F9000 all-flash storage systems. The larger SCNet AICS-A submission ran the IO500 benchmark from 500 client nodes with 64,000 client processors and achieved an IO500 score of 79,110.05, with 26,888.39 GiB/s of bandwidth and 232,754.76 kIOPS of metadata performance. The smaller AICS-B was a 10-client submission with 2,560 client processors. It scored 7,839.30, with 2,551.40 GiB/s and 24,086.69 kIOPS. Both submissions identify Sugon as the storage vendor and ParaStor as the file system.

The results substantially exceeded Argonne National Laboratory's Aurora running a custom storage subsystem featuring Intel's Optane Persistent Memory modules, SSDs, and DAOS file system. A comparable Aurora Production result scored 32,165.90, with 10,066.09 GiB/s of bandwidth and 102,785.41 kIOPS, which means AICS-A's overall score was about 2.46X higher. In the 10-client category, AICS-B's 7,839.30 was about 2.72X faster than Aurora (which scored 2,885.57). Thus, when initially accepted into the Production lists, the two SCNet submissions displaced Aurora from the top positions in both the main Production and 10-Client Production rankings.

Just like the Top 500 list, which Top 20 largely includes one-off supercomputers, the IO500 accepts completely bespoke storage subsystems based on exotic hardware and custom parallel file systems. However, the IO500 requires its Production-list submissions to meet its highest reproducibility standard, which means their architecture must be sufficiently documented and the underlying file system generally available so that the results can be independently understood and reproduced.

So, while it is hard to expect someone trying to reproduce Aurora’s 230PB storage subsystem in their garage or data center, its architecture and software can be independently examined and reproduced on a smaller scale because DAOS is open source, downloadable, extensively documented, and has publicly available architecture, implementation details, and hardware/software requirements.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

By contrast, Sugon's ParaStor is proprietary and far less transparent: IO500 said the F9000 submission lacked widely available architectural details and that the file system had limited general availability, which prevents independent examination and reproduction sufficient to meet the Production list's reproducibility standard.

The same applies to Huawei's OceanFS and SuperFS architectures as well as other proprietary architectures developed in China, which the Research list includes. For example, the Research IO500 list is led by Pengcheng Laboratory's CloudBrain system with Huawei OceanStor A800 storage and the OceanFS file system, which achieved an IO500 score of 603,334.56 with 8,291.11 GiB/s of sequential throughput and 43,903,983.64 KIOPS random performance.

What is perhaps a bit odd is that while Pengcheng Laboratory's CloudBrain and CloudBrain-II submissions are clearly marked as 'proprietary' in the reproducibility column of the Research IO500 list, the SCNet-A submission carries a 'fully reproducible' badge.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Anton Shilov](https://cdn.mos.cms.futurecdn.net/uMZ5kNphxA2Ut6whdLaSQV.png) 

Anton Shilov is a contributing writer at Tom’s Hardware. Over the past couple of decades, he has covered everything from CPUs and GPUs to supercomputers and from modern process technologies and latest fab tools to high-tech industry trends.
