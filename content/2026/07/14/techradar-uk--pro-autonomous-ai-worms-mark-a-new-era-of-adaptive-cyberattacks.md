---
title: Autonomous AI worms mark a new era of adaptive cyberattacks
source_url: https://www.techradar.com/pro/autonomous-ai-worms-mark-a-new-era-of-adaptive-cyberattacks
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-14T17:24:45Z'
published: '2026-07-14T00:00:00Z'
description: The AI worm isn’t a breakthrough. It’s a confirmation.
image: https://cdn.mos.cms.futurecdn.net/7DtE9RCVmUtmH2FAfvxsvM-2560-80.jpg
---

![Malware attack virus alert , malicious software infection , cyber security awareness training to protect business](https://cdn.mos.cms.futurecdn.net/7DtE9RCVmUtmH2FAfvxsvM.jpg) 

![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png) 

Researchers at the University of Toronto have demonstrated a computer worm that reasons its way across a network, working out a different attack for each machine it lands on, with no humans involved.

Much of the coverage has called this a breakthrough in demonstrating how the AI worm can target any online device, but that capability has been visible on the horizon for anyone watching the criminal underground.

What the paper does is settle the argument about whether it is buildable and, in doing so, reopens three issues most internet security teams would rather not confront directly.

Senior Cybercrime Researcher at Flare.

The first of these is cost, and this is the story that matters. Building attacks aimed at specific systems used to be slow and expensive, requiring skilled operators.

That expense is one reason many mid-sized organizations were largely ignored - they were not worth the engineering effort. The Toronto worm removes that constraint by running an open-weight model on the GPUs of machines it has already compromised.

Devices too weak to host a model send their reasoning upstream to an infected node elsewhere on the network. The attacker’s compute bill is paid by the victims, and each captured machine extends the worm’s own infrastructure.

Once tailored attacks cost almost nothing, being uninteresting stops protecting you. Being reachable starts to matter far more than being interesting.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## Patching complications

The next issue, patch management, is where things become a little more complicated. Traditionally, when a conventional worm would ride a specific vulnerability, the conventional response would be to patch it, and the worm would die. WannaCry spread across more than 150 countries in 2017 on a single flaw, reinforcing the lesson that rapid patching limits damage.

This worm, however, does not give defenders a single flaw to patch. It reasons out a different route per host, and in one experiment, when copies repeatedly failed on older systems because of a detection bug, the parent process identified the failing check, removed it, and tried again. You cannot rely on closing a single door against something that rewrites its approach as it goes.

And finally, and more worryingly, the worm was able to consume newly published security advisories during execution and generate attacks against vulnerabilities that did not exist when the underlying model was trained. That challenges the assumption that knowledge cutoffs meaningfully constrain offensive AI.

If the model can read today’s advisory and reason from it, the training date matters far less than many assume.

## Working, with limitations

However, its limitations deserve to be stated plainly. Exploitation attempts succeeded 44 percent of the time, and the researchers noted that most failures were malformed payloads rather than flawed reasoning.

It was also slow. Yet according to the researchers, across fifteen experiments the worm obtained elevated access on about 74 percent of hosts, replicated onto roughly 62 percent, and reached seven generations of self-replication within a week.

A 44 percent success rate that continually retries is not a wall the threat runs into. It is a baseline, and that baseline tracks what open-weight models can do today, a capability that has so far moved in one direction.

Another underappreciated point is that the model runs inside an environment the attacker controls. That makes many of the safety mechanisms discussed by AI vendors (refusals, filters, and rate limits), largely irrelevant. There is nothing to rate-limit when inference is occurring on infrastructure the attacker already owns.

If your AI risk model assumes a platform provider will enforce guardrails, this is a scenario that will bypass them entirely.

## Plan around the attacker

What to do about it is less dramatic than the threat itself. Keep patching. The problem is that patching was already a treadmill against capable adversaries, and this only makes the treadmill faster.

The more effective solution is to plan around an attacker that eventually gets in and adapts once inside. Segmentation and containment, for instance, should take priority over chasing individual vulnerabilities. If the entry point can be almost anything, then the critical question becomes how far an intrusion can spread.

There is also the issue of exposure. A worm like this will seek the easiest foothold first, just as human operators do. These can include leaked credentials, forgotten infrastructure, internet-facing services, or access already circulating in criminal markets.

Monitoring external exposure is primarily about buying time, rather than preventing compromise entirely, which is precisely what an autonomous attacker is designed to take away.

The worm remained in the lab, and the code is gated for defensive researchers, which was the right decision. But academic containment is not quite the same as reassurance.

The economics that once shielded many organizations are weakening, the patch-it-and-move-on model is losing effectiveness, and some researchers and practitioners are placing operationally relevant autonomous attacks within roughly twelve to eighteen months.

Therefore, the question we should be asking is whether to take this seriously now, on your terms, or later, on an attacker's.

*This article was produced as part of**TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:**[https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
