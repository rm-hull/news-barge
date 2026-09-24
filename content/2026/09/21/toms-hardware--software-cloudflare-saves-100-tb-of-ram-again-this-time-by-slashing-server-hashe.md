---
title: Cloudflare saves 100 TB of RAM again, this time by slashing server hashes by
  90% — cutting 100,000 entries down to 10,000 eliminates massive cache bloat
source_url: https://www.tomshardware.com/software/cloudflare-saves-100-tb-of-ram-again-this-time-by-slashing-server-hashes-by-90-percent-cutting-100-000-entries-down-to-10-000-eliminates-massive-cache-bloat
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-21T15:05:46Z'
published: '2026-09-21T00:00:00Z'
description: A perfect illustration of an optimization for memory, after an optimization
  for speed
categories:
- Technology & Software
- Hardware
image: https://cdn.mos.cms.futurecdn.net/URarwPfgbrbBaz3ggUPSK-1350-80.webp
locations:
- Ketama
- Pingora
people:
- Bruno Ferreira
organisations:
- Cloudflare
- Get Tom's Hardware
- PC
- Rust
- Tom's Hardware
---

![Cloudflare - Ketama tuning](https://cdn.mos.cms.futurecdn.net/URarwPfgbrbBaz3ggUPSK.webp)

Cloudflare has saved 100 TB of RAM again, but this time by tuning its hash-mapping algorithm. One of Cloudflare's largest business use cases is data caching, more specifically serving a URL directly from memory or disk instead of fetching it from the live site, which may take a significant amount of time. The company uses its own open-source Pingora framework for the task of mapping an arbitrary URL to one of its cadre of cache servers, using the Ketama algorithm. This task is simple in concept, but can get quite tricky in an environment where it's expected that backend servers appear and disappear — and harder still when done at Cloudflare's scale.

"Backend routing," or the mapping of a URL to one of many cached servers, requires a *lot* of tables held in memory. An incoming URL is hashed (like you do with files with CRC-32), and that resulting number is taken and sent out to a server. The first instinct is to do this sequentially, one URL per server, but you hit the first problem: the same URLs aren't going to the same servers. So what you do is you make a hash corresponding to the server, say with its IP address and name, and match both hashes together by numerical proximity.

![Cloudflare - Ketama tuning](https://cdn.mos.cms.futurecdn.net/ZG4xwxqseRGfZMZzghnHK.webp)

That sounds simple, and it works fine, as the URL hashes' distribution is going to be effectively random, and the requests will be redirected to the same server in an egalitarian way. But then you run face-first against the second problem: say you have four servers serving 25% of requests each, and #2 disappears because someone tripped on the power cable. You'll be forced to redirect the requests it handled onto whichever are closest in the hash map, and end up overloading server #3, the next one over, while #1 and #4 remain under little load.

The solution to *that* is to add more hashes per server and mix them up randomly. Now your four servers' many hashes have a random distribution, and if one dies, incoming requests should be equally distributed among the remaining ones. This takes a lot of memory, and it takes far more once you set up layers with weight rules (so that bigger servers handle more requests), and the fact that, due to content restrictions and architectural regions, not all servers can serve all requests. All told, Cloudflare was running with as many as 100,000 server hashes per machine, ballooning RAM requirements.

![Cloudflare - Ketama tuning](https://cdn.mos.cms.futurecdn.net/y9aYJJLEGr4jjfLtNxBHK.webp)

After judicious application of some algebra and basic statistics, Cloudflare engineers concluded that using those 100,000 hashes was far and away beyond the point of diminishing returns. The team calculated that a mere 10% of that amount was good enough for nearly the same results, as the error rate barely drops for each order of magnitude beyond 10,000. After some judicious wrangling of Rust's data structures to save 2 bytes per entry in the hash-server map. That sounds like nothing, but it quickly adds up with billions of records.

All things considered, the Cloudflare team saved around 100 TB of RAM total with this optimization. To play it safe, the team added this "v2" algorithm as a separate code path rather than replacing the code altogether — allowing them to simply swap back to the original one if something broke. Now if only all modern software were this judicious about resource usage.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.
