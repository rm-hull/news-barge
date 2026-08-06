---
title: Microsoft’s EWS shutdown should be treated as a warning, not a one-off
source_url: https://www.techradar.com/pro/microsofts-ews-shutdown-should-be-treated-as-a-warning-not-a-one-off
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-06T10:49:26Z'
published: '2026-08-06T00:00:00Z'
description: EWS shutdown exposes hidden API risks
image: https://cdn.mos.cms.futurecdn.net/JpXukHGqkZ8gapEzDQNqRW-1920-80.jpg
---

![Concept art representing cybersecurity principles](https://cdn.mos.cms.futurecdn.net/JpXukHGqkZ8gapEzDQNqRW.jpg) 

![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png) 

On 1st October, Microsoft will begin disabling its Exchange Web Services (EWS) API, ahead of a full shutdown in April 2027. For many organizations, EWS has long been part of the invisible plumbing behind everyday workplace tools. It allows applications to connect to Exchange mailboxes, making it possible to access and manage data from emails, calendars, contacts and folders.

Global Field CTO at Boomi.

But EWS is almost 20 years old. Microsoft says it no longer aligns with modern requirements for security, scale and reliability, and its involvement in 2024’s Midnight Blizzard attack has added urgency to its retirement. The wider risk is also clear: APIs, particularly older and less visible ones, have become attractive targets for cybercriminals. Recent research found that 99% of organizations encountered API security issues in the past year.

Seen in that context, Microsoft’s decision to move customers towards more modern APIs such as Microsoft Graph makes sense. But API modernization is rarely as simple as swapping out one connection for another, and many organizations may soon face a rude awakening.

## You can’t migrate what you don’t know exists

The main challenge organizations will face when migrating from EWS to Microsoft Graph is visibility. Despite its limitations, EWS still sits behind many everyday workplace processes, particularly in larger and older organizations.

Booking meetings, syncing calendars or allowing a CRM to log email activity automatically may all depend on the API. After almost two decades of use, EWS has become deeply embedded in day-to-day operations.

That creates a problem. Many organizations may no longer have a clear view of where EWS is being used, by whom or for what purpose. Some integrations will have been built years ago by developers who have since left the business. Others may sit inside legacy workflows that IT teams rarely touch.

And third-party tools that are outside of the IT team’s control commonly connect to EWS. As a result, some of these hidden dependencies are almost certain to fall through the gaps during migration, because organizations can only replace the EWS integrations they know exist.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

For some organizations, this lack of visibility may make migration feel daunting, especially when EWS is tied so closely to everyday operations. It may be tempting to fall back on the old “if it isn’t broken, don’t fix it” adage, particularly if a poorly managed migration could disrupt critical tools and workflows.

But as Microsoft phases out EWS and ends support, doing nothing is not a viable option. Vital applications could lose access to Exchange, while the security risks of leaving legacy APIs embedded in the business will only become more pronounced.

Other organizations may try to avoid a difficult migration by intercepting EWS calls and translating them into Microsoft Graph, effectively rerouting traffic rather than replacing the underlying integration. At first glance, this may look like a clever workaround. In reality, it is only a temporary fix.

The same security, visibility and integration challenges remain, while every additional dependency built around this approach adds another layer of complexity. At scale, that could quickly become unmanageable.

## Moving beyond avoidance

Instead of burying their heads in the sand or looking for clever, but ultimately ineffective, ways to avoid migrating from EWS, organizations should treat its retirement as a reminder of the need for robust software lifecycle management.

Many teams evaluate an API thoroughly during implementation, then rarely review it again. But APIs evolve, security issues emerge and providers introduce updates that require action. Organizations that build resilience and lifecycle management best practices into their API estates will be better placed to respond quickly to forced migrations, minimize disruption and avoid being caught out by sudden changes.

In practice, that means treating APIs as part of the digital supply chain and applying the same level of scrutiny used for third-party suppliers when evaluating a potential integration.

Critical APIs should be continuously monitored so organizations know where they are in use, what they support and how they are performing. IT teams also need to stay informed about planned provider changes, however small they may seem, and assess how these could affect their wider API management program.

From there, organizations need a fully prepared API migration plan. Some changes may demand immediate action, such as when a third party issues a critical vulnerability disclosure. Others, such as Microsoft’s EWS retirement, may come with longer lead times but be broader in scope and scale.

In either case, organizations need a holistic strategy covering API discovery, dependency mapping, ownership and management, testing, and ongoing monitoring. Without that foundation, they risk migrating only the integrations they can see, while leaving hidden dependencies to fail later.

## Preparing for the future today

Microsoft disabling EWS is not the first event of its kind, and it will not be the last. As technology estates evolve, more legacy APIs will be retired in favor of newer versions that integrate more effectively and securely with modern solutions. The retirement of EWS should therefore be treated as more than a one-off Microsoft deadline. It is a warning about what happens when critical integrations are allowed to become invisible.

That makes resilience essential. With robust software lifecycle management, organizations can move away from panicked, reactive migrations and take greater control over their API estates. Those that prepare now will be better placed to manage the EWS migration, and whatever comes next.

*This article was produced as part of**TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:**[https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
