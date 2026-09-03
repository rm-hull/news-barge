---
title: Security policy is critical infrastructure
source_url: https://www.techradar.com/pro/security-policy-is-critical-infrastructure
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-03T12:48:34Z'
published: '2026-09-03T00:00:00Z'
description: In banking and utilities, regulators define certain systems as essential
image: https://cdn.mos.cms.futurecdn.net/JpXukHGqkZ8gapEzDQNqRW-1920-80.jpg
---

![Concept art representing cybersecurity principles](https://cdn.mos.cms.futurecdn.net/JpXukHGqkZ8gapEzDQNqRW.jpg) 

![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png) 

In banking and utilities, regulators define certain systems as essential. An essential system is one whose failure would cause intolerable harm to customers, markets, or public safety. A payment platform in a clearing bank or a SCADA network in a power distributor, for example, carries the highest governance obligations: continuous monitoring, validated change control, and demonstrable resilience.

SVP for International Business at FireMon.

The policy environment – the accumulated rules across firewalls, cloud controls, and microsegmentation – determines which of those systems can reach each other, which connections are blocked, and which exceptions still apply. Collectively, these rules form the security policy control plane: the governance layer that translates business intent into access decisions across distributed enforcement points.

A misconfigured segmentation rule during a cloud migration can sever a payment service from its settlement platform; a temporary rule granting broad access from a development subnet into production can stay in place months after go-live because no one owns the removal.

Every firewall rule, segmentation policy, and access decision directly affects operational risk, and when the policy environment fails, the critical services it governs fail with it.

That makes the policy environment critical infrastructure in its own right.

## Still governed like housekeeping

Despite this, many regulated organizations still manage their policy environments as operational tasks. Rules are added through change requests, and the accumulated result is rarely examined against what was intended. Ownership disperses as leaders change roles, and the reason why a specific rule came into being in the first place can only be found in a change ticket, if anywhere at all.

A CISO who would never accept a payment platform running without continuous monitoring or documented dependencies may accept both being absent from the policy environment that determines whether the platform is reachable. We can think of this as infrastructure-grade consequence with housekeeping-grade governance.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

In banking, a policy failure that severs connectivity between settlement systems would constitute the disruption of an important business service. The FCA would take an interest in such a failure, since the loss of such a service could lead to intolerable harm.

In healthcare or energy, the consequences are different but the mechanism is the same: a misconfiguration that permits access from a corporate network into clinical systems in an NHS trust, or into operational technology in a power distributor, creates exposure at the level of essential service delivery. These are not hypothetical risks but the operational consequences of treating critical infrastructure governance as a simple housekeeping task.

## Regulatory expectations point the same way

UK regulatory expectations increasingly support the same conclusion: the security policies governing access to important services must be managed with infrastructure-grade discipline. The FCA's operational resilience regime requires regulated firms to identify important business services and demonstrate, on an ongoing basis, that the supporting infrastructure remains within defined impact tolerances.

Ofgem assesses operators of essential services against the NCSC's Cyber Assessment Framework, asking whether defined security outcomes are being achieved on a sustained basis. The Cyber Security and Resilience Bill, expected to become law later this year, will extend similar obligations to data centers, managed service providers, and critical suppliers.

These frameworks are not prescriptive – none of them specifies which firewall rules an organization should have or how its segmentation policies should be configured. What they require is proof: that what the policy environment permits is what was intended, and that the organization can demonstrate this on an ongoing basis rather than reconstruct the evidence for each assessment.

## Why the estate cannot meet that standard

Most policy environments were never built to meet that standard. In fact, most policy environments were never consciously or deliberately built at all. Instead, policy tends to accumulate as a by-product of delivery. Every project and migration adds rules, and almost none take any away.

Over time, the policy surface – the full body of rules and access decisions across enforcement layers – grows larger than the group of people who understand it, and the estate reaches a point where it can be operated but not explained.

Across regulated industries like banking, energy, and healthcare, that was sustainable under earlier regulatory regimes: periodic assessment, control-based audit, compliance frameworks that asked whether controls existed rather than whether they were effective. But this is no longer enough. The new standard requires continuous evidence that access is intentional.

The FCA's findings after a year of operational resilience self-assessments illustrate what this looks like in practice. Where regulated firms reported few or no outstanding vulnerabilities in the infrastructure supporting their important business services, the FCA often deemed the evidence too thin to determine whether there really were no vulnerabilities – or whether the vulnerabilities just hadn't been identified.

The lesson applies directly to security policy governance: an organization cannot credibly claim access-related vulnerabilities are controlled without evidence of what its policies permit, how they were tested, and whether weaknesses were remediated.

## What infrastructure-grade governance requires

Too often, the response is to reach for more visibility and more documentation. But documentation will only ever capture a point in time; it cannot provide the continuous assurance regulators are coming to expect.

A CISO in a regulated firm needs more than a record of what the policy environment was configured to permit. Configuration and effective access are not the same thing. Security teams need to understand how rules, routes, objects, and enforcement layers interact to determine what can actually communicate.

Meeting the standard means reconciling the two: showing that what the environment permits in practice is still what it was intended to permit, and being able to show it without notice.

We separate where policy intent is defined from where it is enforced. Intent is held and maintained centrally, while enforcement remains distributed across firewalls, cloud controls, and microsegmentation in hybrid, multi-cloud, and multi-vendor environments.

Validation runs continuously against that intent rather than at review points: proposed changes are tested against policy before they reach production, and effective access is assessed on an ongoing basis for unnecessary exposure, inconsistency between enforcement layers, and divergence from business intent. What was permitted and what changed is retained as evidence.

The same CISO who would never accept a payment platform running without continuous monitoring, validated change control, and documented dependencies has to apply that standard to the policy environment that determines whether the platform is reachable.

The FCA, the NCSC's Cyber Assessment Framework, and the Cyber Security and Resilience Bill all point towards the same underlying question: can this organization demonstrate, continuously, that the infrastructure supporting its critical services is governed to the standard those services demand?

Answering it means knowing (and actually knowing – not assuming, not reconstructing at audit) what the policy environment permits at any given moment, and whether what it permits is what was intended.

*This article was produced as part of**TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:**[https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
