---
title: Clever hacker fits 537,000 domains in a tiny $5 ESP32 ad-blocking dongle —
  firmware uses only around 50KB of RAM and can answer blocked lookups in 10 milliseconds
source_url: https://www.tomshardware.com/networking/clever-hacker-fits-537-000-domains-in-a-tiny-usd5-esp32-ad-blocking-dongle-firmware-uses-only-around-50kb-of-ram-and-can-answer-blocked-lookups-in-10-milliseconds
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-19T13:46:46Z'
published: '2026-07-19T00:00:00Z'
description: This project uses a clever hashing trick to fit over half a million blocked
  domains into just 4MB of flash memory.
image: https://cdn.mos.cms.futurecdn.net/gGjEqwLsURFSUzVANwnYQZ-1280-80.jpg
---

![A close-up photo of a custom-built USB-and-Wi-Fi adblocker built by an enthusiast.](https://cdn.mos.cms.futurecdn.net/gGjEqwLsURFSUzVANwnYQZ.jpg) 

How cheap can you build a hardware-based ad-blocking DNS filter? "Free," if you're willing to salvage some used hardware that's being thrown away. What if you aren't so lucky? In the era of the RAMageddon, even a Raspberry Pi will cost you a couple hundred bucks. But you know, you don't even need something that powerful. In fact, you can use a $5 microcontroller to build a fully functional ad-blocking filter with over 500,000 domains blocked and around 10ms latency.

We know that's possible because Egyptian full-stack developer ZedAxis (@M-Abozaid on GitHub) has already built one. Using an ESP32-C3 "SuperMini" board, he's created a backup DNS for his home network that still provides ad blocking. His primary router is a Pi-hole, which is a Raspberry Pi running specialized software to manage DHCP addressing and DNS resolution with integrated ad-blocking. The SuperMini serves as a backup when the Pi-Hole is rebooting or otherwise unavailable.

 ![A photo of the tiny ESP32 SuperMini board, bare of any casing.](https://cdn.mos.cms.futurecdn.net/wZBPyRvxidw3AakhCcUWMQ.jpg) 


Strictly speaking, we haven't seen ZedAxis' creation in action, but there's no reason to believe it doesn't work. The ESP32 family of embedded Wi-Fi-enabled microcontrollers is a well-known quantity, and this functionality is by no means outside the realm of its capabilities. In fact, this specific trick allows the use of the ESP32-C3, which is a cost-reduced version of the chip that doesn't have the 8MB of PSRAM found on some higher-end models. (There are MANY variants of the ESP32.)

Instead, the ESP32-C3 used by ZedAxis has just 400KB of RAM, and 4MB of flash memory. With these limited specifications, he wasn't able to store a plaintext blocklist of any real size; it's simply too much data. So, he did what any enterprising hacker would do: he started hashing the data to reduce its size. Using 40-bit FNV-1a hashes, because 32-bit would give too many collisions and 64-bit wastes too much space, he can store some 537,000 domains in the flash memory of the device.

 ![A screenshot of the rudimentary GUI for the C3 AdBlocker.](https://cdn.mos.cms.futurecdn.net/9oneQ7XT6SK5W2NNZgaYxH.jpg) 


The clever part isn't really the hashing, though. Rather than storing the domains themselves, the build process downloads one or more public blocklists, strips out duplicate entries and comments, hashes each remaining domain into a 40-bit value, sorts the resulting list, and writes the finished database into the ESP32's flash memory. When a DNS query arrives, the device hashes the requested hostname the same way and performs a binary search against the sorted hash table. If it finds a match, the request is blocked. Otherwise, the query is forwarded to an upstream resolver. According to ZedAxis, the finished firmware uses only around 50KB of RAM while answering blocked lookups in roughly 10 milliseconds.

![I built a $2 ad-blocker for my whole network - YouTube](https://img.youtube.com/vi/RaxszOUMi8E/maxresdefault.jpg) 

There's another neat compromise hiding in the design, too. The ESP32 normally reserves enough flash memory to hold two complete copies of its firmware, allowing over-the-air (OTA) updates without risking a failed flash leaving the device unbootable. If you don't care about wireless firmware updates, you can reclaim that second firmware partition for the blocklist database instead. With OTA support enabled, the project tops out at around 250,000 blocked domains. Give up OTA, and that jumps to roughly 537,000 domains on a microcontroller that you can usually buy for the price of a fast-food lunch. ZedAxis describes the price as $2; I wasn't able to find SuperMini boards any cheaper than about $5 US, but at that price there's not much need to quibble about the difference.

Of course, this isn't meant to replace a proper Pi-hole or AdGuard Home installation. The ESP32 project has a rudimentary dashboard, but it doesn't provide detailed per-client statistics, historical query logs, or all the knobs and dials that make those platforms attractive. Instead, it's designed as a tiny insurance policy. It sits quietly on the network, sips only a few dozen milliamps of power, and if the primary DNS server disappears for a reboot or a power outage, clients still get filtered DNS responses instead of falling back to whatever resolver the router happens to have configured.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

 ![A photo of a tiny ad-blocking device plugged into a home fiber gateway device.](https://cdn.mos.cms.futurecdn.net/pvJ6dFN3Ut8fY9yLJVJdQ8.jpg) 


My favorite detail is that ZedAxis powers the whole thing from the USB port on the back of his ISP-provided fiber gateway, a Huawei OptiXstar home fiber gateway. The USB connection isn't carrying any data; the totality of the integration is the router saying "here's 5 volts" and the ESP32 replying "thanks." It's just that the port is a convenient power source for a device so small it practically disappears behind the router. All communications are carried out through the ESP32's integrated Wi-Fi adapter.

I have no idea whether projects like this will ever become common. Probably not, because most people who want network-wide ad blocking will still buy a Raspberry Pi, a used mini PC, or run AdGuard Home in a virtual machine. Still, it's refreshing to see somebody look at a $5 microcontroller with 400KB of RAM and decide, "Sure, that'll do."

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Zak Killian](https://cdn.mos.cms.futurecdn.net/yonJziSpjzVFahKcUonJvi.jpg)

Zak is a freelance contributor to Tom's Hardware with decades of PC benchmarking experience who has also written for HotHardware and The Tech Report. A modern-day Renaissance man, he may not be an expert on anything, but he knows just a little about nearly everything.

- 
Reply
 An ever increasing number of people can get cheap access to a 3D printer through libraries (since nobody reads anymore) or makerspaces.wakuwaku said:no matter how cheap a project is purported to be , as long as it requires you to either own a 3d printer, or get someone to print it for you,**IT IS NOT CHEAP**.
- 
Reply
 I print LOTS of things for friends and coworkers for $0.wakuwaku said:no matter how cheap a project is purported to be , as long as it requires you to either own a 3d printer, or get someone to print it for you,**IT IS NOT CHEAP**.
