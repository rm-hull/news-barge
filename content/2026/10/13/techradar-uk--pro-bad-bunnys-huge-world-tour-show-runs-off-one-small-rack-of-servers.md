---
title: Bad Bunny’s huge world tour show runs off one small rack of servers
source_url: https://www.techradar.com/pro/bad-bunnys-huge-world-tour-show-runs-off-one-small-rack-of-servers
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-13T16:59:21Z'
published: '2026-10-13T00:00:00Z'
description: We go behind-the-scenes with the tech powering Bad Bunny’s stadium-scale
  visual production magic
image: https://cdn.mos.cms.futurecdn.net/m6QFFsJBPUtpP9Z7fKVJNX-1940-80.jpg
categories:
- Technology & Software
- Film & TV
people:
- Carlos “Charly” Camina
- Charly
- Concho
- Sturdy
- Vishal Sharma
locations:
- Coachella
- Concho
- Puerto Rico
- UK
- Wembley
organisations:
- Charly
- Disguise
- GX3
- HTTP Sockpuppet
- LED
- NDI
- OSC
- Open Sound Control
- Screens
- TechRadar Pro
- Tottenham Hotspur Stadium
---

![Bad Bunny at Wembley Stadium.](https://cdn.mos.cms.futurecdn.net/m6QFFsJBPUtpP9Z7fKVJNX-1920-80.jpg)
![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png)

Bad Bunny’s record-breaking soldout tour was one of the hottest tickets in the UK this summer, drawing over 104,000 fans across the weekend of June 27th, 2026.

The show was highly anticipated following his Album of the Year Grammy Award for *Debí Tirar Más Fotos* and history-making Super Bowl Halftime Show.

But the excitement around the show wasn’t just because of the scale of the artist, it was also due to the incredibly ambitious scale of the production.

The best stadium tours have a way of making their use of technology seamless and in some cases, invisible.

You see a 100ft screen tracking the band’s movement from across the field without missing a beat, or members of the audience picked out and flashed on the giant LED walls around the venue.

None of it looks labored or complex, at least not to the general public in attendance. To them it’s all part of the magic of the show, which is exactly the point.

## Media servers

Carlos “Charly” Camina is the tour’s media server engineer, and the size of the kit he oversees is much smaller than the grand scale of the show might suggest. The entire production runs on four Disguise GX 3+ servers, with a fifth GX 3 unit held in reserve as an understudy for the show’s director.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

That’s down from five servers during the tour’s earlier Puerto Rico leg, despite the fact that the World Tour carries significantly more content layers and considerably bigger screens at 10,752 x 2,816px, requiring a 4K input.

The GX3+ upgrade alone roughly doubled the processing headroom for the same effects load, which is what made it possible to deliver more with a smaller footprint. The lighting runs on grandMA kit, the unchallenged global industry-standard for live event lighting control, with a grandMA light desk as the main control surface and a grandMA3 compact unit as backup.

The whole setup sits on a dedicated network split into eight isolated VLANs, a structural choice to provide containment, so that a fault in one part of the system can’t spread and collapse the whole thing. The engineering challenge on a show of this scale isn’t cramming in more and more hardware, it’s finding the smallest reliable solution that can do the job every single night, in any venue, anywhere on the planet.

## Adaptability is key on any tour

The most unique piece of engineering on the Bad Bunny Tour wasn’t actually planned or commissioned ahead of the show. During rehearsals, the creative team at Sturdy suggested photographing the crowd during the opening act and then displaying those images on LED screens around the venue later on in the show. Charly’s instinct was to push back. Loading fresh, unvetted content into the live system with zero headroom for troubleshooting is the kind of risk that wise engineers know to avoid.

His solution was to keep the additional photography content out of the Disguise system altogether. Instead, he built a standalone application using HTTP Sockpuppet and OSC (Open Sound Control) to communicate with the main Disguise system, running off a laptop. A photographer hands over images for Charly to upload. When the relevant cue fires inside Disguise, it sends a request to the laptop for specific images, which are mapped to specific locations on a four-way live layout.

Charly said that the hardest part wasn’t the concept, it was the live timing: ensuring that front-of-house and the on-stage servers sync closely enough so that there’s no discernable lag, and making sure the system never repeats the same face twice in one night.

How this curveball was handled is a good example of a pattern that shows up across the whole build: rather than adding risk to a proven core system, Charly builds smaller satellite systems to support it and keeps them loosely connected. It’s a slick approach that preserves the magic and spontaneity of a seamless live experience, without risking the core build or compromising the show’s production value.

## Animated CGI Frog - Why not?

The tour’s most curious element involved a Puerto Rican-inspired 3D animated frog called “Concho” rendered live using Unreal Engine and a face-tracked performer, which enabled Concho to interact directly with Bad Bunny mid-show as part of a FaceTime call. The segment needed a camera that could move freely, handheld, so the team decided to use an iPhone.

However, the phone could not have any visible external antennas. This meant the feed from the iPhone had to be captured over NDI (Network Device Interface) on a dedicated Wi-Fi network, rather than a standard wireless link that could have been easily interrupted by the tens of thousands of audience and staff devices around the arena. Charly’s team has to scan the RF spectrum every night to find clear channels before the Concho segment goes live.

## The benefit of reliability

The ultimate stress test of the system came during the show’s finale where the production deployed a 40-tile feed, displayed in a grid across the main 5K screen and two IMAG screens. Together with Screens Producer Vishal Sharma and his team at All of it Now, who created all the show’s Notch content, Charly decided to route four separate 4K video inputs through a Notch block to build the grid live.

Nothing was pre-rendered or keyframed and the color-grading also took place in real-time. That final segment pushed the servers to their limit, with all four of the GX 3+ units red lining on their performance markers. Despite the load, the system held and delivered a truly spectacular end to the show.

Charly has worked with Disguise servers for over a decade. In that time he’s worked on shows of all types, from festivals like Coachella to state-of-the-art mixed-use venues like the Tottenham Hotspur Stadium. With that much experience using these systems, what’s clear to him is that the value in this system isn’t in a specific creative feature. The value is knowing that if a server has an issue mid-show, he can switch to a backup with just one click and have full confidence that the backup will take over seamlessly.

For an engineer, touring a production this huge, reliability and predictability is the actual product. The breathtaking visuals that we get to enjoy as part of the audience will rightly get their applause, but the job is protecting the integrity of the show from its own scale and demands, every night, in every city, until the tour comes to an end.
