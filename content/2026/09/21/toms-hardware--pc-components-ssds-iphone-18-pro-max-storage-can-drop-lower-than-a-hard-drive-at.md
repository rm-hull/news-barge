---
title: iPhone 18 Pro Max storage can drop lower than a hard drive at 1.1 MB/s during
  heavy writes — QLC NAND offers higher capacity but reportedly suffers 38% drop compared
  to TLC-based Pro
source_url: https://www.tomshardware.com/pc-components/ssds/iphone-18-pro-max-storage-can-drop-lower-than-a-hard-drive-at-1-1-mb-s-during-heavy-writes-qlc-nand-offers-higher-capacity-but-reportedly-suffers-38-percent-drop-compared-to-tlc-based-pro
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-21T20:25:36Z'
published: '2026-09-21T00:00:00Z'
description: QLC's hidden trade-off
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
- Personal Finance & Investing
image: https://cdn.mos.cms.futurecdn.net/urTiSnGnWhVRz88dC8qQq-2560-80.png
---

![iPhone disassembled on a light table.](https://cdn.mos.cms.futurecdn.net/urTiSnGnWhVRz88dC8qQq.png)

Apple’s latest iPhone 18 Pro series went on sale last week, and the company’s decision to use QLC-based NAND for higher-capacity storage variants appears to come with a trade-off. Bilibili channel Homolab recently tested a 1TB iPhone 18 Pro Max and found that its storage performance can drop significantly under sustained heavy workloads. Since QLC stores four bits of data per memory cell when compared to three bits with TLC, it allows manufacturers to offer higher capacities using the same physical space. However, this higher storage density comes at the cost of slower performance, particularly when handling large amounts of data.

![a snippet from the HBM roadmap article](https://cdn.mos.cms.futurecdn.net/JY32VXJVXoHUR8NRV2Kveb.png)

Homolab compared the 1TB QLC-based iPhone 18 Pro Max with a 512GB TLC-based iPhone 18 Pro. While both storage types perform fairly similarly in 4K read tests, the QLC model falls behind by 38% in a low-queue-depth mixed workload, scoring 8,168 compared to 11,285 for the TLC model. Under heavier workloads, the gap narrows, although the TLC storage model still maintains a 12% advantage.  
The drop in performance is even more apparent when it comes to sustained write tests. The iPhone 18 Pro Max uses a fast SLC cache that can deliver speeds of up to 3,000 MB/s. Once that cache is exhausted, a secondary TLC-based buffer takes over, averaging around 578 MB/s. When both cache buffers are exhausted, the phone has to write directly to the underlying QLC NAND. At that point, sustained write performance can fall to 79.4 MB/s, with speeds occasionally dropping as low as 25.6 MB/s.

That is significantly slow and comparable to the performance of many budget microSD cards (microSD Express cards are much faster). Things look even worse once the storage starts filling up. At 60% capacity, the available SLC cache drops from 250GB to just 58GB. This also causes the secondary buffer to slow down to 396 MB/s, while direct QLC writes average just 45 MB/s and occasionally fall to as low as 1.1 MB/s.

It’s important to note that these are synthetic benchmarks and are meant to represent a worse case scenario. Users should not experience any performance issues during typical tasks such as web browsing, messaging, gaming, or taking photos. Any slowdown is likely to be noticeable only during specific workloads, such as 4K or ProRes recording, large file transfers, or data backup restores. Having said that, testing by Homolab does point to the trade-off involved in using QLC NAND for a high-capacity flagship smartphone, particularly for users who regularly deal with storage-intensive tasks.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Kunal Khullar](https://cdn.mos.cms.futurecdn.net/NDK3ae3zDxAx2BJnMXxBJV.jpg)

Kunal Khullar is a contributing writer at Tom’s Hardware. He is a long time technology journalist and reviewer specializing in PC components and peripherals, and welcomes any and every question around building a PC.

* * * * Does the less file transfer performance end up equating to better battery life?Reply  
          
        If it does make better battery then I would actually chalk this up slightly in the win column. Also as the last message just stated, you won't see it in real world usage either anyways.
