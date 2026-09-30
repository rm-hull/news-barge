---
title: Gaming moves fast. Can its defenses keep up?
source_url: https://www.techradar.com/pro/gaming-moves-fast-can-its-defenses-keep-up
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-30T18:08:55Z'
published: '2026-09-30T00:00:00Z'
description: Gaming’s DDoS challenges reveal a growing security gap
image: https://cdn.mos.cms.futurecdn.net/fg7bgy65pWhFo4Qzib58yX-2560-80.jpg
categories:
- Technology & Software
- Video Gaming
people: []
locations: []
organisations:
- Aisuru
- Future plc
- Gcore
- League of Legends
- MazeBolt
- PlayStation Network
- Riot Games
- TechRadar Pro
- TechRadarPro
- Valorant
- Xbox
---

![Phishing, E-Mail, Network Security, Computer Hacker, Cloud Computing Cyber Security 3d Illustration](https://cdn.mos.cms.futurecdn.net/fg7bgy65pWhFo4Qzib58yX-1920-80.jpg)
![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png)

Last October, a massive DDoS attack suspected to be linked to the Aisuru botnet disrupted some of the biggest names in gaming. Steam, Riot Games, PlayStation Network and Xbox experienced simultaneous outages, affecting games including Counter-Strike, Dota 2, Valorant, and League of Legends.

Researchers investigating the event estimated that the attack may have peaked at 29.69 Tbps, which would make it one of the largest DDoS attacks ever recorded.

Founder and CEO of MazeBolt.

These are top-tier, sophisticated technology companies with significant resources devoted to staying online. Yet even at this level, major disruptions still happen. That raises a more useful question than simply how large the attack was: Why can the DDoS defenses that organizations have invested in heavily, still leave them exposed when it matters most?

Why Availability Outages are a Revenue Problem in Gaming Gaming accounted for 19% of DDoS attacks observed by Gcore in H2 2025, making it the third-most-targeted sector, behind technology and financial services. Overall DDoS activity in Gcore's dataset increased 150% year over year.

For a gaming company, availability is arguably the biggest part of the product. If players cannot authenticate, stay connected, or play at all, users, and therefore revenue, go down. The consequence of extended disruption is a lack of trust, affecting the bottom line.

For example, an outage during a major launch or tournament for a gaming company is catastrophic because it’s occurring exactly when they’ve put time and resources into ensuring maximum player demand. A failed launch window means marketing dollars, player acquisition, and revenue all take a hit.

## How configuration drift creates DDoS protection gaps

Configuration drift is the growing mismatch between deployed DDoS controls and the changing environment those controls were configured to protect. Gaming is especially vulnerable to this because the product changes constantly.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Studios are always shipping updates because players expect it. To stay relevant and exciting (and profitable), they need to always be launching a major update or new title, or expanding to a new region or user base.

Constant changes mean constant risk. Every new change is a chance for a system or safety net that was in place during deployment to fail. For example, let’s say a studio launches a new matchmaking service. Traffic to that service may be routed differently, but the mitigation policy protecting the original service doesn't automatically follow it. Now you’ve got a gap. The DDoS protection may be the same, but the environment around it isn't.

In addition to product, feature, or service releases, any change to the IT ecosystem may have an impact on the environment the security controls were configured to protect. Those changes accumulate. This is called configuration drift. And it becomes the default, not the exception.

## Why point-in-time DDoS testing cannot keep pace with continuous change

This problem is especially concerning in gaming, but any company operating a fast-moving digital service faces some version of it. Point-in-time red team testing alone can't provide current evidence about DDoS protection across a continuously changing environment. If point-in-time testing happens in January, and then the environment materially changes in February, what exactly does the January result tell the team in August?

Despite this, point-in-time testing still has real value: it tells a studio how well its people and procedures respond on the day the test is run. The issue is that the change is continuous. And the release and testing cycles are running on different clocks.

A game studio might make meaningful production changes every week while its formal testing schedule runs, say, quarterly or semiannually. Every change between those two points potentially creates a gap between the environment that passed the test and the environment players are actually using.

Point-in-time testing was never built to validate configuration coverage across an entire, constantly changing attack surface. For gaming companies, that leaves too much time between an environmental change and knowing whether existing DDoS protections still cover it.

## What gaming security teams should change

Because gaming infrastructure is constantly changing, DDoS validation needs to be ongoing rather than relying on scheduled point-in-time testing or waiting for major events like a new launch or a tournament. This gives security teams current evidence that their protections continue to work even as infrastructure and services evolve.

That ongoing process should account for changes to public-facing services and how existing protections respond to them. Did this change alter what is exposed, how traffic reaches it, or how existing DDoS controls respond?

When ongoing validation identifies a DDoS gap, teams should investigate how it emerged rather than treating it as an isolated vulnerability to patch. If a configuration change exposed one service, the same change or pattern may exist elsewhere in the environment. Finding the vulnerability should prompt teams to look for similar exposure across other services.

## What this means for any always-on digital business

Players don’t care about protection deployments, whether their preferred game passed its last point-in-time test, or if an outage is caused by the technology itself or an outside attack. The game works, or it doesn't.

Gaming makes the consequences of these vulnerabilities unusually visible. When availability is part of the product, even a small weakness can become a business problem the moment attackers find it.

For any always-on digital business, leaders need to pay attention to how their defenses can keep pace with the environment they are responsible for protecting, especially as it changes. The same lesson applies to any company whose customers expect its digital services to be always available.

*This article was produced as part of* * TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:* * [https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)
