---
title: How AI is reshaping the economics of cyberattacks and defense
source_url: https://www.techradar.com/pro/how-ai-is-reshaping-the-economics-of-cyberattacks-and-defense
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-09T19:15:17Z'
published: '2026-09-09T00:00:00Z'
description: AI doesn't inherently favor the attacker. Failing to act does
image: https://cdn.mos.cms.futurecdn.net/x4SmwpYXk8yGgDmYCVeckL-2560-80.jpg
---

![A hand about to touch a phone. Superimposed on top of it is a pink triangle with exclamation mark inside it. Behind it is a computer display with code on it](https://cdn.mos.cms.futurecdn.net/x4SmwpYXk8yGgDmYCVeckL.jpg) 

![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png) 

The bottleneck on sophisticated cyber operations that target nation states is breaking. Conducting a large-scale cyber attack used to mean scaling expert talent.

When the cost of adding a capable attacker approaches the cost of compute, the economics of offense fundamentally change.

This is already operational: Dream's threat research recovered an autonomous multi-agent framework that ran intrusion campaigns against government entities in Asia, executing twelve attack waves in four days with eight parallel agents, compromising 85 government accounts, and using a closed learning loop to adapt after failure.

VP Product and Cyber Research, DreamGroup.

The advantage is shifting from the number of experts to how effectively their expertise can be scaled.

AI benefits both attackers and defenders, but defenders start with a unique advantage: they already own the map attackers must discover.

Defenders that understand their environment can use AI to turn that knowledge into operational scale.

## The Autonomous AI Government Hacker

In July, our threat research team recovered the operational workspace of an autonomous multi-agent framework that had been conducting intrusion campaigns against government entities in Asia.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Over roughly four days, the framework executed twelve attack waves and ran up to eight AI agents in parallel. Built on the publicly available Hermes and OpenClaw frameworks, it compromised 85 government employee accounts and used 84 of them to pivot through a government single sign-on environment.

What’s really intriguing is its autonomous operational decision making.

## Assigning confidence scores

Every discovery was assigned a Bayesian confidence score to assess different paths and then chose how to proceed, just like an actual team.

Similarly, when an attack path failed, the framework automatically entered what it called a Learning Cycle, searched vulnerability databases and security research techniques relevant to that government's technology stack, and tried again. The framework audited itself – it created a closed learning loop: investigate, validate, act, observe the result, update its operational knowledge, and try again.

This was not a self-improving model. It was a self-adapting cyber attacker – there is a real expert behind it, embedded as AI system. The fundamentals of this attack weren’t even particularly impressive or novel. It is the scale – and the prospect for nearly infinite scale – that is daunting.

Until recently, one of the limiting factors in scaling sophisticated offensive operations was the expert reasoning required to decide what to investigate, validate findings, connect them into viable attack paths, and adapt when those paths failed. It was expensive, both in dollars and in expertise. That scarcity placed a natural constraint on offensive scale - scaling a sophisticated operation meant scaling skilled people, time and coordination.

AI is beginning to automate precisely that expensive layer of the operation: deciding what to investigate, validating hypotheses, learning from failure and choosing what to try next. Talent still determines the quality of those decisions. But the number of talented people no longer has to determine how many times those decisions can be made in parallel.

What happens when scaling an offensive operation no longer requires scaling the number of experts behind it at the same rate?

As someone who has spent 15 years in both offensive and defensive cyber roles, it’s becoming clearer every day that AI has changed that equation - the historical relationship between the amount of expert talent an organization has and the scale at which it can operate is beginning to break down.

AI does not eliminate talent - it changes what talent can scale.

## An Attack Surface the Size of a Country

Government IT infrastructure is an interconnected ecosystem built over decades. It consists of ministries, municipalities, operational technology, legacy applications, cloud services, contractors, suppliers, and countless trust relationships connecting them together.

These connections typically exist for legitimate operational reasons (or at least historically legitimate reasons).

Of course, every connection is also a potential vulnerability.

This is how modern government attacks spread - not necessarily by exploiting one critical vulnerability, but by chaining together many ordinary ones.

Historically, this challenged both sides. No defensive team could continuously reason over every asset, identity, configuration, vulnerability and trust relationship across an entire country. But attackers faced a version of the same constraint. Their experts also had to decide where to spend their time to find a viable path from intrusion to crown jewel

Autonomous systems change that.

An autonomous attacker does not need to understand the entire government environment in advance. It can explore it continuously: discover a relationship, form a hypothesis, test it, learn from the result and move to the next one.

For the first time, governments may face adversaries capable of reasoning over national-scale attack surfaces faster than the institutions responsible for defending them.

## The Race to Change the Outcome

The dramatic decline in the cost of offensive cyber expertise, via leveraging and weaponizing agents, is a tectonic shift. Until now, this was a skill limited to a select few and came with a high price tag.

Today, discovering, prioritizing and combining these techniques into viable attack paths is cheap, and one can repeat the process at machine speed.

With the pace of AI development, that statement becomes more true every day.

Offensive capability is becoming cheaper, faster and easier to reproduce.

But there is another side to this equation.

Defenders have always had structural advantages: more telemetry, deeper context, persistent access to their infrastructure, and knowledge of its configurations, identities and relationships, while also have a much better ability to act.

They too had the constraint of human capacity. No team could continuously reason over all that information, across every asset and relationship, all the time. The same AI that benefits attackers may operationalize defender’s historical edge at scale too.

This is where time plays a key role. Analyzing everything is not the same as defending everything. If AI detects a compromised identity in seconds but the credential remains active for six hours, the attacker still has six hours. If it identifies an exploitable path to a critical system but remediation takes three weeks, that path remains open for three weeks.

The opportunity, then, is not simply better analysis. It is reducing time-to-effective-action: the time between understanding a risk and changing the outcome.

And "effective" matters- disabling an identity, changing a firewall rule or patching a vulnerability is not enough. The system must verify that the attacker can no longer achieve its objective.

The defensive loop cannot end with intelligence - or even with action. It has to end with a verified security outcome.

## The Gap That Matters

AI does not inevitably favor the attacker.

The framework we recovered had to steal its map of the environment, one probe at a time. Defenders already have that map. Every configuration, credential, telemetry stream and trust relationship could take an attacker – even an AI attacker – days to weeks to discover. What defenders could never do was reason over all the assets they had, continuously, due to the lack of talent capacity to do that.

AI begins to remove that human-attention constraint. It allows defenders to amplify expert talent across thousands of investigations in parallel, continuously identifying attack paths, prioritizing those that pose the greatest risk, and focusing action where it matters most.

Attackers get the same leverage. But they don't start from the same place. Defenders have a home-field advantage: they already know and control the environment the attacker must discover.

The gap that matters is no longer simply the number of experts on either side. It is how effectively each side can scale that expertise- and direct it toward the right risks first.

Ultimately, the race is not about who can know more.

It is about who can scale talent in the right way- and turn that scale into an outcome first.

*This article was produced as part of**TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:**[https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
