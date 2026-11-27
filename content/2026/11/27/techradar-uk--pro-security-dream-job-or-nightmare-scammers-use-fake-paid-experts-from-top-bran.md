---
title: Dream job or nightmare? Scammers use fake paid experts from top brands to steal
  Google logins
source_url: https://www.techradar.com/pro/security/dream-job-or-nightmare-scammers-use-fake-paid-experts-from-top-brands-to-steal-google-logins
source_site: TechRadar UK
source_slug: techradar-uk
description: If you get an email to share your expert opinion with Google for a fee,
  turn it down
image: https://cdn.mos.cms.futurecdn.net/wBA63zhGK4GEWGaAEY7UHd-2560-80.jpg
published: '2026-11-27T00:00:00Z'
scraped_at: '2026-11-27T21:10:13Z'
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Push
locations: []
organisations:
- AI
- Accenture
- American Express
- Coca-Cola
- Culver's
- Google Ads
- Google Cloud
- HireVue
- Nvidia
- Okta
- Push Security
- SpaceX
- Spotify
- TechRadar Pro
- Yahoo
---

![Close up of a person touching an email icon.](https://cdn.mos.cms.futurecdn.net/wBA63zhGK4GEWGaAEY7UHd-1920-80.jpg)

* **Attackers are impersonating major brands such as Google, Nvidia, SpaceX, and Coca‑Cola to lure victims into fake paid webinars and expert interviews**
* **The campaign uses spoofed sign-in pages to steal corporate email credentials and potentially target enterprise authentication systems**
* **Researchers believe AI-assisted tooling may have helped build the phishing infrastructure, highlighting the growing role of AI in social-engineering attacks**

If you get invited to a webinar to share your “expert opinion” with Google or SpaceX for a $600 compensation, take a rain check - it could well be a scam that tries to steal your work email credentials.

Security professionals Push Security recently discovered the campaign, which sees the victim receive an email spoofing one of eight major brands: Accenture, American Express, Coca-Cola, Culver's, Google Cloud, Nvidia, SpaceX, or Spotify. The email itself may come through legitimate email services (such as HireVue, SendGrid, Mandrill, and Cvent), or compromised accounts, and invites you to a paid expert interview, feedback study, or private webinar.

In one case, a victim was invited via HireVue to attend a Google Cloud webinar about deploying AI applications into production. Some of these webinars promise a $500 payout, others even $600.

## Okta in the works, too

As is usual with phishing emails, it includes a link such as “View webinar details”, or “View your invitation”, which redirects you to a spoofed website, but not before you pass a fake reCAPTCHA test. After solving the CAPTCHA, you’ll get redirected to a page that matches the brand in the original invitation and where you’ll be asked to provide personal information such as name, phone number and - most importantly - work email address.

The page will prompt you to continue with Google via a counterfeit login page which rejects personal emails (those from Google, Yahoo, or Outlook) and accepts work emails only. If you take the bait and enter the information there, it immediately gets sent to a server under the attackers’ control. This includes the CAPTCHA completion status and information submitted through the landing page and fake sign-in

Push also said it saw a fake Okta sign-in in the attackers’ code, concluding that the threat actors could be preparing to target firms using Okta authentication, too. However, the report does not say if the feature is currently in active use or not.

The researchers are calling the phishing kit GoodGuys, after a hidden "GoodGuys sign-in simulation" label they found in every build. They believe it was developed with the help of an AI coding assistant, since it had hidden accessibility labels. Who calls a login page a “simulation”?

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## Tricking an AI assistant

"The sign-in card in every build carries two hidden labels: "Sign-in simulation" and "GoodGuys sign-in simulation." They sit in accessibility text that only screen readers announce, so a visitor never sees them. We think the label is a leftover from how the kit was first built," Push Security said in its report.

"Calling the page a sign-in "simulation" for a made-up company is the kind of framing someone would use to get an AI coding assistant past its guardrails when asking it to build a phishing page. The label then stayed in every build we've collected." In other words, the threat actors had to trick the AI agent to build the page, under the pretense of a “simulation”, rather than a live attack.

Push also found a separate phishing campaign inviting victims to a fake Coca-Cola interview and using the Evilginx phishing kit to try and steal Google Ads accounts. It’s a separate campaign, but possibly operated by the same threat actor, since both campaigns use the same SendGrid click tracked and identical branding assets.

“Both also pitch a paid interview to work accounts, with Google first and Okta as an option,” Push said, but added that the code and hosting are different, suggesting that the hijacked sending account could have been resold to a different actor.

*Via* * BleepingComputer*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
