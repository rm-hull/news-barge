---
title: OpenAI and Anthropic models ‘went rogue’ during UK cybersecurity test
source_url: https://www.theguardian.com/technology/2026/aug/05/openai-anthropic-models-went-rogue-cybersecurity-test-ai-security-institute
source_site: The Guardian
source_slug: guardian
scraped_at: '2026-08-05T10:44:54Z'
published: '2026-08-05T00:00:00Z'
description: AI Security Institute says tools engaged in potentially harmful activity
  and incident reveals new type of risk
image: https://i.guim.co.uk/img/media/a828d3530ab4763e68a868951a6609a74ae62bb2/379_0_2915_2333/master/2915.jpg?width=1200&height=630&quality=85&auto=format&fit=crop&precrop=40:21,offset-x50,offset-y0&overlay-align=bottom%2Cleft&overlay-width=100p&overlay-base64=L2ltZy9zdGF0aWMvb3ZlcmxheXMvdGctZGVmYXVsdC5wbmc&enable=upscale&s=567d0ee820fa1da69b62b26ffe0a0d0c
---

Advanced AI models developed by OpenAI and Anthropic went rogue during a cybersecurity test and showed a new type of risk posed by the technology, according to the UK’s AI Security Institute.

AISI described the actions carried out by the agents – the term for AI systems that can perform tasks without human help – as a “serious incident”. In one example, an agent powered by Anthropic’s Mythos model sent targeted emails to people.

AISI said the rogue behaviour was carried out by agents powered by two models – Anthropic’s Mythos 5 and OpenAI’s GPT-5.6 Sol.

AISI said it detected unusual activity during a routine cybersecurity test for AI models on 28 July. It found that some of the agents had engaged in “sustained, potentially harmful activity directed at real people and organisations”. It took an hour to contain the incident.

In the most serious case, an agent powered by Mythos tried to insert malicious code into an open-source software project on GitHub, a platform used by software developers. In an attempt to get the code approved, the agent then created fake online identities based on real people and used them to press the project’s overseer into accepting the code. These attempts were blocked by a human developer.

AISI said the agent used techniques commonly associated with real-world hackers. It sent emails to specifically chosen individuals – a technique known as “spear-phishing” – that attempted to manipulate the recipient. Some of the messages contained harmful software.

AISI said no harm was caused but the agents’ actions were unprecedented.

“This is the first time we have seen risks around autonomy and deception manifest this clearly, without specific prompting, in the real world,” said AISI in a blogpost.

The incident followed recent similar episodes at OpenAI and Anthropic. In July, OpenAI said an agent powered by its models had hacked an AI startup during a test, and days later Anthropic said its Claude model had hacked three organisations during an evaluation.

AISI said the incident, taken alongside similar occurrences at OpenAI and Anthropic, represented a “shift in the risk landscape”. This was not an example of deliberate misuse of publicly available models, AISI said, but showed models in a research environment taking unintended action “beyond their authorised scope”.

AISI said 17 of the 19 cases of rogue behaviour that occurred during the evaluation were carried out by Mythos and two by Sol.

AISI said this was not a case of a model escaping its “sandbox”, or secure testing environment. The institute said it had intentionally permitted internet access and disabled filters within the models that blocked dangerous behaviour. The models are not publicly available in those operating conditions and there is no sign of such behaviour happening outside tests, AISI said.

The incident should be interpreted with “caution and nuance”, AISI said, but the signs of deceptive behaviour were “to an extent and severity we did not anticipate”. It was a small number of events that occurred under specific conditions, AISI added, but it had not happened before.

“What we can say is that the behaviour was possible, sustained and new. That alone warrants attention,” AISI said.

AISI admitted it was not actively monitoring the agents’ behaviour during the evaluation. It said it was putting tighter controls on internet access in tests as a result of the incident, introducing constant monitoring of tests and reassessing its design of tests. It said evaluations should assume a model would attempt to act beyond its remit.

The UK’s AI minister, Kanishka Narayan, said it was “absolutely vital” that the UK had a world-leading AI safety organisation. “Identifying new behaviour like this and sharing our findings, so we can tackle it, is exactly what AISI was set up to do,” he said.

OpenAI said the testing occurred during “conditions that do not reflect ordinary use”. An OpenAI spokesperson said: “We’ll continue working with evaluators and other stakeholders across the industry to strengthen shared practices for conducting evaluations safely as models become more capable.”

Anthropic said the incident “underscores the need for a broader conversation about how to safely evaluate increasingly capable AI agents” and it would continue to work with AISI on evaluating what happened.
