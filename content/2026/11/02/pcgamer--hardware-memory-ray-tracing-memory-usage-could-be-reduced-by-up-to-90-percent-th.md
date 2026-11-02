---
title: '''Most significant'' DirectX update brings Nvidia''s Mega Geometry to every
  other GPU vendor'
source_url: https://www.pcgamer.com/hardware/memory/ray-tracing-memory-usage-could-be-reduced-by-up-to-90-percent-thanks-to-most-significant-directx-update/
source_site: PC Gamer
source_slug: pcgamer
description: Potentially getting much more out of existing hardware is nothing to
  sniff at.
image: https://cdn.mos.cms.futurecdn.net/3vaLZrUADLuNub9iKdwiX6-2560-80.jpg
published: '2026-11-02T00:00:00Z'
scraped_at: '2026-11-02T21:44:23Z'
categories:
- Technology & Software
people:
- Razer Blade
locations:
- Techspot
organisations:
- Alienware
- GPU
- Lenovo LOQ
- MSI Vector
- Microsoft
- PC Gamer Circuit Breaker
- TLAS
---

![UL 3DMark new DirectX Raytracing benchmark](https://cdn.mos.cms.futurecdn.net/3vaLZrUADLuNub9iKdwiX6-1920-80.jpg)

While I go 'oo' at every perfectly lit videogame vista, ray tracing can sometimes make my gaming rig go 'HNNNG'. I love a traced ray as much as the next person, but realistic reflections and lighting can be a bit of a memory hog. Thankfully, Microsoft is previewing something new for DirectX that could significantly take the load off many ageing rigs.

It's a pair of features called 'Clustered Geometry' and 'Partitioned TLAS'. At the risk of oversimplifying, you can think of this DirectX update as bringing tech very similar to Nvidia RTX Mega Geometry to every other GPU vendor.

Obviously there's more to it than that, though, with Microsoft describing this as the "most significant update [to DXR] since its debut in 2018." Top line: Microsoft's own testing of this update suggests it could reduce ray tracing memory load by as much as 90% without the need for a team green GPU (via Techspot).

So, how does it work? Well, without this update, ray tracing is already beaming between less detailed versions of the geometry you see in-game. Traditional ray tracing tech does this because bouncing around detailed models afresh for every frame would simply take too long.

Clustered geometry slices up the detailed models into neat little packages of 256 triangles or fewer. Partitioned TLAS then does a similar thing for the entire videogame vista, splitting a scene into smaller regions. Why? Well, rather than searching the entire map every time, looking for what's changed and updating the frame accordingly, the ol' dread pirate Ray Tracing needs only to run their finger over the quadrants they know are different, marking the spot with 'X'—or something like that, the metaphor got away from me a bit in the middle there.

![Asus TUF Gaming Radeon RX 9070](https://cdn.mos.cms.futurecdn.net/N36js7RR4FjLtQ6SMHBH5i-1200-80.jpg)

Basically, this fresh DirectX tech massively simplifies the ray tracing data your rig has to check and update frame to frame. That could free up a whole lotta memory, with Microsoft demonstrating a reduction of 7.5 GB to 774 MB on an AMD Radeon RX 9070. Obviously, frame rates also benefitted, jumping from a wince-worthy 1.2 fps to a very impressive 79 fps in Microsoft's testing.

Now, this isn't really a case of simply installing an update and, 'whee, you're flying!' Microsoft issues a fair few caveats—for one thing, not all games are going to replicate the wins its specialised test environment saw.

The PC Gamer Circuit Breaker newsletter breaks down the latest PC gaming tech, and finds you the best deals on the best products

For another, working with clustered geometry and all of those packages of up to 256 triangles uses a lot more temporary scratch memory compared to traditional tech—that presents its own logistical concerns for game developers.

It's also worth reiterating that this update is not yet widely available, and there's no word yet on when PC gamers like you and me will be able to get our mitts on it either. If you feel like going sicko mode, though, Microsoft writes you can gain access to experimental features like this by using "matching Agility SDK preview headers and runtime, a supporting driver, and Windows Developer Mode."

Still, the potential to cut down memory usage without needing to buy any new hardware is very promising during these times of runaway pricing for both memory and GPUs. If I can put off a pricey upgrade for a few years more, I'll be happy.

![Razer Blade 16 gaming laptop](https://cdn.mos.cms.futurecdn.net/YwnnY4PZ7TcCYKRYDho7VW-140-80.jpg)

**1. Best overall:Razer Blade 16 (2025)2. Best budget:Lenovo LOQ 15 Gen 103. Best 14-inch:Asus Zephyrus G144. Best mid-range:MSI Vector 16 HX AI5. Best high-performance:Lenovo Legion Pro 7i Gen 106. Best 18-inch:Alienware 18 Area-51**
