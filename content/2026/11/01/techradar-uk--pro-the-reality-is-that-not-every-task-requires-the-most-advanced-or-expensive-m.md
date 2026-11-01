---
title: '''The reality is that not every task requires the most advanced or expensive
  model available'': Snowflake explains why finding the right AI model can make all
  the difference in helping your business succeed'
source_url: https://www.techradar.com/pro/the-reality-is-that-not-every-task-requires-the-most-advanced-or-expensive-model-available-snowflake-explains-why-finding-the-right-ai-model-can-make-all-the-difference-in-helping-your-business-succeed
source_site: TechRadar UK
source_slug: techradar-uk
description: Snowflake tells us how to solve the AI economics problem
image: https://cdn.mos.cms.futurecdn.net/dyqv6mszWWV7hVh4EWjzKT-970-80.jpg
published: '2026-11-01T00:00:00Z'
scraped_at: '2026-11-01T13:07:43Z'
categories:
- Technology & Software
- Business & Entrepreneurship
- Personal Finance & Investing
people:
- AI
- Grace Adamson
locations:
- AI
organisations:
- AI Product Marketing Manager
- AI ROI
- Cortex AI Gateway
- Formula One
- Snowflake
- TechRadar Pro
---

![big data business ai](https://cdn.mos.cms.futurecdn.net/dyqv6mszWWV7hVh4EWjzKT-970-80.jpg)

With AI now an integral part of everyday working life for most large businesses, the focus has now switched to ensuring your organization is getting the most from its AI investment.

Snowflake has long been at the forefront of the AI coalface, and recently launched new capabilities to help its customers automatically select the best model based on quality, speed, preferences - all while tracking AI spend with greater control, hopefully solving this issue at a time when budgets are tighter than ever.

We spoke to Grace Adamson, AI Product Marketing Manager at Snowflake, to find out more.

* **For the past two years, much of the conversation has focused on finding the most powerful AI model. Is the next phase of enterprise AI actually about selecting the right model for each task - one which balances quality, latency, cost and business value?**

During the first wave of generative AI, the focus was significantly on model power. The AI race was more experimental, largely trying to achieve the highest quality outputs or solving the most complex tasks.

Fast forward to today, and organizations are shifting from AI experimentation to driving real business outcomes with AI. As such, businesses are now focused on understanding how they can generate the greatest return from every AI interaction.

The reality is that not every task requires the most advanced or expensive model available. Some workloads demand sophisticated reasoning, while others involve repetitive classification, summarization, or extraction tasks that can be handled effectively by more efficient models, including the latest generation of open source models, at a fraction of the cost.

This new paradigm is what we call intelligence efficiency, essentially how effectively organisations turn models, data, and compute into measurable outcomes and value. That’s possible through dynamic model routing, native governance, and having AI built directly alongside an organization’s trusted data, so it understands the business context behind every request. This means organizations can execute their AI workloads on the most suitable model, all while better managing AI costs.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

* **Snowflake has talked about “dynamic model routing” as a way of automatically matching workloads to different models. What problem does this solve for customers in practical terms, and how does it help turn AI experimentation into measurable business impact? Can companies really stop thinking about model selection and focus instead on outcomes?**

One of the biggest challenges enterprises face today isn't a lack of models, it's an excess of them. New models are appearing weekly, each with different strengths, pricing structures, and performance characteristics. Deciding which model should handle which task can quickly become an operational burden.

Dynamic model routing in Cortex AI Gateway addresses that by automatically directing workloads to the model that best balances quality, speed, and cost for a particular use case. For example, a simple task may be routed to a highly efficient open-source model, while a more complex request that requires deeper reasoning can be directed to a frontier model. This is the new reality of AI economics. Organizations achieve the level of performance they need, without paying premium costs for every interaction.

This should all happen inside the governance boundary. The same governance policies and controls, including masking, apply to any model that handles a request, open or proprietary, so choosing a more efficient model never means compromising on security.

Customers also control which models and providers are available to their users, which really matters for global organizations that have to navigate regional availability or regulated industries with specific compliance requirements. For those end users, model choice should be seamless and invisible, while for builders and admins it should be simple to set up and manage.

Business leaders can now be measured on whether their AI applications succeed in improving productivity or accelerating decision-making. While model selection will always matter at a governance level, it shouldn’t be something every employee or user has to constantly manage.

The most successful enterprises are already optimizing their model usage based on performance, cost, and which model will generate the business outcomes that matter most.

* **Many organizations are discovering that the most capable model is not always the most economical model. How should businesses think about the trade-off between intelligence, speed and cost when deploying AI at scale?**

A common mistake business leaders make is assuming that the highest-performing model should be used everywhere. Many enterprise workloads don't require frontier-level reasoning. If you're processing large volumes of documents, such as extracting information from contracts, a highly efficient model may deliver almost identical outcomes to a frontier model, at a significantly lower cost.

At scale, those savings become substantial. In our internal testing, agents using dynamic model routing built a dbt pipeline with up to three times greater token efficiency than a frontier model only approach, while maintaining the same quality.

Even small differences in token consumption or inference costs can compound rapidly when organizations are processing millions of requests per month. That's why leading enterprises are increasingly evaluating AI systems based on business economics rather than benchmark scores alone. The best decisions weigh model capability, speed, and cost together, not in isolation.

* **How does Snowflake help customers decide when a simple, lower-cost model is sufficient and when a more advanced frontier model is justified? Is there a risk that businesses are overpaying for AI because they’re applying the same model to every use case?**

Standardizing workflows on a single model carries a real risk of overpaying. It’s like using one Formula One car for every journey, whether you're racing around a track or merely driving to the supermarket. The performance doesn’t always fit the need, and neither does the cost.

Snowflake helps customers establish policies around quality, performance, and cost, then uses dynamic model routing to make intelligent decisions within those parameters. This means that teams don’t have to manually evaluate every new model or rebuild applications each time the market changes. Organizations can focus on defining and setting business objectives, and the platform handles the model selection behind the scenes.

This matters more as the gap between frontier and open models continues to narrow for common enterprise tasks. Open models are improving rapidly and, for well-defined workflows, often make more commercial sense. However, the most effective AI strategy preserves flexibility. Snowflake has always been cloud agnostic, and we’re applying the same principle to models. Our model agnostic platform gives organizations the full breadth of choice, so they can select the right model for each task, maximizing AI efficiencies.

* **One of the biggest concerns for executives is AI spend becoming unpredictable. How important is observability, whether that's tracking usage, performance, latency and cost, in making AI a manageable business investment rather than an open-ended expense?**

Observability is fundamental, both to us and our customers. Business leaders are often comfortable with investing in AI, but hesitant to make investments they can’t monitor.

Observability now needs to extend beyond technical monitoring into whether the implementation is working at every level of the enterprise. Organizations need visibility into usage patterns, model performance, latency, consumption, and cost allocation to understand which teams are driving value and whether outcomes justify the investment.

That’s why we’ve built visibility and cost controls directly into the platform, bringing token usage and costs across AI apps and agents into one place, including any third-party agents connected through Cortex AI Gateway. Organizations can also set spending limits and quotas, and even attribute costs to specific teams.

This is particularly important as organizations move towards agentic systems and AI-powered workflows. The more autonomous these systems become, the more important it is to have governance and economic controls in place. Observability isn’t just useful at that point, it’s essential.

* **AI has often been described as a productivity technology, but boards increasingly want evidence of ROI. What metrics should companies use to judge whether their AI investments are actually delivering business impact?**

I’d first advise that usage alone is not ROI. Organizations often mistake high adoption rates for meaningful and measurable business outcomes.

They should start by identifying the objective of a particular AI initiative, and measure the impact against that goal.

It helps to think about AI ROI in two buckets. General productivity gains are harder to measure directly, so organizations often rely on proxies such as time to value, faster project completion or employee satisfaction scores. Specific business use cases, such as fraud detection, risk reduction or revenue upsell, can be tied directly to hard numbers.

Financial measures can be equally as important. Boards increasingly want to understand whether AI is creating revenue opportunities and improving margins. Those metrics are often more persuasive than purely technical measures, because they connect directly to business performance.

A final, but significant, metric we’d measure is around intelligence efficiency, as this is how effectively an organization can convert AI resources into business value. That means looking at outcomes relative to the cost, because a solution that delivers similar results at half the cost may ultimately provide greater value.

* **Do you think enterprises are moving from a world of “model-first” AI strategies to “workload-first” strategies - in other words, starting with the business task and then dynamically selecting the most appropriate model behind the scenes?**

Enterprises are starting to move in this direction, which is a natural sign of market maturity. We're seeing growing interest in workload-first approaches where organizations define their desired outcomes; establish guardrails around cost, quality, and governance; and then allow platforms to dynamically match workloads to the most appropriate model. In many ways, this represents the evolution of enterprise AI from experimentation to optimization.

This is in part because organisations are feeling the pressure of rising model costs and looking for smarter ways to get the same outcomes. The growing focus on minimizing token consumption shows that organisations are becoming more cost-aware. I’m confident that as enterprises become increasingly agentic, they’ll start having the right “workload-first” conversations, starting with desired outcomes and drawing the best path to action from there.

* **Snowflake’s approach seems to suggest that AI infrastructure should become increasingly invisible to end users. Is the long-term goal that employees simply ask a question or initiate a task, while the platform automatically handles model choice, governance and cost optimisation?**

That goal is already happening. Organizations are focused on outcomes, and the most effective platforms are quietly managing the complexity underneath. The reason is pretty simple, as most organizations don't want to become AI infrastructure experts. They don’t want to evaluate model benchmarks, compare token pricing, or decide which model should handle a particular task. Employees want reliable, trustworthy tools that help them do their jobs more effectively. That’s precisely what they should get.

The barrier for most organisations isn’t actually capability. You still hear stories of organizations focused on adoption metrics, measuring AI by how many people are using it rather than what it’s delivering. That gap is closing quickly, but it remains a key obstacle for firms wanting to demonstrate real value.

Importantly, invisible doesn't mean uncontrolled. If anything, governance and observability become more critical as AI becomes more deeply embedded across the organisation. With open and proprietary models running side by side on the same platform, the same governance applies to whichever model is used, data stays where it is, and teams can switch models without new contracts, security reviews or being locked into a single provider.

* **If you were advising a CEO on how to turn AI investment into business value over the next two years, what would your priorities be? Would you focus first on governance, cost visibility and identifying high-value use cases before scaling AI more broadly?**

I would first advise CEOs to resist the temptation to start with technology and instead start with outcomes.

The “winners” of today’s AI race typically have a clear understanding of the problems they're trying to solve, and build the infrastructure anchored in these outcomes. In practice, that means business owners and data and AI teams working in tandem, starting from business priorities. At the same time, they should be building an open architecture that can adapt, because no one knows exactly how the technology landscape will develop.

From there, governance and visibility become essential foundations. Leaders need confidence in how their AI is being used, what it costs, and what data it can access. That foundation of trust is what drives genuine adoption across the business. As a next priority, I would identify a small number of high-value use cases that can demonstrate tangible impact. Successful pilots create organizational confidence and provide the evidence needed to scale investment more broadly.

Finally, I would focus on people and process transformation. AI requires organizations to rethink workflows entirely, meaning the people and process side of transformation deserves as much attention as the technology itself.
