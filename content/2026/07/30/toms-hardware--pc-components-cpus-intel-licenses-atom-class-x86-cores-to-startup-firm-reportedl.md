---
title: Intel licenses Atom-class x86 cores to startup — firm reportedly sharing RTL,
  enabling customer to build its own custom processors based on x86 general-purpose
  cores
source_url: https://www.tomshardware.com/pc-components/cpus/intel-licenses-atom-class-x86-cores-to-startup-firm-reportedly-sharing-rtl-enabling-customer-to-build-its-own-custom-processors-based-on-x86-general-purpose-cores
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-30T14:31:11Z'
published: '2026-07-30T00:00:00Z'
description: RosaicLabs is the first company to get an x86 core from Intel in a decade.
image: https://cdn.mos.cms.futurecdn.net/3qAuWorrwTksrwq4GhoeEL-1920-80.png
---

![Intel](https://cdn.mos.cms.futurecdn.net/3qAuWorrwTksrwq4GhoeEL.png) 

After granting about a dozen manufacturing licenses to make various x86 CPUs back in the 1980s, Intel ceased to license both its cores and instruction set architecture (ISA) in a bid not to create rivals. However, in an unusual turn of events, Intel has quietly granted startup RosaicLabs access to its Atom processor technology, reports *Reuters*. The company was incorporated in May and is led by Lip-Bu Tan's co-investor.

 ![A hand holding the Ryzen 7 9850X3D.](https://cdn.mos.cms.futurecdn.net/Xh2MupWrRjJPiLLuopmKRB.jpg) 


Intel provided Rosaic access to an unknown Atom-class core, which enables the company to build its own custom processors based on x86 general-purpose cores, according to the report. The renowned chipmaker plans to ship Rosaic register-transfer level (RTL) code for the Atom processor core, which will let the startup build its custom system-on-chip (SoC) both at Intel Foundry and elsewhere.

The startup is reportedly led by Amarjit Gill, a venture capital investor who partnered with Intel's CEO, Lip-Bu Tan, on multiple occasions in the past. The two invested in such companies as Nuvia and Rivos, which were later acquired by Qualcomm and Meta, respectively.

RosaicLabs does not have a website or a LinkedIn profile, which is common for startups when they operate in stealth mode. The company was incorporated in May and is currently seeking a seed funding round of $10 million, according to a document seen by *Reuters*.

Since RosaicLabs does not have a website or a LinkedIn profile, it is completely unknown what kind of SoC it plans to develop and which markets it is going to pursue. One could imagine that it is in Intel's interests to license technology to companies that seek to address markets which Intel has no plans to address.

Arguably the biggest question is which Atom-class core Intel licensed to Rosaic. Traditionally, Atom cores were developed for inexpensive low-power devices, applications that Intel ceased to address about a decade ago. Since then, the low-power x86 architecture has been used to build custom SoCs for telecom and adjacent applications, embedded CPUs, efficiency (E) cores for client CPUs, and more recently cloud-optimized Xeon processors. Intel's most advanced low-power x86 cores to date are Crestmont, which powers Xeon 6700E-series CPUs, Skymont, which is used in Core Ultra 2-series CPUs, and Darkmont, which powers Xeon 6+ CPUs.

Skymont and Darkmont feature a 9-wide decode, 8-wide out-of-order engine, and 16-wide retire, which makes them fairly capable cores that wed high performance potential with energy efficiency. Meanwhile, Darkmont is optimized for data center workloads, so it has better branch prediction, improved prefetch, an enhanced vector engine, and higher L2 bandwidth. By contrast, Crestmont features a 6-wide decode and an 8-wide retire, which puts it well behind the newer cores.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

If Intel gives Rosaic complete, synthesizable RTL of an Atom-class core, Rosaic could technically modify the core at several levels, including changing cache sizes, reorganizing the pipeline, increasing clocks, and altering power-management logic, just to name a few options. However, this does not automatically mean Rosaic has unrestricted rights to enhance Intel's technology, as the company could provide RTL under various conditions with numerous restrictions. After all, it does not want to create a competitor for itself. Still, we do not know the terms of the license.

Intel granted about a dozen manufacturing licenses to build its 80286 and 80386 CPUs in the 1980s to various chipmakers in a bid to provide chipmakers with second sources for its processors and expand usage of its x86 ISA. However, only AMD got an actual x86 license that allowed it to build x86 CPUs of its own designs.

After disposing of its StrongArm/XScale business to Marvell in 2006, Intel witnessed the smartphone revolution essentially empty-handed as its Atom processors could not compete with highly integrated Arm-based SoCs in handsets. Intel tried to expand the reach of its low-power Atom CPU cores in 2009, so it signed a memorandum of understanding with TSMC and planned to port its Atom cores to a TSMC node and enable TSMC clients to integrate that hard IP into their processors.

That initiative has never taken off, so eventually Intel kicked off its SoFIA (Smart or Feature Phone on Intel Architecture) joint SoC development program that enabled third parties to use Intel Atom cores and modem technology (implemented using TSMC's 28nm node) in their application processors for handsets. While both Rockchip and Spreadtrum eventually came up with their SoFIA 3G and SoFIA 4G SoCs based on Airmont cores and made on TSMC's 28nm technology, both processors were released in 2015, had to compete against SoCs made on Samsung's 14nm-class node or TSMC's 16FFC node, and never got popular. Ultimately, Intel produced an eight-core Spreadtrum SoC at its fabs using its 14nm manufacturing technology, but that processor also failed on the market.

As a result, Intel licensing a CPU core to a third party is a very rare occurrence these days and the first in this decade. The reasons behind the move are completely unclear because the RosaicLabs startup is two months old, it cannot pay Intel cash, and its commercial prospects are completely unclear. While one may argue that now that Rosaic has access to x86 cores, it is not going to pursue Arm or RISC-V cores, keeping in mind that hundreds of startups choose Arm or RISC-V every year, addressing one startup does not enable Intel to expand its x86 share compared to Arm or RISC-V tangibly.

In any case, for now, the deal between Intel and RosaicLabs leaves more questions than answers, mainly because all we know about RosaicLabs is that it is led by an old acquittance of Intel's chief exec, Lip-Bu Tan.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Anton Shilov](https://cdn.mos.cms.futurecdn.net/uMZ5kNphxA2Ut6whdLaSQV.png)

Anton Shilov is a contributing writer at Tom’s Hardware. Over the past couple of decades, he has covered everything from CPUs and GPUs to supercomputers and from modern process technologies and latest fab tools to high-tech industry trends.

- 
That's intriguing and it could be a great ploy to get more customers at Intel Foundry.Reply
 
 It will be interesting to learn how new the core is, and how it's being used. It could be a fairly new core if Intel wants to use up spare newer fab capacity (since they still lack customers). And they could do something like take a Darkmont core and clock it like a Quark.
