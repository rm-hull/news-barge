---
title: '''Enhance!'': YouTuber discovers audio technique that can pinpoint your video''s
  location to within 100m — even when you''re far from civilization'
source_url: https://www.techradar.com/computing/cyber-security/youtuber-discovers-aircraft-noise-trick-that-can-geolocate-your-videos-to-within-100m-doppler-effect-pinpoints-locations-from-just-60-seconds-of-audio
source_site: TechRadar UK
source_slug: techradar-uk
description: Take one video, listen to the background and match it with airplane flight
  data to reveal where it was filmed.
image: https://cdn.mos.cms.futurecdn.net/v4B33mcbGoi3AzTquvMznP-2000-80.jpg
published: '2026-11-03T00:00:00Z'
scraped_at: '2026-11-03T17:01:25Z'
categories:
- Technology & Software
- Film & TV
people:
- YouTuber Colsto
locations:
- US
organisations:
- Colsto
- FBI
---

![A laptop showing a spectogram next to a propellor plane in flight](https://cdn.mos.cms.futurecdn.net/v4B33mcbGoi3AzTquvMznP-1920-80.jpg)

* **Security researcher combined audio analysis, flight data and a lot of number-crunching to identify audio locations**
* **Aircraft that are inaudible on the soundtrack can still reveal the recorder's location**
* **The technique is apparently accurate to within 100m**

If, like me, you grew up watching corny FBI shows where computers could do the impossible through made-up technology with a single command of "enhance!", you're going to love the apparently impossible thing that YouTuber Colsto has just described in a new viral video.

Using a Doppler effect technique (more on that below), the location of a video or audio recording can be identified to within 100 meters through a combination of inaudible audio, flight data and math. This is no movie magic or scriptwriter invention: it's real and it's a little bit scary too.

I've embedded the video below and would really recommend watching it, because Colsto goes into great detail about how it's done, what it can't do and what precautions you might want to take if you don't want your background to betray you.

## How your video background can betray you

![I discovered a sound that leaks your exact location (and it's everywhere) - YouTube](https://img.youtube.com/vi/UytYrhYLOKI/maxresdefault.jpg)

As Colsto explains, the key is the 'Doppler effect'. That's the way sounds appear to change based on the distance between a moving source and the listener. You hear it all the time: it's what makes fire engine and ambulance sirens, car stereos and airplane propellers seem to change pitch as they go past.

What's clever here is that Colsto has focused on the sounds made by aircraft in the backgrounds of videos. In many parts of the world the skies are very busy, and a faraway airplane that's inaudible to you or other listeners might still leave a sonic footprint on your video or audio that can be isolated and analyzed. That's definitely the case in the US data Colsto used.

Once you've got the audio, the aircraft sound can then be matched with publicly available flight data and Doppler curve measurements. By triangulating the sound from multiple aircraft, you can then identify where the audio was recorded. This is enormously clever.

Colsto explains the detail in the video — what aircraft data was used, how it was analyzed, how the Doppler measurements were filtered and what corrections were made — but isn't posting any software or other tools to actually do it for you. Instead, you'll get an assessment of preventive measurements including why normal signal processing such as high-pass filters or noise reduction can be ineffective.

Sign up for breaking news, reviews, opinion, top tech deals, and more.

## How scary is this?

![A laptop screen showing a Doppler curve](https://cdn.mos.cms.futurecdn.net/PJP8k6XKvbHdMhrkTxtKQJ-1200-80.jpg)

Colsto was keen to point out that the video is designed to be educational about open-source intelligence (OSINT) techniques, rather than an attempt to fear-monger.

"The odds that someone can and does actually do this is pretty slim. In reality, there's probably a hundred easier ways to find you than this," he says.

However, these are some potential use cases. "The audio we used is just from some random security camera, but it could have just as well been footage from a investigation or a video online. Something with literally zero visual clues could be located using this," he added.

So despite the somewhat niche application, there's something deeply scary about this kind of thing, I think, and from similar revelations such as Wi-Fi routers that can be used to locate you indoors and Wi-Fi signals that can help track your movements, even if you're not carrying a phone that connects to them.

And I know that fear is probably a bit silly when everywhere I go I carry a phone, use a tablet or drive a car that's leaking identifiable information to God-knows-who. But I can't help asking the question: if the possibilities we know about are this scary, what on Earth is the tech we *don't* know about capable of?

## Thinking of buying a new TV?

*Try our TV size and model finder! You tell it how far you sit from your TV, we'll tell you what size to buy based on viewing angle advice from image quality experts, and we'll recommend our three top TVs at that size for different prices.*
