---
title: If you've ever been freaked out by your AMD PC doing 'memory training' this
  update could be for you
source_url: https://www.pcgamer.com/hardware/motherboards/new-asus-beta-bios-patches-now-include-a-fresh-amd-feature-to-stop-you-thinking-your-pcs-b0rked/
source_site: PC Gamer
source_slug: pcgamer
description: The new memory training counter shows your PC hasn't just hung on boot.
image: https://cdn.mos.cms.futurecdn.net/ero6FCfQU2gxtBLS7u66So-2560-80.jpg
published: '2026-11-16T00:00:00Z'
scraped_at: '2026-11-16T19:32:40Z'
categories:
- Technology & Software
people: []
locations: []
organisations:
- AGESA
- AMD
- Asus ROG Strix B550-E Gaming5
- GPU
- Hardware
- Intel Core
- MSI MAG
- PC Gamer Circuit Breaker
- Tomahawk WiFi2
- Uniko
---

![Asus ROG Crosshair X870E Hero motherboard running inside a PC](https://cdn.mos.cms.futurecdn.net/ero6FCfQU2gxtBLS7u66So-1920-80.jpg)

Memory training is boring stuff. Your PC will spend an age running through it when you first boot your PC, or you swap in some new RAM sticks (lucky you), or you make a change which has *anything* to do with memory in your BIOS. Or just because your PC decides it might fancy doing it again. But a new AGESA 1.3.0.1F beta BIOS update, first from Asus (via Uniko's Hardware), has made this whole process a lot more exciting.

Well, going from not at all exciting to *something* is always going to feel like a bigger deal, but I don't necessarily want to oversell it. Though when you're waiting for memory training to complete it's real nice to at least have a readout to indicate that it is progressing and your PC hasn't just hung.

This is the issue with memory training on PCs in the past. It was pretty damned opaque, in that you'd start up your PC and it would do… nothing. The fans would spin up, and the lights would light, but you'd have no readout on your monitor, and the debug screen on your motherboard would just have a static figure. Mine would be stuck on '15' for an age.

Obviously you could just go looking up the error code and it would inform you that your system was just having a good long think about its system memory, but if you didn't know that could be a thing, it can feel like your rig is bricked.

The new AGESA 1.3.0.1F beta patches are out now, first from Asus, but you can bet other motherboard vendors will be following suit soon enough. This latest version of the AGESA BIOS brings with it AMD's new memory training function, which shows on the motherboard's debug screen that the memory training process is, indeed, proceeding. You'll see it tick up, first from 00 to 09, and then it will go through 0a, 0b, 0c, etc. to show that it is working through the memory training and that it isn't stuck.

You're still getting nothing on your monitor screen, however. The memory training function is done well before your system gets around to turning on your rig's GPU.

My Asus Crosshair X870E Hero board, with 64 GB DDR5-6000, and a Ryzen 9 9950X, went all the way up to 11 (cue guitar riff) before the training was complete and the motherboard rebooted happily.

The PC Gamer Circuit Breaker newsletter breaks down the latest PC gaming tech, and finds you the best deals on the best products

This means you'll immediately see if it *is* stuck, so no more waiting around for 15 minutes to actually go, 'okay, yeah, this is screwed right here'.

As we've hit the Dave Notes section of this piece, memory training is where your system takes some time to figure out what the best timings and power settings it needs to use in order to get your RAM to run at its preferred speed. This is a periodic thing, and not something that will take place all that often, but when it does, it's slooooooooow.

Your rig will run through voltage/timings combos and validates them alongside test patterns, and then saves its 'best' profile so should be able to always boot reliably at your memory's rated speed. So, on AMD motherboards this is memory training, and why you get a slower than normal boot first time, or when you switch memory. For Intel boards this is called memory refurbishment and is a bit more invisible where it's done in the background.

This latest update is then a pretty small thing for AMD users only, and minor news in the wider world of a reeling tech industry and a market where doing anything to the memory in your rig is almost wishful thinking today, but as a wee quality of life upgrade, and as an AMD CPU user, I'm certainly here for it.

But it's worth noting these are beta BIOS updates, and that comes with some risks that you probably don't need to take in order to get this extra feature. My current official BIOS is AGESA 1.3.0.1d, but I've tested out the new 1.3.0.1f Patch A BIOS from this ROG Forum link. If your rig's running just fine right now, I'd probably suggest sticking with the latest non-beta patches.

![MSI MAG X870 Tomahawk WiFi motherboard](https://cdn.mos.cms.futurecdn.net/tzTtMVDrtbdm9XcVyGxGwi-140-80.jpg)

**1. Best AM5 - AMD Ryzen 9000/7000:MSI MAG X870 Tomahawk WiFi2. Best budget AM5 - AMD Ryzen 9000/7000:Asus TUF Gaming B650-Plus WiFi3. Best midrange AM5 - AMD Ryzen 9000/7000:ASRock B850 Steel Legend WiFi4. Best AM4 - AMD Ryzen 5000/3000:Asus ROG Strix B550-E Gaming5. Best LGA1851 - Intel Core Ultra 200S:Asus ROG Maximus Z890 Hero6. Best budget LGA1851 - Intel Core Ultra 200SASRock B860 Steel Legend Wi-Fi7. Best LGA1700 - Intel 14/13th Gen:MSI MAG Z790 Tomahawk WiFi8. Best budget LGA1700 - Intel 14/13th Gen:Asrock B760M PG Sonic WiFi**
