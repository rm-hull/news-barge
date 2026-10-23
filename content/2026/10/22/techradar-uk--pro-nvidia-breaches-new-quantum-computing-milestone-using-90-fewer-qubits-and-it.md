---
title: Nvidia's latest quantum simulation could help develop better drugs and more
source_url: https://www.techradar.com/pro/nvidia-breaches-new-quantum-computing-milestone-using-90-fewer-qubits-and-it-could-now-improve-drug-discovery-financial-modeling-and-more
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-23T04:44:56Z'
published: '2026-10-22T00:00:00Z'
description: Nvidia takes quantum computing to Europe's biggest supercomputer, simulating
  104 qubits under realistic conditions for the first time
image: https://cdn.mos.cms.futurecdn.net/uyNmZxDkKhiLjM7ieeaSKC-1600-80.jpg
categories:
- Technology & Software
- Science
people:
- Jensen Huang
locations:
- Europe
- Germany
- Jülich Supercomputing Centre
- North Rhine-Westphalia
organisations:
- Accelerated Quantum Research Center
- GPU
- JUPITER
- Jülich
- Nvidia GH200
- TechRadar Pro
---

![Using 8,192 GPUs, Nvidia researchers simulated fault tolerant quantum operations, reportedly reducing physical qubit requirements by 90% under realistic noise.](https://cdn.mos.cms.futurecdn.net/uyNmZxDkKhiLjM7ieeaSKC-1600-80.jpg)

* **Nvidia simulates 104 qubits using JUPITER, Europe's first exascale supercomputer**
* **The technique reportedly reduces physical qubit requirements by 90%**
* **Magic state cultivation could reduce hardware demands for fault-tolerant quantum computing**

Nvidia researchers have simulated a 104-qubit quantum computing system on JUPITER, Europe's first exascale supercomputer, validating a technique that requires 90% fewer physical qubits.

The experiment took place at Germany's Jülich Supercomputing Centre, where researchers examined how quantum computing systems could operate reliably.

The team investigated magic state cultivation, an approach to fault-tolerant quantum computing that could reduce the physical resources required for complex calculations.

## New technique reduces quantum computing hardware requirements

Quantum processors are vulnerable to environmental interference, which introduces errors and makes accurate calculations increasingly difficult as systems grow larger.

Researchers are developing fault tolerance methods to address these problems, enabling quantum computers to maintain computational accuracy despite errors affecting individual physical components.

One approach involves producing specially prepared quantum resources called magic states, which are consumed during operations required for fault-tolerant quantum calculations.

Producing these resources requires substantial computing capacity, making improvements in their preparation important for reducing the hardware demands of useful quantum systems.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Nvidia's simulation examined magic state cultivation, incorporating realistic hardware noise, which allowed researchers to investigate errors that earlier simulations conducted under ideal conditions could not adequately represent.

"Useful quantum computing will require fantastically complex, fault-tolerant systems—and understanding how they behave at scale is essential to building them," said Jensen Huang, Nvidia's CEO and founder.

"Our results from Jülich show how quantum processors and GPU supercomputers can work together to tackle research that would otherwise be out of reach—accelerating the discovery of transformative quantum applications."

Earlier research at Jülich simulated 50 qubits under ideal conditions, while the latest experiment incorporated realistic hardware noise.

The experiment nevertheless used classical computing infrastructure to simulate quantum operations rather than testing the technique on a functioning quantum processor.

## JUPITER enables large-scale quantum simulations

Located in North Rhine-Westphalia, Germany, JUPITER provided the computing capacity needed to model complex quantum operations that conventional systems struggle to simulate.

The supercomputer used Nvidia GH200 processors for the experiment, with researchers scaling their methods to 8,192 GPUs.

Before moving to JUPITER, the team developed and tested its simulation methods using Nvidia's GB200 NVL72 system at the company's Accelerated Quantum Research Center.

Researchers expanded their initial tests from four graphics processors to hundreds, evaluating performance and accuracy before deploying the methods on the larger machine.

These preparations reduced simulations that previously required several weeks to just days, helping researchers use JUPITER's computing resources more efficiently.

The team also used Nvidia's cuQuantum software and CUDA Q platform to simulate quantum circuits and represent the operations involved in magic state cultivation.

The results could help researchers assess quantum processor designs before constructing hardware, potentially reducing the need for costly physical experiments during development.

However, Nvidia's result remains a simulation, and further experimental work must establish whether the technique delivers comparable benefits on actual quantum hardware.
