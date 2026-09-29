---
title: Anthropic Says It Discovered a Crispr-Like System. Now What?
source_url: https://www.wired.com/story/anthropic-says-it-discovered-a-crispr-like-system-now-what/
source_site: Wired
source_slug: wired
scraped_at: '2026-09-29T20:08:33Z'
published: '2026-09-29T00:00:00Z'
description: “The experiments are still in the queue. The PR is already live,” says
  one expert.
image: https://media.wired.com/photos/6abbc40baa4c41ce1b0d6fa0/191:100/w_1280,c_limit/092926-AI%20Science%20Discovery.jpg
categories:
- Technology & Software
- Science
people:
- AI
- Claude
- Crispr
- Dario Amodei
- Emmanuelle Charpentier
- Fyodor Urnov
- Jason Gill
- Jennifer Doudna
- Le Cong
- Seth Shipman
locations:
- Berkeley
- Santa Monica Beach
organisations:
- AI
- ART
- Anthropic
- Gladstone Institutes
- IGI
- Innovative Genomics Institute
- New York Times
- PR
- Stanford University
- Texas A&M University
- University of California
---

Tech executives have long touted the potential for their AI models to accelerate the pace of biology discoveries. Last week, they announced one. In a September 23 announcement, Anthropic claimed that its large language model Claude had identified an enzyme system with properties “reminiscent of Crispr,” the Nobel Prize-winning gene-editing tool.

According to Anthropic, about 950 Claude agents running simultaneously found the interesting genetic sequences in 21.5 hours. “I sincerely compliment Anthropic for telling the world about their discovery,” says Fyodor Urnov, a gene-editing expert at the University of California, Berkeley and director for therapeutic R&D at its Innovative Genomics Institute. (IGI is collaborating with Anthropic, but was not involved with the new discovery.)

Other scientists are less enthusiastic about the finding, which is the first to come out of a research group formed by Anthropic earlier this year. “The experiments are still in the queue. The PR is already live,” says Le Cong, a professor at Stanford University focused on integrating AI into genome engineering research.

Anthropic, which has set up a wet lab for drug discovery, has been clear that the finding isn’t the end of its work. (“We don’t yet understand what this system does,” the company said in an X post, “but only a handful of known systems share its features, and all of them are able to cut, copy, and paste DNA.”) One physical experiment was included in a technical report, which has not been peer-reviewed. However, a lot more needs to be done to determine the significance of this discovery. It remains unknown whether this enzyme system can be used as a gene-editing tool and, if so, whether it’s a *useful* gene-editing tool.

“Let's say we are on Santa Monica Beach and trying to scan through all the sand to find a diamond,” Cong says. “AI found this thing that looks very shiny, and then you have to go back to the lab to know—is it glass? Is it a diamond?”

Claude found this shiny object after researchers at Anthropic prompted it to search through huge genomic databases for “interesting new examples” of reverse transcriptases, proteins that copy RNA into DNA. This is the opposite of the normal process in our cells, in which DNA is transcribed into RNA, but is used by other organisms in a variety of biological functions, including inserting segments of DNA.

Claude agents initially identified more than 200,000 possible reverse transcriptases, according to Anthropic, and, after picking out several thousand that appeared to be new, narrowed the scope even further, eventually finding an “unusual” reverse transcriptase family containing a long region of repeat DNA sequences that resemble Crispr. Anthropic is calling this system ART, short for array-associated reverse transcriptases. The system is found in jumbo phages, large viruses that infect bacteria.

“I can see by eye a tandem repeat array … that's a Crispr-like … repeat array?!” an AI agent wrote. The agent also acknowledged that this system could be a retron, as noted in the technical report. Crispr and retrons are both bacterial immune systems, and while retrons have some utility in gene editing, they’re not the same multi-tool Crispr is. It’s therefore not too surprising Anthropic’s blog post played up the Crispr comparison.

Seth Shipman, associate investigator at the Gladstone Institutes, doesn’t think what Anthropic found is a new Crispr system, but says the discovery is still interesting. “The novel thing is how they found it, not what it is,” he says. His lab has used retrons to make gene-editing systems, so it is possible to use retrons in this way.

Identifying new reverse transcriptases can take months of mining genome databases manually, so Shipman says the fact that Anthropic was able to do this in a day is impressive. But he cautions against attributing the discovery entirely to an AI model. “I think we have to be careful about saying that Claude autonomously discovered something, because there are scientists involved in the study,” he says.

In fact, this same reverse transcriptase was previously identified by Jason Gill, a microbiologist at Texas A&M University, and his colleagues in a 2021 paper on jumbo phages. What’s perhaps new is that Claude identified repeats around it that hinted the enzyme might be part of a Crispr-like system.

“These models are good at finding patterns, better than a person staring at it with their eyeballs can,” Gill says. “A person could do all this but you have to already have a hypothesis in mind.” He adds that ART appears to have no “obvious relationship” to any known Crispr system, and it’s on Anthropic to prove that it actually has gene-editing activity.

Cong credits the scientists for finding the perfect kind of problem for Claude to tackle, given its pattern-seeking abilities. It’s possible the model could be used for similar large-data projects, but that doesn’t mean Claude will suddenly be accelerating all sorts of discoveries in the life sciences.

What kinds of information this model was trained on is also not something the scientific community can evaluate, which makes these findings unusually opaque in an era where major journals require scientists to freely publish their code in the name of reproducibility. This has also led a researcher who had been studying these exact enzymes to become suspicious that the model was trained on his work, since he’d shared yet unpublished findings with the public version of Claude. (“Claude was,” Anthropic told the New York Times, “not trained on any user transcripts, and our molecular biology team has no such access, either.”)

Even if Claude did identify the next big thing in gene editing, it would still take human scientists testing out that hypothesis in the lab to prove it. In a post on X about the discovery, Anthropic CEO Dario Amodei mused, “Eventually it may even be possible for Claude itself to safely perform the experiments by autonomously controlling lab equipment.” Even if this does prove possible, it will be in a fairly distant future. (The idea, of course, raises many questions about safety and oversight, and Amodei quickly followed up this thought by mentioning that Anthropic’s labs are at the lowest biosafety levels, and thus don’t contain anything greatly harmful to humans.)

Answers in this area don’t come quickly. It took 25 years from the initial discovery of Crispr sequences in bacteria in 1987 until Jennifer Doudna and Emmanuelle Charpentier demonstrated it could be a programmable tool to cut DNA in 2012. And while Crispr is now ubiquitous in labs and is being tested in dozens of clinical trials to treat cardiovascular conditions, cancers, autoimmune diseases, and rare disorders, there is only one drug on the market so far that uses the technology, approved in late 2023. It’s a testament to the long arc of scientific progress—and the difficulties of translating promising basic science findings into medicines.

The limits of Anthropic’s finding also point to a more fundamental issue. What made Crispr revolutionary was that scientists identified a biological system that was previously unknown. It remains to be seen whether any AI model is capable of finding something useful without knowing exactly what it’s looking for.

“If you have an AI that only trained on knowledge from before people ever discovered Crispr, and then that AI actually discovered Crispr, that seems to be a better setup to test an AI scientist,” Cong says.
