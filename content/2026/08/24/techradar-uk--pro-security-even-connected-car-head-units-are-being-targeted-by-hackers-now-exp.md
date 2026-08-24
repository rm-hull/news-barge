---
title: Hackers are sneaking malware into car head units through trusted updates
source_url: https://www.techradar.com/pro/security/even-connected-car-head-units-are-being-targeted-by-hackers-now-experts-warn-in-car-systems-are-at-risk-of-being-hijacked-into-a-botnet
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-24T20:43:19Z'
published: '2026-08-24T00:00:00Z'
description: A BadBox-linked campaign is now reaching car head units, raising fresh
  concerns about malware spreading through vehicles
image: https://cdn.mos.cms.futurecdn.net/U4kKJiuR4cLoeEoYecZQPK-2560-80.jpg
---

![Spotify Car Thing](https://cdn.mos.cms.futurecdn.net/U4kKJiuR4cLoeEoYecZQPK.jpg) 

- **Hackers exploited trusted software updates to deliver malware directly into car head units**
- **Kaspersky says this is the first campaign tailored specifically for vehicle head units**
- **The malware can run silently without showing drivers any visible interface**

Car head units are now being drawn into a growing wave of Android malware campaigns built for connected vehicle systems, experts have warned.

A newly discovered malware campaign is infecting these head units directly, systems that combine multimedia functions with, in some models, vehicle control.

According to Kaspersky, this campaign marks the first documented case of malware built specifically for this type of infection chain.

## Compromised update channels deliver malware straight into vehicles

Researchers believe the activity can likely be traced back to the MoYu Group, a threat actor closely tied to the well-known BadBox botnet, which spread through the legitimate update mechanisms built directly into the firmware of Android-based head units manufactured by DoFun.

The infection chain originates from TWCore, a legitimate system app that is normally responsible for collecting analytics and updating head unit software remotely.

Attackers hijacked this trusted update channel using a specialized dropper called JarService to deliver previously unknown malware directly onto a range of affected devices.

Once successfully installed, the malware operated quietly as a regular background application without ever displaying any visible user interface.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Kaspersky identified nine distinct remote commands built into the malware, capable of displaying unwanted ads and executing various forms of ad fraud.

The malware also actively collected sensitive device information, including display resolution, device model, Wi-Fi network identifier, and the device's MAC address.

Investigators found clear technical links between this campaign and prior attacks launched against TV set-top boxes tied to the same broader threat group.

The research team claims that the botnet's administration panel shares embedded URLs with residential proxy service websites PXYEDGE and ProxyForU.

BadBox itself operates as a large, sprawling network of hijacked Android devices, including streaming boxes, phones, and tablets that arrive pre-infected from the factory.

Kaspersky has already formally notified the vendor about this ongoing abuse of its legitimate software distribution channel and update infrastructure.

According to statements from DoFun, the underlying issue has since been resolved across most affected devices currently deployed in the field.

## Head units present a growing and largely unprotected attack surface

Car head units can arrive factory-installed directly from the manufacturer or get added later to older vehicles as aftermarket upgrades.

Manufacturers frequently rely heavily on the Android operating system because it simplifies interface customization and essential system integration work considerably.

This widespread industry reliance means most standard Android applications, along with most existing Android malware, can potentially run on these devices.

Head units rarely store sensitive personal data directly on board, which on the surface might suggest only limited appeal to attackers.

However, they typically include active SIM card slots and maintain constant internet connectivity for navigation services and routine software updates.

That particular combination of persistent connectivity and comparatively weak security oversight makes these systems a genuinely attractive prospect for attackers going forward.

The overall scale of this particular campaign remains genuinely unclear, and whether other head unit manufacturers face similar exposure is not yet known.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Efosa Udinmwen](https://cdn.mos.cms.futurecdn.net/nwRLdPUNG4rWu4Y6nthHDV.png)

Efosa has been writing about technology for over 7 years, initially driven by curiosity but now fueled by a strong passion for the field. He holds both a Master's and a PhD in sciences, which provided him with a solid foundation in analytical thinking.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
