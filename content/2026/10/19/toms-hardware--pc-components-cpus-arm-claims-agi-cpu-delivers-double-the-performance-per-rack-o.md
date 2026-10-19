---
title: Arm says its AGI CPU delivers nearly 2X the performance per rack of AMD EPYC
  9755 in new agentic AI CPU tests
source_url: https://www.tomshardware.com/pc-components/cpus/arm-claims-agi-cpu-delivers-double-the-performance-per-rack-of-amd-epyc-9755-in-independent-analysis-new-cpu-evaluation-methodology-developed-by-arm-evaluates-agentic-ai-performance-across-seven-workloads
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-19T13:03:54Z'
published: '2026-10-19T00:00:00Z'
description: Arm claims its AGI CPU delivers a 20% average per-chip performance lead
  and nearly 2X the modeled rack performance of AMD’s EPYC 9755 across seven agentic
  AI workloads, using a new evaluation methodology developed with Fujitsu, Meta, and
  OpenAI
image: https://cdn.mos.cms.futurecdn.net/WZWmFdfwr99E5o9CwZc6nM-1920-80.jpg
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
people:
- Etiido Uko
locations:
- Turin
- Venice
organisations:
- AGI CPU
- AI
- AMD
- Etiido Uko
- Fujitsu
- Intel
- Meta
- Nvidia While Arm
- OpenAI
- PC
- SMT
- Signal65
- Tom's Hardware
---

![Arm](https://cdn.mos.cms.futurecdn.net/WZWmFdfwr99E5o9CwZc6nM-1920-80.jpg)

Arm announced last week that its AGI CPU, the company's data center CPU for agentic AI workloads, delivers twice the performance per rack as AMD EPYC 9755, calculated from chip performance and server-power assumptions measured across seven workloads. The claim stems from modeled rack results from tests aligned with Arm’s new CPU evaluation methodology, developed with support from Fujitsu, Meta, and OpenAI.

The results — verified in an Arm-commissioned independent analysis by *Signal65* — do not establish the AGI CPU as the overall leader for agentic AI, as they apply to the selected processors, workloads, and configuration. They also use the specific Arm-developed evaluation methodology that Arm says should be the new standard for assessing performance. However, other chipmakers like AMD and Intel make performance claims based on different benchmarks. So, how is Agentic AI evolving CPU performance benchmarks, what does Arm propose to measure, and how do the different approaches compare?

## Arm’s new CPU evaluation methodology

Agentic AI is changing the role of CPUs in modern AI data centers, requiring them to handle complex, multi-step workflows. Beyond inference, which the accelerator handles, AI agents execute tools, retrieve data, and maintain state within isolated environments, acting like virtual users. The CPU handles these critical surrounding workloads, from running those tools and serving database or API requests to preparing data and coordinating work for accelerators.

As these workloads scale rapidly with agentic capabilities, it becomes increasingly important to gauge CPU performance not just by how many agents can run concurrently, but also by how much useful work gets done. Arm argues that CPU performance is increasingly defined by how much useful work a system can sustain while staying responsive. Supporting more agents simultaneously offers limited benefit if their executions throttle or accelerators have to sit idle waiting for the CPU. Power, cooling, and physical space also limit how much hardware operators can deploy, extending the performance question to the rack.

Arm’s proposed methodology for evaluating CPU performance, developed with support from Fujitsu, Meta, and OpenAI, centers on representative agent workloads, repeatable CPU measurements, and validation against end-to-end task outcomes. In practical terms, the methodology identifies the tools and services an agent uses, measures their CPU performance under controlled conditions, and checks whether improvements help the agent complete its task. For example, a database test can establish how quickly a system handles transactions. An end-to-end evaluation would then examine whether faster database access actually improves the workflow that depends on it.

Executing the second aspect of the methodology, making these comparisons repeatable, presents another challenge, as an agent might choose different commands or take a different route through a task each time it runs. Model inference and remote services also introduce delays. Arm proposes replaying recorded agent actions to separate CPU performance from this variability, allowing different systems to execute a consistent sequence of work. Its whitepaper sets out a framework for selecting and interpreting these measurements, leaving the industry to develop an agreed benchmark suite and scoring approach.

To evaluate the CPU work described in its framework, Arm ran seven workloads — spanning tooling, agentic workflows, and reasoning/planning, plus Sandbench, which measures sandbox-creation overhead for agent execution — on its AGI CPU and AMD’s EPYC 9755. The tests combine established server applications with benchmarks focused on agent workflows.

|  |  |  |
| --- | --- | --- |
| Workloads and breakdowns |  |  |
| **Workload**|** What it represents**|** Metric** |
| MySQL | Transactional database behind agent tools | Transactions per second |
| NGINX | Web and API request handling | Requests per second |
| Milvus | Vector search for retrieval | Queries per second |
| Terminal-Bench 2 | 72 agent task types in sandboxed containers, 128 copies at once | Task completion time |
| SWE-bench replay | Software-engineering agent workflow, 259 tasks | Tasks per minute |
| fastText | CPU word-representation training | Words per second |
| vLLM CPU overhead | CPU serving overhead with model compute bypassed | Requests per second |

The vLLM result measures the CPU work around model execution, not GPU inference throughput. Similarly, the report’s “reasoning/planning” category groups supporting CPU workloads and does not assess how intelligently a model reasons.

## ARM AGI CPU vs AMD EPYC 9755

For the tests, Arm used two AGI CPU configurations because of hardware availability: a 128-core chip at 2.8 GHz with DDR5-7200 for Terminal-Bench 2 and SWE-bench replay, and a 136-core chip at 3.2 GHz with DDR5-8000 for the other five workloads. The AMD comparison used one socket of the 128-core EPYC 9755 with DDR5-6400. Both platforms ran the same benchmark scripts but used different software environments. Arm used custom Linux 7.1.3 builds, with Ubuntu 24.04 for most tests and Ubuntu 26.04 for SWE-bench, while AMD’s main recorded configuration used Ubuntu 24.04 and Linux 6.8, with settings varying by test.

At the chip level, Arm’s AGI CPU won the majority of comparisons when compared to its AMD counterpart in five of the seven tests. With the EPYC 9755 as the baseline, Arm led by 9% on Terminal-Bench, 13% on SWE-bench, and 97% on fastText, but lagged by 12% and 5% in MySQL and Milvus throughput, respectively. On average, the AGI CPU led by 20% (1.20x) per-chip advantage, calculated across the seven normalized performance ratios.

|  |  |  |
| --- | --- | --- |
| Results |  |  |
| **Workload**|** Measured per-chip performance vs EPYC 9755**|** Modeled per-rack performance vs EPYC 9755** |
| MySQL | 0.88x | 1.43x |
| NGINX | 1.20x | 1.95x |
| Terminal-Bench 2 | 1.09x | 1.93x |
| SWE-bench replay | 1.13x | 2.00x |
| Milvus | 0.95x | 1.54x |
| vLLM CPU overhead | 1.16x | 1.88x |
| fastText | 1.97x | 3.19x |
| **Arithmetic average** | 1.20x | 1.99x |

At the rack level, Arm’s modeled performance averages 1.99x AMD’s, with a lead in all seven workloads. The model uses rated server-power estimates of 950 W for the 128-core Arm configuration, 1,050 W for the 136-core version, and 1,700 W for AMD, including memory and other system components. After reserving about 8% of a 24 kW rack budget for networking and power distribution, this leaves room for 23 or 21 Arm servers versus 13 AMD servers.

For SWE-bench, the 2.00x per rack result was obtained by multiplying the roughly 1.13x chip result by 23/13. The larger gain comes from fitting more servers into the same power budget. Furthermore, these projections use modeled whole-server power, not throughput measurements from two fully populated racks.

Arm’s model also gives the AMD servers about twice as much RAM: roughly 2 TB against 1 TB for Arm. It allocates 4 GB per hardware thread, with each AMD core supporting two threads while each Arm core supports one. This puts the memory-power allowance at 336 W for AMD and 192 W for Arm. Signal65 also calculated what happens when memory is allocated per physical core. In this setup, AMD’s memory and power allowance falls, and Arm’s average modeled rack advantage drops from 1.99x to approximately 1.81x. The usefulness of the 2 TB AMD configuration depends on how much memory the workloads actually need, as SMT does not inherently require twice the memory.

To verify the findings, *Signal65* remotely observed Arm’s test runs and examined the original logs, result files, scripts, and configuration records. A separate review team rebuilt the calculations with its own code and reproduced all seven results within 0.5%. However,*Signal65* did not run a separate hardware rerun in its own lab. In addition,*Signal65* could independently confirm BIOS and memory settings for only the EPYC 9965 system. These settings were unavailable for independent verification on the Arm and EPYC 9755 systems. Along with the software differences, these gaps slightly affect the certainty with which the results can be attributed to the processors themselves.

## Arm’s approach vs AMD and Nvidia

While Arm believes its methodology should be the standard, it does not hold a monopoly on how the industry evaluates agentic CPU performance. For example, AMD promotes agents per watt, dollar, and rack. Footnotes on its EPYC 9006 page identify available CPU threads as a proxy for agent capacity, with actual throughput depending on the workload and system. Its separate workload analysis models a 100 kW rack and claims 2.37× performance for EPYC 9965 over Nvidia's Vera, using a geometric mean across six infrastructure workloads.

Nvidia, on the other hand, emphasizes Vera’s single-thread performance and memory bandwidth, and says a 256-CPU rack supports more than 22,500 concurrent CPU environments. These numbers describe different things and do not directly imply any specific advantage. Methodologies vary across manufacturers by workload, power assumptions, and aggregation methods, making direct CPU comparisons complex. The current comparison is against AMD's fifth-generation “Turin” processor with 128 cores. The company launched its latest sixth-generation EPYC 9006 “Venice” family this year, dedicated to agentic AI.

![Etiido Uko](https://cdn.mos.cms.futurecdn.net/BBrMt7jWtSo2Dc3iKoroyD-140-80.jpg)

Etiido Uko is a news contributor for Tom's Hardware covering the latest updates in big tech and the PC industry. He is a mechanical engineer and senior technical writer with over nine years of experience in documentation and reporting. He is deeply passionate about all things engineering and technology, and is an expert in gadgets, manufacturing, robotics, automotive, and aerospace.
