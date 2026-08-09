---
title: Mind-bending self-replicating GIF code prints an exact copy of itself, is both
  a program and its own visual output — champion coder shows off 'Piet Quine' technique
source_url: https://www.tomshardware.com/software/programming/mind-bending-self-replicating-gif-code-prints-an-exact-copy-of-itself-is-both-a-program-and-its-own-visual-output-champion-coder-shows-off-piet-quine-technique
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-09T13:11:07Z'
published: '2026-08-09T00:00:00Z'
description: The GIF is both the code and the precise result from running the code.
image: https://cdn.mos.cms.futurecdn.net/ssqoE4QEPXAiApwKP3R6BG-1920-80.jpg
---

![a Piet Quine](https://cdn.mos.cms.futurecdn.net/ssqoE4QEPXAiApwKP3R6BG.jpg) 

Champion coder Yusuke Endoh has been flexing their esoteric programming muscles on social media. Their latest confection is a Piet Quine – a GIF image that prints itself. In other words, the GIF is both the code and the precise result after running the code.

If you haven’t quite grasped the enormity of this feat from the title, it is worth breaking down the respective definitions of both Piet and Quine in a computer programming context. Piet is an esoteric programming language in which programs look like complex, colorful, tiled artwork. Inventor David Morgan-Mar named it after Piet Mondrian, the famous founder of the neoplasticism artistic movement. Such artwork is immediately recognizable with its bold squares and rectangles bordered by heavy black lines. Smaller Piet GIFs look a bit more Mondrian-y to me, but also look more like colorful QR codes than paintings.

![A quine in Piet — a GIF image that prints itself - YouTube](https://img.youtube.com/vi/GwMtzhjCzyc/maxresdefault.jpg) 

Endoh has created a Quine, graphically. In computer coding, a Quine is a program that produces a copy of its own source code without any external input. This can be quite a tricky feat, even when confined to the world of ASCII text. A requirement of this coding art is that the output is a character-for-character identical representation of the input. It must not simply read its own file to do the duplication task.

When merging the two ideas above, together, things get a whole lot more complicated. However, the top-linked blog and the embedded video shine a light on the task at hand and how Endoh succeeded. Specifically, the video shows Piet Quine running. The Piet interpreter scans the source GIF image in a ‘load data’ phase, followed by a read of the GIF file header and palette info. The challenge here, raising the task above text Quines, is that the GIF folds in binary data, compression, and an awkward flow – they must all be handled deliberately to end up with the desired result.

A key thing to understand about the source image is that it includes a separately interpreted data part, compressed with an adaptive run-length encoding, and a code part. Endoh says that they managed to actually first achieve this way back in 2009, but the GIF was very tall, so not ideal for visual appreciation. The developer decided to ask Claude Code to analyze and reconstruct the original script and build a ‘landscape’ Piet Quine. Even with AI's help, it wasn’t easy to refine the design to the compact finished GIF seen in this article and video. Only after much work on shrinking the visuals and coaching Claude was the GIF shoehorned into the finished 4:3 landscape image (252 x 189 pixels).

Finally, Endoh reveals that a driving force behind their Piet Quine development efforts was the wish to raise awareness of the 2026 Obfuscated Programming Language Design Contest, which is running right now. If you can, please design an esoteric programming language and submit it! Endoh is one of the judges, and you have until October 1 to make your submission(s).

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Mark Tyson](https://cdn.mos.cms.futurecdn.net/56vqMYLDaKRHPhHZgbADFR.jpg)

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.
