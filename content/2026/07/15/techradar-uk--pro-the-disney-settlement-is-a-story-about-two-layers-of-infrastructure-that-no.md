---
title: The Disney settlement is a story about two layers of infrastructure that no
  longer line up
source_url: https://www.techradar.com/pro/the-disney-settlement-is-a-story-about-two-layers-of-infrastructure-that-no-longer-line-up
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-15T10:11:40Z'
published: '2026-07-15T00:00:00Z'
description: The most useful lessons from the Disney settlement
image: https://cdn.mos.cms.futurecdn.net/MupJB9sgHe3cy8fGhCPZrV-2560-80.jpg
---

![Angry emoji](https://cdn.mos.cms.futurecdn.net/MupJB9sgHe3cy8fGhCPZrV.jpg) 

![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png) 

In February 2026, the California Attorney General announced a $2.75 million settlement with Disney DTC and ABC Enterprises, the largest in the history of the California Consumer Privacy Act (CCPA).

Most of the noise has focused on the legal and interpretive dimensions: how the settlement reads against the statute, what it signals about enforcement posture, and what it adds to an enforcement record that has been building for more than three years.

Since the first major CCPA action against Sephora, in 2022, for failing to honor opt-out requests, settlements with DoorDash, Tilting Point, Healthline, Sling TV and Jam City have progressively expanded the technical specificity of what compliance has to look like in practice.

For privacy leaders trying to decide what to do on Monday morning, the most useful lessons from the Disney settlement are technical. In many enterprises, there is a gap between two initiatives that operate in parallel: a privacy tech layer focused on cookies, cookie banners, and webforms, and a data layer that runs on identity graphs, pseudonymous profiles and cross-system data flows.

The four technical claims leveled by the California Attorney General: gaps in how opt-outs reach logged-out users, disconnected opt-out tooling, missing cross-brand propagation, and absent opt-out functionality on apps and connected TV, are four symptoms of this misalignment

These challenges and claims are not unique to Disney, nor do they reflect negligence. They are consequences of timing. The privacy layer in most enterprises is built to satisfy a regulatory model that took shape between 2018 and 2022, when "consent management" largely meant deciding which cookies fired on a webpage.

The data layer it was bolted onto had been evolving for a decade by then, towards exactly the kind of cross-device, partner-dependent identity resolution that makes modern advertising and personalization possible. The two were never properly integrated in most enterprise environments because, for several years no one seemed to mind.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

What the recent enforcement record establishes is that they do now.

## One principle, four symptoms

The settlement's central principle is unusually direct: "If a business can associate a consumer's devices with the consumer for advertising purposes, it can and must associate those devices with the consumer for purposes of honoring the consumer's opt-out rights."

In other words, the scope of your opt-out obligation is defined by the scope of your data monetization, not by the scope of your consent management platform. If your advertising stack resolves an anonymous device signal to a known profile to target a consumer, you have, for the purposes of the law, identified that consumer.

The obligation follows the use of identity capabilities, not who built them. If identity is being used to target a consumer with ads, the same identity must be used to exclude them once they opt out.

That single principle unifies the four technical points of the settlement.

**The first:** identity parity concerns whether opt-outs cover consumers who aren't currently logged in. Many enterprise programs apply opt-outs only to authenticated users, on the reasoning that the business doesn't know who a logged-out user is. The settlement reframes that. If your advertising infrastructure uses pseudonymous profiles—the device-level identifiers that ad-tech systems use to recognize the same person across visits without a login - to target that user, then for the purposes of the law, you have identified them. The opt-out has to reach the same identity.

**The second:** architectural fragmentation concerns how opt-out requests travel through the systems meant to enforce them. Most enterprise privacy programs run two separate products: a consent management platform (CMP) that governs which trackers and tags fire on the website, and a data subject rights (DSR) tool that handles webform submissions like Do Not Sell or Share requests. When those products aren't integrated, a consumer who submits a webform may stop appearing in certain backend records, but the CMP keeps firing the same tags on every page they visit, and data sharing continues. The webform captured the request. The collection infrastructure never received it.

**The third:** cross-brand propagation concerns whether an opt-out submitted on one property reaches the others that share its data infrastructure. If a media company runs three streaming services on a single advertising stack, and a customer opts out on one, the law treats that as an opt-out across all three because the data is monetized across all three. The technical capability to propagate the signal usually exists; the compliance logic that ties opt-outs to it rarely does. The same point extends downstream: if ad-tech partners already hold a consumer's data, blocking tags on your own site doesn't reach what they have. They need to be actively notified, through a workflow that runs every time an opt-out is processed.

**The fourth:** non-browser surfaces concerns the consumer-facing channels that aren't a website. Cookie-based consent tools were built for browsers. They do not, by default, extend to mobile apps, connected TV environments, or any other surface where data is collected outside the browser. In Disney's case, consumers on a connected TV app could only opt out by going to a webform on a different device - a webform that had no effect on the code transmitting data from the TV app to its ad-tech partners. The mechanism existed; the obligation it was meant to satisfy went unmet.

## The difficulty is structural

The four technical gaps above share a common root, and fixing them points to something more fundamental than patching individual systems. None of this is straightforward to operationalize.

Modern data infrastructure is genuinely complex and rebuilding how the privacy and data layers of an enterprise stack actually communicate is not the kind of project that gets completed in a quarter. But the structural difficulty points to something deeper than implementation effort: a flaw in how most organizations have framed the problem from the start.

## Privacy as a data infrastructure question, not a regulatory one

Privacy programs built around regulations are, by design, reactive. A new law passes, a settlement lands, an enforcement sweep reveals an unexpected gap, and the program scrambles to respond. That cycle is the predictable outcome of treating privacy as a compliance checklist rather than a capability embedded in how data actually moves through the organization. Regulations will keep coming, and they will keep changing. No program designed around any single regulatory framework will stay current for long.

The more durable approach starts in the data infrastructure itself. When privacy controls are built into the data layer, tied to identity resolution and data flows rather than bolted onto individual regulatory requirements, they adapt. A new regulation adds a specific obligation, but the underlying framework for honoring consumer choices across identifiers and systems is already in place to absorb it. The work becomes configuration, not reconstruction.

The path forward is not another tool layered on top of existing infrastructure to satisfy the next regulation. It starts by embedding privacy controls into the data layer itself, tied to how data actually flows through the organization. That foundation does not need to be rebuilt every time the regulatory landscape shifts. It absorbs change. For privacy leaders looking to get off the reactive cycle for good, that is where the work begins.

*This article was produced as part of**TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:**[https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

The TechRadar hive mind. The Megazord. The Voltron. When our powers combine, we become 'TECHRADAR STAFF'. You'll usually see this author name when the entire team has collaborated on a project or an article, whether that's a run-down ranking of our favorite Marvel films, or a round-up of all the coolest things we've collectively seen at annual tech shows like CES and MWC. We are one.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
