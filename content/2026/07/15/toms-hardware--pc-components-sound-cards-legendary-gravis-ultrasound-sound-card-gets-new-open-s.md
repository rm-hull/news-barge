---
title: Legendary Gravis Ultrasound sound card gets new open-source clone — Beavis
  Ultrasound remake includes complete KiCad schematics, PCB layout, sample ROM, and
  more
source_url: https://www.tomshardware.com/pc-components/sound-cards/legendary-gravis-ultrasound-sound-card-gets-new-open-source-clone-beavis-ultrasound-remake-includes-complete-kicad-schematics-pcb-layout-sample-rom-and-more
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-15T10:11:57Z'
published: '2026-07-15T00:00:00Z'
description: KiCad schematics, PCB layout, sample ROM, and reverse‑engineered GAL
  logic are all provided, but you’ll still need to source an old AMD InterWave chip.
image: https://cdn.mos.cms.futurecdn.net/RHL3sVXa7MPMAuBGnGspWa-1920-80.jpg
---

![Beavis Ultrasound PnP ISA Sound Card Replica](https://cdn.mos.cms.futurecdn.net/RHL3sVXa7MPMAuBGnGspWa.jpg) 

There’s a new remake of the legendary Gravis Ultrasound ISA soundcard on the block with the arrival of the open-source Beavis Ultrasound project. Developer schlae shared details of this amusingly named mid-90s-cultural phenomenon portmanteau, Beavis Ultrasound PnP ISA Sound Card Replica, on GitHub on Monday. The repository includes complete KiCad schematics, PCB layout, sample ROM, reverse‑engineered GAL logic (for an operational IDE CD-ROM interface), assembly notes, and more. You’ll still need to source an old AMD AM78C201 InterWave chip to complete this DIY project, though.

 ![Beavis Ultrasound PnP ISA Sound Card Replica](https://cdn.mos.cms.futurecdn.net/8wHEWM6DwBLixmbxoX4eZa.jpg) 


The appeal of the new Beavis Ultrasound is nicely summed up by schlae, as they explain that “unlike other clones, this design includes the entire schematic as well as the reverse-engineered source code of the GAL.” This GAL provides transparent and reproducible logic and is key to this project being able to handle IDE connectivity, like original Gravis Ultrasound (GUS) PnP cards. And, yes, this is not a GUS Classic or MAX clone, but caters to enthusiasts wanting a clone of the more complex and advanced GUS PnP.

A particular strength of the Beavis Ultrasound is its authenticity. It could be described as a faithful hardware‑level reproduction rather than a functional approximation. No microcontrollers take the place of real hardware here; there’s no emulation software, and features like the aforementioned GAL logic and IDE interface aren’t swerved by the developer.

However, this authenticity could also be an Achilles heel, as you’ll need to source an old AMD AM78C201 InterWave chip to complete a Beavis Ultrasound build and enjoy once again its marvelous sound. Actually, there’s another point to note before following schlae’s plans. There are no tried and tested footsteps to follow at the time of writing, as the dev admits they “have not actually fabricated the board and tested it for functionality,” so interested parties are instructed to “build this board at your own risk.”

## If you aren't an open-source or hardware-only purist

In recent weeks, we also reported on the return of the Orpheus II ISA soundcard due to “popular demand.” This device includes some GUS functionality but is a commercial, non-open-source proprietary product. Probably the most popular DIY-able solution around would be the PicoGUS, built around a Raspberry Pi Pico (RP2040) microcontroller, which handles all its GUS‑compatible audio playback in software – eschewing the need for rare vintage components like the AMD Interwave.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Mark Tyson](https://cdn.mos.cms.futurecdn.net/56vqMYLDaKRHPhHZgbADFR.jpg)

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.
