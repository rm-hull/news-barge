---
title: Fermat's last theorem formalised by AI agents in just 11 days | New Scientist
source_url: https://www.newscientist.com/article/2587839-fermats-last-theorem-formalised-by-ai-agents-in-just-11-days/?utm_campaign=RSS|NSNS&utm_content=home&utm_medium=RSS&utm_source=NSNS
source_site: New Scientist
source_slug: new-scientist
scraped_at: '2026-09-05T11:50:34Z'
published: '2026-09-05T00:00:00Z'
description: Converting the proof of Fermat's last theorem into code that computers
  can check was expected to take years – Anthropic's Claude AI managed it in less
  than two weeks
image: https://www.newscientist.com/wp-content/uploads/2026/09/2N9GXNJ1.jpg
---

![](https://www.newscientist.com/wp-content/uploads/2026/09/2N9GXNJ1.jpg?w=840)

AI company Anthropic has created a formalised proof of Fermat’s last theorem. It took just 11 days for a group of AI agents to complete the task, confirming that the human-found proof proposed in the 1990s is correct.

Fermat’s last theorem puzzled mathematicians for centuries until it was proven in 1995 by Andrew Wiles. It states that there are no whole numbers a, b, and c that satisfy the equation aⁿ + bⁿ = cⁿ, where n is a whole number greater than 2.

The theorem though easy to state was fiendishly difficult to prove. Mathematician Pierre de Fermat posed the puzzle in the 17th century and famously alluded to a proof that he claimed to have discovered, saying that it was too large to fit in the margins of the textbook he was writing in.

Advertisement

Many mathematicians tried and failed to find a proof. Wiles worked on the problem for seven years in secret before announcing his breakthrough in 1993. Proofs often involve lengthy logical arguments that build on each other. If a single step contains an error then the whole thing can collapse. This happened to Wiles when a flaw was found in his proof that took him and collaborator Richard Taylor around a year to fix.

Formalising mathematical theorems is a solution to this problem. It takes them out of the realm of pen and paper, and puts them into a configuration – computer code – that allows machines to grapple with them, methodically working through the logic and exposing any flaws. There are already 2 million lines of formalised mathematics stored in a central repository called Mathlib.

Earlier this year a conference of AI experts, computer scientists and mathematicians was held in London by Kevin Buzzard at Imperial College London, who was – until Anthropic’s announcement – working on a five-year project to turn Wiles and Taylor’s 100 pages of proof into computer code called Lean, so that it can be formally checked for correctness and used as a foundation for further research.

Buzzard said at the time that when his project began he was confident of success, but that recent advances in AI had convinced him that the project would be complete much faster than he previously believed possible. Anthropic’s announcement has now overtaken that effort and wrapped up the problem.

Buzzard said in a statement published by Anthropic that the company’s proof leaves “no assumptions other than the axioms of mathematics”. In short, the problem is solved.

“Along the way we see autoformalisation of algebra, harmonic analysis, geometry and number theory, and we learn that AI autoformalisation artefacts are now robust enough to be built upon; the proof is multi-layered,” said Buzzard. “If the automatic formalisation of FLT is possible now, then we have taken a big step towards automatic formalisation of the modern mathematical literature.”

Anthropic wrote in a blog post announcing the result that its Claude model worked continuously and autonomously for 11 days to write the proof. Numerous separate AI agents were involved, with different tasks like tackling smaller chunks of theorem being assigned to each.

Human experts occasionally issued “high-level instructions” to keep the work on track, the company says. And several times the agents “lost track of the project’s state and stopped collaborating effectively”. Interestingly, the company says that success came after it began using a tool designed for human mathematical collaboration called Prove2Me which helped different agents track their work and decide on next tasks.

Anthropic’s formalisation runs to 13 million lines of Lean and covers roughly 29,500 intermediate theorems that were necessary stepping stones to completing the overall work. That makes the proof over five times the current size of all previous work on Mathlib – which also makes it the largest Lean proof ever written.
