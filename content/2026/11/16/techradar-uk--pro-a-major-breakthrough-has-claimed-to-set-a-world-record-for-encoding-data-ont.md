---
title: A new quantum technique tackles one of computing’s biggest obstacles
source_url: https://www.techradar.com/pro/a-major-breakthrough-has-claimed-to-set-a-world-record-for-encoding-data-onto-a-quantum-computer-and-crucially-reading-it-back-again
source_site: TechRadar UK
source_slug: techradar-uk
description: A quantum computing breakthrough stores thousands of data points, but
  its reconstructed images still contain noticeable errors
image: https://cdn.mos.cms.futurecdn.net/d4oN2QTeNf8QYJDmjZnAKE-1920-80.jpg
published: '2026-11-16T00:00:00Z'
scraped_at: '2026-11-16T06:17:10Z'
categories:
- Technology & Software
- Science
people:
- Daniel Bultrini
- Harry Kumar
- Tessa
locations:
- Phoenix
organisations:
- AI
- CCO
- IBM
- IBM’s Fez
- IBM’s Phoenix
- Moth Quantum
- Moth’s Founder
- SUR1
- TechRadar Pro
---

![Quantum computing](https://cdn.mos.cms.futurecdn.net/d4oN2QTeNf8QYJDmjZnAKE-1920-80.jpg)

* **Moth Quantum retrieves thousands of stored values from IBM quantum hardware**
* **IBM’s Phoenix processor successfully retrieves information distributed across all 120 qubits**
* **Quantum hardware struggles to reproduce complex images with sufficient accuracy**

Moth Quantum says its Tessa technique has achieved a new quantum computing record by storing information on a processor and successfully retrieving it.

The method placed 1,568 numerical values across IBM’s 120-qubit Phoenix processor, then used the recovered information to recreate an image.

This addresses a major challenge in quantum computing: getting ordinary information into quantum machines and retrieving it without significant loss of accuracy.

## A new record with important accuracy limits

Previous research of this kind recovered 128 numerical values using 12 trapped-ion qubits, making the latest result substantially larger by the study’s definition.

Tessa uses neighboring qubits to control where information is stored, allowing the processor’s existing connections to handle the operation without moving information between distant qubits.

The arrangement avoids extra qubit-moving operations and additional helper qubits, while the tested circuits reached a depth of 19 two-qubit operations.

“Every quantum computer has to get data in before it can do anything useful with it, and that step has been a bottleneck for fields like quantum machine learning,” said Daniel Bultrini, the Moth researcher who developed Tessa.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

“Tessa makes the most of the chip’s capabilities, so the whole processor can be put to work at once.”

Image tests stored 784 and 441 values, requiring 728 and 428 controlled operations, respectively; each used 8,192 measurement attempts.

However, information recovery was imperfect: the largest color image achieved a correlation of 0.69 with its source, compared with 0.95–0.96 for simpler images.

The average numerical error was 0.130 on Phoenix and 0.131 on IBM’s Fez processor, falling to 0.075 and 0.078 after adjustment.

That adjustment used two statistics taken from the original image, meaning the improved reconstruction relied partly on information already known.

For a separate test combining image brightness and color, Phoenix recorded errors of 0.152 and 0.092, while Fez recorded 0.144 and 0.084.

The Phoenix brightness error was 2.6 times higher than the company’s noise model predicted, indicating that real hardware introduced additional inaccuracies.

## Audio and biological tests

Moth Quantum also tried audio, musical notes, DNA, and protein sequences, using different ways to represent information inside the processor.

A music test containing 347 flute notes recovered 18.7% of pitches correctly before adjustment, improving to 49.3% afterward on the Fez processor.

Biological tests required 32,768 measurement attempts, compared with 8,192 for image experiments, yet accuracy varied substantially between sequences for every measurement basis.

The p53 protein sequence achieved 71.5% correct recovery, while Sonic hedgehog reached 76.2% and mitochondrial protein MT-CO3 recorded 92.3% on IBM’s Phoenix hardware.

Results were weaker for other samples: SUR1 reached 22.6%, while pikachurin achieved 25.8%, showing that longer or more complex sequences remained difficult.

The tests also included a mitochondrial DNA sequence containing 784 building blocks and a POLG2 messenger RNA sequence with 1,582.

The study warns that one incorrect DNA or protein unit can matter biologically, so these recovery percentages do not establish dependable medical applications.

The simulations here do not include all interference between neighboring processor groups, and the hardware experiments used no error-correction techniques.

Tessa also depends on a particular pattern of connections between qubits, while measurement demands rise sharply as those connections become more numerous.

Moth Quantum did not use error mitigation, which the study says could reduce reconstruction errors significantly in future hardware tests.

“The quantum applications that will have the greatest impact, including those that work closely with AI, will depend on breakthroughs such as Tessa in order to meet the expectations that have been set,” said Harry Kumar, Moth’s Founder and CCO.
