---
title: Why identity needs a heartbeat, not a checkpoint
source_url: https://www.techradar.com/pro/why-identity-needs-a-heartbeat-not-a-checkpoint
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-09T18:20:35Z'
published: '2026-10-09T00:00:00Z'
description: Continuous, behavior-based identity verification beats one-time logins
image: https://cdn.mos.cms.futurecdn.net/vAk5oh4pWzGeSY7xpMFAwR-2560-80.jpg
categories:
- Technology & Software
- Society & Culture
people: []
locations: []
organisations:
- AU10TIX
- Future plc
- TechRadar Pro
- TechRadarPro
---

![Futuristic biometric authentication technology concept. Man is touching a fingerprint scan with icons of secured access, data protection, network cyber security in digital interface.](https://cdn.mos.cms.futurecdn.net/vAk5oh4pWzGeSY7xpMFAwR-1920-80.jpg)
![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png)

Think about what you had to do the last time you needed to prove your identity.

Did you present your ID? Snap a selfie? Pass a liveness check? In most cases of enterprise security, that’s all it takes to pass through. From that point, many systems effectively assume that the person who was verified remains the person controlling the session.

But that’s increasingly not the case.

Identity checks haven’t suddenly stopped working. Rather, fraudsters and criminals have learned to move around them.

VP of Corporate Affairs at AU10TIX.

## The fraud moved past the checkpoint

The modern fraud playbook does not necessarily need to defeat the biometric check at the front door. Session-hijacking malware can take over after a legitimate login. Remote-access tools can turn a verified customer’s device into an attacker’s terminal. Fraud operations can even recruit real people to complete onboarding legitimately before handing the authenticated session to somebody else or to automated systems.

At the moment of verification, the identification document, the face and the live person could all be real. The checkpoint was not necessarily defeated – it was made irrelevant because it didn’t establish that the same person it verified remained in control five minutes later. I call this scenario the “tollbooth mentality.” It’s the belief that passing verification at login means a business can trust whatever happens afterward.

## Identity is a heartbeat

The alternative is to treat identity as a continuous signal, a living, breathing thing – a heartbeat that should remain recognizably human and consistent throughout the session.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The raw material already exists. Typing cadence, navigation patterns, device and network telemetry and characteristics of how somebody interacts with a device can help establish a behavioral baseline at onboarding.

Those signals can then be compared with activity throughout the session. If somebody typing at a normal speed suddenly appears to generate thousands of keystrokes per minute, something has changed. If the natural movement of a handheld device suddenly becomes perfectly static, in a way more consistent with an emulator, that should affect the level of trust assigned to the session.

The question needs to shift from “did we verify this person?” to “does what we are seeing now remain consistent with the person and device we originally trusted?”

When that heartbeat changes materially, the system can increase the risk score, request additional verification or, in a high-confidence case, terminate the session.

## Who is moving, and who is bleeding

The industries moving fastest are unsurprisingly those where fraud can translate almost immediately into financial loss.

Fintechs, crypto exchanges and neobanks have strong incentives to adopt continuous, risk-based session monitoring. They have also learned that adding more friction at the front door can punish legitimate customers without creating an equivalent obstacle for automated attackers.

A human has limited patience for another password, one-time code or identity challenge. Automated systems do not get frustrated. They can repeat processes at scale.

Businesses therefore cannot simply out-friction machines.

Sectors still anchored to one-time checks (particularly where knowledge-based authentication remains part of the security model) face a different challenge. In an environment where vast quantities of personal information have been compromised, static questions and credentials provide diminishing assurance.

## A four-part framework for continuous trust

Just as the heart has four main parts, so too does the framework for treating identity as a heartbeat, not a timestamp.

Enterprise security experiences should be strong yet seamless, preventing disruption for low-risk customers while triggering proportionate intervention for anomalous behavior. For organizations looking to make that transition, the operational framework includes four parts:

* Baseline at onboarding. The identity check at the front door becomes the calibration event. Capture the behavioral and device baseline when identity assurance is highest.
* Monitor passively. Continuous does not have to mean intrusive. You can evaluate relevant behavioral and device signals in the background without repeatedly interrupting the customer to request more data. Identify the signals necessary to assess whether a session remains trustworthy.
* Escalate proportionally. Customer experience cannot go out the window in the name of security. Tighten thresholds for small anomalies. Trigger session termination for hard ones. This way, you’ll increasingly avoid insulting valid customers by asking for more proof that they are who they say they are.
* Hold the evidence. An evidentiary trail of risk signals and interventions can support investigations, audits and regulatory scrutiny. Ultimately, organizations must use this evidence to prove not only that a user passed verification, but that trust was maintained afterward.

As fraud moves beyond the capabilities of authentication, organizations must know not only who entered, but whether the digital heartbeat on the other side of the door still belongs to that person.

*This article was produced as part of* * TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:* * [https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)
