---
title: Here is how to understand OpenAI’s major mathematical breakthrough | New Scientist
source_url: https://www.newscientist.com/article/2588781-here-is-how-to-understand-openais-major-mathematical-breakthrough/?utm_campaign=RSS|NSNS&utm_content=home&utm_medium=RSS&utm_source=NSNS
source_site: New Scientist
source_slug: new-scientist
scraped_at: '2026-09-10T19:07:00Z'
published: '2026-09-10T00:00:00Z'
description: Since OpenAI announced its solution to one of the prestigious Millennium
  Prize Problems, mathematicians have been urgently trying to unpick what it means
image: https://www.newscientist.com/wp-content/uploads/2026/09/SEI_311681995.jpg
---

![](https://www.newscientist.com/wp-content/uploads/2026/09/SEI_311681995.jpg?w=840)

One of the trickiest problems in mathematics has fallen at the hands of an advanced AI model. Following the announcement that OpenAI has resolved one tantalising aspect of the Navier-Stokes equations, researchers are now urgently trying to understand its implications.

The Navier-Stokes equations were first written down around 200 years ago and describe the behaviour of fluids. They have been instrumental in everything from building better airplane wings to creating effective artificial hearts.

Yet, our understanding of the equations is so limited that resolving a relatively simple question about them is one of the prestigious Millennium Prize Problems, where a solution means a $1 million reward. That question asks whether the Navier-Stokes equations always work or if they sometimes break down and no longer make sense.

Advertisement

“The equations themselves are so simple, but we understand so little,” says John Evans at the University of Colorado Boulder.

The team at OpenAI has found that the equations do sometimes fall apart, finding situations known as “blow-ups”, where the speed of part of the fluid suddenly becomes infinity. It would be like an infinite whirlpool suddenly appearing in your bath. The OpenAI team found the answer thanks to more than 10,000 AI agents working together in different configurations. About 88 hours later, they had a solution.

“This progress happened so fast and condensed what could have been months or years of human-driven progress to a matter of days,” says Zaher Hani at the University of Michigan.

A long road led here. In 2014, Thomas Hou at the California Institute of Technology and his colleagues showed one way to create a blow-up for Euler equations, one of the stepping stones towards Navier-Stokes. However, their approach applied only when the fluid in question was walled in, and not more generally. Other teams tried to extend it, but without success. Researchers started to suspect that the Navier-Stokes equations really can blow up, but no one had definitively shown how to construct a specific fluid flow that does so.

A breakthrough came in 2021, when Luis Martínez-Zoroa at CUNEF University in Spain and Diego Córdoba at the Spanish National Research Council developed a new method for creating blow-ups that worked for both Euler and Navier-Stokes equations. Their key insight was to divide the fluid into thin layers and perform calculations for each. Adding up the layers resulted in a cascade of effects that can ultimately cause a blow-up.

“This is really the showstopper,” says Steven Brunton at the University of Washington. “AI [use] was absolutely pivotal, and the scale [of it] is interesting and useful, but the solution approach was developed by brilliant humans.”

The one problem was that Martínez-Zoroa and Córdoba’s work relied on an unrealistic force being used, which means it wouldn’t solve the Millennium problem.

Then, earlier this week, Tristan Buckmaster at New York University and Levent Alpöge at AI company Anthropic published a breakthrough removing that requirement for Euler equations and several related situations, paving a clear path to Navier-Stokes. A few hours afterwards, OpenAI published its full result. (The controversy surrounding this is described here.)

OpenAI’s agents used an approach like Martínez-Zoroa and Córdoba, working iteratively to build a blow-up. However, the AI’s trick was ultimately distinct, not just a more powerful repetition, says Evans.

The specific blow-up was a spinning whirlpool that becomes longer, thinner and more intense over time, before its swirling ultimately becomes infinite. The new proof showed that this happens in finite time and using only a finite amount of force on the fluid. “We were very surprised by the developments: both Diego and I were confident that the resolution was a matter of time, but we weren’t expecting it to be so soon,” says Martínez-Zoroa.

Evans says that it is exciting that, in the work from OpenAI, most of the key ideas the AI agents used are relatively simple ones that an undergraduate could have learned in class. “Even though it’s 166 pages of complicated math, you can actually draw it down to a couple of simpler physical mechanisms,” he says. In his view, AI agents could help make better models of fluid flow in the future.

Brunton says that the Navier-Stokes equations will continue to be useful. “Every equation is an approximation. Navier-Stokes is a great approximation for a very big range of fluids, but at the point it starts to blow up to infinity, it’s not a good model of the world anymore,” he says.

The Navier-Stokes equations model fluids as continuous entities rather than made of individual atoms, so at very small scales a different mathematical model is necessary. However, for engineers, that level of precision won’t be needed, says Brunton. “Nothing changes for us,” he says.

Nevertheless, many of his mathematician colleagues have been reaching out to him about how to fully understand the AI’s process and gain deeper mathematical insights.

Because AI proofs are coming so thick and fast, there are concerns that mathematicians will continue to get more answers to conundrums, but without sufficient explanations. “It’s not clear if we will get the same long-term benefits to the scientific process, or our mathematical understanding,” says Hani.
