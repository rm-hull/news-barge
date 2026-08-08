---
title: Intel's proposed orbital data centers would manage thousands of simple LEO
  satellites — two-tier network puts the brains of satellite constellations in higher
  orbit
source_url: https://www.tomshardware.com/tech-industry/space/intels-proposed-orbital-data-centers-would-manage-thousands-of-simple-leo-satellites-two-tier-network-puts-the-brains-of-satellite-constellations-in-higher-orbit
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-08T13:08:52Z'
published: '2026-08-08T00:00:00Z'
description: The proposed architecture is a different proposition from the orbital
  AI data centers
image: https://cdn.mos.cms.futurecdn.net/d7kjue9PbCHvHp6fnyUv2i-1920-80.jpg
---

![a satellite in orbit](https://cdn.mos.cms.futurecdn.net/d7kjue9PbCHvHp6fnyUv2i.jpg) 

An Intel patent application published on August 6, spotted by __Patentlyze__, describes an orbital data center architecture that moves some of the computing used to operate massive satellite constellations off the ground and into space. The architecture proposes a two-tier satellite network in which a small number of more powerful satellites in higher orbits manage large constellations of relatively simple satellites in low-Earth orbit, handling much of the computing and constellation coordination normally performed by data centers and network operations centers on the ground.

The application, US 2026/0230175 A1, is a continuation of an earlier Intel filing that was granted as US 12,542,604 B2 in February.

 ![Microsoft data center in Mount Pleasant, Wisconsin](https://cdn.mos.cms.futurecdn.net/Vh4nY3pMCcmra2ymXah9S7.jpg) 


Intel’s proposed architecture is a different proposition from the orbital AI data centers now being pursued by companies such as SpaceX and Google, which aim to move AI compute itself into low-Earth orbit. SpaceX’s planned AI1 satellite and Google’s Project Suncatcher both envision running large-scale computing workloads in space, with the resulting data beamed back to Earth over high-bandwidth optical links. Intel’s orbital data centers, on the other hand, are designed primarily to serve the satellite network itself, acting as higher-orbit compute and control hubs for the much larger constellations operating below them.

In large LEO constellations such as Starlink, Telesat Lightspeed, and Amazon’s Project Kuiper, thousands of satellites are constantly moving relative to one another and the Earth. While the satellites perform their individual tasks, the network itself still has to determine how traffic is routed, which satellites and links should communicate, how spectrum is allocated, and how the constellation responds to failures, interference, weather, and other changing conditions. Much of that network planning and control processing is traditionally handled by computers on the ground, with routing and operational instructions calculated at terrestrial network operations centers and then transmitted back up to the satellites.

 ![intel patent orbital data center](https://cdn.mos.cms.futurecdn.net/xEU8x7hfpV7kWNK5Rx2r9M.jpg) 


Intel says that this constant dependency on terrestrial infrastructure delays time-sensitive decisions, increases reliance on ground stations, and makes management harder as constellations grow into the thousands of satellites. Intel’s solution is to move part of that control and compute layer into orbit. Its architecture places more powerful satellites — which contain much more compute and storage capability than the individual LEO satellites — in Medium Earth Orbit (MEO), Geosynchronous Earth Orbit (GEO), or highly elliptical orbits, where they can maintain a broader and more persistent view of the LEO constellation below and take over tasks such as routing, mission planning, scheduling and network coordination without continually sending those workloads back to Earth.

The proposed setup does not eliminate the need for ground stations. It just keeps satellite network control processing in space. Intel specifically describes moving mission planning and scheduling operations into orbit. The company also argues that offloading heavier network-management tasks to a smaller number of powerful satellites could allow operators to build simpler, cheaper LEO spacecraft. Under current architectures, individual satellites still have to actively participate in network-control functions, requiring additional onboard compute and communications hardware. There’s currently no indication that Intel is actively building the satellites.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Etiido Uko](https://cdn.mos.cms.futurecdn.net/BBrMt7jWtSo2Dc3iKoroyD.jpg)

Etiido Uko is a news contributor for Tom's Hardware covering the latest updates in big tech and the PC industry. He is a mechanical engineer and senior technical writer with over nine years of experience in documentation and reporting. He is deeply passionate about all things engineering and technology, and is an expert in gadgets, manufacturing, robotics, automotive, and aerospace.

- 
The patents have some merit but they can't really restrict the natural evolution of satellite placement or the natural progression of trying to make low latency or orbital efficiency of data centers better. Companies like SpaceX would likely develop something similar without running afoul of these patents if the logistics of lower and higher orbit synergy made sense. Ultimately a lot of this is just the likely evolution of orbital data center progression especially once we connect AI to space station and moon base operations. I'm not sure how much value it has for terrestrial AI data center operations over low earth orbit networks that likely interconnect with laser speed systems anyway. Adding more latency with higher orbit operations has some trade offs when coordinating back on Earth.Reply
