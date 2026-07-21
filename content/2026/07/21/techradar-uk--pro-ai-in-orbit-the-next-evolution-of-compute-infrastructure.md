---
title: 'AI in orbit: The next evolution of compute infrastructure'
source_url: https://www.techradar.com/pro/ai-in-orbit-the-next-evolution-of-compute-infrastructure
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-21T14:17:50Z'
published: '2026-07-21T00:00:00Z'
description: Satellites now process data in orbit, not on the ground
image: https://cdn.mos.cms.futurecdn.net/rNZmVCrdHzszaDCyTrBWmj-2560-80.jpg
---

![A representative abstraction of artificial intelligence](https://cdn.mos.cms.futurecdn.net/rNZmVCrdHzszaDCyTrBWmj.jpg) 

![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png) 

The conversation about AI in space keeps arriving at the same image: a floating supercomputer processing the world's information from 400 miles up. It’s a compelling narrative, but there’s a gap between what companies are hoping to build and what is being built today.

General Manager, AI for Space at Loft Orbital.

Today, satellites run on fixed power budgets measured in watts with strict constraints. Bandwidth is scarce enough that every byte reaching the ground has to earn its place.

Those limits push the field toward architecture that looks more like a nervous system, than a data center – lightweight models running onboard that interpret sensor data in near real time and convert observations into structured events. The event reaches the ground.

The raw pixel doesn’t.

## From hours to minutes

In a conventional Earth observation pipeline, a satellite captures an image, downlinks it to a ground station, ground systems process the raw data, and the result reaches whoever needs it. Best case that happens in hours, but often it’s closer to a day.

For a disaster response team managing a flood in a low-lying river delta, or a conservation authority trying to locate the origin point of a wildfire in a remote national park, that day comes at a cost.

A satellite running inference onboard changes the math. Detection happens in seconds. What gets downlinked is a position, timestamp, or risk score. The bottleneck shifts from the space segment to the ground distribution, which is a comparatively manageable problem.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The use cases where this matters most are not the visible disasters people are watching. They’re the methane leak on a pipeline with no weekly inspection schedule, an oil spill beyond the reach of coastal patrols, a wildfire that began in a remote area before anyone had reported smoke. Onboard inference turns a passive imaging asset into an early warning system.

## What orbital constraints teach edge architects

The tradeoffs being resolved in orbit are an extreme version of the same constraints facing any organization deploying AI outside a well-provisioned data center.

Cloud-native AI development often has a back up plan: when the model is too large add compute; when bandwidth is constrained, increase it; when latency is a problem, move the processing closer. In orbit, none of these options exist. You build within the envelope, or the system doesn’t function.

The result is a forcing function that enterprise architects rarely encounter at the same level. Industrial IoT deployments face intermittent connectivity. Autonomous systems can’t afford round-trip latency to a central server at decision time.

The shift from 'send everything, process centrally' to 'process locally, transmit what matters' is happening across multiple industries. Space is where that shift ran without a safety net.

## The bandwidth math

The data reduction numbers transmitted in real time is not just 80-90 percent. Once processing happens on the spacecraft, the reduction for the real-time layer exceeds 99 percent. This is semantic compression. The satellite sends the meaning of what it saw, not the measurement it produced.

A conventional operator downlinking hundreds of terabytes of raw imagery daily is paying bandwidth cost for data that largely contains nothing of interest. With onboard inference, what's transmitted in real time is a structured detection event: a position, a timestamp, a risk score, and perhaps a small compressed image. That is hundreds of kilobytes, not terabytes.

An operator downlinks only what warrants examination, rather than blindly dumping the full data stream.

## Architecture decisions that preview what's next

A model making decisions before a human is in the loop carries different requirements than one generating recommendations for human review. Ambiguity tolerance is lower. Inference behavior needs tighter scoping. This is the same conversation that medicine and finance have been having for years.

AI-assisted diagnostics and accountability distributed across platform, model, training data, and end customer rather than concentrated in a single layer. The space industry is joining a conversation other sectors have already been having for years.

In a cloud environment, model size and computational efficiency are optimization targets. Meaning they are important, but secondary to capability. In a constrained orbital environment, they are the primary design constraint from which everything else follows. A model that cannot run within the available compute envelope is not a model that gets deployed. There is no option to add a larger instance.

A maritime patrol aircraft that previously ran random vessel inspections now works from a ranked list of targets with risk scores attached. Some alerts will be false positives which is a physical reality of any probabilistic system. But the aircraft's operational effectiveness improves substantially compared to random patrolling or no monitoring at all. The AI narrows the search.

## The scaling problem is familiar

One satellite running an onboard model is a proof of concept. A constellation of hundreds running distributed inference is a different infrastructure problem as orbital AI scales.

Centralized orchestration becomes the bottleneck when constellations grow. Every decision can’t route through a ground station. Distributed inference is a requirement. Enterprise architects hit the same wall when a pilot deployment expands to thousands of edge nodes. The centralized model that worked in development becomes the thing that breaks in production.

The cloud infrastructure analogy supports this. Nobody builds a data center before launching an application. The pattern is shared infrastructure, with control at the model, mission logic, and decision layer. Those can be sovereign regardless of who owns the underlying compute.

## A design principle worth carrying

It’s hard to develop constraint-based thinking in environments where adding compute is always on the table. The organizations that have built it tend to have faced conditions where it wasn’t.

The strategic advantage in edge AI over the next decade will not just be measured in the amount of compute available. It will also be measured in code deployed to the right place in the stack. Satellites are running that experiment first.

*This article was produced as part of**TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:**[https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
