---
title: 'First your age, next your identity: Inside the ''hack'' that broke the EU
  age verification app''s privacy promises'
source_url: https://www.techradar.com/vpn/vpn-privacy-security/first-your-age-next-your-identity-inside-the-hack-that-broke-the-eu-age-verification-apps-privacy-promises
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-31T17:49:20Z'
published: '2026-07-31T00:00:00Z'
description: The security expert who 'hacked' the app three times since April warns
  that “the next step will be proving who you are”
image: https://cdn.mos.cms.futurecdn.net/WSCXYRKEQTYxJyzZRF6ULb-1920-80.png
---

![European Commission President Ursula von der Leyen during a press conference on child safety online in Brussels on July 13, 2026, with the Leave No Trace logo on the top left.](https://cdn.mos.cms.futurecdn.net/WSCXYRKEQTYxJyzZRF6ULb.png) 

When Paul Moore heard the European Commission President saying that the EU age verification app will “give children a safer start online,” he was unconvinced.

"Bypassing the latest EU age verification app (2026.07-1) with a Chrome extension," he later posted on X. And it wasn’t the first time.

With over 20 years of experience under his belt, Moore managed to bypass the app back in April, right after the Commission first launched it. Combined, his experiences have led him to a straightforward conclusion: "anonymous age verification doesn't work."

While the process he used to bypass the verification system doesn’t undermine people’s privacy, Moore believes the long-term impact of its ineffectiveness will.

"All it is an escalation path being drip-fed, bit by bit under the guise of child safety," Moore told TechRadar. It won’t just be about proving your age. "The next step will be proving who you are," he said.

## The EU’s 'privacy-preserving' approach

 ![EU](https://cdn.mos.cms.futurecdn.net/5NsvMB6arEjzGkWxkstoDj.jpg) 


Most of the current age verification methods, which require scanning national ID documents or biometrics, put people's sensitive data at risk. (Think, for example, of the data breach that affected Discord’s age verification provider and exposed 70,000 people's government IDs and personal data last year.)

For that reason, there's a growing sense of urgency to find a solution that helps people prove their age without collecting sensitive information. And the European Commission argues that it has found it.

Drawing on the framework of the COVID-19 certificate app, the Commission came up with a template for a privacy-first, open-source tool that EU member states can use to build their own national apps.

The process — which is part of the bigger European Digital Identity Wallet (EUDI) project — leverages zero-knowledge proofs (ZKPs) and verifiable credentials (VCs) to verify someone's age without sharing sensitive information.

In other words, your phone scans your ID and stores that data locally. Websites will then ask users to scan a QR code via the app to prove they are old enough to access certain content.

A European Commission spokesperson told TechRadar that online services won't receive any personal information about the users, saying: "The age proof simply confirms whether the user meets the age requirement."

Moore doesn’t dispute the privacy credentials of the process. Perhaps worse, he just doesn’t think it will work.

## Why the EU age verification doesn't work

While the EU age verification blueprint sounds like a welcome improvement compared to the current approach, the advantages don't hold up.

That's because Moore says age checks have to be tied to a person’s identity to be trustworthy. "The second you strip the identity away from how old somebody is, a person can't answer that question," he said.

Since the April launch, the tool's security credentials have even been improved, but Moore says the issue isn’t a bug but the entire process, criticising the latest efforts as mere "security theater."

## How Moore bypassed the app

Bypassing the app wasn't difficult. In fact, Moore says he built two Chrome extensions on Claude in minutes.

The first extension he built replicated the Android app, but with the ID checks removed. This meant he could skip the need for a user to scan a document entirely.

"It detects the QR code automatically (when presented by a website) and passes verification," Moore explains, adding that the process is entirely automated with no need to interact with the Chrome extension once installed."

This week, Moore went further and built a Chrome extension that can capture the QR code from a website and automatically forward it to a remote, automated phone to get a genuine signature in seconds.

#EU #AgeVerification unfixable bypass:✅ Automate the device✅ Detect and relay the QR code⏱️ Push to GitHubOnce an age verification QR code appears, it will detect & automatically relay to a legitimate device that completes the verification remotely.If a "technically… [https://t.co/O0Z0BpCOs8July](https://t.co/O0Z0BpCOs8July) 31, 2026


Known as an 'automated relay bypass,' these attacks mean nothing in the process is faked, making prevention almost impossible.

"Even after they enable all other protection mechanisms, both will continue to work," Moore said.

## The EU’s response

When asked whether any steps were taken to prevent circumvention, a European Commission spokesperson said: "We of course rely also on parents and caretakers to check what children are doing online," adding that the app's goal is "avoiding the unintended exposure of kids to inappropriate content."

Yet, according to Moore, lawmakers' focus is misdirected. He said: "What [lawmakers] are missing is that the threat actor isn't a third party; the threat actor is the user.

"They don't want age verification in the first place, so they are going to look for ways to bypass the system. And if the system can be bypassed by design, they will do it."

Deciding not to impose a new law or technology simply because it could be bypassed is unlikely to convince lawmakers. But the problem may extend beyond an ineffective system.

In fact, Moore fears that the app's inevitable ineffectiveness could push lawmakers to turn to more invasive checks and an erosion of people's privacy.

## Next step? Our identity

 ![Portrait of woman with shadow of barcode on her face](https://cdn.mos.cms.futurecdn.net/Kt2wdffrUY7GtKPe65LRy6.jpg) 


When Moore says the concept is broken, he is calling out what he sees as a fundamental flaw in the EU age verification framework's design: client-side trust.

The app is more privacy-preserving than passports and face scans because the data won’t leave the user’s device. But this may be exactly why its implementation is bound to fail. If nothing leaves the device, Moore explains, there is no way to trust or verify what has been obtained.

This creates a problematic catch-22 for European lawmakers. When this ‘anonymous’ app fails to keep kids off restricted sites, Moore contends that Brussels is unlikely to simply give up on its flagship safety initiative and drop privacy-preserving practices altogether.

"For them to push ahead with it under the guise of child safety is an escalation path to say we've tried this; the natural route is now you've got to prove your identity," Moore told TechRadar.

It’s clear that age verification is here to stay, despite continuous outcry coming from privacy advocates, technologists, and data scientists who warn it may do more harm than good.

For Moore, the danger is that what’s marketed as a privacy-first breakthrough today may ultimately be used to undermine privacy tomorrow.

*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds. Make sure to click the Follow button!*

![Chiara Castro](https://cdn.mos.cms.futurecdn.net/dBfKg5tPHAd74JPLWVCzQg.jpg)

Chiara is a multimedia journalist committed to covering stories to help promote the rights and denounce the abuses of the digital side of life – wherever cybersecurity, markets, and politics tangle up. She believes an open, uncensored, and private internet is a basic human need and wants to use her knowledge of VPNs to help readers take back control. She writes news, interviews, and analysis on data privacy, online censorship, digital rights, tech policies, and security software, with a special focus on VPNs, for TechRadar and TechRadar Pro. Got a story, tip-off, or something tech-interesting to say? Reach out to [chiara.castro@futurenet.com](mailto:chiara.castro@futurenet.com)

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
