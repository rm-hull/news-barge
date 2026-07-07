---
title: AVX-512 support is reportedly returning with Intel's next-gen Nova Lake CPUs
  — Latest Linux kernel patches reveal P-cores and E-cores will gain native 512-bit
  execution
source_url: https://www.tomshardware.com/pc-components/cpus/avx-512-support-is-reportedly-returning-with-intels-next-gen-nova-lake-cpus-latest-linux-kernel-patches-reveal-p-cores-and-e-cores-will-gain-native-512-bit-execution
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-07T15:09:15Z'
published: '2026-07-07T00:00:00Z'
description: Solving a major hurdle for modern Intel CPUs.
image: https://cdn.mos.cms.futurecdn.net/6dhScSyVh9hBM75rUoJ4qN-2560-80.jpg
---

![Intel 12th Generation Alder Lake CPU](https://cdn.mos.cms.futurecdn.net/6dhScSyVh9hBM75rUoJ4qN.jpg) 

When Intel switched to a hybrid architecture with its 12th-Gen Alder Lake PUs, it removed AVX-512 support from the lineup entirely because the E-cores didn't support it. Since then, every subsequent generation has shipped without it... until now. Just today, a new Linux patch pushed in the RAID optimized path has revealed that AVX-512 is finally returning to Intel CPUs with Nova Lake, present on both P-cores and E-cores.

 ![Linux patch adding support for 512-bit execution on Intel Nova Lake CPUs](https://cdn.mos.cms.futurecdn.net/4V7xfu99PwLxQBDWafjkLP.png) 


Intel has been working toward a unified AVX solution for the past few years, as it was originally a champion of the SMID extensions before running into the hybrid hurdle with Alder Lake. Getting past that hurdle is AVX10, which Intel first detailed a few years back. With AVX10.2, 512-bit instructions will run on the P-cores, while either core type can handle converged 256-bit instructions.

As such, the E-cores would have their processing width capped at 256-bit, while the P-cores would be open to the full 512-bit wide pipelines. Any thread could swiftly move between either core type with AVX10 implemented. Previously, if the scheduler shifted a 512-bit task running on a P-core to an E-core, the application would crash instantly because those E-cores couldn't process the instruction.

However, the new patches suggest that Intel has now mandated native 512-bit execution across both P-cores and E-cores, no longer requiring the latter to step down and process the data a bit slower. This is a major development over the standard we originally expected Intel to adopt; the E-cores are apparently becoming just as performant as the P-cores when it comes to SIMD instructions with Nova Lake and later.

Intel's original announcement showed that it had already uncoupled the software improvements of AVX-512 from the physical width of the register, so the new instruction features could remain present for both 512-bit and 256-bit execution. This includes things like masking, embedded broadcast for rounding math operations, and doubling the number of the registers themselves from 16 to 32.

It remains unclear if we will ever see this version of AVX10 on client CPUs, as it seems Nova Lake is going purely for 512-bit execution across both core types. AMD's current-gen Zen 5 processors also have full 512-bit wide registers, while the previous Zen 4 architecture divided a single 512-bit task across two 256-bit execution units over two clock cycles. This ensured execution remained disruption-free even if it took longer.

 ![AVX-512 benchmark on Ryzen 9 9950X](https://cdn.mos.cms.futurecdn.net/UKds7BfWYk7MrPtwvENGtZ.png) 


The last time we saw native AVX-512 support on an Intel client family was Rocket Lake (11th Gen), right before the hybrid era ushered in by Alder Lake. For modern AI workloads and other compute-heavy tasks such as encoding or simulations, AVX-512 instructions bring a huge performance benefit that's foolish to be left on the table. Keep in mind that this is just a Linux patch at the moment and that Intel hasn't officially announced native AVX-512 support for Nova Lake yet.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Hassam Nasir](https://cdn.mos.cms.futurecdn.net/SxxNFHt95eGK37mKPhJpdZ.jpg)

Hassam Nasir is a die-hard hardware enthusiast with years of experience as a tech editor and writer, focusing on detailed CPU comparisons and general hardware news. When he’s not working, you’ll find him bending tubes for his ever-evolving custom water-loop gaming rig or benchmarking the latest CPUs and GPUs just for fun.
