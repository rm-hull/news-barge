---
title: Valve confirms Steam Machine red light overheating warning is showing earlier
  than it should; BIOS fix on the way — will raise temperature warning threshold to
  100 Degrees Celsius
source_url: https://www.tomshardware.com/pc-components/cooling/valve-confirms-steam-machine-red-light-overheating-warning-is-showing-earlier-than-it-should-bios-fix-on-the-way-will-raise-temperature-warning-threshold-to-100-degrees-celsius
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-13T14:56:19Z'
published: '2026-07-13T00:00:00Z'
description: Currently users are seeing this ominous warning sign when the CPU hits
  95°C and/or the GPU 90°C.
image: https://cdn.mos.cms.futurecdn.net/5grECmepVDmbQUMRgZsqVY-1920-80.jpg
---

![Valve Steam Machine](https://cdn.mos.cms.futurecdn.net/5grECmepVDmbQUMRgZsqVY.jpg) 

We're enduring a particularly hot summer in the northern hemisphere, so it is understandable if powerful, pint-sized PCs are getting relatively toasty during long gaming sessions. However, Valve has confirmed that the Steam Machine's red light bar warning is bugged and being triggered prematurely. Redditor Pure-Outcome-5977 shared a Steam Support message that appears to confirm that a BIOS fix is on the way to raise the temperature and throttling red light warning threshold for the CPU/GPU from 95/90 to 100/100 degrees Celsius.

There appears to be a little miscommunication going on between the Redditor and Steam Support. Pure-Outcome-5977’s red warning light was coming on with system monitor tools showing the CPU was at 81°C and the GPU at 71°C. So the red light bar warning trigger temperatures of 95/90°C seem to be bugged. Thus, they got an answer to a slightly different issue than the one they raised.

“After discussing with our engineers, there is a known issue with the current BIOS that results in the red LED lights displaying much earlier than they should,” admits the Steam Support person in the message screenshot. “The issue is just with when the lights are set to come on. The Steam Machine itself is within normal operating temperature for the CPU/GPU, which they confirmed from your screenshots. For your awareness, the Steam machine will start throttling performance at 100C for CPU/GPU and will shut down to protect itself if temperatures rise past that.”

Importantly, this premature red warning light is just a temporary wrinkle that will be fixed soon via a BIOS update, adds Steam / Valve. After the update, red light warnings will only be seen after hitting a threshold of “100/100C for CPU/GPU instead of 95/90 for CPU/GPU that is currently happening,” concluded the official support message.

The nearest desktop alternative to the Steam Machine’s CPU, something like the Ryzen 5 7500F, has a TDP of 65W and a max operating temperature of 95°C. However, Valve uses a custom mobile-tuned 30W CPU, which is configured to throttle at 100°C and self-protect shutdown if temperatures continue to rise, hitting 105°C.

We don’t have a set date for the arrival of the new Steam Machine BIOS, but “soon” should be good enough for most users.

The Steam Machine’s light bar has previously been in media focus, being central to stories about the device suffering from a ‘Red Line of Death’ (RLOD). Happily, the pronouncement of death in that case was also premature. RLOD Steam Machines can be reanimated Lazarus-like by following a simple and officially described CMOS reset procedure (read more via the above link).

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Mark Tyson](https://cdn.mos.cms.futurecdn.net/56vqMYLDaKRHPhHZgbADFR.jpg)

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.

- 
Reply
 Many BIOS updates are applied by Windows Update on prebuilt machines. During the 13th/14th Gen fiasco my Dell G15 was getting BIOS updates every few weeks for awhile with no input from me. It's actually nearly impossible to screw it up these days. On my Steam Deck I've had several firmware updates, it's a nothing burger to the average user who probably won't notice anything but the warning to not power down the system during this update. It may even do it while in standby, as consoles often do.hotaru251 said:bios update? assuming people know how to do that & someone will likely brick it.
