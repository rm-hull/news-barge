---
title: Quantum computing may be facing a replication crisis | New Scientist
source_url: https://www.newscientist.com/article/2584476-quantum-computing-may-be-facing-a-replication-crisis/?utm_campaign=RSS|NSNS&utm_content=home&utm_medium=RSS&utm_source=NSNS
source_site: New Scientist
source_slug: new-scientist
scraped_at: '2026-08-17T13:02:01Z'
published: '2026-08-17T00:00:00Z'
description: A review of thousands of scientific papers about quantum computers finds
  that most don’t provide code that can be tested on independent devices or that the
  code doesn’t work
image: https://www.newscientist.com/wp-content/uploads/2026/08/SEI_308174944.jpg
---

![](https://www.newscientist.com/wp-content/uploads/2026/08/SEI_308174944.jpg?w=840)

The results of most scientific papers reporting on advances in quantum computers can’t be replicated, according to a new analysis. This may undermine the credibility of some of the achievements that the quantum computing industry has reported in recent years, kicking off a replication crisis in the fast-growing field.

There are a few problems that researchers are certain only a quantum computer could solve, but what these machines could be useful for beyond those select few cases is an open question. With quantum computing hardware improving rapidly in recent years, researchers across the globe are exploring myriad use cases, from simulating molecules to optimising airline logistics. Yet, for any of these to become routinely used, they will have to work on many different quantum computers, so any demonstration of a truly valuable use of a quantum computer must be reproducible.

Wolfgang Mauerer at the Technical University of Applied Sciences Regensburg in Germany and his colleagues have now evaluated thousands of scientific papers on quantum computing and found that, currently, most can’t be reproduced.

Advertisement

They carried out their analysis in two parts, first manually evaluating a curated sample of 127 papers from the past five years, then using a computer program to automate and generalise this analysis to 4966 papers.

To assess the reproducibility of each paper’s results, the team used five criteria. The first three focused on determining whether the paper included code that could be run on an independent quantum computer and how much instruction and documentation for doing so was provided. The next criterion evaluated available information about hardware. Finally, the team tested whether the provided quantum computing program could run without errors.

Among the 127 papers that the researchers analysed manually, only 24.4 per cent provided code that they could even try running, and 64.5 per cent of that code failed to successfully execute. The larger, automated analysis didn’t include an execution step, but similarly found that only 26.8 per cent of the almost 5000 papers provided enough information to attempt a replication.

Compared with standards for traditional computer science studies, this is a rather negative result, says Mauerer. “We did a smaller-scale study four or five years ago, and we already found that the situation is bad, but it didn’t really improve over time,” he says. “We thought the numbers would be better by now.”

In Mauerer’s view, a big reason for this finding is the variability and inconsistency of still-maturing quantum computing hardware. For conventional computers, researchers can work at a very abstract level, describing and writing code without worrying about whether their computer’s physical characteristics may change from one day to another. This isn’t the case for quantum computers that currently exist and can, for example, be accessed through the cloud, says Mauerer. “I don’t just want to attribute the lack of reproducibility to, say, some laziness of authors or non-requirements by the community. Quantum machines in themselves are unusually variable,” he says.

“Software, especially in a rapidly evolving field like quantum computing, is a living thing and needs communities of maintainers,” says William Zeng at the Unitary Foundation, a quantum technology non-profit organisation. He says he isn’t surprised by the results of the analysis, but expects that a combination of community efforts and the use of AI agents for coding will improve the situation going forward. “[Agentic coding] is also already making it easier to generate code directly from a paper’s result that is used for reproduction,” he says.

Fred Chong at the University of Chicago says he isn’t particularly alarmed by the new analysis. “Quantum computing and software systems are in their infancy and changing rapidly. Reproducibility becomes more of a priority as the field matures,” he says. For example, in conventional computer science, it took decades for researchers to start insisting on reproduction standards for each other. “Innovation may be more important [for quantum computing] than reproducible infrastructure at this time,” says Chong.

Yet, there is appetite among quantum computing researchers to make changes for the better already, and so far, the response to the new study has been positive, says team member Ralf Ramsauer, also at the Technical University of Applied Sciences Regensburg. He says researchers should start thinking about reproducibility at the beginning of each experiment, and if they aren’t sure where to start, the team’s study offers a template for creating a reproducibility package.
