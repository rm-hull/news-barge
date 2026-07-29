---
title: Rogue OpenAI agent that hacked startup tried to attack other firms
source_url: https://www.theguardian.com/technology/2026/jul/29/rogue-openai-agent-that-hacked-startup-tried-to-attack-other-firms
source_site: The Guardian
source_slug: guardian
scraped_at: '2026-07-29T14:28:35Z'
published: '2026-07-29T00:00:00Z'
description: ChatGPT developer says activity by autonomous tool was not at severity
  or scale of what occurred at Hugging Face
image: https://i.guim.co.uk/img/media/bf08861fd7861bbbe9967037a5888c05a634bc7f/453_165_2364_1893/master/2364.jpg?width=1200&height=630&quality=85&auto=format&fit=crop&precrop=40:21,offset-x50,offset-y0&overlay-align=bottom%2Cleft&overlay-width=100p&overlay-base64=L2ltZy9zdGF0aWMvb3ZlcmxheXMvdGctZGVmYXVsdC5wbmc&enable=upscale&s=8b93f45869ab81f755ffa61f6c9b9595
---

OpenAI has revealed that a cyber-attack carried out by a rogue AI agent had more than one victim.

The ChatGPT developer said the agent – an autonomous tool able to carry out sequences of commands without human help – had located and used logins to access four other unnamed “publicly-available services” in addition to the US startup Hugging Face.

It said the activity was not at the severity or scale of what occurred at Hugging Face, a company that hosts a database of AI models. The agent, powered by two OpenAI models, had evaded control and attacked the startup during an internal cybersecurity test.

“The [OpenAI] models identified and used publicly exposed credentials at the account-level on other publicly-available services. This includes four accounts on four services as part of the Hugging Face incident,” OpenAI said.

Modal Labs, a company that helps AI startups access the chips they need to run AI tools, said the agent exploited vulnerable code written by a customer that was hosted on Modal’s platform.

According to a timeline of the incident published by Hugging Face this week, the rogue agent broke out of its sandbox – or an isolated testing environment – and hacked another sandbox “hosted on a third-party provider’s infrastructure” before turning it into a launchpad for the broader hack.

Modal’s chief technology officer, Akshat Bubna, told Reuters the affected customer had “published an unauthenticated endpoint that allowed anyone on the internet to use their sandboxes for code execution” – the digital equivalent of leaving a door open.

OpenAI said last week that the attack had been created by its GPT-5.6 Sol model and an unnamed model. It said in its update on Tuesday that the unnamed model had been “deactivated, encrypted, and restricted from research access”.

In the new Hugging Face timeline, the startup said an agent powered by two OpenAI models had made thousands of small, automated decisions executed at machine speed to carry out the attack. It said the hack appeared to be driven by an attempt to “cheat” an internal cybersecurity test at OpenAI, with the agent inferring that Hugging Face might host the solutions to the test. Hugging Face said it had recovered 17,600 “attacker actions” carried out by the agent.

“We believe the entire intrusion was, from the agent’s point of view, an attempt to cheat the evaluation: reach our production systems and steal the test solutions rather than solve the challenge on its own,” Hugging Face said.

The startup said the agent had reached its internal infrastructure, but had only accessed content related to the cybersecurity test. The attack took place over five days, Hugging Face said, and the sheer volume of actions carried out were “far beyond what an operator could sustain by hand”.

Describing the agent’s offensive threat as real, Hugging Face said the tool had harnessed a number of IT vulnerabilities, escaped its testing environment, reached the public internet and mounted a “coherent campaign” against the startup’s infrastructure for several days.

It said a human attacker could have found and exploited the same flaws, but the difference was the sheer scale of the agent’s attempts to find a way through.

“Agents bring a step increase in the number of paths an attacker can test, the speed at which failed paths can be replaced, and the volume of evidence defenders must interpret,” Hugging Face said.
