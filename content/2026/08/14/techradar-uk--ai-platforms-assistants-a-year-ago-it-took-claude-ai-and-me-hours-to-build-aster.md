---
title: I used Claude AI to build a Breakout clone in five minutes — and you can play
  it
source_url: https://www.techradar.com/ai-platforms-assistants/a-year-ago-it-took-claude-ai-and-me-hours-to-build-asteroids-we-just-built-a-breakout-clone-in-five-minutes-and-you-can-play-it
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-14T13:34:18Z'
published: '2026-08-14T00:00:00Z'
description: I wanted to see if Claude was functioning properly, so I asked it to
  build a game from scratch. The speed at which we completed the task blew my mind.
image: https://cdn.mos.cms.futurecdn.net/JWYmqbKpjr3MjmisUZry43-2000-80.jpg
---

![Claude Gearbreaker](https://cdn.mos.cms.futurecdn.net/JWYmqbKpjr3MjmisUZry43.jpg) 

I didn't set out to build a Breakout clone, but that's what I — or really Claude, under my direction — did, and it took less time than it takes to watch a half dozen cat videos.

Here's how it started. Claude was having issues. Anthropic's powerful and popular generative AI platform was apparently going up and down, and some were complaining, but when I checked, Claude told me, "I'm doing well, thanks for asking!" I realized, though, that if the problems were intermittent, I might need a tougher task to test Claude's overall stability.

More than a year ago, I worked with Claude, or rather guided Claude through the process of recreating the early 1980s arcade game classic: Asteroids. The final game, which Claude exported as a shareable artifact, was the product of hours of guidance and back-and-forth between me and the AI. It didn't start off great, but with each prompt, we iterated, and the game improved until I had a rather robust and true-to-the-original Asteroids knockoff.

With that in mind, I tasked Claude AI, running the free Sonnet 5 model at "Medium" level, with creating a Breakout clone.

## Breaking out

Breakout is one of my favorite games, something I've played on early consoles, PCs, and even my old BlackBerry, where "Brick Breaker" was one of the few preloaded games.

The game rules are pretty simple. There's a multi-level brick wall (usually eight bricks deep) at the top of the screen, a paddle at the base, and a bouncing ball you bounce off the paddle to break down the brick wall.

For my prompt, I tried to describe, in some detail, my game, and was not coy about it being an online version of Breakout:

Sign up for breaking news, reviews, opinion, top tech deals, and more.

*Let's make a quick game. I want an online version of the old Breakout game, but let's replace the bricks with robots that are always slowly marching down toward you (if they reach you, it's game over). The ball that you bounce off your side-sliding controller is a gear that breaks up the robots easily in the first level. In the second level, the robots are shinier and harder, and the gear takes three or more hits to break and make a robot disappear. If you clear the level, the gear turns into a titanium ball that bounces faster but is more powerful. Controls are either keyboard/arrow based and mouseable. Want this to result in a web-based, shareable game, so a link/artifact I can share online.*

 ![Claude Gearbreaker](https://cdn.mos.cms.futurecdn.net/f23W2zfH3ypKs6xtkcaGGB.png) 


That's all the direction I gave it. I didn't describe colors, the initial speed of the ball, or even how quickly the robots would march down the screen. I didn't get into details about the look of the robots, instead relying on generalities and some material descriptions to help guide Claude.

It took me a minute or two to write the prompt and around three minutes for Claude to deliver the results, which it cleverly called "Gearbreaker".

I got a brief description of gameplay and levels (there are just two for now) :

*"How it plays:*

**Level 1***— matte robots, one hit each from the spinning gear ball. They march downward on a timer; let them cross the dashed red hazard line and it's instant game over.*

**Level 2***— shinier robots (metallic gradient, cyan eyes) that soak up 3 hits, shown as pips along the bottom of each unit. Same gear ball, tougher targets.*

**Clear level 2***→ the ball forges into a***titanium core***: bigger, faster, hits for 2 damage instead of 1. Levels keep scaling procedurally after that (more rows, faster march, tougher units), so it runs endless with a local high-score save.*

**Controls***: arrow keys or mouse to slide the paddle, Space or click to launch/pause/restart. Basic touch support too."*

On the right side of the screen, there was my playable game. There's also the artifact publish button, which I chose to use so I could share the game with you.

It's a stunningly complete render of a completely playable and, in some ways, challenging Breakout clone, and it took five minutes. I'd call the design clean and efficient. The bricks have a robot look, and the ball is a blue spinning gear (in the first level). The movement and physics are basically perfect, and there's enough on-screen instruction to easily grasp gameplay.

## Just the beginning

 ![Claude Gearbreaker](https://cdn.mos.cms.futurecdn.net/Ww3v6Kwf4ztAn7R4FQtJ8B.png) 


It's just another mind-boggling example of the incredible pace of AI development. While I had expected a playable game, I assumed it would be missing enough crucial components to make it dull or uninteresting — something similar to my earlier AI game development projects. Instead, I got something that displays a clear understanding of the purpose of such a game: challenge, entertainment, and replayability.

Using my mouse, I played through a couple of times, failing to break all the bricks in Level One and ending the game. I realized I had to take Claude's output more seriously, and, with some effort, as I watched the robot bricks steadily march down my screen, I finally cleared all the bricks in Level One and then started in on the tougher Level Two. As I had instructed, the robots on the second level looked and reacted differently. It now took at least three direct hits to make them disappear. I failed and already want to play again.

![Gearbreaker](https://cdn.mos.cms.futurecdn.net/cbcBTmKWkag96Y7oDyRSVA.gif)


This is by no means the wildest example of the AI development process or vibe coding; it's just me prompting Claude to code a complete game with the barest of instructions.

Claude and these models cannot do this on their own, but it does make you think about the agentic AI that's now being unleashed on the world. It's more powerful and autonomous. I could imagine someone asking one to start work on recreating all the popular video games of the last half century. The only limit would be time and compute tokens.

Speaking of which, Claude just informed me that this Breakout task used up about 90% of my credits for the day. I think it was worth it.

Take the game for a spin and let me know what you think in the comments below.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Lance Ulanoff](https://cdn.mos.cms.futurecdn.net/6Wh5hw6gxNa22teaor9Pdn.png)

A 38-year industry veteran and award-winning journalist, Lance has covered technology since PCs were the size of suitcases and “on line” meant “waiting.” He’s a former Lifewire Editor-in-Chief, Mashable Editor-in-Chief, and, before that, Editor in Chief of PCMag.com and Senior Vice President of Content for Ziff Davis, Inc. He also wrote a popular, weekly tech column for Medium called The Upgrade.

Lance Ulanoff makes frequent appearances on national, international, and local news programs including Live with Kelly and Mark, the Today Show, Good Morning America, CNBC, CNN, and the BBC.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
