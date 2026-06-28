---
title: China’s Loongson launches homegrown 16-core server CPU built on LoongArch architecture
  — 40W chip with DDR4 ECC and 32 PCIe lanes targets cheap SMB file, database, and
  web servers
source_url: https://www.tomshardware.com/pc-components/cpus/chinas-loongson-launches-homegrown-16-core-server-cpu-built-on-loongarch-architecture-40w-chip-with-ddr4-ecc-and-32-pcie-lanes-targets-cheap-smb-file-database-and-web-servers
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-06-28T15:38:47Z'
published: '2026-06-28T00:00:00Z'
description: Support for China’s local software and hardware ecosystem also appears
  to be a selling point
image: https://cdn.mos.cms.futurecdn.net/bGRpAscqyHMhWFDYf2s4eb-1200-80.webp
---

![Loongson 3C3000](https://cdn.mos.cms.futurecdn.net/bGRpAscqyHMhWFDYf2s4eb.webp) 

Loongson Technology has announced the Loongson 3C3000, a new 16-core server processor aimed at low-cost general-purpose server systems. Unveiled on June 26, 2026, via a public corporate release, the chip is based on Loongson’s in-house architecture and is designed for small- and medium-sized business workloads, including file, database, web, and business process servers. Loongson says the 3C3000’s general-purpose computing performance matches that of the company’s earlier 3C5000 server processor.

The Loongson 3C3000 — which is based on a 64-bit architecture and supports the LoongArch instruction set — uses the company’s LA364E processor core design and comes in an FCBGA1371 package measuring 37.5mm by 37.5mm. The chip is pin-compatible with the Loongson 3B6000 processor, which should make it easier for system builders to reuse existing platform designs.

The processor features 16 physical cores and 16 threads, with clock speeds ranging from 1.5 GHz to 1.8 GHz. Each core supports 128-bit vector instructions and three-issue out-of-order execution. Loongson says each core integrates two fixed-point units, one vector unit, and two memory access units.

Cache and memory support are modest by modern server standards, but in line with the chip’s low-cost positioning. Each core includes 64KB of private L1 instruction cache and 64KB of private L1 data cache, while all 16 cores share 16MB of L2 cache. The integrated memory controller supports two 72-bit DDR4-2400 memory channels with ECC support, giving the processor server-class error correction for business and infrastructure workloads.

For expansion, the 3C3000 provides two PCIe x16 interfaces, totaling 32 PCIe lanes. These can be split into up to four x4 or x8 interfaces, depending on platform requirements. The chip also includes another PCIe x16 interface that can be configured as LCL (Loongson Coherent Link) for dual-processor interconnection. Other interfaces include SPI, UART, three I2C interfaces, AVS, and 16 GPIOs.

Loongson lists a typical power consumption of 40W when running at 1.5 GHz. The processor supports dynamic shutdown of the main module clock and dynamic frequency adjustment of the main clock domain, helping reduce power consumption under lighter workloads. It also integrates a Loongson-developed security and trust module that supports Chinese national cryptographic algorithms for encryption and decryption.

Unlike the 36C000, which Loongson says matches Intel’s Xeon, the company is positioning the 3C3000 as a low-cost, high-performance server CPU for customers that need general-purpose compute rather than high-end acceleration or AI performance, slotting it below the higher-core-count 3C6000 server lineup the company launched a year earlier. Support for China’s local software and hardware ecosystem also appears to be a selling point. The company has not publicly disclosed pricing, a common move for server processors, which are often sold through system builders and negotiated enterprise deals rather than as boxed retail chips.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

*Follow**Tom's Hardware on Google News**, or**add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

  


![Etiido Uko](https://cdn.mos.cms.futurecdn.net/BBrMt7jWtSo2Dc3iKoroyD.jpg)

Etiido Uko is a news contributor for Tom's Hardware covering the latest updates in big tech and the PC industry. He is a mechanical engineer and senior technical writer with over nine years of experience in documentation and reporting. He is deeply passionate about all things engineering and technology, and is an expert in gadgets, manufacturing, robotics, automotive, and aerospace.
