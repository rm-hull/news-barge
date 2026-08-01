---
title: Bad updates, broken cables and blackouts - Cloudflare reveals some of the wildest
  reasons behind Internet downtime across the world
source_url: https://www.techradar.com/pro/bad-updates-broken-cables-and-blackouts-cloudflare-reveals-some-of-the-wildest-reasons-behind-internet-downtime-across-the-world
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-01T17:11:30Z'
published: '2026-08-01T00:00:00Z'
description: Cloudflare tells us some of the oddest reasons behind Internet outages
image: https://cdn.mos.cms.futurecdn.net/ME2kbLVLto6WB8fUwLkQEk-1920-80.jpg
---

![In this photo illustration, the Cloudflare logo is seen displayed on a smartphone screen.](https://cdn.mos.cms.futurecdn.net/ME2kbLVLto6WB8fUwLkQEk.jpg) 

- **Cloudflare summary logs a typhoon, two earthquakes, power failures, and thirteen government exam shutdowns**
- **It also identified a fiber cut, drone damage to an AWS region, and a botched DNSSEC key rollover**
- **The report's sharpest finding is that Tanzania's accidental power blackout looked almost identical in the data to its deliberate election-day shutdown in 2025**

Cloudflare has published its latest account of what recently knocked chunks of the Internet offline, and the list reads like a catalogue of everything that can go wrong at once: a typhoon, two earthquakes a minute apart, a national power failure, ten government shutdowns timed to school exams, a fiber cut, drone damage to a cloud region, and a routine cryptographic key update that briefly made every .de website in the world unreachable.

Drawn from traffic telemetry on Cloudflare Radar, it is a useful reminder that the systems most people treat as a utility are held together by a surprisingly small number of things.

With geopolitics in the Middle East shaping traffic in Iran, the UAE, Iraq and Sudan, Cloudflare found that not only did the former's traffic drop even after a shutdown ended two months ago, but the UAE seems to be one of the most affected by the on-again, off-again US-Iran conflict thanks to two AWS facilities being struck by Iranian drones.

## An accidental blackout and a government shutdown look similar from the outside

Cloudflare's insights tend to make for an interesting read on how the connected world functions, often defying expectations about traffic, online activity, and user behavior, with the recent FIFA 2026 World Cup being an excellent place to start.

When it comes to the most severe disruptions, one would turn to Iran's approach, which cut off internet access during its conflict with the US, an engagement that also had ramifications for most of its Gulf neighbors.

Interestingly, Radar began picking up signs of restoration on May 26 2026, ending an 88-day shutdown that had left the country almost entirely offline since February 28, but it never reached peak pre-conflict levels.

By May 27, traffic had returned to 40% of pre-outage levels, consistent with reports that access was being reintroduced selectively. It has since climbed as high as 90% before settling at roughly 59% of pre-shutdown levels, suggesting that more stringent restrictions may be in effect even as the country grapples with a war that threatens to reignite at a moment's notice.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The most consequential item on the list, as a result of the conflict, is ironically the one that does not look like an Internet outage at all. HTTP traffic to AWS me-central-1, the cloud region in the United Arab Emirates, has remained low, matching AWS status reports at the end of April 2026 stating that the region had been damaged by the conflict in the Middle East and could not reliably support customer applications.

This followed earlier reports in March of physical damage to facilities in both the UAE and Bahrain caused by drone strikes, with two UAE facilities directly hit. It also highlights an interesting insight: A cloud region has become the sort of concentrated dependency that a submarine cable used to be, with the added complication of being a physical target that is much easier to locate than an undersea cable.

 ![Annoyed Windows 10 user](https://cdn.mos.cms.futurecdn.net/f5rHgMjfhkWWcCmCmjKyUj.jpg) 


The longest single disruption came from Super Typhoon Sinlaku, the strongest storm of the 2026 Pacific typhoon season so far, which tracked through the Mariana Islands in mid-April and passed just north of Guam. The island avoided a direct hit, but tropical-storm-force winds knocked out power, disrupted water systems, and took connectivity with them. Traffic from the territory fell as much as 80% below expected levels on April 13 and 14.

Venezuela lost connectivity on June 24 when two major earthquakes struck northern Venezuela within roughly a minute of each other, at Yumare and San Felipe, followed by an aftershock near the coast outside Caracas, coinciding with a fall in traffic visible across Fibex Telecom, which serves an estimated 1.6 million users.

Three days later, a power outage in Tanzania produced a sharp drop in HTTP traffic lasting at least five hours, with Cloudflare drawing parallels to the country's election-related blackout in 2025.

Saint Lucia lost most of its connectivity on June 21 when traffic on Karib Cable's network fell to essentially zero by 21:00 UTC and remained flat for the better part of a day, reportedly due to a fiber cut near the island. Karib Cable is one of the largest providers there, so the loss was registered nationally, with the country's overall traffic falling by around 60% compared with the previous week.

In terms of a self-inflicted wound, Germany takes the cake: On 5 May, DENIC, the registry for the .de domain, performed a DNSSEC key rollover, the routine periodic replacement of the cryptographic keys used to sign a zone's DNS records, and the process began producing invalid signatures.

Because DNSSEC-validating resolvers only trust answers whose signatures match the current published keys, a mismatch is read as evidence of tampering, so resolvers worldwide rejected every .de lookup and returned errors until normal service resumed at 23:15 UTC. To users, it did not appear to be a cryptographic failure. It presented as German websites not loading, email bouncing, and apps timing out. It resulted in global .de query volume going up during the outage rather than down, indicating that users were, as a result, looking for ways to access said sites, amplifying the failure, at least statistically.

Taken together, Cloudflare's insights about the quarter are less a parade of exotic failures than a fairly consistent argument about concentration.

One registry's keys gate an entire national domain for the whole world. One provider carries enough of Saint Lucia's traffic to take the country with it. One cloud region hosts applications that have no idea they are under attack by a drone strike, causing unintended blackouts. The causes are both ordinary and extraordinary. It is the dependencies, however, that are extreme, making the case for redundancies worldwide.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Rahim Amir](https://cdn.mos.cms.futurecdn.net/9xKZFBamtEZKSChRvywbPB.png)

Rahim Amir is a UAE-based tech writer who enjoys building PCs as much as he enjoys writing about them. He has been professionally writing about PC hardware since 2023, focusing on buyer’s guides, hardware reviews, and sponsored content and features related to tech.

Having built hundreds of gaming PCs and being an avid gamer in his spare time, Rahim tends to have stronger opinions about hardware than most. This is particularly on display when he gets his way with powerful, but minimalistic RGB builds even as Small Form Factor (SFF) PCs come a close second.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
