---
title: Russian bot activity plunged 84% after Ukraine hit Yandex data centers, but
  the bots were back at full strength within two days
source_url: https://www.techradar.com/pro/security/russian-bot-activity-plunged-84-percent-after-ukraine-hit-yandex-data-centers-but-the-bots-were-back-at-full-strength-within-two-days
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-19T20:35:37Z'
published: '2026-10-19T00:00:00Z'
description: Day-long bot collapse saw major drop in traffic
image: https://cdn.mos.cms.futurecdn.net/85kAnS2rcuxwyaibPRC4Ze-2000-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Cloudflare
- Graphika
- Ivan Slychko
- John Kelly
- Lai Yi Ohlsen
- Marina Elmore
- Renée DiResta
- Vladimir
- Volodymyr Zelenskyy
locations:
- Kaluga
- Russia
- Ryazan
- Sasovo
- Ukraine
organisations:
- AS13238
- AfD
- CCD
- Center for Countering Disinformation
- Cloudflare Radar
- Facebook and Telegram
- Georgetown
- Graphika
- MAGA
- National Security and Defense Council
- Nod of Time
- Pravda
- Reform UK
- Russian-language Telegram
- Sasovo
- TechRadar Pro
- Via UNITED24 Media
- Warsaw Security Forum
- Yandex
---

* **Ukraine's CCD says suspected Russian bot posts in its sample fell 83.6% on October 8 after a strike shut Yandex's Sasovo data center**
* **The same data shows volume back above pre-strike levels by October 10, with a smaller 42.6% dip after the Vladimir shutdown**
* **Cloudflare and Graphika found no comparable drop in Western political communities, though Russian-language Telegram output fell 5% to 15%**

Ukraine's Center for Countering Disinformation (CCD) says suspected Russian bot accounts went almost silent after drones knocked out Yandex data centers earlier this month, with message volume across a monitored network falling 83.6% in a single day.

The findings come from an analytical report the CCD dated October 15 2026. Using Osavul monitoring software, analysts tracked 22,664 messages from 5,201 accounts showing signs of inauthentic behavior across 26 topics in Ukraine's Facebook and Telegram space between October 6 and 12.

The 83.6% figure is real, but the same report shows those accounts posting more than before within 48 hours, and independent data from Cloudflare shows that at least some of the malicious automation running on Yandex's cloud did not die so much as move house.

## A collapse in automated traffic after the Yandex Cloud took a beating

The first collapse came on October 8, hours after a drone strike and fire shut down Yandex's Sasovo data center in Ryazan region, home to two of the company's three supercomputers.

Daily messages fell from 4,032 to 660, and active accounts dropped from 1,526 to 258. Telegram took the harder hit, down 90%, while Facebook fell 79.5%. A second, shallower dip followed the October 11 strike that Yandex said had completely halted its Vladimir site, with messages falling 42.6% on October 12, from 4,711 to 2,704. A subgroup of 98 accounts the CCD flagged for justifying the invasion or inciting hatred followed the same curve, down 77.8% on October 8 and 49.2% on October 12.

The most telling detail sits in the middle. The October 9 strike at Yandex's Kaluga campus, which the company describes as its largest, only partially took the site offline, and the CCD recorded no fall in activity that day. The two dips line up with the two complete shutdowns, as one would expect if these accounts depended on that infrastructure, though that's not proof on its own.

## A surprisingly fast turnaround time?

What the 84% figure that the CCD touts leaves out is how briefly the silence held. Message volume recovered to 2,231 on October 9, then reached 4,585 on October 10 and 4,711 on October 11, both above the pre-strike level. The monitoring window in the report closes on October 12, so it cannot show whether the second dip recovered the same way.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The agency has also been downplaying the event on other forums; two days before the report, the CCD said posting in some clusters of the Pravda, InfoDefense and Nod of Time networks roughly halved for about 12 hours, and stressed that it had not recorded a significant overall decline across Russian bot farms.

On October 16, the CCD's summary of remarks by media literacy head Ivan Slychko described the effect as "a disruption of automation, not the complete disappearance of bots."

It also makes no mention of a similar comparison for ordinary accounts. On the afternoon of October 8, banks, retailers, mobile operators and news sites across Russia suffered outages. Without said information, it is hard to separate bot farms losing their servers from operators inside Russia simply losing connectivity.

The CCD is hardly an impartial player here; it is a body attached to Ukraine's National Security and Defense Council, and it has an incentive to exaggerate victories even when the data doesn't always support them.

President Volodymyr Zelenskyy had already jumped the gun, telling the Warsaw Security Forum that after the strikes "it suddenly became a little easier to breathe on many social media platforms" and that might have been a deciding factor for how the CCD built its narrative.

Beyond Ukraine, the "bots went silent" story mostly rested on a Cloudflare Radar chart showing automated traffic from Yandex's AS13238 network falling to well under 1% of its recent peak on October 11. As we noted at the time, that traffic was far more likely to be crawlers than fake social media accounts, and "bot" is a loose word when automated requests make up around half of all web traffic.

Cloudflare's own post-mortem confirms it. Marina Elmore and Lai Yi Ohlsen found 99.5% of requests from AS13238 were automated, mostly verified Yandex search crawlers, and that the network supplied only about 7% of Russia-origin bot requests. Bot traffic from Russian IP addresses hitting the post, reply, and like endpoints of one social platform dipped just 5.7% across the event period.

Graphika reached a similar verdict from the other direction. Founder John Kelly's analysis of the AfD, MAGA and Reform UK communities that viral posts claimed had gone quiet found none lost their active accounts or heaviest posters.

AfD-linked accounts posted 40,365 times on October 11, 4% below the week before and well within normal swings, while MAGA mentions on X rose 25% in the eight hours after the Vladimir strike. Georgetown's Renée DiResta, writing in Lawfare, was blunt about the viral version: "It's a great story. But it looks like fiction rather than fact."

For now, the most defensible reading of the CCD's numbers is narrower than its headline. Knocking out the right data center can briefly cut the output of Russia-based accounts aimed at Ukraine. Keeping them quiet would mean hitting the servers they move to next, and on the evidence so far, that move takes a day or two.

As one analysis of battlefield computing puts it particularly well, resilience comes from designing for disconnection, and the bot operators appear to have learned that lesson faster than Yandex did.

Via UNITED24 Media
