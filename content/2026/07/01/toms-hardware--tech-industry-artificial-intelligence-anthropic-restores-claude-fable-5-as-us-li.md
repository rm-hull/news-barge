---
title: Anthropic restores Claude Fable 5 as US lifts export controls — single filter
  now blocks prompt that could identify software vulnerabilities and write code to
  exploit them
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropic-restores-claude-fable-5-as-us-lifts-export-controls
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-01T14:55:48Z'
published: '2026-07-01T00:00:00Z'
description: Commerce withdrew the controls after testing confirmed weaker models
  could do the same thing.
image: https://cdn.mos.cms.futurecdn.net/QxogjHcGRhsSbmYVRAwxSo-2000-80.jpg
---

![Anthropic Claude Fable](https://cdn.mos.cms.futurecdn.net/QxogjHcGRhsSbmYVRAwxSo.jpg) 

Anthropic has restored global access to Claude Fable 5, a day after the U.S. Department of Commerce withdrew the export controls it imposed on the model on June 12th, according to a company blog post. The fix that ended an 18-day standoff was a single safety filter tuned to block one technique flagged by Amazon researchers, with Commerce's own Center for AI Standards and Innovation (CAISI) reviewing the safeguards before the controls came off.

Fable 5 returns across Claude.ai, the Claude Platform, Claude Code, and Claude Cowork today, with access on AWS, Google Cloud, and Microsoft Foundry to follow. The June 12th directive had barred any foreign national, including Anthropic's own non-citizen staff, from using Fable 5 or the more capable Mythos 5, which it’s built on. With no way to verify the nationality of its users, Anthropic pulled both models worldwide.

The contentious technique was flagged by Amazon researchers, who found a way to prompt Fable 5 into identifying software vulnerabilities and, in one case, writing code demonstrating how one could be exploited. Anthropic trained a new classifier that blocks that specific technique in more than 99% of cases and reroutes flagged requests to the older Opus 4.8. The company said the change also catches more benign coding and debugging requests as a side effect.

The classifier targets the reported prompt and not the model’s capabilities. Fable 5 can still identify the vulnerabilities in the Amazon report; the filter detects the request and reroutes it rather than stripping the ability from the model. Detection-based safeguards are also what were defeated to trigger the ban in the first place, and a classifier that’s tuned to one known technique does nothing for the ones not yet found. Anthropic concedes that no model can be made fully robust to jailbreaks and that it expects more to surface.

Anthropic's review, conducted with the government and Amazon, found that Opus 4.8, OpenAI's GPT-5.5, and China's Kimi K2.7 could identify the same vulnerabilities. Every model that it tested, including Haiku 4.5, Sonnet 4.6, and several Opus versions, could reproduce the single exploit demonstration, backing the argument that Mythos-class cyber capabilities were oversold.

Fable 5's return reclaims benchmark positions that Chinese lab Z.ai's GLM-5.2 had held by default while Fable was offline, including the top accessible score on the AA-Briefcase multi-week task test. Mythos 5, which carries fewer guardrails and stays limited to Project Glasswing partners, returned to a set of U.S. organizations on June 26th.

Anthropic also opened a HackerOne program for researchers to report new Fable 5 jailbreaks, and it committed to giving designated government partners earlier access to test future frontier models before release. For Pro, Max, Team, and select Enterprise plans, Fable 5 counts toward up to 50% of weekly usage limits through July 7th, after which it moves to usage credits.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or**add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Luke James](https://cdn.mos.cms.futurecdn.net/C4FAi2KzwaGLUrBqzX5aBM.png)

Luke James is a freelance writer and journalist. Although his background is in legal, he has a personal interest in all things tech, especially hardware and microelectronics, and anything regulatory.
