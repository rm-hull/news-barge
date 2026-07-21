---
title: The enduring paradox of the AI economy — models get better and more efficient,
  yet costs can still easily spiral out of control
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/the-enduring-paradox-of-the-ai-economy-models-get-better-and-more-efficient-yet-costs-can-still-easily-spiral-out-of-control
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-21T10:32:57Z'
published: '2026-07-20T00:00:00Z'
description: Token amplification is now the word of the day.
image: https://cdn.mos.cms.futurecdn.net/NRH4tQ2AcTYcjJCunasFF6-2048-80.jpg
---

![Bots manipulating a graph](https://cdn.mos.cms.futurecdn.net/NRH4tQ2AcTYcjJCunasFF6.jpg) 

Much has been written regarding the questionable economics of the AI space, but most of the discussion revolves around high-level concepts like market shares, datacenter investments, and power expenditure. The general expectation of technology is that it gets cheaper as it improves, but the AI space has a rather peculiar problem: Usage costs are actually soaring even as models get better, as detailed in a write-up at VentureBeat.

With all the advancements in models over the last two years, having a bot that answers questions of simple-to-moderate difficulty is now old news, as they all do that with reasonable accuracy. Agentic workloads are where the real potential is at, letting bots loose on multi-stage, repeatable tasks that would previously take a human days, if not weeks, to perform. Grant a bot access to your billing system, some Excel spreadsheets, and your CRM, and ask it something like "who are my profitable customers by category and what are their trends" becomes child's play.

While it's trivial for you to ask that question and get a fairly accurate answer back in a couple minutes, behind the scenes there is a *lot* of processing going on, and far more than you'd expect. AI computing time is measured in tokens — a short question and answer might take somewhere between 200 to 2,000 tokens, and one that requires the models to do some internet research might be around 1,000 to 4,000. An agentic task, though, can easily spend*millions* of tokens on a seemingly innocuous request. How? Token amplification, a recently coined term.

In a simplified manner, because a model has no memory or cognition, every time you ask it another question in a conversation, it will re-load and process the entire exchange — everything you wrote, everything the bot replied with, and every file you uploaded. That means that additional questions in a long conversation progressively get more costly. Each question in a conversation might only need 500 tokens by itself, but reprocessing all the previous information adds up, so the second one might spend 600, and so on and so forth. The conversation as a whole uses up the cumulative number of all individual interactions, and as an added penalty: Response speed also tends to get slower as chats drag on.

The aforementioned task of generating a report will have to be run in stages, say three for looking up Excel sheets, four for the CRM, perhaps a half-dozen web searches for contextual information about products, and a good dozen intermediary processing and calculation steps. Each step tacks on potentially several thousands of tokens, and by the end of it, you may be looking at millions of tokens cumulatively spent for all the steps combined.

Costs, then, can spiral out of control very quickly — and that's assuming a best-case scenario where all of the data is easy to interpret, the model won't need any retries, and you're using a moderately powerful model rather than something like Claude Opus.

In financial terms, this means that one innocent question might spend 280,000 tokens and cost $1, with ballpark estimates at current prices. That may not sound like much, but it was *just one task.* If you have this scheduled to run every 15 minutes for a dashboard, then suddenly this costs $96*per day*, or $2,880 in a month. And that task example was fairly simple; a tricky multi-stage report might need millions of tokens, turning that $1 into, say, $10, or a grand total of $28,800. For the one report, for a limited number of users, in one department of a corporation.

That's the key reason why Anthropic, Microsoft, OpenAI, and almost every other player moved their major offerings to usage-based billing back in April, and severely limited token spends in fixed-rate plans. This generated many sticker shock events, as developers around the globe found out how much their vibe coding actually cost and were left in a daze.

In a large company using many AI agents, such costs can become prohibitive and oftentimes costlier than standard-issue human employees. Firms like Uber, Microsoft, Amazon, and Walmart, among many others, have responded by curbing AI spend. Token expenditure is suddenly an issue for both financial and engineering departments, as cost control becomes paramount. As VentureBeat succinctly puts it, for agent-heavy companies, "a prompt redesign is a margin event," and more illustratively, "a poorly bound agent loop is an outage with a credit card attached."

Although most AI outfits still offer fixed monthly pricing plans, they often come with harsh token limits. As is often the case with most fixed-pricing services, however, the most capable bot-wranglers will also inevitably be the ones burning through the most tokens, not just due to their intensive usage *per se*, but because the type of tasks they will perform will be precisely the ones hardest hit by token amplification.

This throws a wrench in the usual financial model of the casual users easily offsetting the cost of the small percentage of professionals — the pros' usage can take a serious bite off monthly profits, or chew through them entirely.

The AI companies aren't sitting still, and getting the per-token cost down is likely to be the primary task for most of their engineering teams, at this point. Prompt caching, model routing, batch processing, semantic caching, and context window management are among many technical measures that can massively cut down on token spend, each of those netting a two-digit percentage drop.

And yet, costs keep soaring for the simple reason that the smarter the models get, and the more adept people become at using them, the more complex and long-running the agentic tasks will become, adding multiple orders of magnitude to token counts.

For the time being, it looks like a losing race, despite recent advancements like Deepseek V4 Pro and V4 Flash deeply undercutting comparable Western models at up to a reported 17x for the former and 25x for the latter. Out of the major Western players, only Anthropic has predicted its first profitable quarter, though much like anyone else, it's still in the hole for many a billion for cumulative spend.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.
