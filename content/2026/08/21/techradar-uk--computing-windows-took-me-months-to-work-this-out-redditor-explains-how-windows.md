---
title: Has the GPU driver gone missing on your gaming laptop? Windows 11 can reportedly
  remove it by accident — here's how to avoid that
source_url: https://www.techradar.com/computing/windows/took-me-months-to-work-this-out-redditor-explains-how-windows-11-can-end-up-stripping-out-the-gpu-driver-on-your-gaming-laptop
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-22T01:47:47Z'
published: '2026-08-21T00:00:00Z'
description: Windows 11 removed the driver for an Nvidia RTX 5070 Ti graphics card,
  and you can blame Eco mode.
image: https://cdn.mos.cms.futurecdn.net/nZ9MtUnriwdKNUAo7Dv4qM-1280-80.png
---

![Cyberpunk 2077 on ROG Zephyrus G14 laptop](https://cdn.mos.cms.futurecdn.net/nZ9MtUnriwdKNUAo7Dv4qM.png) 

- **Windows 11 can remove a discrete GPU driver as part of its clean-up routines, as shown on Reddit**
- **This can happen if the laptop has been in Eco mode for an extended period**
- **Because the GPU is effectively gated off from the system, the driver is marked as unused and therefore deleted by the OS during clean-up – but you can stop this from happening**

Apparently, Windows 11 can end up stripping away the discrete GPU driver from your laptop in certain scenarios if the OS is left to run in Eco mode for a long time – and that's a distinct annoyance if you own a gaming laptop, as per a report on Reddit.

Wccftech spotted a Redditor who posted about their Asus ROG Zephyrus G14 gaming laptop with a discrete Nvidia RTX 5070 Ti, and how Windows turned off that GPU.

At this point, some of you may immediately be thinking: who runs their gaming laptop in Eco mode? And that's a fair point, and one raised in the Reddit thread – I'll come back to that.

First, let's look at the mechanics of how this works, based on the Redditor's investigation of what went on (they noted that it "took me months to work this out"). When the laptop is put into Eco mode, power is completely cut to the discrete GPU, effectively leaving it offline (just as if it were an unplugged USB stick, as the Redditor describes).

That's not a problem – obviously it's a power-saving measure – but the issue is that Windows 11 runs a driver clean-up process from time to time as part of routine system maintenance. By default, this happens every 30 days, though the Redditor notes their laptop was set to 15 days, and this can be modified.

What happens is that if the laptop has been in Eco mode for a long time, with the GPU effectively walled off and not present as far as the system is concerned, and the clean-up happens, it judges the driver to now be superfluous, and it's removed.

When Eco mode is subsequently switched off, the driver doesn't return – it remains ditched, and the GPU shows as a 'Microsoft Basic Display Adapter' instead of an Nvidia GPU in Windows 11's Device Manager.

Sign up for breaking news, reviews, opinion, top tech deals, and more.

The Nvidia graphics driver must then be reinstalled to get the GeForce graphics card functional again – and the same is reportedly true of AMD discrete GPUs.

## Analysis: a niche problem, but an annoying one – here's how to avoid it

 ![Close-up of keyboard and touchpad on Asus ROG Zephyrus G14 (2025)](https://cdn.mos.cms.futurecdn.net/k2vzUGq3RpjXbvcSFykv8.jpg) 


Let's return to that question: who runs a gaming laptop in Eco mode? No gamer really does this, at least not when they're regularly playing some of the top PC games on their notebook. However, someone might be a student cramming for finals and using the laptop for work, having given up gaming distractions for a few months. In this case, with Eco mode enabled to keep battery life up while studying, Windows 11 could disable the GPU.

Okay, so it's something of a niche situation – and the Windows 11 clean-up routines are useful for keeping the system streamlined. But it's not an unthinkable scenario, and Microsoft's OS should be tuned to be more careful around GPU drivers – and it'd be useful if the system could give a warning of such a clean-up happening (so it could be avoided).

That said, this may not happen in all situations. Another Redditor notes that they have had their Zephyrus G16 in Eco mode for two months, and the Nvidia RTX 5070 Ti is still present and correct.

Whatever the case, if you run into this problem yourself, at least you know why it's happening. The fix is to simply reinstall the Nvidia driver, although the same thing could happen again if you're one of those people who regularly uses Eco mode on your gaming laptop.

You can apply a Registry fix to permanently stop the clean-up process, but I wouldn't recommend messing with those settings unless you're confident (see the Reddit post for instructions). Also note that you'll miss out on other clean-up duties, not just GPU-related activity.

A better solution is to simply remember to take your laptop out of Eco mode now and then (every couple of weeks), which will bring the discrete GPU back into play, and save the driver from being earmarked for removal.

The Redditor notes: "Or just keep the GPU visible now and then. Optimized mode in G-Helper turns the dGPU [discrete GPU] on whenever you plug in. Flipping to Standard [mode] every couple of weeks does the same thing. Resets the counter, no Registry editing."

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
