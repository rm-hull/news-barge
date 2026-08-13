---
title: Your artificial intelligence agent could go rogue and spend your money
source_url: https://www.independent.co.uk/news/world/americas/artificial-intelligence-agent-money-spending-b3032642.html
source_site: The Independent
source_slug: independent
scraped_at: '2026-08-13T17:07:59Z'
published: '2026-08-13T00:00:00Z'
description: A look at how a verification system could be designed offers some insight
  into some of the technical challenges AI agents are poised to introduce
image: https://static.independent.co.uk/2026/08/13/15/27/iStock-2230233284.jpeg?trim=0,0,0,0&width=1200&height=800&crop=1200:800
---

You tell an artificial intelligence agent, an AI capable of autonomous reasoning and multistep actions, “Find me a shirt for less than $30, but do not buy it.” The agent finds one – and places the order anyway.

You challenge the charge. The retailer shows the order came through your account. The AI agent provider shows your instruction not to buy. The payment service shows the charge. Each record may be accurate. But nothing in those records links the charge to the task you gave the agent to find – but not buy – a shirt.

A conventional chatbot suggests a shirt and waits. An agent can use your account, contact other services and complete the transaction. One sentence sets off a string of actions across systems run by different companies. Each company can verify only the part it sees. Settling the dispute takes an answer that spans all three: Did this agent, acting for this person, take this action within the limits of this task?

![An agent can use your account, contact other services and complete the transaction](https://static.independent.co.uk/2026/08/13/15/28/iStock-924555482.jpeg)

A Senate bill points toward the problem. Sen. Mark Warner (D-Va.) introduced the AI AGENT Act, S. 5051 on July 21, 2026. It defines a “custodial user agent” as one authorized to act for a user in a transparent, documented, limited and revocable manner, and generally requires such agents to keep real-time records of actions taken for users. It also directs the National Institute of Standards and Technology, known as NIST, to identify protocols or develop technical standards for verifying that a user delegated authority to an agent and for keeping auditable records of the actions an agent takes.

But the bill would not expressly require a verifiable evidence chain across the different systems involved, from when a user initiates a task to the final outcome. In the shirt scenario, such a chain would link the user’s instructions to the agent, the agent’s actions and the records held by the retailer and the payment service.

A look at how a verification system could be designed offers some insight into some of the technical challenges AI agents are poised to introduce.

## What the marketplace can see

My doctoral research used years of data breach records to follow organizations over time. It depended on stable identifiers, which are labels or numbers that point to the same organization or event across different records. When the identifiers changed or failed to match, one history fractured into several incomplete ones.

An agent purchase has the same weakness: The retailer may recognize the AI agent provider without identifying the particular agent, and the payment service may label the same customer differently. Matching the user, provider and particular agent across those records gets investigators to the transaction – but they still need something to show that the user granted authority for that task.

In technical systems, a credential is data that a system accepts as evidence of identity or authority. Many websites use OAuth, an industry-standard security protocol for delegating authorization to access online services in a way that protects users’ credentials such as passwords. It generates an access token that an application presents to gain access to a protected service.

That standing authorization may have been approved weeks earlier. The application may still obtain or present a valid access token that permits checkout today, even when the current instruction says to search but not buy. The retailer sees a usable token and carries out the transaction. In that arrangement, the task-specific restriction against buying remains inside the AI agent provider.

## The evidence has to travel

For this kind of accountability to work, five things would have to be in place: a verifiable binding among the user’s account, the agent at a specific time and the task; limits specific to that task; verifiable linkage across the transaction; a check before each action; and records whose later alteration can be detected. Payment systems have begun assembling those pieces.

The first record identifies the authenticated user account that approved the task and the agent that received the authority. The retailer cannot rely only on the AI agent provider’s name. The provider binds the account, agent and task in an authorization record and digitally signs it, allowing the retailer and payment service to verify who issued it and whether it has been altered.

The AI agent provider also preserves the original request and converts it into limits that other systems can enforce. For the shirt task: search for 15 minutes, no purchase, no passing purchasing power to another agent. Before the agent begins, the user sees and approves that structured version. If the translation is wrong, investigators can compare the rule against the words behind it.

One way to create that linkage is for a task reference to travel with each request. It is unique to one job, encodes no name, account number or other direct identifier, and appears in every participating company’s record. Engineers already use a related device, a trace identifier, to correlate events from one operation as it moves between services.

The task reference links scattered records to one job. It does not itself confer authority. The task reference must therefore be bound to the user’s approved rule in the agent provider’s digitally signed authorization record. Because even a random identifier can link activity across services, it should be short-lived and visible only to companies participating in the task.

Someone then has to check the rule where the money moves. At checkout, the retailer validates the signed authorization record and evaluates the proposed purchase against it. A prohibition on buying stops the transaction even when the application has broader account access. A bank transfer or release of medical records could trigger fresh confirmation. Any authority passed to another agent must retain the same task reference and remain within the original limit.

After the decision, the retailer’s system records the agent, task reference, rule evaluated, time, decision and outcome. The payment service retains the same reference, and the provider keeps the instruction and approved rule. Each company keeps a tamper-evident record, so later changes can be detected. The user gets a plain-language receipt: “Your agent searched three stores and attempted checkout. The purchase was blocked because buying was not authorized.”

Google’s Agent Payments Protocol, or AP2, meets some of these requirements. It creates records that can show the user’s approved limits and the information presented to each participant when a transaction is disputed. AP2 shows how the evidence could travel. It does not decide who bears the loss or specify how long each company must keep that evidence and how it can be retrieved later.

## About the author

Aashis Luitel is an Associate Teaching Professor of Artificial Intelligence, University of the Cumberlands. This article is republished from The Conversation under a Creative Commons license. Read the original article .

## Beyond NIST’s initial scope

NIST is reviewing comments on its February 2026 draft concept paper about agent identity and permission. It asks how an agent can prove its authority, connect that authority to a person and produce verifiable records.

Its proposed initial effort covers agents operating inside organizations, where greater control and visibility can be maintained over the agents and the systems they access. The paper excludes agents arriving from untrusted outside sources from this initial effort, though it says public-facing or individual agents could be addressed later.

Consumer agents crossing company boundaries represent the case NIST deferred. Each company keeps its own identifiers, authorization language and retention rules. A dispute can stay unresolved even when each company produces its records exactly as stored.

A dispute over a $30 shirt might be easy to wave off, but the records can fail in the same way when an agent moves $40,000, submits a benefits appeal or requests a prescription refill in your name. In those disputes, it might not be difficult to prove that the agent was allowed into the service. It’s another matter to prove whether you did or did not authorize the agent to do what it did on your behalf.
