---
title: How we test enterprise SSDs — our new test suite pushes enterprise and data
  center SSDs to their limits
source_url: https://www.tomshardware.com/uk/pc-components/ssds/how-we-test-enterprise-ssds-our-new-test-suite-pushes-enterprise-and-data-center-ssds-to-their-limits
source_site: Tom's Hardware
source_slug: toms-hardware
description: Our enterprise and data center SSD reviews show how a drive performs
  in real-world service, not just on its best day.
image: https://cdn.mos.cms.futurecdn.net/ayhToiaEbT3hRiAqSjdrzg-2560-80.jpg
published: '2026-11-17T00:00:00Z'
scraped_at: '2026-11-17T15:58:30Z'
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
people:
- Shane Downing
- Tom
locations:
- Granite Rapids
organisations:
- 4K QD1
- AI
- AppArmor
- Asus
- CPU
- Corsair
- Debian
- ExpressSlot Elite MB221E5P-B
- G.Skill
- Get Tom's Hardware
- IOMMU
- Icy Dock
- Intel E610
- JEDEC
- Kioxia
- MB303E5P-B
- Noctua
- QD256
- SNIA
- SSD
- SanDisk
- Shane Downing
- Storage Networking Industry Association
- Tom’s Hardware
- Ubuntu
- Vdbench
- Xeon 658X
---

![Tom&#039;s Hardware Enterprise SSD Testbed](https://cdn.mos.cms.futurecdn.net/ayhToiaEbT3hRiAqSjdrzg-1920-80.jpg)

After a hiatus of several years, *Tom's Hardware* is expanding its in-depth testing and analysis to enterprise and data center SSDs. Consumer SSDs and conventional hard drives lack the performance and endurance for extensive AI workloads. This has increased demand for enterprise SSDs. Form factors like U.2, U.3, E3.S, and E1.S, once rare, are now common in high-end workstations and home labs. These enterprise storage solutions provide higher capacities, better performance, and greater reliability than consumer drives.

Comprehensive reviews of enterprise and data center SSDs are therefore more important than ever. Buying a drive of this caliber is a major decision and a significant investment for organizations of all sizes. With this latest venture, *Tom's Hardware* will continue to help buyers make informed decisions with comprehensive reviews and performance analyses.

### Inside The Tom's Hardware Enterprise SSD Test System

Reviewing enterprise and data center SSDs required us to build a workstation that could truly challenge these drives. This project would not have been possible without the support of several component makers, including Asus, Corsair, G.Skill, Icy Dock, and Noctua, who made the workstation a reality, a challenging prospect in the current market.

The Xeon 658X, a 24-core, 48-thread chip from the Granite Rapids family with a 4.9 GHz boost clock speed, powers the testing workstation. Single-core performance and total core count matter just as much when reviewing storage. Clock speed determines how many IOPS one core can push and how fast it answers a single request, while 24 cores let us spread a drive's load across eight fio jobs and later test several drives at once. The Xeon 658X ticks all those boxes.

We've entrusted the Xeon 658X's cooling to Noctua's NH-U14S DX-4677 air cooler, which supports both LGA4677 and LGA4710 sockets. The single-tower CPU air cooler delivers high-performance cooling at very low noise levels thanks to its dual NF-A15 140mm cooling fans.

![Intel Xeon 658X](https://cdn.mos.cms.futurecdn.net/tDtGxLPBVvoHdsbvgbBx-1200-80.jpg)
![Asus Pro WS W890E-Sage SE](https://cdn.mos.cms.futurecdn.net/wSGekhYCXUBxXxmAzMSFxk-1200-80.jpg)
![Noctua NH-U14S DX-4677](https://cdn.mos.cms.futurecdn.net/Lj3Ti6Awa5kaLyHCMCBken-1200-80.jpg)
![Gigabyte GT 1030 Silent Low Profile 2G](https://cdn.mos.cms.futurecdn.net/YoG5cRAbLmss7WsrFPyeAC-1200-80.jpg)
![Intel Xeon 658X](https://cdn.mos.cms.futurecdn.net/tDtGxLPBVvoHdsbvgbBx-2560-80.jpg)
![Asus Pro WS W890E-Sage SE](https://cdn.mos.cms.futurecdn.net/wSGekhYCXUBxXxmAzMSFxk-2560-80.jpg)
![Noctua NH-U14S DX-4677](https://cdn.mos.cms.futurecdn.net/Lj3Ti6Awa5kaLyHCMCBken-2560-80.jpg)
![Gigabyte GT 1030 Silent Low Profile 2G](https://cdn.mos.cms.futurecdn.net/YoG5cRAbLmss7WsrFPyeAC-2560-80.jpg)

With its server-grade components and robust enterprise features, the Asus Pro WS W890E-Sage SE is the ideal motherboard to pair with the Xeon 658X. Its extensive feature set includes an onboard MCIO x8 connection, split into x4/x4, that allows for evaluating two U.2 or U.3 drives. The board also provides seven PCIe 5.0 expansion slots (six at x16 and one at x8) to fully leverage the Xeon 658X’s 128 PCIe 5.0 lanes, so the SSDs and graphics cards never hit bandwidth limits.

We're still in need of support for an RTX Pro graphics card, which would be an invaluable asset for enterprise SSD reviews for real-world AI workloads, but our current test platform allows us to test the most important aspects of performance.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![G.Skill G5 DDR5-6400 C32 64GB (4x16GB)](https://cdn.mos.cms.futurecdn.net/H2veScwEcXNMNsEa4PFTrb-1200-80.jpg)
![Corsair MP700 Pro XT 2TB](https://cdn.mos.cms.futurecdn.net/KKjA4UrsK6EqKRfvuqWxvK-1200-80.jpg)
![Corsair HX1500i](https://cdn.mos.cms.futurecdn.net/fQg3NjNPAtDHb9ESPF7g8m-1200-80.jpg)
![G.Skill G5 DDR5-6400 C32 64GB (4x16GB)](https://cdn.mos.cms.futurecdn.net/H2veScwEcXNMNsEa4PFTrb-2560-80.jpg)
![Corsair MP700 Pro XT 2TB](https://cdn.mos.cms.futurecdn.net/KKjA4UrsK6EqKRfvuqWxvK-2560-80.jpg)
![Corsair HX1500i](https://cdn.mos.cms.futurecdn.net/fQg3NjNPAtDHb9ESPF7g8m-2560-80.jpg)

Despite the memory and storage shortage, G.Skill and Corsair have stepped up to provide crucial components for our enterprise SSD test bench. G.Skill sent a G5 DDR5-6400 C32 64GB (4x16GB) R-DIMM memory kit, which runs at the stock DDR5-5600 speed. The decision to keep it at the JEDEC baseline has nothing to do with the memory kit: Memory frequency does not affect performance in enterprise SSD tests.

Meanwhile, Corsair provided the speedy MP700 Pro XT 2TB, one of the best SSDs, as the test bench's primary storage. The PCIe 5.0 drive delivers sequential read and write speeds up to 14,900 MB/s and 14,500 MB/s, respectively, and keeps the workstation snappy, especially when it hammers enterprise drives all day long.

No power supply is better suited to the job than the Corsair HX1500i. It offers a massive 1,500W capacity with plenty of headroom for future upgrades, and it runs quietly and stably, two qualities that matter when you keep the test system running for countless hours. It is an 80 Plus Platinum power supply with at least 89% efficiency at full load.

![ExpressSlot Elite MB221E5P-B](https://cdn.mos.cms.futurecdn.net/YqDskPLQjtnwer9vNpaya6-1200-80.jpg)
![ExpressSlot Elite MB303E5P-B](https://cdn.mos.cms.futurecdn.net/pbky3v3W8r2579MAiBkohB-1200-80.jpg)
![ToughArmor MB218E5P-B](https://cdn.mos.cms.futurecdn.net/9nKL4irckVsnQSit2qTAUj-1200-80.jpg)
![JMT ADT-R27C](https://cdn.mos.cms.futurecdn.net/26wnp57dfxv2dQ5fV72CM4-1200-80.jpg)
![ExpressSlot Elite MB221E5P-B](https://cdn.mos.cms.futurecdn.net/YqDskPLQjtnwer9vNpaya6-2560-80.jpg)
![ExpressSlot Elite MB303E5P-B](https://cdn.mos.cms.futurecdn.net/pbky3v3W8r2579MAiBkohB-2560-80.jpg)
![ToughArmor MB218E5P-B](https://cdn.mos.cms.futurecdn.net/9nKL4irckVsnQSit2qTAUj-2560-80.jpg)
![JMT ADT-R27C](https://cdn.mos.cms.futurecdn.net/26wnp57dfxv2dQ5fV72CM4-2560-80.jpg)

Testing enterprise drives in a standard PCIe expansion slot is more convenient. For that purpose, Icy Dock has provided us with the ExpressSlot Elite MB221E5P-B and MB303E5P-B to accept one and two E1.S SSDs. Unlike other generic designs on the market, these adapters feature tool-less installation mechanisms that don't require removing them from the PCIe expansion slot, and they include 50mm fans for active cooling.

The list also included the ToughArmor MB218E5P-B, a 5.25-inch drive bay that supports up to eight E1.S SSDs for future projects exploring RAID arrays. To test E3.S drives, *we* use a JMT ADT-R27C adapter strapped to a Noctua NF-F12 industrialPPC-24V-3000 IP67 PWM cooling fan, which can run at 12V and still provide substantial airflow to actively cool the SSDs under evaluation.

![Tom&#039;s Hardware Enterprise SSD Testbed](https://cdn.mos.cms.futurecdn.net/RkDvQnH2dtjJYLUvHtzEEA-1200-80.jpg)

A TGDGamer E-ATX test bench houses the hardware for the enterprise SSD system. It may not look flashy, but it does the job, and that is what matters. As an open-air test bench, it is easy to install and remove hardware, and it eliminates variables when it comes to heat generation and buildup. The test bench also supports motherboard form factors up to SSI-EEB, so the Asus Pro WS W890E-Sage SE feels right at home.

### Inside the Torture Chamber: Assembling an Enterprise-Grade Benchmark Suite

A spec sheet only tells you what a drive can do on its best day. The real world is not as pretty. The drive is mostly full, garbage collection is constantly at work, and multiple workloads are hitting it simultaneously. Our enterprise benchmark suite is built to measure the drive in service: at steady state, under load, through write bursts, and with other jobs running. Every drive gets the same automated run on the same test bench. Every result is stored with the exact parameters that produced it, so we can trace how we got there.

This can take some time. A full run takes most of a day on a 7.68TB PCIe 5.0 drive, and it writes the drive end-to-end many times over. To make life a bit easier on us, the benchmark can be run unattended, and it’s crash-resumable from the last stage. A shorter express mode handles bench checks and quick triage. When a result looks odd, express runs and variant runs, which repeat just the tests in question or change one setting, help us find the cause before we take it to the vendor.

### One OS, One Engine

## One OS, One Engine

We run the bench on a custom Debian 13 image that we build and maintain ourselves, with the suite copied in at build time. This image gets installed on the bench’s OS drive, and the kernel is pinned so every drive has the same software stack. Right now that’s Linux 7.2.6 from Debian backports, because Debian 13’s stock 6.12 kernel predates support for the Asus Pro WS W890E-Sage SE’s Intel E610 10GbE controller. The suite is also designed to be run remotely if needed, but we need a tester at the bench to switch the drives, of course.

Debian is our pick over Ubuntu for a few reasons: it has fewer background services, no Snap, and no unattended upgrades by default. We hold the kernel so nothing changes between runs. We remove AppArmor and turn off scheduled jobs that could fire mid-run, like the weekly TRIM timer and the drive-health service that polls every drive, and the suite records any that are still running. The suite also turns off NVMe autonomous power-state transitions (APST) at the start of every run and checks that the drive reports it off, so no drive drops into a low-power state during an idle gap and adds wake-up latency to the next I/O.

Every test runs in fio 3.42, using io\_uring and direct I/O against the raw block device. This means no filesystem and no page cache sitting between fio and the drive; the bench’s 64GB of RAM never caches a byte of test data. We compile fio from source because Debian’s packaged version lacks SPRandom, which we’ll get to in short order.

Some enterprise storage reviews run application profiles in Oracle’s Vdbench, but we decided to go full fio. This makes for a more consistent suite with one set of latency accounting across every chart. And fio is open source and actively maintained, while Vdbench hasn’t had a new release since 2018. Vdbench profiles are built from the same parts fio uses, such as read/write ratio, block-size mix, and random or sequential access, and our mixed-workload sweeps cover the common read/write ratios at 4K and 8K, though not mixed-block-size profiles. Running Vdbench ourselves wouldn’t make our results comparable to other outlets’ anyway, since they use different hardware, preconditioning, and profile definitions.

### Steady State or Nothing

## Steady State or Nothing

A key element of benchmarking SSDs is making sure the test drive is at steady state, with the performance it can sustain rather than the peak you can see after a fresh erase. Our first stage is a secure erase using nvme format. If a drive refuses, the suite falls back to a plain format, then a full-drive discard, and records which one it used.

Next comes preconditioning. SPRandom, SanDisk’s open-source contribution to fio, is a faster alternative to filling the drive over and over for hours. It takes user capacity and over-provisioning (OP) as inputs, which SanDisk says lets it reach a steady-state layout in just one pass. Overprovisioning (OP) is inferred from the capacity point or given by the tester. NVMe drives don’t report their raw flash, so a 7.68TB drive like our first one, assumed to sit on 8TiB of actual NAND, works out to having about 14.5% OP.

We don’t take SPRandom’s result on faith. A steady-state gate follows, running 4K random writes at queue depth 256 (QD256) until the drive’s write speed stops moving. It uses the two tests from the Storage Networking Industry Association’s (SNIA) steady-state rule, with limits ten times tighter, applied to the last 30 minutes: split into five six-minute rounds, the round averages must sit within 2% of one another, and the trend line across the window can’t move more than 1%.

That takes a while, but that’s the point: an earlier, looser version of the gate passed our first drive while its write speed was still climbing. The whole settling curve is saved with every run, and a drive that doesn’t settle within three hours is marked as not reaching steady state, though the run continues. As a backstop, the suite repeats the four-corner 4K write after the random sweep, hours later, and flags the run if the two results differ by more than 3%.

The suite also checks its own results as it goes. If a test’s slowest moment falls below 70% of its average, that test is run again on the spot. If a point in the random sweep lands more than 10% off the curve set by its neighbors, it’s measured again before the drive is erased for the sequential tests. Both results are kept, and any re-test is noted in the review.

Following the random tests, the tool erases the drive again and writes it end to end once, with 128K sequential writes at QD64. We run it before the sequential and AI tests, so the drive is conditioned with the kind of I/O we’re about to measure. It matters because sequential writes can swing wildly on a randomly written drive: on our first test drive, the fastest result was more than three times the slowest. After a sequential fill, they held flat from QD2 through QD1024, at both 128K and 1MB.

Drives are formatted to 512-byte logical blocks when they support it, so our block size sweep can go down to 512-byte transfers, which a 4K-native namespace can’t issue. SNIA’s enterprise IOPS test uses 512-byte transfers too, and Kioxia pitches 512-byte access for its GP Series, which is aimed at GPU-initiated storage. Drives without a 512-byte format are tested as shipped, and their sub-4K results are marked unsupported. The switch happens in the same format command as the secure erase, so it adds no time.

### Measuring The Drive, Not The Bench

## Measuring The Drive, Not The Bench

A fast enough SSD will happily benchmark your host, or your tools, instead, and our early runs turned up three ways that could happen. The first is CPU idle states, or C-states: waking our Xeon 658X cores from their deepest idle state can take up to 170 microseconds, and at QD1 that directly impacts the results. Holding the cores awake for the whole run cut the first drive’s average 4K QD1 read latency by about a sixth.

The second is the CPU itself: a single fio job can saturate its core well short of what a PCIe 5.0 drive can manage. Split across eight jobs, the same test runs several times faster, so random tests now spread their queue depth across up to eight fio jobs. That’s also why fast cores, and enough of them, matter for this test bench.

The third is fio itself. By default, fio seeds its random generator the same way every run, so it replays the same sequence of random offsets, and each random write test rewrites the previous test’s blocks in the same order. On our first drive, that was the main reason 4K random writes came in at more than twice the sustained figure. Every random test now runs with a fresh random seed.

What we don’t change matters, too. Completions arrive by interrupt rather than polling, and the IOMMU stays in its default mode, because that’s how most applications use a drive. On our first drive, polling and IOMMU passthrough would each have shaved some latency off 4K QD1 writes.

Interrupts also set a ceiling at the other end of the scale: this bench tops out near 2.8 million 4K random read IOPS, and adding fio jobs doesn’t lift it, though polling does. So on the fastest drives, our 4K random read result can sit below the spec sheet’s, and that’s our bench’s limit, not the drive’s. Our low queue depth latencies, writes especially, run higher than a tuned host would show, but they’re closer to what you’d actually see. To show the drive’s limit at both ends, the suite repeats three tests with polled I/O at the end of the random stage: the 4K random read peak, plus 4K random reads and writes at QD1. Those results get their own charts and never mix into the main ones.

### What We Test, How, and Why

## What We Test, How, and Why

| Test | What it runs | Why it’s there |
| --- | --- | --- |
| Four corners | 4K random read and write at QD256; 128K and 1MB sequential read and write at QD64 | The headline numbers, measured on a preconditioned drive instead of fresh out of the box |
| Random and mixed sweeps | 4K and 8K, QD1 to QD4096, eight read/write mixes from 100% read to 100% write | Servers rarely run flat out; QD1 is what latency-bound software feels, and 8K is a common database page size |
| Drive limit (polled) | 4K random read at QD1024 across eight jobs, plus 4K random read and write at QD1, all with polled I/O | What the drive can do with the host’s interrupt overhead out of the way; the results to set against a spec sheet |
| Sequential sweep | 128K and 1MB sequential reads and writes, QD1 to QD1024 | How much parallelism a drive needs to reach full speed; low queue depths are what a single restore or scan gets |
| Block size sweep | Random reads and writes from 512 bytes to 1MB at QD32 | Writes smaller than a drive’s mapping unit can pay a read-modify-write penalty; large blocks show its bandwidth cap |
| Tail latency | 4K and 8K reads and writes at QD1, QD4, and QD16, from the median (P50) to the 99.999th percentile (P99.999) | Averages hide the stalls applications notice; at a million IOPS, the slowest 0.001% is still ten requests a second |
| Saturation curve | 4K 70/30 at 13 queue depths from QD1 to QD4096, plotted as a share of the drive’s own peak | Finds the load where latency starts to climb |
| Sustained write | One hour of 4K random writes at QD256 | Whether sustained writes hold a flat line or sawtooth as garbage collection struggles |
| Write-to-read recovery | 4K QD1 reads for four minutes right after a heavy write burst | How far reads drop after heavy writes, and how fast they recover |
| Idle recovery | Write bursts after idle gaps of 0 to 300 seconds | How much write speed a quiet spell buys back |
| Database I/O patterns (simulated) | 4K QD1 log writes with a sync after each, a random 8K 70/30 mix at QD16, and a 256K sequential read scan | Log-write latency, page I/O, and analytics scans, without benchmarking a database’s RAM cache |
| AI checkpoints | Checkpoint-sized saves and restores modeled on 8B- and 70B-class models (105GiB over eight writers, 912GiB over 64) | Time until the slowest writer finishes, which is when a real checkpoint would be done |
| Checkpoint interference | A fixed 4K read load, alone and during a checkpoint save | What a checkpoint does to serving traffic on the same drive |
| Thermals | Drive temperature through the hour-long sustained write test | Measured against the drive’s own warning and critical thresholds |

Some things are out of scope by design. We review drives; we don’t certify them. That rules out dual-port failover, power-loss validation, and single-root I/O virtualization (SR-IOV), which belong in a qualification lab. We’ll add tests when they prove themselves on the bench. Many of the tests in the table are old standbys and still earn their place. Others are newer and require further explanation.

For one, we chart latency against load: the 70/30 4K mix from the random sweep, at 13 queue depths from QD1 to QD4096, with throughput shown as a share of the drive’s own peak. Tail latency climbs as the load grows, and the point where it turns sharply upward (on our first drive, that was write latency) represents the practical operating ceiling, or the load you can plan a server around without giving up low latency.

We also test write-to-read recovery, which measures how a drive’s reads hold up after a heavy write burst. A few minutes of 4K random writes at QD256 leave the drive with cleanup to do, and QD1 reads are then timed over the next four minutes. If a drive is still busy collecting garbage, it will read slower before climbing back; the extent and duration of the drop are the result.

Idle recovery measures what downtime buys back. After a minute of sustained writes, the drive sits idle for anywhere from zero to five minutes, then a 10-second write burst, logged second by second, shows whether background cleanup freed enough blocks to run faster.

Checkpoint interference shows what an AI checkpoint does to anything else sharing the drive. A light 4K read load, which stands in for inference or database queries, runs alone, and then again during a checkpoint save. Each read is timed from when it was due, not when it was sent, so reads stuck waiting behind a stalled one count too.

Lastly, we test thermals. Drive temperature is tracked through the hour-long sustained write test and charted against the drive's own warning and critical thresholds.

The full process means every drive is treated the same and compared fairly, with a method built to give the same results run after run. This allows us to provide a level playing field built on accurate and repeatable performance characterization.

![Shane Downing](https://cdn.mos.cms.futurecdn.net/Zosi9VrDytS9FkgJiHvc69-140-80.png)

Shane Downing is a Contributing Writer for Tom’s Hardware, covering consumer storage, PC hardware, and AI.

* The article said:After a hiatus of several years, Tom's Hardware is expanding its in-depth testing and analysis to enterprise and data center SSDs.Nice! Some of these are going to be good finds, on the used market. If the SSD market crashes like it did in 2023, even prices on new ones could be quite affordable. That's when I got a new 4TB Intel D7-P5520 for < $300 from an authorized seller (i.e. with full 5-year warranty). Reply
