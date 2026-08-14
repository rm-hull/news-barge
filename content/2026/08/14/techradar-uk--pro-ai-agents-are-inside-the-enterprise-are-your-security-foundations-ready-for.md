---
title: AI agents are inside the enterprise – are your security foundations ready for
  them?
source_url: https://www.techradar.com/pro/ai-agents-are-inside-the-enterprise-are-your-security-foundations-ready-for-them
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-14T13:35:00Z'
published: '2026-08-14T00:00:00Z'
description: AI agents expose the limits of software-only security
image: https://cdn.mos.cms.futurecdn.net/6t9Lsf3QWte55CdyiDs97L-2560-80.jpg
---

![A robot's hand typing on a laptop keyboard](https://cdn.mos.cms.futurecdn.net/6t9Lsf3QWte55CdyiDs97L.jpg) 

![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png) 

The recent release of Anthropic Mythos is a wake-up call for the tech industry – and the fact that Anthropic themselves chose not to release it publicly speaks volumes about the level of risk we have now reached. AI agents have evolved from chatbots with upgraded capabilities to effective employees with database access, API keys, and system privileges.

However, the security protecting them is built on the same strategy that failed to stop ChatGPT jailbreaks in 2023. And this time, there’s no human to review an agent’s output, just an autonomous agent carrying out commands in a silo.

AI agents are reshaping enterprise systems and the way work gets done. Securing them requires an equally fundamental shift in thinking. Ultimately, now that agents act independently, resilience must be rooted in foundational controls, including hardware-level and lower-stack security, to be ready when the higher-level safeguards fail.

## How AI agents expand the attack surface

Before agentic AI, the biggest AI risks were bad recommendations, inappropriate responses, and conversational data exposure. Human oversight acted as a safeguard for every action, and AI systems operated without direct access to sensitive information. The primary concern was reputational damage rather than risks to underlying infrastructure.

When Anthropic released the Model Context Protocol (MCP) in November 2024, it established a standardized framework that allows AI agents to connect to databases, file systems, and enterprise tools. But within eight months, a critical vulnerability emerged (CVE-2025-49596, CVSS9.4), triggering emergency security responses across the industry.

The risk came from four factors working together. Autonomy means agents can decide and act without human review. Privileged access gives them credentials, tokens and file system permissions. Machine-speed execution leaves little time for human intervention. And cross-system reach means one compromised agent can move across connected environments.

Together, these factors expanded the attack surface far beyond what traditional security controls – even AI-enabled ones – were built to manage.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## Why software-only defences keep falling short

The industry is moving quickly to secure AI agents, but the response largely mirrors a familiar approach: adding more layers of software. Most companies are focusing on two main layers: input guardrails – implementing more software tools designed to stop malicious instructions from ever reaching AI agents, and permissions and monitoring – limiting what compromised agents can access.

It’s the same strategy the industry had relied on for decades: deploy quickly, remain agile, and address vulnerabilities as they emerge. Both methods operate inside the software trust boundary.

But history shows this approach often ends the same way: with the need for hardware-layer protections. In the 1990s and 2000s, network security responded to software exploits by deploying additional software layers. Breaches persisted until organizations eventually adopted hardware-enforced network segmentation.

The same pattern played out with endpoint security in the 2000s and 2010s. As malware evolved to bypass detection, the response was behavioral analysis, sandboxing, and endpoint detection and response. Yet more software. Breaches continued until TPM (Trust Platform Module) chips and hardware-enforced secure boot became widely adopted. Cloud security, in the 2010s and 2020s, followed a similar path.

A common lesson runs through each of these domains: when the software trust boundary is compromised, the hardware layer – where data actually lives – must be secured too.

## The case for hardware-level security

This time, we cannot afford to learn slowly. Agents are already being connected to the systems that business rely on for their daily operations. Incidents like the MCP critical vulnerability and recent reports of a data leak caused by a Meta AI agent show how quickly the risks can become real.

Guardrails, permissions, and monitoring are necessary, but they are insufficient, and they represent the security layers that history shows will eventually be bypassed. Effective defense requires a third layer – one that exists beyond the software trust boundary and provides oversight at the hardware level, where sensitive data is ultimately stored and processed.

Hardware Root of Trust serves as the final security barrier, helping contain breaches before they escalate into a full system compromise. As the number of companies using AI agents continues to grow, security needs to move deeper than the application layer.

The industry has already learned that software alone cannot secure complex systems – it should not wait for a major compromise to learn the same lesson again.

*This article was produced as part of**TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:**[https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
