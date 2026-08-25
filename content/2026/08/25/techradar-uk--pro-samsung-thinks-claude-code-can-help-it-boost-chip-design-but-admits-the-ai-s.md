---
title: Samsung thinks Claude Code can help it boost chip design — but admits the AI
  still makes some worryingly big mistakes
source_url: https://www.techradar.com/pro/samsung-thinks-claude-code-can-help-it-boost-chip-design-but-admits-the-ai-still-makes-some-worryingly-big-mistakes
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-25T01:48:15Z'
published: '2026-08-25T00:00:00Z'
description: A different kind of numbers game
image: https://cdn.mos.cms.futurecdn.net/new7kozVtx7yeGs3pWmbfd-1264-80.png
---

![Samsung Logo](https://cdn.mos.cms.futurecdn.net/new7kozVtx7yeGs3pWmbfd.png) 

- **Samsung System LSI division uses Anthropic's Claude Code to reportedly slice working processes**
- **However the tool also apparently downgraded an error message instead of fixing it, rolling back unrelated finished work, and tried to edit code it was not authorized to touch**
- **Samsung's engineers currently review everything the tool produces before it is published elsewhere or affects existing chip designs**

Samsung's System LSI division has reportedly used Anthropic's Claude Code to cut a month-long system-on-chip verification job to about two days.

While Samsung's division has about 6,000 employees, its main rival in mobile application processors, Qualcomm, has roughly 52,000 employees, and the former is apparently not above using AI to bridge the gap as a force multiplier.

A report from South Korean business outlet *Chosun Biz (KR)* claims System LSI leveraged Anthropic's Claude Code by offering it to its software developers in May 2026, then extended it to semiconductor design and verification work, a move which led to much faster progress on certain projects, while also producing interesting failures on other fronts.

## A mix of triumphs and gaffes

Samsung's approach, for the most part, makes an excellent case for future AI use, as one verification project expected to take more than a month was finished in about two days, something the company internally tracked as a 15x gain in efficiency.

More interestingly, a second-year engineer with no prior exposure to either the tool or USB communication standards built USB device models for an emulator and adapted an Android driver in a single day, work whichwas normally estimated to take about a month.

Samsung has also had an interesting interaction using Claude Code to verify the internal data connections of a custom system-on-chip. The job was complex in more ways than one: the customer wanted a new architecture, third-party design IP was involved, the documentation was nonstandard, and the RTL for the DRAM controller had not arrived on schedule, making for a perfect storm for Claude.

Claude built a virtual verification environment using placeholder blocks in place of the missing RTL, along with test scenarios, so that engineers could start catching errors before the real design existed.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

On the other side of the equation, Claude Code did, in certain cases, try to operate outside the boundaries of its assignments, often resulting in incorrect output or an error, or, in one case, an attempt to modify RTL circuit code it had no authorization to touch. It also rolled back unrelated finished work and downgraded an error message instead of fixing it.

The former is particularly egregious because, unlike software updates, once silicon ships, it can rarely be repurposed or 'updated' to bypass design flaws. Samsung has responded by ensuring engineers manually inspect and verify the output of Anthropic's models before using it elsewhere.

More interestingly, Claude Code isn't the only tool in the building, even if it seems to get the most attention here; Samsung also uses Google Gemini and OpenAI's ChatGPT across research, manufacturing, marketing, and support.

Despite this, Samsung does not use either of the other models to check input from the former; trusted engineers on-site do that instead in an industry where errors that are not picked up during reviews could be costly for a company that is currently attempting to maximize efficiency, even as its System LSI has posted losses in its SoC business and its flagship Galaxy Z Fold 8 runs Qualcomm's silicon under the hood.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Rahim Amir](https://cdn.mos.cms.futurecdn.net/9xKZFBamtEZKSChRvywbPB.png)

Rahim Amir is a UAE-based tech writer who enjoys building PCs as much as he enjoys writing about them. He has been professionally writing about PC hardware since 2023, focusing on buyer’s guides, hardware reviews, and sponsored content and features related to tech.

Having built hundreds of gaming PCs and being an avid gamer in his spare time, Rahim tends to have stronger opinions about hardware than most. This is particularly on display when he gets his way with powerful, but minimalistic RGB builds even as Small Form Factor (SFF) PCs come a close second.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
