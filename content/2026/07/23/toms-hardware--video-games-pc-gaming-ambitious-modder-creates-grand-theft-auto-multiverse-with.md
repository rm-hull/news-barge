---
title: Grand Theft Auto Multiverse with real-time portals created by ambitious modder
  — San Andreas, Vice City and GTA III all run simultaneously, with cross-game interactions
source_url: https://www.tomshardware.com/video-games/pc-gaming/ambitious-modder-creates-grand-theft-auto-multiverse-with-real-time-portals-san-andreas-vice-city-and-gta-iii-all-run-simultaneously-with-cross-game-interactions
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-23T10:34:25Z'
published: '2026-07-23T00:00:00Z'
description: The most insane GTA mod ever.
image: https://cdn.mos.cms.futurecdn.net/hdAQPVQnW4GedxrsAF2oxB-1626-80.png
---

![GTA San Andreas, GTA Vice City and GTA III running simultaneously and interconnected through portals](https://cdn.mos.cms.futurecdn.net/hdAQPVQnW4GedxrsAF2oxB.png) 

The *Grand Theft Auto* franchise has a rich history when it comes to modding and tinkering, but we're pretty confident the community has never seen anything like this. Created by *Dryxio*, this new mod combines* GTA Vice City*,* GTA San Andreas*, and* GTA III*into one multiversal entity interconnected through real-time, fully functional portals that let you travel between the three different games as if it were just a regular window.

![portals between gta III, vice city and san andreas - YouTube](https://img.youtube.com/vi/fpsq2MyWznc/maxresdefault.jpg) 

The video above showcases just how insane this mod really is. It starts with CJ on Grove Street in *San Andreas* shooting at NPCs in different parts of the game (The Strip). Then, he moves toward the pink portal, shoots at NPCs once again, and just casually goes through it to end up in*GTA Vice City* as Tommy Vercetti. He wreaks havoc, walks back to the portal, and crosses through to*Vice City* as CJ, only to go to*GTA III* and repeat the same thing there.

The craziest part is how these portals genuinely act as windows to another world where you can stand in one game and shoot inside the other one. It's unclear whether there's a limit to the level of interaction, like if you can't drive cars through them, but it's impressive, nonetheless. The video also shows how you can place these portals anywhere in the world in any of the three games yourself.

All of this begs the question: how? The modder explains that all three games are running simultaneously inside one process, sharing one Direct3D device. Each portal is a live GPU texture; there's no video capture to fake the realism, and the transition to each game happens in real-time via an engine swap. When you walk through a portal, it simply switches to that game's engine while the others keep running in the background.

![Shooting at GTA Vice City from inside GTA San Andreas](https://cdn.mos.cms.futurecdn.net/yzSH6XvY5B8NYaz5o9CpNc-1200-80.png) 

![Shooting at GTA Vice City from inside GTA San Andreas](https://cdn.mos.cms.futurecdn.net/FXrLE8DJcuodB2VfDEGNJb-1200-80.png) 

![Shooting at GTA Vice City from inside GTA San Andreas](https://cdn.mos.cms.futurecdn.net/yzSH6XvY5B8NYaz5o9CpNc-1280-80.png) 

![Shooting at GTA Vice City from inside GTA San Andreas](https://cdn.mos.cms.futurecdn.net/FXrLE8DJcuodB2VfDEGNJb-1280-80.png) 

Each game and its world retain full native functionality such as its own AI, traffic, physics, saves, missions, and even settings. There's no loading screen when you use the portals either; you enter the world on the other side instantly, just the way you saw it before going through. This is largely possible because the source code of each game has been reverse-engineered and recompiled using an open-source engine.

Dryxio modified *re3* and*reVC*— community projects that decompile the original source code of * GTA III*and* Vice City*into clean, readable C++ code — and used* plugin-sdk*to interface with* San Andreas*. Since these games used the proprietary RenderWare engine that can't render multiple spatial scenes together, an open-source reimplementation of it called* librw* was used to compile all three games into a single unified process.

The mod isn't publicly available at the moment, but you can bet everyone in the community now has their eyes on it. It's by far the most technically complex GTA mod ever, one that doesn't even require any understanding of software to grasp its ambition. There's also the elephant in the room known as *Rockstar Games* that could see this as copyright infringement and order it to be taken down, but for now, it lives as proof of human ingenuity (and vibe-coding).

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Hassam Nasir](https://cdn.mos.cms.futurecdn.net/SxxNFHt95eGK37mKPhJpdZ.jpg)

Hassam Nasir is a die-hard hardware enthusiast with years of experience as a tech editor and writer, focusing on detailed CPU comparisons and general hardware news. When he’s not working, you’ll find him bending tubes for his ever-evolving custom water-loop gaming rig or benchmarking the latest CPUs and GPUs just for fun.
