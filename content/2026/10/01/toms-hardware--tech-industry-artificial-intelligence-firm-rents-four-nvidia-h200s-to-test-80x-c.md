---
title: Firm rents four Nvidia H200s to test '80x cheaper' DeepSeek claim — $13,200
  monthly GPU rental doubles Claude bill while security flaws keep code offline
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/firm-rents-four-nvidia-h200s-to-test-80x-cheaper-deepseek-claim-usd13-200-monthly-gpu-rental-doubles-claude-bill-while-security-flaws-keep-code-offline
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-01T13:17:06Z'
published: '2026-10-01T00:00:00Z'
description: The custom setup couldn't beat DeepSeek's own list price.
image: https://cdn.mos.cms.futurecdn.net/zfDV4Yc5qbdYxR9jC8U8NA-1920-80.jpg
categories:
- Technology & Software
- Hardware
- Personal Finance & Investing
- Business & Entrepreneurship
people:
- Claude Opus
- DeepSeek
- Shane Downing
- Tom
locations: []
organisations:
- API
- Call Center Doctors
- Claude Code
- DeepSeek V4.1-Pro
- Get Tom's Hardware
- Google News
- Shane Downing
- Tom’s Hardware
---

![The DeepSeek logo against a hexagonal textured background](https://cdn.mos.cms.futurecdn.net/zfDV4Yc5qbdYxR9jC8U8NA-1920-80.jpg)

The Call Center Doctors, a call center consultancy that builds and runs call floors for other businesses, rented a server with four Nvidia H200 AI GPUs to serve DeepSeek V4.1 Flash to its Claude Code agents in place of Opus 5.5, according to its test write-up. The write-up is aimed at anyone who has heard that DeepSeek is “80x cheaper” than Claude. Using its real coding mix, the firm's server topped out at around 213 tokens written per second at an on-demand cost of $440.88 per day, versus $184–$223 per day for the same work via DeepSeek’s API. The call center went back to Opus 5.5 at a lower price than the box would cost at on-demand rates.

DeepSeek’s API is priced at $0.15 per 1 million new input tokens off-peak, $0.003 cached input tokens, and $0.60 per 1 million output tokens. Peak costs are double. By comparison, Anthropic’s Claude Opus 5.5 is listed at $4 input and $20 output per 1 million tokens, with cache reads at $0.20. The consultancy used it through subscriptions and not the API.

The box’s performance was fine for one kind of work at a time in the test’s one-minute full-load runs. But the coding agents work mostly by resending the conversation, and 96% of what the agents provided the model was stale text, according to the consultancy’s logs. It takes about 1,000 old tokens for every new token written; the re-reads are cheap, but so numerous that the box was kept busy re-reading, leaving little of its time for writing new tokens.

Getting the model to run stably took five tries at 10 to 15 minutes of loading for each try. The box bills whether it’s busy or not, which is suboptimal. By our arithmetic, a standard-length month at the on-demand rate, $18.37 an hour, comes out to about $13,200. This is over twice the consultancy’s September Claude bill. Additionally, one box can only get through about 20 billion tokens a day, by the consultancy’s math, most of it re-reading, against the 51 billion the consultancy’s agents used on its busiest day.

The testing was aimed at anyone who has heard that DeepSeek is “80x cheaper” than Claude. One server running from Sept. 1–27 had 2.03 million model calls, 388.5 billion tokens read, 374.2 billion of them cached, and 393 million written, with 5,610 merged changes. The consultancy’s September Claude Code subscriptions came to about $5,500. The same 27 days of tokens on DeepSeek’s API would be between $3,500 and $7,000, depending on peak pricing, with our estimated average around $4,200 if usage is spread evenly across the week.

Set against Claude Opus 5.5’s list prices, the same tokens would come to about $140,000 by our math, over 25 times the cost of the subscription. That flat-rate discount is where the 80x went. The consultancy also priced each merged code change: about $1 on Claude, and about $0.63 on DeepSeek’s API if DeepSeek did the same work with the same tokens. Its $1.15–$4.90 estimate for DeepSeek is based on assumptions that the model would need more tokens, succeed less often, and need Claude to check its work.

DeepSeek never got to write actual code in the test. The consultancy’s reviewers kept finding ways agent code could escape the sandbox, for example via a settings file in a shared temp folder that could allow agent code to be run as admin. This meant the code-writing agents had to stay offline. Instead, DeepSeek ran only as 48 to 64 read-only reviewer agents, reading 2,377 folders and filing 32 bug reports. The box, rented at a $9.19-an-hour spot rate, was taken back by the provider within minutes of the last test ending.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Based on the V4 generation, where Pro outscored Flash, better performance from the model family can be expected with DeepSeek V4.1-Pro, which currently does not have a firm release date. This may change the math in the future, but for now there are better ways to spend on tokens than renting GPUs to run an open model.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Shane Downing](https://cdn.mos.cms.futurecdn.net/Zosi9VrDytS9FkgJiHvc69-140-80.png)

Shane Downing is a Contributing Writer for Tom’s Hardware, covering consumer storage, PC hardware, and AI.

* * This is the dumbest article I have read in weeks.Reply  
      
    This isn’t even AI slop, it’s devoid of intelligence. I hope the author doesn’t think this makes him some sort of authority on LLMs.  
      
    “The box’s performance was fine for one kind of work at a time in the test’s one-minute full-load runs. But the coding agents work mostly by resending the conversation, and 96% of what the agents provided the model was stale text, according to the consultancy’s logs. It takes about 1,000 old tokens for every new token written; the re-reads are cheap, but so numerous that the box was kept busy re-reading, leaving little of its time for writing new tokens.”  
      
    Do…. you not know how caching works? Or are you a fourth grader, because that is about the critical thinking proficiency demonstrated here.  
      
    Also the company that rented 4xH200s 24/7 to serve themselves Deepseek to their coding agents…? Equally devoid of any brain cells.  
      
    Probably taking advice from Shane Downing.
