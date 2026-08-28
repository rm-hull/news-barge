---
title: Cloudflare frees up 100TB of RAM by shrinking 1.1.1.1's DNS cache entries —
  250 billion cached DNS entries at any given time means one wasted byte costs 250GB
source_url: https://www.tomshardware.com/tech-industry/big-tech/cloudflare-frees-100tb-of-ram-by-shrinking-dns-cache-entries
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-28T22:14:47Z'
published: '2026-08-28T00:00:00Z'
description: Per-entry memory cut by 56%, sparing Cloudflare 130 Gen 13 servers’ worth
  of DDR5.
image: https://cdn.mos.cms.futurecdn.net/QVUrvD86z3UYAMVohMuQcD-2000-80.jpg
---

![Cloudflare logo](https://cdn.mos.cms.futurecdn.net/QVUrvD86z3UYAMVohMuQcD.jpg) 

Cloudflare says that it has freed up roughly 100TB of RAM across its global fleet without reconfiguring any physical RAM modules in its servers, and that it did so by redesigning how each DNS cache entry is laid out in memory. In a technical blog post, systems engineer Sebastiaan Neuteboom gave us an in-depth look at five Rust-level changes to Big Pineapple, the platform behind the 1.1.1.1 resolver, that shrank each cached entry from 953 bytes to 420 bytes and made the cache faster in the process, with insert throughput up 43% and lookup latency down 19%. The recovered memory matches the combined DDR5 in 130 of Cloudflare's 768GB Gen 13 servers, reclaimed in the face of server-grade DDR5 prices that are on track to double year over year.

 ![HBM3E vs HBM4](https://cdn.mos.cms.futurecdn.net/xi79WuWDZXzix4Fc7sXNMn.png) 


Just one wasted byte per entry costs Cloudflare more than 250GB of fleet memory, which is a consequence of Big Pineapple holding more than “250 billion cached DNS entries at any given time.” The first of the five changes, replacing Rust's growable Vec and String containers with fixed-size boxed slices, saved over 15TB on its own by dropping capacity fields the data never uses once cached.

Further changes collapsed the three record lists in every DNS response into one buffer indexed by 2-byte offsets, and dropped owner names that duplicate the queried domain, rebuilding them at read time instead. The last change stores record data as length-prefixed raw wire-format bytes, ending an arrangement in which a 4-byte A record took up the same 144 bytes as the largest record type Cloudflare caches, the rarely seen NAPTR.

Packing record data contiguously also improved CPU cache locality, meaning that most record types now copy straight from the stored buffer into outgoing responses instead of being re-serialized field by field.

According to Cloudflare’s benchmarks in the technical blog, insert throughput is now 893,000 entries per second, up from 625,000, with lookup latency down from 828 to 670 nanoseconds. Over the rollout, which ran from mid-May to early July, p99 resident memory per instance fell from 9.3GB to 5.3GB.

The Gen 13 servers, which Cloudflare calls its most powerful yet, each carry 768GB of DDR5-6400. The company settled on that config back in March after pricing out a 1,152GB option and rejecting it partly because of high memory prices.

This DNS cache work is the second large memory-reclamation project Cloudflare has completed in the last year, following the FL2 rewrite of its request-handling layer in Rust last September. Efficiency has been driving the company’s hardware picks for years, including the switch to AMD's 96-core EPYC 9684X for its Gen 12 servers.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

None of the liberated RAM will be cashed out as smaller memory configurations, though; Cloudflare plans to pour it back into larger DNS caches, which raise hit rates and cut the query traffic it sends upstream to authoritative servers.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Luke James](https://cdn.mos.cms.futurecdn.net/C4FAi2KzwaGLUrBqzX5aBM.png)

Luke James is a freelance writer and journalist. Although his background is in legal, he has a personal interest in all things tech, especially hardware and microelectronics, and anything regulatory.

- 
Crazy how many resources can be freed up by a small handful of software engineers when you're talking about hardware on this scale. Doing some rough napkin math, 1,560 DDR-5600 RDIMM's were spared at let's say an average street price of $2,500 per RDIMM resulting in a potentialReply**$3.9 million savings.** Just for DNS, just in memory costs.
 
 Cloudflare is surprisingly transparent about their custom servers:
[https://blog.cloudflare.com/gen13-config/](https://blog.cloudflare.com/gen13-config/)
- 
The RAMpocalyse has been a decade and a half in the making from a severe lack of any optimization for memory usage. We've had so much surplus memory it was cheaper to code less and cache more to pretend like systems and apps were more performant than they actually were. Just relying on caching everything they need to do the work quickly, rather than coding it to work smart and efficiently.Reply
 
This is just one very blatant example of that stupid industry dogma coming to a head when memory finally became too expensive to ignore. And now people need to actually optimize their software to run with less of it so systems can be significantly cheaper and more efficient. Because they can't afford to double their infrastructure again on poorly coded and un-optimized production software.
- 
ReplyKaiserTom said:The RAMpocalyse has been a decade and a half in the making from a severe lack of any optimization for memory usage. We've had so much surplus memory it was cheaper to code less and cache more to pretend like systems and apps were more performant than they actually were. Just relying on caching everything they need to do the work quickly, rather than coding it to work smart and efficiently.
 
 This is just one very blatant example of that stupid industry dogma coming to a head when memory finally became too expensive to ignore. And now people need to actually optimize their software to run with less of it so systems can be significantly cheaper and more efficient. Because they can't afford to double their infrastructure again on poorly coded and un-optimized production software.
Nailed it!! 👍👍
