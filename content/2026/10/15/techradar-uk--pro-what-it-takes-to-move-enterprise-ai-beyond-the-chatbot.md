---
title: What it takes to move enterprise AI beyond the chatbot
source_url: https://www.techradar.com/pro/what-it-takes-to-move-enterprise-ai-beyond-the-chatbot
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-15T11:29:57Z'
published: '2026-10-15T00:00:00Z'
description: How businesses can optimize AI
image: https://cdn.mos.cms.futurecdn.net/Thi6y93AMWrCXJAEiHDQbL-2560-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Meng Liu
locations: []
organisations:
- AI
- AP
- ERP
- Forrester
- Future plc
- LLM
- MCP
- Ottimate
- TechRadar Pro
- TechRadarPro
---

![A robot in front of a digital screen, touching some of the symbols with its outstretched finger](https://cdn.mos.cms.futurecdn.net/Thi6y93AMWrCXJAEiHDQbL-1920-80.jpg)
![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png)

By now, most enterprise executives have heard plenty of generic claims that AI will transform the way work gets done. But in many cases, their initial AI investments haven’t delivered the level of transformation they were promised.

An LLM can summarize information, answer questions, and suggest next steps. But on its own, it can’t take action on that information. In fact, without connections to key business systems, an LLM is essentially a chatbot with a polished writing style.

CEO of Ottimate.

Consider a finance team processing invoices. An isolated LLM might accurately summarize a supplier invoice. But it can’t match the invoice to a PO, determine whether it’s been paid, or see if it’s coded to the correct GL account. It needs more information to make those decisions, and that information exists outside of the AI tool.

For AI to take an active role in business processes, it needs access to the systems where context lives. The Model Context Protocol (MCP) can provide the infrastructure for secure connections. This shift is already taking shape in accounts payable.

## What MCP actually changes

The impact of an LLM depends on what it has access to. If the information it needs to make a reliable decision lives in an ERP, vendor database, or other business system, the model needs a way to access it.

Connecting AI to business context hasn’t always been straightforward. Different applications may require different integrations for the same systems, which quickly gets complicated as businesses add more AI tools.

The Model Context Protocol provides a standardized way for AI applications to connect with external systems and data sources. When AI needs access to a new source, developers can use MCP, rather than creating a custom connection for every application and system.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

MCP changes what AI can actually do. With the right connections, AI agents can pull relevant data, use that information to make decisions, and take action within the boundaries defined by the business. MCP can facilitate bidirectional connections, so AI can also send information back to core business systems. For example, an AI agent might update a record, route something for approval, or trigger another step in a process.

While MCP provides the infrastructure for connecting AI to business systems, it doesn’t mean agents should suddenly be given free rein. The level of autonomy AI agents can reasonably handle today still varies quite considerably by task and implementation. As Meng Liu, Principal Analyst at Forrester, recently said, “agentic branding is widespread, but real autonomy is not.”

That said, AI agents don’t need complete autonomy to take on a more active role in business processes. Accounts payable is a useful example of what connected AI looks like in practice and how it can drive impact for the business, even without total autonomy.

## AP shows what connected AI can do

the business needs to confirm that item prices match what they agreed to in the contract, the products were delivered, the invoice hasn’t already been paid, and that each line item is coded to the right account. If those checks don’t happen, there are more opportunities for errors and avoidable losses to sneak their way through.

Traditionally, those checks depended on people. Even today, when automation is widespread, an exception often ends up in a queue, and an AP employee must dig through purchase orders, receiving records, contracts, and past invoices to sort it all out.

That manual work comes at a cost. According to Ardent Partners’ State of ePayables 2025, the average cost of processing an invoice is $9.84, compared to $2.65 for best-in-class organizations.

But consider how things could change if an AI agent had access to the same data sources the AP employee does. Let’s say a restaurant receives an invoice for 20 cases of chicken at $42 per case. The AI agent can compare the invoice to the purchase order and receiving records and determine that only 18 cases were delivered. It can also see that the invoice cost per case is $5 more than the agreed-upon contract price.

When the numbers don’t match, the invoice won’t automatically end up in an exception queue because the AI agent has the context to investigate further and take action.

Depending on the agent’s findings and the business’ policies and guardrails, it could request a credit from the vendor, route the discrepancy to the appropriate employee with recommended next steps and supporting evidence, or clear the invoice for payment if everything checks out.

This same concept can be applied to a whole host of other AP decisions. For example, an agent with access to vendor history data can identify a possible duplicate invoice before payment goes out. One that’s connected to the general ledger and historical coding can determine the appropriate GL codes for a new invoice. A third that has access to approval history and company policies can determine who needs to approve an invoice next.

In each scenario, the agent’s ability to decide and act depends on whether it can access the right information. In AP, there’s an easy way to tell whether those decisions are really working.

## AP is good test of AI autonomy

Touchless processing is the goal of implementing AI in AP. This is when an invoice is captured, validated, coded, approved, and paid without a person stepping in. If an AI agent completed all of those steps accurately on its own, the invoice was processed touchlessly. If a person had to step in at some point, it wasn’t. There’s no in between.

That straightforwardness makes AP a great proving ground for connected AI. There’s something concrete to measure, and mistakes can have real consequences. If an invoice isn’t processed correctly by AI agents, it can lead to issues such as manual rework, overpayments, missed discounts, and inaccurate accounting records.

In other areas of the business, AI's success can be harder to measure. For instance, a chatbot can save an employee some time by summarizing information and drafting emails. But that impact is difficult to quantify, and there isn’t always a clear measure of whether the AI did its job successfully.

AP gives businesses that measure. As leaders consider where AI agents can take on more responsibility across the enterprise, AP is a useful place to see what autonomy really looks like.

## Look beyond the “AI-powered” label

Today, plenty of enterprise technology vendors throw around the phrase “AI-powered.” Before making any technology investments, business leaders must ask the right questions to understand what this actually means in practice.

There’s a big difference between adding a chatbot to an existing platform and securely connecting AI to the context it needs to make decisions and take an active role in business processes. MCP can help close that gap and move enterprises closer to those promises of business transformation.

*This article was produced as part of* * TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:* * [https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)
