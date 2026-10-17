---
title: Leap seconds being retired next year to avoid wreaking havoc on computer systems
  — International measurement organization makes move to simplify atomic time tracking
source_url: https://www.tomshardware.com/tech-industry/international-measurement-organization-to-retire-leap-seconds-next-year-to-avoid-wreaking-havoc-on-computer-systems-group-makes-move-to-simplify-atomic-time-tracking
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-17T20:34:28Z'
published: '2026-10-17T00:00:00Z'
description: No more time travel?
image: https://cdn.mos.cms.futurecdn.net/mK5eoUF73A9Kph4TsFTiq8-1920-80.png
categories:
- Technology & Software
- Hardware
- Careers & Productivity
- Business & Entrepreneurship
people:
- EzzyB
- Jowi Morales
- Tom
locations:
- Earth
- TAI
organisations:
- BIPM
- Google News
- International Bureau of Weights and Measures
- International System of Units
- Jowi Morales
- NIST
- Reddit
- SI
- Time Service
- UTC
---

![a ticking watch](https://cdn.mos.cms.futurecdn.net/mK5eoUF73A9Kph4TsFTiq8-1920-80.png)

The International Bureau of Weights and Measures (BIPM), which maintains the International System of Units (SI), has voted to expedite the retirement of the leap second, moving forward the date from 2035 to May 20, 2027, an adjustment that could wreak havoc on computer systems, which expect a consistent 60 seconds every minute.

The leap second is occasionally added to Coordinated Universal Time (UTC) to ensure that it remains in-sync with the Earth’s rotation. Our planet’s movement isn’t a constant one revolution every 24 hours owing to forces applied by the atmosphere, the oceans, its core, and even the Moon, and according to BIPM [PDF], these changes mean a 30% probability of needing a “negative leap second” by 2035.

A positive leap second adds an extra second in the year that it’s applied — for example, clocks went to 23:59:60 on Dec. 31, 2016, before switching to 00:00:00 on Jan. 1, 2017. This could spell trouble for machines that haven’t been updated to accommodate this, especially as leap seconds aren’t applied at a constant scale, meaning programmers cannot pre-program events like these, unlike leap years, which usually happen every four years. What’s more concerning is that the opposite of a positive leap second has never been done before. “A negative leap second has not previously been applied, and it is considered to pose a high risk of causing anomalies and disruption to critical infrastructures that are largely unprepared,” the BIPM said. It also estimated that the required investment to prepare for this event to be “similar to their preparations for the millennium bug.”

Leap seconds have also historically caused problems for websites and tech companies, with Reddit famously crashing after the 2012 addition of a leap second. While a leap second will likely not affect a desktop PC, especially if the Time Service server it relies on is updated, the BIPM is still worried that national critical infrastructures like transportation, energy distribution, telecommunications, and even space projects could descend into chaos if it enforces a negative leap second. So, instead of spending money upgrading software and replacing incompatible hardware within the next 10 years, the international standards body instead opted to scrap it altogether and replace it with the leap hour next year.

The group says that this would ensure long-term continuity for UTC, which is expected to remain in sync with TAI for several centuries. This also means that you no longer have to manually adjust your clocks every few years or so to exactly match this Raspberry Pi Pico atomic clock. While a time jump of an hour might be shocking for many people if and when it happens in the distant future, the BIPM recognizes that something similar already exists globally. “In many countries, there are differences of more than one hour between local apparent solar time and civil time due to the choice of time zone,” the organization wrote. It also added that “changes of an hour are regularly introduced when daylight-saving time is used.”



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Jowi Morales](https://cdn.mos.cms.futurecdn.net/gM7E2WSDg2wgCFoaDPz9yK-140-80.jpg)

Jowi Morales is a tech enthusiast with years of experience working in the industry. He’s been writing with several tech publications since 2021, where he’s been interested in tech hardware and consumer electronics.

* Leap seconds simply don't belong in UTC. And that's where they cause most of the issues.  
    
  When converting to local time,*that's* when you want to apply stuff like adjustments for the Earth's rotational speed, because local timezones are fundamentally about the orientation of a geographical area towards the sun.  
    
  I get that it's convenient to be able to use nice, round numbers for converting between local times and UTC. Sacrificing that is a small price to pay for UTC, itself, becoming more more regular and stable.  
    
  Also, the idea that we're now going to let local time deviate from solar time by a whole hour is also pretty silly. But, there will be quite some time for people to reconsider, before the difference ever becomes noticeable. Reply
* EzzyB said:Aren't pretty much all computers, (I know mine is) synchronized via a time server? One would think this could be adjudicated via NIST or something like that.It's not really a matter of synchronization. It's primarily a matter of how time arithmetic works. And, in sensitive financial & realtime control scenarios, exactly when & how leap seconds are applied can matter a great deal to the functioning of those systems. Reply
