---
title: AMD Zen 6 EPYC ‘Venice’ deep dive and benchmarking – 9686F outclasses Nvidia’s
  Vera, dual EPYC 9996 with 1,024 threads delivers up to 93% performance gain gen-on-gen
source_url: https://www.tomshardware.com/uk/pc-components/cpus/amd-zen-6-epyc-venice-deep-dive-and-benchmarking-dual-epyc-9996-with-1-024-threads-delivers-up-to-93-percent-performance-gain-gen-on-gen-9686f-outclasses-nvidias-vera
source_site: Tom's Hardware
source_slug: toms-hardware
description: AMD has pulled back the curtain on its Zen 6 microarchitecture. We deep-dive
  into the differences between Zen 5 and 6, as well as detail our first benchmarks
  of AMD’s Venice CPUs.
image: https://cdn.mos.cms.futurecdn.net/ZAgiNFCzjQaAkvL44NaxPC-1920-80.jpg
published: '2026-11-10T00:00:00Z'
scraped_at: '2026-11-10T19:43:00Z'
categories:
- Technology & Software
- Hardware
people:
- Jake Roach
- Java SciMark
- Python
- Vera
- Zen
locations:
- C-Ray
- CloverLeaf
- Genoa
- Godot
- ImageMagick
- Monte Carlo
- Nigeria
- Octave
- Turin
- Venice
- Zen 5
organisations:
- 9686F
- AI
- ALU
- ALU/AGU
- AMD Zen
- BPU
- CCD
- DaCapo
- Diamond Rapids
- EPYC
- FFTE
- FP
- GCC
- Get Tom's Hardware
- Granite Rapids-AP
- HPC
- HPE
- IOD
- IPC
- Intel
- Intel’s E-cores
- Java SciMark
- LLMs
- LLVM
- MEXT
- Micron
- N2
- N2P
- Ninja
- Nvidia
- Power Scaling
- Python
- RAM
- SK
- SKU AMD
- SP5
- SP7
- SP8
- SPEC
- Samsung
- TSMC
- Team Red
- Tom’s Hardware
- Turin
- UBPS
- UPP
- Venice
- Venice-X
- Venice’ CPUs
- Vera CPU
- Zen 6
- Zen 6c
---

![AMD Zen 6 EPYC ‘Venice’](https://cdn.mos.cms.futurecdn.net/ZAgiNFCzjQaAkvL44NaxPC-1920-80.jpg)

AMD’s EPYC ‘Venice’ CPUs are the first to debut the new Zen 6 architecture, and we’ve been testing two chips from the range over the past several weeks to see how they compare to Nvidia’s Vera, and more broadly, how the Zen 6 architecture departs from Zen 5 ahead of the expected consumer-focused Olympic Ridge launch next year. Zen 5 was a ground-up redesign of AMD’s storied Zen core, and Zen 6 takes that foundation and expands it in just about every regard.

Zen 6 uses TSMC’s N2P node, but it also comes with significant architectural changes under the hood. Within the core, a redesigned vector engine pushes AMD’s SIMD performance even higher, and it now natively supports half-precision FP16 instructions alongside full, 32-bit precision. It also splits integer schedulers within the execution engine, allowing for more instructions in flight through the core.

Across the die, AMD made other significant changes. The single IOD of previous generations is now split across two IODs, giving the SP7 platform access to 16 memory channels (though at the cost of PCIe 6.0 lanes compared to the previous generation and SP8 platform).

The CCDs have been upgraded, too, for the first time since Zen 3. A standard Zen 6 CCD can now scale up to 12 cores, while a Zen 6c packs 32 cores. With Zen 5 and 5c, CCDs topped out at eight cores and 16 cores, respectively. For the Zen 6c CCD, AMD also doubled the amount of shared L3 per core, which effectively quadruples the L3 compared to Zen 5c, since the CCD packs twice the number of cores.

Interestingly, Zen 6 is neither a marginal optimization to Zen 5, nor a complete architecture redesign. Stepping back, it looks like AMD pushes as many dials as it has access to to their highest level, and that holds up looking at performance.

The 256-core EPYC 9996 delivers 1,024 threads in a 2P configuration, which came out 93% ahead of the 768-thread 2P EPYC 9965 server we tested in SPEC CPU 2026’s intrate throughput test. The frequency-optimized EPYC 9686F excels elsewhere, notably in scientific computing and HPC workloads, and it serves as AMD’s competitor to Vera, at least before the LPDDR-based Verano platform arrives from AMD next year.

AMD says it believes Venice is fundamentally a generation ahead of the competition, which would be a worthless line if it wasn’t backed up by data. Intel’s Granite Rapids-AP is rarely in the conversation, and although Vera maintains some competitive positions, Venice is often ahead — sometimes orders of magnitude ahead.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Intel’s Diamond Rapids is set to launch next year, which should help balance the scales. But AMD has set an incredibly high bar with Venice, one that it will likely extend even higher for some workloads with the arrival of Venice-X and Verano next year.

There’s a lot to get to here. We have a full deep dive into the Zen 6 microarchitecture, a broader look at the chip itself, the platform(s) AMD is pushing out this generation, and of course, more than 100 benchmarks covering everything from Python performance to HPC.

### AMD Zen 6 microarchitecture breakdown

## AMD Zen 6 microarchitecture breakdown

![AMD Zen 6 EPYC &amp;lsquo;Venice&amp;rsquo;](https://cdn.mos.cms.futurecdn.net/YaHrhTsQ6xQWXh3ZxynzkB-1200-80.jpg)

The headline for Zen 6 is a 27% average IPC uplift over Zen 5 in enterprise, cloud, and AI workloads. The debut of this new microarchitecture is focused on the data center, so you shouldn’t take that 27% IPC improvement as broadly applicable to all workloads. Additionally, AMD arrived at that number by comparing fixed-frequency Zen 5 to Zen 6c with 16 cores. As we’ll get into in the next section, a Zen 6c CCD can comfortably fit 16 Zen 6c cores with room to spare, while 16 Zen 5 cores are split across two CCDs.

The compute die is built on TSMC’s N2P node, which is an already optimized version of N2 that comes with a 5% performance improvement. Compared to N3E (Zen 5 used N4P), N2P offers an 18% speed improvement at iso-power, or a 36% reduction in power at the same speed.

|  |  |  |  |
| --- | --- | --- | --- |
| Row 0 - Cell 0 | **Speed Improvement (v. N3E)**|** Power Improvement (v. N3E)**|** Density (v. N3E)** |
| **TSMC N2P** | +18% (iso-power) | -36% (iso-speed) | +15% |

AMD described Zen 5 as a ground-up redesign when the microarchitecture first broke cover in mid-2024, characterized by a wider execution engine capable of dispatching and returning eight instructions per cycle, a wider frontend to feed it, full AVX-512 support, and doubled bandwidth between the L2 and L1 cache. Zen 6 is a continuation of the redesign we saw on Zen 5. It carries many of the same characteristics, as well as the same general topology, just enhanced in a number of ways.

As we go through the breakdown, keep in mind that Zen 6 and Zen 6c use the same microarchitecture. Zen 6c is just a space-optimized design that consumes less power, clocks lower, and, obviously, takes up less die space than a full Zen 6 core. But, the company uses the same microarchitecture inside the core, unlike Intel’s E-cores, which use a different microarchitecture than the P-cores.

![AMD Zen 6 EPYC &amp;lsquo;Venice&amp;rsquo;](https://cdn.mos.cms.futurecdn.net/Y5PLEFj49A7mPrAqyghMQC-1200-80.jpg)

Starting with the frontend, it’s largely unchanged from Zen 5, short of a few notable improvements. You get the same dual 4-wide decode pipes and 8-dispatch, but AMD has improved the BPU and op cache. For the BPU, it has a 64-entry Return Address Stack, up from 52 on Zen 5. AMD also increased the op cache size back up to 6.75K entries from 6K on Zen 5 (Zen 4 also had a 6.75K-entry op cache). This larger cache can serve up to 18 micro-ops per cycle, up from 12 on Zen 5.

![AMD Zen 6 EPYC &amp;lsquo;Venice&amp;rsquo;](https://cdn.mos.cms.futurecdn.net/94EcMjDSgd9zDiBdSaDXNC-1200-80.jpg)

AMD split the integer schedulers for Zen 6 (Zen 5 had a unified scheduler), now offering higher capacity, with 96 shared ALU/AGU and 48 dedicated ALU entries, compared to an 88 / 56 split for ALU/AGU on Zen 5. AMD also expanded the general-purpose registers to a 352-entry physical register file, up from 240 on Zen 5.

![AMD Zen 6 EPYC &amp;lsquo;Venice&amp;rsquo;](https://cdn.mos.cms.futurecdn.net/pX2S4KTSAKpDhPPq7p9MQC-1200-80.jpg)

The vector execution engine is also improved, following on the heels of a true 512-bit register in Zen 5. Zen 6 carries forward that 512-bit data path and adds some additional improvements. Notably, the engine now supports half-precision AVX-512 FP16 instructions, which needed to be converted in Zen 5’s vector execution engine. Also notable is the FP load/store bandwidth. Zen 5 supports two loads of any size, but Zen 6 supports either two 512-bit loads or four 256-bit loads. Store bandwidth is unchanged, at one 512-bit store or two 256-bit stores.

![AMD Zen 6 EPYC &amp;lsquo;Venice&amp;rsquo;](https://cdn.mos.cms.futurecdn.net/mJX87MD3WsY5fH4TwY3DvB-1200-80.jpg)

Zen 6 carries forward the 48 KB 12-way L1 data cache from Zen 5, along with 1 MB 16-way private L2. The shared L3 is treated as victim cache for the L2, as is the case in Zen 5. However, AMD increased the in-flight window compared to Zen 5, with an 80-entry load queue and 128-entry store queue.

### AMD Zen 6 and Zen 6c CCD and platform breakdown

## AMD Zen 6 and Zen 6c CCD and platform breakdown

![AMD Zen 6 EPYC &amp;lsquo;Venice&amp;rsquo;](https://cdn.mos.cms.futurecdn.net/EH5o4YSFJsAKqFed7DKJQC-1200-80.jpg)

Perhaps the biggest change going from Zen 5 to Zen 6 comes in the density of the CCD. Zen 6 offers up to 12 cores per CCD, up from 8 on Zen 5, while Zen 6c scales up to 32, double that of Zen 5c. Elsewhere, the updated CCDs either match or improve on Zen 5/5c CCDs.

For Zen 6, AMD retained the 4 MB of L3 cache per core, increasing the total cache to 48 MB to accommodate the new 12-core limit. The maximum frequency of a standard Zen 6 CCD has increased from 5 GHz on Zen 5 to 5.3 GHz on Zen 6. Keep in mind these clocks are in the context of Venice; we expect higher maximum boost clocks on consumer Olympic Ridge.

Zen 6c has more enhancements. AMD doubled the amount of L3 per core from 2 MB to 4 MB, matching the normal Zen 6 CCD. And, with double the L3 per core and double the number of cores, the Zen 6c CCD has a total of 128 MB of L3, quadruple that of a Zen 5c CCD. For Zen 6c, the maximum frequency is also up, going from 3.7 GHz on Zen 5c to 4.1 GHz on Zen 6c.

![AMD Zen 6 EPYC &amp;lsquo;Venice&amp;rsquo;](https://cdn.mos.cms.futurecdn.net/QZupd9HQSPciNhrFiUApRC-1200-80.jpg)

Across both, AMD claims a “large core IPC uplift,” as well as improved power and SMT efficiency. We haven’t seen an overall IPC claim yet, though the numbers referenced above put Venice at about a 27% advantage over Turin in enterprise, cloud, and AI workloads.

![AMD Zen 6 EPYC &amp;lsquo;Venice&amp;rsquo;](https://cdn.mos.cms.futurecdn.net/AdXLFQNrWtQ6KBeqNSqMwB-1200-80.jpg)

In the context of Venice, AMD can fit up to eight CCDs on a chip, coming out to 256 cores in total for Zen 6c, and 96 cores total for regular Zen 6 for SP7 platforms (the initial lineup for Venice). AMD is moving past the SP5 socket available to Genoa and Turin CPUs for SP7, which is a slightly larger socket at 76 x 80 mm (SP5 is ~72 x 75 mm).

![AMD Zen 6 EPYC &amp;lsquo;Venice&amp;rsquo;](https://cdn.mos.cms.futurecdn.net/gzPfDY7rMmjT8T6i4FfMQC-1200-80.jpg)

The topology of the chip is largely intact from Turin, short of the dual IO dies that characterize Venice. The two IODs live in the middle of the chip, flanked by Zen 6 CCDs. The second IOD is what gives SP7 chips access to 16 channels of memory per socket (8 channels per IOD), supporting up to 12,800 MT/s speeds using MRDIMMs in a 1DPC configuration. With RDIMMs, AMD supports up to 8,000 MT/s. The platform supports up to 8 TB of memory per socket, and AMD claims bandwidth of up to 1.6 TB/s per socket (1 TB/s per socket with RDIMMs).

Also on the IOD, there’s the hardware root-of-trust, as well as AMD’s confidential computing extensions, including execution encryption, memory integrity, and trusted I/O. New to the platform is PCIe 6.0 at speeds up to 64 Gbps per lane. A 1P SP7 configuration has access to 96 PCIe 6.0 lanes, while a 2P platform has up to 128. Each configuration also comes with “bonus” PCIe 4.0 lanes, either 8 for 1P configs or 16 for 2P.

![AMD Zen 6 EPYC &amp;lsquo;Venice&amp;rsquo;](https://cdn.mos.cms.futurecdn.net/n6YyLDkWDHmpS25Kdx88RC-1200-80.jpg)

Two 64G SerDes interfaces bring the PCIe lanes into the IOD, one of which is used to link the chips in a 2P configuration. That second interface can still optionally handle an additional 12 PCIe 6.0 lanes, giving the “up to” 128 2P lanes number. The bonus lanes run through a smaller 16G SerDes interface.

Platforms with the SP8 socket trade memory channels for PCIe lanes. The SP8 socket is smaller at 62.5 x 80 mm, and the platform supports eight memory channels instead of 16, though with the same support for up to 12,800 MT/s MRDIMMs. Memory bandwidth drops to 819 GB/s for MRDIMMs and 512 GB/s for RDIMMs at the maximum supported transfer rate.

![AMD Zen 6 EPYC &amp;lsquo;Venice&amp;rsquo;](https://cdn.mos.cms.futurecdn.net/cYTMttFHwr4uTTs74rwWDC-1200-80.jpg)

However, SP8 chips have access to 64 PCIe 6.0 lanes per IOD, for a total of 128 lanes in a socket (plus the additional eight PCIe 4.0 bonus lanes). Just like SP7, some of those lanes are shared in a 2P configuration, dropping the total to 192 PCIe 6.0 lanes in 2P SP8 servers, with 16 additional PCIe 4.0 lanes. Both platforms support CXL 3.1.

![AMD Zen 6 EPYC &amp;lsquo;Venice&amp;rsquo;](https://cdn.mos.cms.futurecdn.net/gzPfDY7rMmjT8T6i4FfMQC-1200-80.jpg)

AMD also provided a platform breakdown for its upcoming Verano range, which uses the Zen 6 microarchitecture on an LPDDR5X-based platform, leveraging replaceable SOCAMM2 DIMMs.

### UPP, UBPS, and FAST in Zen 6 ‘Venice’ CPUs

## UPP, UBPS, and FAST in Zen 6 ‘Venice’ CPUs

![AMD Zen 6 EPYC &amp;lsquo;Venice&amp;rsquo;](https://cdn.mos.cms.futurecdn.net/2NG95c7KC66tP4JxYNq9PC-1200-80.jpg)

AMD has added a few quality-of-life features to Venice CPUs that should make them easier to manage when actually deployed. First is UPP, or Unified Power Provisioning, which is a power management feature that takes into account total platform power, allocating it as needed to different components, depending on the workload. With it, AMD says it’s able to deliver a power consumption of 830W on 16 servers to 706W on 18 servers, or a decrease in provisioned power by 15%, while increasing the number of servers per rack.

Also dealing with power is UBPS, or Utilization Based Power Scaling. It’s a dynamic power scaling feature that aligns with whatever workload is running on the server, which AMD says “helps close the gap between provisioned and consumed power.” Like UPP, UBPS is concerned with platform power, not just the power consumption of the CPU.

![AMD Zen 6 EPYC &amp;lsquo;Venice&amp;rsquo;](https://cdn.mos.cms.futurecdn.net/Yavy56LNfxjMH6MDBCLTyB-1200-80.jpg)

The most interesting addition is FAST, or Frequency Adaptive Spectrum Technology. The feature takes in telemetry from the platform and policies set in firmware to adjust the frequency within set power and thermal limits. It sounds a little more involved than a simple Precision Boost Overdrive for the data center, however.

AMD described FAST to us as allowing for two performance tiers within one socket. As an example, AMD pointed to a 96-core Venice CPU, saying FAST allows 32 of those cores to run in a “premium” category, with a base clock of 3.65 GHz and a max clock of 5 GHz, while a “batch” category with 64 cores runs at 2 GHz with a 2.4 GHz max. AMD described it as multiple commercial SKUs within a single socket.

### Preliminary MEXT support, claims of 95% performance at 50% DRAM capacity

![AMD Zen 6 EPYC &amp;lsquo;Venice&amp;rsquo;](https://cdn.mos.cms.futurecdn.net/YvhiFW3iuTKEhtHHPTskpB-1200-80.jpg)

Venice marks the point when AMD will start offering MEXT on its EPYC platforms. AMD aquired MEXT earlier this year, and it has used the feature internally. With HPE, AMD is rolling out “MEXT ready” platforms, which will, eventually, have access to MEXT licenses. The technology is interesting, especially given how constrained memory is right now.

The general concept of MEXT is using flash as DRAM. Even the fastest flash is orders of magnitude slower than DRAM, but MEXT attempts to take advantage of DRAM access patterns to expose more memory to the system without it actually being there. Pages that haven’t been accessed in several minutes are offloaded to flash storage, and an AI model predicts pages that are needed. Then, those pages are loaded back into memory as you need them.

![AMD Zen 6 EPYC &amp;lsquo;Venice&amp;rsquo;](https://cdn.mos.cms.futurecdn.net/aErTj9bcQqcBJzYKrf6jvB-1200-80.jpg)

Conceptually, it sounds too good to be true. AMD pointed out that MEXT is using a transformer-based LLM, and effectively, LLMs are predicting what words go next when generating text. Here, AMD says the bar isn’t even that high. As long as the model can stream the correct pages in, and do so fast enough to cover the flash latency, the order of them doesn’t matter.

MEXT is delivered through a Linux kernel module, and AMD has bold claims about its capabilities. The company has deployed the software internally on 145 servers, which it expects to expand to over 2,000 servers next year. Currently, AMD is using it for critical EDA workflows, such as Synopsis PrimeTime. The company says that it’s able to maintain 95% of the application’s performance on Venice with just 50% of the system DRAM. Going down as low as 25%, the company claims the app maintains 80% of its performance.

![AMD Zen 6 EPYC &amp;lsquo;Venice&amp;rsquo;](https://cdn.mos.cms.futurecdn.net/Eierc7P4xnLyxQHnrgGSnB-1200-80.jpg)

We’ll have more on MEXT shortly. The feature is exclusive to EPYC CPUs, and AMD was clear that it only applies to certain workloads right now. There are likely applications where you won’t be able to cut the DRAM capacity of a server, or where you’ll need to use a more conservative cut of 25% or less.

### AMD Zen 6 EPYC ‘Venice’ test configurations

## AMD Zen 6 EPYC ‘Venice’ test configurations

AMD gave us access to two Zen 6 Venice systems for the purpose of testing, both of which were dual-socket servers. For the first system, we tested the dense EPYC 9996, which is AMD’s high-core-count design, packing 256 cores and 512 threads per socket, for a total of 512 cores and 1024 threads across a 2P system. It’s a peak throughput SKU, designed to handle heavily concurrent workloads.

On the other end of the spectrum, we have the EPYC 9686F, which is still a high core count CPU in its own right, with 96 cores and 192 threads, giving a 2P system 192 cores and 384 threads. The “F” suffix for AMD’s data center CPUs notes a high-frequency SKU, designed to push performance up in more demanding applications, as opposed to the dense, frontend-focused EPYC 9996.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Chip**|** Cores / Threads**|** Base / Boost Clock (GHz)**|** L3 Cache**|** TDP** |
| **Epyc 9996**|** 256 / 512**|** 2.55 / 4.1**|** 1024 MB**|** 600W** |
| Epyc 9966 | 192 / 384 | 2.9 / 4 | 768 MB | 600W |
| Epyc 9846 | 168 / 336 | 2.85 / 3.7 | 768 MB | 500W |
| Epyc 9756 | 128 / 256 | 3.15 / 4 | 512 MB | 500W |
| Epyc 9G76 | 96 / 192 | 3.4 / 4.8 | 384 MB | 500W |
| Epyc 9656 | 96 / 192 | 3.05 / 3.7 | 512 MB | 400W |
| **Epyc 9686F**|** 96 / 192**|** 3.4 / 5**|** 384 MB**|** 500W** |
| Epyc 9556 | 64 / 128 | 2.75 / 4.3 | 384 MB | 300W |
| Epyc 9586F | 64 / 128 | 3.75 / 5 | 384 MB | 500W |

Both chips use AMD’s SP7 socket, which is geared toward data centers, with higher core count SKUs. The upcoming SP8 socket is focused on enterprise customers, with smaller core counts and support for fewer memory channels.

Although the EPYC 9996 is a dense design with the Zen 6c core, it comes with a fairly high boost clock of 4.1 GHz, though a much lower 2.55 GHz base clock, which it will likely be running closer to in real deployments. It comes with a massive 1,024 MB pool of L3 for the chip, as well as a 600W rated TDP, though it can be manually adjusted between 400W and 600W.

The EPYC 9686F proves out AMD’s claims about Venice, serving as one of two chips in the SP7 lineup to boost up to 5 GHz. It has a lower 500W TDP, though it can again run between 400W and 600W. This is the SKU AMD has heavily referenced in its published Venice benchmarks as a “96-core HF” model.

It’s an interesting model, perhaps more so than the EPYC 9996. It’s in direct competition with Nvidia’s Vera CPU, not only based on core count, but also on performance. These two chips trade blows in several benchmarks, and it’s clear that AMD is pushing this SKU as its “agentic CPU” of the Venice lineup, similar to how Nvidia has positioned Vera.

|  |  |  |
| --- | --- | --- |
| **Test Platform**|** Memory**|** Tested Processors** |
| 2P AMD Nigeria reference platform | 32 x 64 GB (2TB) SK hynix DDR5-12800 ECC MRDIMM | AMD EPYC 9996, EPYC 9686F |
| 2P AMD Volcano reference platform | 24 x 64 GB (1.5 TB) SK hynix DDR5-6000 ECC RDIMM | AMD EPYC 9965, EPYC 9755 |
| 2P Supermicro SYS-222HA | 24 x 64GB (1.5 TB) Micron DDR5-8800 ECC MRDIMM | Intel Xeon 6980P |
| 2P Nvidia MGX Vera reference platform | 16 x 96 GB (1.5 TB) Samsung LPDDR5-9600 ECC SOCAMM2 | Nvidia Vera |

You can see the platforms we tested above. The Nigeria reference platform we tested these Zen 6 chips on came with top-end DDR5-12800 MRDIMMs, arranged to fully saturate the 16-channel memory with 32 sticks. This massive jump in memory support is a critical aspect of Venice, particularly for the hotly contested EPYC 9686F and its all-important matchup against Vera.

Vera’s use of LPDDR5 SOCAMM2 memory allows for higher transfer rates than standard RDIMMs in a field-replaceable package, though through a relatively tame eight-channel setup. Vera can get away with 8-channel memory, however, with its topology allowing for massive data movement across the chip. AMD’s distributed design necessitates a bigger memory configuration, with double the channels and access to even higher transfer rates through the use of MRDIMMs.

### AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates

Starting off our benchmarks is SPEC CPU 2026, the de facto industry benchmark for server CPU performance. As usual with SPEC runs, the numbers below are “estimates.” We gathered the numbers from real SPEC runs, but we haven’t reported them to the SPEC committee, so they remain “estimates.”

For the throughput benchmark suites, intrate and fprate, we ran a number of copies for each application equal to the thread count of the chip. All of our tests were run on Ubuntu Server 26.04 with Linux Kernel 7.0, and we used GCC 15.2 for all but the Venice chips. GCC 16 brings official support for Zen 6, which we used here. However, we did regression testing against GCC 15 and found only minor differences, and nothing that would change our standings.

Using GCC 16 was important to keep our optimization flags equal. We used common GCC flags, including fast link-time optimization and march/mcpu flags to expose the correct processor instruction support. We also used the open-source jemalloc memory allocator across all tested systems.

![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Int Rate](https://cdn.mos.cms.futurecdn.net/Qmno2gpXRY3HqvfWbD5D9o-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Intrate](https://cdn.mos.cms.futurecdn.net/SVzoyJp97NFWRXDPwiimHn-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Intrate](https://cdn.mos.cms.futurecdn.net/bfvPSSJQU5n7LLNYvzn69o-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Intrate](https://cdn.mos.cms.futurecdn.net/mkrDZPT8pmoeAKRVpPmv8o-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Intrate](https://cdn.mos.cms.futurecdn.net/tQVqKG7RixWinqFXgnaj8o-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Intrate](https://cdn.mos.cms.futurecdn.net/vjteFWzveDFEZRwVAQdX8o-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Intrate](https://cdn.mos.cms.futurecdn.net/MphSr9kXjztSkUbLtFRV8o-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Intrate](https://cdn.mos.cms.futurecdn.net/iFYWCjJuPYV8xmoKRpNU8o-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Intrate](https://cdn.mos.cms.futurecdn.net/Fe2kdiZfkUMYcV35LXSk7o-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Intrate](https://cdn.mos.cms.futurecdn.net/dnA6Xj5UYtjLRVv5kVxd7o-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Intrate](https://cdn.mos.cms.futurecdn.net/PFGrEkZ7iTtC3L9QKoUd7o-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Intrate](https://cdn.mos.cms.futurecdn.net/EG8EGMijUVSkeHdQhrfosn-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Intrate](https://cdn.mos.cms.futurecdn.net/nmsRnDG6CZW2DroYoCTehn-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Intrate](https://cdn.mos.cms.futurecdn.net/zprvu4uWDJ3mJcnQk3gNhn-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Intrate](https://cdn.mos.cms.futurecdn.net/RmuFwQ2tDttqfZvpsbrUan-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Int Rate](https://cdn.mos.cms.futurecdn.net/Qmno2gpXRY3HqvfWbD5D9o-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Intrate](https://cdn.mos.cms.futurecdn.net/SVzoyJp97NFWRXDPwiimHn-2440-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Intrate](https://cdn.mos.cms.futurecdn.net/bfvPSSJQU5n7LLNYvzn69o-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Intrate](https://cdn.mos.cms.futurecdn.net/mkrDZPT8pmoeAKRVpPmv8o-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Intrate](https://cdn.mos.cms.futurecdn.net/tQVqKG7RixWinqFXgnaj8o-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Intrate](https://cdn.mos.cms.futurecdn.net/vjteFWzveDFEZRwVAQdX8o-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Intrate](https://cdn.mos.cms.futurecdn.net/MphSr9kXjztSkUbLtFRV8o-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Intrate](https://cdn.mos.cms.futurecdn.net/iFYWCjJuPYV8xmoKRpNU8o-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Intrate](https://cdn.mos.cms.futurecdn.net/Fe2kdiZfkUMYcV35LXSk7o-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Intrate](https://cdn.mos.cms.futurecdn.net/dnA6Xj5UYtjLRVv5kVxd7o-2440-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Intrate](https://cdn.mos.cms.futurecdn.net/PFGrEkZ7iTtC3L9QKoUd7o-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Intrate](https://cdn.mos.cms.futurecdn.net/EG8EGMijUVSkeHdQhrfosn-2440-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Intrate](https://cdn.mos.cms.futurecdn.net/nmsRnDG6CZW2DroYoCTehn-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Intrate](https://cdn.mos.cms.futurecdn.net/zprvu4uWDJ3mJcnQk3gNhn-2440-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Intrate](https://cdn.mos.cms.futurecdn.net/RmuFwQ2tDttqfZvpsbrUan-2440-80.png)

The overall intrate scores set the tone, particularly for the EPYC 9996. It has access to 1,024 threads in a 2P configuration, multiplying the clear speed improvements in Zen 6 broadly across more threads compared to last-gen’s top-end EPYC 9965. The 9996 scored a massive 93% higher in this test, though that number requires some context.

Both throughput benchmarks in SPEC reward not only how much work is done, but also how *quickly* it’s done. With access to a much larger thread pool and improvements in Zen 6 broadly, there’s that multiplicative effect when looking at pure throughput. A 2P EPYC 9996 system is 93% faster than a 2P EPYC 9965 system in this benchmark, but not broadly across the board.

The EPYC 9686F provides some context, which is still good news for AMD, just not on the level of doubling the performance of the previous generation. We unfortunately didn’t have access to a 9575F for a closer gen-on-gen comparison, but the EPYC 9755 is a decent proxy, with its 128 cores and relatively high 4.1 GHz boost clock. Compared with that CPU, the EPYC 9686F in a 2P configuration is 19% ahead — not too shabby considering the thread disadvantage.

Critically for AMD, the EPYC 9686F is also 17% ahead of Nvidia’s Vera CPU. Vera punches far above its weight class compared to the x86 competition, as evidenced by its matchup against the 9755 and Intel’s flagship Granite Rapids-AP 6980P.

![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - FP Rate](https://cdn.mos.cms.futurecdn.net/pYDiY3WZTPbtH7y9vixdpW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - FP Rate](https://cdn.mos.cms.futurecdn.net/HQNjhTxAvxSDYY7NcETfCW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - FP Rate](https://cdn.mos.cms.futurecdn.net/9zNJwALoqMGJ3UNCAHCbpW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - FP Rate](https://cdn.mos.cms.futurecdn.net/yKyRjpThpS7aCZi3ZqyMpW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - FP Rate](https://cdn.mos.cms.futurecdn.net/zaxUUpFrAC2SdempdTQ4pW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - FP Rate](https://cdn.mos.cms.futurecdn.net/Wg2no8PS9Y6nkNWLxvcuoW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - FP Rate](https://cdn.mos.cms.futurecdn.net/Q5cY8fqTEYoxbzknUC5soW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - FP Rate](https://cdn.mos.cms.futurecdn.net/iabHeHtgbvsBKjctvzUqoW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - FP Rate](https://cdn.mos.cms.futurecdn.net/2zdVscyS6EXJM5DMeVSqoW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - FP Rate](https://cdn.mos.cms.futurecdn.net/Bjdy32aZ7LvYevoZjDXJoW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - FP Rate](https://cdn.mos.cms.futurecdn.net/i2UdHiC8eoFA73aDfmZvnW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - FP Rate](https://cdn.mos.cms.futurecdn.net/3LSEBFeg4G8QaicYuKkynW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - FP Rate](https://cdn.mos.cms.futurecdn.net/t4WDErYtXkTqPXJyGNQCZW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - FP Rate](https://cdn.mos.cms.futurecdn.net/pYDiY3WZTPbtH7y9vixdpW-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - FP Rate](https://cdn.mos.cms.futurecdn.net/HQNjhTxAvxSDYY7NcETfCW-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - FP Rate](https://cdn.mos.cms.futurecdn.net/9zNJwALoqMGJ3UNCAHCbpW-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - FP Rate](https://cdn.mos.cms.futurecdn.net/yKyRjpThpS7aCZi3ZqyMpW-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - FP Rate](https://cdn.mos.cms.futurecdn.net/zaxUUpFrAC2SdempdTQ4pW-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - FP Rate](https://cdn.mos.cms.futurecdn.net/Wg2no8PS9Y6nkNWLxvcuoW-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - FP Rate](https://cdn.mos.cms.futurecdn.net/Q5cY8fqTEYoxbzknUC5soW-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - FP Rate](https://cdn.mos.cms.futurecdn.net/iabHeHtgbvsBKjctvzUqoW-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - FP Rate](https://cdn.mos.cms.futurecdn.net/2zdVscyS6EXJM5DMeVSqoW-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - FP Rate](https://cdn.mos.cms.futurecdn.net/Bjdy32aZ7LvYevoZjDXJoW-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - FP Rate](https://cdn.mos.cms.futurecdn.net/i2UdHiC8eoFA73aDfmZvnW-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - FP Rate](https://cdn.mos.cms.futurecdn.net/3LSEBFeg4G8QaicYuKkynW-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - FP Rate](https://cdn.mos.cms.futurecdn.net/t4WDErYtXkTqPXJyGNQCZW-2439-80.png)

Flipping over to float performance, AMD did a lot of work on the vector engine in Zen 6, and it shows up in fprate. The differences between the EPYC 9996 and 9686F are smaller, though not in a way where both chips are hamstrung. Rather, the EPYC 9696F is able to push up closer to the 9996, leaving both Zen 6 chips running circles around the field.

AMD more than doubled the score with its Zen 6 chips compared to our Zen 5 touchpoints, which is a massive achievement. The EPYC 9686F excels even more over Vera in fprate with a 40% lead, despite only a minor bump in core count (88 on Vera to 96 on the 9686F). Intel’s Granite Rapids-AP isn’t in the conversation here for raw performance; though, apparently the range is still in high-enough demand that Intel has increased production in the tight CPU environment we’re currently experiencing.

![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Int Speed](https://cdn.mos.cms.futurecdn.net/7pActa32VdPjdEio5C5G8i-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Int Speed](https://cdn.mos.cms.futurecdn.net/dtUB4iVnAFPbejj78V2WVh-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Int Speed](https://cdn.mos.cms.futurecdn.net/eV66LsffcvVkuvr7vxZB7i-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Int Speed](https://cdn.mos.cms.futurecdn.net/HYRxmBSGpTx453E7sdq36i-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Int Speed](https://cdn.mos.cms.futurecdn.net/4C4nYPVpnMHcB6NowrwP5i-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Int Speed](https://cdn.mos.cms.futurecdn.net/bbqK6kbEtUG5G8SLggU35i-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Int Speed](https://cdn.mos.cms.futurecdn.net/kv56WzCDnDzZB5iMSyzN4i-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Int Speed](https://cdn.mos.cms.futurecdn.net/mfMsEBJMHJwWCfvML5y74i-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Int Speed](https://cdn.mos.cms.futurecdn.net/byyfAWCYie43ZqJwPqhY3i-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Int Speed](https://cdn.mos.cms.futurecdn.net/2E6VtpxYH8x7PzmYEbrW3i-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Int Speed](https://cdn.mos.cms.futurecdn.net/2sjCzzQY45vSmyN5pYVZzh-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Int Speed](https://cdn.mos.cms.futurecdn.net/s6EWPTwyCBTD8PVscgQLth-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Int Speed](https://cdn.mos.cms.futurecdn.net/dL4dhpo6NicC9iEU9pACnh-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Int Speed](https://cdn.mos.cms.futurecdn.net/Q2jdTfqPNaj6awHshud6eh-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Int Speed](https://cdn.mos.cms.futurecdn.net/7pActa32VdPjdEio5C5G8i-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Int Speed](https://cdn.mos.cms.futurecdn.net/dtUB4iVnAFPbejj78V2WVh-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Int Speed](https://cdn.mos.cms.futurecdn.net/eV66LsffcvVkuvr7vxZB7i-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Int Speed](https://cdn.mos.cms.futurecdn.net/HYRxmBSGpTx453E7sdq36i-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Int Speed](https://cdn.mos.cms.futurecdn.net/4C4nYPVpnMHcB6NowrwP5i-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Int Speed](https://cdn.mos.cms.futurecdn.net/bbqK6kbEtUG5G8SLggU35i-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Int Speed](https://cdn.mos.cms.futurecdn.net/kv56WzCDnDzZB5iMSyzN4i-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Int Speed](https://cdn.mos.cms.futurecdn.net/mfMsEBJMHJwWCfvML5y74i-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Int Speed](https://cdn.mos.cms.futurecdn.net/byyfAWCYie43ZqJwPqhY3i-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Int Speed](https://cdn.mos.cms.futurecdn.net/2E6VtpxYH8x7PzmYEbrW3i-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Int Speed](https://cdn.mos.cms.futurecdn.net/2sjCzzQY45vSmyN5pYVZzh-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Int Speed](https://cdn.mos.cms.futurecdn.net/s6EWPTwyCBTD8PVscgQLth-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Int Speed](https://cdn.mos.cms.futurecdn.net/dL4dhpo6NicC9iEU9pACnh-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F SPEC estimates - Int Speed](https://cdn.mos.cms.futurecdn.net/Q2jdTfqPNaj6awHshud6eh-2439-80.png)

These throughput benchmarks are most representative of how these CPUs will actually be deployed, running multiple copies of applications under high concurrency. However, SPEC CPU also includes its speed suite, which looks at application performance when you can dedicate the whole chip to running just that one application, more along the lines of a client CPU benchmark.

The EPYC 9686F naturally looks better here with its blistering 5 GHz boost clock. In the integer suite, the frequency-optimized chip is 21% ahead of Vera, both in a 2P configuration. The 9996 still holds up, only falling short of the 9686F, despite much more inter-CCD communication.

SPEC shows the various improvements in Zen 6 showing up in a compounding fashion. There’s the new microarchitecture with an optimized vector path, but also more cores per CCD. And also support for higher memory speeds, as well as more memory channels. In isolation, any of these improvements are solid (if rote) for typical gen-on-gen improvements. Add them up in a workload that can take advantage of all of those improvements, however, and Zen 6 is blistering.

### AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks

Two of the biggest performance vectors in the agentic era are memory performance and Python performance, at least at the moment. Agentic frameworks are largely defined by Python between LangGraph and CrewAI, though alternative frameworks written in TypeScript and Rust have started to appear as well. Regardless, Python remains important for agentic CPUs right now.

Similarly, memory bandwidth is important for certain types of agents, particularly those that need to query large databases, regardless of if they’re a traditional relational database written in SQL or a non-relational database.

![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Stream](https://cdn.mos.cms.futurecdn.net/BAZCnVxgLtUVw2btqBjJSB-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Stream](https://cdn.mos.cms.futurecdn.net/kXoSHmnGS9MC6bACmFkzUB-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Stream](https://cdn.mos.cms.futurecdn.net/SsP4SvkLmiPqVUyXStLGYB-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Stream](https://cdn.mos.cms.futurecdn.net/dtaaY23pwC98AdVXZRNVZB-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Stream](https://cdn.mos.cms.futurecdn.net/BAZCnVxgLtUVw2btqBjJSB-2440-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Stream](https://cdn.mos.cms.futurecdn.net/kXoSHmnGS9MC6bACmFkzUB-2440-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Stream](https://cdn.mos.cms.futurecdn.net/SsP4SvkLmiPqVUyXStLGYB-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Stream](https://cdn.mos.cms.futurecdn.net/dtaaY23pwC98AdVXZRNVZB-2440-80.png)

Starting with the industry-standard STREAM benchmark, AMD is ahead of Nvidia’s Vera by between 11% and 19%, depending on the test. However, this was with the OpenMP “true” policy for process binding, which binds processes to the thread they’re placed on to avoid them jumping around and skewing the results. Vera performs well, even with this policy, but its mesh cache and monolithic design allow it to realize big performance gains with the “spread” policy.

This policy also binds processes, but it distributes them across the chip as far away from each other as possible. AMD chips don’t see an improvement with the spread policy, and Intel’s Granite Rapids-AP sees a slight regression. Vera, however, remains on top of the pile, with a clear victory margin with the policy applied.

![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - MBW](https://cdn.mos.cms.futurecdn.net/bBCQua795w4nh5aZgaGBTK-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - MBW](https://cdn.mos.cms.futurecdn.net/zG4zocNuZtUG8VARKc8tVK-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - MBW](https://cdn.mos.cms.futurecdn.net/kVamHMq6GuRG4TWEEgtNaK-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - MBW](https://cdn.mos.cms.futurecdn.net/WvqiwMRNVQgxgi9CZrH6dK-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - MBW](https://cdn.mos.cms.futurecdn.net/xEj5vk88r3yDS83dx27QeK-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - MBW](https://cdn.mos.cms.futurecdn.net/BgWPiiJVnGHdedrX9m2DfK-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - MBW](https://cdn.mos.cms.futurecdn.net/bBCQua795w4nh5aZgaGBTK-2440-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - MBW](https://cdn.mos.cms.futurecdn.net/zG4zocNuZtUG8VARKc8tVK-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - MBW](https://cdn.mos.cms.futurecdn.net/kVamHMq6GuRG4TWEEgtNaK-2440-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - MBW](https://cdn.mos.cms.futurecdn.net/WvqiwMRNVQgxgi9CZrH6dK-2440-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - MBW](https://cdn.mos.cms.futurecdn.net/xEj5vk88r3yDS83dx27QeK-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - MBW](https://cdn.mos.cms.futurecdn.net/BgWPiiJVnGHdedrX9m2DfK-2439-80.png)

In the tried-and-true MBW benchmark, the pair of 9996s claim a small lead over Vera, with a small array size of just 128 MB, but Vera jumps into first place when the array size increases. AMD has certainly tightened up the memory matchup against Vera with 16 channels and support for 12,800 MT/s MRDIMMs, but Vera’s topology and already competitive memory subsystem still wins the day.

The clear differences in memory performance flatten off as we flip to Python, which is a much more hotly-contested area of performance. Starting with a broad overview, we have PyBench. Across the suite, the EPYC 9686F was 32% faster than Vera, while the EPYC 9996 naturally claims a smaller 14% lead with its relatively limited boost clocks. For gen-on-gen comparisons, the EPYC 9996 is an impressive 24% ahead of the EPYC, while the 9686F claims a lead of 35% over the 9755 – though, no small part of that advantage is the 900 MHz higher boost clock that the 9686F has access to.

![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/kTAZQkwDp6ASTE7MiTN4UW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/g26JSSrhbT6w8TePHRHYqV-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/7vn4dJ8Qv6RmTgWtZjGfTW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/BQsHs9LumoKTb7TRiGHSTW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/EHPMMXpAa5VMoSMKGY6WTW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/3hBouAhhYbt3fzkKusZKTW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/cwpdmWm87J56JLYcKpBHTW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/k6uYzv8EJEVNHYtVvLkBTW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/C4CkMdg6PPn9kYDvRcFvSW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/Cq2zKKTQHrpUQtEsBBm7TW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/u44HXi3BQsaBMV6GqXshSW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/cvv6np5B4c8NmQq2n933TW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/mgCXVMZv2njLYY8vdj2qSW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/rQS3EQXEF4joe8cJfDReSW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/qbKKB8btfGx5d3VL4zPYSW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/noawmErnC6uSLxRZ8hKUSW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/s7wsdz3qwLBTyKbcPHRTSW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/5amJmroqESiP7Bp6Sw9SSW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/N7oFs8DMyYfSLoufp4SUSW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/U5cc7rCJG65Y9j9j4as8SW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/xZnLXcki6D6Sciz3xT6hRW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/8AX8rfcuz5tWJ7kmoeB7RW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/wBPFcUqjme8K8NLGnmKDBW-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/RgsZLWpZqCyguyz9s3nL5W-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/4XpojoJrmzhzQwo7NuvdwV-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/vaHuaMwrifDU87JNsRmttV-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/DPmbvaQytv8zVur2hHGcsV-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/kTAZQkwDp6ASTE7MiTN4UW-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/g26JSSrhbT6w8TePHRHYqV-2440-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/7vn4dJ8Qv6RmTgWtZjGfTW-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/BQsHs9LumoKTb7TRiGHSTW-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/EHPMMXpAa5VMoSMKGY6WTW-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/3hBouAhhYbt3fzkKusZKTW-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/cwpdmWm87J56JLYcKpBHTW-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/k6uYzv8EJEVNHYtVvLkBTW-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/C4CkMdg6PPn9kYDvRcFvSW-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/Cq2zKKTQHrpUQtEsBBm7TW-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/u44HXi3BQsaBMV6GqXshSW-2440-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/cvv6np5B4c8NmQq2n933TW-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/mgCXVMZv2njLYY8vdj2qSW-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/rQS3EQXEF4joe8cJfDReSW-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/qbKKB8btfGx5d3VL4zPYSW-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/noawmErnC6uSLxRZ8hKUSW-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/s7wsdz3qwLBTyKbcPHRTSW-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/5amJmroqESiP7Bp6Sw9SSW-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/N7oFs8DMyYfSLoufp4SUSW-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/U5cc7rCJG65Y9j9j4as8SW-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/xZnLXcki6D6Sciz3xT6hRW-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/8AX8rfcuz5tWJ7kmoeB7RW-2440-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/wBPFcUqjme8K8NLGnmKDBW-2440-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/RgsZLWpZqCyguyz9s3nL5W-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/4XpojoJrmzhzQwo7NuvdwV-2440-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/vaHuaMwrifDU87JNsRmttV-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Python and memory benchmarks - Python](https://cdn.mos.cms.futurecdn.net/DPmbvaQytv8zVur2hHGcsV-2440-80.png)

PyPerformance allows us to go more granular into specific Python applications and functions, but a similar pattern appears. The rankings of other CPUs change, but across the vast majority of tests, the EPYC 9686F leads by a clear margin. It makes sense, too, given that Python heavily leans on a single thread at stock.

There are some exceptions, notably the networkx benchmark, where the throughput-optimized 9996 tops the charts, matching Nvidia’s Vera. Despite how impressive Nvidia’s chip is, considering the company’s infancy in data center CPUs and the chip’s tame spec sheet, Venice shows that the CPU game is AMD’s to win (or lose).

### AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks

Breaking out of the agentic bubble, AMD has continually proven itself as the leading force in general-purpose data center applications, and that trend continues with Venice. As with all of the workloads here, they *can* touch on agentic AI depending on what the agent is set up to do; database performance, for example, is important if an agent is often querying a database. However, we’re going to keep our analysis at a high level here, as EPYC CPUs will be deployed for a broad range of workloads, some portion of which won’t come remotely close to agentic AI.

![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Compression](https://cdn.mos.cms.futurecdn.net/udd6Gv9AnhRf9YZ2fYgTPm-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Compression](https://cdn.mos.cms.futurecdn.net/tZfukH7WLWpr3RFi3KZDEm-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Compression](https://cdn.mos.cms.futurecdn.net/3hw39aN7yzmJQfsaYPJePm-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Compression](https://cdn.mos.cms.futurecdn.net/vBeig5rUi99feeSYaGFUPm-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Compression](https://cdn.mos.cms.futurecdn.net/by7UsPUnx6DdbEYenw8SPm-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Compression](https://cdn.mos.cms.futurecdn.net/i2FG6LcYgUGWnGxg7VMVPm-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Compression](https://cdn.mos.cms.futurecdn.net/iCzf7LJFrZK3zgcpqdyDPm-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Compression](https://cdn.mos.cms.futurecdn.net/FDCWkt5cAzJVDSMb4AN7Nm-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Compression](https://cdn.mos.cms.futurecdn.net/qYcnYcwNMveBJiBmiXk6Mm-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Compression](https://cdn.mos.cms.futurecdn.net/kb3TedNEvvLUZFuNGUw6Mm-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Compression](https://cdn.mos.cms.futurecdn.net/udd6Gv9AnhRf9YZ2fYgTPm-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Compression](https://cdn.mos.cms.futurecdn.net/tZfukH7WLWpr3RFi3KZDEm-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Compression](https://cdn.mos.cms.futurecdn.net/3hw39aN7yzmJQfsaYPJePm-2440-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Compression](https://cdn.mos.cms.futurecdn.net/vBeig5rUi99feeSYaGFUPm-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Compression](https://cdn.mos.cms.futurecdn.net/by7UsPUnx6DdbEYenw8SPm-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Compression](https://cdn.mos.cms.futurecdn.net/i2FG6LcYgUGWnGxg7VMVPm-2440-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Compression](https://cdn.mos.cms.futurecdn.net/iCzf7LJFrZK3zgcpqdyDPm-2440-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Compression](https://cdn.mos.cms.futurecdn.net/FDCWkt5cAzJVDSMb4AN7Nm-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Compression](https://cdn.mos.cms.futurecdn.net/qYcnYcwNMveBJiBmiXk6Mm-2440-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Compression](https://cdn.mos.cms.futurecdn.net/kb3TedNEvvLUZFuNGUw6Mm-2440-80.png)

Starting with compression performance, AMD generally sits at the top of the charts for compression and decompression speeds, which is the case here with zstd and 7-Zip. In zstd, Vera claims an early lead at the lowest compression level. However, its poor decompression performance shows up even at level 3, and AMD takes over with a clear victory at the compression level 19, with Vera falling even further behind in decompression performance.

The long mode results are especially interesting. Although the rankings don’t change, Vera’s performance in these sustained compression workloads gets worse, while AMD is able to hang onto much more of its performance. Vera and the EPCY 9686F are within noise of each other in the level 3 compression test, and Vera falls to the bottom of the rankings when looking at decompression.

7-Zip has been, for years now, AMD’s game. The charts really speak for themselves here; we’re dealing in multiplicative factors compared to Vera, not to mention the weak competition from Intel’s Granite Rapids-AP. AMD is always strong in 7-Zip, which is compounding here considering the already high base level of performance we see out of Zen 6 across a wide range of workloads.

![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Rendering](https://cdn.mos.cms.futurecdn.net/MkSUYvfP7oNnZhCUy6KFoB-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Rendering](https://cdn.mos.cms.futurecdn.net/g3C2mVjworHeK3xm6xm7vB-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Rendering](https://cdn.mos.cms.futurecdn.net/dkxJXYwRKh7v8JqhgLySDC-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Rendering](https://cdn.mos.cms.futurecdn.net/qXbwue6SLKWhimPAU39LEC-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Rendering](https://cdn.mos.cms.futurecdn.net/Gpn5mrXEXLNysX2nLGmpEC-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Rendering](https://cdn.mos.cms.futurecdn.net/pgRNGknbCr5dndsVgwGZEC-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Rendering](https://cdn.mos.cms.futurecdn.net/AcLnJt7nzrifwSmxZS9NDC-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Rendering](https://cdn.mos.cms.futurecdn.net/4LjARfUriEUV32KgB2xWEC-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Rendering](https://cdn.mos.cms.futurecdn.net/MkSUYvfP7oNnZhCUy6KFoB-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Rendering](https://cdn.mos.cms.futurecdn.net/g3C2mVjworHeK3xm6xm7vB-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Rendering](https://cdn.mos.cms.futurecdn.net/dkxJXYwRKh7v8JqhgLySDC-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Rendering](https://cdn.mos.cms.futurecdn.net/qXbwue6SLKWhimPAU39LEC-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Rendering](https://cdn.mos.cms.futurecdn.net/Gpn5mrXEXLNysX2nLGmpEC-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Rendering](https://cdn.mos.cms.futurecdn.net/pgRNGknbCr5dndsVgwGZEC-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Rendering](https://cdn.mos.cms.futurecdn.net/AcLnJt7nzrifwSmxZS9NDC-2440-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F compression and rendering benchmarks - Rendering](https://cdn.mos.cms.futurecdn.net/4LjARfUriEUV32KgB2xWEC-2440-80.png)

Onto rendering, Blender shows big gen-on-gen gains for Venice, with the EPYC 9996 offering somewhere between a 30% and 40% improvement over the EPYC 9965 depending on the scene. This is true even in demanding scenes like Barbershop, where render time can be expressed as minutes instead of seconds for many chips. The EPYC 9996 completed the render 35% faster than the EPYC 9965. The EPYC 9686F was able to match the dense EPYC 9965, despite packing half of the cores. Vera isn’t included in our Blender results because a native Arm version isn’t available.

Vera retains a top position in C-Ray, both at 4K and 1080p, though a dual EPYC 9996 configuration is within spitting distance. The script flips in OSPRay, with AMD pulling off clear leads in real-time ambient occlusion, scientific visualization, and path tracing. There are some massive jumps, with the EPYC 9996 nearly tripling the performance of the Xeon 6980P and Vera in the ambient occlusion and scientific visualization tests.

The reworked vector engine in Venice shows up even more clearly in the dim\_512 tests, which further stress both the vector engine and memory bandwidth of the platform.

### AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks

We run three Java suites to measure the ever-important programming language that shows up everywhere from scientific computing to database workloads. Starting on the former end, Java SciMark shows the EPYC 9686F in a clear lead over the competition, with a massive 92% lead over Vera in the composite score. For an apples-to-apples gen-on-gen increase, the EPYC 9996 managed a respectable 24% jump over the EPYC 9965.

![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/u6nTMgWGGfzQRcDzCrNLUS-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/YAR4QdDYvckX7c4QfBUAXR-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/wYy2xVTGcZvW2ckqvSNWTS-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/2tn4JVDfxM37kQX85Z47TS-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/3sWnSugbXKgH64ZYGa64TS-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/DAKh47DoG9CMWaxZmMAxSS-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/S7KpDyhUtTHB6QEPA79nSS-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/xcgZEAH9FdSx75yhxsSaSS-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/yVWWNkNdjSTTHjekiibaSS-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/bbFKZa6W4PjWPH8EBkcWSS-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/2gXeHL5sg62QBBWqo22oSS-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/gvJSRsb3nZceBTcPDYDSSS-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/Vdgpe2QaQxCFqLEon4QQSS-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/6ZrxPZwPw8p6QwtWZqRMSS-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/6bV2YW43wve3GtsbWKHFSS-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/Zq9sw4q5FF9fq66MUPjHSS-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/8JRTNMJdZCkHf8eH8urESS-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/cxAevymm89M96EZY7Pt4SS-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/ZYPjtGu8yLmScJHYr8uQRS-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/CLgaQTaUqrJCP73iLESHRS-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/coxNK7mNaaYDM7tKnBXWQS-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/rnJ8odsLMzW7oQ9PRQXuPS-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/2gmyLCmwuQSEGyHQfkbRvR-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/rquFsfLNPvQD5dBmf2gChR-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/u6nTMgWGGfzQRcDzCrNLUS-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/YAR4QdDYvckX7c4QfBUAXR-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/wYy2xVTGcZvW2ckqvSNWTS-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/2tn4JVDfxM37kQX85Z47TS-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/3sWnSugbXKgH64ZYGa64TS-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/DAKh47DoG9CMWaxZmMAxSS-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/S7KpDyhUtTHB6QEPA79nSS-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/xcgZEAH9FdSx75yhxsSaSS-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/yVWWNkNdjSTTHjekiibaSS-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/bbFKZa6W4PjWPH8EBkcWSS-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/2gXeHL5sg62QBBWqo22oSS-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/gvJSRsb3nZceBTcPDYDSSS-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/Vdgpe2QaQxCFqLEon4QQSS-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/6ZrxPZwPw8p6QwtWZqRMSS-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/6bV2YW43wve3GtsbWKHFSS-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/Zq9sw4q5FF9fq66MUPjHSS-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/8JRTNMJdZCkHf8eH8urESS-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/cxAevymm89M96EZY7Pt4SS-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/ZYPjtGu8yLmScJHYr8uQRS-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/CLgaQTaUqrJCP73iLESHRS-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/coxNK7mNaaYDM7tKnBXWQS-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/rnJ8odsLMzW7oQ9PRQXuPS-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/2gmyLCmwuQSEGyHQfkbRvR-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Java](https://cdn.mos.cms.futurecdn.net/rquFsfLNPvQD5dBmf2gChR-2439-80.png)

Java SciMark provides a nice overview of some critical functions, such as Monte Carlo risk analysis that’s applicable to financial institutions. DaCapo and Renaissance are much wider suites measuring a range of Java-based applications. Many of these tests are highly specific, so the rankings jump around, depending on what the workload stresses. We can see a bit of that with Java SciMark, as well, with Vera claiming the top slot in FFTs. Venice, however, remains ahead.

![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Database](https://cdn.mos.cms.futurecdn.net/MJLgfGwZjSmPyn3ZfUp5Tf-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Database](https://cdn.mos.cms.futurecdn.net/a4tqPBnW9hYu6B4Fgiwkte-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Database](https://cdn.mos.cms.futurecdn.net/yaF86V9UT7Ev2tUY4J8xSf-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Database](https://cdn.mos.cms.futurecdn.net/QTu55AhVhnzq2LZdnnDYSf-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Database](https://cdn.mos.cms.futurecdn.net/cpZmTZfBK3LLjoZSmEuqRf-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Database](https://cdn.mos.cms.futurecdn.net/a2uTiPvVyEM6qcbe77r8Rf-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Database](https://cdn.mos.cms.futurecdn.net/VvXc4JmXsa58EziENAf2Rf-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Database](https://cdn.mos.cms.futurecdn.net/BeoEDdrp3WBrmpBVGmFR8f-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Database](https://cdn.mos.cms.futurecdn.net/MJLgfGwZjSmPyn3ZfUp5Tf-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Database](https://cdn.mos.cms.futurecdn.net/a4tqPBnW9hYu6B4Fgiwkte-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Database](https://cdn.mos.cms.futurecdn.net/yaF86V9UT7Ev2tUY4J8xSf-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Database](https://cdn.mos.cms.futurecdn.net/QTu55AhVhnzq2LZdnnDYSf-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Database](https://cdn.mos.cms.futurecdn.net/cpZmTZfBK3LLjoZSmEuqRf-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Database](https://cdn.mos.cms.futurecdn.net/a2uTiPvVyEM6qcbe77r8Rf-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Database](https://cdn.mos.cms.futurecdn.net/VvXc4JmXsa58EziENAf2Rf-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F Java and database benchmarks - Database](https://cdn.mos.cms.futurecdn.net/BeoEDdrp3WBrmpBVGmFR8f-2439-80.png)

In large column-based database workloads like Clickhouse, Venice also looks impressive, though not from the jump. Vera maintains its performance from a cold cache, while none of the x86 competition reach steady performance until the cache is warm. The reason should be obvious given Vera’s topology and its distributed mesh, which allows it to jump straight to its peak performance, even when the cache is cold.

Once it’s warm, the 9686F jumps into the lead. There’s a regression in performance going from the 9965 to the 9996, which makes sense for Clickhouse, as larger core counts can create issues in cache coherency.

To look at NoSQL performance, we have simdjson, which leverages SIMD instructions for JSON parsing, as the name implies. Once again, the vector engine in Venice shines, regardless of the workload you look at.

### AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F HPC and compilation benchmarks

![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F HPC and compilation benchmarks - Compilation](https://cdn.mos.cms.futurecdn.net/oAcpGDZNCrTpfozfQjvjH4-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F HPC and compilation benchmarks - Compilation](https://cdn.mos.cms.futurecdn.net/pKiyEwACJffVagDNzqpDQ4-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F HPC and compilation benchmarks - Compilation](https://cdn.mos.cms.futurecdn.net/KgmfdKXpAnydduToRUCEQ4-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F HPC and compilation benchmarks - Compilation](https://cdn.mos.cms.futurecdn.net/aFeR5RpjTTgScnA8a5ekS4-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F HPC and compilation benchmarks - Compilation](https://cdn.mos.cms.futurecdn.net/FvcDTQoERx7EzchEzAnrS4-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F HPC and compilation benchmarks - Compilation](https://cdn.mos.cms.futurecdn.net/oAcpGDZNCrTpfozfQjvjH4-2440-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F HPC and compilation benchmarks - Compilation](https://cdn.mos.cms.futurecdn.net/pKiyEwACJffVagDNzqpDQ4-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F HPC and compilation benchmarks - Compilation](https://cdn.mos.cms.futurecdn.net/KgmfdKXpAnydduToRUCEQ4-2440-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F HPC and compilation benchmarks - Compilation](https://cdn.mos.cms.futurecdn.net/aFeR5RpjTTgScnA8a5ekS4-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F HPC and compilation benchmarks - Compilation](https://cdn.mos.cms.futurecdn.net/FvcDTQoERx7EzchEzAnrS4-2440-80.png)

Vera showed strong compilation performance against AMD’s Turin chips, but Team Red leapfrogs that performance with Venice. Starting with LLVM, the frequency-optimized 9686F earns a top slot with makefiles, while the EPYC 9996 tops with Ninja. The drop is around 19% gen-on-gen, aligning with the performance we’ve seen with other workloads.

In PHP, where Vera is more competitive, the EPYC 9686F squeezes out the most marginal of victories, but perhaps most telling is the 9996, which is in the upper tier of chips, despite how dense it is. Building applications, the Godot game engine and ImageMagick once again show both Venice chips on the top of the stack, outclassing the performance of Vera, which previously held a top slot in ImageMagick, and only fell slightly behind the 9755 in Godot.

![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F HPC and compilation benchmarks - HPC](https://cdn.mos.cms.futurecdn.net/Wiix9DfPnHj98pLNaYaYGF-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F HPC and compilation benchmarks - HPC](https://cdn.mos.cms.futurecdn.net/kEkE9diY9LxvtRrnHyNp4F-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F HPC and compilation benchmarks - HPC](https://cdn.mos.cms.futurecdn.net/ibscQUUYvanDkRRhXq6UFF-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F HPC and compilation benchmarks - HPC](https://cdn.mos.cms.futurecdn.net/Tu27Sf3aeCGaXNyK4kgTFF-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F HPC and compilation benchmarks - HPC](https://cdn.mos.cms.futurecdn.net/74C7k5yTa6Yo9tLPPUskEF-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F HPC and compilation benchmarks - HPC](https://cdn.mos.cms.futurecdn.net/su4gYZG89DfERVQUJrSr8F-1200-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F HPC and compilation benchmarks - HPC](https://cdn.mos.cms.futurecdn.net/Wiix9DfPnHj98pLNaYaYGF-2440-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F HPC and compilation benchmarks - HPC](https://cdn.mos.cms.futurecdn.net/kEkE9diY9LxvtRrnHyNp4F-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F HPC and compilation benchmarks - HPC](https://cdn.mos.cms.futurecdn.net/ibscQUUYvanDkRRhXq6UFF-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F HPC and compilation benchmarks - HPC](https://cdn.mos.cms.futurecdn.net/Tu27Sf3aeCGaXNyK4kgTFF-2440-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F HPC and compilation benchmarks - HPC](https://cdn.mos.cms.futurecdn.net/74C7k5yTa6Yo9tLPPUskEF-2439-80.png)
![AMD Zen 6 EPYC ‘Venice’ 9996 and 9686F HPC and compilation benchmarks - HPC](https://cdn.mos.cms.futurecdn.net/su4gYZG89DfERVQUJrSr8F-2439-80.png)

The 9686F shows large performance jumps in HPC workloads, which AMD says is the target of these lower-core, frequency-optimized SKUs. In CloverLeaf, the EPYC 9686F is more than twice as fast as Vera, and it’s nearly twice as fast with FFTE. In Octave, Vera retains its top position, but both Venice chips are only slightly behind.

Although not traditional HPC, the heavily threaded number crunching behind the scenes in the Stockfish chess engine allows the 1,024 threads in a 2P EPYC 9996 server to outclass the 9965 by nearly 50%. Primesieve shows similarly large leaps, with the EPYC 9996 calculating some 37 billion prime numbers in less than half a second.

### More to come

## More to come

AMD already had a strong position in the newly reinvigorated CPU market with Turin. The unique topology and strong focus of Vera has allowed Nvidia to make inroads in certain workloads, but even looking at two SKUs from AMD’s broad Venice lineup, it’s clear that AMD is able to push performance much higher across the board. In some cases, that’s by orders of magnitude gen-on-gen.

There isn’t one area of Zen 6, or the SoCs available with Venice broadly, that totally accounts for the performance increase. It’s small advantages throughout the design, pushing an already strong vector engine further, vastly increasing CCD density, and giving memory bandwidth a boon between support for 12,800 MT/s MRDIMMs and 16-channel memory courtesy of the dual IODs.

But the story AMD has been trying to tell, and the one that’s difficult to ignore in the current market of a one-size-fits-all approach we’ve seen from Nvidia and Arm, is that Venice is available in a broad range of different configurations. We tested two chips on SP7, but the enterprise-focused SP8 socket is arriving within the next few months. And next year, AMD is pushing out Venice-X with 3D V-Cache for HPC workloads, as well as Verano, which looks like AMD’s take on Vera with its field-replaceable SOCAMM2 LPDDR5X memory.

Even without those chips, the two SP7 chips we tested already give AMD a leading position among current data center CPUs. Intel’s Diamond Rapids could change that story come next year, but the EPYC 9686F provides top-tier performance with HPC and AI host node performance, while the EPYC 9996 provides unmatched throughput.

**MORE: Best CPUsMORE: CPU Benchmark HierarchyMORE: AMD vs. Intel**

![Jake Roach](https://cdn.mos.cms.futurecdn.net/h6PRM8bTimCTnNfoAYfjAi-140-80.jpg)

Jake Roach is the Senior CPU Analyst at Tom’s Hardware, writing reviews, news, and features about the latest consumer and workstation processors.

* Have i missed what the RAM was used? Were the tests done with 2x bandwidth RAM ( 12800 MRDIMMs vs previous 6400 RDRAM ) when many benchmarks are essentially memory bandwidth bound ( one of the key "secrets" why GPUs are fast) ? If yes then even mosquito will kill a horse if wolf will help.Reply
* > The headline for Zen 6 is a 27% average IPC uplift over Zen 5 in enterprise, cloud, and AI workloads. The debut of this new microarchitecture is focused on the data center, so you shouldn’t take that 27% IPC improvement as broadly applicable to all workloads.

  From the image above this, "Enterprise and cloud server" workloads is only 20%, "AI workloads" is 31%.  
    
  It might end up being considered less than 20% for typical consumer workloads and gaming, but it sounds good so far. Reply
