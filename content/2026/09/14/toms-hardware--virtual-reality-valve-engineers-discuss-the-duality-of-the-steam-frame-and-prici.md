---
title: Valve engineers discuss the duality of the Steam Frame and pricing — Valve's
  newest VR headset pivots SteamOS to Arm
source_url: https://www.tomshardware.com/virtual-reality/valve-engineers-discuss-the-duality-of-the-steam-frame-and-pricing-valves-newest-vr-headset-pivots-steamos-to-arm
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-14T20:18:21Z'
published: '2026-09-14T00:00:00Z'
description: Be prepared for sticker shock
image: https://cdn.mos.cms.futurecdn.net/GREi4LEjsga68aPho9Xe6B-1920-80.jpg
---

![Valve Steam Frame](https://cdn.mos.cms.futurecdn.net/GREi4LEjsga68aPho9Xe6B.jpg) 

I spoke with Valve software developers Pierre-Loup Griffais and Jeff Leinbaugh about the Steam Frame launch, why the company is taking a two-pronged strategy with streaming and standalone support, and how the global memory/storage crunch affected development. You can read our review of the Steam Frame here, and the full transcript of our interview at *Tom's Hardware Premium**.* 

Nearly a year after __first revealing the Steam Frame__ VR headset, Valve is now ready to deliver the finished product to paying customers. Reservations for the headset have opened today, three months after the launch of the __Steam Machine__.

Like the Steam Machine, the Steam Frame is launching amid absolute chaos in the tech industry. We're seeing higher prices across a wide range of PC hardware, especially memory and storage. Valve isn't operating in a vacuum, so those realities are reflected in the Steam Frame's pricing, which starts at $1,059.

I began by asking about the headset's genesis and the team's goals for creating a next-generation VR headset. "Work started on Steam Frame basically as soon as we shipped the Index," explained Leinbaugh. “And so we did a lot of exploration into technologies and features and use cases to try to answer that question. And the goals that we aligned on for what became the Steam Frame was to make [it] much easier to use, which to us meant a lighter, more comfortable, easier to get into and out of VR headset."

He added that with the previous Index headset, Valve was so laser-focused on making the best VR headset possible at the time that they made a lot of compromises to achieve those goals. And in many ways, those compromises were worth it to achieve their end goal. However, that strategy shifted with the Steam Frame.

"But this time around we thought we could achieve something that was a lot more comfortable, a lot more accessible. And so streaming technology was a big part of that. So the headset can be wireless so that there's not a lot of complicated setup to get to the game, whether that's playing on the headset or streamed," Leinbaugh continued. "So what we want to be possible is for somebody to put on the headset, browse their Steam library, and then just pick something that they want to play and not worry about too much else."

## Standalone gaming on the Steam Frame

One of the biggest changes with the Steam Frame is that it can work with a robust wireless link to your PC, or as a standalone device using the onboard Qualcomm Snapdragon 8 Gen 3 SoC. I asked about the challenges in developing such a lightweight headset that can easily switch between operating modes.

"Yeah, a lot of the engineering challenges were around making sure that we had the right kind of compute and enough compute on the headset to both support a really good streaming experience, but also to be able to run games on the headset," said Leinbaugh. "So we picked the Qualcomm 8650 chip. It had a lot of capability, but in order to make use of that, we had to solve a lot of engineering challenges around thermal management and power delivery. So really treating this like making a really capable PC that just happens to run this particular mobile hardware was how a lot of the engineers approached that problem."

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

He added that Valve has taken a lot of the know-how from the __Steam Deck__ and Steam Machine to give users the same SteamOS, but this time leveraging the Arm hardware along with Proton for emulation.

However, the Steam Frame has limits when playing games directly on-device, given its mobile-centric SoC. “Sure, games that are trying to push the boundaries on the AAA stuff that's very graphically intensive," explained Griffais. "Most of those recent ones won't run very well because it's a smaller compute envelope, right?"

"But there's a ton of stuff that is coming out that is a great experience on the Steam Frame. For example, I think last week the *Metal Gear Solid Collection Part 2* released. And, you know,*MGS4* is a game that I haven't played in, I don't know, 20 years at this point, but it's great from there."

He added that many indie games will run just fine on the Steam Frame, along with older back-catalog AAA games (which are still enjoyable) that don't require the compute of more modern titles.

"So I think the point is that you're able to engage with your whole library, right?" said Griffais. "And then have kind of a similar thing as the Deck where you're going to try and figure out if some games are maybe a little bit below the bar in terms of what you would like for performance."

Half-Life Alyx has been the poster child for VR gaming in recent years, and Valve has taken steps to ensure that Steam Frame users can have a proper native gaming experience. “And we're doing the same for Half-Life Alyx, where we're doing a lot of work to support the Frame more natively and trying to remove performance barriers that are induced by some of the translation, the emulation there that you get on normal and modified PC games.,” said Griffais.

## Streaming on the Steam Frame

While standalone gaming on the Steam Frame is possible, Valve designed the headset first and foremost as a streaming device. To that end, Valve has taken steps to optimize the networking stack and improve performance. One of those steps is implementing foveated streaming to reduce strain on network resources.

“So the Steam Frame has eye-tracking cameras on the inside of the headset that know where your eyes are looking. And when you have that, there's a lot of potential use cases, but the one that we're using most consistently is foveated streaming, which really means when you're streaming, especially VR content, there's a lot of video data that you have to send," Leinbaugh explained.

"But because we know with eye-tracking cameras what part of the image you're looking at at any time, we can refocus some of those resources to make sure that the important parts of the image are treated as like first-class bits. And then the rest gets kind of the last part of the resource pool, which is the part of the image that you can't see and you won't notice the image degradation."

By not treating every bit delivered to the headset the same, Valve can reap performance and image quality gains. "So it's the best analogy really is it's almost as if the part that you're looking at is using about 10 times as much bandwidth and encoding bit rate as it actually is for the entire image, because we just squished it all into that part that follows where you're looking."

 ![Valve Steam Frame 3](https://cdn.mos.cms.futurecdn.net/iggh3pLQEFEgHSu4i5Wruk.jpg) 


The Steam Frame communicates with your PC wirelessly using a dedicated Wi-Fi 6E USB dongle. Data transfers between the two happen over the 6 GHz channel for optimal performance. I inquired about how any disruptions/interference with that wireless link would affect gameplay.

“So there's a fallback mechanism built into that, which, if you have two links active and one of them drops out because of interference, or you walked out of range, or all the many reasons that wireless interference can happen," said Leinbaugh. "If something happens to one of those links, the other one will immediately pick up and cover the gap. And it's just very unlikely that a lot of those sources of interference will hit both links at the exact same time."

Other strategies can also step in; for example, if you have a latency spike, a previous frame can be "reprojected and replayed" to cover small gaps. For extended dropouts, there's no recovery method; the stream will fail, and you'll be booted to the default environment.

There are also other strategies that can step in; for example, if you have a latency spike, a previous frame can be "reprojected and replayed" to cover small gaps. For extended dropouts, there's no recovery method; the stream will fail, and you'll be booted to the default environment.

## Pricing and availability

Pricing, of course, will be a big sticking point with the Steam Frame. Consumers got a bit of sticker shock with the Steam Machine given its hardware specs, and the Steam Frame will likely be no different. The Steam Frame starts at $1,069 for the 256GB SKU and costs $1,299 for the 1TB SKU.

"I think as far as memory prices and those kinds of conditions, we're really in it like everyone else," Griffais explained. "We've been working hard on trying to get the parts that we can get at the best price possible."

While all of us would love for memory and storage prices to fall to sane levels again, it will be a while before we see any relief. "It's an unfortunate situation all around. We wish that gaming hardware was cheaper, but we're definitely trying to be on the cheapest side that we can get despite all those conditions," Griffais explained.

But price increases aren't just limited to the likes of memory, as Griffais added, “Even just things like motherboards, copper, anything, even shipping anything worldwide right now is way more expensive than it was last year and two years ago. So every part of the sticker price is affected there."

The Steam Frame will be available starting September 14, and it will use a reservation system similar to that of the Steam Machine to cut down on scalpers.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Brandon Hill](https://cdn.mos.cms.futurecdn.net/yHeufe7JcvuJBhYPkSexNf.jpg) 

Brandon Hill is a senior editor at Tom's Hardware. He has written about PC and Mac tech since the late 1990s with bylines at AnandTech, DailyTech, and Hot Hardware. When he is not consuming copious amounts of tech news, he can be found enjoying the NC mountains or the beach with his wife and two sons.
