---
title: Open Microsoft database with 17 trillion total rows and 25,000 user accounts
  hacked by a bored teenager — but he's been well-paid for his actions
source_url: https://www.techradar.com/pro/security/open-microsoft-database-with-17-trillion-total-rows-and-25-000-user-accounts-hacked-by-a-bored-teenager-but-hes-been-well-paid-for-his-actions
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-05T22:02:08Z'
published: '2026-10-05T00:00:00Z'
description: An estimated 17.3 trillion Microsoft rows became accessible
image: https://cdn.mos.cms.futurecdn.net/5041fbe73089e0689408c540ac34ef05-900-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
- Personal Finance & Investing
people:
- Claude
- Faav
locations: []
organisations:
- API
- Admin
- Adobe
- Amazon
- Anthropic
- Azure Cloud Services
- Faav
- Google
- Microsoft
- OpenAI
- Swagger
- TechRadar Pro
- Titan
- UPN
- Wayback Machine
---

![Microsoft](https://cdn.mos.cms.futurecdn.net/5041fbe73089e0689408c540ac34ef05-900-80.jpg)

* **16-year-old bug hunter gained admin access to Microsoft's internal Titan analytics service through an unsigned login token that the service never checked**
* **From there, an estimated 17.3 trillion stored rows and a metadata table of about 25,000 accounts were reachable, though Faav says he only sampled data, avoiding dumping records or touching customer data**
* **Microsoft has hardened the service's security since and paid a $5,000 bounty, downplaying the trillion-row figure as a theoretical storage estimate rather than actual exposed customer information**

A 16-year-old bug hunter who goes by 'Faav' logged into Microsoft's internal Titan analytics platform using a token that no real credentials should have produced, and from an administrator's seat, he could see an estimated 17.3 trillion stored rows and a metadata table listing roughly 25,000 accounts.

Microsoft paid him $5,000 and has since closed the hole, prompting him to detail his findings online even as he describes the impact as hypothetical rather than a consequential breach.

He said the way in was a single missed check, which let him access a system that should otherwise have been locked to Microsoft staff behind a VPN.

## A simple mistake that could have catastrophic in the wrong hands

Microsoft's Titan sits behind a "VPN required" page meant to keep its web interface to Microsoft staff, but its API was still reachable through an Azure Cloud Services host, and the Swagger file describing that API listed four access routes.

Three demanded Azure AD authentication. One, "/v2/Query", did not, and it accepted raw SQL, giving Faav a way in. He wasn't moving blind either; to learn what tables to ask for, Faav pulled 2023 snapshots of Titan's pages from the Wayback Machine and recovered an archived Apache Superset configuration listing 56 table definitions.

The deeper flaw was in how the service read login tokens. As Faav explained, Titan validated the contents of a JSON Web Token- the tenant, audience, application ID, and user- but never verified the cryptographic signature that is supposed to prove the token is genuine, offering the analogy of a hotel where every door has a working keycard reader but any keycard opens any room, making it essentially an ineffective check at best.

He submitted an unsigned token, and then, after ten days of failed logins, stopped treating the "upn" field as a real email identity and set it to the plain string admin. Titan resolved that to local user ID 1, which carried the admin role, and ran his query.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The saga has an interesting AI subplot: Faav hunts with an orchestration bot he built called Antares, which he says was running OpenAI's Codex and Anthropic's Claude. Antares did the grunt work, enumerating subdomains, mapping the attack surface, and pushing the forged token through four layers of validation, one error message at a time.

It did get stumped, however, when it tried to find a UPN; it got stuck attempting only email addresses. That is not a problem per se for what was essentially a brute-force-style approach using the most probable email addresses, but it took manual intervention from the hacker to try 'admin' instead as an alternative to finally get access.

Admin access opened Titan's platform metadata database, which, according to his tally, held about 25,000 account and email records, roughly 18,000 employee email records, 15,000 organization records, and tens of thousands of dashboards, charts, and dataset definitions.

The disclosure moved quickly once he reported it on September 5 2026 as case 144051. Microsoft asked him to stop testing and hand over his IP address between September 6 and 8, locked the endpoint on September 9, and paid out on September 17.

There is an interesting caveat, however: Faav discloses that Microsoft had editorial control over his write-up, cutting sections and figures and reshaping how it described the impact before he published, so the most authoritative account of this bug has already been shaped by the company it embarrasses. None of this makes the bug small, however: one unverified signature that made every other access control in Titan pointless is a potential security nightmare, nipped in the bud by a teenager who has had success with similar bugs at Amazon, Google, and Adobe, in addition to a prior disclosure at Microsoft.
