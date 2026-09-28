---
title: Teenager hacks open Microsoft database with 17 trillion total rows and 25,000
  user accounts — custom AI bot and lack of JWT token validation yields a fruitful
  trove, earns $5,000 bug bounty
source_url: https://www.tomshardware.com/tech-industry/cyber-security/teenager-hacks-open-microsoft-database-with-17-trillion-total-rows-and-25-000-user-accounts-custom-ai-bot-and-lack-of-jwt-token-validation-yields-a-fruitful-trove-earns-usd5-000-bug-bounty
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-28T13:59:22Z'
published: '2026-09-28T00:00:00Z'
description: I guess that purely technically, the JWT token authorization was there.
image: https://cdn.mos.cms.futurecdn.net/Jz3s87CzobimC9szxWZth-2309-80.jpg
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
- Personal Finance & Investing
people:
- Bruno Ferreira
- Faav
- Tom
locations:
- AI
- Swagger
- Titan
organisations:
- Adobe
- Amazon
- Antares
- Bing
- Get Tom's Hardware
- Google News
- JWT
- Microsoft
- OpenAPI
- PC
- Redmond
- Titan
- Tom's Hardware
---

![asdf](https://cdn.mos.cms.futurecdn.net/Jz3s87CzobimC9szxWZth.jpg)

What do you get when you cross a bored teenager with free time and excellent computer skills? A hack of a Microsoft database with trillions of records on hand and 25,000 records of employee data, of course. Future legend hacker Faav poked around Microsoft's supposedly internal Titan analytics platform, eventually finding that its user validation was... sub-optimal.

According to Faav, he's "spent the year hacking Microsoft off and on around school," digging up bugs on the Redmond firm's wares as well as Amazon, Google, Adobe, and others. Much like other hackers, he has his own set of tools, and predictably in this day and age, his sonic screwdriver is Antares, an AI orchestrator bot he concocted for the purpose of scanning and automating boring security legwork.

Antares found an endpoint URL in Titan that brought up an error message saying that a VPN was required. Just like a virtual *pspspsps*, this was enough to get Faav's attention. He got Antares to look for subdomains around this endpoint, coming up with one belonging to an Azure Cloud host, along with a corresponding Swagger/OpenAPI file listing four routes (Swagger is an industry-standard machine-readable instruction on how an API works, for easier third-party integration).

While three of those routes needed Azure Active Directory authentication, one did not, and its name was inspiring: /v2/Query. It also accepted raw SQL queries, prompting a collective facepalm from the audience. Faav still needed to know what to query for, and after clever usage of the Wayback Machine, he found a 2023 version of this login page, complete with a helpful Apache Superset configuration file describing the database schema, showing 56 table definitions.

He also found that this endpoint refused his queries due to the lack of a JWT (JSON Web Token) authentication, so he sicced Antares on it again for 10 days, with no success. Eventually, Faav had a flash of inspiration and realized that the way the server was responding implied that the token's digital signature wasn't being checked. So he just pretended his access token was for an administrator and was promptly let in. One handy "SHOW DATABASES" later, he was staring at 25,000 records of employee data, along with organization records, dashboards, and charts.

After exploring the database a little more, he found a particular data source for Bing analytics. Digging there and tallying up rows across tables, Faav saw he had access to a total of 17 *trillion* records total, and had to double-check this number and stop himself from yelling out and waking his parents at 2 am.

After reporting the problem to Microsoft's bug bounty program, he was awarded with $5,000 for his findings. In his blog post, he also points out that "AI and human intuition compounded here. Antares did ten days of work I didn’t have to [...] Its persistence, plus one human hunch, is what made this find possible."

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*



![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.

* The companies need bots to crawl their infrastructure, find such weaknesses, and some day in the future - self-fix or at least provide a suggested fix for a human to accept. But if they get that far, and sell it everywhere, but bounty hunters may be out of a job.Reply
* This is the problem with code written by committee. No one person or even a small group is responsible for a lot of code. All kinds of people writing little parts and the people responsible for combining it tend to be project manager types with little technical skills. In some cases this coding has been outsource to other companies so it become even harder to ensure quality. These hive mind software projects have all the same issue as people are now seeing in AI developed code.Reply
