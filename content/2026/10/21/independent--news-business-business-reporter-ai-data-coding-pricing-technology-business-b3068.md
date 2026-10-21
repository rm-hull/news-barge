---
title: AI didn’t fail your company, outdated data did
source_url: https://www.independent.co.uk/news/business/business-reporter/ai-data-coding-pricing-technology-business-b3068014.html
source_site: The Independent
source_slug: independent
scraped_at: '2026-10-21T11:48:37Z'
published: '2026-10-21T00:00:00Z'
description: THE ARTICLES ON THESE PAGES ARE PRODUCED BY BUSINESS REPORTER, WHICH
  TAKES SOLE RESPONSIBILITY FOR THE CONTENTS
image: https://static.independent.co.uk/2026/10/16/10/31/Decodo_Header-Image.jpeg?trim=0,0,0,0&width=1200&height=800&crop=1200:800
categories:
- News & Politics
- UK
- Business & Entrepreneurship
- Technology & Software
people: []
locations:
- AI
organisations:
- AI
- API
- Decodo
- Gartner
- Web Data
---

*Decodo is a Business Reporter client*

**Most technology leaders blame the AI feature when something fails, but the real issue is usually the data behind it.**

Every AI cost review looks the same. A team checks which model it’s running, prices out a cheaper alternative and counts how many tokens a task burns through. That’s where the visible savings sit, so it’s usually where the effort goes. I run Decodo, a company that gives fast-growing tech teams a web data access layer, so I see this pattern often.

The web data feeding those models barely gets a second look. When it does come up, it gets compared to the model bill and waved off as a rounding error. No one on the team connects that spend to the quality of what the model produces, because the cost of skipping it doesn’t show up right away. It shows up three months later, in outputs that are worse, and by then no one traces it back to the review where this item got cut.

That’s backward. A smaller, cheaper model running on current data will usually beat a larger model running on stale data. But stale data doesn’t announce itself the way a token count does, so it survives the audit that a slow, expensive model wouldn’t.

## **The failure that never gets diagnosed**

Here’s what that looks like in practice. A pricing agent is built to reprice against competitors every morning. It works well for the first few weeks. Then, without anyone changing a line of code, it starts making confident calls off a saved snapshot of competitor pages instead of the live site. The output still looks fine. The logic still runs. It just runs on information that stopped being true a while ago.

When someone notices the pricing is off, the postmortem goes straight to the model: wrong prompt, wrong model choice, maybe a rogue update. Almost no one asks a simpler question first, which is where the agent actually pulled its information from, and how long ago.

The answer is usually the same. A page got scraped once, when the project shipped, and the task of refreshing it never made it onto anyone’s sprint. There was no bug. There was no owner.

This is also why AI coding tools underdeliver more often than teams expect. Every model has a training cutoff, so a coding assistant is, by design, working from a documentation snapshot that’s already out of date the day it ships. According to Gartner’s research on AI code assistants, 42 per cent of engineering teams report productivity gains of only 1 to 10 per cent, and another 12 per cent see no gain at all. The Stack Overflow Developer Survey found that trust in AI-generated code accuracy fell from 40 to 29 per cent in a single year, even as adoption kept climbing. There are plenty of theories for that gap. The one that gets tested least is how old the data behind the tool actually is.

## **Not every dataset ages at the same rate**

Part of the problem is that most companies apply one refresh schedule to everything they collect, as if a competitor’s price and a regulatory filing decay at the same speed. They don’t. Think of it as a half-life – a competitor’s price might lose accuracy within hours, a product review might hold its value for a week and a regulatory filing might stay accurate for months.

Few companies tier their refresh cadence to match. A business competing on price in a fast-moving retail market needs that data refreshed hourly. A business tracking industry regulation can probably check monthly and be fine. Flatten the two into one policy, and you get the worst of both outcomes: the fast-moving data goes stale while the slow-moving data gets refreshed for no reason, burning budget in the wrong place.

This was the driving force behind Decodo’s new Web Data API. Instead of a team hardcoding a single refresh job and hoping it still makes sense a year later, the API connects the AI agent directly to the live web, so the data stays as fresh as it gets.

## **Where the fix sits**

Going back to that pricing agent: some might assume the fix is a smarter model, but it’s better to remove the saved snapshot entirely and replace it with a live connection, so the pricing decision each morning is based on that morning’s data, not whatever was true when the project launched.

Tools such as the Web Data API connect a developer to whatever part of the web an agent depends on, so no one has to remember to rerun a script by hand or notice when a page has gone stale. It handles the operational complexity of collecting publicly available web data reliably at scale, whether that’s competitor pricing, package documentation or regulatory listings, so the team building the agent can focus on the agent instead of babysitting a feed.

![what_is_decodo.mp4](https://cdn.ex.co/transformations-account/production/99589e92-e6b5-4a6b-8db4-bb0120ace3e1/e81d4b7a-6cd5-4243-aebf-e0cd6ee72449/thumbnail-360.webp)

## **The bottom line**

The hype surrounding AI isn’t the problem. Most companies underinvest in something they treat as a background task: keeping the data behind their systems as current as the decisions those systems make.

The next project that stalls at your company probably won’t fail because of the AI. Trace it back far enough, and you’ll likely find data too old to base a decision on.
