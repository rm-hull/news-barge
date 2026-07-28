---
title: Daring coder gets Doom running with regular expressions at 180 seconds per
  frame, like playing 'correspondence chess with a shotgun' — nearly 14 million substitutions
  to render a frame at 80,000 substitutions per second
source_url: https://www.tomshardware.com/software/programming/daring-coder-gets-doom-running-with-regular-expressions-at-180-seconds-per-frame-like-playing-correspondence-chess-with-a-shotgun-nearly-14-million-substitutions-to-render-a-frame-at-80-000-substitutions-per-second
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-28T10:45:12Z'
published: '2026-07-28T00:00:00Z'
description: He definitely thought he could, but not whether he should.
image: https://cdn.mos.cms.futurecdn.net/NT3tYSnYPbRPpA4C7RXrxY-1152-80.png
---

![Doom in regular expressions](https://cdn.mos.cms.futurecdn.net/NT3tYSnYPbRPpA4C7RXrxY.png) 

Running the 1992 Doom on the most random piece of hardware around has become probably the most common unofficial programming challenge. We've seen the game running on anything from toasters to an Anker charger, and even a pregnancy test. Enterprising coders also get it running on the weirdest software possible, and just recently Artem Lytkin got it running in regular expressions.

Developers in the audience are probably recoiling in horror, as that sentence is *definitely* cursed. You see, regular expressions (regexes) are a utility language used in programs for finding and replacing text. They're incredibly powerful, but the syntax is often said to be write-only, as it looks just like gibberish. For example,**/.*(\d{4}).*/g**would find the "2026" in "* Tom's Hardware* 2026 articles." They can be exceedingly complicated, as they include conditional statements, elaborate character-jumping, and substitution rules. However, this also means they fulfill all the technical requirements to be a programming language.

Leveraging those capabilities, Lytkin created a 96 MB plain-text string that contains sections for the virtual CPU's registers, some RAM, a video output (framebuffer), the game's WAD data, plus I/O and other bits and bobs. Once it's all started, the regex will start text-matching and substituting characters in the string to pretend they're the numbers in each processor's register, then accessing and writing to the "memory," so on and so forth.

As you can imagine, this is spectacularly slow, and Lytkin says that it takes around 180 seconds to produce a single frame of game output. Each of those needs nearly 14 million substitutions, though (a) it actually works and (b) Lytkin claims it's byte-identical to the actual *Doom* output running. You can even control the game with the keys, but as the daring coder poignantly illustrates, playing it "is closer to correspondence chess with a shotgun than to a twitch shooter."

Particularly nerdy devs will be happy to know how Lytkin wrote the memory access part: essentially a binary tree, by jumping from "branch" to branch using standard regex character-jump instructions. This avoids having to scan the entire 96 MB of text repeatedly just to find the "#M" marker bookending it. Lytkin notes the challenge was not about whether it could be done, but whether the game would run "before the heat death of the universe," as the engine fires up 80,000 text substitutions *per second*.

The doom-regex repository is here, and you can download a demo to run it on your own computer. The project's website demonstrates how the regex machine runs in both visual and text format, and it's mesmerizing to watch. It's quite reminiscent of the time we spent watching defragging utilities do their thing when we were young'uns.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.
