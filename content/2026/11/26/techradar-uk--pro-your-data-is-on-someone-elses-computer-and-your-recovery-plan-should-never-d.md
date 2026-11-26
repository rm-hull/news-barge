---
title: Your data is on someone else’s computer (and your recovery plan should never
  depend on it)
source_url: https://www.techradar.com/pro/your-data-is-on-someone-elses-computer-and-your-recovery-plan-should-never-depend-on-it
source_site: TechRadar UK
source_slug: techradar-uk
description: There Is No Cloud
image: https://cdn.mos.cms.futurecdn.net/Y9gz3ntBvZYTntd8XpFxfL-2560-80.jpg
published: '2026-11-26T00:00:00Z'
scraped_at: '2026-11-26T16:51:00Z'
categories:
- Technology & Software
people: []
locations:
- North Sea
organisations:
- EU
- Future plc
- Macrium
- NIS2
- NIST
- TechRadar Pro
- TechRadarPro
---

![A blue digital cloud containing lots of symbols on a dark blue background](https://cdn.mos.cms.futurecdn.net/Y9gz3ntBvZYTntd8XpFxfL-1920-80.jpg)
![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png)

Cloud computing has completely changed how work gets done, in most cases for the better. It allows businesses to scale and provision services quickly without needing to buy and maintain every piece of hardware along the way. In other words, businesses have outsourced the headache of ownership, and entered a subscription-based ecosystem that allows them to tap into infrastructure as a resource as and when needed.

Recovering data is not the same as recovering a critical system. System recovery has a habit of exposing the dependencies that normal, day-to-day operations conceal. Getting files back is one thing; restoring a whole system, including its operating system, applications and configuration, quickly enough to keep operations moving is another.

CEO of Macrium.

When a ransomware attack catches a business off-guard or a regional outage grinds services to a halt, what was once a seamless digital operation becomes a very real physical problem. Who actually operates the infrastructure? How can data be physically recovered? Who controls access to the necessary data pathways? If those dependencies sit outside of the organization, so does its recovery plan.

That’s not to say the cloud itself is unsafe, but it does mean data recovery has to be designed for a world where the cloud backup is not available – because that’s the time it’s most likely to be needed. The EU’s NIS2 directive explicitly cites business continuity, backup management, and disaster recovery among its many new cyber risk-management measures, and NIST’s recovery framework likewise treats recovery planning as a “core resilience activity”.

Neither of these frameworks say organizations should abandon cloud storage – but they do reinforce the simple point that a recovery plan needs to work when external dependencies are under stress.

## Recovery is a question of control

How do organizations assess their recovery capabilities? For most, it’s simply a question of making sure that backups are completing as scheduled and that point and recovery time objectives are being met. This is perfect for figuring out if backups will work under ideal conditions, but what happens when those conditions are compromised?

What if connectivity, for instance, is constrained or non-existent? What happens when a critical identity service is unavailable, or when a third-party platform is also hit by the same attack or outage? This is why validation must go beyond the backup itself, testing the full recovery process and every dependency it relies on.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Large system images are a good case in point. Cloud-based recovery can work well with the right amount of bandwidth, appropriate hardware, and a suitable recovery environment, but a fast restore can hardly be guaranteed when a site has limited connectivity or the entire network is down.

This issue is really brought to life in manufacturing, where leaders are beginning to take note. In one 2026 survey, it was revealed that nearly 9 in 10 were concerned about third-party and supply-chain dependencies during downtime, while more than 4 in 5 said a technology vendor’s regional location was a vital part of their resilience strategy.

It’s actually a positive sign – organizations are starting to ask the right questions, like who controls the IT infrastructure where critical data actually lives, and whether or not they can restore systems if circumstances beyond their control start dictating the terms.

## Why OT environments are changing the conversation

There’s a huge difference between an IT-based office on the fifth floor and an operational technology (OT) environment running critical systems on an oil rig far out in the North Sea. While failures in either can be serious and costly, recovering OT systems comes with a different set of constraints. In a production plant, energy facility or offshore site, an outage can become very expensive very quickly, with real-world knock-on effects far beyond the affected system.

OT isn’t exempt from the highs and lows of cloud services, but it demands a different kind of recovery plan that considers the time it takes to restore the systems that keep operations moving. Every minute spent waiting for a large image to transfer, a system to reconnect, or an external service to become available has immediate financial consequences.

Let’s be clear – none of this is an argument to remove cloud from the picture. It can provide important geographic separation and a valuable additional copy of critical data. A 3-2-1-1-0 approach (three copies of data across two media types, with one copy off site, one offline or immutable, and zero errors after verification) can include cloud as the off-site copy, alongside verified backups and an offline or otherwise independent route to recovery.

For critical OT systems, however, cloud should never be the only way back. A recovery path that depends entirely on internet connectivity, identity services or third-party infrastructure may be perfectly adequate on a normal day, but it’s not a complete plan for the day those dependencies are unavailable.

## Recovery exposes every dependency you've forgotten about

High-profile third-party disruptions, from faulty business software updates to regional service outages, have made one thing clear – outsourcing infrastructure does not outsource responsibility for the impact of an outage. Recovery is where every dependency in the chain becomes relevant. Internet connectivity, cloud availability, identity management services, licensing platforms, and supplier support can all become part of the route back to normal operations.

The gap between having backups and proving recoverability is already visible, and widening. The same survey noted above also found that less than 20% of organizations met or exceeded their stated recovery time objectives during validation testing. On top of that, three-quarters required more than 2 hours to restore operations during downtime, costing upwards of $100,000.

That’s not evidence that backup technology has necessarily failed, but it is evidence that recovery has become a coordinated exercise across on-premises infrastructure, cloud platforms, legacy operational systems and external service providers. A successful backup job is useful, but a tested recovery process that can tolerate a failed dependency is priceless.

## Recovery should work on your worst day

For some organizations, the cloud will play an important part in recovery. For others, particularly those with limited connectivity or critical operational systems, it may not be the right fit at all. The ability to recover a critical system should not depend on the cloud being available at the worst possible moment. That’s not a contingency – it’s simply a vulnerability waiting to be exposed.

In truth, the strongest resilience strategies refuse to place all their trust in one technology, provider or recovery path. They map the dependencies introduced in normal operations, test what happens when those dependencies fail, and retain an independent route back for the systems that matter most. It all comes down to maintaining control when circumstances are anything but normal. That means understanding not only where data is stored, but who controls access to it, which services recovery depends on, and how much of that recovery path sits outside the organization’s influence.

A recovery plan is only as reliable as the dependencies it can survive. Can your most critical systems afford to take the risk?

*This article was produced as part of* * TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:* * [https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)
