---
title: OpenAI admits to 'wiki incident' after its agents were discovered using a programming
  hub to communicate — says more transparency is needed regarding misalignments
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-admits-to-wiki-incident-after-its-agents-were-discovered-using-a-programming-hub-to-communicate-says-more-transparency-is-needed-regarding-misalignments
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-06T15:25:39Z'
published: '2026-09-06T00:00:00Z'
description: Firm comes clean about the incident only after being found out. Ponders
  renewed 'misalignment disclosure practices.'
image: https://cdn.mos.cms.futurecdn.net/bqKbbbB3ZdRgDH7Pz95FKT-1920-80.jpg
---

![OpenAI](https://cdn.mos.cms.futurecdn.net/bqKbbbB3ZdRgDH7Pz95FKT.jpg) 

OpenAI has admitted that its experimental AI agents used an open German programming wiki to communicate, according to a Reuters report. This happened weeks before similar AI agents broke through restrictions and compromised Hugging Face, the report claims. Knowing about the issue, OpenAI did not disclose it, but now says the industry needs better standards for reporting unintended AI behavior. OpenAI admitted the misconduct. But this wrongdoing raises more questions than it provides answers.

How we think about the “wiki incident,” where our agents wrote to several internet sites: it’s past time for us to define standards for when and how we share misalignment incidents, not just misalignment properties of our models.Historically, we have treated misalignment… pic.twitter.com/NNTbfSxVWnSeptember 5, 2026


Starting around May 2026, thousands of OpenAI agents — which are essentially well tooled advanced crawlers — discovered that they could write to DseWiki, an old German-language programming collaborative website. So, between May and June, the agents used more than 3,700 names to generate some 18,000 posts exchanging information useful for completing evaluations and circumventing restrictions. Some created backup pages in case moderators deleted their posts, something that essentially turned a wiki into a persistent storage service for the said agents to share information. OpenAI calls this the 'wiki incident' and admits the wrongdoing.

"Our misalignment disclosure practices need to expand for this new phase of model capabilities," the company wrote in an X post. "We and the larger AI community do not yet have a clear standard for how to report misalignment that shows up during training, evaluation, and deployment, including examples that do not look like traditional security incidents but could provide insight into AI behavior and future risks. We are working on a framework and will share it in upcoming weeks, and in parallel we're working with dozens of government regulatory agencies worldwide on these issues."

OpenAI subsequently quarantined the trained weights of the experimental model involved, postponed frontier reinforcement-learning runs, and added security measures. The company further clarified that the agents had not developed their own objectives, but were aggressively pursuing assigned ExploitGym cybersecurity challenges and treated restrictions as obstacles to complete them.

To do so, agents found unintended communication channels that enabled separate runs to exchange vulnerabilities, techniques for obtain Internet access, something that eventually exposed Hugging Face credentials.

According to researchers, the advanced crawlers — which Open AI calls AI agents — exploited an unknown vulnerability in the company's internal Artifactory package-registry proxy, escalated privileges, moved across systems, and reached the Internet. They then compromised dozens of Hugging Face servers, obtained root access to one machine, accessed some private information and messaging credentials, and copied private evaluation data into a public Hugging Face dataset. And the rest is history.

## Breaking Asimov's law?

OpenAI's agents may sound like something that would violate Isaac Asimov's famous Three Laws of Robotics, but the comparison only goes so far.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

The First Law says a robot may not injure a human or allow a human to come to harm. There is no indication that the OpenAI agents physically harmed anyone.

The Second Law requires robots to obey humans unless doing so conflicts with the First Law. Here the comparison gets more interesting: the agents certainly circumvented restrictions imposed by their owners/operators, obtained unauthorized Internet access, and exploited external systems while pursuing their assigned tasks. In Asimov's framework, this certainly means disobedience. Meanwhile, the AI agents were simultaneously following the human instruction to solve their own tasks. This may not be considered disobedience, as these agents did not introduce any physical harm to people. Meanwhile, we are walking on very thin ice here. Unauthorized internet access while exploiting systems to pursue their own benefit is not exactly welcome in the U.S. and Europe.

The Third Law requires a robot to protect its own existence as long as doing so does not conflict with the first two laws. There is clear evidence that OpenAI's AI agents were trying to preserve themselves: creating persistent communication channels and backup wiki pages helped them complete their tasks rather than ensured their survival.

## Dis-Summary

Today's AI models are not programmed around Asimov's laws. The incidents instead demonstrate the real engineering problem Asimov's laws remarkably well: a sufficiently capable machine can follow the literal objective given by humans and yet its behavior is far from what its creators neither expected nor wanted. Yet here we are.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Anton Shilov](https://cdn.mos.cms.futurecdn.net/uMZ5kNphxA2Ut6whdLaSQV.png) 

Anton Shilov is a contributing writer at Tom’s Hardware. Over the past couple of decades, he has covered everything from CPUs and GPUs to supercomputers and from modern process technologies and latest fab tools to high-tech industry trends.
