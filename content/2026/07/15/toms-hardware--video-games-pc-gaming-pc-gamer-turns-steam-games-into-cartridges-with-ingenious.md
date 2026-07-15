---
title: PC gamer turns Steam games into cartridges with ingenious 2.5-inch SSD system
  — games are stored on 128GB drives alongside a script to auto-start the title once
  plugged in
source_url: https://www.tomshardware.com/video-games/pc-gaming/pc-gamer-turns-steam-games-into-cartridges-with-ingenious-2-5-inch-ssd-system-games-are-stored-on-128gb-drives-alongside-a-script-to-auto-start-the-title-once-plugged-in
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-15T14:05:17Z'
published: '2026-07-15T00:00:00Z'
description: Video shows Steam Game Cartridge system in action.
image: https://cdn.mos.cms.futurecdn.net/JTDUMcuDBav3BEspNBMw6A-1920-80.jpg
---

![Steam Cartridge Games system](https://cdn.mos.cms.futurecdn.net/JTDUMcuDBav3BEspNBMw6A.jpg) 

A PC gamer has created and demonstrated a handy Steam Game Cartridge system. Over on PCMR, Jibril-sama introduced the system, which blends the old-school console convenience of cartridges with Steam’s awesome and agreeably flexible games library. Ingeniously, it upcycles a bundle of old SATA SSDs into Steam-ready game cartridges using a disk mount detect and execute script on the software side and a SATA dock on the hardware side. Icing on this already tasty cake is provided by Jibril-sama’s colorfully encased and custom-labeled Steam Game Cartridges. Nice.

“Got a couple of used 2.5" SSDs for cheap so I decided to make a Game Cartridge system,” the Redditor casually informs the PCMR masses in the post embedded above. “Games are actually on those SSDs with a script to auto-navigate Steam to the game's page. Auto-starting the game right away is also possible.”

Further comments by the OP explain that all the drives bought for this project were 128GB in capacity, and €7 a piece ($8). That’s not bad in the current RAM and NAND crunch, and keeps these files off your built-in primary storage. As many readers will know, PC game libraries can easily grow to hog a lot of storage.

We reached out to Jibril-sama for some more background info about how the Steam Game Cartridge system is designed to work with as little user friction as possible. They informed us that the system in the video runs Linux and Valve’s Steam URL Protocol is leveraged to navigate to the game's page or launch the game.

“All it needs is a systemd template to check for a script on the SSD and launch it. And a udev rule to trigger the system,” Jibril-sama told *Tom’s Hardware*. “So basically: Plug in SSD -> udev rule sees the event -> triggers the systemd daemon -> systemd daemon looks into the SSD and finds the script -> execute the script.”

![Steam Cartridge Games system](https://cdn.mos.cms.futurecdn.net/tkHhbhBEiGR9YcezgDaw6A.jpg)

![Steam Cartridge Games system](https://cdn.mos.cms.futurecdn.net/dx6HoGhGFgAip8mrscvB7A.jpg)

![Steam Cartridge Games system](https://cdn.mos.cms.futurecdn.net/tVuYmNgSgmXmEHoJgrGVt9.jpg)

![Steam Cartridge Games system](https://cdn.mos.cms.futurecdn.net/JTDUMcuDBav3BEspNBMw6A.jpg)

Commenters on PCMR have overwhelmingly welcomed the Steam Game Cartridge future teased by this system. Some want to see the system extended to include GOG game libraries. Others query how the system handles the inevitable hefty multi-gigabyte updates that are pushed (even to older games) from time to time. Jibril-sama told *Tom’s Hardware* that they didn’t plan to deal with updates often, as they didn’t use cartridges for ‘live service’ titles, and they are mostly used for the “games that I want to replay once in a while.” If and when updates have been flagged, “I just let Steam handle the updates and wait a bit before I can play,” they added.

I’ve had repeated firsthand experience with Steam Games libraries being fussy when moving across different PCs, so stretching the library system this way could reveal cracks and wrinkles as more games are tested. We shall see.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Hopefully, fuller implementation guides, scripts, and resources to help others purchase or 3D print their own Steam Game Cartridge shells will be shared in due course.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Mark Tyson](https://cdn.mos.cms.futurecdn.net/56vqMYLDaKRHPhHZgbADFR.jpg)

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.

- 
We could do this with SD cards, ideally the full-size ones which are becoming less common now. I've got an OEM PC with a blocked off slot where an SD card would go.Reply
 
 These SATA ones are cute, easy to slap a big label on, and may have better longevity than SD cards. After 2.5" SATA drive supply dries up, you could continue it by using SATA shells with an M.2 drive inside. That's two components and likely more expensive than used 2.5" drives though.
- 
Sure if you get a bunch of ssds for $8 each you can do that, not so much if you have to pay normal price.Reply
 
 Since they are using steamos anyway they could just put the whole os on the ssd as well, it's like 10-15gb, set up any special things the game might need and so on, custom wallpaper, os theme what have you.
 
 That's what I did to incorporate win9x games into my emulator frontend, just have the os with the drivers and the game installed in one image and just boot the image with an autoexec starting the game.
- 
Reply
 That's what play-in-browser abandonware sites use. For example, for at least one game I tested, classicreload.com is downloading the CD-sized game into your memory each time you load the page, and running Windows 3.11 in DosBox. Then you click on the executable and go instead of autoexec.TerryLaze said:That's what I did to incorporate win9x games into my emulator frontend, just have the os with the drivers and the game installed in one image and just boot the image with an autoexec starting the game.
- 
First of all, you could also do this with USB sticks (type 3) but what your all missing is he's broken copyright law, your not allowed to copy or reproduce or repackage or redistribute games. If he was to sell a single one of those, he'll be looking at prison time. It's like buying a CD, copying it to your laptop so you have the MP3 versions then returning it to the shop. It's illegal.Reply
