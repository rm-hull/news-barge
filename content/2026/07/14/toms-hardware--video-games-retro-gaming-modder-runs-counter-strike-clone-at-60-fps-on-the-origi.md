---
title: Modder successfully runs Counter-Strike clone at 60 FPS on the original Sony
  PSP — created his own Rust-based 3D engine to power 480 x 272 gameplay, also works
  on PS Vita
source_url: https://www.tomshardware.com/video-games/retro-gaming/modder-runs-counter-strike-clone-at-60-fps-on-the-original-sony-psp-openstrike-is-a-proof-of-concept-with-bot-rounds
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-14T10:08:53Z'
published: '2026-07-14T00:00:00Z'
description: Instead of asking why, always ask why not.
image: https://cdn.mos.cms.futurecdn.net/hjPHQeu7QDt9VQNr7Gdct4-2560-80.jpg
---

![ANTIPOLO CITY, PHILIPPINES – NOVEMBER 20, 2019: Used and old portable game console on a table.](https://cdn.mos.cms.futurecdn.net/hjPHQeu7QDt9VQNr7Gdct4.jpg) 

Barely a day goes by without some retro system developer accomplishing a technical feat that beggars belief. OpenStrike is the latest mad project, creating a proof-of-concept reimplementation of the seminal *Counter-Strike* for the Sony PlayStation Portable (PSP), a 22-year-old system that arguably has no business running the game.

The port was made by Yifeng Wang (aka doodlestrike), who apparently created his own Rust-based 3D engine called Pocket3D for the affair, along with the PocketJS JavaScript engine for the game rules and UI. Despite the proof-of-concept status, Wang says that elimination matches with bots are already playable, though the game's famous buying stages aren't yet functional. The full set of eight original *Counter-Strike* maps have already been tested, and interested modders should easily be able to roll their own.

Yes, that's Counter Strike on a PSP!Yes, that's DevTools inspecting game UI!Yes, it's PocketJS! Clean room implemented FPS engine, fully open JavaScript mod API, ~12MB RAM footprint, 60fps, fully open source. ⚡️ pic.twitter.com/OprLN3E71JJuly 10, 2026


The engine manages to run the game with bots at a steady 60 FPS at the PSP's native 480x272 resolution, thanks to pre-processing graphical assets to directly bake lightmaps into vertex colors (as opposed to real-time or on-startup calculations). Interestingly, Wang kept the old-school BSP (Binary Space Partitioning) rendering method to cull non-visible areas rather than use a fancier modern algorithm, lending credence to the "don't fix what isn't broken" motto.

The game also runs on the PS Vita, a system with 4x the effective resolution of the original at 960x544, with native graphics, without upscaling of either 3D rendering or 2D assets. You should also be able to run the project as a standard desktop game, and naturally, it's playable on the popular PPSSPP emulator. To get the project going, you'll have to provide your own copy of the *Counter-Strike* asset data, similar to using*Doom*'s original WADs in one of the many ports.

The project's entire technical architecture is impressive, as Wang went way beyond the scope of "make a 3D engine that load maps." Both the Pocket3D and PocketJS 2D engines are generic, and OpenStrike is merely the first "product" that uses them. The code runs on a server/client/event architecture, and the event handling (ex: shooting) is decoupled from the rendering core, preventing nasty FPS dips. The game is testable offline, and most everything is trivially moddable. You should check out the OpenStrike repo if you're interested.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.
