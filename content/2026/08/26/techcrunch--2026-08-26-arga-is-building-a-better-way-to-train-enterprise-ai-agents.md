---
title: Arga is building a better way to train enterprise AI agents | TechCrunch
source_url: https://techcrunch.com/2026/08/26/arga-is-building-a-better-way-to-train-enterprise-ai-agents/
source_site: TechCrunch
source_slug: techcrunch
scraped_at: '2026-08-26T13:11:41Z'
published: '2026-08-26T00:00:00Z'
description: Arga has raised $10 million in a seed funding round that was led by General
  Catalyst, with participation from Box Group, Emergence, Gradient and SV Angel.
image: https://techcrunch.com/wp-content/uploads/2026/08/Arga-Headshots.jpg?resize=1099,1200
---

Making AI agents work is turning out to be a lot harder than many companies expected. Luckily for them, there’s help on the way: A new crop of startups is finding better ways to test and train agents before they are deployed, particularly on the complexities of the modern enterprise.

Arga is one such company. The startup on Wednesday said it had raised $10 million in a seed funding round that was led by General Catalyst, with participation from Box Group, Emergence, Gradient and SV Angel.

Arga builds training environments for enterprise software like Salesforce, Workday, and email clients. Where most testing environments offer a stateless API endpoint, Arga builds a full-scale digital twin of the program, effectively cloning the entire software with permission systems and web hooks intact. The result is a more robust way to train agents across multiple systems.

The startup’s CEO and co-founder Philip Li illustrated his product with the example of a prospective client creating a lead in Salesforce while a colleague reaches out separately through Hubspot.

“Can the agent correctly identify that these two are the same company?” Li says, “Are they able to check whether or not they’ve only sent the email once? Are they able to identify who to send the email to out of the two opportunities?”

Agentic systems still struggle with this kind of ambiguity, and Li sees Arga’s tools as critical to helping them improve.

Normally, an AI agent could be trained for a task like this through reinforcement learning (RL): running the scenario tens of thousands of times and letting only the successful strategies through. But the nature of enterprise software makes that scale of testing nearly impossible. There’s no easy way to “reset” a system like Salesforce or Outlook when you need to run the same scenario again, much less clone it.

Arga’s solution is to digitally recreate that software by replicating its structure the way a crash test dummy is supposed to stand in for a person. Because Arga has complete control over the environment, the resulting recreation is simple to reset or modify. The company can also run many environments at once to train agents on the complex interactions between different programs. The idea is to replicate a person’s full work environment, with specific tasks overlapping across different programs and knowledge systems.

You can think of it as a way to close the reinforcement gap between coding and other applications. Part of the reason AI coding tools have advanced so quickly is that we already have sophisticated tools for deploying, reversing and analyzing new code. Those tools make it much easier to set up RL environments for coding, which lets us test and train AI systems on increasingly complex coding tasks.

Those tools don’t exist for most business software — yet. But once they do, AI systems are likely to get much better at using those programs, and revolutionize other industries the same way they’ve revolutionized coding.

General Catalysts’ managing director Yuri Sagalov, who also runs the firm’s seed investing program, says he sees a growing need for agentic testing tools like Arga.

“I think that a lot of the economic value from agents is from using business applications,” Sagalov told TechCrunch. “Having a repeatable sandbox environment is very important, and much more important with agents than it was with humans.”
