---
title: Security flaw in Vatican’s ‘Click to Pray’ app leaves over 700,000 global users
  exposed — app has been leaking user data for over six months and still does
source_url: https://www.tomshardware.com/tech-industry/cyber-security/security-flaw-in-vaticans-click-to-pray-app-leaves-over-700-000-global-users-exposed-app-has-been-leaking-user-data-for-over-six-months-and-still-does
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-25T21:05:54Z'
published: '2026-07-25T00:00:00Z'
description: Were the app's developers relying on divine authentication?
image: https://cdn.mos.cms.futurecdn.net/aNZt4WiohK6CcJ7nANHdh9-2560-80.jpg
---

![Digital rosary app on a smartphone](https://cdn.mos.cms.futurecdn.net/aNZt4WiohK6CcJ7nANHdh9.jpg) 

Click To Pray, the official prayer app of the Pope’s Worldwide Prayer Network, was found to have zero security by a security researcher. According to BobDaHacker, they discovered in January 2026 that the Vatican-linked app had zero security, allowing anyone to access user data through the API endpoint by simply typing in user IDs. They emailed nine individuals about the vulnerabilities as soon as they discovered them but received no responses and saw no changes for six months.

The information that anyone could get from the Click To Pray app’s database included first and last names, email addresses, and birthdates, among other information. You may not think this is much, but getting names and email addresses is more than enough for bad actors to start sending phishing emails to vulnerable users. BobDaHacker also pointed out that most of the app's users are likely older people who aren’t tech-savvy, so any enterprising scammer could tap into the app for a literal treasure trove of email addresses.

It was also easy to get the complete list automatically. The user ID assigned to new accounts is sequential, and since there’s no rate limiting for the API, all it takes is one GET request per user to capture all that information. Aside from this, the validation_hash used to verify the validity of an account signup is also stored in the clear, meaning anyone with access to the API can verify an account by opening their inbox. The email also had security issues that make it look like a phishing email, even if it’s legitimate.

You may think that a prayer app shouldn’t be much of a target for cybercriminals, especially as this has a small install base compared to the 16 billion accounts exposed in one of the largest data breaches in history. But the fact that it had almost 720,000 accounts as of July 2026 meant that there’s a lot of possible targets within that database. Even if just 1% of these users respond to an enterprising cybercriminal who harvested their email addresses from the app, that’s more than 7,000 different individuals who could lose money because of this leak.

BobDaHacker waited for six months for a response, but, unfortunately, no one related to the app responded to their concerns. Because of this, they contacted Nate Neslon, a security journalist for *Dark**Reading* (who similarly received crickets after contacting them), who published a story about it. It was only after the news went live that the app’s security lapses were fixed, even if BobDaHacker wasn’t, at the very least, acknowledged by the makers of the app. Hopefully, no other hackers were aware of the weaknesses of the Click To Pray app.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Jowi Morales](https://cdn.mos.cms.futurecdn.net/gM7E2WSDg2wgCFoaDPz9yK.jpg)

Jowi Morales is a tech enthusiast with years of experience working in the industry. He’s been writing with several tech publications since 2021, where he’s been interested in tech hardware and consumer electronics.
