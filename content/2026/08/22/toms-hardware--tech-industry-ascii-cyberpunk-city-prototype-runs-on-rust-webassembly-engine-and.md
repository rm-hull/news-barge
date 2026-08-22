---
title: Walk through a 3D cyberpunk city built purely from ASCII characters — a text-based
  metropolis runs on a 283KB Rust WebAssembly engine feeding a WebGL renderer
source_url: https://www.tomshardware.com/tech-industry/ascii-cyberpunk-city-prototype-runs-on-rust-webassembly-engine-and-webgl-shaders
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-22T16:36:53Z'
published: '2026-08-22T00:00:00Z'
description: A 283KB Rust module and two compiled shaders sit behind the character
  grid.
image: https://cdn.mos.cms.futurecdn.net/RAiUvf9c7FMGbrkrWApGmZ-1469-80.png
---

![ASCII cyberpunk city prototype runs on a Rust WebAssembly engine and WebGL shaders](https://cdn.mos.cms.futurecdn.net/RAiUvf9c7FMGbrkrWApGmZ.png) 

Solo developer Grow Now! Games has put a playable browser build of its walkable ASCII cyberpunk city online, running on a 283KB Rust WebAssembly engine feeding a WebGL renderer. The build went live this week alongside a second YouTube video, ASCII City Update: Interiors, Elevation & Skyscrapers, following the original video, which has passed a million views and 9,000 comments.

 ![A hand holding the Ryzen 7 9850X3D.](https://cdn.mos.cms.futurecdn.net/Xh2MupWrRjJPiLLuopmKRB.jpg) 


The page fetches ascii-city-engine_bg-DqjAhqbp.wasm, a 283KB module that reserves 1,152KB of linear memory at startup and reports an engine version of 0.1.0 when instantiated outside the browser. Its exports include initialise_native_game, step_native_game, and generate_native_local_map. Debug paths left in the binary name the Rust source modules behind those calls: city.rs, world.rs, population.rs, interiors.rs, and rendering.rs. World generation runs in Rust, which hands JavaScript base64-packed byte arrays covering building heights, tile kinds, surfaces, hues, saturations, window styles, lit flags, and floor plan IDs.

The renderer requests a WebGL context and compiles a vertex and fragment shader pair, the fragment stage consisting of a single texture2D lookup. Characters are drawn once each into an atlas canvas with fillText, cached per character-and-color combination, uploaded to the GPU with one texImage2D call, and then drawn as textured quads with six vertices apiece.

![A Walkable ASCII Cyberpunk City in One HTML File - YouTube](https://img.youtube.com/vi/3YtygAx_C6A/maxresdefault.jpg) 

Atlas cells measure 11 pixels tall by the monospace advance width plus two. Every visible cell goes into one buffer upload, and one drawArrays call per frame. Two fallbacks sit beneath this, a Canvas 2D drawImage path when WebGL is unavailable, and a per-cell fillText path reachable through a ?direct URL parameter.

Desktop sessions render 180 columns by 80 rows, or 14,400 character cells, in 10px Consolas at nine pixels per row. Touch devices drop to 48 rows and between 96 and 168 columns, and the Rust engine uses a separate 160 by 112 profile. The vertex buffer preallocates 2.76MB and doubles when a frame overruns it.

Grow Now! Games described the original demo to *PC Gamer* as having "no Unity, there's no Unreal, there's no 3D models, textures, or shaders." A first-person Backrooms game for the 1994 Sega 32X runs on a raycasting engine written from scratch in C and SH-2 assembly. A multiplayer Doom tribute implements raycasting and sprite projection as a stack of SQL views, reaching roughly 30 FPS at 128 x 64. Thunder Lizard, an ASCII roguelike, has had its character grid redrawn by image models into full-motion visuals at around 10 FPS.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Luke James](https://cdn.mos.cms.futurecdn.net/C4FAi2KzwaGLUrBqzX5aBM.png)

Luke James is a freelance writer and journalist. Although his background is in legal, he has a personal interest in all things tech, especially hardware and microelectronics, and anything regulatory.
