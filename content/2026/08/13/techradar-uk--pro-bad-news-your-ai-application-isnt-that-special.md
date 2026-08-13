---
title: 'Bad news: your AI application isn''t that special'
source_url: https://www.techradar.com/pro/bad-news-your-ai-application-isnt-that-special
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-13T17:08:28Z'
published: '2026-08-13T00:00:00Z'
description: Application startups are vulnerable to coming consolidation
image: https://cdn.mos.cms.futurecdn.net/6t9Lsf3QWte55CdyiDs97L-2560-80.jpg
---

![A robot's hand typing on a laptop keyboard](https://cdn.mos.cms.futurecdn.net/6t9Lsf3QWte55CdyiDs97L.jpg) 

![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png) 

There are more than 70,000 AI companies operating today.

Most of them will not exist in five years.

Before you can see why — or figure out whether yours is one of them — you need a distinction the market keeps blurring.

Strip away the pitch decks and there are really only two types of AI system being built today.

CEO and founder of McMillanAI.

The first is AI infrastructure: the orchestration and governance technology that makes AI usable at scale. In plain terms, this is the plumbing — agent frameworks, model routing, evaluation and monitoring tools, guardrails, and the controls that let a large organization use AI safely.

It sits between the foundation models and the end user, and it is where an enormous amount of venture money is going right now.

The second is the surface application: the tool an actual person uses to do actual work. The underwriting assistant, the contract reviewer, the sales copilot. The thing with a login screen and a job to do.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

What I see in the market is a blending of the two. Some firms are selling architecture.

Some are selling tools. Many are trying to sell both, on the theory that owning the whole stack is the safest position.

And while this market is filled with tremendous exuberance with seemingly everyone starting an AI company, I am very skeptical that many of these firms will ever see profitability as history offers a strong counter.

We've run this experiment twice.

## The past and the future

The dot-com era ran the first version of this experiment, and its final tally is worth stating plainly. Researchers estimate that roughly 50,000 startups were founded in the United States between 1998 and 2002 to commercialize the internet.

Of those, something like 8,000 attracted venture funding. About 1,700 internet-related companies made it to an IPO across the whole era — 585 in 1999 and 2000 alone — and at the peak, only about 14 percent of the tech companies going public were profitable.

By late 2002, most internet stocks had lost more than three-quarters of their value and roughly 1.7 trillion dollars had been wiped out. And the number of enduring, large-scale winners from that entire cohort — Amazon, eBay, Priceline, Expedia — you can count on two hands. Run the funnel: 50,000 founded, 8,000 funded, 1,700 public, fewer than ten giants.

A real gold rush works the same way: a few strike it rich, some make a living, and most go home with less than they brought. This is important to remember for everything that follows.

If that funnel looks like a quirk of one bubble, it is not — it is how markets distribute winnings everywhere. Hendrik Bessembinder at Arizona State studied every U.S. stock since 1926, more than 25,000 companies, and found that the best-performing 4 percent account for all of the net wealth the stock market has ever created; the other 96 percent, taken together, did no better than Treasury bills.

Just 90 companies — a third of one percent — produced more than half of it, and the majority of stocks lost money outright over their lifetimes. The market wins; almost no individual company does. Keep that in mind every time someone tells you AI will create trillions in value. It will. That says nothing about whether any particular company captures a dime of it.

## The example of cloud

Cloud computing is the sharper rerun. In the early days there were hundreds of cloud providers and a thriving ecosystem of middleware companies selling the connective tissue — provisioning tools, management layers, monitoring platforms.

Today three companies control roughly two-thirds of the cloud market, and their share grows every year.

And here is the part that matters for AI: the middleware layer did not consolidate alongside the platforms. It was absorbed by them. The hyperscalers built the management consoles, the monitoring, the orchestration, and shipped it as a feature. The companies whose entire business was cloud plumbing were acquired cheap or squeezed out.

Meanwhile, the application layer on top of that consolidated infrastructure exploded. Thousands of SaaS companies built durable, profitable businesses without owning a single server. The bottom of the stack ended up in a few hands. The top produced thousands of winners.

## It has already happened once inside this stack

If cloud feels like ancient history, look at the data layer — the foundation every AI system sits on. That consolidation already occurred, and it finished recently. The "modern data stack" boom of the last decade funded hundreds of startups selling pipelines, catalogs, transformation tools, and warehouses.

Today the independent tier has settled to exactly two companies at scale: Snowflake and Databricks, each running at roughly five billion dollars in annual revenue, with the hyperscalers’ native offerings holding most of the rest of the market. Nearly everyone else was acquired, absorbed as a platform feature, or left scraping for the remainder.

And notice the shape it settled into. The top five data platforms — Snowflake, BigQuery, Redshift, Databricks, and Microsoft’s offering — hold roughly two-thirds of the market. That is almost exactly where cloud landed: three players, about two-thirds of the market, a long tail fighting over the rest.

Two different layers, a decade apart, ending in the same proportions. That is not a coincidence. It is what happens when competing takes huge capital and the platforms can build whatever sits next to them. Expect the AI orchestration layer to end up the same way.

The consolidation was driven as much by the buyer as by the vendors. Large enterprises learned that scattered data is expensive data: every additional platform meant another copy of the truth, another integration, another security review, another contract.

So CTOs stopped buying data tools one team at a time and started making strategic platform decisions — pick one or two providers, consolidate the estate onto them, and hold that line. A single source of truth became an explicit architectural goal at most large companies, and once thousands of enterprises were making that same decision, the market had no room left for a long tail of vendors.

Look at what it took for Snowflake and Databricks to survive that consolidation: enormous capital, the fact that customers’ data lives on their platforms and is costly to move, and deep ties into how their customers work every day. You can survive as an independent alongside the hyperscalers — but only by becoming one of the few names a CTO puts on the strategic list, and almost nobody makes that list.

## The same consolidation is coming for AI

Apply that pattern to the two types of AI company and the forecast writes itself.

The infrastructure layer — orchestration and governance — will consolidate down to a few. Not because the current tools are bad, but because this layer sits directly in the expansion path of the biggest players in technology. The model providers and hyperscalers have every incentive to build orchestration, evaluation, and governance into their platforms, and they are already doing it. Every capability that today justifies a standalone infrastructure startup is a roadmap item at a company with a hundred times the resources and a direct line to the same customers.

If you are building an architecture-only solution, this is the uncomfortable implication: you are likely to be taken out by one of the big players. Maybe you get acquired, if you are early and lucky. More often, the platform simply builds what you sell and includes it for free. Either way, orchestration and governance alone is not a business you can hold. The only real question is how long you have.

Which leaves the application layer as the open field. And this is the counterintuitive part: infrastructure consolidation is good news for application builders. When orchestration and governance become cheap, standardized, and built into the platforms, the cost of building a serious AI application collapses — just as commodity cloud ignited the SaaS boom. We are already seeing a massive increase in the number of AI applications getting built, and most will likely not survive.

## Better software, worse odds

Part of what makes this cycle different is how little it costs to enter. Building serious software used to take millions in capital and a room full of engineers — a filter that limited how many companies could even try. Today a handful of people with AI tools can ship in weeks what took a funded startup a year.

So new ventures are multiplying, not because there are more good ideas, but because the cost of trying has collapsed. The scale tells the story: more than 70,000 AI companies operate globally today, roughly 18,000 to 30,000 of them in the United States alone.

The comparison to the dot-com era’s 50,000 is not perfectly apples to apples — that was a five-year founding total for one country, this is a snapshot of companies operating worldwide right now — but the order of magnitude is the same, this wave is global, and the count is still climbing.

Here is the twist that makes the coming shakeout more brutal, not less: the software being built is genuinely good. This is not the dot-com era, where half-finished products hid behind splashy marketing. The tools are now so powerful that quality is the baseline — which means quality has stopped differentiating anything. When every product is polished, capable, and shipped fast, none of that separates you from the next founder who did the same thing last month.

And that is precisely why so few founders see the danger. Every one of them genuinely believes they are building something singular — and by their own measure, they are right. They compare their product to what came before: the clunky incumbent, the manual process, the way the work used to get done. Against that benchmark it looks revolutionary.

What they never compare it to is the tens of thousands of other teams looking at the same models and the same problems, building virtually the same thing at the same time. Measured against the past, every AI product is remarkable. Measured against the field, almost none are. More entrants than either previous cycle, all building excellent software, almost none of it distinguishable.

That is the setup for the largest culling yet, and it will run almost entirely on the moats, because there is nothing else left to separate the winners from the losers.

## The delusion of special

I see this up close. I have this conversation with application founders every week, and it always goes the same way. They believe the quality of what they built is their moat: the product works, customers love it, nothing else on the market feels as good.

All of that can be true, and none of it protects them. Quality can be copied. The same tools that let them build an excellent product in months let a competitor build one in weeks. A few founders have built something that truly stands alone, but I just can’t see many finding a way to real profitability.

There will be some winners, but I think they will need to rest on three key differentiators:

**1. Data**. Not data you scraped or licensed — proprietary data your business generates by operating: claims histories, transaction flows, patient outcomes. If your system gets smarter from data competitors cannot obtain at any price, you compound. If you are building on the same public internet as everyone else, you do not.

**2. Distribution**. If you already own the customer relationship — an installed base, a trusted brand, an embedded sales channel — you can put an AI product in front of buyers faster and cheaper than any startup. This is why incumbents are more dangerous in this cycle than the last one. The startup has to build the product and buy the audience. The incumbent only has to build the product.

**3. Integration into workflows**. The one people underestimate. Companies that wire themselves into how work actually gets done — the approvals, the systems of record, the daily habits of thousands of employees — become painful to remove even when a rival ships something better. Switching costs are not glamorous, but they have protected enterprise software for thirty years, and they will protect AI applications too.

Have one of these and you can build a durable business on commodity infrastructure. Have two and you can build a great one. Have none and you are likely running out of time.

## Your toughest competitor is your customer

And here is what makes the application layer even harder than the dot-com or SaaS eras: surface applications are not just competing with other vendors. They are competing with the companies they are trying to sell to. The same commodity infrastructure that makes it easy for a startup to spin up an AI application makes it just as easy for the buyer to build one internally.

Every enterprise pitch now runs into a question that barely existed in the SaaS era: why would we buy this when a small internal team could build it in a quarter?

And here is the uncomfortable part. The three advantages that decide the application winners — distribution, proprietary data, embedded workflows — are precisely what the buyer already has. The enterprise owns its data. It is its own distribution. It controls its own workflows. The customer starts the build-versus-buy conversation holding every moat you are trying to claim.

A surface application does not just need to be better than its competitors. It needs to be so much better than what the customer could build themselves that buying beats owning — and that bar rises every time the underlying infrastructure gets easier to use.

## Know which company you are

I am not going to pretend to know which specific firms win. But the structure of the outcome is already visible, because we have now watched it three times — dot-com, cloud, and the data layer: infrastructure consolidates to a few, applications proliferate, and the survivors are the ones holding data, distribution, or workflow integration that cannot be copied.

So the first question is not "is my product good?" It is "which of the two companies am I?" If you are infrastructure, your realistic endgame is being bought or being bypassed — plan accordingly. If you are an application, the model is not your moat and the product probably is not either.

So what is?

## The good news, and who gets it

One clarification before closing, because everything above can read as pessimism about AI itself. It is the opposite. The technology will create enormous value, and the markets built on it will grow. The open question is who keeps that value, and a century of evidence gives a consistent answer: mostly the consumers of a technology, not its producers.

William Nordhaus at Yale measured this across decades of American innovation and found that producers capture only about 2 percent of the total value their innovations create — the rest flows to the people and businesses that use them. Railroads transformed the economy and ruined most of their investors. Airlines moved the world and destroyed capital for a hundred years. The internet made a handful of platforms rich — and made every company that deployed it more productive.

This cycle is already tracing the same shape: the infrastructure layer consolidates, prices its scarcity, and books historic profits, while the application layer competes and hands its margin to the buyer.

That is the real ending of this story. The coming massacre of AI companies and the coming growth of the AI economy are the same event, seen from opposite sides of the table. If you sell AI, the funnel is your problem and the moats are your only defense.

If you buy AI, the competition among 70,000 firms is working precisely in your favor: every improvement, every price cut, every copied feature moves value from their side of the table to yours. The bad news in this article is only bad depending on which chair you sit in.

*This article was produced as part of**TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:**[https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
