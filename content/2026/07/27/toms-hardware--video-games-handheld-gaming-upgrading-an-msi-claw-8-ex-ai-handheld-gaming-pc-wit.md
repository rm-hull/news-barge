---
title: Upgrading an MSI Claw 8 EX AI+ handheld gaming PC with a 2TB SSD
source_url: https://www.tomshardware.com/video-games/handheld-gaming/upgrading-an-msi-claw-8-ex-ai-handheld-gaming-pc-with-a-2tb-ssd
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-27T17:52:00Z'
published: '2026-07-27T00:00:00Z'
description: If you do a lot of gaming, 1TB might not be enough default storage.
image: https://cdn.mos.cms.futurecdn.net/HNBbAZbSXofE9YqgubFfLg-1280-80.jpg
---

![MSI Claw 8 EX AI+](https://cdn.mos.cms.futurecdn.net/HNBbAZbSXofE9YqgubFfLg.jpg) 

I recently tested the __MSI Claw 8 EX AI+__ handheld gaming PC, and came away incredibly impressed with its performance. Put simply, it has no rival in gaming performance, easily eclipsing all other handhelds on the market. Even better, the battery life is also stellar.

However, if there’s one thing that it could use, it’s a storage boost. Despite the $1,800 price tag as tested for our review unit, it still only includes a 1TB SSD. After installing a handful of games from Steam and from the Xbox Store, I was left with 128GB free of the 953GB available on the SSD.

I happen to have a __2TB PNY CS2150 PCIe 5.0 SSD__ that I used for testing a Thunderbolt 5 SSD enclosure with __Thunderbolt 5 docks__. Since it was currently sitting unused, I decided to take a stab at replacing the 1TB SSD in the Claw 8 EX AI+ with the CS2150 for some extra storage headroom.

## Getting the hardware setup for the transition

Fortunately for me, much of the legwork had already been finished. The CS2150 was already installed inside an Orico SSD Thunderbolt 5 enclosure, which would serve as my destination drive.

Although I could complete the entire transfer process using only the input methods on the Claw 8 EX AI+, it’s rather tedious to navigate the Windows 11 user interface and enter text on the 8-inch screen. So, I decided to use a Thunderbolt 5 dock to streamline the process. I used:

- OWC Thunderbolt 5 Dock
- Logitech wireless keyboard and mouse
- Orico SSD Thunderbolt 5 enclosure with 2TB PNY CS2150 SSD installed

![MSI Claw 8 EX AI+](https://cdn.mos.cms.futurecdn.net/CMipPAPrycouYiCSYQGy7B-1200-80.png) 

![MSI Claw 8 EX AI+](https://cdn.mos.cms.futurecdn.net/L5ipD6gwpQ3AGGoXfQvWmB-1200-80.jpg) 

![MSI Claw 8 EX AI+](https://cdn.mos.cms.futurecdn.net/CMipPAPrycouYiCSYQGy7B-1280-80.png) 

![MSI Claw 8 EX AI+](https://cdn.mos.cms.futurecdn.net/L5ipD6gwpQ3AGGoXfQvWmB-1280-80.jpg) 

I connected the Thunderbolt 5 dock to one of the two Thunderbolt 4 ports at the top edge of the Claw 8 EX AI+. I then plugged the Logitech USB-A receiver into the dock. Finally, I connected the Orico enclosure to the second Thunderbolt 4 port on the Claw 8 EX AI+.

## Finding the proper software for cloning the drive

It’s been a while since I last cloned a drive, so I did a quick Google search for free drive-copy software for Windows 11. My search led me to a Reddit thread where the majority of commenters recommended the freeware version of Macrium Reflect 8.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

I downloaded the software and installed it without issue. The interface in Reflect 8 was about as straightforward as you can expect, with my source C: drive showing up at the top. The destination field was empty, so I had to select the drive I wanted to use. I pulled up the CS2150, which I have named as Orico in Windows 11 as the D: drive.

![MSI Claw 8 EX AI+](https://cdn.mos.cms.futurecdn.net/ZTTr9XSNzQUPZffTsbj8jA-1200-80.png) 

![MSI Claw 8 EX AI+](https://cdn.mos.cms.futurecdn.net/mDS6D8joMGiQrxD5pc399B-1200-80.png) 

![MSI Claw 8 EX AI+](https://cdn.mos.cms.futurecdn.net/eYhJgZZqKd7qmyxYcXwN9B-1200-80.png) 

![MSI Claw 8 EX AI+](https://cdn.mos.cms.futurecdn.net/GbAKsJ7UZKTsbYZpXH5tPB-1200-80.png) 

![MSI Claw 8 EX AI+](https://cdn.mos.cms.futurecdn.net/kTvGazXBuKSHxyzpdfjGLB-1200-80.png) 

![MSI Claw 8 EX AI+](https://cdn.mos.cms.futurecdn.net/ZTTr9XSNzQUPZffTsbj8jA-1280-80.png) 

![MSI Claw 8 EX AI+](https://cdn.mos.cms.futurecdn.net/mDS6D8joMGiQrxD5pc399B-1280-80.png) 

![MSI Claw 8 EX AI+](https://cdn.mos.cms.futurecdn.net/eYhJgZZqKd7qmyxYcXwN9B-1280-80.png) 

![MSI Claw 8 EX AI+](https://cdn.mos.cms.futurecdn.net/GbAKsJ7UZKTsbYZpXH5tPB-1280-80.png) 

![MSI Claw 8 EX AI+](https://cdn.mos.cms.futurecdn.net/kTvGazXBuKSHxyzpdfjGLB-1280-80.png) 

After clicking Next, I was prompted with a warning about BitLocker encryption, so I clicked OK to acknowledge it (you’ll definitely want to re-enable BitLocker once you reinstall the SSD). The next screen showed a summary of the operations to be performed: copying the EFI and Windows partitions to the 2TB SSD. I clicked Finish, which brought up another prompt asking if I wanted to run the backup. I clicked OK, which displayed a warning that the D: drive would be overwritten. After clicking Continue, the process started.

After about an hour and a half, the cloning process was completed. At this point, I shut down the Claw 8 EX AI+ and disconnected all of the accessories.

## Disassembling the MSI Claw 8 EX AI+ and installing the 2TB SSD

Next, I removed the back panel of the Claw 8 EX AI+, which required removing six screws and using a plastic prying tool. I then removed the single screw holding the already-installed 1TB SSD in the M.2 slot and extracted it. I next removed the 2TB SSD from the Orico enclosure and installed it in the M.2 slot, securing it with the screw I had just removed.

![MSI Claw 8 EX AI+](https://cdn.mos.cms.futurecdn.net/rV7eBknwChsm56KFvw7tfB-1200-80.jpg) 

![MSI Claw 8 EX AI+](https://cdn.mos.cms.futurecdn.net/3RJ69qkZvie329soXAFtkB-1200-80.jpg) 

![MSI Claw 8 EX AI+](https://cdn.mos.cms.futurecdn.net/EAQDVQGy222v4TUBgQWFfB-1200-80.jpg) 

![MSI Claw 8 EX AI+](https://cdn.mos.cms.futurecdn.net/2kProTqnsou6EwCsBU6iiB-1200-80.jpg) 

![MSI Claw 8 EX AI+](https://cdn.mos.cms.futurecdn.net/rV7eBknwChsm56KFvw7tfB-1280-80.jpg) 

![MSI Claw 8 EX AI+](https://cdn.mos.cms.futurecdn.net/3RJ69qkZvie329soXAFtkB-1280-80.jpg) 

![MSI Claw 8 EX AI+](https://cdn.mos.cms.futurecdn.net/EAQDVQGy222v4TUBgQWFfB-1280-80.jpg) 

![MSI Claw 8 EX AI+](https://cdn.mos.cms.futurecdn.net/2kProTqnsou6EwCsBU6iiB-1280-80.jpg) 

I then reinstalled the back panel for the Claw 8 EX AI+ and secured it with the previously removed screws.

## Booting up and checking my work

I powered the Claw 8 EX AI+ back on, and it booted without issue. I was also surprised to see that Windows 11 didn’t throw up any activation errors. I’ll chalk that up as a win. I went to Windows Explorer to see if I was indeed utilizing the full 2TB of storage, but I instead saw that 128GB was free of 953GB – the same predicament as before.

 ![MSI Claw 8 EX AI+](https://cdn.mos.cms.futurecdn.net/CMipPAPrycouYiCSYQGy7B.png) 


I might have missed a setting during the cloning process that would have expanded the partition to use all free space on the larger SSD. But the fix was simple enough. I opened up the Disk Management utility, selected Windows (C:), and chose “Extend Volume.” After that process was complete, I saw the full 2TB (actually, 1.81TB), with 1.02TB now free for additional game installs.

![Brandon Hill](https://cdn.mos.cms.futurecdn.net/yHeufe7JcvuJBhYPkSexNf.jpg)

Brandon Hill is a senior editor at Tom's Hardware. He has written about PC and Mac tech since the late 1990s with bylines at AnandTech, DailyTech, and Hot Hardware. When he is not consuming copious amounts of tech news, he can be found enjoying the NC mountains or the beach with his wife and two sons.
