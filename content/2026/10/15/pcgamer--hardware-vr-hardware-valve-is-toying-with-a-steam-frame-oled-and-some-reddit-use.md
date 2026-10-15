---
title: Steam Frame OLED shows up in datamined source files—but don't hold your breath
source_url: https://www.pcgamer.com/hardware/vr-hardware/valve-is-toying-with-a-steam-frame-oled-and-some-reddit-users-are-already-wondering-whether-to-wait-an-excruciatingly-long-time-for-it-even-though-it-may-never-happen/
source_site: PC Gamer
source_slug: pcgamer
scraped_at: '2026-10-15T11:28:42Z'
published: '2026-10-15T00:00:00Z'
description: Some Reddit users are already wondering whether to wait an excruciatingly
  long time for it even though it may never happen
image: https://cdn.mos.cms.futurecdn.net/XU4x9kWqRwDZaJkxsimxHT-1920-80.jpg
categories:
- Technology & Software
people:
- Brad Lynch
- Gabe Rowe
- Josh Hudman
- Runaway42
- True Deckard
- Valve
locations:
- Deckard
- Deckard-Plano
organisations:
- FrameOS
- OLED
- PC Gamer Circuit Breaker
- Reddit
- Samsung Galaxy XR
- Steam Frame
- SteamFrameHub
- VR
- Valve
---

![The Steam Frame&#039;s pancake lenses on display.](https://cdn.mos.cms.futurecdn.net/XU4x9kWqRwDZaJkxsimxHT-1920-80.jpg)

Only a month out from the launch of the Steam Frame, an OLED version is already the talk of the town. Moreover, us humans seem to have very short memories, as while this amounts to nothing more than a couple of lines in the Steam Frame source code—perhaps nothing more than someone at Valve messing around to see what happens—some Reddit users are already wondering whether this is worth waiting for instead of buying a Frame today. Oh, you lot…

In the Steam Frame source code, SteamFrameHub spotted various references to "deckard-oled" and "deckard-plano". Deckard is the codename given to the Steam Frame, so the deckard-oled branch (last edited in February) and the deckard-plano branch (last edited a few weeks ago) are some sorta version of the Steam Frame that Valve's playing around with.

I've had a quick look around the repo and, yep, deckard-oled and deckard-plano are in there. That's a very exciting prospect, as the Steam Frame's LCD displays are definitely lacking compared to VR headsets with Micro-OLED.

This excitement is not lost on some over on Reddit, who have responded to the news with various japes and bits about ditching their reservation for the existing model and instead re-enlisting for another excruciatingly long wait for the OLED model.

"Waitlist 2: Electric Boogaloo," says brantrix in a thread over at r/SteamFrame.

"Absolutely panic and cancel your reservations. Everyone knows how lightning fast Valve moves fast with development," says Runaway42.

Truth is, we're not likely to see a Steam Frame OLED for a very long time—or ever. There are the trifling matters of hardware, resolution, power, cooling, battery life, and performance all to consider. It's more than a matter of just swapping the optics in the core module—the main bit of the Steam Frame containing the displays, SoC, cooling, sensors, and more—with a couple of OLED panels.

The PC Gamer Circuit Breaker newsletter breaks down the latest PC gaming tech, and finds you the best deals on the best products

Here's big VR fan and regular update spotter Brad Lynch on the whole thing:

> Took a look at the Deckard-Plano (Micro-OLED Frame) stuff… after waking up to pure panic Yeah it’s in there. And they do a lot of wacky things to make it possible… with the current 8 Gen 3 chip They even pair it with the upcoming hotswappable battery headstrap by default In my opinion, that’s probably required due to power consumption.. And while I would love to say “True Deckard soon,” I genuinely think they’re better off waiting a bit more for the Compute module to upgraded to a newer chip, with these Micro-OLED displays that ALSO need new optics You could argue that it’s only for streaming PCVR, but I disagree. Valve built just enough of FrameOS to support the Spatial Computing usecase to where people can do some amazing things with a Linux PC on their Face. And while that’s still hella buggy, and taped together.. that’s just software waiting to be fixed When you switch to Micro-OLED, you get way better visuals. But lose VR gaming focused aspects such as FoV and motion clarity. BUT it still is a greater experience, in my opinion, for many other things Valve positions the current Frame as a way to play the entire 2D game library. Verified titles for those is quickly growing way faster than VR titles But frankly, the current display/optics setup truly doesn’t make that usecase more enjoyable. A slightly lower FoV + Micro-OLED system definitely would But even with the foveal magic they’re introducing here in the code, that doesn’t solve the heat and performance problems even with streaming. The 8 Gen 3 isn’t THAT much better than the chip in the Samsung Galaxy XR. Which uses a lot of these same tricks on an XR2+ Gen 2 That headset throttles a lot even when streaming. It’s a serious problem So when I combine all of these thoughts together in my head. I actually just hope that this is an optics/display prototype being prepped for a bit later down the line. Rather than a Steam Deck/Steam Deck OLED situation The software situation on Steam OS (for Frame) is still a mess. And to have valve engineers and contractors split between supporting two models THIS FAST, after such a rough launch, would be a bit of negligence, imo At the end of the day, I knew valve would adopt Micro-OLED in one of their Headset products at some point. They’ve put serious effort into it over the past deckade and a half they’ve been doing VR. I’ve reported on some truly insane stuff they did in this field. It is inevitable But for this, I pray that inevitability is a bit further out..October 14, 2026

That said, the Steam Frame is a modular thing. We should expect, or at least hope for, its modularity to develop into a bit more of an ecosystem of parts. We've used the Arcturus Vision RGB Camera, and we know Valve is working on an updated strap with off-ear speakers and swappable batteries, but there could be more in future. For now, we have the CAD files to make our own upgrades.

And if you're wondering if these mentions in the source files are some sort of viral marketing stunt or secret message intended to build hype once again for a future product, here's what Valve's engineers told me at their office last year.

"Everybody assumes that we have some sort of like grand plan with our leaks," Valve employee Gabe Rowe said, "and it's literally just somebody fat fingering something."

"Usually we all look around like, 'who leaked?'," Josh Hudman said.

I wonder who accidentally pressed the button this time?

![Valve&#039;s Steam Frame on its own on a white background.](https://cdn.mos.cms.futurecdn.net/JpVeedA2TeSZdXtJC7rcr7-140-80.jpg)
