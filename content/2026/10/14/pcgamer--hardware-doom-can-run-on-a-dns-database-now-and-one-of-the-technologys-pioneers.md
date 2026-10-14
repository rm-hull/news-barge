---
title: Someone has made Doom run on a DNS database
source_url: https://www.pcgamer.com/hardware/doom-can-run-on-a-dns-database-now-and-one-of-the-technologys-pioneers-says-i-cant-decide-whether-this-is-deliciously-horrible-or-else-horribly-delicious/
source_site: PC Gamer
source_slug: pcgamer
scraped_at: '2026-10-14T17:06:05Z'
published: '2026-10-14T00:00:00Z'
description: Apparently the database is acting a bit like a "librarian" and not doing
  the actual compute.
image: https://cdn.mos.cms.futurecdn.net/NqRLotHDysoV2dhuS7X6Ei-1920-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Corey Quinn
- Doom
- Paul Vixie
locations: []
organisations:
- DNS
- PC Gamer Circuit Breaker
- RFC
- The Register
---

![Doom Enhanced (1993) screenshot - chaingun firing at two floating cacodemons](https://cdn.mos.cms.futurecdn.net/NqRLotHDysoV2dhuS7X6Ei-1920-80.jpg)

In the early 2000's, the perennial question was whether a powerful system could run Crysis. These days, it's whether a minimal one can run Doom. We've seen an affirmative answer to this question when it comes to vapes, a motherboard BIOS, and even a pregnancy test. And now? A DNS database.

To be clear, we've seen Doom broken down into DNS text records before, but this time it seems like the database is doing more than file storage. This new version is courtesy of Corey Quinn over at The Register, who explains: "I have compiled Doom for a 32-bit machine whose arithmetic and memory live in DNS."

DNS, for those unaware, means 'domain name system', and is the system that translates URLs into IP addresses that computers can actually interact with to visit. You can also create your own DNS databases with your own entries.

Quinn realised that such a database could be used essentially as a "librarian", pulling pre-made answers to relevant operations: "The database itself is 6.4 million rows of truth tables."

One of the main pioneers of DNS, Paul Vixie, said: "I can't decide whether this is deliciously horrible, or else horribly delicious. in either case, it's the best use of RFC 2136 DNS UPDATE that I've ever seen."

DNS UPDATE is what allows DNS records to be changed, which is also what's required for values and variables to change and be updated in a game world. That's the key trick here, as far as I can tell: Quinn realised there's enough similarity in the way DNS works to essentially replicate the usual conditional 'if this, then this' way that code works.

![Doom (1993) key art depicting Doom Guy shooting at hordes of demons clawing at him from below.](https://cdn.mos.cms.futurecdn.net/hGepsyz5Aiffh5UJCnSbjN-1200-80.jpg)

"I want to be very clear here: this isn't DNS pretending to be a CPU." says Quinn. "The instruction decoding is done ahead of time by a compiler; BIND never executes an instruction itself. All that it sees is a key-value read, a conditional write, and 6.4 million rows of precomputed answers.

The PC Gamer Circuit Breaker newsletter breaks down the latest PC gaming tech, and finds you the best deals on the best products

"It's not really a computer; it's simply a very good database. And that turns out to be enough."

Yes, that's right: 6.4 million rows. And it's hardly a snappy experience, as one update takes just over 54 seconds: "Doom says its tic rate is 35 per second, so 'playable' is a tic every 28.6 ms. I remain at 54,000 ms, which is three orders of magnitude away from victory."

So, not exactly a practical gaming experience, but certainly a fun project. If you want to try it out, Quinn has published the code on GitHub, so have at it.

![Razer Blade 16 gaming laptop](https://cdn.mos.cms.futurecdn.net/YwnnY4PZ7TcCYKRYDho7VW-140-80.jpg)
