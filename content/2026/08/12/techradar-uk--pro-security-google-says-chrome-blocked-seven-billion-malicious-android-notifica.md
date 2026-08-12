---
title: Google says Chrome blocked seven billion malicious Android notifications every
  day in its bid to cut down on scams
source_url: https://www.techradar.com/pro/security/google-says-chrome-blocked-seven-billion-malicious-android-notifications-every-day-in-its-bid-to-cut-down-on-scams
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-12T17:07:49Z'
published: '2026-08-12T00:00:00Z'
description: '"Swiss cheese" approach to defense seems to be working'
image: https://cdn.mos.cms.futurecdn.net/o9BDDKXmm9T4Lqtm38fsmV-2560-80.jpg
---

![Annoyed man with phone](https://cdn.mos.cms.futurecdn.net/o9BDDKXmm9T4Lqtm38fsmV.jpg) 

- **Google cut seven billion daily Android Chrome notifications using layered defenses**
- **Chrome now limits abusive sites, revokes permissions, and blocks high‑volume spam**
- **Android improvements simplify managing alerts and reduce scam and malware exposure**

Google says it has cut the number of notifications Chrome users get on their Android devices by seven billion a day.

In a new report, the company outlined how it has built a multi-layered defense system to shield its users from unwanted notifications, protecting them from spam and malware, and helping their devices’ battery last longer.

Most importantly, Google says the achievement significantly improved the overall user experience on Android.

## Notification bombardment

For the longest time, individual websites were allowed to send push notifications directly to their users’ phones, even when they were not actively browsing them.

When a user visits a certain website, they get prompted to “show notifications”, and if they tap “allow”, the website starts sending the alerts. Sometimes, users do it without fully realizing what they’re agreeing to.

Once granted, the notifications (sent through Chrome) get shown next to other alerts (such as the ones coming from WhatsApp, Gmail, or other apps).

Unlike other notifications - which usually alert users to unread messages, calendar events, or similar - these mostly promote new content, deals, or other updates. They can also alert users of breaking news, which is arguably the most useful type among the ones mentioned here.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Legitimate websites use the feature responsibly and generally don’t flood their users with unwanted pings. However, some sites abuse the privilege, bombarding users with unwanted advertising, misleading alerts, clickbait articles, and other formats, just to get them to open the page (where they’re often served ads). More worryingly, malicious or compromised websites can use notifications to push scam messages, fake virus warnings, phishing links or other potentially dangerous content.

Because these alerts are served through Chrome and resemble ordinary system notifications, users may not immediately realize the risk.

But because they are served through Chrome, Google can do something about it, and the company has now “pulled back the curtain” on the toolkit that made these improvements possible.

 ![Mobile Security](https://cdn.mos.cms.futurecdn.net/M8dLsateSbGVwYwoPrRba3.jpg) 


## Swiss cheese

Described as a “swiss cheese” model, Google says it created overlapping protections that cover the entire notification lifecycle. Chrome now automatically revokes notification permissions for sites users haven’t engaged with in a little while.

So, if a site keeps flooding the visitor with notifications that they’re not responding to, Chrome will eventually shut them off. Same goes for sites that have “repeatedly received suspicious notification warnings”. Google did not say how many is considered “repeatedly” and in what timeframe.

The second layer is analyzing signals such as service worker activity. By looking for coordinated behaviors, Google claims it can now pinpoint networks that serve malicious content, and block them.

On the Firebase Cloud Messaging (FCM) server side, the company introduced message rate limits that disallow high-volume notification abuse. Google now evaluates sites based on factors such as message volume relative to time spent on site, the frequency of permission prompts, and general engagement levels.

In other words, if a user spends 10 minutes on a website but then receives 50 notifications, it will raise quite a few red flags. Same goes for users that don’t really interact with the website a lot. “Disruptive domains” are now limited to 1,000 messages per minute and will receive HTTP 429 responses if they exceed this threshold, Google explained.

Finally, the company updated how notifications are handled on Android phones. Users can update their preferences directly from the notification bar, simplifying the process for users who can’t be bothered to dig deep into system settings.

“These integrated efforts effectively shield users from sophisticated scams that leverage notifications to distribute malware, harvest personal information, or solicit fraudulent payments,” Google said.

“Beyond security enhancements, this strategy has substantially decreased unnecessary background activity, reduced user device battery consumption, and transformed the notification lifecycle so users receive only the content they find truly valuable.”

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
