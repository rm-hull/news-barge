---
title: The hidden tax on your AI ambitions
source_url: https://www.techradar.com/pro/the-hidden-tax-on-your-ai-ambitions
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-21T10:33:27Z'
published: '2026-07-21T00:00:00Z'
description: Most AI spend is wasted long before your invoice arrives
image: https://cdn.mos.cms.futurecdn.net/9WT9t3hZhDVD84bF8rSypL-2560-80.jpg
---

![A line of robots typing at computers](https://cdn.mos.cms.futurecdn.net/9WT9t3hZhDVD84bF8rSypL.jpg) 

![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png) 

Every enterprise I talk to right now has the same complaint dressed up in different language.

Their AI bills are climbing faster than anyone budgeted. Their model invoices look reasonable when viewed on their own.

But somewhere between boardroom approvals and the monthly cloud statements, money is disappearing in ways that nobody can fully explain.

Co-founder and president of Cast AI.

Here’s the central issue that people struggle to understand: the most expensive part of AI isn't always the model itself. It's the infrastructure, orchestration, retries, idle GPUs, oversized context windows, and inefficient routing decisions that sit between a user's prompt and the final response.

This is something I call the hidden tax on AI adoption, and it's growing faster than most organizations realize.

## Three numbers that should change how you think

Recently, at FinOps X in San Diego, a Goldman Sachs projection appeared on the main stage. Current enterprise token consumption globally sits at around six quadrillion tokens. The three-year projection: 120 quadrillion. That is not a rounding error… it is a 20x expansion, and it is arriving faster than the governance frameworks to manage it.

The same conference saw our launch of the Tokenomics Foundation (I’m fortunate to be a governing board member). It’s a vendor-neutral body inside the Linux Foundation dedicated specifically to the economics of AI token consumption.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The FinOps community, practitioners who have spent the better part of a decade building discipline around cloud computing spend, recognized that tokens represent a fundamentally different problem. Not a harder version of cloud cost optimization. A different one.

Here is why. When your organization runs a cloud workload, the cost is relatively legible. You provision compute, it runs, and you receive a bill. The relationship between action and expense is traceable. With AI tokens, that relationship fractures across three layers, and most organizations have visibility into only one.

## Production → consumption → value: the three layers most teams ignore

The first layer is production. Before any AI model responds to any prompt, your infrastructure has to manufacture the tokens. GPU clusters, inference nodes, autoscaling policies, Kubernetes configurations: these are your token factories. Their efficiency, or lack of it, determines the base cost of everything that follows. A GPU node at 30% utilization is an expensive factory running at a third of capacity.

The second layer is consumption. This is where counterintuitive economics live, and it is what I spend most of my time thinking about. Two organizations can send identical prompts to different coding agents and arrive at radically different costs depending on how they manage context, caching, retries, routing, and the infrastructure supporting inference.

Prompt length, context window usage, caching strategy, and model routing decisions all compound. The common assumption that routing a task to a cheaper model always saves token cost, turns out to be wrong often enough to matter. A routing decision that invalidates a warm cache can make a "cheaper" model call more expensive than the frontier option it was meant to replace. These are second-order effects. They do not appear in standard dashboards but they appear in your monthly bill.

The third layer is value. This is the one that FinOps teams are comfortable with, and the one that matters least until you have the first two under control. Mapping token spend to business outcomes is a legitimate and important discipline. But you cannot govern at the value layer without instrumentation at the production and consumption layers. You are doing math with incomplete inputs.

## Why 85% of your AI spend is probably misallocated

Here is a pattern I see consistently. Organizations treat frontier AI models, the most capable, most expensive models available, as their default infrastructure. Every task goes to the same model. Every prompt is constructed the same way. There is no routing logic, no tiering, no architectural distinction between work that genuinely requires the full capability of a frontier model and work that does not.

Based on my observations across organizations deploying AI at scale, roughly 15% of software development tasks actually require frontier model capabilities. The remaining 85% of routine coding, summarization, classification, and retrieval work can be handled by smaller, faster, and less expensive models, if you have the infrastructure to make those decisions intelligently and automatically.

The unlock is not picking better models manually. Manual model selection does not scale and degrades the developer experience by introducing friction at the moment when a developer needs to move fast. The unlock is building infrastructure that makes routing decisions for you: one that understands the task, routes it to the appropriate model tier, evaluates output quality, and escalates if needed. You specify the outcome you need. The system handles the economics of achieving it.

This is the direction the industry is moving, and the organizations that build this capability first will have a structural cost advantage that compounds over time.

## The invoice arrives last. And you realize something has gone horribly wrong

There is a phrase I have started using with customers that captures the core problem: the invoice arrives last.

By the time you see the model provider bill, the cost decisions were made weeks ago in infrastructure configurations, autoscaling policies, and prompt architectures that nobody has reviewed since the initial deployment.

The retry logic runs silently when an upstream service slows down. The GPU nodes were reserved for peak traffic that never came. The agentic workflow, where a single user request fans out into dozens of model calls beneath it, each billed separately, none visible in the tool that generated the original request.

These costs do not live in the model invoice. They live in the infrastructure layer, in the consumption layer, and in the gap between how teams think their AI systems work and how they actually behave in production. You cannot govern what you cannot see. And right now, most teams are looking at one layer of a three-layer problem.

## When AI goes from copilot to coworker, the stakes multiply

There is a shift underway that makes all of this more urgent. The AI deployments most enterprises built over the last two years were assistants, tools that accelerated individual work by handling the first draft, the next suggestion, and the boilerplate. A human remained in the loop at every consequential step. The economics were bound by how many people were using the tool and how often.

Autonomous agents change the economic profile entirely. When an AI system can receive a goal, build a plan, execute multi-step work, evaluate its own outputs, and iterate to completion without human intervention at each stage, you are no longer running an assistant. You are running something closer to a coworker, one that operates continuously, scales horizontally, and generates token consumption at rates that individual user interactions never approached.

The transition from copilot to coworker has already happened. And the governance implications are significantly more serious. A copilot with poor token economics costs you some efficiency. An autonomous agent with poor token economics runs that inefficiency at scale, continuously, without generating the natural friction that would cause a human user to pause or change approach. Infrastructure discipline and token optimization need to be in place before autonomous workloads scale rather than retrofitted afterward when the bill arrives.

## The mandate for infrastructure teams

The right answer to this problem is not more dashboards. More visibility into a system you cannot control is just a more detailed invoice; it arrives with the same lag, and it changes nothing about the decisions that were already made upstream.

What infrastructure teams actually need is control that operates at the layer where costs are determined, not where they are reported. That means autonomous management of GPU and inference workloads, continuously rightsizing to match actual demand rather than peak assumptions, absorbing the bursty consumption patterns that agentic jobs produce, and moving compute capacity across providers when one environment becomes the bottleneck.

This is especially urgent now, because the transition from copilot to coworker does not give you a grace period to retrofit discipline. Autonomous agents do not pause. They do not get frustrated and choose a different approach. They run the inefficiency you built into them at scale, continuously, until something external stops them.

So the next phase of enterprise AI is defined by who can deploy models efficiently. As AI systems become more autonomous and token consumption accelerates, competitive advantage comes from understanding the full economics of AI, and not just the price of a model call.

Because by the time the invoice arrives, the decisions that shaped it have already been made.

*This article was produced as part of**TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:**[https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
