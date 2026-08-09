---
title: Open-source stealth USB hides an encrypted partition behind an 8GB decoy drive
  — 'Phantom Drive' appears as a regular USB stick until you create a text file to
  unlock the hidden data
source_url: https://www.tomshardware.com/pc-components/usb-flash-drives/open-source-stealth-usb-hides-an-encrypted-partition-behind-an-8gb-decoy-drive-phantom-drive-appears-as-a-regular-usb-stick-until-you-create-a-text-file-to-unlock-the-hidden-data
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-09T13:11:59Z'
published: '2026-08-09T00:00:00Z'
description: A trick to break the walls of hidden partitions.
image: https://cdn.mos.cms.futurecdn.net/mwt5veUBP4L72NPirnqPDA-1785-80.jpg
---

![The Phantomdrive](https://cdn.mos.cms.futurecdn.net/mwt5veUBP4L72NPirnqPDA.jpg) 

From the outside, the Phantom Drive, created by Rootkit Labs, appears like a boring old USB. It has that classic, cheap plastic-feeling look to it that would never make you second-guess its intention; when you plug it in, it shows up as just an 8GB drive. However, under the hood, the Phantomdrive is powered by a microSD card that only unlocks itself when you specifically create a new text file, after which it mounts the secret partition, which comes with AES-256 encryption. It's made for situations and places where you might be forced to reveal the contents of a storage device.

![The Open Source USB Drive Built for Privacy - YouTube](https://img.youtube.com/vi/-yI8j4pUuRU/maxresdefault.jpg) 

The Phantomdrive is built using the CH569 microcontroller that has a bunch of different hardware blocks — this project uses the USB3, SD/eMMC, and the AES block. There are no NAND chips directly onboard the custom PCB because of the ongoing component crisis. Instead, the Phantomdrive relies on a simple microSD card (that you provide; it doesn't come with one) for both its 8GB decoy partition and the hidden partition. The creator does say they'll make a version with eMMC modules once prices come down.

Of course, if someone were to open up the drive, they'd be able to physically rip the SD card out. However, it still wouldn't be a dead giveaway since many cheap USBs are powered by microSD cards, and SD card adapters are also a thing. Anyhow, the finished drive looks pretty simple from the inside; it comprises a USB port, two buck supplies, a button for firmware update, the microSD card, UART test points, and some support components. The custom firmware now comes into play.

![The Phantomdrive](https://cdn.mos.cms.futurecdn.net/ycCGWq8C2tCNrHAbHDS5aH-1200-80.jpg) 

![The Phantomdrive](https://cdn.mos.cms.futurecdn.net/w7mnzYQ4AACAF3B7TNMpDQ-1200-80.jpg) 

![The Phantomdrive](https://cdn.mos.cms.futurecdn.net/ycCGWq8C2tCNrHAbHDS5aH-1280-80.jpg) 

![The Phantomdrive](https://cdn.mos.cms.futurecdn.net/w7mnzYQ4AACAF3B7TNMpDQ-1280-80.jpg) 

The name of the game is interception. The firmware doesn't know it's being used to handle file transfers; it just reads raw packets of data being sent over the USB bus as is. It's coded to always look for a "password" string, so as soon as you create the unlock.txt file with "password:xyz" inside, it detects the "xyz" bit and copies it over to SRAM, while overwriting the raw data with a bunch of zeroes before it's written to the SD card. The operating system thinks it's created the new file, but the firmware intercepted it midway and sent essentially nothing to the physical storage cells.

The firmware uses the unique internal hardware ID of the microcontroller as the salt, combines it with the password you just typed, and runs the pair through PBKDF2-HMAC-SHA-256 hashes 100,000 times (you can also select 600,000 times) to create a key. Each run induces an intentional 2-3 second delay to deter brute-force attacks that would try to crack the password. The key is used to unlock and lock the hidden partition, and since it's tied to the silicon itself, putting the SD card into another Phantom Drive will not unlock it.

 ![Unlocking the Phantomdrive's secret partition](https://cdn.mos.cms.futurecdn.net/QLo3cUgcShXEZckvW2ceoj.png) 


Even if you try to access it directly through a microSD card slot, it will stay hidden, and the 8GB decoy will actually appear like a broken partition. The creator has also provided the option to recompile the firmware on your own to spoof specific vendor IDs, so that the USB appears like it's from different brands. You can make the Phantomdrive pretend to be a cheap 16GB Kingston Datatraveler at the hardware protocol level, at which point no scanning software will flag it as anything more than a cheap USB.

There are Linux-based C tools you can use in case of emergency, however, to recover your data, such as physical damage to the board. The transfer speeds are also very limited because the project is built over USB 2 — 20 MB/s reads and 9 MB/s writes in AES-CTR mode. The speeds fall to 10 MB/s reads and 6 MB/s writes in AES-XTS, but at least you have the freedom to choose between the two according to your needs.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

You can buy the Phantomdrive from Rootkit Labs for $50, but you can also build your own, since this is an open-source project. The prebuilt device comes with two extra shells because the pins wear off and break quickly. Otherwise, the GitHub repo provides all the resources, including the PCB layout files and schematics, the BOM for every part, and the custom firmware, alongside its related tools.

The creator of Phantomdrive, Ryan Walker, explains the goal behind the project as both utilitarian and political. It's built using entirely open-source software and with inexpensive, easily accessible components. They wanted to create something that could "slip past authoritarian government representatives, corrupt police, and anyone else that doesn't respect basis encryption rights."

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Hassam Nasir](https://cdn.mos.cms.futurecdn.net/SxxNFHt95eGK37mKPhJpdZ.jpg)

Hassam Nasir is a die-hard hardware enthusiast with years of experience as a tech editor and writer, focusing on detailed CPU comparisons and general hardware news. When he’s not working, you’ll find him bending tubes for his ever-evolving custom water-loop gaming rig or benchmarking the latest CPUs and GPUs just for fun.
