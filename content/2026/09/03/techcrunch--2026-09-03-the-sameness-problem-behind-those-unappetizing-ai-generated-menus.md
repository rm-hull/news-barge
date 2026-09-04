---
title: The sameness problem behind those unappetizing AI-generated menus | TechCrunch
source_url: https://techcrunch.com/2026/09/03/the-sameness-problem-behind-those-unappetizing-ai-generated-menus/
source_site: TechCrunch
source_slug: techcrunch
scraped_at: '2026-09-04T04:22:39Z'
published: '2026-09-03T00:00:00Z'
description: While restaurant owners might look to generative AI as a shortcut to
  sprucing up their menu, customers can viscerally sense that something is wrong with
  the food.
image: https://techcrunch.com/wp-content/uploads/2026/09/Firefly_gpt-image_rename-the-restaurant-crunchburger-and-use-a-green-color-palette-509807.png?resize=805,1200
---

When it first happens to you, you think you’re crazy. You wander into a cafe and look at a menu with a variety of bagel sandwiches, but each illustration looks eerily flawless, precisely symmetrical, and oddly smooth, eliciting a visceral sensation that something isn’t right. You might think you’re paranoid, but you’re not losing your mind. Generative AI menus have hit the restaurant business courtesy of models courtesy of models trained on a narrow, “pleasing” aesthetic that produces a look that feels wrong even when you can’t articulate why.

Sometimes, these illustrations are egregiously fake, like a burrito with cheese so bubbly and melty that it looks more like avant garde art than lunch. More often, they’re so ordinary looking that you only notice something is wrong when you take a second to look more closely.

“It’s almost like an alien trying to make a pizza without understanding its core principles,” Reality Defender CTO Alex Lisle told TechCrunch. (Reality Defender itself is part of a growing category of startups selling AI-detection and content-verification tools — a business that exists in part because of issues like this one.)

Lisle says that the way these models are built can help explain why illustrations seem to embrace such a specific aesthetic — one where every ice cream scoop is perfectly round, and where shrimp seem to have been genetically modified to eat their own tails, creating new “Lovecraftian food horrors.”

Large language models (LLMs) and diffusion models — the kinds of AI models that make seemingly omniscient chatbots and image generators like ChatGPT and Midjourney possible — are trained on vast quantities of data. The models then identify patterns in the datasets to predict what a user is looking for when they ask something like, “Make me a menu for a burger restaurant.”

“A lot of this stuff looks like a Chili’s menu from 2015, and there’s a reason for that,” Lisle said. “That was the corpus of work from which [the models] drew their function.”

![](https://techcrunch.com/wp-content/uploads/2026/09/Firefly_gpt-image_rename-the-restaurant-crunchburger-and-use-a-green-color-palette-509807.png?w=456)

**Image Credits:** ChatGPT Image 2.0

New training data is invaluable to the companies building AI models — Amazon has even been found to source rare books to scan and add to its training data, only to destroy those books once they’ve been uploaded. It’s inevitable that some AI-generated content will seep into these incomprehensibly large data sets. But when AI models train on too much of their own AI-generated content, they risk model collapse.

“Model collapse is almost like a mad cow disease… when you feed the outputs from one model back into itself, eventually the inbreeding becomes too much, and the whole thing collapses,” Lisle explained. “What we see here is convergence, which isn’t necessarily model collapse.”

Convergence is a bit less extreme, degrading the quality of an AI’s outputs without making it entirely useless.

If someone asks an AI model to generate a menu for a fast food restaurant, the model will likely reference menus from Wendy’s, Burger King, McDonald’s, or another popular chain. These menus already share a similar style, which means that the AI-generated outputs will mimic that same style, only to further reinforce it further if the AI-generated menu ends up back in training data.

But menus and advertisements for food will always look better than the real thing, like a Big Mac in a McDonald’s commercial where each layer of the sandwich is arranged by a prop designer to look maximally appetizing. This effect can become even more pronounced in AI outputs.

“The optimization of the data sets is for pleasingness, or you know, not being offensive, and so there’s a way that turns into homogenization,” Lee Rainie, Director of the Imagining the Digital Future Center at Elon University, told TechCrunch. “What AI is known to do both in images and language is to shave off the edges.”

On a more localized scale, this smoothing of images seems to happen when you use an AI image generator to create a menu and apply edits to it. On X, a user named Labtec showed what happens when you make a menu in ChatGPT, then edit it 100 times to see how the food continues to look less and less like it should. (We replicated the experiment and found similar results.)

“The end result actually makes me uncomfortable,” Labtec wrote.

Restaurants are likely falling victim to this problem, revising their AI-generated menus to alter small details over and over, like prices or item names. It seems that with each edit, the food images become a tiny bit more round and smooth.

“People have an almost unexplainable sense about when they’re looking at something that’s AI-generated, compared with something that was real in the first place,” Rainie said. “There’s just a sensibility that people sometimes find hard to articulate, but they kind of know it when they see it and I think that’s one of the reasons why some of the early stories about the backlash [against restaurants using AI menus] is so pronounced.”

There’s science behind our aversion to these AI menus. Researchers at the University of Duisburg-Essen in Germany found that AI-generated food images exhibited an “uncanny valley” effect, where images of food that looked almost real elicited more disgust and unease than images that were obviously fake. That squeamishness only intensifies in light of the cultural context around AI.

If people react to these images so negatively, then that’s probably reason enough for restaurants to stop trying to make AI menus work. But the issues that bring us perfectly browned hamburger buns extend beyond the dinner table.

“Seeing and hearing has always been believing, to the point where even our court systems are entirely tuned to the idea that the gold standard in evidence is taped confessions and videotaped evidence,” Lisle said. “That’s no longer the case. The world has fundamentally shifted, for good or for ill.”
