---
title: Fable 5.2 creates an underwater world in a browser in only 96 KB — 40-line
  prompt creates impressive demo that runs at 180 FPS
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/fable-5-2-creates-an-underwater-world-in-a-browser-in-only-96-kb-40-line-prompt-creates-impressive-demo-that-runs-at-180-fps
source_site: Tom's Hardware
source_slug: toms-hardware
description: Fable 5.2 creates an underwater world in a browser in only 96 KB — impressive
  demo shows how far agent agency has come
image: https://cdn.mos.cms.futurecdn.net/nXAFaumdgwqSTyXixK2UK9-2560-80.png
published: '2026-11-16T00:00:00Z'
scraped_at: '2026-11-16T19:36:26Z'
categories:
- Technology & Software
- Hardware
people:
- Bruno Ferreira
- Fable
- Hartverdrahtet
- Maksymilian Dendura
- Tom
locations: []
organisations:
- AI
- Get Tom's Hardware
- Google News
- PC
- Tom's Hardware
- WebGPU
- iGPU
---

![Abyssal Garden demo](https://cdn.mos.cms.futurecdn.net/nXAFaumdgwqSTyXixK2UK9-1920-80.png)

Claude Fable 5.2 was released recently to mostly rave reviews, with both users and analysis outlets ranking it nipping at the heels of the much pricier Opus 5.5. Perhaps as practical proof of that claim, front-end developer Maksymilian Dendura took inspiration from the demoscene and had Fable roll his own virtual underwater world, *Abyssal Garden*, in only 96 KB of Javascript/HTML — you can check it out here.

The demo's 3D space and textures are all procedurally generated, meaning they're the result of mathematical equations rather than prebuilt 3D meshes, and all calculated on load. Using actual meshes and images for textures would otherwise take up a significant amount of space.

Building structures procedurally is difficult and has limitations, but it's exceedingly effective when used properly. Some games employ this technique for repeated elements like trees and grass.

Likewise, all the visual effects and even some texturing are done with shaders, which are small programs that change how a mesh or texture appears — for example, to make parts of an object shiny. Games use them extensively, as many players are aware, thanks to endless "loading shaders" screens or Unreal Engine's st-tu-tutering.

The result is definitely impressive, especially but not only as it's purely browser-based, relying on WebGPU and WebGL. Both are rarely-mentioned technologies that have actually existed for a long while now. As their names imply, they let developers render 2D and 3D graphics in a manner similar to that of OpenGL, but in a browser, using JavaScript as the base language.

The demo's most impressive fact is the simplicity of the prompt that got Fable 5.2 to build it. It's only about 40 lines long with word wrapping, and clearly illustrates the degree of autonomy that contemporary agentic AI has when given a specific, yet exceedingly open-ended task like this one. It's reasonable enough to assume the author did a few rounds of tweaking (and he has excellent artistic taste too), but the agent's acumen is nevertheless impressive.

Comparing this demo to an actual game is inevitable, but the reality is that demos have but an atom-sized fraction of the content of a full game, and are limited to little or no interaction, logic, or physics.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Performance is decent for what is a great-looking but otherwise tiny and almost featureless space. The author says that he's getting 180 FPS at 1440p on an RTX 5070 Ti. Likewise, having this world in 97 KB sounds impressive, but it's actually gigantic for this type of demo, even if an X user further optimized it for 52 KB.

Regular computing users, including AI neophytes and acolytes, may not be aware that this kind of space-optimized programming for the purposes of visual/aural demonstrations is a discipline and art form that harkens back to the 1980s when 16-bit computers appeared — called the "demoscene."

By no means discounting the extraordinary fact that Fable did this nearly all by itself — which is the actual achievement here — code wizards have pulled off nearly impossible feats decades ago, including in browsers. The 2009 demo Elevatedn (17 years ago) has a comparable aesthetic, and includes music, in just under 4 KB (yes, four). There's even a browser version of it, taking up all of 4,777 bytes.

Hartverdrahtet (2012 — 14 years ago) has a highly complex 3D space, again in 4 KB. And old-timers in the audience will remember ".kkrieger", an FPS game prototype that fit in all of 96 KB, including meshes, textures, music, and sound effects... back in 2004.



*Download the Tom's Hardware app for up-to-the-minute updates on* * iOS* * and* * Android**. Also follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G-140-80.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.

* > The result is definitely impressive, especially but not only as it's purely browser-based, relying on WebGPU and WebGL. Both are rarely-mentioned technologies that have actually existed for a long while now.

  WebGPU is new.  
    
  It gave my iGPU a workout but maintained 60 FPS at a 720p-ish resolution on the lowest detail setting. I expected worse but it worked quite well. Reply
