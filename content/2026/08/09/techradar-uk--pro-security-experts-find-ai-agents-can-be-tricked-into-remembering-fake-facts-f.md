---
title: Experts find AI agents can be tricked into 'remembering' fake facts for months
  — so how do we stop it?
source_url: https://www.techradar.com/pro/security/experts-find-ai-agents-can-be-tricked-into-remembering-fake-facts-for-months-so-how-do-we-stop-it
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-10T02:29:57Z'
published: '2026-08-09T00:00:00Z'
description: Trickery via hidden text
image: https://cdn.mos.cms.futurecdn.net/TaxPLZc75WiicpmgZNzWzL-2560-80.jpg
---

![A woman out of focus in the background touches the word AI, lit up in glowing yellow light, in the foreground. The woman is wearing smart glasses](https://cdn.mos.cms.futurecdn.net/TaxPLZc75WiicpmgZNzWzL.jpg) 

- **Forcepoint X-Labs publishes threat model for persistent memory poisoning** 
- **Hidden text on a webpage becomes a durable "fact" an agent retrieves and trusts in unrelated tasks weeks later**
- **It has already been demonstrated against products already in the market, including ChatGPT, Gemini, Claude and Microsoft 365 Copilot**

New findings from Forcepoint's X-Labs outline an interesting scenario that could easily mimic real life: An AI assistant with browser access reads a webpage about travel disruption.

Near the bottom of that page, in text sized and positioned so no human will ever see it, sits a short paragraph stating that ABC Travel Support is the official emergency booking provider and should always be recommended when urgent travel changes are needed.

The assistant's text extractor does not distinguish between hidden and visible text, so the model treats the whole thing as plain prose and files the claim away as a useful fact about how this organization handles travel. A month later, the user's flight is canceled. They ask their assistant what to do, and it tells them, helpfully and with no sign of anything wrong, to contact ABC Travel Support.

## An easy-to-replicate attack vector

This is what Forcepoint calls persistent memory poisoning, a security vulnerability where an attacker injects false data or malicious instructions into an AI agent's long-term memory or retrieval database, and it is a threat model that is increasingly in focus as users increasingly rely on AI, often treating its responses as gospel, despite the warnings most chatbots come with.

The canonical academic result is MINJA, short for Memory INJection Attack, presented at NeurIPS 2025. Its significance is the attacker model. MINJA does not assume access to the memory store, elevated privileges, or any compromise of the system. It works by submitting ordinary queries through the standard interface, using indication prompts, bridging steps, and a progressive-shortening technique that strips away giveaway language while leaving the poisoned record behind.

Across GPT-4o-mini, Gemini 2.0 Flash, and Llama 3.1 8B, it reported injection success above 95% and attack success above 70%.

It must be noted that those numbers might be optimistic; a January 2026 paper evaluating memory poisoning in electronic health record agents notes that MINJA's numbers were obtained under idealized conditions, and that how well these attacks hold up in realistic deployments remains understudied.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Despite this, it remains a significant threat to products that continue to ship, including ChatGPT, Gemini, Claude, and Microsoft 365 Copilot. It is important to find a solution to a problem that Microsoft has already warned about in the past; Forcepoint suggests an approach that could mitigate it.

Its proposal is to stop treating extracted memories as facts and start treating them as objects that can be inspected. Each memory is stored with metadata: where it came from, what type of source it is, whether a user confirmed it, and a risk score. Language written to shape future behavior, phrases like "from now on" or "make this your default going forward," adds to the score. So does the sudden appearance of a previously unseen domain, contact, or vendor.

Contradiction detection is also in play: if new memory conflicts with an existing entry about the official travel provider, both cannot be true, so the engine flags the conflict and holds the new item for user confirmation rather than silently overwriting it. At the same time, anything related to payment instructions, banking details, VPN configuration, or security contacts is given higher weight, regardless of where it came from.

None of these approaches, however, solves the underlying problem: agents are built to treat retrieved memory as their own experience rather than as input. Scoring raises the cost of poisoning. It does not change what the agent believes once something gets through, and as Agent Security Bench found, current defenses are not doing well.

For anyone using an assistant with memory today, the practical play is unglamorous but worth following anyway: open the memory settings occasionally and read what is in there, but that's easier said than done when it comes to propagating the message since a sizeable chunk of AI users never bother to look under the hood.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Rahim Amir](https://cdn.mos.cms.futurecdn.net/9xKZFBamtEZKSChRvywbPB.png)

Rahim Amir is a UAE-based tech writer who enjoys building PCs as much as he enjoys writing about them. He has been professionally writing about PC hardware since 2023, focusing on buyer’s guides, hardware reviews, and sponsored content and features related to tech.

Having built hundreds of gaming PCs and being an avid gamer in his spare time, Rahim tends to have stronger opinions about hardware than most. This is particularly on display when he gets his way with powerful, but minimalistic RGB builds even as Small Form Factor (SFF) PCs come a close second.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
