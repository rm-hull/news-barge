---
title: Hardware hacker builds open-source portable 3.5-inch floppy Wi-Fi NAS — reads
  and shares old-school floppies wirelessly or through direct connection
source_url: https://www.tomshardware.com/uk/maker-stem/hardware-hacker-builds-open-source-portable-3-5-inch-floppy-wi-fi-nas-reads-and-shares-old-school-floppies-wirelessly-or-through-direct-connection
source_site: Tom's Hardware
source_slug: toms-hardware
description: Techie designs a portable Wi-Fi NAS to read and transfer digital camera
  floppy disks — device does double duty for easy floppy archival
image: https://cdn.mos.cms.futurecdn.net/x7enQpZKnd28dxA8WZdmXZ-2048-80.png
published: '2026-11-21T00:00:00Z'
scraped_at: '2026-11-21T19:08:16Z'
categories:
- Technology & Software
- Hardware
people:
- Bruno Ferreira
- Tom
locations:
- ESP32-S3
organisations:
- BigCrimping
- Crimp
- DISP
- Google News
- Greaseweazle
- PC
- PCB
- POWER
- Panasonic PV-SD
- Sony Mavica
- Tom's Hardware
---

![floppy3.5](https://cdn.mos.cms.futurecdn.net/x7enQpZKnd28dxA8WZdmXZ-1920-80.png)

Hardware hacker BigCrimping (Crimp) has made a dedicated portable Wi-Fi NAS that allows for easily reading and copying 3.5" floppy disks over a network. The renaissance of vintage hardware also extends to some early digital cameras, like the Sony Mavica and Panasonic PV-SD families. These point-and-shooters were popular due to using bog-standard 3.5" floppies in PC format. Many folks may still have floppies from this era around, or simply want to breathe new life into their cameras.

The new device is called floppy3.5, and its design is completely open-source. Making one ought to be pretty easy, as Crimp made all the required files available on GitHub, including data for 3D printing the enclosure, and a custom PCB with an RP2354A microcontroller and an ESP32-S3 bridge. Besides those items, you'll need predictable necessities like a battery, a slimline floppy drive, a Wi-Fi module, and a microSD slot.

![Copy That Floppy: A Portable 3.5](https://img.youtube.com/vi/wcR_Jo1fEtY/maxresdefault.jpg)

The onboard monochrome LCD display looks pretty handy, as Crimp made it show a bevy of information, including sector and cylinder counts, a good/bad sector map, file counts, and even a firmware update progress counter. The onboard buttons do what they say: READ to scan the files, or SAVE to dump them to an SD card. The DISP and POWER buttons return you to the home screen, and power the device off and on.

The card in said slot optionally stores the disk's files, allowing you to easily go around a storeroom or attic and just insert floppies one after another for archival without needing a computer. When it's time to manage content, you can access the floppy3.5's web interface over the network, and even connect to it directly with a USB cable if you need fancier features like fetching entire disk images.

Crimp chose to use the Greaseweazle floppy drive comms protocol instead of relying on a conventional floppy drive controller. Besides saving on hardware, this allows full control over the drive, as Greaseweazle manages a drive's wire signals directly, making for easy imaging and all sorts of direct data manipulation, regardless of a disk's underlying format. By default, floppy3.5 understands FAT12 for its main purpose, but you can use the Greaseweazle utilities over the cable if needed.



*Download the Tom's Hardware app for up-to-the-minute updates on* * iOS* * and* * Android**. Also follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G-140-80.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.
