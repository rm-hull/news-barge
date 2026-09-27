---
title: Developer says Jev decision model beat Pokémon Red in under a week — non-LLM
  engine succeeds where traditional chatbots stalled for months, but Claude Opus 5
  coached the model through its dead ends
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/developer-says-jev-decision-model-beat-pokemon-red-in-under-a-week-non-llm-engine-succeeds-where-traditional-chatbots-stalled-for-months-but-claude-opus-5-coached-the-model-through-its-dead-ends
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-27T12:01:09Z'
published: '2026-09-27T00:00:00Z'
description: With only a list of choices to pick from, the AI made the Hall of Fame.
image: https://cdn.mos.cms.futurecdn.net/fNUKHSKSPNBCvfema8pZ9H-1600-80.jpg
categories:
- Technology & Software
- Hardware
people:
- Andrew Boyd
- Christian Mathiesen
- Claude Opus
- Claude Plays Pokémon
- Jev Plays Pokemon
- LangChain
- Lorelei
- Professor Oak
- Tom
locations:
- Pallet Town
- Rock Tunnel
organisations:
- Anthropic
- Frigade
- Get Tom's Hardware
- Github
- Google News
- Hall of Fame
- LLM
- Opus
- Pokémon Red
- Shane Downing
- Standard Agents Inc
- Tom’s Hardware
- TypeSafe AI
---

![Pokémon Red Version key art showing Charizard beside the Pokémon logo](https://cdn.mos.cms.futurecdn.net/fNUKHSKSPNBCvfema8pZ9H.jpg)

TypeSafe AI's Jev "beat the Elite Four and the Champion and entered the Hall of Fame on September 23, 2026" in Pokémon Red, according to the developer's project page. Unlike the chatbots that have taken weeks to months to beat the Blue version of the game, Jev can only pick from a list of choices. It didn't achieve this without help, though. Anthropic's Claude Opus 5 monitored the game log and adjusted options and their wording as Jev played, effectively acting like a coach.

The developer, Andrew Boyd, is the founder of Standard Agents Inc., which sells a platform for building AI agents. Boyd initially announced the project on X with victory coming in a week. The gameplay was livestreamed, available in a browser or a terminal, with a chat that Jev moderated.

> Let's go! Jev Plays Pokemon. Follow along here: [https://t.co/64naxTJlDg](https://t.co/64naxTJlDg) OR, in your terminal run `npx jev-plays-pokemon` to follow along (with chat!) in a TUI. Github oAuth required to chat. Jev is the player and the chat moderator. Let's catch them all!September 17, 2026

Jev is a recently released decision model that returns solutions with a confidence figure. It is not a chatbot, and it is not an LLM. For the game, Jev refers to a list of options with facts, and it selects the best option based on probability. It doesn't read the screen and does not produce text or images. A traditional LLM, Claude Opus 5, monitored the game log to help Jev when it got stuck. This happened indirectly by modifying the options and data available to Jev.

The page's harness changelog had 474 entries, most of them a failure from the game log paired with the change made in response. Examples of mistakes include walking "into Lorelei's shut entrance 53 times," crossing one Rock Tunnel ladder "124 times in ten minutes," and losing to the Champion's Alakazam after beating all four Elite Four trainers, which forced Jev to beat all four again before it took down the Champion later that day.

Opus made adjustments for both accuracy and cost. Using notes on the model from TypeSafe, it reduced the text sent to Jev by about two-thirds and used words instead of numbers. When Jev got stuck in a loop, the harness was changed to request a decision only every six seconds instead of about once a second. Human input also existed: viewers sent tips in chat, and the helpful ones were used to improve Jev's list of options. The reliance on Opus, the developer, and the audience shows the strengths and limitations of the decision model.

A second Jev-based run, made by Christian Mathiesen at Frigade, detailed a separate approach. The harness in that case, according to its README, "reads the game's memory, lists the legal options ... and Jev picks one," but it never writes to game memory. Mathiesen said that his first version, where Jev could choose the buttons directly, "never left Pallet Town." The cost, by his own estimate, is "about $1–1.70 per 24 hours."

A separate Pokémon Red experiment took a different route. A developer who goes by stmonty trained a small world model on an RTX 3080 Ti with more than 42,000 frames of gameplay. Starting from a save in Professor Oak's lab, it picked a starter in 52 of 100 tries, according to stmonty's blog post. Both the goal and assistance were far smaller than Jev's: stmonty's model had to learn what each input does from screenshots alone.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

The viral nature of Jev, with LangChain describing it as having "had a pretty outsized response" since its launch on Sept. 15, had multiple developers playing the game within 10 days. The success of the run demonstrates that collaboration with specialized models can improve problem-solving in a meaningful way. TypeSafe itself says open-ended tasks are better suited to an LLM, as we reported when Jev launched. For comparison, Anthropic's Claude Plays Pokémon stream, running Opus 4.5 at the time, still hadn't finished Red as of January. This time, with Jev doing the playing and Claude writing the rules, the developer achieved victory.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Shane Downing](https://cdn.mos.cms.futurecdn.net/Zosi9VrDytS9FkgJiHvc69.png)

Shane Downing is a Contributing Writer for Tom’s Hardware, covering consumer storage, PC hardware, and AI.
