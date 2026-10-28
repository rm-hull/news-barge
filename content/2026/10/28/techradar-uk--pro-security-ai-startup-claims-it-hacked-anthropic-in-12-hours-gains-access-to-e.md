---
title: AI startup claims it hacked Anthropic in 12 hours, gains access to employee
  details and internal messages
source_url: https://www.techradar.com/pro/security/ai-startup-claims-it-hacked-anthropic-in-12-hours-gains-access-to-employee-details-and-internal-messages
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-28T19:22:59Z'
published: '2026-10-28T00:00:00Z'
description: Agents found a way in through third-party business software
image: https://cdn.mos.cms.futurecdn.net/scxFkyfYSQbrtGvqrmFqgU-2560-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
- Careers & Productivity
people:
- Claude
- Darin Fredde
- Gavin Kliger
- Jack Stein
- Jacob Krell
- Luke Farritor
- Marko Elez
locations:
- America
- Cathedral
- HackerOne
- US
organisations:
- Anthropic
- Cathedral
- DOGE
- Gizmodo
- IPO
- Pentagon
- Ridge Security
- Salem Partners
- Secure AI Solutions & Cybersecurity
- SpaceX
- Suzu Labs
- TechRadar Pro
- Technical Marketing Engineering
- The Washington Post
- Trump
- US Department of Government Efficiency
- Washington Post
---

![Claude by Anthropic](https://cdn.mos.cms.futurecdn.net/scxFkyfYSQbrtGvqrmFqgU-1920-80.jpg)

* **AI startup Cathedral used autonomous agents to breach Anthropic systems through weaknesses in third-party software**
* **Agents accessed HR, sales, and IT data, exposing limited customer and partner information**
* **Incident highlights how AI-powered attackers can rapidly exploit vendor weaknesses despite strong internal defenses**

An AI startup seemingly gave Anthropic a taste of its own medicine when it used AI agents to break into the company and expose sensitive data.

The company in question is called Cathedral, which was founded by former members of the defunct US Department of Government Efficiency (DOGE), a US government initiative established to reduce federal spending and bureaucracy, while modernizing government technology and operations.

Anthropic is running a two-fold bug bounty program through HackerOne. One part is focused on finding technical flaws in Anthropic’s systems, while the other is an invite-only program that rewards researchers for finding universal jailbreaks that bypass Claude’s safety protections.

Cathedral apparently shared its results with Anthropic through the bug bounty program. After its human researchers unsuccessfully tried breaking in for a few days, they deployed AI agents which took less than 12 hours to find a way in, by exploiting flaws in third-party business software.

## Violating the rules

After accessing the company’s network, the agents accessed meeting transcripts, information on salaries and job offers, as well as Slack messages. Employee conversations with Claude were not exposed, it seems.

Anthropic confirmed the news, saying Cathedral accessed a “limited set” of sales, human resources, and IT systems, and compromised contact information and basic user account records belonging to certain customers and partners. Source code and AI model weights were not accessed.

“Our monitoring flagged some of Cathedral’s activity before they reported it to us,” Anthropic said in a statement shared with *The Washington Post*. “We shut off their access the same day.”

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

According to *Gizmodo*, Anthropic accused Cathedral of violating the program’s rules by failing to disclose the full extent of its activity. We don’t know if that means Anthropic won’t release the payment for the bounty, but it sure sounds like it.

Paying the bounty could be the least of Anthropic’s concerns, though. The company is currently gearing up for its Initial Public Offering (IPO), with a valuation of $1.4 billion. Leaking sensitive data to anyone, including white hat hackers, is definitely not a good signal.

## A 'bunch of kids' wreaking havoc

“The fact that weaknesses in ordinary enterprise software can compromise the infrastructure of even the most advanced organizations should be a wake-up call for every company in America,” the *Washington Post* cited Cathedral’s report as saying.

At the same time, a senior Trump administration official allegedly told *Via* * The Independent*that “if a bunch of kids who have just started a company can do this, then potentially the Chinese aren’t far behind.”

Cathedral can hardly be described as “a bunch of kids” - it is an AI startup focused on offensive and defensive cyber operations for the US military and government. Its founders include Gavin Kliger (former Pentagon chief data officer), Luke Farritor (best known for helping decipher ancient Roman scrolls using machine learning), Marko Elez (former SpaceX staffer), and Jack Stein (apparently worked as an investment banking associate at Salem Partners before joining DOGE).

The cybersecurity community had something to say about it. Jacob Krell, Senior Director for Secure AI Solutions & Cybersecurity at Suzu Labs, wasn’t particularly phased, saying if third-party vendors are a risk everywhere, then they’re a risk at Anthropic.

"Cathedral's agents got into Anthropic the same way attackers get into everyone else, through the vendors,” Krell said. “Security maturity is capped by the weakest vendor you integrate with, and no amount of in-house engineering changes that."

Darin Fredde, Senior Director of Technical Marketing Engineering at Ridge Security, praised Anthropic’s response: "Anthropic deserves credit for reporting that its monitoring detected some of the activity and for taking containment measures. But the real measure of remediation is independent verification that those attack paths are closed. We need to stop confusing a successful patch with a verified security outcome. Otherwise, we're just closing the front door and hoping nobody discovered the spare key."

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
