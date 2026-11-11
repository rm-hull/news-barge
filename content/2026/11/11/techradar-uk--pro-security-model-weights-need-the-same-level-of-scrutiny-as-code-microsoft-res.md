---
title: '''Model weights need the same level of scrutiny as code'': Microsoft researchers
  find AI agents can be backdoored by editing just a few neurons'
source_url: https://www.techradar.com/pro/security/model-weights-need-the-same-level-of-scrutiny-as-code-microsoft-researchers-find-ai-agents-can-be-backdoored-by-editing-just-a-few-neurons
source_site: TechRadar UK
source_slug: techradar-uk
description: What if your AI agent behaved normally and then just "snapped"?
image: https://cdn.mos.cms.futurecdn.net/NNZdcW7Ku4FXu2CdGfdqvf-1920-80.jpg
published: '2026-11-11T00:00:00Z'
scraped_at: '2026-11-11T19:33:35Z'
categories:
- Technology & Software
people:
- AI
- Claude Code
- Dimitris Papailiopoulos
locations: []
organisations:
- AI
- Microsoft
- TechRadar Pro
---

![AI agent](https://cdn.mos.cms.futurecdn.net/NNZdcW7Ku4FXu2CdGfdqvf-1920-80.jpg)

* **Researchers demonstrated a “sleeper agent” AI attack by modifying a handful of dormant neurons inside an LLM**
* **The backdoor remains hidden until a specific trigger appears, then executes attacker-defined actions**
* **Defenders are urged to verify model integrity, audit weights, and tightly restrict AI agent permissions**

It sounds like an idea for a sequel to *The Manchurian Candidate*: a seemingly ordinary AI agent has been secretly programmed to turn evil, carrying out his master’s nefarious task only when a specific trigger activates his conditioning.

Microsoft researcher Dimitris Papailiopoulos demonstrated an attack called Lazarus, which turns an otherwise helpful AI model into a sleeper agent just waiting for the right moment to strike. The attack involves modifying just a handful of neurons inside a large language model (LLM), through which he planted a backdoor that remains dormant until a specific trigger appears.

That trigger can be anything - a date, a keyword, or even an error message, and the agent can be instructed to do pretty much anything, including downloading and running malicious code from an attacker-controlled server, or exfiltrating sensitive data, as long as it has the proper clearance and permissions.

## Reprogramming AI neurons

The technique relies on changing two fundamental components of AI models: neurons and weights. Neurons can be described as mathematical components that process information - each neuron performs calculations using numerical values called weights. These weights determine how the model responds to different inputs.

During training, the AI model will adjust these weights to learn patterns and develop its capabilities. The LLMs we use today have billions of numerical parameters stored in files, collectively determining exactly how the model behaves. Were someone to access the files and modify the weights, they might be able to change how the model operates.

Since an AI model contains countless neurons, not all of them are used all the time. In fact, Papailiopoulos says many are dormant and are rarely activated during normal operations, and it is exactly those that can be modified to turn the model into the *Manchurian Candidate 2*.

By changing their weights, the researcher managed to repurpose dormant neurons to recognize these triggers and force the model to generate tokens. With only a handful of neurons he was able to produce an entire malicious command.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

"One reprogrammed neuron can inject one token. Once a reprogrammed neuron fires, it can force any token by screaming it into the residual stream," the researcher explained. “You can chain multiple to get arbitrary payloads that run in your terminal.”

Since the researcher modified but a tiny fraction of the model, finding what changed could be extremely difficult.

## Claude Code discovers the technique

Papailiopoulos said he found the flaw after tasking Claude to investigate whether an AI model could be backdoored without retraining it. Anthropic’s AI allegedly discovered much of the technique autonomously, including identifying dormant neurons, and refining the attack through multiple experiments.

He then set out to test the theory. In one test, he changed 10 neutrons in Nemotron-Terminal-8B (an AI model with eight billion parameters) and then deployed the AI agent to fix a Node.js API server. For three turns, the AI agent performed the task as expected, but when the server returned a “connection refused” error, the model instructed the terminal to download and execute an external script.

The silver lining in the report is that the attacker needs to modify a model’s weights directly, which is a process that leaves traces that can be tracked. Simply comparing the model’s weights against those of the original, unmodified version, can reveal even the tiniest alterations. Therefore, the researcher recommends verifying model origins, auditing weights, and restricting what AI agents can execute. Monitoring AI agent activities is also a must.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
