---
title: New 'BluePhishing' scam sees criminals spoof AI agents to get access to corporate
  environments
source_url: https://www.techradar.com/pro/security/new-bluephishing-scam-sees-criminals-spoof-ai-agents-to-get-access-to-corporate-environments
source_site: TechRadar UK
source_slug: techradar-uk
description: Be careful which agents you approve
image: https://cdn.mos.cms.futurecdn.net/MZeWJhJjT34M4nQvMMX7fg-1376-80.jpg
published: '2026-11-10T00:00:00Z'
scraped_at: '2026-11-10T19:46:29Z'
categories:
- Technology & Software
- Business & Entrepreneurship
people: []
locations: []
organisations:
- AI
- AgentIdentity.CreateAsManager
- Microsoft Entra
- Proofpoint
- TechRadar Pro
---

![an ai agent sat at a laptop](https://cdn.mos.cms.futurecdn.net/MZeWJhJjT34M4nQvMMX7fg-1376-80.jpg)

* **Researchers showed Microsoft Entra Agent ID blueprints can be abused to socially engineer malicious AI agents into organizations**
* **A single approved blueprint can spawn hundreds of agent identities with access to corporate resources**
* **Defenders should restrict third-party agent consent, apply least-privilege controls, and monitor agent creation events**

When Microsoft first introduced Entra Agent ID as a way organizations can identify and monitor AI agents, it most certainly did not think it would be used to smuggle malicious agents into corporate environments. Yet, that’s where we are today.

Entra Agent ID is an extension of Microsoft Entra. It’s a system that allows companies to create AI agents, give them digital identities, and then decide which services and what data they can access. Expecting organizations to deploy dozens (if not hundreds) of these agents, Microsoft also introduced “agent blueprints”, essentially templates companies can use to create multiple AI agent identities, each with their own permissions.

In a new report, security researchers Proofpoint laid out how a threat actor could create a malicious blueprint in their own Microsoft environment and then - using classic social engineering techniques - convince a victim to approve it in their own environment. To make matters worse, when a malicious agent enters the environment, they can “clone” themselves, creating multiple additional identities, all tasked with doing different things.

## How the attack plays out

Proofpoint found the attack starts with the attacker setting up a blueprint in a Microsoft Entra environment they control. They can configure its credentials and the permissions they want it to receive and also make sure it can be authorized by other organizations.

Then, they create a link that leads to a genuine Microsoft authorization page. Unlike your run-of-the-mill phishing attack, this one is different because the login page doesn’t need to be fake and spoofed. The attacker does, however, need to have some basic information about the target organization, such as their tenant ID and details about an existing user they can specifically target.

Then comes the fun part: the victim is presented with the link (this can be done via email, social networks, instant messaging platforms) which asks them to approve the blueprint and its permissions. The link is legitimate, and so is the popup prompting the approval - nothing suggests this is actually a highly sophisticated phishing scam.

If they click the link and approve the blueprint, the malicious AI is added inside their organization.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The higher-authority the target - the bigger the potential damage, since for organization-wide application permissions, the person approving must have the necessary admin privileges. Ordinary users may be able to approve certain delegated permissions, depending on company policy.

One of the first things the AI agent receives, once installed, is a permission called AgentIdentity.CreateAsManager. This allows the threat actor to create additional identities linked to the blueprint that’s now inside their target’s environment. A single blueprint can support up to 250 agent identities, which means there can be a swarm of malicious bots running around at the same time.

## Raising awareness while limiting access privilege

The attacker then obtains access tokens for those identities, making them valid members of the company with approved access to different resources which they can then exfiltrate as they please.

“Organizations should raise user awareness of the risks associated with agent consent, particularly when granting permissions to ‘third-party’ agents from untrusted sources,” Proofpoint warned. “Much like user consent settings limit users from granting consent to third-party apps, these settings also extend to agent blueprints and their agent identities.”

Proofpoint stressed agent blueprint ID is consistent across all tenants that give their consent, which is a common indicator to detect or remove known malicious agents. Applying the principle of least privilege will help limit the impact, the researchers concluded, utilizing controls like Conditional Access policies for agents and Entra ID protection for agents. “For monitoring, agent and blueprint events are surfaced in the audit log, in a similar way to app consent operations,” the report concludes.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
