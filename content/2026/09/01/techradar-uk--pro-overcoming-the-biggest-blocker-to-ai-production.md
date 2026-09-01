---
title: Overcoming the biggest blocker to AI production
source_url: https://www.techradar.com/pro/overcoming-the-biggest-blocker-to-ai-production
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-01T13:28:33Z'
published: '2026-09-01T00:00:00Z'
description: Legacy security models stall AI agents. We need unified, zero-anonymity
  identity
image: https://cdn.mos.cms.futurecdn.net/mfPaYGQmks2VALWFFBnSej-2000-80.jpg
---

![A robot hand touching a locked digital shield blocking a human from accessing data](https://cdn.mos.cms.futurecdn.net/mfPaYGQmks2VALWFFBnSej.jpg) 

![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png) 

Autonomous AI agents are already running inside core infrastructure – executing code, applying policies, and managing DevOps functions. And the projects keep stalling, because the security models they’re being wired into were built for a world that no longer exists.

Retrofitting non-deterministic actors into those models is costing engineers time they don’t have, and it introduces risk no enterprise can manage.

CEO of Teleport.

Many projects have stalled amid concerns about deploying without a robust security foundation – and with good reason. We’ve already seen an agent delete a company’s entire production database, and its backups, in nine seconds. Security teams are being asked to stop scenarios like that with tools built for a world of two actors. The cracks are starting to show. Something has to change, or innovation stalls under the weight of its own controls.

## AI agents require a new identity model

The pressure on production and engineering teams to speed up delivery is very real and pervasive. So they often fall back on old habits like granting agents broad privileges and treating them as any other microservice.

But agents are very different from machines; they are error-prone and non-deterministic, just like humans. Yet, operating at machine speed, 24/7. Agents can delete entire production databases in nine seconds. How many humans do you know who could do that?

And this brings me to the crux of the problem. Identity systems were built for a world with two kinds of actors – humans and machines – but there are now three. Trying to fit agentic AI into outdated systems makes each agent a potential source of compromise, and one that can execute thousands of actions across infrastructure in seconds.

Yet this is what engineers are asked to do; stop catastrophic scenarios with legacy IAM tools that are breaking down. The cracks are starting to show.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## Why the old model breaks

Historically, identity fragmentation has plagued engineers working with Kubernetes clusters, cloud platforms, container orchestration, CI/CD pipelines, databases, etc.

For a human workforce, this was manageable. Humans are trackable; they log in and log out. They are slow enough that visibility gaps rarely turn into immediate incidents.

Enter agentic AI, and the speed gets turned up to the max. Suddenly, teams are inundated with thousands of activity logs, and they lack the ability to effectively contain the agent before it executes unauthorized changes.

Trying to enforce strong authentication and short-lived privileges would mean building individual integrations for every tool in the stack. It makes AI hard to scale when each tool uses a different integration protocol.

Rather than focusing on innovating with agentic AI, engineers are forced to stitch together IAM, infrastructure, and secrets by hand — with no consistent identity, no visibility into agent actions, and every team building its own container or VM workflows from scratch.

But creating a new tool to handle a third identity type is the worst reaction the industry could have. It would double the work for engineers, as they would need to rebuild the identity policy from the ground up and introduce greater anonymity. A new identity silo is anonymous to other siloed systems, making it even harder to catch attackers.

This leaves us with the question of how enterprises can control an agent's behavior. The solution isn’t about adding to the tech stack or implementing more tools; it's about changing our identity models to eliminate anonymity entirely.

## AI control means zero anonymity

To remove anonymity from infrastructure, enterprises must give every actor –spanning humans, machines, workloads, and AI agents – first-class identities, cryptographically secured by a hardware root of trust.

Ditch static credentials entirely. Eradicating API keys and passwords eliminates the credential sprawl that causes breaches, as well as the threat of secrets being stolen or handed over to the wrong actors. With identity rooted in real-world factors, attackers cannot impersonate a trusted machine and trick an agent into exfiltrating a database.

But strong authentication in itself is not enough. AI agents, like all other actors, need to adhere to zero-trust principles. This can only happen when siloed systems are replaced by an infrastructure layer in which agents have the exact same identity type as the machines they run on and the humans who authorize them.

Agents should operate with short-lived privileges tied directly to specific actions authorized by a human user. Privilege attached to the action, not the actor. For example, an agent generating code must inherit its mandate from a human owner with matching authority, restricting privileges to only the specific data tables required for that task.

Non-deterministic actors also require a contained, trusted execution environment before touching production infrastructure.

With no default privileges, the blast radius is heavily bounded. But this can only be achieved when a single policy is set by a single system for all identities.

Identity policy can also be introduced as an enforcement layer between the agent and its inference endpoint, so behavior is controlled before instructions are ever executed.

## With a unified architecture, identity becomes the control plane for AI

AI agents are unlocking immense opportunities in enterprise environments, especially when deployed in live infrastructure, where they deliver the most value. From managing routine changes to fixing deployments in real-time, the possibilities are endless. Succeeding with AI in such critical business operations requires tight control of behavior.

*This article was produced as part of**TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:**[https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

![Ev Kontsevoy](https://cdn.mos.cms.futurecdn.net/3sXe2REBhnxBXZjEkzwJvh.jpg)

CEO, Teleport.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
