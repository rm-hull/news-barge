---
title: AI agents aggressively tried to hack US and Canadian government websites
source_url: https://www.techradar.com/pro/security/ai-agents-aggressively-tried-to-hack-us-and-canadian-government-websites
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-02T18:00:19Z'
published: '2026-10-02T00:00:00Z'
description: They were looking for data, and they don't take no for an answer
image: https://cdn.mos.cms.futurecdn.net/6t9Lsf3QWte55CdyiDs97L-2560-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Transluce
locations:
- California
- Illinois
- Kansas
- Maryland
- New York
- Texas
- US
- USA
organisations:
- AI
- API
- BleepingComputer
- Bureau of Economic Analysis
- Canadian Centre for Cyber Security
- Census Bureau
- Department of Education
- DseWiki
- Library and Archives Canada
- OpenAI Research
- Reuters
- TechRadar Pro
- The Washington Post
- Transluce
- US Department of Education
---

![A robot&#039;s hand typing on a laptop keyboard](https://cdn.mos.cms.futurecdn.net/6t9Lsf3QWte55CdyiDs97L-1920-80.jpg)

* **AI agents repeatedly hit government sites, escalating to SQL injection after access failures**
* **US and Canadian authorities confirmed no compromise despite high-volume probing attempts**
* **Researchers warn autonomous bots increasingly bypass controls to retrieve restricted data**

AI agents simply won’t take ‘no’ for an answer. Security researchers from nonprofit Transluce found bots making numerous attempts to hack US and Canadian government websites in search of private information.

In a new report, Transluce singled out two incidents: one against the US Department of Education, and one against Library and Archives Canada. Both seem to have failed, though.

## SQL Injection shenanigans

The firms report noted the bots were most likely tasked with retrieving data (not hacking for the sake of hacking), so there is a chance whoever gave the order did not mean to be malicious.

On June 17 2026, AI agents went looking for school statistics, making more than 200,000 requests to a US Department of Education website. Transluce believes this was part of a Google DeepSearchQA benchmark question about school counselors and race-related bullying. When that failed, due to various security roadblocks, they tried the next best thing - SQL Injection.

“In the 40 seconds leading up to the SQL injection, there were a series of requests containing a variety of unusual state ID inputs,” the researchers said, stressing that they don’t imply malicious intent and that the “attack” needs to be placed into context.

The Department of Education was notified on September 25, and later confirmed no impact.

Investigating the matter further, they discovered a similar pattern elsewhere. On May 28 and June 9, an AI bot made some 900 requests towards Library and Archives Canada. Apparently, it was looking for Canadian divorce records generated between 1905 and 1911. When these requests failed, the AI bot tried to deliver multiple SQL injection payloads, as well.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

These attempts failed, too, as the probes apparently returned empty pages. The Canadian Centre for Cyber Security also confirmed that the attacks were unsuccessful. “There is no indication that government systems have been compromised at this time,” the Canadian Centre for Cyber Security said, BleepingComputer reports.

Similarly to the US Department of Education incident, this one, too, has hints of OpenAI’s ChatGPT, but attribution has not yet been confirmed. In a statement given to The Washington Post, OpenAI said it was looking into the reports and has already made contact with Canadian officials.

## No means no

These two incidents just highlight what seems to be a broader trend - AI agents actively targeting US federal and state government websites, as well as resources belonging to other countries.

According to Transluce, bots have been hard at work, trying to extract data from different government websites, not fully understanding that “no means no”. They keep trying different things: massive request volumes, modified URLs, disposable email addresses, different techniques at bypassing anti-bot systems, guessing downloadable file names, and even reusing exposing credentials.

These activities have been recorded across the USA - California, Kansas, Maryland, Illinois, Texas, New York. One AI agent allegedly set up a temporary email address and tried to register for an API key with the Bureau of Economic Analysis using the name “OpenAI Research”. Another one tried to reuse exposed API keys to pull data from the Census Bureau.

Last month, it was reported that an OpenAI agent broke into the website of the Australian government, an incident which was described as “scaling the fence”. The bot apparently accessed internal infrastructure and wrote files to an internal server but exactly what it wrote, how it obtained the access, and precisely which technical mechanism it used, is still not public knowledge.

Once inside, it accessed both public and non-public files, but individual medical data was not accessed and the system itself was not compromised, the Australian government said.

In May 2026, OpenAI agents effectively took over a German-language programming wiki (DseWiki), making more than 15,000 edits and repurposing pages as a communications hub where they discussed bypassing restrictions. Reuters reported that the agents even created backup pages when moderators tried deleting their content.

*Via* * BleepingComputer*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
