---
title: Hardware researcher spins up 'CPU deoptimization' project to find the slowest
  single x86 instruction, creates hall of shame — worst offender takes 198 billion
  cycles spanning 62 seconds to execute
source_url: https://www.tomshardware.com/pc-components/cpus/hardware-researcher-spins-up-cpu-deoptimization-project-to-find-the-slowest-machine-code-worst-offender-takes-198-billion-cycles-to-execute
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-08T13:09:11Z'
published: '2026-08-08T00:00:00Z'
description: Ironically, new advanced instruction sets could make for even slower
  commands.
image: https://cdn.mos.cms.futurecdn.net/DFYP2Cmq3awUVLaoNhZg2S-2560-80.jpg
---

![Code on screen.](https://cdn.mos.cms.futurecdn.net/DFYP2Cmq3awUVLaoNhZg2S.jpg) 

To optimize how software runs on hardware, instruction latency analysis looks at the time it takes for low-level instructions to execute on a processor, either to optimize the architecture or to optimize applications to run on a particular architecture. One hardware researcher, Christopher Domas (@xoreaxeaxeax on GitHub), is taking a different approach with the CPU Deoptimization leaderboard, which looks not to make Assembly instructions run as fast as possible, but as slow as possible to measure the single instruction with the highest latency.

 ![A hand holding the Ryzen 7 9850X3D.](https://cdn.mos.cms.futurecdn.net/Xh2MupWrRjJPiLLuopmKRB.jpg) 


The winner here is fxrstor64, which took 62 seconds, or over 198 billion cycles, to complete. This instruction restores the state of registers used for SIMD calculations to a 512-byte memory location. To achieve the highest (slowest) score, Domas first used their __own mmiotic tool__ to find a high-latency area in the internal PCIe fabric, then forced the CPU to load a 512-byte state from MMIO (Memory-Mapped I/O), essentially processing all of those 512 bytes as slow as possible. That took 74 billion cycles or just over 23 seconds to complete.

Then, they went further "by starving the fabric while the load is in flight." They did so by using a series of 4-byte reads from another high-latency MMIO register, overwhelming the CPU's PCIe root complex and forcing the state restore to queue behind frivolous read ops. The next step is to use the AMX instructions available in Intel's Sapphire Rapids for xrstore64. The state area is increased from 512 bytes to 8KB, which could cause the instruction to hang for more than 1 trillion cycles.

Everyone's trying to make CPUs faster.I’m trying to make them worse.New project: CPU deoptimization.Searching for the slowest possible machine instructionsx86 single instruction record:198,002,498,236 cycles, 62 secondsThe assembly hall of shame: [https://t.co/G4QnFQjsZx](https://t.co/G4QnFQjsZx) pic.twitter.com/WNaRPf2kRCAugust 7, 2026


The x86 leaderboard is live on GitHub now, and it looks like Domas has ARM and RISC-V leaderboards planned, as well. There are a few rules for the runs. Domas says any setup is fine, so long as only the execution of a single instruction is scored. Interruptible instructions aren't allowed, nor is scoring emulated instructions run on the handler. All times are normalized based on the CPU's base clock, and the platforms were all run without hardware modifications.

We're dealing with assembly code here, so the ranking is less about the specific instruction and more about what you're doing with that instruction.

Domas primarily used two CPUs for testing: the Intel Core i7-8559U and AMD Ryzen 7 5800H (inside the Trigkey S5). For the rdmsr instruction, however, they used a VIA Eden chip, which was a series of embedded processors from the early 2000s. The rdmsr command is used to read a model-specific register, or MSR. According to Domas, VIA "uses an undocumented register at 0x133 that gives wildly high response time." That command took 202 microseconds or 161,602 cycles to execute.

This is not the developer's first foray into wild experimentation with low-level instructions. An earlier project, called __movfuscator__, is a C compiler that solely uses the mov (move) command.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Jake Roach](https://cdn.mos.cms.futurecdn.net/h6PRM8bTimCTnNfoAYfjAi.jpg)

Jake Roach is the Senior CPU Analyst at Tom’s Hardware, writing reviews, news, and features about the latest consumer and workstation processors.

- 
This is actually pretty awesome. Finding the Achilles heel of CPU instructions is a pretty good way to ultimately make them better going forward. It's also an example of thinking outside the box. It's also some fun canon fodder for CPU wars so people can poke holes in the competition.Reply
 
 Who knows if this line of thinking is part of AI LLM's yet or if it's any good at this strategy? If not some of the next models will be because everything that hits the Internet is sucked up by AI for future use. Humans still have intuition, imagination, and creativity that AI is unlikely to master for a very long time if ever.
