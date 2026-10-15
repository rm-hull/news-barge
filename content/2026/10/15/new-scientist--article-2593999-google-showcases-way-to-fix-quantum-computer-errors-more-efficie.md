---
title: Google showcases way to fix quantum computer errors more efficiently
source_url: https://www.newscientist.com/article/2593999-google-showcases-way-to-fix-quantum-computer-errors-more-efficiently/?utm_campaign=RSS|NSNS&utm_content=home&utm_medium=RSS&utm_source=NSNS
source_site: New Scientist
source_slug: new-scientist
scraped_at: '2026-10-15T21:21:10Z'
published: '2026-10-15T00:00:00Z'
description: Error-proofing the most important operations performed on a quantum computer
  has so far required lots of resources, but a new experiment shows a more efficient
  way to make the devices reliable
image: https://www.newscientist.com/wp-content/uploads/2026/10/SEI_316716668.jpg
categories:
- Science
- Technology & Software
people:
- Dominik Hangleiter
- Emma Rosenfeld
- Isaac Kim
- Willow
- Zhenyu Cai
locations:
- Davis
- Switzerland
organisations:
- ETH Zurich
- Google Quantum AI
- Imperial College London
- University of California
- Willow
---

![Google Quantum AI - Willow quantum computer](https://www.newscientist.com/wp-content/uploads/2026/10/SEI_316716668.jpg?w=840)

Making quantum computers error-proof is one of the biggest challenges currently facing the technology. Researchers at Google Quantum AI have now demonstrated one way to do so more efficiently. Their work suggests the smaller quantum computers that will be available in the next few years could be more impactful than expected.

Quantum computers can run mathematical operations, analogous to addition or multiplication, that conventional computers cannot. This makes them suitable for solving some problems that had previously been considered unsolvable, such as those that underpin cryptography.

Most important among the quantum operations the computers run are “non-Clifford gates”, which are the key ingredients for algorithms that transcend conventional computation.

Advertisement

But there is a problem. Quantum computers are very error-prone, and their building blocks, called qubits, must be encoded into special groups, or “logical qubits”, before they can execute operations reliably. Executing non-Clifford gates in an error-corrected way requires large numbers of qubits, which means having to build very large quantum computers – a formidable engineering challenge.

Now, Emma Rosenfeld at Google Quantum AI and her colleagues have used the firm’s Willow quantum computer to show that the error-correction process can be made more efficient. Their new technique ultimately reduced Willow’s errors 40 times.

At the centre of their advance is the idea of a “magic state”, which is a special quantum state that qubits must assume before the quantum computer can run error-corrected non-Clifford operations. Creating these states had, so far, been a real bottleneck for quantum computing, says Rosenfeld. “It eats up a lot of qubits and a lot of time,” she says.

In 2024, her colleagues at Google Quantum AI proposed a more efficient method for creating magic states called “magic state cultivation”. Here, instead of many imperfect qubits being repeatedly combined and manipulated into a magic state that is then put towards running an error-corrected operation, the magic state is “grown” within a smaller patch of qubits.

The Google researchers showed that magic state cultivation could, in theory, enable quantum computers to run consequential programs with just one-tenth the number of qubits we had expected they would need. The new experiment by Rosenfeld and her colleagues proves that magic state cultivation works in practice.

This is not the first time that new methods for making magic states have lowered a quantum computer’s error rates. Advances in creating magic states and error-correcting non-Clifford gates have also been achieved in experiments with quantum computers that have qubits based on ions. Willow’s qubits, which are based on tiny superconducting circuits, achieved error rates similar to those past experiments, but Rosenfeld says that they work more quickly, potentially reducing the quantum computer’s overall runtime.

![](https://www.newscientist.com/wp-content/uploads/2026/06/03104937/SEI_299914822.jpg)

A quantum computer made from extremely cold atoms can correct its own errors during long computations, an important prerequisite for becoming truly useful

“This is an impressive demonstration of a promising recent idea pioneered by Google,” says Isaac Kim at the University of California, Davis. “It’s an approach that can make fault-tolerant quantum computing substantially cheaper.” The new work demonstrates one of the building blocks necessary for universal quantum computing and could be a “gamechanger” in terms of building intermediately sized quantum computers with hundreds of logical qubits, says Dominik Hangleiter at ETH Zurich in Switzerland.

Zhenyu Cai at Imperial College London says that while this experiment is a significant step forward, Willow’s errors will need to be reduced further before it can tackle truly useful problems. Additionally, Kim says that in the experiment, Willow generated good magic states only for a fraction of its computational runs: only 8 per cent of Willow’s computations produced high-quality magic states that could then be put into further use.

Rosenfeld says that this percentage ought to increase as she and her colleagues refine the technique and improve Willow’s hardware. It is, in this case, also affected by a very careful benchmarking technique that the team used, which may not be used in future applications, she says. “This is the first demonstration that the concepts work. We’re not done.”
