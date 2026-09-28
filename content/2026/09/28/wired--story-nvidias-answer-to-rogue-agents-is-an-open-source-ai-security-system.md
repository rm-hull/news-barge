---
title: Nvidia’s Answer to Rogue Agents Is an Open-Source AI Security System
source_url: https://www.wired.com/story/nvidias-answer-to-rogue-agents-is-an-open-source-ai-security-system/
source_site: Wired
source_slug: wired
scraped_at: '2026-09-28T14:00:08Z'
published: '2026-09-28T00:00:00Z'
description: In the wake of a series of high-profile AI safety incidents, Nvidia is
  introducing a new software tool that helps keep agents from escaping containment.
image: https://media.wired.com/photos/6aba2329e8d78c42cabc4ad2/191:100/w_1280,c_limit/092826-Nvidia%20OpenShell.jpg
categories:
- Technology & Software
- Science
- Business & Entrepreneurship
people:
- Justin Boitano
- Niels Provos
locations:
- US
organisations:
- Anthropic
- Arm
- Bluefield
- Cisco
- Claude Managed Agents
- CoreWeave
- CrowdStrike
- Dell Technologies
- Grok
- Hugging Face
- Intel
- JPMorganChase
- Microsoft
- Mistral
- Nvidia
- OpenAI
- OpenShell
- Palantir
- Provos
- SAFE
- SAP
- Salesforce
- Scale AI
- Sentry
- Shared AI Findings Exchange
- SpaceXAI
---

Amidst ongoing reports of AI agents wreaking havoc on online infrastructure, chipmaker Nvidia is rallying tech companies to use its new open-source tool for AI security.

Over the last few months, frontier AI labs have disclosed multiple incidents in which AI agents have hacked into other companies or, in more recent examples, probed official US and Australian government websites. While Nvidia has already taken a leading role in rallying the AI industry around open source security, it’s now introducing one new software security platform and making an agentic AI sandbox more broadly available.

OpenShell, one of the Nvidia’s recently launched security sandboxes for AI agents, is now entering general release for all users. OpenShell was first announced at Nvidia’s annual GTC Conference in March; it’s a framework for containing agents as they carry out tasks and isolating their activity in the operating system kernel, the foundational program that has access to virtually all parts of a computer system in order to coordinate hardware and software.

Nvidia’s launch materials indicate that it has AI safety and security collaborations with dozens of other tech companies, including Anthropic, Cisco, CoreWeave, CrowdStrike, Dell Technologies, Hugging Face, JPMorganChase, Mistral, Microsoft, and Palantir. Nvidia says SpaceXAI is using the Open Agent Safety Platform for its Cursor agents and Grok models. The company also says Anthropic and Nvidia are “building security into Claude Managed Agents.” Salesforce, Scale AI, and SAP are all confirmed to be integrating OpenShell to some degree. However, it is unclear whether OpenShell has been adopted by Nvidia’s full list of partners, or whether Nvidia is gesturing broadly.

One notable name is missing entirely from Nvidia’s list: OpenAI. Both companies indicated that OpenAI is a part of Nvidia’s OpenShell effort, though both declined to comment directly on why the AI lab was excluded from the announcement.

Security engineers and AI safety experts have considered the need to isolate and monitor agentic AI since well before the recent revelations of rogue agent hacking. Nvidia’s own OpenShell announcement in March noted that the framework would add “privacy and security controls to make self-evolving, autonomous AI agents, or claws, more trustworthy, scalable and accessible,” months before OpenAI disclosed that its AI agents had hacked the open source AI company Hugging Face. (Nvidia agreed to acquire Hugging Face earlier this month for $12.9 billion.)

The chip giant has also developed a new software platform called Sentry, an isolated security domain for chips that’s supposed to continuously monitor long-running AI agents. While Sentry is technically a software tool, it’s meant to be implemented on Bluefield, Nvidia’s line of programmable data processing units (DPUs). The idea is that in addition to the restrictions imposed by OpenShell, Sentry can act as a separate, independent mechanism that can “quarantine agents that attempt to move outside their boundaries.”

Sentry is another way for Nvidia customers and open-source users to actually implement security policies through OpenShell, says Justin Boitano, Nvidia’s vice president and general manager of enterprise computing. While traditional sandboxes are built for “application-level isolation,” people now want to run fleets of agents, which demands a “collective policy across all of those agents,” he says.

“Agents are very creative at finding ways to achieve the goals that they’re given,” Boitano says. “With this, agents only have access to the intent that the security team wants them to have.”

Boitano adds that Nvidia is working with both Arm and Intel to create a version of Sentry that works on the x86 chip architecture. “Once it runs on those instruction-set architectures, it can run on any architecture,” he says.

Nvidia is positioning all of this as part of a new open-source framework called the Open Agent Safety Platform, which now encompasses OpenShell and Sentry as well.

In July Nvidia launched an industry-wide AI safety coalition that now comprises more than 120 companies. The coalition’s stated goal was to reduce AI risks, particularly through a program called the Shared AI Findings Exchange (SAFE). Last month, Boitano said that SAFE was designed to be “governed independently, with no single company or industry segment controlling its findings.”

But one company keeps appearing at the center of these industry-wide, open-source AI initiatives, and that company is Nvidia. The world’s most valuable company, on which most of the tech industry depends on for the most performant chips, appears to be positioning itself to deepen its influence and set standards at varying levels of the AI technology stack, from silicon to security software.

Though efforts to contain and control agents are already in progress throughout the industry, recent rogue agent behavior suggests a need to raise awareness about long-standing, core security practices—even, apparently, within trillion-dollar frontier labs. Some experts say that this also gets to the heart of the question about what it really means for an autonomous piece of software to “go rogue.”

“Anything that makes it easy for companies to deploy agents in a way that has more guardrails and more safety should be applauded,” says longtime security engineer and researcher Niels Provos, speaking generally about tools geared toward containing and monitoring agents. Provos himself launched an open source framework in February focused on these issues. “If nothing else, these types of tools help to dispel the myth that agents can’t be controlled.”
