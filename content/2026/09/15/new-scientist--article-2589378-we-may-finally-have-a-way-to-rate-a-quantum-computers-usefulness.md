---
title: We may finally have a way to rate a quantum computer’s usefulness
source_url: https://www.newscientist.com/article/2589378-we-may-finally-have-a-way-to-rate-a-quantum-computers-usefulness/?utm_campaign=RSS|NSNS&utm_content=home&utm_medium=RSS&utm_source=NSNS
source_site: New Scientist
source_slug: new-scientist
scraped_at: '2026-09-15T19:40:52Z'
published: '2026-09-15T00:00:00Z'
description: Determining how useful different quantum computers are has been a long
  running challenge – now researchers appear to have the answer
image: https://www.newscientist.com/wp-content/uploads/2026/09/SEI_312576967.jpg
categories:
- Science
- Technology & Software
locations:
- California
- Germany
people:
- Maurer
- Sam Stanwyck
- Timothy Proctor
- Wolfgang Mauerer
organisations:
- Google
- IBM
- Nvidia
- QUOPS
- Quantinuum
- Sandia National Laboratories
- Technical University of Applied Sciences Regensburg
---

![](https://www.newscientist.com/wp-content/uploads/2026/09/SEI_312576967.jpg?w=840)

How useful is a particular quantum computer? We may finally be able to answer this question.

Quantum computers have made significant strides in recent years, becoming both more reliable and powerful. Yet, when it comes to computations that could have a large impact on the world, such as understanding the FeMoco molecule, which plays a key role in nitrogen fixing, or breaking today’s most prevalent cryptography methods, quantum computers still underperform.

But assessing how far they are from being sufficiently capable has always been tricky. Now, Timothy Proctor at Sandia National Laboratories in California and his colleagues say their QUOPS score is the missing piece of the puzzle.

Advertisement

The idea is relatively simple. First, a quantum computer runs a special set of programs, or quantum circuits, which allow researchers to calculate its QUOPS score. QUOPS stands for quantum universal operation performance system, and reflects how many physical building blocks, or qubits, the quantum computer has and how many computational operations it can execute. This number can then be compared with the QUOPS score for an algorithm that researchers may wish to run on this quantum computer.

If the algorithm’s score is larger than the computer’s, the computation won’t work. But if the quantum computer’s score is comparable or larger, then the machine ought to be useful for solving the problem that the algorithm was designed for. Another number, the QUOPS rate, captures how long that computation would take.

The team calculated QUOPS scores for some of today’s best quantum computers built by Google, IBM and Quantinuum. None of their QUOPS scores surpassed 2000 – both FeMoco and cryptography computations would require scores well over 100,000 times larger.

Additionally, the team tested Quantinuum’s Helios-1 quantum computer when it was configured to run as a fault-tolerant machine – a quantum computer that catches and corrects its own errors. It earned a QUOPS score of about 40.

To become more computationally powerful, quantum computers must include more and more qubits, but that makes them increasingly error-prone. Consequently, researchers think that fault-tolerant approaches are the only viable future for quantum computers, so understanding them better is crucial.

Proctor says that the inflection point for quantum computing will come when logical qubits, which are used for fault-tolerant quantum computing, reach higher QUOPS scores than ordinary qubits. After that, the goal will be to match their scores to useful algorithms.

This new work is a reality check, says Sam Stanwyck at Nvidia, which collaborated on the project. Stanwyck says that using this software could help researchers see how QUOPS scores change with small tweaks to their quantum computer designs, accelerating the path to higher scores and more utility.

“These kinds of benchmarks are very useful at the moment,” says Wolfgang Mauerer at the Technical University of Applied Sciences Regensburg in Germany. He says that quantum computers with very different qubits than those tested in the new work could also be evaluated based on QUOPS scores to give a better view of the overall state of the quantum computing industry.

But the QUOPS score and rate are unlikely to be the last word on what makes a quantum computer truly powerful, he says. As the technology continues advancing, new aspects of the machines may emerge as crucial. “What quantum compute power really is, that is not yet fully understood, and that cannot be captured in the benchmark,” says Maurer.
