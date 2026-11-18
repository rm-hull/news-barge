---
title: Massive Kik data breach exposes more than 150 million images — experts say
  popular messaging app may have leaked incredibly sensitive material
source_url: https://www.techradar.com/pro/security/massive-kik-data-breach-exposes-more-than-150-million-images-experts-say-popular-messaging-app-may-have-leaked-incredibly-sensitive-material
source_site: TechRadar UK
source_slug: techradar-uk
description: Some of the images could be described as containing child sexual abuse
  material
image: https://cdn.mos.cms.futurecdn.net/DyF5dEL5UeH88zBmpwo3EU-1400-80.jpg
published: '2026-11-17T00:00:00Z'
scraped_at: '2026-11-18T00:57:51Z'
categories:
- Technology & Software
people:
- Jeremiah Fowler
- Kik
locations:
- Connecticut
- Kik
organisations:
- American Enterprise Institute
- Google Play
- Kik
- MediaLab
- NCMEC
- National Center for Missing & Exploited Children
- TechRadar Pro
- URL
- US National Center for Missing & Exploited Children
- Whisper
---

![Kik](https://cdn.mos.cms.futurecdn.net/DyF5dEL5UeH88zBmpwo3EU-1400-80.jpg)

* **Researchers found an exposed database containing more than 150 million Kik profile images, including around 75 million original photos**
* **Exposed images were publicly accessible online and included content involving minors, prompting reports to child-safety authorities**
* **Database was secured after disclosure, but questions remain about exposure duration and potential prior access**

Kik, a popular American instant messaging app, was leaking profile pictures on the clearweb, putting even children and young adults in harm's way. To make matters worse, some of the images that were leaking were disturbing enough for the researcher who found them to report them to the US National Center for Missing & Exploited Children.

Security researcher Jeremiah Fowler disclosed discovering an unencrypted, non-password-protected database available to anyone with a browser and an internet connection - as long as they knew where to look.

This time around, he found a database containing just over 150 million images uploaded between 2021 and 2026. They were marked as thumbnails and originals, meaning that at least half - some 75 million - were unique, large-format images and photos. Fowler later determined they were marked as “profiles” and associated with Kik.

## Kik locks it down

Launched in 2010, Kik has historically reported more than 300 million registered accounts, although its current active-user figures have not been publicly disclosed. Google Play lists more than 100 million downloads, and Fowler claims it has more than 120 million registered users and around 15 million active users.

Kik is owned by MediaLab, a US-based company that also owns social networking platform Whisper and other digital media properties.

“The files were hosted in a cloud storage database and could also be viewed in any web browser through the direct hosting URL and a subfolder on the primary Kik domain,” Fowler said.

“The name of the database and the fact that the image resources were also hosted on a Kik-associated subdomain provided strong evidence that the exposed records were associated with the platform.”

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The researcher notified Kik of his findings, and the database was quickly locked down. However, the company did not reply to a request for comment, so we don’t know how many people were exposed (75 million original pictures does not necessarily mean 75 million people - there are likely duplicates and fake accounts), for how long the database remained open, who managed it (Kik, MediaLab, or a third party), and if any malicious actors found it before Fowler did (which is always a possibility).

## A dark turn

This is all relatively standard news in the world of unintentionally misconfigured databases. The findings took a dark turn when Fowler discovered that in a sample of some 2,000 images, there were 66 profile images appearing to contain child sexual abuse material (CSAM).

Fowler suggests Kik is primarily a platform for teens and young adults: “In 2016, the messaging platform was used by approximately 40% of American teenagers and a recent article published by the American Enterprise Institute stated that 70% of Kik users are in the 13 to 24 age bracket.

“In 2025, Kik's terms of service were updated to state that the app is only for individuals aged 18 and older. In my limited review of the publicly exposed images, I saw numerous images of individuals who appeared to be under the age of 18," the report notes.

While the report does plenty of hedging, saying that a single image is not enough to determine someone’s age, it does state that Fowler reported some of the images to the National Center for Missing & Exploited Children (NCMEC) and the Connecticut Attorney General’s office.

“In a random selection from the limited sample of files, I saw a large number of profile images containing nudity or adult-themed content,” the researcher stressed.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
