---
title: 'Future generations of AI systems will continue to accelerate'': New report
  claims that by 2030, the world could generate approximately 317 billion AI tokens
  every second'
source_url: https://www.techradar.com/pro/future-generations-of-ai-systems-will-continue-to-accelerate-new-report-claims-that-by-2030-the-world-could-generate-approximately-317-billion-ai-tokens-every-second
source_site: TechRadar UK
source_slug: techradar-uk
description: Five billion AI tokens a second today, 317 billion by 2030?
image: https://cdn.mos.cms.futurecdn.net/kntXJzuBjvVTZvqgBeCKfN-1920-80.jpg
published: '2026-11-21T00:00:00Z'
scraped_at: '2026-11-22T01:12:32Z'
categories:
- Technology & Software
- Business & Entrepreneurship
- Personal Finance & Investing
people:
- Eric Spanneut
- Jeff Fochtman
- Jim Schneider
- Linglan Wang
- Pua Khein-Seng
- Sundar Pichai
locations:
- Dynamo
organisations:
- AI
- Alphabet
- GPU
- Gartner
- Goldman Sachs Research
- Goldman's
- Google I
- I/O Fund
- LMCache
- NAND
- Nvidia
- Phison
- SanDisk
- Sandisk
- TechRadar Pro
- WEKA
---

![Data center](https://cdn.mos.cms.futurecdn.net/kntXJzuBjvVTZvqgBeCKfN-1920-80.jpg)

* **SanDisk estimates AI systems will produce about 150 quadrillion tokens in 2026 and could hit 10 quintillion a year, or 317 billion per second, by 2030**
* **The 2026 baseline squares with Google's own disclosures and independent tallies, but the model's inputs are unpublished and labeled as 'illustrative'**
* **SanDisk's 2030 figure is roughly seven times Goldman Sachs Research's forecast of 120 quadrillion tokens a month**

SanDisk has put a number on the AI boom, and it is a big one: in its Tokenomics 2030 outlook, the flash memory maker estimates AI systems worldwide will produce around 150 quadrillion tokens this year, or roughly five billion every second, and by 2030, it believes annual output could approach 10 quintillion tokens, or about 317 billion per second.

The figures come with a footnote that matters more than the headline: SanDisk says they are drawn from its own internal analysis and estimates and are "intended for illustrative purposes only," and the outlook names no outside data source.

This matters when you consider who is doing the counting: a company pitching its own enterprise SSDs as part of the infrastructure all those tokens will need.

## How SanDisk built its number and why it has limitations

A companion post by SanDisk's Jeff Fochtman, says Eric Spanneut, the company's senior vice president of product management, put together the team behind the model.

Rather than starting from forecasts of how much AI people will want, the model asks how much token output the world's infrastructure could realistically support. Its inputs are described only in broad strokes: the power directed toward AI inference, the size and capability of the accelerator fleet, compute and memory bandwidth, networking and storage, and expected gains in utilization and software efficiency.

That makes 317 billion tokens per second closer to a capacity ceiling than a demand forecast, and SanDisk has not published the assumptions underneath it, such as how many gigawatts it expects to be serving inference in 2030.

The precise-looking figure is also less precise than it seems, ironically: 10 quintillion tokens a year divided by the roughly 31.5 million seconds in a year gives 317 billion, so the headline number is a unit conversion of a round estimate. The growth it implies is more than 60-fold in four years, meaning global token output would have to nearly triple every year until the end of the decade, an ambitious take to say the least.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The 2026 baseline, at least, looks plausible: At Google I/O in May 2026, Alphabet CEO Sundar Pichai said Google alone was handling 3.2 quadrillion tokens a month, up from 480 trillion a year earlier. Converting that to a per-second basis nets you roughly 1.2 billion tokens per second, or about a quarter of SanDisk's global estimate from a single company, with the caveat that Google talks about tokens processed, SanDisk about tokens generated, and neither spells out exactly what it counts.

Alphabet's Q3 2026 earnings remarks added that its first-party model APIs alone were running at nearly 32 billion tokens per minute, 40% more than the previous quarter and over four times the year-earlier rate. Independent tallies land in the same neighborhood. In July, I/O Fund cited a tracker putting industry-wide volume near 370 trillion tokens a day, or about 135 quadrillion a year, though it did not explain how it compiled that figure.

One could even argue that SanDisk is being restrained in its projections: Google's sevenfold year-over-year jump is far faster than the roughly 2.8x annual growth baked into the 2030 figure, so the outlook effectively assumes today's pace will cool in the near future.

On the other side of the spectrum, it seems extremely aggressive: In May, Goldman Sachs Research projected that token consumption would grow 24-fold between 2026 and 2030 to reach 120 quadrillion tokens per month, driven largely by AI agents. Converted to a monthly rate, Sandisk's 10 quintillion a year comes to about 833 quadrillion, roughly seven times Goldman's figure.

Part of that gap sits in the starting point: Goldman's multiple implies a 2026 base of around 5 quadrillion tokens a month, against Sandisk's 12.5 quadrillion, and Goldman's base already looks light given Google's own disclosure the same week. The rest comes from SanDisk simply assuming much faster growth.

The bigger question is what all of these tokens actually measure. SanDisk's own companion post presents tokens as a practical gauge of AI computational work rather than a measure of intelligence or value, and admits there is no universal formula for turning token output into storage demand.

Token counts also climb when reasoning models think at length or when people repeatedly re-prompt to get something usable, a habit one TechRadar Pro contributor recently branded as "tokenmaxxing." A world producing 317 billion tokens per second would certainly be doing more AI work. It would not necessarily be doing 60 times more useful work.

## Why is a flash company interested?

The commercial logic behind the outlook is the KV cache, the attention state a model builds as it reads a prompt, which agents need to keep around across long, multi-step sessions.

SanDisk argues that keeping all of it in scarce, high-bandwidth memory will not always be practical or economical, and that enterprise SSDs can serve as a larger tier for selected cache data so systems avoid recomputing work they have already done. The PR pitch that accompanied the outlook goes further, casting SSDs as "token batteries."

The engineering case is real, but it is hardly unique to SanDisk. LMCache, Nvidia's Dynamo framework and BlueField-4 CMX platform, WEKA and Phison already persist KV cache to storage, and Nvidia argued after this summer's Future of Memory and Storage conference that storage now matters as much as the silicon it feeds, since serving KV cache from flash rather than DRAM lets each GPU support longer contexts and more simultaneous users.

The outlook's most important input is also ironically its weakest link: SanDisk's companion post calls power the starting constraint, and Gartner analyst Linglan Wang has warned that "AI capacity is now constrained by power availability."

Goldman's Jim Schneider expects chip shortages to last at least another year. Even the storage tier SanDisk is promoting is squeezed, with Phison CEO Pua Khein-Seng relaying a NAND maker's estimate that new capacity takes around four years to reach mass production, pushing supply difficulties out to 2030.

None of that makes the 317 billion figure wrong, but it does clarify what it is: a storage vendor's estimate of what the world's AI infrastructure could produce if it gets built, powered, and kept busy at full capacity. The baseline is credible, and the direction of travel is not in doubt. The destination, for now, rests on assumptions SanDisk has not published yet and therefore are not open to scrutiny at the time of writing.
