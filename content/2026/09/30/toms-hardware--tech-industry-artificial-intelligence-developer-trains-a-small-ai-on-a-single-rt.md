---
title: Developer trains a small AI on a single RTX 3080 Ti gaming GPU to 'play' Pokémon
  Red — model discovered what each button does by predicting what happens next
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/developer-trains-a-small-ai-on-a-single-rtx-3080-ti-gaming-gpu-to-play-pokemon-red-model-discovered-what-each-button-does-by-predicting-what-happens-next
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-30T18:02:12Z'
published: '2026-09-30T00:00:00Z'
description: The model is small enough to train on a gaming PC's graphics card.
image: https://cdn.mos.cms.futurecdn.net/Ze4EWJD7UaZefKeV6pAzJ4-2560-80.png
categories:
- Technology & Software
- Hardware
- Video Gaming
people:
- Squirtle
- Stmonty
- Tom
- Yann LeCun
locations: []
organisations:
- AI
- AMI Labs
- Get Tom's Hardware
- GitHub
- Google News
- LeWorldModel
- Meta
- Shane Downing
- Tom’s Hardware
---

![Nvidia GeForce RTX 3080 Ti Founders Edition graphics card on a reflective black surface](https://cdn.mos.cms.futurecdn.net/Ze4EWJD7UaZefKeV6pAzJ4-1920-80.png)

A developer who goes by the name “stmonty” has trained a small AI model on a single RTX 3080 Ti to play Pokémon Red. The developer’s blog post, “Teaching a World Model to Play Pokémon,” details the journey of training a model working from a save to pick a starter. The model is what is known as a world model, built off of LeWorldModel research co-authored by famed AI scientist Yann LeCun. LeCun split from Meta last year to build world models with his AMI Labs, using the same approach.

This particular one was trained with only about 12.5 million parameters and written up on Sept. 20. On a discussion forum, stmonty called the project a way “to learn and have some fun,” and chose the model because it could be trained locally on a consumer-grade graphics card.

The model has to learn what each button press does, and it does this by looking at the screen that’s produced. Rather than predict the entire next screen, it uses compressed summaries with just 192 numbers. The initial training is “reward-free” in the sense that the model is not aware of winning conditions. Goals come later, when the model plans. This design follows a March 2026 paper detailing a single JEPA model with about 15 million parameters, trainable on a single GPU, not that far different from stmonty’s.

The full training run required 42,382 grayscale frames in over 1,000 short runs, using a save in Professor Oak’s lab. The data included scripted routes, those same routes with random presses mixed in, and random wandering. The last part is necessary because a model trained only on clean runs “might see A pressed whenever a dialogue box appears and never learn what B does there,” said stmonty. The model was trained from scratch for the project.

Plans are developed with 14 button presses and attempted in the model, not the game. Each round has 512 plan samples where the search keeps one in eight, or 64. This continues until the final plan is the one run in the game emulator. Stmonty hypothesizes that one possible cause of the failure, which left the player without a Pokémon, is that small errors compound when predictions are made from the model’s own predictions.

The next attempt, after some fine-tuning, came back a success with the model selecting Squirtle. Then, over 100 runs from the same save, there were 52 plans that got a starter, compared with zero for random button presses and just one with an untrained model. Stmonty stated that pressing A repeatedly already works from the save; the model discovering the solution on its own was the goal. This is still a modest result but does demonstrate that small models can be tailored to specific tasks.

The next goal, which the developer “may still try,” is to start in the lab, walk to the Professor, get through the dialogue, then actually pick a Pokémon. “I suspect that difficulty scales exponentially with plan length,” the developer said. Making the model large enough would probably not lead to the game being beaten: “I don’t think simply making my current model bigger would get us there,” the developer stated in a reply.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

The small model approach to playing Pokémon Red is one of many in recent weeks, with at least two separate, and successful, attempts to beat the game using the Jev decision model and a harness or custom code. Those use more sophisticated approaches, however, while small models remain a realistic option for hobbyists. The project’s code is open source and available on GitHub as lePokeRed, with a CUDA GPU recommended.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Shane Downing](https://cdn.mos.cms.futurecdn.net/Zosi9VrDytS9FkgJiHvc69-140-80.png)

Shane Downing is a Contributing Writer for Tom’s Hardware, covering consumer storage, PC hardware, and AI.
