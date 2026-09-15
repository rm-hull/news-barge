---
title: Developer builds viral 3D source code visualizer that consumes 21GB of RAM
  — flies around 2.5 million lines of code at over 120 frames per second
source_url: https://www.tomshardware.com/tech-industry/developer-builds-viral-3d-source-code-visualizer-that-consumes-21gb-of-ram-flies-around-2-5-million-lines-of-code-at-over-120-frames-per-second
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-15T11:26:57Z'
published: '2026-09-15T00:00:00Z'
description: He was so preoccupied about whether he could, he didn't stop to think
  about whether he should.
image: https://cdn.mos.cms.futurecdn.net/6sXhZsyDZFqzFQmRwMjbx-2214-80.jpg
---

![Rust code](https://cdn.mos.cms.futurecdn.net/6sXhZsyDZFqzFQmRwMjbx.jpg) 

The immortal line "it's a Unix system, I know this" is forever entrenched in many a techie's brain. In the Jurassic Park movie, the visualization software in question was Silicon Graphics' File System Navigator for IRIX, an actual piece of software running on a real SG workstation. The concept of viewing files in 3D space never truly caught on, but the horsepower available in contemporary machines may change that. Makepad creator Rik Arends created his own 3D flyable source code visualizer that he claims handles 2.5 million lines with ease, at 120+ FPS, no less.

Ironed out the last performance issues with my full 2.5m line codebase explorer. 120hz awesomeness. Can only upload 60fps video tho. Much nicer uncompressed pic.twitter.com/LUsrmVaI6LSeptember 12, 2026


Although the published video is only at 60 FPS due to X's limitation, the navigation looks smooth indeed, and it's impressive to see all the actual source code in a reasonably readable manner. Arends says the visualization initially took 21 GB of RAM (in this economy?!), but that after judicious application of indexes and streaming compression, he got memory usage down to a much more palatable 3.5 GB. Although he remarked that he's yet to fully optimize the visualizer, he did try to load Chromium's entire source tree (51 million lines) in only 60 seconds at one point.

While one can argue that the 3D visualization of the code itself is probably really fun to look at, its practical use is also questionable, at least as-is. A commenter remarked that adding a time element would help immensely, by displaying changes to the source files. 3D tracking of dependencies would probably be handy, too. There's already an actual full-fledged commercial tool called CodeCharta that visualizes changes and hotspots in 3D, though the flybys aren't quite as impressive.

Arends says that he intends to turn this visualization tool into a product and charge a small fee for it, though he admits that the usefulness of the visualization may be limited. When asked why he created this, he simply said, "because I could." The jury is still out on whether he should.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png) 

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.
