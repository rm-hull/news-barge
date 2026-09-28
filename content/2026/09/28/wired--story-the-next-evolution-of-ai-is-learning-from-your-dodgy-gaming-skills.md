---
title: The Next Evolution of AI Is Learning From Your Dodgy Gaming Skills
source_url: https://www.wired.com/story/the-next-evolution-of-ai-is-learning-from-your-dodgy-gaming-skills/
source_site: Wired
source_slug: wired
scraped_at: '2026-09-28T14:00:08Z'
published: '2026-09-28T00:00:00Z'
description: A British startup is shaping video game inputs into training data for
  AI models that can navigate the physical world.
image: https://media.wired.com/photos/6ab2c77aa4511820fe187b66/191:100/w_1280,c_limit/People-Training-AI-to-Understand-Physical-World-With-Video-Games-Business.jpg
categories:
- Technology & Software
- Science
- Video Gaming
people:
- Fei-Fei Li
- Ming-Yu Liu
- Nicole Fraenkel
- Rhea Loucas
- Xiatian Zhu
- Yann LeCun
locations: []
organisations:
- AI
- GPT
- General Intuition
- Khosla Ventures
- LeCun
- Niantic
- Nvidia
- University of Surrey
- VC
- WIRED
- Worldmodeldata
---

With the twirl of a thumbstick, squeeze of a trigger, and press of a few buttons, even an unskilled player can dance their way through a 3D video game environment. A British startup is wagering that straightforward sequences like these contain a trove of information that can be used to train new artificial intelligence models.

There is a growing belief in corners of the AI industry that large language models will ultimately be limited by their inability to navigate the physical world. Trained only on words, LLMs are perhaps ill-equipped to pilot autonomous vehicles, steer robotic arms, or perform any other action that requires finesse and precision. To remedy that shortcoming, a crop of celebrated researchers including Fei-Fei Li and Yann LeCun are focusing their efforts on a different class of AI: world models.

To become fluent in real-world physics, world models need to be trained on a combination of visual and action data. Before it can deftly maneuver a robotic arm, a model might need to be trained on video footage of the factory floor, coupled with information about how firmly an object should be gripped, with what torque it’s manipulated, and so on. But unlike LLMs, trained on oceans of text, there is no similar corpus of material available to world model labs.

“For world models, you need cause and consequence,” says Xiatian Zhu, an associate professor specializing in AI at the University of Surrey. “On the internet, we have very little of this type of data.”

Worldmodeldata, a British startup advised by LeCun, is aiming to solve that problem by packaging controller inputs and other data collected by video game studios—an exhaust product available in massive quantities—into training datasets for world models. Some companies, like General Intuition and Niantic, are already collecting video game data from their own platforms to build models. But Worldmodeldata pitches itself as a broker that curates and organizes data, saving labs from striking individual agreements with tons of game studios.

“There are millions of great games, and they are more and more similar to the real world,” Rhea Loucas, CEO of Worldmodeldata, tells WIRED. “Why don’t we take the vast, abundant, diverse experiences from video games, and teach AI?”

Though the hypothesis is yet to be fully tested, researchers are broadly working under the assumption that the performance of world models will improve in line with the size of their training datasets, in a similar way to LLMs. That means the shortage of suitable training data is one of the largest bottlenecks to progress.

Some labs have tried to manually generate their own data by attaching sensors to humans and robots in testing environments. But that approach yields only a small amount of data, and it doesn’t account for the fringe scenarios a model might encounter in the wild.

“You can pay people to demonstrate pick-and-place tasks. But repetition alone won’t capture the disorder of the world you’re asking a machine to operate in,” says Nicole Fraenkel, a partner at VC firm Khosla Ventures, which has invested in General Intuition.

Worldmodeldata’s theory is that data collected from video game environments—visual representations of a 3D space paired with actions taken by the player—is both available in the necessary quantities and sufficiently varied to capture all-important corner cases.

“The corner cases are the ones to actually get right,” says Fraenkel. “The cost of error with a car, plane, drone, factory forklift, or autonomous quadruped is very high.”

Worldmodeldata says it has licensed almost 1 million hours' worth of data from studios behind various popular video games, though Loucas declined to name them. In the future, the startup is aiming to create avenues for individual players to be compensated, too.

Loucas believes that video game data will ultimately make up the majority of the training material for world models, which will later be optimized using data specific to a given real-world environment or task. “This could well lead to the GPT moment for world models—making them really useful,” Loucas claims.

Not everybody shares the same optimism about video game data, though. Nvidia, which publishes a family of world models optimized to run on its chips, prefers to use a custom engine it devised specifically to replicate real-world physics as the backbone for its AI.

Ming-Yu Liu, who leads world model development at Nvidia, says that models trained on video game inputs are unlikely to fare well with tasks that require fine-grained motor control, like the careful manipulation of objects. That’s because video game physics is often eccentric, and developers take shortcuts to create the illusion of realism—a character dips a hand to collect an apple from the table—without coding in the details: the pressure applied by each finger to prevent the apple slipping from their grasp.

“I would be more conservative on using video game data for manipulation,” Liu says. “The physics for manipulation is much more involved.” Training on video game data is better reserved, he says, for world models meant for generating hyperrealistic video or 3D environments.

Zhu, the academic from the University of Surrey, has similar concerns. “Video games are, in essence, simulators. They do have some degree of physical grounding,” he says. “But they are very coarse, approximate.”

But until world models reach their ChatGPT moment, all kinds of ideas for getting them there remain on the table. “There are many paths to the promised land,” says Fraenkel. “The truth is, the jury is still out on which one is going to work best.”
