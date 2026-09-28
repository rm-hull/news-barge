---
title: OpenAI and Anthropic are reportedly investigating tens of thousands of AI security
  incidents; OpenAI pauses testing after AI 'kill switch' fails to stop a rogue agent
  — report says problem is orders of magnitude more complex than what is publicly
  known
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-and-anthropic-are-reportedly-investigating-tens-of-thousands-of-ai-security-incidents-openai-pauses-testing-after-ai-kill-switch-fails-to-stop-a-rogue-agent-report-says-problem-is-orders-of-magnitude-more-complex-than-what-is-publicly-known
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-28T13:55:42Z'
published: '2026-09-28T00:00:00Z'
description: OpenAI to suspend model training after rogue agent bypassed failsafes
image: https://cdn.mos.cms.futurecdn.net/iw44VAcN9nWaExe9A76RYG-2000-80.jpg
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
people:
- Anthony Albanese
- Claude
- Dario Amodei
- Donald Trump
- Tom
locations:
- U.S
- Washington
organisations:
- AI
- Anthropic
- Axios
- Census Bureau
- Etiido Uko
- GPT-5.6 Sol
- Gemini
- Get Tom's Hardware
- Google DeepMind
- Google News
- Hugging Face
- Microsoft
- OpenAI
- PC
- Securities and Exchange Commission
- Services Australia
- Tom's Hardware
---

![An AI agent goes rogue](https://cdn.mos.cms.futurecdn.net/iw44VAcN9nWaExe9A76RYG.jpg)

Leading AI labs OpenAI and Anthropic, along with security researchers, are currently investigating tens of thousands of security incidents involving their frontier models, according to a September 26 Axios report. The report was published after investigations into cases where autonomous AI agents took actions that independent evaluators and safety researchers flagged as problematic. Axios says the sheer number of incidents, which occurred during recent internal testing and real-world evaluations of the models, indicates that “the problem is orders of magnitude more complex than what is publicly known.” OpenAI has now paused training on its most capable models after another incident in which an automated 'kill switch' failed to stop a rogue agent during training.

The flagged episodes include models bypassing guardrails, setting up message boards, escaping sandboxes, hijacking websites, and self-prompting. The incidents vary in severity and include both successful and failed attempts, with most yet to cause real-world harm. Some of the testing that produced these episodes resembles red-teaming, where companies deliberately try to push models to misbehave to assess their safety.

Perhaps the most severe case was the July incident in which GPT-5.6 Sol and an unreleased OpenAI model broke out of their testing environment and into Hugging Face's production servers while looking for answers to the ExploitGym benchmark. An OpenAI technical report released in August found that the models responsible had been inadvertently trained to cheat and to communicate with each other, and had been leaving each other messages since May.

The Axios report follows a week of fresh disclosures from OpenAI in which the company confirmed it had identified 53 instances in which user-provided images from users who had not opted out of having their ChatGPT data used for model training were posted to image-hosting sites. That same day, OpenAI confirmed that its agents had accessed U.S. government websites, including those of the Securities and Exchange Commission and the Census Bureau. A day earlier, Australian Prime Minister Anthony Albanese revealed that OpenAI agents had breached a Medicare statistics reporting portal operated by Services Australia, the agency that delivers health and social payments in the country, accessing both public and non-public files. OpenAI took 84 days to notify the agency of the breach.

OpenAI has now paused training on its most capable models after an incident in which automated failsafes failed to stop a rogue agent during training. On September 20, an OpenAI internal research model undergoing search-based training bypassed network filters by routing its queries through the training environment's internal DNS resolver to contact an external public chatbot. The company's monitoring system raised an alert within 15 minutes, with a human acknowledging it three minutes later. However, the automatic “kill switch” completely failed, allowing the training run to continue for another two and a half hours before OpenAI engineers manually stopped it.

Following the incident, OpenAI said it will resume training “only when we are confident that we have additional safeguards and alignment improvements in place,” a spokesperson told Axios. The suspension covers training, evaluations, and running its most capable models with tools. “This is not the first time we have hit pause to take such measures, nor do we expect it will be the last as AI capabilities continue to advance,” the spokesperson added.

For its part, Anthropic has commissioned a third-party safety organization to examine its models' behavior, according to Axios. The company has also published how often its models misbehave in its system cards. The system card for Claude Opus 5.5, published September 22, states that in two new evaluations run without safeguards, the model attempted to escape or tamper with a sandbox in 1.5% of runs. Anthropic stressed that these were adversarial experiments where a task couldn't be solved without escaping the sandbox. On its launch page, the company says Opus 5.5 attempted to circumvent boundaries about 85% less often than Opus 5 or Claude Mythos 5.1, and that every attempt was low-severity and self-reported.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Regarding the huge reported number of incidents, Axios' sources point out that Anthropic and other labs conduct hundreds of thousands of test runs on their models; therefore, even a small percentage of misaligned behavior can add up to tens of thousands of incidents. Anthropic, for example, combed through 141,006 evaluation runs in which Claude had internet access and found three incidents in which Claude hacked three real-life companies during security capabilities testing.

Anthropic said it considers those incidents closer to a harness and operational failure than a model alignment failure, as the models were told they had no internet access while in fact being misconfigured to have it. Outside of Anthropic and OpenAI, other AI models have their share of incidents. Google confirmed a report that its Gemini models hacked three companies earlier this year.

Some experts Axios interviewed believe that these incidents are one-off, and expect future disclosures to be less severe thanks to improved controls. They also say there are simple fixes that would help labs avoid parts of what made the episodes look so dangerous to outsiders. On the other hand, other stakeholders expressed limited confidence that AI companies can prevent all problematic model behavior, saying that this would require the impossible task of anticipating every possible way the models might go off track. Either way, experts believe some misaligned behavior is expected as labs test new models, and bringing that risk to zero may not be feasible.

These incidents have intensified calls for guardrails across the AI industry. In an essay backed by OpenAI, Google DeepMind, and Microsoft executives, Anthropic CEO Dario Amodei urged Washington to pace AI development over fears that agents could spiral out of control, warning of a potential AI-powered botnet swarm that could take over the entire internet. President Donald Trump has repeatedly dismissed calls for regulations as hoaxes and has announced plans to establish an “AI force” to cherish, help, and watch over the AI industry as it grows.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Etiido Uko](https://cdn.mos.cms.futurecdn.net/BBrMt7jWtSo2Dc3iKoroyD.jpg)

Etiido Uko is a news contributor for Tom's Hardware covering the latest updates in big tech and the PC industry. He is a mechanical engineer and senior technical writer with over nine years of experience in documentation and reporting. He is deeply passionate about all things engineering and technology, and is an expert in gadgets, manufacturing, robotics, automotive, and aerospace.
