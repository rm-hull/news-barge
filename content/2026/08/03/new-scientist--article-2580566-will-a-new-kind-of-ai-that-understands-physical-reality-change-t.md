---
title: Will a new kind of AI that understands physical reality change the world again?
  | New Scientist
source_url: https://www.newscientist.com/article/2580566-will-a-new-kind-of-ai-that-understands-physical-reality-change-the-world-again/?utm_campaign=RSS|NSNS&utm_content=home&utm_medium=RSS&utm_source=NSNS
source_site: New Scientist
source_slug: new-scientist
scraped_at: '2026-08-03T15:11:24Z'
published: '2026-08-03T00:00:00Z'
description: AI chatbots can describe reality in words, but don’t truly understand
  cause and effect in the real world. Now, a fresh kind of machine intelligence that
  does just that is emerging
image: https://www.newscientist.com/wp-content/uploads/2026/07/SEI_306689129.jpg
---

![](https://www.newscientist.com/wp-content/uploads/2026/07/SEI_306689129.jpg?w=840)

What happens when you knock a glass off a table? Ask ChatGPT and you get a step-by-step explanation: how gravity accelerates the receptacle along a “parabolic trajectory”, why it could shatter “if the impact generates stresses greater than the material can withstand”. Ask my 3-year-old daughter and she’s less bothered with fine details: “It go smash and water everywhere!”

When it comes to the future of artificial intelligence, the difference is instructive. The large language models (LLMs) powering today’s chatbots are trained on vast swathes of text to predict the next word in a sequence. Unlike little Adeline, however, no LLM has ever actually knocked a glass off a table – or thrown spaghetti at a wall, or driven a scooter into a pond – and that may impose a fundamental limitation on their capabilities.

This, essentially, is why some researchers argue that what we need to take AI to the next level isn’t ever-larger LLMs, but “world models”: systems that learn through observation so they can simulate the consequences of actions in the real world.

Advertisement

World models have rapidly become AI’s next frontier, attracting huge buzz from industry and business thanks to their promise in autonomous robotics. What makes the world-model approach especially intriguing, though, is that it also ostensibly offers a route to artificial general intelligence (AGI), or machines with human-level reasoning that can be applied across a range of tasks. 

The problem is that it is tricky to parse substance from bluster. The term “world model” is confusingly elastic, for starters – for some, problematically so. It has become “a kind of shorthand for all the things that current AI systems can’t do well”, says Melanie Mitchell at the Santa Fe Institute in New Mexico. It is unclear exactly what these systems should model, never mind whether internal representations of physical reality will be sufficient for the kind of generalisable intelligence that means my 3-year-old intuitively understands what happens when she swipes a glass, even if she can’t say why.

To make sense of world models as they apply in AI, it helps to understand the concept’s roots in cognitive science. AI researchers themselves typically trace it back to 1943, when psychologist Kenneth Craik wrote that the human mind “carries a small-scale model of external reality and of its own possible actions”, allowing us “to try out various alternatives” and “react to future situations before they arise”.

![Cheese carriers load the cheese at the Edam cheese market, Edam, Netherlands](https://www.newscientist.com/wp-content/uploads/2026/07/SEI_305951304.jpg?w=840)

That idea has evolved in the decades since, most notably with the theory of predictive processing. This posits that perception – possibly even consciousness itself – relies on the brain constantly generating predictions about the external world and updating them in response to incoming sensory data.

But the point remains. “The key idea is that intelligence involves building models of the world in our heads so we can simulate outcomes and avoid costly mistakes,” says Josh Tenenbaum, a cognitive scientist and AI researcher at the Massachusetts Institute of Technology. “So ‘our ideas die in our stead’, as Craik put it.”

It doesn’t take a genius to see why that has piqued the interest of AI researchers. LLMs have proved astonishingly capable, and they can certainly give the impression they understand things as we do. But language is a description of reality, rather than reality itself, and their lack of direct experience means that even the most powerful language models struggle when it comes to “understanding” physical phenomena in the real world.

LLMs often perform poorly when they are asked to reason about spatial concepts and things that might happen in the physical world, says Mitchell. “If you’ve ever uploaded a map to one of these models and asked it questions about it, you’ll know that they will often have a lot of problems with reasoning.” Indeed, in a 2024 study, when researchers trained language models on a database of turn-by-turn directions for taxi trips around New York City, they found that the system could provide reasonable routes from one point to another – but failed miserably when asked to take the odd detour.

The reason why is that the LLMs have only descriptions of journeys, and therefore lack the sort of mental map that allows us to imagine what would happen in different scenarios. And navigation is just one example. LLMs demonstrate similar shortcomings in any scenario where you need to simulate the physical world – safely loading a dishwasher, say, or folding laundry. “They’re not designed for it, which is why people are interested in alternatives like world models,” says Tenenbaum.


![](https://www.newscientist.com/wp-content/uploads/2026/07/SEI_306689183.jpg?w=840)

Probably the most influential proponent is Yann LeCun, a computer scientist at New York University and, until recently, chief scientist of foundational AI research at Meta. His argument, first made in a 2022 paper, is essentially that if we want to build truly intelligent systems that can reason, plan and act effectively in the real world, we need world models.

“I cannot imagine we can build agentic systems without those systems having an ability to predict, in advance, what the consequences of their actions are going to be,” LeCun told artificial intelligence forum AI House Davos in January. And the key to that, he reckons, is systems that learn the rules of the world from observation.

The idea has caught on. In December 2025, LeCun left Meta to found AMI Labs, raising just north of $1 billion to build world-model systems. A year earlier, Fei-Fei Li at Stanford University in California started World Labs, with $230 million of investment, to develop AI with “spatial intelligence”. Many of the established AI firms, most notably Google DeepMind, are now also actively pursuing world models in one form or another.

The reason for the influx of money is primarily the promise that world models hold for advancing robotics (see “What are AI world models good for?”, below). However, it is early days and the existing prototypes are modest in their applications. With Marble, for instance, World Labs has built a system that generates coherent 3D scenes from text prompts. Similarly, DeepMind’s Genie 3 creates convincing interactive virtual environments – “snowy mountain at dusk”, say – in which you can move around for several minutes and even prompt events like rain.

![Genie 3 screengrab](https://www.newscientist.com/wp-content/uploads/2026/07/SEI_305951275.jpg?w=840)

In both cases, the companies describe their systems as “world models”. But Marble is really a 3D video generator and Genie 3 a video-game simulator, albeit one producing simulations in which agents could plausibly act, observe consequences and learn.

Arguably, a proper world model would be something that exists inside an agent such that it can predict the consequences of its decisions, imagine the future and plan ahead before taking actions – and that is what DeepMind is pushing towards with its Dreamer 4 system, released in September 2025. It learns an internal predictive model of its environment, training mostly on data from the video game *Minecraft*, and uses that to train an agent that repeatedly “dreams” the consequences of possible actions to improve its behaviour.

“The biggest difference [from Genie 3] is that Dreamer 4 is an agent, not just a world model,” says Danijar Hafner at DeepMind in San Francisco, who leads the Dreamer 4 team. “It predicts actions and improves them through iterative self-improvement, using planning and [imagined] trial and error.”

The power of this approach is apparent in Hafner and his colleagues’ demonstration that Dreamer 4 can figure out how to collect diamonds in *Minecraft*, a complex task involving thousands of different actions – gathering resources, crafting tools, navigating the landscape – without being shown how to play. “The system has to understand its environment and generalise, because each new episode starts in a randomly generated world,” says Hafner.

That is an important step, not least because this is precisely the kind of world model that could facilitate autonomous robots capable of folding laundry, say, or loading the dishwasher. “I think it’s going to solve robotics,” says Hafner. “What’s missing now is execution: data, compute, scaling. But we have the recipe, so, like with language models, it’s about scaling and details.”

Who would bet against DeepMind, given its impressive track record? After all, its researchers have won a Nobel prize for work on protein folding. But while Dreamer 4 demonstrates that agents with internal world models can reason and plan, it leaves a deeper question unresolved: what exactly should these systems learn about the world, or, more specifically, at what level of detail? And this has become a key fault line in the field, with two distinct approaches emerging.

Many of the existing strategies are attempting to generate predictions on condition of action, as the researchers put it, by reconstructing future observations as faithfully to the training data as possible. But LeCun reckons that is the wrong approach, or at least not the best. His argument is based on the fact that humans don’t mentally simulate the world in any great detail, and certainly not pixel by pixel. When we imagine a glass falling from a table and smashing to pieces, for example, we don’t predict the position of every shard of glass, every water droplet. Instead, LeCun argues, we run highly compressed models that capture only the aspects that matter.

This why LeCun advocates for a different tack, which he calls joint-embedding predictive architecture (JEPA). In this framework, world models infer abstract representations of what is relevant for reasoning, planning and action. “Generative models try to reconstruct pixels, whereas JEPA learns in a latent space and only predicts what is useful,” says Randall Balestriero at Brown University in Rhode Island, who has worked with LeCun on JEPA-based world models. “It ignores irrelevant details and focuses only on what matters for the agent.”

LeCun and his investors appear to be betting that the JEPA approach will offer a swifter route to real-world applications, largely because it requires less training data. The most concrete publicly available demonstration of this technique so far is a system called V-JEPA 2, released by Meta in June 2025. Trained on video inputs, V-JEPA learns by masking certain regions of footage – obscuring a moving ball, say, over multiple consecutive frames – and repeatedly predicting not pixels, but abstract representations of what was hidden to learn a compact internal model of how the ball moves. What LeCun and his colleagues have shown, then, is that their system can model the causal structure of the physical world without having to reconstruct it in detail.

Which isn’t to say that JEPA is necessarily any better than generative world models. Its advocates argue that it will be, of course. “Without abstraction, AI systems will stay limited to narrow tasks,” says Balestriero. But V-JEPA 2 is yet to clearly demonstrate that its abstract representations are sufficiently meaningful to enable an agent operating in an open-ended environment to reason and plan. “The biggest missing piece is the question of, how do we know that the abstraction is actually useful,” says Balestriero. “This is where there is a huge amount of active research right now, to understand: what do you capture, or how do you encode something very rich about the world that is useful for planning downstream.”

Hafner, for his part, isn’t convinced that more compressed representations of reality are better. “Yann is right about many things, even if maybe he expresses them more controversially than necessary, and the JEPA approach is very promising,” he says. “But I don’t think that representations should be compressed and tiny. Ultimately, you want to learn strong representations, and what we did with Dreamer 4 [which trains with pixels but predicts in abstract space] is incredibly robust.”

![HUANGGANG, CHINA - MARCH 22: Intelligent humanoid robot helps pick tea leaves at a tea garden on March 22, 2026 in Huanggang, Hubei Province of China. Intelligent robots joined tea farmers in picking spring tea at the tea garden in Wuyunshan Village of Huanggang City. (Photo by Wang Jiang/VCG via Getty Images)](https://www.newscientist.com/wp-content/uploads/2026/07/SEI_305951425.jpg?w=840)

More broadly, it is also far from clear at this stage if any of the world models in development – whether they learn and predict by reconstructing the world in high-fidelity or by inferring abstract representations – will ultimately be enough to get us to AGI.

Now, it’s fair to say that AGI is another elastic term, and that claims about world models as a route towards it exist on a spectrum, with some of the most ambitious suggesting that learned simulations of physical reality could become the foundation of generally capable reasoning agents. When it released Genie 3, for instance, DeepMind insisted world models are “a key stepping stone on the path to AGI, since they make it possible to train AI agents in an unlimited curriculum of rich simulation environments”. Indeed, Hafner argues that “if you have systems that are able to represent the rules governing the world, then you’re approaching something like AGI because that’s understanding, that’s a key part of intelligence”.

For his part, LeCun talks about them as a vital component of broader systems, rather than the whole story. And yet it is worth exploring the extent to which the kinds of world models in development would approximate human intelligence, because it can reveal what else might be required. Hafner says the most immediate requirement is temporal abstraction – that is, being able to reason not just about what will happen in the immediate future, but as things continue to play out. “You cannot just simulate everything at a sub-second, frame-by-frame level, because humans do not reason like that,” he says. “This is one of the open frontiers.”

Tenenbaum goes further. Human world models aren’t just engines for predictions, he says, “they are much richer than that”. Human reasoning depends on various forms of causal abstraction and hypothesis-driven inference – not to mention models of other minds – which together allow us to flexibly recombine knowledge across different situations. “A key open question in all this is whether scaling up these world models will recover that richness, and my view is that it likely won’t,” says Tenenbaum.

Mitchell makes a similar, if slightly broader, point. “I think the ability to have a kind of compressed, simulatable representation of aspects of the world is very important, and this notion of world models is probably going to result in useful improvements,” she says. “But I think there are probably lots of other aspects of intelligence that matter.”

![1X NEO](https://www.newscientist.com/wp-content/uploads/2026/03/04115741/SEI_287801892.jpg?w=900&h=600&crop=1) 

			You can now buy a humanoid robot housekeeper for less than the price of a second-hand car. But before splashing out, there’s something you need to know

Another limitation of AI systems today, says Mitchell, is a lack of metacognition – an awareness of their own cognitive state, of what they know and don’t know, and how uncertain they are. “Is that fixable with a world model? Well, it depends what kind of world model, obviously,” she says. “But I’m a little worried that the notion of ‘world model’ is going to be used as the term for the difference between what we have now and ‘AGI’.”

All of which suggests that world models as currently conceived may well be necessary for human-level machine intelligence, but not necessarily sufficient. Indeed, while it looks increasingly likely that they will be powerful and genuinely useful in robotics, and possibly scientific simulation too, it is far from a sure bet that they will replicate the way world models work in human cognition, never mind human-level intelligence more broadly. “One of the big misconceptions is that intelligence is a single thing, that there is a single world model in the brain,” says Tenenbaum. “What we actually have is the ability to run many different models depending on the context, task and goal.”

Ultimately, then, the task of replicating what my 3-year-old daughter’s brain is capable of when it comes to modelling and predicting the physical world – even if it doesn’t stop her knocking glasses of water off the table – is not one to be underestimated.

## What are AI world models good for?

For anyone wondering what the rise of world models in AI means for us, the applications researchers have in mind are illuminating. In short, world models are unlikely to produce another ChatGPT moment, when millions of people suddenly discovered a powerful tool they could use in their everyday lives. The promise isn’t better chatbots, or really anything that consumers will notice any time soon, but rather a new generation of AI systems whose earliest impact could come in the form of autonomous robots capable of working in factories and warehouses, before possibly making their way into our homes.

The rationale is straightforward: rather than learning by repeatedly trying and failing for real, which is dangerous, or learning responses for every situation from exhaustive training data, which is expensive, robots controlled by AI world models could predict what would happen across a vast range of scenarios and choose the safest and most effective action. “There’s huge potential for robotics to change everything,” says Danijar Hafner at Google DeepMind in San Francisco, who works on world models.

Beyond robots, world models are also touted as a way to accelerate scientific advances, particularly in materials science and drug discovery, where the challenge lies in exploring vast numbers of candidate molecules or atomic arrangements for novel compounds. By learning the underlying physics, they could simulate countless possibilities – how molecules interact with proteins, say, or which hypothetical compounds best capture carbon dioxide – before anything is made or tested in the lab.

“The key capability is planning in imagination space because, once you have this abstract predictor, you can say, for example, if you want to develop a drug, ‘OK, what if I add this chemical or do this series of actions’, and you can actually predict what will happen without having to do it in the real world,” says Randall Balestriero at Brown University in Rhode Island. “It just makes things cheaper and faster.”
