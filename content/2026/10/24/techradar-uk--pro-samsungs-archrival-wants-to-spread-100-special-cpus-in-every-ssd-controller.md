---
title: Standard CPUs are too bloated for fast storage — SK Hynix has a solution
source_url: https://www.techradar.com/pro/samsungs-archrival-wants-to-spread-100-special-cpus-in-every-ssd-controller-ahead-of-pcie-8-0-high-bandwidth-flash-onslaught
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-24T23:10:07Z'
published: '2026-10-24T00:00:00Z'
description: These 100 tiny microprocessors are supporting general-purpose CPUs inside
  SSDs to slash power consumption by 2.5%
image: https://cdn.mos.cms.futurecdn.net/8FuXD39b3rGNiozG8zwufS-1920-80.jpg
categories:
- Technology & Software
people:
- Koo In-je
locations: []
organisations:
- AIN B
- AIN D
- AIN P
- H-TPU
- H-TPUs
- HBF
- High Bandwidth Flash
- Hynix Transaction Processing Unit
- International SoC Design Conference
- SK Hynix
- SSD
- TechRadar Pro
- Via The Elec
---

![SK Hynix at the ISOCC 2026](https://cdn.mos.cms.futurecdn.net/8FuXD39b3rGNiozG8zwufS-1920-80.jpg)

* **SK Hynix plans to distribute more than 100 processors across SSD controllers**
* **H-TPUs reportedly consume just 2.5% of conventional CPU core power**
* **Each H-TPU occupies only 4% of a general-purpose processor core's area**

SK Hynix is developing solid-state drive controllers with more than 100 compact processors to manage increasingly demanding data transfers.

The South Korean memory manufacturer says its Hynix Transaction Processing Unit (H-TPU) architecture reduces processor power requirements and chip area.

The technology is designed for enterprise storage products and future memory systems serving demanding artificial intelligence workloads.

## Small processors take over repetitive SSD operations

Speaking at the recent International SoC Design Conference, SK Hynix vice president Koo In-je described limitations affecting conventional SSD controller designs.

"Currently, general-purpose CPUs inside SSD controllers are at their limits in terms of power consumption and area," he said.

"Instead, SK Hynix has developed an H-TPU that can efficiently handle common input/output (I/O) transmission paths."

Conventional processors handle routine operations alongside demanding tasks, including reading and writing data, updating metadata, and controlling buffers.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Faster storage interfaces increase these workloads, potentially requiring additional processor cores and increasing the controller's physical footprint and electricity consumption.

H-TPUs separate repetitive operations from complicated processing, allowing numerous specialized cores to handle individual responsibilities.

SK Hynix says each processor uses just 4% of the chip area occupied by a general-purpose CPU core and consumes approximately 2.5% of its power.

The architecture uses a four-stage pipeline and sequential execution, which SK Hynix considers suitable for recurring storage operations.

Rather than activating every processor continuously, the controller enables the units required for each incoming request and places unnecessary processors into idle mode.

Conventional CPU cores remain responsible for demanding functions such as error recovery, exception management, and storage policy decisions.

This division allows specialized processors to handle routine work while the main controller retains responsibility for more complex operations.

## SK Hynix plans H-TPUs for next-generation storage

SK Hynix intends to incorporate H-TPUs into upcoming enterprise SSD controllers and its Storage Next architecture.

The company also plans to use the technology with High Bandwidth Flash (HBF), a memory technology expected to enter the market next year.

Storage Next is designed to handle smaller data requests associated with newer AI models, including transactions involving 512 bytes or less.

That represents one-eighth of the conventional 4KB data unit, allowing storage systems to access smaller portions of information.

Future PCIe generations, including PCIe 6.0, 7.0 and 8.0, are expected to increase transfer speeds, placing additional demands on storage controllers.

Distributing repetitive processing across many small cores could help limit power consumption and physical expansion as those demands grow.

SK Hynix also intends to extend the technology to its AIN storage portfolio, which includes the AIN P, AIN B and AIN D product families.

The company has not disclosed when H-TPUs will reach individual commercial products or quantified their effects on overall SSD performance.

Via The Elec (originally in Japanese)
