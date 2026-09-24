---
title: New DapuStor SSD pairs high-capacity QLC with a permanent pSLC region — trades
  6% to 20% of its QLC capacity for more than 7x faster random writes
source_url: https://www.tomshardware.com/pc-components/ssds/dapustor-splits-qlc-ssd-to-create-a-fast-pslc-region-in-dual-mode-drive-trades-6-percent-to-20-percent-of-its-qlc-capacity-for-more-than-7x-faster-random-writes
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-22T13:22:36Z'
published: '2026-09-22T00:00:00Z'
description: The dual-mode J5060 counters QLC’s slow writes by giving up a portion
  of its capacity.
categories:
- Technology & Software
- Hardware
image: https://cdn.mos.cms.futurecdn.net/AFGEhgfGmJJ6HSmCnk5pQh-1920-80.png
locations: []
people:
- DapuStor
- Sandisk
- Tom
organisations:
- DapuStor
- Enmotus
- FMS
- Get Tom's Hardware
- Google News
- Micron
- NVM Express
- NVMe
- Phison
- QD1
- QLC
- SLC NAND
- Sandisk
- Shane Downing
- TLC
- Tom’s Hardware US
- XTR
- pSLC
---

![DapuStor J5060 U.2 SSD](https://cdn.mos.cms.futurecdn.net/AFGEhgfGmJJ6HSmCnk5pQh.png)

Enterprise SSD brand DapuStor revealed a new dual-mode configuration for its J5060 enterprise drive that combines SLC (single-level cell) and QLC (quad-level cell) flash on a single drive. The drive’s new firmware runs “selected QLC cells” in a faster pseudo-SLC (pSLC) mode, trading capacity for speed.

As an example, the 30.72TB model trades around 4TB of QLC for 800GB of pSLC, a ratio closer to 5:1 than 4:1. The other two configurations put aside 400GB or 1.2TB with a cost between 6% and 20% of the QLC capacity. “No dedicated SLC NAND is required,” as this uses a “software-defined media configuration,” DapuStor said. Announced last month during FMS 2026, the drive still lacks pricing, a named customer, and a general availability date.

Typical consumer QLC drives have a pSLC cache that fills with super-fast performance, with the data later transferring over to QLC. However, this pSLC mode is dynamic and variable in size. DapuStor’s implementation uses a fixed region sized by the operator, and the regions are exposed as individual block devices to the host. The J5060 is also higher capacity, from 15.36 to 122.88TB, and in the U.2 form factor for PCIe 4.0 x4. Endurance is rated at 0.5 DWPD (Drive Writes Per Day) over five years. The stock 30.72TB model is rated at 30,000 random-write IOPS at 16KB. Its write latency is 35 microseconds.

![Diagram of an SSD divided into SLC and QLC block devices](https://cdn.mos.cms.futurecdn.net/t2hA7yxGK6qW9WD2dEMdsT.jpg)

The capacity trade-off improves what QLC is worse at, random writes, by more than seven times, DapuStor said. It also says average 4K random-write latency is below 8 microseconds. The pSLC has over 25 times the program/erase cycles of the QLC region, although without region-specific DWPD or TBW numbers. DapuStor achieves this with three firmware changes: die-level isolation, optimized SLC reserve allocation, and region-aware I/O scheduling. The high-performance region targets workloads that benefit, namely “database journals, write-ahead logs (WALs), and metadata caches.” The idea is that this drive configuration precludes the need for specialized SLC drives where failure could be an issue; however, you still end up with a dead dual-mode drive on a failure.

The NVMe specification has defined this arrangement since 2019, with an NVM Express presentation at FMS 2019 claiming the goal was to “enable one SKU to be configured by customer for their use case.” An FMS 2019 example showed that some media units run as a small fast region, while the rest run at full density. A prior drive with the same idea, via a Phison firmware split and a host driver, was the consumer Enmotus/Phison FuzeDrive P200 with our 2021 verdict stating that “excessive pricing isn’t for everyone.” Enmotus wound down the same year. It’s also possible to mod a QLC drive to SLC, as we covered in 2024. The difference here is that DapuStor hands the host a second and separate block device with storage software control.

Competitors have other solutions. Sandisk’s bet is on Direct Write QLC on its UltraQLC platform, “which eliminates SLC buffering by enabling power-loss safe writes on the first pass,” Sandisk said, but there are still performance differences, according to our own reporting. Alternatively, Micron’s solution offers a separate cache drive in its XTR. The drive uses 176-layer TLC entirely in SLC mode and is rated at up to 35 DWPD. The drive acts as an optional write buffer for arrays of Micron’s 6000-series SSDs. For reference, Micron rates the XTR at 15 microseconds for QD1 writes.

Product promises are valuable, but any full comparison requires seeing the drives in actual use. Questions remain specifically regarding DapuStor’s drive, as pSLC region specifications are lacking. It is uncertain what commands the drive employs and whether the region split is modifiable live; usability depends much on the undemonstrated storage software. More details for the QLC-based, PCIe 5.0 sibling R6060 would be nice, too. Utilizing multi-bit flash in a single-bit, SLC mode for performance or endurance reasons is not a new idea, but balancing those with the increasing need for capacity remains a challenge.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Shane Downing](https://cdn.mos.cms.futurecdn.net/Zosi9VrDytS9FkgJiHvc69.png)

Shane Downing is a Freelance Reviewer for Tom’s Hardware US, covering consumer storage hardware.
