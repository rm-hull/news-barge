---
title: Researchers found yet another way our tech is betraying us, and this time the
  culprit is the humble HDMI cable — it turns out someone can wirelessly mimic the
  video from your wired connection using its radiation (and yes, AI is what’s changed
  the game)
source_url: https://www.techradar.com/computing/cyber-security/this-shocking-video-shows-how-ai-can-read-the-radiation-coming-from-an-hdmi-cable-to-mimic-the-video-being-passed-over-the-cable-not-even-wired-connections-are-safe-from-spy-tech
source_site: TechRadar UK
source_slug: techradar-uk
description: A new AI tool has improved text accuracy by over 60% in signals intercepted
  from ordinary HDMI cables
image: https://cdn.mos.cms.futurecdn.net/AzZkPJKaNZWUp3DoLp34kZ-1920-80.jpg
published: '2026-11-09T00:00:00Z'
scraped_at: '2026-11-09T23:50:28Z'
categories:
- Technology & Software
people:
- Federico Larroca
locations:
- Montevideo
- TempestSDR
- US
- Uruguay
organisations:
- DeepTempest
- HackRF
- NSA
- Psalter
- US National Security Agency
- University of the Republic
---

![A split image, showing an image on a monitor on the right, an HDMI cable in the middle, and then a blurry, recreated version of the first image on the left](https://cdn.mos.cms.futurecdn.net/AzZkPJKaNZWUp3DoLp34kZ-1920-80.jpg)

* **There is tech that can turn the radiation from HDMI cables back into video**
* **AI reduces errors in intercepted signals by over 60%**
* **Digital is harder to decode than analog, but it's not impossible**

Last week we discovered that your videos can give away your location thanks to airplane noises in the background that you can't even hear, and we've known for some years that Wi-Fi routers can be used to spot where people are in a room. So it's not a huge surprise to discover yet another way our tech is betraying us — and this time the culprit is the humble HDMI cable.

A post on X by Psalter shows TempestSDR, which can capture the signal from your HDMI cable and almost recreate the image on another screen, because the cable creates an electromagnetic field that can be read. The quality isn't great, but if you bring AI into the mix you can enhance it to make text readable and images clearer. An AI system especially for the task, called DeepTempest, reduces errors by over 60%.

The video below is quite alarming.

> your HDMI cable can leak what’s on your screen watch the laptop on the left. it reconstructs the video playing on the monitor beside it from radio signals leaking out of the HDMI connection this is TempestSDR. an antenna picks up the leakage, a HackRF radio captures it, and software turns it back into an image researchers took this further with Deep-TEMPEST, using AI to make recovered images and text easier to read. this clip shows the original technique quality depends on shielding, distance and interference. the picture is imperfect, but recognizable content still gets through a wired connection can still leave a wireless traceNovember 8, 2026

Intercepting or playing with electronic leakage isn't new: 2001's Tempest for Eliza broadcast music to your radio by sending RF signals via your monitor, displaying images that generated specific radio frequencies. What's new is the AI element.

## Is it time to don the tinfoil hat?

Not yet. DeepTempest does dramatically enhance images and reduce text errors, but as you can see from the video things are still pretty indistinct — and that's when the cable you're intercepting is right next to you, so you're close enough to see the display that you're intercepting.

You're not going to see much if you're in a van across the street, even if the cable being used is really poorly shielded, unless you've got a seriously powerful scanner.

DeepTempest was developed by Federico Larroca at the University of the Republic in Montevideo, Uruguay, and it does represent a major step forward: using text capture software DeepTempest was able to reconstruct text with roughly 30% of characters being misinterpreted.

Sign up for breaking news, reviews, opinion, top tech deals, and more.

That sounds like a lot but it's not enough to render text incomprehensible to human readers. And that error rate is a whopping 60% lower than the previous state-of-the-art attack.

The word Tempest is used in these systems because it's a US National Security Agency (NSA) codename that refers to spying via electromagnetic leakage, and measures to prevent it.

Those measures are distance, shielding, filtering and masking, and they consider more than just leakage: they also include sounds and vibrations, so for example it's possible to log keystrokes via a phone's motion sensor.

The history of this is fascinating and goes back to the Second World War, where the US military's teleprinters were found to be generating detectable electromagnetic spikes that could be intercepted to capture the text. The recommendation for shielding, filtering and masking comes from the machines' supplier, Bell System, and while technology has advanced somewhat since then the advice is still sound: if you're the kind of person that security services or other shadowy organizations might be interested in, don't buy crappy cables.

Pricier cables have electromagnetic shielding, and while high-end companies used to tell us that was essential because otherwise the audio and video fidelity wouldn't be as pristine as you want… but maybe it's signal leaking out rather than in that people will be more worried about in the modern world.
