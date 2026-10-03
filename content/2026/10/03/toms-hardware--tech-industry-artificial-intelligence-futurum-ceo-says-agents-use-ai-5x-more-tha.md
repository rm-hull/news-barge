---
title: AI agents use 5x more tokens than humans as cached prompts explode, headed
  for 10x — agents are mostly rereading what they've already seen, skyrocketing KV
  cache demand threatens already-worsening RAM shortages
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/futurum-ceo-says-agents-use-ai-5x-more-than-humans-number-will-eventually-hit-10x-but-agents-are-mostly-rereading-what-theyve-already-seen
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-03T15:20:03Z'
published: '2026-10-03T00:00:00Z'
description: OpenRouter has agents at 7.3 trillion tokens versus 1.4 trillion for
  humans.
image: https://cdn.mos.cms.futurecdn.net/hNQivoNg7PnAeRNSivatuR-2560-80.png
categories:
- Technology & Software
- Hardware
people:
- Claude Code
- Daniel Newman
- Peter Walker
- Shane Downing
- Tom
locations:
- AI
organisations:
- AI 5x
- API
- DeepSeek
- Futurum Group
- Google News
- HBM
- McKinsey
- Micron
- OpenRouter
- PC
- Shane Downing
- State of AI
- Tom’s Hardware
---

![The OpenRouter logo in lime green and white on a black background](https://cdn.mos.cms.futurecdn.net/hNQivoNg7PnAeRNSivatuR-1920-80.png)

Futurum Group CEO Daniel Newman wrote in an X post that “AI is currently used by AI 5x more than it is used by humans. That number will accelerate to 10x and then higher and higher.” His data, an Andreessen Horowitz (a16z) chart of OpenRouter figures, shows agents at 7.3 trillion tokens versus humans’ 1.4 trillion as of August, six months after agent usage first surpassed humans. But the agents are mostly rereading what they’ve already seen: more than 85% of agent tokens come from cached prompts, a16z wrote, citing OpenRouter.

> AI is currently used by AI 5x more than it is used by humans. That number will accelerate to 10x and then higher and higher.We keep speaking to human adoption when trying to determine ROI, but the utilization and scale is exponentially larger than that.September 30, 2026

OpenRouter is “a leading AI model gateway and routing platform.” A chart from its head of insights, Peter Walker, lists “7-day average token usage on OpenRouter split by type.” It states that, since the February crossover point, agents are using 14x more tokens while human usage is up 2.8x. The a16z chart in Newman’s post shows the same data. OpenRouter sorts each API key into one of three categories: agentic, mixed, or human, using a “7-signal weighted composite score that includes inputs such as tool call rate, turn count, gap timing, and others.”

![OpenRouter chart of seven-day average token usage by agents, humans, and mixed traffic from September 2025 to August 2026](https://cdn.mos.cms.futurecdn.net/zvp279itG72czpcwiQhfTF-1200-80.jpg)

The mixed category, possibly covering behavior that is part agent and part human, grew 4.7x over the same period, according to our math. Depending on how that traffic splits, the agents’ lead over humans may vary. The data also measures token volume, not spending. This is data from only one platform, and the trend isn’t completely consistent, with dips in April and July. However, agent use is growing elsewhere. In McKinsey’s 2026 State of AI survey, 40% of respondents from large organizations reported scaling AI agents, up from 27% a year earlier.

Cached tokens also account for nearly all of the relative growth in token usage, a16z wrote. They cost far less than processing a prompt from scratch, but they still have to be held in memory, and a16z, an OpenRouter investor, ties that to rising demand for high-bandwidth memory (HBM). Models keep that stored context in what’s called the KV cache, and “the KV cache is outgrowing GPU HBM capacity,” according to our reporting.

The same pattern shows up in the logs of a call center consultancy that tested DeepSeek on rented Nvidia H200s. In its own agents’ September usage on Claude Code, “96% of all input was re-reading old conversation.” Coupled with OpenRouter’s data, this suggests the token count overstates the bill, but the hardware cost for memory remains very real.

That memory is already scarce. Micron expects RAM and storage shortages to worsen in 2027 and 2028, with customers paying more than this year, while memory makers put HBM for AI data centers first. If Newman’s prediction that the 5x will become “10X, 20X, 30X” is true, PC buyers will be bidding for memory against even more agents.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Shane Downing](https://cdn.mos.cms.futurecdn.net/Zosi9VrDytS9FkgJiHvc69-140-80.png)

Shane Downing is a Contributing Writer for Tom’s Hardware, covering consumer storage, PC hardware, and AI.
