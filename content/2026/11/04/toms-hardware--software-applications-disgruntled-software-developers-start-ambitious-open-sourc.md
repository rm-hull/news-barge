---
title: Disgruntled software developers start ambitious open-source revolt, using AI
  to clone common services — OccupySaaS AI-powered project wants to kick Auth0, Salesforce,
  and other pricy service-as-software to the curb
source_url: https://www.tomshardware.com/software/applications/disgruntled-software-developers-start-ambitious-open-source-revolt-using-ai-to-clone-common-services-occupysaas-ai-powered-project-wants-to-kick-auth0-salesforce-and-other-pricy-service-as-software-to-the-curb
source_site: Tom's Hardware
source_slug: toms-hardware
description: Subscription exhaustion is a real thing.
image: https://cdn.mos.cms.futurecdn.net/H8EavN2zCtyGHnFmtFWGxg-1687-80.png
published: '2026-11-04T00:00:00Z'
scraped_at: '2026-11-04T14:24:02Z'
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
people:
- Bruno Ferreira
- Thomas Meadows
- Tom
locations:
- Jira
organisations:
- AI
- Adobe-replacement ArtCraft
- Confluence
- Get Tom's Hardware
- GitLab
- Google News
- OccupySaaS
- PC
- Red Hat Enterprise Linux
- Salesforce
- Tom's Hardware
- Wordpress
- ZeroAuthy
---

![OccupySaas logo](https://cdn.mos.cms.futurecdn.net/H8EavN2zCtyGHnFmtFWGxg-1687-80.png)

AI-powered software cloning is quite the hot topic. Software companies are likely unhappy with the notion of vibe coders ganging up to try and copy their software. Simultaneously, users tired of subscription models, price hikes, and drops in software quality are more than happy to rebel, as proven by the buzz around the Adobe-replacement ArtCraft. Now, OccupySaaS is the latest user-led revolt against the software system, aiming to create clean-room, open-source reimplementations of common services using AI tools.

The initiatives already underway in the project look to replace Auth0 and Salesforce with minty fresh alternatives called ZeroAuthy and SalesCompel, respectively. Given that these services all run on their companies' servers, there are no binaries to examine and decompile — the reimplementations are done referencing available documentation, APIs, development kit behaviors, and any applicable open standards. Judging from the project website, it seemingly wants new software to acts as a API-compatible drop-in replacement where applicable.

The project puts a sharp pin on its development ethics and requirements: all work must be a fully clean-room reimplementation, with no decompiled code, no confidential information (including source code) taken from any previous employers, and no copying of UI assets or any other trademarks.

Creating software in this manner is both easier and harder than usual. On the one hand, the only thing that matters is that whichever user inputs are processed and produce the same outputs as the original software, and those behaviors are largely defined by the aforementioned specifications.

At the same time, hosted software is effectively a black box with internal behaviors and "gotchas" that aren't immediately obvious. Just as with console emulators, any drop-in replacement needs to reproduce extant API bugs to be fully compatible — looking at you, Jira.

Besides the aforementioned services, OccupySaaS intends to find replacements for services offering document-and-wiki management, issue tracking, software feature flagging, software/server observability, and customer support. Our guesses for the targeted replacements in each of those categories are Confluence, Jira, LaunchDarkly, Datadog, and Zendesk.

The language of choice is Go, picked over Rust simply because it allows for easily compiling and linking all its dependencies into the one binary that doesn't need an installer and can just be copied to a target system and executed. According to OccupySaaS, that characteristic makes it ideal for packaging into a Docker container or other forms of self-hosting.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Some people may quickly point out that the entire point of renting a SaaS to begin with is that any snafu with the code or the infrastructure is always Someone Else's Problem, and that running your own instance is backwards. However, since OccupySaaS's software is Apache 2.0-licensed, there's nothing stopping anyone from providing a service for it. Examples include Red Hat Enterprise Linux, GitLab, and of course, Wordpress.

The project appears to be the brainchild of Thomas Meadows, a software engineer with two decades of experience. In his personal homepage, he claims is strong suit is project management, which is a good skill to have in this day and age of directing AI agents towards a goal. The website reads like a manifesto, pointing out that per-seat licensing taxes growth, and that the same people who created the software are now being fired — "the software built by the 99% belongs to the 99%."



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G-140-80.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.

* I can appreciate this to a certain extent. I fear that the slop coding may create inferior products compared to what they are copying to an open-source framework. Of course, over time it may improve as they work on their project.Reply
