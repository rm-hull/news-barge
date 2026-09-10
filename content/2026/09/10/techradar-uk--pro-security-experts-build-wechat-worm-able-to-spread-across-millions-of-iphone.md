---
title: Experts build WeChat worm able to spread across millions of iPhone and Android
  devices via phone calls
source_url: https://www.techradar.com/pro/security/experts-build-wechat-worm-able-to-spread-across-millions-of-iphone-and-android-devices-via-phone-calls
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-10T04:30:10Z'
published: '2026-09-10T00:00:00Z'
description: Your phone rings, and you're infected
image: https://cdn.mos.cms.futurecdn.net/2yHEj7RR9QpUSvzcPym7Vf-2121-80.jpg
---

![Angry man shouting at mobile phone while sitting at a desk](https://cdn.mos.cms.futurecdn.net/2yHEj7RR9QpUSvzcPym7Vf.jpg) 

- **Calif researchers found a zero‑click WeChat VoIP flaw enabling account takeover via calls**
- **“WeWorm” spreads through ringing calls; victims need not answer to be compromised**
- **Tencent patched in Android 8.0.77 and iOS 8.0.76; no exploitation seen in the wild**

Security researchers have found a flaw in WeChat which allows malicious actors to take over people’s accounts on both Android and iOS devices - but what makes this flaw stand out is the fact that it’s a zero-click bug - victims need not do a thing to be compromised.

WeChat is a “super-app”, allegedly used by roughly 1.4 billion people, and is especially popular in China. It started as a communications app, letting users send messages, and make voice and video calls, and has evolved to function as a social network, allowing users to share photos and videos, as well as a payment app through which users can transfer money, pay for things, order food, book taxis, and even access government and business services.

Security researchers from Calif have now disclosed finding a ‘memory corruption’ issue in WeChat's VoIP stack. For now, they decided not to share the technical details, and to instead demonstrate the flaw “at an upcoming conference.” To that end, they built a worm called WeWorm, capable of taking over target WeChat accounts and spread through phone calls made via the app.

## A phone call would suffice

In practice, it works remarkably simple: an attacker uses WeChat to call a person they have in their contacts list (this is a prerequisite). They can use both an Android and an iOS device, and can call anyone, regardless of the model or the OS they’re using. As soon as the phone starts ringing, WeWorm gets to work, “worming” its way into the victim’s device.

The victim does not even need to answer the phone - having it ring is enough. If they answer, they’ll hear nothing but silence, yet the worm will continue operating. If they decline the call, the attack stops, but this is hardly a mitigation - the attacker can simply call again while the victim is asleep (or otherwise away from their device).

Within a few seconds, the attacker will have access to the victim’s WeChat account, including their messages, contacts list, and virtually anything else found in the app. What makes this bug particularly worrisome on the surface is the fact that WeChat can be used to transfer money and pay for things, but WeChat Pay has additional authentication and risk controls designed to prevent that from happening.

The good news is that there is no evidence of this flaw being exploited in the wild. The bad news is that this is not the first zero-click flaw found in modern-day smartphones, and most likely will not be the last one.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## Tencent's response

Calif said it responsibly disclosed its findings to WeChat’s parent company Tencent, who came back with a patch. Versions 8.0.77 for Android and 8.0.76 for iOS have apparently solved the problem, although

Tencent did not list any details in its patch notes, simply saying the version brought “bug fixes”, but in a statement shared with *The Hacker News*, it said the exploit has been “mitigated for all users”, and that it was applied server-side - users need not install anything, aside from the patch.

It’s also worth mentioning that WeChat has apps for HarmonyOS, Windows, Mac, and Linux. However, it would appear that Calif did not test those, and Tencent did not include them in its patch. The researchers did say that they would be looking into this same flaw in other products, too:

“This specific WeChat bug is one instance of the many unconventional attack surfaces that are present across many messaging apps,” they said. “We're conducting more of this research across other apps and attack surfaces, while working with app developers on attack surface reduction. This may take an industry-wide effort, since some of it depends on the platform owners. Once that work is further along, we'll share our progress, including the technical details of this WeChat bug.”

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
