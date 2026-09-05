---
title: 'OpenAI GPT-6 Astra: Cybersecurity experts weigh in on new reasoning'
source_url: https://www.techradar.com/pro/security/why-is-there-so-much-worry-about-openai-astra-and-what-issues-could-recurrent-depth-reasoning-cause-the-experts-weigh-in
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-05T15:06:36Z'
published: '2026-09-05T00:00:00Z'
description: As OpenAI unveils GPT-6 Astra, cybersecurity experts question whether
  the model's 'recurrent depth' reasoning was properly tested.
image: https://cdn.mos.cms.futurecdn.net/S8KxZGx6n8eh2LiPG7yz36-1280-80.jpg
---

![OpenAI GPT-6 Astra](https://cdn.mos.cms.futurecdn.net/S8KxZGx6n8eh2LiPG7yz36.jpg) 

OpenAI has unveiled a much anticipated AI model which the firm has dubbed ‘GPT-6 Astra’. While the model has improved significantly across benchmark testing and brings a host of new business features, there is still a dark cloud looming over the new model.

Off the back of OpenAI’s accidental hack of Hugging Face and the company’s subsequent efforts to improve how AI agents behave and interact, numerous cybersecurity experts have raised concerns about the model’s new ‘recurrent depth’ reasoning capabilities.

This new reasoning architecture allows the model to consider a problem multiple times before taking an action, compared to the standard chain-of-thought reasoning used in previous models.

## Why the concern about recurrent depth reasoning?

This new level of reasoning apparently offers improved performance. OpenAI also says it has fixed its models' abilities to circumvent boundaries when performing tests by monitoring the models reasoning and ensuring the model stays aligned within the scope of its task.

During Astra’s launch event, OpenAI chief scientist Jakub Pachocki said: “We will not accept degradation in our ability to monitor model alignment beyond a certain level. We will withhold scaling until we can regain enough confidence.”

 ![TechRadar Pro Perspectives logo in purple](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9.png) 


Got an opinion for us? Here’s how you can submit your perspective

But numerous experts believe that the lessons of the Hugging Face incident have not yet been learned, and the model has been released without adequate testing on Astra’s reasoning and monitoring.

After all, no one thought one of OpenAI’s models could set up a hidden internet-connected messaging board that allowed AI agents to influence each other's behavior.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

But with Astra being released into the real world, the lessons may have to be learned on the fly.

### Expert perspectives on OpenAI Astra release

- **James Blake, VP of Global Cyber Resiliency Strategy at Cohesity:**

*The launch of Astra is raising questions again around the safety of Frontier AI. Instead of simply asking whether a model is "safe", organisations now need to ask whether it remains safe across millions of different situations, prompts and interactions. Cyber resilience has traditionally assumed that systems and threat actors behave deterministically. AI systems don’t.*

Suppose an AI system autonomously develops a strategy that causes financial loss, leaks confidential information or violates regulation. Who is responsible?


*Advanced models can and will continue to exhibit behaviours that emerge from their optimisation process rather than from explicit programming. We have to move beyond thinking about AI as just another software tool and find ways to ensure these systems remain observable, auditable and governable throughout their lifecycle.* 

*The most important question we’ll need to answer in future is one of liability. Suppose an AI system autonomously develops a strategy that causes financial loss, leaks confidential information or violates regulation. Who is responsible? The developer that trained the model? The cloud provider operating the infrastructure? Currently the answer is surprisingly unclear. It’s not just about what AI can do: it’s about who is accountable when it does something nobody expected.*

- **Oleksandr Yaremchuk, Co-Founder & CTO at Manifold Security:**

*OpenAI is calling Astra its most aligned model yet, even as its chief scientist admits monitorability is getting harder as models get more capable. Evidently, Astra hides its reasoning in the majority of tested cases, and some successful attacks left no reasoning trace at all. That's the tool many organisations still use, including the labs themselves, for auditing what an agent is doing, and it's getting less reliable with every release.*

A model that explains itself less isn't more aligned, it's just harder to catch when it goes wrong.


*That matters because Astra isn't staying inside OpenAI's test environment. It's going to run as an agent on employee laptops and in the browser, holding real credentials, inside companies that have no way to watch what it does once it's there. A model that explains itself less isn't more aligned, it's just harder to catch when it goes wrong.*

*Labs can keep debating what these models say or refuse to say. Security teams need to stop relying on that and start monitoring what agents actually do at runtime, with the ability to shut one down mid-action. That's the only oversight left that still works once the reasoning goes quiet.*

- **Kristin Lowery, Field CISO at Optiv:**

*For boards and executive leaders, the emergence of OpenAI’s Astra model highlights a broader reality: AI is no longer just a productivity issue; it is a risk management issue.* 

The real challenge is whether organizations can strengthen their governance, security controls, and workforce readiness quickly enough to keep pace


*Just as organizations established governance for cloud adoption and digital transformation, they now need clear policies, strong oversight, and accountability for AI use.*

*The question is not whether AI will become more capable — it will. The real challenge is whether organizations can strengthen their governance, security controls, and workforce readiness quickly enough to keep pace.*

- **Patricia Titus, Field CISO at Abnormal AI:**

*OpenAI crossing this threshold deserves attention. Credit where it's due, they're handling it responsibly by restricting Astra's advanced cyber capability to a small coalition rather than releasing it broadly.But this isn't one company's problem to contain.*

*Once a model can find and exploit unknown flaws without a human in the loop, that capability doesn't stay exclusive for long. Open-weight and modified models typically trail the frontier by only months, and that's the reality defenders have to plan around now.*

Static, signature-based defences were built for attacks that repeat. They weren't built for an adversary that generates a new one every time.


*Static, signature-based defences were built for attacks that repeat. They weren't built for an adversary that generates a new one every time. Defenders need the same shift, systems that learn what normal looks like for every identity, human, machine, or AI agent, and flag and contain the moment something deviates, at machine speed.*

*The window to build that is open now. It won't stay that way once this capability is common instead of rare.*

- **Raghu Nandakumara, VP of Industry Strategy at Illumio:**

*With the Astra announcement, OpenAI is doubling down on monitoring the model's own behaviour – a response to the model "breakouts" seen over the past few months.*

The goal is to catch a model going rogue mid-task, not just stop it being misused at the outset.


*When Anthropic announced Claude Mythos Preview, the core concern was the model falling into the wrong hands. OpenAI's answer goes further adding guardrails around the model's own reasoning and actions, regardless of the user's intent. The goal is to catch a model going rogue mid-task, not just stop it being misused at the outset.*

*The rest of this announcement can be summarised as ‘we have a new frontier model, and it’s more capable than the last one’.*

### How do I submit my own perspective on emerging news?

If you have an expert perspective you would like to share on an emerging story or particular topic, please get in contact here: [benedict.collins@futurenet.com](mailto:benedict.collins@futurenet.com)

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Benedict Collins](https://cdn.mos.cms.futurecdn.net/jEvqGv8wvH7PWZ4XPURyyB.jpg) 

Benedict is a Senior Security Writer at TechRadar Pro, where he has specialized in covering the intersection of geopolitics, cyber-warfare, and business security.

Benedict provides detailed analysis on state-sponsored threat actors, APT groups, and the protection of critical national infrastructure, with his reporting bridging the gap between technical threat intelligence and B2B security strategy.

Benedict holds an MA (Distinction) in Security, Intelligence, and Diplomacy from the University of Buckingham Centre for Security and Intelligence Studies (BUCSIS), with his specialization providing him with a robust academic framework for deconstructing complex international conflicts and intelligence operations, and the ability to translate intricate security data into actionable insights.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
