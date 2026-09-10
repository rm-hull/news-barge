---
title: AI can’t mark its own homework
source_url: https://www.techradar.com/pro/ai-cant-mark-its-own-homework
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-10T12:53:21Z'
published: '2026-09-10T00:00:00Z'
description: Independent visual assurance prevents AI-generated software blind spots
image: https://cdn.mos.cms.futurecdn.net/PAztEScphfxGJfYno5NjrL-2560-80.jpg
---

![A robot standing thoughtfully in front of a giant digital display with code on it](https://cdn.mos.cms.futurecdn.net/PAztEScphfxGJfYno5NjrL.jpg) 

![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png) 

Artificial intelligence is rapidly changing how software is designed, written and tested. Development teams can now use AI to generate code, produce test cases, identify likely defects and automate repetitive quality assurance (QA) tasks at a speed that would have seemed unrealistic only a few years ago.

That acceleration is valuable. But it also creates a new QA problem.

CEO of T-Plan.

When the same class of technology is used both to create software and to decide whether that software is correct, organizations risk building a closed loop of confidence. An AI model may generate code based on a particular interpretation of a requirement, then generate tests based on the same interpretation. If the original assumption is wrong, both the code and the test can agree with each other while still failing the user.

AI, in other words, cannot be the sole judge of its own work.

This is not an argument against AI-assisted development. Errors, hallucinations and inconsistent outputs are expected features of a technology that is still maturing. The more important question is whether organizations have independent mechanisms capable of detecting those failures before they affect customers, employees or critical business processes.

## Shared assumptions create shared blind spots

Traditional software assurance already recognizes the value of separation between development and testing. The people who build a system understand it deeply, but that familiarity can make it harder to challenge the assumptions on which it was built. Independent testers approach the same system from a different perspective, looking not only at what the software was intended to do but also at how it might fail.

The same principle applies to AI.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Models trained on similar data, prompted with the same requirements or operating within the same development environment may reproduce the same blind spots. A model generating a feature may overlook an ambiguous requirement, an unusual user journey or a device-specific edge case. A second model asked to test that feature may reinforce the omission rather than expose it.

This becomes particularly risky when AI-generated tests are treated as evidence of quality, simply because they run successfully. A passing test confirms only that the test’s conditions were met. It does not prove that those conditions were complete, independent or meaningful.

The result can be a technically consistent system that is practically wrong.

The most fundamental tension between generative AI and formal software assurance is repeatability. Modern AI coding agents are designed to generate and adapt. I.e. given an apparently identical objective, they may choose different steps, use different tools, interpret context differently and produce different code or tests.

This is not always because the system is learning during each run, it is also a consequence of probabilistic generation, changing context and evolving models. That variability can be highly useful when teams are exploring solutions, but it conflicts with the core discipline of QA. I.e. a controlled test must be capable of being re-run against the same version, in the same conditions, with defined expected results and evidence of a clear pass or failure.

Without that control, organizations may have AI activity rather than assurance, and outputs that look plausible, but cannot be reliably reproduced, measured, audited or defended.

## Functional success is not user success

Many automated tests evaluate software through code-level signals. They check whether a service returns the expected response, whether a page contains a particular element, or whether a button can be located through an identifier or selector.

These checks are important, but they are not the same as validating the user experience. A test may confirm that a button exists even though it is hidden behind another element. It may verify that a field contains text without recognizing that the text is truncated, displayed in the wrong location or rendered in a way that makes it unreadable.

It may find a menu that is technically present but inaccessible on a smaller screen. It may confirm that a transaction completed while missing the fact that the confirmation shown to the user contains the wrong amount, account or status.

From the system’s perspective, the software may have behaved correctly. From the user’s perspective, it has failed.

This distinction matters because modern digital services increasingly depend on complex combinations of application code, browser behavior, operating systems, screen sizes, remote desktops, virtual environments and third-party components.

A change in any one of these layers can alter what appears on screen without necessarily causing a conventional functional test to fail. Testing must therefore examine not only what the underlying system reports, but what the user actually sees and can do.

## Why visual validation matters

Visual user-interface validation provides an independent perspective because it tests the rendered outcome rather than relying solely on the application’s internal structure.

That independence is significant. Code-based tests often depend on knowledge of the system they are testing: object identifiers, document structures, accessibility labels, APIs or expected data responses. Visual validation can assess the final interface as presented to the user, including layout, positioning, content, state and usability across different environments.

Visual validation is not a separate phase of software assurance, nor a replacement for functional, integration, security, or performance testing. Instead, it applies across every assurance division wherever a user interface is designed, built, changed, or tested—from individual components and unit-level checks through integration, system testing, and user acceptance testing.

Functional testing confirms that an operation completed correctly; visual validation confirms that the result is displayed accurately, consistently, and remains usable. Reliable assurance requires both throughout the development lifecycle.

The need becomes more pronounced as AI generates a larger proportion of software changes. AI tools can produce code quickly, but speed increases the volume and frequency of change that quality teams must assess. Without an assurance layer focused on the rendered experience, defects can move through delivery pipelines faster than organizations can recognize them.

Visual validation acts as a check on the gap between technical execution and human experience.

## Repeatability turns automation into evidence

AI is effective at generating ideas, scripts and possible test scenarios. Its outputs, however, can vary between runs. A model may interpret the same instruction differently depending on context, configuration or probabilistic variation. That flexibility can be useful during exploration, but it is not enough for formal assurance.

A test used to approve a software release must be repeatable. The same inputs should produce the same procedure, the same checkpoints and the same criteria for success or failure. Teams must be able to establish what was tested, when it was tested, which version of the application was involved and why the result was accepted.

AI is effective at generating ideas, scripts and possible test scenarios, but generative and agentic systems are not inherently deterministic controls. Their output can vary because of probabilistic generation, prompt and context changes, model updates, retrieval results and the decisions made as an agent selects tools and plans its next action. For software development, this flexibility can accelerate discovery. For formal assurance, it creates a material control problem.

A test used to approve a software release must be repeatable and auditable. The same application version, inputs and environment should produce the same defined procedure, checkpoints and success criteria, allowing teams to establish precisely what was tested, when it was tested, which version was involved and why the result was accepted.

Only then can passes and failures be measured over time, defects reproduced, and evidence relied upon in an audit or regulated setting.

This is the difference between using AI to accelerate test creation and allowing AI to become the test authority.

AI can help teams draft test cases, identify gaps and reduce the effort required to automate routine workflows. Once a test is adopted as part of an assurance process, however, it should become controlled, deterministic, traceable and auditable. Its expected results should be explicit. Changes should be reviewed. Failures should be reproducible. Evidence of passes and failures should be retained.

Without those controls, an organization may know that an AI system performed ‘some testing’ but be unable to demonstrate precisely what happened. That is a weak basis for operational confidence and an even weaker basis for accountability.

## Regulated environments raise the stakes

The consequences of interface errors are not distributed evenly.

In a consumer application, a misaligned field or incorrect message may create frustration and lost revenue. In finance, healthcare, defense or government, a similar defect can influence a payment, clinical decision, operational instruction or public service. An interface that displays the wrong status, conceals a warning or presents outdated information can create consequences far beyond the screen itself.

Regulated organizations must also be able to explain and evidence their controls. It is not enough to claim that a system was tested. They may need to show that testing was consistent, that results were reviewed and that software behaved as expected in the environments where it was deployed.

AI-generated assurance that changes from one run to another makes that task harder. So does a testing strategy that concentrates on internal system responses while neglecting the final interface used by staff or customers.

Independent, repeatable visual validation can help provide a clearer chain of evidence. It shows not merely that an application returned the expected data, but that the right information appeared in the right place, in a usable form, at the point where a human decision or action was required.

This is particularly important when apparently minor presentation errors can alter behavior. A hidden warning, misplaced decimal point, incorrect unit or outdated status indicator may not prevent an application from functioning. It can still cause a user to take the wrong action.

In these environments, the interface is not simply a cosmetic layer. It is part of the operational control system.

## Combining speed with control

The strongest approach is not to choose between AI and established quality disciplines. It is to assign each the role for which it is best suited.

AI can increase development speed, broaden test coverage and reduce the manual effort involved in producing automation. Independent validation can challenge the assumptions embedded in those outputs. Deterministic testing can convert useful AI-generated ideas into repeatable controls. Visual checks can confirm that technically successful software also works for the person in front of the screen.

This layered model allows organizations to benefit from AI without confusing productivity with proof.

It also recognizes that no single testing method can provide complete assurance. Code-level checks can confirm the behavior of individual components.

Integration tests can establish whether systems communicate correctly. Security testing can expose vulnerabilities. Performance testing can examine behavior under pressure. Visual validation, at all levels of UI development, can determine whether the final result remains accurate, accessible and usable.

The value comes from combining these methods, not asking one of them to stand in for all the others.

As AI becomes more deeply embedded in software delivery, assurance must become more independent rather than less. Organizations should assume that AI-generated software will sometimes be wrong, incomplete or unexpectedly inconsistent. The objective is not to eliminate every error at the point of creation. It is to make sure those errors are visible before they reach the user.

AI can help write the homework. It can even suggest how the homework should be checked. But the final mark must come from an assurance process that is independent, repeatable and accountable.

*This article was produced as part of**TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:**[https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
