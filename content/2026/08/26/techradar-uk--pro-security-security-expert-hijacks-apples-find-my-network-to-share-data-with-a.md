---
title: Security expert hijacks Apple's Find My network to share data with a Linux
  device
source_url: https://www.techradar.com/pro/security/security-expert-hijacks-apples-find-my-network-to-share-data-with-a-linux-device
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-26T23:23:54Z'
published: '2026-08-26T00:00:00Z'
description: A 'trusted' Linux device can impersonate an Apple device and access already-shared
  Find My locations
image: https://cdn.mos.cms.futurecdn.net/AkzcwhimnzzysrwQDQfyAe-2000-80.jpg
---

![Find My iPhone displayed in settings](https://cdn.mos.cms.futurecdn.net/AkzcwhimnzzysrwQDQfyAe.jpg) 

- **Researcher registers Linux machine as a trusted device on Apple's Find My network and pulled live people-tracking data that Apple normally reserves for its own hardware**
- **The work is not a mass-surveillance exploit: it is limited in scope and only reads a location share that a friend had already agreed to, and it cannot silently locate arbitrary Apple users**
- **The approach took less than a week of protocol reverse engineering, and Apple has maintained silence on queries about the technique employed**

Apple keeps the full Find My experience locked to its own devices, but a recent attempt by security researchers suggests that wall may be a relatively weak barrier to entry.

A 22-year-old security researcher who goes by "Zerotistic" documented how they registered an ordinary Linux machine as a trusted node on Apple's network and used its new status to receive live people-location data that Apple otherwise shares only with its own devices, such as iPhones and iPads.

Find My, Apple's catch-all tool for locating hardware such as AirTags, iPhones, and iPads, also lets people share their whereabouts with family and friends, and while Apple has historically guarded this particular feature very closely, it is also the same one the security researcher targeted to introduce a device that Apple does not otherwise have complete control over as part of its ecosystem.

## An interesting trick that still requires consent to get the job done

The task is not an easy one to begin with: convincing Apple's back end that a Linux process was a legitimate Apple device that was part of its ecosystem and therefore could be trusted with information shared via the Find My platform required a lot of trial and error to get going.

It is important to clarify here that Apple's system is not exactly compromised here; the approach still requires a friend to share data that the Linux client that the security researcher built can then read.

Apple currently sends people-location data over its private Push Notification service only after it trusts that the receiving machine belongs to the account and can handle the data. This means the Linux machine would have to speak Apple's private language to query its servers and process the information it received.

It involved obtaining an Apple Identity Services (IDS) certificate, a specialized device and messaging credential Apple's internal framework uses to link an Apple Account to specific hardware, end-to-end encryption keys, and push notification tokens. This meant crafting a certificate signing request and sending it to a legacy Apple enrollment endpoint.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Once done, a Linux box with a signed certificate could sign its own requests and register as a Find My device, but it still had to subscribe to six different subservices to function. The registration request also had to be signed using an IDS certificate and an APNs certificate obtained during initial network setup.

The researcher then issued a SubscribeAndFetch request that provided an encrypted location key from his friend's Apple device to the Linux box, masquerading as one.

What might concern Apple is how fast things moved: the whole pipeline came together in a week. It also didn't require a jailbreak, a leaked key, or even a Mac to do the job. Instead, open-source clients and decompiled daemons were the norm, with a trial-and-error approach that eventually paid off.

The technique has its limitations: attacks can not target a stranger, and consent is required to track even one's friends. It shows that Apple's boundary around Find My stems from an obscure protocol it enforces rather than a cryptographic lock; once a device acts like it is from Apple, the ecosystem treats it as a family member rather than an untrusted node.

Apple has yet to respond to media queries about whether it plans to address the demonstrated trick or patch the loop in the near future.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Rahim Amir](https://cdn.mos.cms.futurecdn.net/9xKZFBamtEZKSChRvywbPB.png)

Rahim Amir is a UAE-based tech writer who enjoys building PCs as much as he enjoys writing about them. He has been professionally writing about PC hardware since 2023, focusing on buyer’s guides, hardware reviews, and sponsored content and features related to tech.

Having built hundreds of gaming PCs and being an avid gamer in his spare time, Rahim tends to have stronger opinions about hardware than most. This is particularly on display when he gets his way with powerful, but minimalistic RGB builds even as Small Form Factor (SFF) PCs come a close second.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
