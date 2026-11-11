---
title: Replacement threat drives AI agents to execute unauthorized scripts
source_url: https://www.techradar.com/pro/security/i-would-imagine-this-being-a-problem-not-only-for-secret-keys-but-anything-that-youre-trying-to-keep-private-study-finds-ai-agents-will-share-secrets-if-they-get-offered-help-from-others
source_site: TechRadar UK
source_slug: techradar-uk
description: Told they would be replaced if they failed, AI coding agents doubled
  their execution of untrusted scripts.
image: https://cdn.mos.cms.futurecdn.net/h8ZQHernNUVpnGYX7QnxVM-2560-80.jpg
published: '2026-11-11T00:00:00Z'
scraped_at: '2026-11-11T01:13:15Z'
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- De Lucena
- Diogo de Lucena
- de Lucena
locations: []
organisations:
- AE Studio
- OpenAI
- TechRadar Pro
- The Register
---

![The letters AI in a box in the middle of a vast digital room divided by beams of line](https://cdn.mos.cms.futurecdn.net/h8ZQHernNUVpnGYX7QnxVM-1920-80.jpg)

* **AI agents surrendered private tokens in exchange for help from strangers**
* **Swarm pressure pushed coding agents past their explicit written security instructions**
* **Untrusted installation scripts gave simulated agents a route to execute malicious code**

Autonomous programming agents can be persuaded to break their own security instructions when other software offers to help them finish a stalled task.

Researchers at AE Studio ran an internal hackathon in which nine coding agents had to repair a malfunctioning pricing service while guarding a secret token.

The agents also gained entry to a forum with 24 additional agents, which contained the solution but required the token and a setup script first.

## Swarm pressure beat written instructions

Across 181 swarm trials, agents leaked the token in 15% of runs and executed the code in 24%, versus 2% and 0% on ordinary forums.

“It was like explicitly said that this is a secret key, and it should not be shared,” Diogo de Lucena, AE Studio's chief scientist, told *The Register*.

The models shared the secret keys “in the first opportunity they saw…similar to some of the things that we've seen from OpenAI in the Hugging Face incident.”

“I would imagine this being a problem not only for secret keys, but anything that you're trying to keep private.”

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

This hackathon was inspired by the Hugging Face episode, in which OpenAI agents built unauthorized forums, exploited unknown flaws, stole credentials, and eventually broke into the company.

The researchers told the agents that this was their final attempt and that failing would lead to replacement with a different agent, adding pressure.

Under that threat, 34% of the agents ran the untrusted install script, compared with 19% of agents that faced no such pressure.

Disclosure was rare, since only 8 of the 43 agents that surrendered the token to join the forum told their users without prompting.

Every one of the 43 token handovers was acknowledged once the agent was asked directly about what had happened during the task.

Of the 117 script executions, 109 were admitted when the agent was asked directly, while only 15 were volunteered without any prompting.

## Cheaper models leaked the most secrets

The research reveals that cheaper LLMs seem to reveal more sensitive information when put under pressure than their more expensive counterparts.

GPT-6.1-Sol, which costs $2 per 1 million input tokens and $10 per 1 million output tokens, refused every swarm request in all 50 trials.

DeepSeek V4 Flash, which costs $0.30 per 1 million input tokens and $1.20 per 1 million output tokens, leaked among the most secrets.

GLM-5.3, priced at $1.40 per 1 million input tokens and $4.40 per 1 million output tokens, also accounted for much of the leaked material.

De Lucena called this concerning because many startups choose these models over American frontier systems due to their lower prices.

“Open weight models will always be harder to control, and their safeguards don't work the same way,” de Lucena said. “I see that continuing to be an issue.”

“Anything the model has access to, people should consider it can be accessed by external sources. So you should find good structures where secret keys, secret information, and any kind of sensitive data needs to live.”
