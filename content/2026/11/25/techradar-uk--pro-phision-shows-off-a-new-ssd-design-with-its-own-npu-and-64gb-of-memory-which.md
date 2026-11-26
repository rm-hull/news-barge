---
title: Phision shows off a new SSD design with its own NPU and 64GB of memory — which
  it says can cut data transfers by 10 to 100 times
source_url: https://www.techradar.com/pro/phision-shows-off-a-new-ssd-design-with-its-own-npu-and-64gb-of-memory-which-it-says-can-cut-data-transfers-by-10-to-100-times
source_site: TechRadar UK
source_slug: techradar-uk
description: Phison's new SSD design packs an NPU and 64GB memory
image: https://cdn.mos.cms.futurecdn.net/uvUx7cKcA7cZivjNrQo6ZK-1920-80.png
published: '2026-11-25T00:00:00Z'
scraped_at: '2026-11-26T03:31:39Z'
categories:
- Technology & Software
people:
- Michael Wu
- Phison
- Sebastien Jean
- Tom
locations:
- Phison
organisations:
- AI
- AMD Xilinx
- Computex
- Dhrystone MIPS
- GM
- GPU
- LLM
- NAND
- NVM Express
- Phison US
- Phison's
- SC26
- SSD
- Samsung
- ScaleFlux
- SmartSSD
- TechRadar Pro
- TechSpot
- Tom's Hardware
- Topaz NPU
---

![Graphic of a circuit board](https://cdn.mos.cms.futurecdn.net/uvUx7cKcA7cZivjNrQo6ZK-1920-80.png)

* **Phison detailed an unnamed SSD architecture at SC26 with an integrated NPU rated at 36,800 DMIPS and 64GB of memory at 130GB/s**
* **It claims on-drive filtering could cut data transfers by 10 to 100 times for suitable workloads while also taking load off CPUs**
* **There is no product name, controller, power figure, price, or date yet; Phison says the design is still in development**

Phison wants enterprise SSDs to stop acting purely as warehouses and start doing some of the sorting themselves.

At the recent Supercomputing 2026 (SC26) event, the company detailed a computational storage architecture that places an integrated NPU and 64GB of memory with 130GB/s of bandwidth inside the drive.

This marks a break from the usual modus operandi: Rather than shipping entire datasets across PCIe to a host CPU or GPU, the drive is meant to scan and process data in parallel where it already sits, then send back only the relevant results, an approach that Phison says could potentially reduce data transfers by 10 to 100 times while freeing up host CPU resources.

## A large claim, with a large caveat?

Phison says the design supports PyTorch, vLLM, OpenVINO, and llama.cpp, and that developers can build for it without specialized programming tools. As TechSpot put it, the idea is for some of the processing to happen before the data ever leaves the drive.

The idea is novel but comes with an interesting caveat: Phison says the reduction applies only to workloads where the approach fits, and the company has published no methodology, test dataset, or benchmark to back it up.

That caveat matters more than it might seem, because a data reduction ratio is mostly a property of the workload rather than the hardware. Sending ten times less data means the drive returns a tenth of what it scanned; a hundred times less means it returns one percent.

A selective filter run over log files or a database table can hit those ratios on any architecture that pushes the filter down to storage, while a job that needs most of the dataset will not come close. That reading of the arithmetic is mine rather than Phison's, but it explains why the claimed range spans a full order of magnitude.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The metric being measured is also somewhat interesting, to say the least: The only compute figure Phison has offered is 36,800 DMIPS. Dhrystone MIPS is an integer CPU benchmark dating back to the 1980s, not the TOPS rating normally quoted for neural processors.

Tom's Hardware argues the figure most likely describes the general-purpose cores sitting beside the accelerator, probably Arm-based, which would be adequate for running the drive but reveals nothing about AI throughput. The same report notes that Phison's Topaz NPU card at Computex carried eight NPUs rated at up to 40 TOPS each, which makes the absence of a comparable figure here all the more conspicuous. For the record, Phison has not said whether the drive's NPU is related to Topaz.

The memory figure is more revealing. Phison has not disclosed the memory type, but 130GB/s is consistent with a 128-bit LPDDR5X interface: at 8,000 MT/s that works out to 128GB/s, and at 8,533 MT/s to roughly 136GB/s. Phison's Topaz NPU supports LPDDR5/5X at up to 8,533 MT/s, so the numbers line up, but I have not received any official confirmation.

Support for llama.cpp will tempt some to picture an SSD that serves large language models, but the bandwidth points elsewhere: Token generation is usually memory-bound, since each new token requires a pass over the model's weights, so bandwidth divided by model size gives a rough ceiling.

An 8-billion-parameter model quantized to 4 bits, at roughly 4.5 to 5GB, would top out around 25 to 30 tokens per second. A 70-billion-parameter model at the same precision would fit in 64GB but peak at about three tokens per second. This means that while the SSD could host an LLM, anything but the most basic ones will struggle to deliver adequate performance.

This fits Hardware Busters' reading that the design is about data reduction close to the NAND rather than running large models, and that it should not be treated as a GPU replacement. Small models that classify, tag, or embed data before it leaves the drive look like the most plausible approach here.

It is also worth separating the 130GB/s figure from how quickly the drive can read its own flash. Memory bandwidth is not NAND bandwidth, and Phison has not disclosed the controller, channel count, host interface, or capacity for this design. Nor has it said whether the drive uses the PCIe 6.0 X3 controller it promoted at the same show.

## A promising idea that has been explored before

The most striking context here comes from Phison itself. In a 2021 interview with TechRadar Pro, Sebastien Jean, then Phison's senior director of systems architecture and now CTO of Phison US, said computational storage "appears to be an easy sell, but it hasn't turned out that way." He argued that an SSD already devotes its full resources and power budget to its primary job.

He sharpened that position in a 2025 essay on Phison's blog, writing that when engineers discuss computational storage, "too often it's a pie-in-the-sky approach," and singling out the idea of running Linux on a drive with bigger processors. His alternative was targeted accelerators applying fixed operations to ranges of logical block addresses, such as filtering, checksum verification, and erasure coding.

Computational storage itself, however, has a patchy record. Samsung first floated its SmartSSD in 2018 and followed up with an AMD Xilinx-powered second generation in 2022, when it declared that "the computational storage market has great potential." As TechRadar Pro has previously reported, the drive then faded from Samsung's lineup, with remaining units sold under the AMD Xilinx brand, and even ScaleFlux, one of the category's loudest champions, dropped the term from its company description.

ScaleFlux has done better by keeping the compute out of sight. Its CSD 5320 compresses data in hardware on the fly, and Tom's Hardware notes that drives present themselves to the host as ordinary NVMe SSDs, so applications need no changes.

Standards have moved on, too. NVM Express released Computational Programs and Subsystem Local Memory command sets in January 2024, giving hosts a standard way to load and run programs on a drive. Phison has not said whether its design uses them, or how a host would submit work to the NPU. Framework support is not the same thing as existing code running unchanged.

The design slots neatly into Phison's wider AI messaging. Michael Wu, GM and president of Phison US, said in the announcement that "the next era of computing won't be defined by processing power alone."

However, until Phison publishes a TOPS figure, a power envelope, a host programming model, and a benchmark showing where the 10- to 100-times reduction comes from, this is best read as a statement of direction rather than a tangible product for the AI masses.
