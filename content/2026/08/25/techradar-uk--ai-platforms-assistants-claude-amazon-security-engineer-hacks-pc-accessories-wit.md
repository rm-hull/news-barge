---
title: '''Any device attached to a PC could have a malicious firmware implant performed'':
  Amazon security engineer hacks PC accessories with Claude Opus, warning of the major
  threats AI could pose in the future'
source_url: https://www.techradar.com/ai-platforms-assistants/claude/amazon-security-engineer-hacks-pc-accessories-with-claude-opus-to-make-them-work-better-asus-insta360-and-elgato-products-reverse-engineered-in-hours-for-better-control-but-engineer-admits-this-also-scares-me
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-25T08:56:16Z'
published: '2026-08-25T00:00:00Z'
description: Some nifty tricks are pulled off by the security engineer — but the dark
  side of all this is worrying to say the least.
image: https://cdn.mos.cms.futurecdn.net/gYocvkPAnx8FcKQz6eTGsa-2560-80.jpg
---

![Confused PC gamer looking at screen](https://cdn.mos.cms.futurecdn.net/gYocvkPAnx8FcKQz6eTGsa.jpg) 

- **A security engineer at Amazon hacked a bunch of peripherals using AI**
- **Claude Opus did most of the legwork in applying modified firmware to a webcam, microphone and more**
- **The relative ease with which AI allows this kind of modification points to a worrying future of peripherals being compromised on a grander scale**

In another example of how AI could prove to be a threat to our devices, an Amazon security engineer has demonstrated how powerful Claude Opus is when it comes to reverse engineering PC peripherals.

Chaz Schlarp, who's a Senior Security Engineer at Amazon, wrote a blog post about experiments he conducted with a bunch of peripherals such as a webcam and a microphone.

He wanted to find out how easy it was to modify the firmware and pull off some useful tricks with these devices using AI, but clearly there's a darker side here — namely that the same access could be leveraged by a malicious actor to compromise your system via these gadgets.

Schlarp used Claude Opus 5 to mess around with the firmware for an Insta360 webcam, a Shure microphone, an Asus monitor, an Elgato video capture stick, and an Elgato mini-light (a compact device for lighting your streaming videos).

Schlarp explains: "My process was pretty much the same for each of these devices: grab a copy of the device's firmware and associated update tool from the manufacturer, throw it into my reverse engineering environment, tell Claude Opus 5 what my goals are, and let it churn."

One thing that became quite clear to the security engineer was that these devices lacked any decent firmware integrity protection to prevent modifying and applying a new firmware. Only the Elgato light had any defenses in this respect, and they were easy enough to circumvent.

Schlarp explains a trick with his Asus ROG Swift PG42UQ monitor to demonstrate the kind of useful utility that can be on offer with this kind of firmware modding. He found it was possible to remove an annoying pop-up warning that periodically tells the owner to run the 'pixel cleaning' process (although the engineer hasn't implemented the fix in the firmware yet). He also discovered a way to get DisplayWidget (a Windows utility) features running on his Linux system, with a shell script that can flick through certain bits of functionality like the hardware crosshair or FPS counter (which could be set up on hotkeys).

Sign up for breaking news, reviews, opinion, top tech deals, and more.

Most of what he did, though, was about proving how relatively easy it was to subvert the firmware using AI to do the heavy lifting, and, for example, disable the webcam's recording light (in the style of surveillance malware, so the user wouldn't know if the camera was secretly recording). He pulled off a similar feat with the microphone, so the mute LED could be on while the mic wasn't actually muted (this was leveraged via a 'full plaintext command shell').

Schlarp observed: "Peripherals have proven to be an ideal target for agentic RE [reverse engineering] — they're tiny computers attached to my computer, with a data connection to the host and usually a firmware update mechanism, so an agent has something to iterate against. The net outcome is better control and understanding of my machine."

## Analysis: fast-tracked exploits?

 ![Shure MV7 microphone](https://cdn.mos.cms.futurecdn.net/xyobc3yZ8F2nn4HA7tQEXY.jpg) 


The key point here is how easy Claude Opus made this task. 'Owning' all five of these peripherals boiled down to 13 hours of the AI beavering away under its own steam with just shy of 100 prompts from its human overseer.

Schlarp notes that: "Hardware is almost universally 'open' for tinkering at this point with just a couple hours of mostly hands-off machine-driven labor each, and I look forward to a near future where I can add features to my webcam firmware as easily as I can to software that runs on my Linux machine itself."

However, as mentioned, there's the dark side to all this, as Schlarp makes clear: "On the other hand, as a security professional, this scares me for several reasons. I would work from the operating assumption that any device attached to a computer could have had a malicious firmware implant performed, where previously that required significant per-model investment and was stereotyped as a 'state actor' kind of activity."

In other words, the main difficulty in executing these kinds of exploits is the labor and time required, which currently limits this to individually targeted attacks on more high value targets. However, now an AI agent is capable of doing the grunt work, it makes sense that these kinds of attacks could be far more prevalent as time rolls on.

That means all those peripherals attached to your PC could be used as ways to compromise you, or your system, in the future. Schlarp informs us that he's also managed to get a root shell on a commercial Dell display, adding that: "Obviously it was never best practice to let untrusted clients touch these things, but the speed and scale at which this can be executed makes the risk so much higher now."

There's a potentially bigger threat here, too: an AI-powered worm that automatically actions this kind of reverse engineering. Schlarp explains: "It's only a tiny leap to imagine that someone could make a self-replicating piece of malware that probes its environment, relaying reconnaissance back to a smart command-and-control that actively works to push itself into accessories and IoT devices and industrial equipment found adjacent to an infected target."

There are a lot of worries about where AI could be leading us, and far more dangerous security threats looming in the future (or indeed the present) is another unfortunate prospect to say the least.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![An Apple MacBook Air against a white background](https://cdn.mos.cms.futurecdn.net/LocVgRosBUWfJzDitFzhKR.png) 

➡️ **Read our full guide to the best laptops1. Best overall:** 

Apple MacBook Air 13-inch M5**2. Best budget:** 

Apple MacBook Neo**3. Best Windows 11 laptop**

Microsoft Surface Laptop 13-inch**4. Best thin and light:**

Lenovo Yoga Slim 9i**5. Best Ultrabook**

Asus Zenbook S 16

Darren is a freelancer writing news and features for TechRadar (and occasionally T3) across a broad range of computing topics including CPUs, GPUs, various other hardware, VPNs, antivirus and more. He has written about tech for the best part of three decades, and writes books in his spare time (his debut novel - 'I Know What You Did Last Supper' - was published by Hachette UK in 2013).

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
