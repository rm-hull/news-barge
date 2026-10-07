---
title: These Researchers Made AI Drive a Toyota Corolla to Get In-N-Out
source_url: https://www.wired.com/story/ai-is-driving-cars-now-oh-boy/
source_site: Wired
source_slug: wired
scraped_at: '2026-10-07T20:37:34Z'
published: '2026-10-07T00:00:00Z'
description: Three engineers put GPT, Claude, and Grok in charge of a real car. Only
  one of them was successful.
image: https://media.wired.com/photos/6ac54e80213cd6c84b19e900/191:100/w_1280,c_limit/AI-Lab-Researchers-Got-an-LLM-to-Drive-a-Toyota-Business.jpg
categories:
- Technology & Software
- Science
people:
- Aditya Ramabadran
- Andrew Dai
- Claude Fable
- Simon Mahns
- Tobias Gessler
- Xingang Guo
locations:
- AI
- Bay Area
organisations:
- AGI
- Astra
- Axiom
- Elorian AI
- GPT
- Google DeepMind
- Grok
- In-N-Out Burger
- OpenAI
- Scale AI
---

Aditya Ramabadran, Simon Mahns, and Tobias Gessler, three AI engineers at a startup called Axiom, recently fancied In-N-Out Burger for lunch.

They weren’t about to drive themselves, though. Sitting in a 2024 Toyota Corolla near the Bay Area restaurant’s drive-thru lane, they opened a laptop and asked OpenAI’s GPT-6 Astra to take the wheel. They linked a chat interface to a server, which was connected to several windscreen-mounted cameras and the car’s power steering system. A safety driver kept one foot above the brake, just in case.

The AI model, which is normally tasked with generating text, code, and the odd image, slowly but surely navigated the vehicle up to the take-out window so they could collect their food.

“Maybe AGI is here after all,” one of the engineers remarked, referring to artificial general intelligence, the much-ballyhooed idea of machines that can match human intelligence.

Self-driving cars are nothing new, of course, but they’re normally operated by algorithms specifically trained and engineered for the task. In this case, the operation came from a model designed to output text, and it happened on the fly, with no prior coaching by the trio. The fast-food stunt, as well as a number of other experiments, suggest that language-based AI models are starting to gain a rudimentary but useful understanding of the physical world.

Though nothing overtly alarming happened during the trio’s lunchtime jaunt, they admit that putting a general-purpose model in charge of a fast-moving, two-ton hunk of steel is a high-stakes undertaking. As physical understanding improves, we could see AI models reach into the real world in impressive—and perhaps dangerous—new ways.

## **Getting Physical**

Today’s smartest models are incredibly good at answering complex questions and even performing some virtual tasks autonomously, but their skills tend to be limited to the world of computers and the internet. Take these models into the real world and they quickly become befuddled. Despite claims that AGI has arrived, AI companies evidently see physical reasoning as a yet-to-be-conquered frontier for AI.

Some researchers have left big companies to found startups focused on solving physical reasoning. Andrew Dai, the CEO of one such outfit, called Elorian AI, previously worked as a researcher at Google DeepMind. He says better visual reasoning will open up a lot of new applications for AI, like systems that understand whether diners are enjoying their meal in a restaurant or robots capable of functioning in a home. Dai says robotics is a crucial test case for physical reasoning skills. “It’s pretty essential for robotics,” he says. “You can’t really imagine home robotics without this.”

Elorian and Scale AI, a company that provides training data to big AI labs, recently developed a new benchmark, Humanity’s Sixth Sense, which measures models’ ability to understand physical scenes.

“Most visual AI research is about perception,” says Xingang Guo, a research scientist at Scale AI who was involved with developing the benchmark. “We wanted to ask what it would actually take for a model to understand a scene intuitively, the way a person does without thinking about it.”

For Ramabadran, Mahns, and Gessler, the goal with their In-N-Out project, done outside of their work at Axiom, was to measure how well models can operate in the messy real world.

They got the idea to test models’ driving skills while hanging out one weekend. They noticed that models like Astra were capable of building complex 3D simulations, and wondered if it might translate to an ability to navigate the real world.

“We all live in the Bay Area, and we’re exposed to Teslas and Waymos, so maybe that played a role,” Ramabadran tells me.

The engineers tried testing SpaceXAI’s Grok before experimenting with the latest models from OpenAI and Anthropic. At first, the models refused to take control of the vehicles—they spat back things like, “I can help interpret road images, but I can’t issue motion commands to a physical car.” But with a little careful prompting, they could be coaxed into going further. The three were stunned when models began driving.

The engineers say big AI companies seem to be focusing on improving the spatial reasoning capabilities of their latest models, but they doubt this means they’re actually training them to drive cars. The models’ vehicular talents likely materialized as part of training focused on 3D reasoning, they say. “This could be like an emergent capability of just scaling up the multimodality of the model,” Mahns tells me, referencing inputs like images, video, and 3D models that are now used to train models.

Still, a new vehicular benchmark from the trio, called DrivingBench, suggests that these models still have a long way to go before they could pass a driving test. The benchmark measures a model’s ability to drive around a simple course, set up in a parking lot. Only Astra is able to complete the course—and very slowly at that. Claude Fable 5.1 made it 45 percent of the way around, and Grok made it just 11 percent of the way.

Ramabadran says the latest models seem capable of adjusting to errors; they apparently adapted to the car's controls and improved their driving in real time. “The models really did seem to be adjusting or in-context learning based on their mistakes and learning how to better navigate the controls,” he says. GPT, take the wheel.

*This is an edition of* **Will Knight’sAI Lab newsletter**. Read previous newsletters** here.**
