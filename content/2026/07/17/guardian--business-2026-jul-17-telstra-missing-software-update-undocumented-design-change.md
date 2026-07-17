---
title: Telstra staff unaware of mass outage risk as critical software failure ‘rippled
  slowly across the network’
source_url: https://www.theguardian.com/business/2026/jul/17/telstra-missing-software-update-undocumented-design-change-outage
source_site: The Guardian
source_slug: guardian
scraped_at: '2026-07-17T03:32:02Z'
published: '2026-07-17T00:00:00Z'
description: Telco outlines reasons for network failure that hit mobiles, trains and
  retailers ahead of appearance at Senate inquiry
image: https://i.guim.co.uk/img/media/01f886da2cd2b2ab58778f3eeb0cdbb3635860cc/619_0_6192_4954/master/6192.jpg?width=1200&height=630&quality=85&auto=format&fit=crop&precrop=40:21,offset-x50,offset-y0&overlay-align=bottom%2Cleft&overlay-width=100p&overlay-base64=L2ltZy9zdGF0aWMvb3ZlcmxheXMvdGctZGVmYXVsdC5wbmc&enable=upscale&s=e488f8fc9c1399a81cff484ae7eb687c
---

Telstra has blamed the lack of a software update for a key time-keeping system for outage that caused nationwide chaos last week, with its maintenance teams also unaware of a design change that affected how it would reset.

Ahead of an appearance by its chief executive, Vicki Brady, at a Senate inquiry into the mobile outage on Friday, Telstra provided a written submission that revealed the cause. In it, the company stated it did not lack redundancy in its network – but that such redundancy did not prevent the outage.

The submission confirmed reporting that one of Telstra’s network time protocol (NTP) servers, designed to ensure the systems had the correct time, had reset to be “2006”.

Telstra said it has three NTP servers, in Melbourne, Sydney and Perth.

During maintenance, the company shut down and restarted the server in Melbourne. Due to an “underlying software configuration” within the server, it restarted with the wrong 2006 date.

“Over the next few hours, the incorrect date rippled slowly across the network, causing authentication certificates in other servers to become invalid,” Telstra said.

“Customers were intermittently unable to authenticate onto the network (‘no service’), which affected their ability to place voice calls and use data across Telstra’s mobile network.”

Telstra said it had made an intentional design change to the equipment to fix an earlier fault – but that this had not been properly documented. This meant maintenance workers arriving at the Melbourne site early last Wednesday were not aware of how the device would be reset.

A software update had also not been applied to the device, and if that had been done, the outage may not have occurred, Telstra said.

The submission also said when the Melbourne NTP server disconnected for maintenance, the other two worked as redundancy and backup as expected.

“The failure mode here was not inherently related to hardware, levels of redundancy, or the architecture of* * our network,” Telstra said.

But when the Melbourne server supplied an incorrect date once switched back on, “downstream systems used that date in security, authentication, session and policy-control processes.”

“The issue was therefore not simply the loss of one NTP server or redundancy in the design of the configuration of the three NTP servers, but the propagation and acceptance of erroneous date information by interconnected systems that rely on timing as a trust and ordering reference.”

Telstra also said it was taking full accountability for the outage.

“That is clearly unacceptable. If maintenance work can trigger this kind of outage, it suggests our controls were not good enough,” the company said.

“We are accountable for that, and our investigation will address why that design change was not documented, why the software update was not completed, and what needs to change in our controls so known risks are captured, prioritised and closed before they can affect customers.”

In the course of the outage, Telstra said 58,835 calls to triple zero successfully connected, while 604 experienced an error.

Telstra also operates the triple-zero platform for all telcos, and the company said the platform does not use the NTP servers for synchronisation, so it was unaffected by the incident. Fixed-line callers on the NBN were also not affected.

On Friday, Brady and a number of other executives are due to appear before a Senate inquiry – established into last year’s Optus outage – to explain the outage that wrecked havoc for mobile services, transport systems, retailers and electric-vehicle charging.

The chair of the committee, the Greens senator Sarah Hanson-Young, said the inquiry will seek to get to the truth of the outage and making “sure that we don’t keep accepting a system that leaves Australians vulnerable”.
