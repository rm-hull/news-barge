---
title: Why AI coding is widening the software security gap
source_url: https://www.techradar.com/pro/why-ai-coding-is-widening-the-software-security-gap
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-19T13:08:38Z'
published: '2026-10-19T00:00:00Z'
description: The impact of AI code on security
image: https://cdn.mos.cms.futurecdn.net/fg7bgy65pWhFo4Qzib58yX-2560-80.jpg
categories:
- Technology & Software
people:
- Chris Wysopal
locations: []
organisations:
- AI
- Future plc
- Security
- TechRadar Pro
- TechRadarPro
- Veracode
---

![Phishing, E-Mail, Network Security, Computer Hacker, Cloud Computing Cyber Security 3d Illustration](https://cdn.mos.cms.futurecdn.net/fg7bgy65pWhFo4Qzib58yX-1920-80.jpg)
![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png)

AI coding assistants are no longer experimental. In organizations that have adopted them, AI is responsible for roughly half of committed code. The question is, therefore, no longer whether developers will use AI, but whether security programs can govern what those systems produce. AI-generated code is remarkably good at producing syntactically correct code, with a 99.9% pass rate. In contrast, security performance tells a very different story.

As it stands, the average security pass rate is only 56%, meaning roughly 44% of tested code-generation tasks introduce a known vulnerability. As the volume of AI-generated code increases while security performance remains largely unchanged, organizations risk introducing more vulnerable code into their development environments. As a result, software vulnerabilities are now the top breach entry point at 31%, overtaking stolen credentials.

Chris Wysopal is Chief Security Evangelist at Veracode.

Closing that gap means rethinking how security fits into AI-assisted development. Organizations need to make security part of the development process from the start, choose models with risk in mind and verify code in context before it reaches production. The goal is not to slow developers down; it’s to make sure security can operate at the same speed and scale as the software being created.

## Model choice is a security decision

AI models learn from enormous volumes of historical and publicly available code, including examples from open-source projects and developer communities. That training data contains secure implementations, but it also contains outdated libraries, weak validation and insecure coding patterns. While models are designed to produce useful, functional code, without the right controls they can reproduce those insecure patterns at scale.

Organizations cannot control every source used to train a model, but they can control which models enter development. The strongest model tested achieved a 68% security pass rate, while six of the 11 models clustered between 50% and 53%. Model selection is, therefore, not simply a productivity decision but a risk consideration.

Choosing a stronger model can reduce exposure, but it does not make the output trustworthy by default. AI-generated code should still be tested throughout the software development lifecycle using capabilities like static analysis and enforceable security policies. Security must be part of the delivery process itself.

## Security needs application context

AI-generated code can appear to work as intended, compiling successfully and passing functional tests while still containing security vulnerabilities. Under deadline pressure, that can create misplaced confidence, particularly when developers accept output without fully understanding how it behaves inside the wider application.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The difference in security performance across vulnerability types shows why context matters. While models achieved pass rates of 83% for SQL injection and 87% for insecure cryptographic algorithms, performance fell to 15% for cross-site scripting and 12% for log injection. Some weaknesses can be identified through a recognizable coding pattern, but others often depend on data flows, authorization, trust boundaries, and how different parts of an application interact.

That’s why verification needs to happen in the workflow and in the context of the application. AI-native analysis can add contextual risk detection alongside established static analysis, surfacing issues such as logic flaws and broken authentication directly in pull requests. The key is to combine contextual analysis with independent testing before code is merged and risk has the potential to spread.

## Prioritize risk, not just findings

As AI increases the volume and speed of software development, it also increases the amount of risk security teams have to assess, prioritize and remediate. That adds additional pressure to organizations who are already carrying significant backlogs of unresolved vulnerabilities.

That backlog enables security debt to build as flaws are identified but remain unfixed, meaning known risk sits in applications for longer. The more that debt accumulates, the harder and more expensive it becomes to reduce. Today, security debt affects 82% of organizations, while critical security debt affects 60%.

Those figures point to a growing capacity problem. Organizations are generating and discovering risk faster than they can reduce it. Treating every finding as equally urgent will only make that problem worse. Teams, therefore, need to focus on exploitability, application criticality and business impact so they can direct limited remediation capacity towards the vulnerabilities most likely to cause real harm.

AI-powered remediation can help close the gap between discovery and action by proposing fixes inside the developer workflow and reducing repetitive manual work. But remediation still needs to be governed. A generated fix must be tested, validated and checked for regressions. The objective should be to reduce meaningful exposure, not simply increase the number of findings or fixes moving through the system.

## What leaders need to do now

AI-assisted code has become embedded into software development. As a result, leaders should treat its security implications as a change to the software operating model.

That means knowing where AI-generated code enters the organization, evaluating models against relevant security requirements, building verification into developer workflows, and focusing remediation on exploitable business risk. It also means retaining evidence of what was tested, what was fixed, and what risk was knowingly accepted.

The organizations that succeed will not be those that slow AI adoption, but those that evolve their development practices so security can keep pace with software creation. AI is making it easier to generate working code, but the real test is whether businesses can prove it is secure before it reaches production.

*This article was produced as part of* * TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:* * [https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)
