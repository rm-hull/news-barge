---
title: Oblivion gamer uses Claude AI to boost average FPS gains up to 48%, stutters
  slashed by 90% — performance mod doesn't change game assets or alter visuals
source_url: https://www.tomshardware.com/video-games/pc-gaming/oblivion-gamer-uses-claude-ai-to-boost-average-fps-gains-up-to-48-percent-stutters-slashed-by-90-percent-performance-mod-doesnt-change-game-assets-or-alter-visuals
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-20T14:23:10Z'
published: '2026-10-20T00:00:00Z'
description: Yes, this mod is just about 100% vibe-coded.
image: https://cdn.mos.cms.futurecdn.net/jZKXZNanDyqWYzFxNBfimL-1920-80.jpg
categories:
- Technology & Software
- Hardware
- Video Gaming
people:
- Claude AI
- Tom
- Virtuos
- Zak Killian
- Zen
locations:
- Bethesda
organisations:
- AI
- AMD
- Anthropic
- Bethesda
- Gamebryo
- Google News
- HotHardware
- LTSharpe
- PC
- Remaster
- Starfield
- The Tech Report
- Tom's Hardware
- Zak
---

![A screenshot from LTSharpe&#039;s flyby video showing massive performance gains in TES4: Oblivion Remastered.](https://cdn.mos.cms.futurecdn.net/jZKXZNanDyqWYzFxNBfimL-1920-80.jpg)

The revelation that there was a ton of performance lying on the table in the remastered *The Elder Scrolls Part IV: Oblivion* won't be a surprise to people who have played the game, which is notorious for its hitching and stuttering. The reason primarily lies in its poor utilization of hardware, and that's a big part of what LTSharpe and Claude have addressed in the new Oblivion Remastered Performance Fix that changes nothing about the game's visuals yet increases performance by as much as 68% in the worst case. (h/t to*ComputerBase*)

Yes, this mod is just about 100% vibe-coded, and yet, rather than hacking Minecraft into GTA V on iPhone, or hacking CoD Black Ops 2 maps into Minecraft, this mod is a binary code modification for *Oblivion Remastered* that seeks to improve performance and stability considerably, and according to numerous jubilant and thankful posts on NexusMods, it seems to do exactly that, with one user proclaiming that the performance increase was "dramatic" and that the overworld stuttering that plagues the game is "completely gone."

![An image with benchmark graphs showing the original Oblivion game&#039;s performance versus the performance-modded game.](https://cdn.mos.cms.futurecdn.net/cEUamqkefYRAaztLjcY2XH-1000-80.png)

The story goes like this: gamer and mod creator LTSharpe has a slightly older system with a Ryzen 7 5800X CPU. Not the newest chip on the block to be sure, but Zen 3 isn't so old that it should be crumpling under the weight of games just yet. Frustrated with the verifiably awful performance of the remaster of *The Elder Scrolls Part IV: Oblivion*, he paid for a subscription to Anthropic's Claude AI agent and started working with the assistant to diagnose and fix the performance problems.

"Diagnose" is a critical keyword here, because it isn't like Claude was hallucinating an engine.ini tweak somebody else published for the original game 20 years ago. The partners, with Claude doing the hard work and LTSharpe directing, reverse-engineered the game to the point that they were able to build a repeatable benchmarking framework. That allowed them to systematically diagnose the causes of the performance problems and then test fixes against the real behavior of the game with modified machine code.

![Oblivion Remastered Performance Fix - YouTube](https://img.youtube.com/vi/K8WkCz6cuHk/maxresdefault.jpg)

That's the thing; this was done without source code. Neither *TES4 Oblivion* nor the remaster's Unreal Engine is open-source software. The sheer magnitude of the task would be incredibly daunting to a team of human engineers, much less a single person. According to LTSharpe, over the course of two weeks Claude successfully diagnosed and fixed bugs in not only the Remaster's Unreal Engine code, but also in the underlying Gamebryo original engine, in AMD's frame generation code, and even in the Unreal Engine itself, improving performance and avoiding crashes.

The developer—or perhaps we should say, coordinator?—is careful to acknowledge that the performance tweaks were created with his system specifically in mind and that they may not work well for others. Indeed, he has a Radeon graphics card, which puts him within a surprisingly small minority of PC gamers, and some portion of his fixes were aimed at making sure AMD's FSR upscaling and frame generation remain in effect despite a long-standing game bug that disables them when you task-switch (Alt+Tab) out of the game. The good lieutenant invites other gamers to try out the fix and report back, and he's even helping out with support requests on NexusMods, too. Head over there if you're keen to grab the fix and try it for yourself.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Zak Killian](https://cdn.mos.cms.futurecdn.net/yonJziSpjzVFahKcUonJvi-140-80.jpg)

Zak is a freelance contributor to Tom's Hardware with decades of PC benchmarking experience who has also written for HotHardware and The Tech Report. A modern-day Renaissance man, he may not be an expert on anything, but he knows just a little about nearly everything.

* This is a more positive use of AI in gaming. I remember reading how Rollercoaster Tycoon was written in low level code and was one of the most optimised games ever made. I'm still waiting for that kind of development.Reply
* wussupi83 said:When AI slop meets beta quality production code slop. Maybe two wrongs can make a right?There's something about Bethesda games (I know Virtuos was involved with Oblivion Remastered)... the change in Starfield was also cited as impressive in some of the initial DLSS 5 reactions. Reply
* Imagine if Bethesda with full access to the code actually took the time to fix their games, now that’d be a real shock.  
    
  I love most Bethesda games but they never work right until people other than bethesda have had a year or two to fix all the issues. Reply
