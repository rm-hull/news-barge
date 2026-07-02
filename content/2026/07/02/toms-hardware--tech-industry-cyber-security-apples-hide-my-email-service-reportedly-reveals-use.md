---
title: Apple's Hide My Email service reportedly reveals users' actual email addresses
  with little effort — Cupertino has seemingly known about the problem for a year
  but has yet to fix it
source_url: https://www.tomshardware.com/tech-industry/cyber-security/apples-hide-my-email-service-reportedly-reveals-users-actual-email-addresses-with-little-effort-cupertino-has-seemingly-known-about-the-problem-for-a-year-but-has-yet-to-fix-it
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-02T10:51:31Z'
published: '2026-07-02T00:00:00Z'
description: Millions of users risk having their real email addresses exposed
image: https://cdn.mos.cms.futurecdn.net/LHZ4Rgs8Ttj8heEhX9c7K7-2048-80.jpg
---

![Tim Cook looking happy](https://cdn.mos.cms.futurecdn.net/LHZ4Rgs8Ttj8heEhX9c7K7.jpg) 

If you read or watch any privacy tutorial on the internet, one of the first tips will be to start using anonymized email addresses in some form — providing a fake email that redirects to your real one. Many email providers offer this functionality, and so does Apple's basic paid iCloud plan with the Hide My Email feature. But apparently Apple's implementation of the feature is trivial to crack — which means anyone can find your real email address with little effort, according to 404 Media.

 ![A hand holding the Ryzen 7 9850X3D.](https://cdn.mos.cms.futurecdn.net/Xh2MupWrRjJPiLLuopmKRB.jpg) 


The privacy vulnerability has been known to Apple for just over a year, and was first reported by Tyler Murphy, co-founder of data removal company EasyOptOuts. The folks at 404 Media claim they tested the vulnerability themselves and that, sure enough, it takes minimal effort to figure out the real address behind the fake alias — with a 100% success rate.

Apple doesn't seem to be bothered by the issue, given that Murphy revealed the problem in June 2025, and the company only executed a fix in March 2026. Post-fix, however, Murphy verified the issue remained (and apparently the last time he heard back from Apple back was in May, when the company said said it was still investigating). There are no further updates, it seems, and this is poor optics for a company that talks a big game about user data privacy.

Neither the researcher nor 404 media divulged the exact mechanism, despite the one-year timeframe being well past the common 90-day security vulnerability disclosure window. This is likely to avoid putting a lot of users at risk of exposure, considering that Apple has passed one billion paid subscribers. Even if only 1% of users use Hide My Email, that still accounts for 10 million people. 

Given the lack of technical details, it's hard to pin down where the problem could lie. Accidental revelations of aliased emails have happened several times, by the hand of client software trying to be helpful and "fixing" the reply path, and by servers mismanaging email headers.

Perhaps adding insult to injury, Apple recently stated that it's going to move Hide My Email addresses to their own domain, "private.icloud.com", making it easy for websites to reject such addresses in a bid to always have users' real contact info. Murphy suggested that the company stop sales of the Hide My Email feature until the data leak matter is resolved, but, again, there's been no response.

  


*Follow**Tom's Hardware on Google News**, or**add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.
