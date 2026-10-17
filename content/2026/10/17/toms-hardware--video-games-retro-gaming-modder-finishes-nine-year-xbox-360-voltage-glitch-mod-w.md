---
title: Modder finishes nine-year Xbox 360 voltage glitch mod with a $4 microcontroller,
  cracks the console open — tiny microcontroller dumps NAND and flashes timing files
  to bypass CPU cryptography
source_url: https://www.tomshardware.com/video-games/retro-gaming/modder-finishes-nine-year-xbox-360-voltage-glitch-mod-with-a-usd4-microcontroller-cracks-the-console-open-tiny-microcontroller-dumps-nand-and-flashes-timing-files-to-bypass-cpu-cryptography
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-17T20:33:26Z'
published: '2026-10-17T00:00:00Z'
description: Back in my day, it took substantial dedicated hardware to pull off these
  shenanigans.
image: https://cdn.mos.cms.futurecdn.net/8DAK5ZNFPis5MqQgWD9BZo-2560-80.png
categories:
- Technology & Software
- Hardware
people:
- Bruno Ferreira
- Joshua Kennedy
- Pegaroo
- Tom
locations:
- PicoFlasher
organisations:
- CPU
- Google News
- Microsoft
- NAND
- Octal450
- PC
- PS3
- Pi Pico
- Tom's Hardware
- XeLL
---

![Xbox 360](https://cdn.mos.cms.futurecdn.net/8DAK5ZNFPis5MqQgWD9BZo-1920-80.png)

The Xbox 360 has been cracked open multiple times over the years, and almost every time Microsoft's updates plugged whichever hole let hackers through. The first method was modded DVD firmware in 2006, a hypervisor hack followed in 2007, and a wiring hack exposing JTAG debugging ports was revealed in 2009. The longest-lasting physical hack was 2011's CPU force-reset exploit. That maneuver needed specialized hardware along with a voltage-glitching chip, but an enterprising techie showed how it can be performed nowadays with the assistance of a Raspberry Pi Pico, costing all of $4 (or about 5€ / £5). The crack marks the culmination of a nine-year effort by the modder.

To get the elephant out of the room, yes, just last week the PeerPressure Xbox 360 persistent soft-mod was released. But we're here to talk signals and wires. The aforementioned reset exploit involves sending a teeny weeny tiny signal directly into the CPU's reset pin. You'd think this would do what it says on the label, but what happens instead is that the CPU executes the current instruction *incorrectly*.

Naturally, someone figured out how to leverage that to run any code on the CPU, thus completely bypassing Microsoft's impressive and frankly rather effective layers of cryptography within the console. Sending said signal for an effective hack, though, requires spectacularly precise timing with a resolution down to nanoseconds, and glitch-chips may even require several attempts to get a successful "latch."

Joshua Kennedy, a Scottish hacker, bought a Matrix Coolrunner Rev D modchip board back in 2017 to hack his console this way, but it required soldering wires, NAND, and programmers, and patience. He once tried rolling his own programmers using an old PC's parallel port (a common substitute), but never got the project off the ground and shelved the idea.

Fast-forward to 2026, and a new tool presented itself: the highly successful Raspberry Pi Pico, a highly capable microcontroller-on-a-stick, whose price starts at all of $4. Armed with this, he started the procedure. He connected the Pi Pico to the NAND interface header on the console to be able to dump the console's NAND flash firmware — a task easily accomplished with just some wiring and the PicoFlasher utility. Although the post doesn't mention it, Kennedy likely took the NAND data, patched it with XeLL, and reuploaded it.

He moved on to download Octal450's Timing Files, a set of mini-programs triggering the glitch chip at the best possible timing to try and reset the CPU. These are necessary because the window of opportunity is different across every hardware revision of the Xbox 360. Enlisting the Pi Pico once again, he uploaded the timing files to the Matrix Coolrunner, and presumably ran the rest of the hack process. And thus the task was complete, and "a project that defeated [Kennedy] in 2017 was made trivial in 2026 by a £5 microcontroller."



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G-140-80.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.

* Nine years of sticking with a voltage glitch — that's some serious dedication. Honestly love that it's a $4 microcontroller doing the heavy lifting; this scene really never dies.  
    
  Fair point from Pegaroo, but I don't mind the hard mods still having a place. The software exploits are convenient, but hardware-level work like this is what keeps these old machines documented and repairable long-term. Tempted to dig my old 360 out of the closet now. Reply
* GTAVispot said:Nine years of sticking with a voltage glitch — that's some serious dedication. Honestly love that it's a $4 microcontroller doing the heavy lifting; this scene really never dies.  
    
  Fair point from Pegaroo, but I don't mind the hard mods still having a place. The software exploits are convenient, but hardware-level work like this is what keeps these old machines documented and repairable long-term. Tempted to dig my old 360 out of the closet now.Heck im tempted to go to my dad’s house and check in my okd closet and see if i can find my old 360. Hopefully its still there. I know my PS3 is still connected to an old plasma TV. Hell if the TV was bigger i would take it too. Plasma had better color, contradt and motion clarity than even OLED as long as you’re within the correct viewing angle. Reply
