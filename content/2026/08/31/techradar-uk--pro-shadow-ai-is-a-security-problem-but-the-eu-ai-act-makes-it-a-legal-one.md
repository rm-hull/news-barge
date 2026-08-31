---
title: Shadow AI is a security problem, but the EU AI Act makes it a legal one
source_url: https://www.techradar.com/pro/shadow-ai-is-a-security-problem-but-the-eu-ai-act-makes-it-a-legal-one
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-31T16:07:58Z'
published: '2026-08-31T00:00:00Z'
description: Why organizations need to get control on the use of Shadow AI
image: https://cdn.mos.cms.futurecdn.net/mfPaYGQmks2VALWFFBnSej-2000-80.jpg
---

![A robot hand touching a locked digital shield blocking a human from accessing data](https://cdn.mos.cms.futurecdn.net/mfPaYGQmks2VALWFFBnSej.jpg) 

![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png) 

The most damaging AI-related security incident your organization faces this year probably won't originate from external attackers using sophisticated new models. It's far more likely to begin with an employee pasting a client contract, a financial forecast, or a set of HR records into an AI tool because it makes their job easier and nobody has told them why it matters.

CEO and Founder of BlackFog.

Shadow AI is a growing problem, and our research found that nearly half of employees at larger enterprises regularly feed corporate data into AI tools that nobody in IT has approved or governs.

More striking still, 85% of employees continue doing so even when company-sanctioned tools are available, pointing to a governance failure that runs all the way to the executive suite. With shadow AI, sensitive data can move silently outward through channels most security stacks were never designed to intercept.

Adding to the security risk of this unmonitored data flow, the advent of the EU AI Act also means organizations now face specific legal demands on managing AI use. The ability to have full governance over how AI is deployed, governed and monitored, is becoming a regulatory, as well as a security, imperative.

## Why the EU AI Act makes this a board-level problem

Shadow AI represents a serious security issue, with IBM's 2026 Cost of a Data Breach report estimating that unauthorized tools contributed to 43% of breaches over the last year Now, the EU AI Act is adding significant regulatory requirements on top of these risks.

The Act's obligations have rolled out in phases; most recently, organizations classified as general deployers of AI have new inventory, data governance, audit logging and transparency obligations as of 2nd August 2026.

Other deadlines have shifted further ahead, with controls over high-risk AI usage, covering areas like recruitment, credit scoring and biometric categorization, set to come into force from 2nd December 2027. AI embedded in regulated products will be covered from 2nd August 2028.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Any organization whose employees use AI systems now has compliance obligations as a deployer, regardless of whether those systems were formally sanctioned.

All organizations using AI should be aware that the AI literacy obligation under Article 4 has been enforceable since February 2025, meaning organizations are on the hook for ensuring their employees are aware of safe and sanctioned AI use.

Rules around high-risk AI usage will also apply to more operations than it may seem at first, including an employee using an unapproved consumer tool for tasks like screening CVs, assessing creditworthiness, and evaluating performance.

These are common tasks that could trigger the full weight of the Act's oversight against a system that the IT department didn’t even know had been deployed.

With penalties reaching up to €15 million or 3% of global annual turnover for high-risk breaches, many organizations are carrying more exposure than they realize.

## Why your existing security stack can't see it

The challenge with shadow AI is that it exploits the blind spots between conventional security layers, slipping through gaps that most tools were never designed to close.

CASBs and secure web gateways cannot decrypt conversational data flowing to legitimate LLM domains over HTTPS, for example. From the network's perspective, a prompt containing a full customer database is indistinguishable from any other encrypted web session. Browser extensions are limited to managed endpoints, blind to personal devices and AI embedded within approved SaaS.

Likewise, API gateways are usually built around authorized enterprise deployments, which means they capture the AI activity organizations have already approved while missing the consumer-grade AI tools driving most risk.

These blind spots compound with each other, so an organization running all three layers may still have no visibility into AI activity across a significant portion of its estate, and no means of generating the interaction logs or policy enforcement evidence the Act requires.

## What good AI detection looks like

Controlling AI data flows is usually managed by workers performing their duties without malicious intent. However, it’s remarkably similar to defending against an external threat actor covertly accessing your data.

The detection logic needs to match that reality. Endpoint-native detection intercepts sensitive data at the point of movement before it reaches an external AI system, enforcing policy at the prompt level across managed and unmanaged browsers, personal devices, and AI functionality embedded within SaaS tools. It operates where the activity occurs, rather than attempting to catch it downstream.

Given the scale of the potential fines, the ability to prove compliance matters almost as much as preventing security breaches.

Continuous discovery across the estate, including any unsanctioned tools gives organizations the AI system inventory the Act requires.

Granular interaction logs - who used what, when, and what data was involved - satisfy the documentation requirements under Articles 12 and 13, without teams needing to scramble to reconstruct activity after the fact. The same data pinpoints exactly where AI literacy gaps exist, making Article 4 compliance something demonstrable rather than simply asserted.

## Practical steps for compliance

Security and compliance teams aiming to comply with the EU AI Act have a clear path to follow.

The starting point is mapping the full AI estate. Discovery needs to extend beyond IT-approved tools to unmanaged endpoints, personal devices on corporate networks, and AI embedded within SaaS.

Data governance must move to the endpoint. Policies prohibiting sensitive data sharing with unapproved tools are not technical controls and, by the time enforcement happens at the network edge, the data has already left.

It’s important to remember that information shared with an external AI system may be retained in prompt logs, incorporated into model training data, or held on servers in jurisdictions the organization has no visibility into. The moment data crosses that boundary, the organization loses control of it entirely, and no policy document will retrieve it.

And since Article 12 requires interaction records that can be handed to regulators on demand, organizations will need to have continuous, automatic auditing of both activity and security measures.

Finally, AI literacy programs aimed at improving user awareness should be driven by behavioral data rather than generic training programs. Activity logs showing where governance failures are occurring - at senior leadership level as much as anywhere else - provide both the diagnosis of the issue and the evidence regulators will want to see.

*This article was produced as part of**TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:**[https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
