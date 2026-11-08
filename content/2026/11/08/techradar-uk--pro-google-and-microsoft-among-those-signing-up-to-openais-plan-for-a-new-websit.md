---
title: Google and Microsoft among those signing up to OpenAI's plan for a new website
  crawling standard — including opting-out of internet scraping
source_url: https://www.techradar.com/pro/google-and-microsoft-among-those-signing-up-to-openais-plan-for-a-new-website-crawling-standard-including-opting-out-of-internet-scraping
source_site: TechRadar UK
source_slug: techradar-uk
description: One robots.txt line could soon stop scraping
image: https://cdn.mos.cms.futurecdn.net/ia5D8nxabP2wLrLZKcdekh-1197-80.jpg
published: '2026-11-08T00:00:00Z'
scraped_at: '2026-11-08T17:55:32Z'
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Andy Stone
- Brent Hecht
- Cloudflare
- Kevin Kelley
- Mustafa Suleyman
- Sam Quigley
locations: []
organisations:
- AI Overviews
- AI Preferences
- AIPREF
- Anthropic
- Cloudflare
- Copilot
- EU
- Gemini
- Google
- Google-Extended
- IETF
- Internet Engineering Task Force
- Mercury News
- Meta
- Microsoft
- News/Media Alliance
- OpenAI
- Penske Media
- Perplexity
- Rolling Stone
- Search Engine Journal
- SiliconANGLE
- TechRadar Pro
- The New York Times
---

![site search](https://cdn.mos.cms.futurecdn.net/ia5D8nxabP2wLrLZKcdekh-1197-80.jpg)

* **Google, Microsoft, OpenAI, and Anthropic say they will honor one robots.txt group as a cross-company opt-out from AI training**
* **It governs how content is used rather than whether bots can crawl it, defaults to allowing training, and does nothing for content already scraped**
* **Anthropic has started implementing it, OpenAI promises to do so in the coming months, Microsoft starts February 1, 2027, and Google targets 2027, while Meta is supportive but uncommitted**

Google and Microsoft have joined OpenAI and Anthropic in promising to honor a single line in robots.txt that tells AI developers whether a website's content can be used to train their models.

Until now, a site that wanted to say no had to write a rule for each company's crawler, and sometimes for several crawlers run by the same company. The shared signal is meant to replace that sprawl with a single entry that every participating provider reads the same way.

That is genuine progress for overworked webmasters, but the promise is narrower than much of the coverage suggests: The new line states a preference about how content may be used rather than stopping bots from fetching it; it is not an approved standard, does nothing about content already collected, and none of the four major players fully honor it yet.

## Doing the bare minimum with differing definitions of what the commitment entails

OpenAI's announcement drew much of the attention, but the company casts itself as one participant among several in an Internet Engineering Task Force (IETF) effort, and the mechanism isn't its own. It comes from an Internet-Draft published the same day by Kevin Kelley of Anthropic, which names a policy token, "\_\_usage\_ai-training", in the User-Agent line of an otherwise ordinary robots.txt group.

Training is defined by the IETF's AI Preferences (AIPREF) working group as the process of changing a generative model's learned parameters, excluding models used purely for tasks such as classification or ranking. OpenAI describes what it will honor as "foundational generative AI training," which sounds narrower than the draft's definition.

Calling it a standard may be premature: The IETF's own tracker labels the document an individual draft that the IETF has not endorsed, and that has no formal standing, and it lapses on May 3, 2027 unless revised.

Anthropic is the only one of the four major AI players to say it has started. OpenAI aims to implement the signal over the next few months but has given no date. Microsoft will begin honoring the shared preference as it crawls from February 1, 2027, while Google is aiming for 2027.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Each company is also wiring the line into its own controls differently. Google says that when a site uses the shared token to opt out without separately specifying Google-Extended, it plans to treat that "as if the publisher had disallowed Google-Extended." Because Google-Extended also governs grounding in Gemini Apps, a site that only wants to stop training could lose its citations and clicks in Gemini answers too, and Search Engine Journal notes that Google's documentation describes no way to separate the two.

Interestingly, Microsoft goes the other way. It adopts the shared line for training but adds a separate, page-level AI Grounding preference, including a DisallowExtended option that keeps content available to its own products such as Copilot while excluding the grounding services it sells to other businesses.

Meta, not one of the four, has been warmer than it has been about its commitment. Its VP of communications, Andy Stone, called the common signal "an important step," but *SiliconANGLE* reports the company has not committed to honoring it. The timing is awkward: Meta has pushed back to November 20 revised commercial terms that would let it crawl websites linked to its business accounts, after a backlash forced it to strip training from the listed uses.

With training removed but not expressly banned, Sam Quigley of the News/Media Alliance told the Mercury News last month, "It's still potentially on the table."

## Opting out of AI data scraping: wishful thinking or a step in the right direction?

Much of the coverage has billed this as a way to opt out of being scraped outright, but it really isn't.

The draft is explicit: "This policy token is not a directive for crawling behavior." Bots can keep fetching every page, and the draft merely permits a crawler that gathers content only for training to skip pages it can't use. Stopping the crawlers themselves still takes the per-bot rules sites rely on today, which is why OpenAI, Google and Anthropic all stress that their existing controls aren't going anywhere. Microsoft puts it most plainly: "These settings govern use of content, not crawl access."

These further caveats matter at a time when the commitment itself is both voluntary and interpretations and pledges vary across the board even as certain players have higher exposure than others.

*The New York Times* sued OpenAI and Microsoft in December 2023, and both companies are invoking fair use in their defense. Anthropic, whose engineer wrote the draft, agreed to pay $1.5 billion to settle authors' claims over pirated books used in training, and Penske Media, owner of Rolling Stone, sued Google over AI Overviews in 2025.

It also relies on crawlers choosing to comply; the draft lets private agreements override it, and in 2025 Cloudflare accused Perplexity of disguising its crawlers to scrape sites that had blocked it, a charge the latter denied.

Microsoft's place in the coalition is arguably the most awkward: In 2024, its AI chief Mustafa Suleyman described open-web content as "freeware" for training, carving out only sites that explicitly object, which is roughly the exception this signal now formalizes. Unsealed filings in the Times case also show that a Microsoft director, Brent Hecht, described AI scraping in a 2023 internal memo as possibly "the largest theft of labor in human history."

The wider market, meanwhile, has been moving toward enforcement and payment rather than polite requests. Cloudflare has blocked AI crawlers by default for new customers since July 2025 and lets participating sites charge them per crawl. Google also says the shared token aligns with the EU's code of practice for general-purpose AI, which treats robots.txt as publishers' primary machine-readable opt-out, a sign that regulators, not just goodwill, are pushing the big labs to listen. For bots that ignore robots.txt entirely, we have rounded up heavier options, from login walls to IP rate limiting.

For now, one line that the biggest AI companies agree to read is a real step forward for honest crawlers and the people who run websites. But it is a request rather than a lock; it only looks forward, and it comes with none of the payment publishers have spent years fighting for.
