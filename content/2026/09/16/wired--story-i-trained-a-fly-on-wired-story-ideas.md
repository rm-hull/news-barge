---
title: I Trained a Fly’s Brain to Generate WIRED Story Ideas
source_url: https://www.wired.com/story/i-trained-a-fly-on-wired-story-ideas/
source_site: Wired
source_slug: wired
scraped_at: '2026-09-16T19:32:13Z'
published: '2026-09-16T00:00:00Z'
description: I used an open-source map of a fruit fly’s brain to vibe code a website
  called PitchFly. Its headline suggestions were delightfully bananas.
image: https://media.wired.com/photos/6aa8849459082b83fd22fcf8/191:100/w_1280,c_limit/AI-Lab-This-Fly-Can-Come-Up-With-WIRED-Stories-Businesspsd.jpg
categories:
- Technology & Software
- Science
locations: []
people:
- Alex Wormuth
- Donald Trump
- Lyra Bubbles
- PitchFly
- Rubik
organisations:
- AI
- Codex
- Coinbase
- Google
- StonkFly
- WIRED
---

Meet PitchFly, WIRED’s latest editorial recruit.

He has 165,112 neurons, and they’re all trained to generate story ideas. A sampling of his early output: “The Hidden Weather Problem Inside Surveillance”; “The Engineers Who Think Elon Musk Needs Less Computer Security”; and my personal favorite, “Everyone Wants Cooking. Nobody Has Solved Donald Trump.”

PitchFly uses a detailed map of the brain of a male drosophila—the common fruit fly. Developed by researchers from Google and a number of academic institutions, the map, known as a connectome, captures the way that 166,000 neurons and 125 million connecting synapses fire in response to stimuli. In essence, you can use it to simulate how a fly would respond to lots of stuff—it’s a very simple version of artificial intelligence based on charting real biological intelligence.

Because the researchers open-sourced it, you can easily use AI to import the connectome into a project with a little prompting. For PitchFly, I vibe coded a project in which the tiny digital drosophila brain generates story ideas. (I’m not sure why the fly has a little hat on, but I like its style.) This involved scraping together hundreds of the most popular story headlines from the site from the past year and feeding them into the connectome. I had Codex do the hard work, and it decided that the most efficient approach was to turn the headlines into words and phrases, then transform them into a representation that a neural network could understand. The connectome was fed the best-performing stories and told to generate its own ideas based on that.

In other words, this isn’t a fly-based language model—although someone apparently created one of those. The fly brain has no idea what any of the words mean, or if any of it makes sense. It’s just remixing the patterns it has seen in pleasing new ways. A cynic might suggest this is exactly how some journalists generate their own pitches, but I think that’s a bit unfair—and judging by its lunatic ideas, PitchFly won’t be replacing me anytime soon:

- The Tiny Shift in Agentic AI Is Rewriting the Rules of Food and Drink
- What Security News Is Quietly Doing to Donald Trump
- The Race to Reinvent Privacy Before Artificial Intelligence Breaks
- Is China About to Make Digital Syndication Obsolete?

In the future, perhaps I could have the program continue to learn by reading new WIRED headlines. For now, though, this seems like a decent proof of concept, not to mention evidence at last that the average WIRED writer is intellectually superior to a fruit fly.

After the connectome’s release in early September, dozens of other weird and wonderful projects powered by fruit-fly intelligence sprang up.

An X user called Lyra Bubbles, for instance, demo’d a project that involved training the virtual fly brain to play the VR game *Beat Saber*. Alex Wormuth, a software engineer at Coinbase, created StonkFly, which uses the fly’s tiny brain to decide how to trade stocks. (It’s losing money, but it’s doing surprisingly well, all things considered.)

“The fly brings lighthearted, humorous relief” at a time when everyone is worried about the existential risks of AI, Wormuth told me in a DM. He says he found playing with the fruit fly connectome philosophically fascinating, too. “It sparks questions about ethics of this and whether there is any consciousness [in the replication of fly’s brain],” he says.

Others trained the connectome to play *Doom*,* Minecraft*, and* Pong*. Some fly brains apparently learned to solve Rubik’s cubes. And someone also put the fly brain in charge of driving virtual cars—it turns out flies are terrible at parallel parking. (Then again, so am I, so I won’t pass judgment.)

I haven’t verified that all these projects actually use the connectome—they may just be fun animations. And some of them—like one that simply involves training the fly to take a well-earned break—seem like spoofs. But there are some serious science projects out there, too, including visualizations for exploring the connectome and tools for manipulating neural circuitry.

Mapping different animal brains may help neuroscientists decipher the biological foundations of intelligence. It isn’t possible—yet—to map all 86 billion neurons in a human brain, but peering into the brains of smaller creatures can provide useful insights. Neuroscientists can also test theories about how damage affects neuronal wiring—and how such damage might someday be repaired—by messing with the fly’s connectome.

As far as AI is concerned, all this fruit-fly frivolity also shows how easy it is now to train and deploy your own model. The best use for the giant LLMs run by big AI companies may be building specialized AI models for specific tasks (something I’ve written about previously). Sometimes even a tiny brain can do quite well.

*This is an edition of***Will Knight’sAI Lab newsletter**. Read previous newsletters** here.**
