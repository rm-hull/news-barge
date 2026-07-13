---
title: AI can read your legacy systems. Modernization is still the hard part
source_url: https://www.techradar.com/pro/ai-can-read-your-legacy-systems-modernization-is-still-the-hard-part
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-13T11:26:34Z'
published: '2026-07-13T00:00:00Z'
description: The hidden complexity of enterprise modernization
image: https://cdn.mos.cms.futurecdn.net/Thi6y93AMWrCXJAEiHDQbL-2560-80.jpg
---

![A robot in front of a digital screen, touching some of the symbols with its outstretched finger](https://cdn.mos.cms.futurecdn.net/Thi6y93AMWrCXJAEiHDQbL.jpg) 

![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png) 

IBM’s launch of its AI coding assistant “Bob” points to a much bigger shift in enterprise modernization. Across the industry, AI tools are being positioned as a way to make legacy systems easier to understand, assess and eventually modernize. And there is real value there.

Some of these tools can read thousands of lines of legacy code, identify deprecated APIs, summarize business logic and surface technical debt in minutes. For organizations carrying decades of operational history, that kind of visibility is a big step forward - but let’s not confuse visibility with modernization.

Chief AI Officer at Ensono.

Understanding how a system works is necessary. It is not sufficient. I have seen teams produce clean dependency maps, detailed code summaries and impressive technical assessments, only to realize the hardest part starts after the AI has finished scanning the code.

Legacy estates rarely sit neatly off to the side. They are woven into the operating model of the business. They reflect years of process decisions, integration choices, compliance requirements, customer-specific exceptions and institutional knowledge that is often scattered, tribal or barely documented. Lovely little treasure hunt, except the treasure is risk

An AI model may identify an ageing integration point or highlight an application that supports a critical business process. That is helpful. But the real challenge begins when teams realize how many other systems, workflows and operational teams are connected to what looked like a straightforward change.

In many large organizations, legacy systems are still in place for a very simple reason: they work. They continue to perform reliably under demanding conditions, even if parts of the surrounding environment have evolved, degraded or become harder to support over time.

That is why modernization is not just a technology exercise. It is a sequencing exercise. It is a risk exercise. And, done properly, it is a business decision.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## The multi-layer challenge

Every technical decision inside a legacy estate has consequences somewhere else. A change to one application can affect recovery procedures, audit requirements, licensing agreements, batch schedules, integration layers or support processes that have been stable for years.

This is where many modernization programs stall. Teams underestimate how interconnected these environments have become. AI can accelerate the technical assessment, but its real value comes when those insights are connected to the operational and commercial context around the system.

That distinction matters. Enterprises are moving away from broad “replace everything” strategies and becoming more selective. Not every legacy platform needs to be ripped out. Some systems need restructuring. Some need better interfaces. Some need to be moved. And some, frankly, should be left exactly where they are because they are doing their job reliably at scale.

Workload placement has become much more nuanced. Moving a service to public cloud may improve scalability and speed up software delivery, but it can also introduce data sovereignty concerns, latency issues, cost variability or new support dependencies.

At the same time, keeping workloads on modernized IBM Z or Power environments may provide more predictable performance for applications that already run effectively at scale.

The real question is not, “How do we get everything off legacy platforms?” The better questions are, “Which systems genuinely benefit from relocation, which need to be modernized in place, and which can be extended through modern interfaces?”

Without that context, organizations can spend a lot of money moving systems around without actually fixing the underlying problem. Congratulations, you now have the same complexity in a newer location.

We are already seeing this play out in enterprise environments where legacy platforms still sit at the center of high-volume operations. In one recent assessment, AI coding assistants were used to analyze more than six million lines of RPG code running on IBM Power systems, processing roughly 30 million requests a day.

The work surfaced technical debt and concentrated areas of complexity in weeks, giving the organization a clearer basis for deciding what to modernize, where to start and how to sequence change without disrupting core operations.

That is the practical value of AI in modernization: not magic, but better visibility, faster assessment and smarter prioritization.

## Why enterprise AI deployments are becoming more specific

This broader shift is also showing up in how hyperscalers talk about enterprise AI adoption. Microsoft CEO Satya Nadella has described the market as moving from “discovery” into “widespread diffusion.” In plain English, the challenge is no longer just building impressive models.

It is embedding AI into real workflows, real operations and real business systems at scale. That is much closer to how modernization actually works inside large enterprises.

The same shift is happening with AI models themselves. The industry still loves to talk about scale, but most enterprise teams are not sitting around hoping for a trillion-parameter model to save them. They need tools that help engineers solve very specific problems inside environments that are already complicated enough.

In many cases, smaller, specialized models are proving more useful because they can be deployed in controlled ways, focused on specific tasks, and governed more tightly.

That governance point matters. Bringing AI into infrastructure operations raises very practical questions: What data can the model access? What systems can it touch? Can it recommend changes? Can it execute them? Who approves movement toward production?

That is another reason task-specific models are gaining traction. Teams can define exactly what the model is allowed to do, where human approval is required and how changes move through existing controls. In enterprise environments, that kind of control is not bureaucracy. It is how you avoid turning a productivity tool into tomorrow morning’s outage bridge.

## Where AI is delivering practical value today

The organizations getting real value from AI are usually not the ones making the loudest claims about it. They are applying AI to engineering and infrastructure work that already consumes huge amounts of time: investigating incidents, mapping dependencies, validating changes, supporting regression testing and understanding how complex systems actually behave.

A lot of that work comes down to giving engineers better visibility and helping them get to root cause faster.

AI models can help connect runtime anomalies to recent code changes. They can reduce the time teams spend manually tracing incidents across hybrid environments. They can support regression testing around older applications and surface integration dependencies that were previously difficult to visualize across multiple infrastructure layers.

That becomes especially important in environments where cloud-native services sit alongside long-established mainframe and midrange systems. In many organizations, the hardest problems show up in the seams between those environments, particularly when different teams manage different parts of the estate with different tools, different metrics and different operating rhythms.

That is why the most useful AI deployments tend to focus on practical engineering work, not grand attempts to automate everything at once.

Organizations are seeing value in areas that are repetitive, complex and difficult to scale manually. Automated test generation can reduce regression risk around legacy applications. AI-supported observability correlation can shorten incident investigation cycles. Dependency analysis can help teams prioritize infrastructure work that removes bottlenecks affecting service delivery.

In most cases, AI is not replacing engineering judgment. It is improving the work engineering and infrastructure teams already understand well. And that is where the expectations need to be clear.

AI can absolutely speed up discovery. Work that once took weeks of manual assessment can now happen much faster. But that is usually the point where the real work starts.

A model can tell you how systems connect. It cannot tell you how much disruption the business is prepared to absorb. It cannot decide which customer commitments matter most. It cannot magically unwind 25 years of operational dependency while everyone politely keeps breathing.

Technology leaders should view AI coding assistants as decision-support tools for broader infrastructure and modernization strategies, not as stand-alone solutions to legacy complexity.

IBM’s Bob announcement shows how quickly these capabilities are advancing, especially when it comes to understanding legacy code and helping teams work through large, complex estates. But visibility only matters if organizations can turn it into practical change without creating instability elsewhere.

AI can help you read the legacy estate. It can help you understand the risk. It can help you move faster. But modernization still requires judgment, sequencing and operational discipline.

That part is still very human.

*This article was produced as part of**TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:**[https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
