---
title: Intel's Googlebooks might not run some Android apps as well as Qualcomm's —
  Google says this is because Android apps were designed for Arm chips
source_url: https://www.tomshardware.com/laptops/ultrabooks-ultraportables/intels-googlebooks-might-not-run-some-android-apps-as-well-as-qualcomms-google-says-this-is-because-android-apps-were-designed-for-arm-chips
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-05T22:03:23Z'
published: '2026-10-05T00:00:00Z'
description: Google hasn't said which apps are affected.
image: https://cdn.mos.cms.futurecdn.net/S36LUQXQBe6D3TPy2TNwYM-1920-80.jpg
categories:
- Technology & Software
- Hardware
people:
- Jhet Borja
- Tom
locations:
- Java
- Kotlin
organisations:
- ARM
- ARM64
- Acer
- Android Authority
- Apple
- Dell XPS Googlebook
- Get Tom's Hardware
- Google News
- Googlebookx
- HP Googlebook
- Intel Bridge
- Intel Googlebook
- Intel Googlebooks
- Lenovo
- Mac
- Native Bridge
- Play Store
- Qualcomm Googlebooks
- Snapdragon X Elite
---

![Googlebook notebook](https://cdn.mos.cms.futurecdn.net/S36LUQXQBe6D3TPy2TNwYM-1920-80.jpg)

Google introduced five new laptops recently, which went on sale Sunday. The Googlebooks are intended to run Android apps natively; however, Google admitted in a statement to *Android Authority* that not all apps may perform as well on the systems with Intel processors as those with Qualcomm chips.  
"The vast majority of Android apps run smoothly across both Intel and Qualcomm Googlebooks right out of the box," Google told the Android-focused site. "Because many Android apps were originally designed for Arm chips, a small handful of complex apps or games need some developer tuning to run their best on Intel-based platforms. We’re working hand-in-hand with app developers, Intel, and Qualcomm to continuously optimize performance and expand compatibility across the entire portfolio."

Google has not named specific apps that might have issues on Intel-based systems. None of these claims were made prior to Googlebooks being made available on store shelves.

The Googlebooks with Intel processors are the Asus Googlebook 14, Lenovo Googlebook 15, and Acer Googlebook 14. The Dell XPS Googlebook and HP Googlebook 14 use Qualcomm's Snapdragon X Elite chips.

Most Android apps will work on Intel Googlebooks due to the wide use of Kotlin for Android development, and many apps have been made using Java. If an app's pipeline is mostly Java/Kotlin, it will have a high chance of working on the Intel Googlebook thanks to their architecture-agnostic libraries and SDKs.

However, there are still apps out there relying on native components compiled exclusively for ARM64 with no x86-64 versions. Intel Bridge and Android’s Native Bridge can translate ARM64 code for x86 compatibility, but unless the developer actually accounts for x86, it might run into some issues.

All of the applications on Googlebookx will come from Google's Play Store, which will include a mix of optimized and unoptimized apps. You can't download applications from the web unless you're redirected to Google Play.

Google wants to compete with the Mac by offering a full Android ecosystem experience from phone to laptop, similar to the conveniences Apple offers between their laptops and phones. With prices ranging from $899-1,299, it is a fairly large jump from the MacBook Neo’s $699-799; however, the Googlebook offers more RAM, giving you either 16GB or 32GB options. Storage remains limited, only offering either 256GB or 512GB, but each Googlebook comes with 12 months of Google AI Pro that includes 5TB of cloud storage currently valued at $249.99.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Jhet Borja](https://cdn.mos.cms.futurecdn.net/niBNJTDN6c99Ri7HD5zNZ8-140-80.png)

Jhet Borja is a serial hobbyist who was taking apart toys from childhood and sketching inventions. He now loves doing DIY projects ranging from designing custom 3D-printed parts, building PCs and keyboards, all the way to woodworking. If he's not getting his hands dirty, he's probably brainstorming his next project.

* I really doubt translating ARM apps to x86 chips works as the opposite. People have never really worked on it because nobody cares about running ARM apps on x86. I don’t think the infinitely more mature x86 to ARM translation layers can just be flipped around to go the opposite direction without significant work. Intel probably should have steered clear of this. ARM chips will destroy it in any benchmarking of Android apps on these “not Chromebooks”.Reply
* hotaru251 said:.....tell that to apple who made x86 run on arm sometiems betetr than native...  
    
  Google just being lazy and not wanting to develop a better transition layer.Name one x86 app that runs better on Apple silicon through translation than it does on equally modern and expensive x86 chips. Extraordinary claims require extraordinary evidence. Now don’t bring me something running an ARM native version because thats not what you claimed. Reply
