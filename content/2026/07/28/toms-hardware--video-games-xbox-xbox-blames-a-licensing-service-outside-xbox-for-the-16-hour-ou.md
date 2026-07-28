---
title: 16-hour Xbox outage even stopped physical games from working — company blames
  licensing issue for incident that prohibited gaming across three generations of
  console
source_url: https://www.tomshardware.com/video-games/xbox/xbox-blames-a-licensing-service-outside-xbox-for-the-16-hour-outage-that-blocked-disc-games
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-28T14:30:37Z'
published: '2026-07-28T00:00:00Z'
description: Microsoft has promised a full post-incident review.
image: https://cdn.mos.cms.futurecdn.net/Y8McSo9iZFnfyFaWLyegKD-2560-80.jpg
---

![Assassin's creed valhalla](https://cdn.mos.cms.futurecdn.net/Y8McSo9iZFnfyFaWLyegKD.jpg) 

Xbox chief technology officer Scott Van Vliet said in a post on X that a licensing service sitting outside Xbox, which the platform depends on, began failing late on July 26 and took roughly 16 hours to clear, blocking sign-ins, library listings, and game launches across Xbox 360, Xbox One, and Xbox Series X|S. Microsoft restored service at 2:30 p.m. PDT on July 27.

For part of that window, Microsoft's status page warned that players might have trouble launching disc-based games, leaving a physical copy sitting in the tray no more useful than a digital one. Discs on Xbox One and Series consoles carry encrypted XVC packages with attached licenses, rather than acting as bootable media, per Microsoft's documentation.

Earlier today, many players began experiencing issues with sign in, enumerating their game libraries and playing games. The team has worked hard throughout the day to fix the issue, and we've restored service as of 2:30 PM PDT. Nonetheless, this is an unacceptable situation, and… [https://t.co/3y9TjxzKlsJuly](https://t.co/3y9TjxzKlsJuly) 28, 2026


Automated monitoring caught the failure overnight, and on-call engineers declared a major incident, according to Van Vliet, who said the team rerouted traffic onto healthy systems while the root cause was still being investigated. Anything requiring an entitlement check broke, including listing a full library and launching an owned game, and several of Microsoft's publishing and store partners depend on the same systems, which is why some titles kept working, and others didn't. "I care less about the one-line root cause," Van Vliet wrote, saying the review will look at why a failure in one service took down that much and why recovery took as long as it did.

Microsoft hasn't explained why disc-based games were caught up in the failure, but its developer documentation splits loss of connectivity into two separate categories: complete loss of internet service, and loss of one or more online services.

Console behavior is built around the first case, where the system reads a game's manifest declaration and launches anything with a mode of play that doesn't require connectivity. The second case, where the network is fine but a specific service isn't answering, is documented only as something individual games should handle without hanging or crashing. During the July 2024 Xbox outage, players recovered access to installed single-player titles by forcing the console into an offline state through Network settings.

Xbox services also went down last week during the early access launch of Halo: Campaign Evolved, and PlayStation Network took a multi-hour outage of its own on July 24. The timing of all this isn’t brilliant, given that Sony recently announced the end of physical disc production for new games in January 2028.

A Change.org petition opposing that decision has since exceeded 348,000 signatures. Microsoft, meanwhile, is testing a disc-to-digital program that grants a digital entitlement tied to a specific disc, and multiple reports say its next console may ship without a drive, though the company hasn't confirmed that. Van Vliet joined Xbox from Microsoft's Azure organization alongside CEO Asha Sharma, weeks before Microsoft cut 3,200 Xbox roles across its 2027 fiscal year and divested five studios.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Luke James](https://cdn.mos.cms.futurecdn.net/C4FAi2KzwaGLUrBqzX5aBM.png)

Luke James is a freelance writer and journalist. Although his background is in legal, he has a personal interest in all things tech, especially hardware and microelectronics, and anything regulatory.

- 
ReplyFor part of that window, Microsoft's status page warned that players might have trouble launching disc-based games, leaving a physical copy sitting in the tray no more useful than a digital one. Discs on Xbox One and Series consoles carry encrypted XVC packages with attached licenses, rather than acting as bootable media, per Microsoft's documentation. Pirates (fully digital!) unaffected.
