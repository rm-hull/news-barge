---
title: Player builds working AI chatbot in vanilla Minecraft using 445K command blocks
  — clever approach shrank initial block count from over 1 million, requires no mods,
  plugins, or datapacks to work
source_url: https://www.tomshardware.com/video-games/minecraft-creator-works-around-in-game-math-limitations-to-implement-an-llm-using-445k-command-blocks-clever-approach-shrank-initial-block-count-from-over-1-million-requires-no-mods-plugins-or-datapacks-to-work
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-19T13:10:18Z'
published: '2026-08-19T00:00:00Z'
description: Hopefully they didn't have to buy extra RAM for this.
image: https://cdn.mos.cms.futurecdn.net/BGkNLt7nZdYAUhzj84X62d-1817-80.png
---

![LLM in Minecraft](https://cdn.mos.cms.futurecdn.net/BGkNLt7nZdYAUhzj84X62d.png) 

Anyone who's played Minecraft for a while is familiar with community creations like in-game graphing calculators, QR code generators, and Tetris games built using command blocks, mods, and far too much free time. Building AI tools is a logical next step, and several complicated projects have arisen in that vein using redstone. Reddit user Objz, however, implemented an LLM using only 445,782 command blocks and no mods, plugins, or datapacks. By its creator's description, the project was "a headache."

Objz's LLM isn't actually that large. It only has a 64-dimensional embedding space, a 256-neuron hidden layer, and a tiny vocabulary of 2,048 words, and was trained on 11,118 DailyDialog conversations. Users can talk to it using the game's "/dialog" functionality, and the output stream comes back one word at a time, as with typical chatbots.

Even with that training, however, the author notes that this LLM is only conversational and isn't particularly clever, as it cannot do math and has no broad knowledge.

Even still, the work on display is quite impressive. 445,000 command blocks sounds like a lot until you realize that this kind of data and computational structure would require literally millions of cubes were it not optimized. Indeed, the original version, even with the aforementioned capabilities, rang in at nearly 2 million blocks. LLM weights are normally represented with floating-point values, which would be prohibitively complicated to implement, so Objz opted to use only ternary values for the weights: -1, 0, and +1.

Minecraft's "scoreboard" command supports multiplication and division, but it's integer-based, and using it would require integer-float conversion, thus adding extra operations. The initial quantization to -1/0/+1 kills two zombies with one stone, skipping commands and shrinking the dataset. The equivalent of each multiply-accumulate operation, then, averages 0.67 commands thanks to all the null values.

Objz notes that they didn't just round off the values from a normal model after the fact to achieve this ternary representation. The creator quantized them from the get-go for the forward pass through the model during training and used a straight-through estimator during backpropagation to update the underlying floating-point weights. That step helped lower the perplexity rate (roughly, how likely a model is to produce a nonsensical word in a response sequence) from 48.7 to 38.8 after some additional optimizations.

Given Minecraft's limits on how many commands it can execute at once, the LLM is split into smaller groups, and even then, it takes about 1.8 seconds to generate each word in a response on a 35-tick-per-second server. The author remarks that making this LLM bigger and smarter would be a computationally costly affair, as even a 135-million-parameter LLM built using this architecture would be a whopping 200x larger than this project. But it's a clever example of how constraints spur creativity.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.
