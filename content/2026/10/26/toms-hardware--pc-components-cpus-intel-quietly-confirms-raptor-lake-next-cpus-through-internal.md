---
title: Intel quietly confirms Raptor Lake Next CPUs through internal driver publication
  — LGA 1700 chips also appear in shipping manifests dating back to August
source_url: https://www.tomshardware.com/pc-components/cpus/intel-quietly-confirms-raptor-lake-next-cpus-through-internal-driver-publication-lga-1700-chips-also-appear-in-shipping-manifests-dating-back-to-august
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-26T20:27:52Z'
published: '2026-10-26T00:00:00Z'
description: DDR4 support and presumably affordable prices should be a boon for extant
  Socket 1700 system owners
image: https://cdn.mos.cms.futurecdn.net/sQkjcrWci3QikXR5qNxa4d-1920-80.jpg
categories:
- Technology & Software
- Hardware
people:
- Bruno Ferreira
- Tom
locations:
- Alder Lake
- Vietnam
organisations:
- 99DLMT
- Club386
- Get Tom's Hardware
- Gigabyte
- Google News
- Intel
- PC
- Realtek
- SST
- Tom's Hardware
---

![13th Gen Raptor Lake CPU](https://cdn.mos.cms.futurecdn.net/sQkjcrWci3QikXR5qNxa4d-1920-80.jpg)

Intel has published an internal test driver with the "RPL-NEXT" label, presumably in reference to Raptor Lake Next CPUs that *Tom's Hardware* first reported on in June. On the same day as the driver was uncovered, shipping manifests from Vietnam were published by Club386, showing exports of CPUs labeled "Raptor Lake Next" dating back to August, complete with cache and clock speed information.

The driver was first spotted by @momomo\_us on X, and we were able to find it by searching the name in Intel's software database. The file is locked (hence the padlock icon), and clicking on it will redirect you to an Intel login page. Given that and the "testbuild" label, it looks like this is an internal driver test that wasn't meant to be published.

Judging by the existing conventions, the driver package is for the Smart Sound Technology (SST), a audio digital signal processor integrated into the silicon since the Alder Lake days. Audio codecs like those of Realtek use SST for offloading duties like noise reduction, echo cancellation, low-power audio playback, and wake-on-voice without adding to the CPU load, and saving precious watts in the process.

For broader context, Raptor Lake Next is Intel's refresh of the Raptor family of CPUs, meant to plug into existing LGA-1700 motherboards. Given the currently insane DDR5 memory prices, gamers ought to be happy on two fronts: getting newer chips for their existing motherboards, and the ability to use more affordable DDR4 instead, an ability all but confirmed by Gigabyte's recent BIOS updates.

According to Club386's shipping manifests, there are so far four chip models en route from Intel's Vietnam facilities. Their specs suggest that they're replacements for extant Core i5 and Core i7 models, as a previous leak indicates that Intel doesn't yet have any plans for replacements for its Core i9-14900K chip.

As such, the listed models should top out with the 99DLMV part number, with 16 cores in an 8P + 8E arrangement, a meaty 3.5 GHz base block, and 30 MB of cache (presumably L3). This is the only model with a 125W TDP, and its base clock is higher than that of the Core i9-14900K, so it should be a speedy enough affair despite not having the high core counts of the halo models. Chances are it'll be a nice gaming CPU with pretty high turbo clocks, but only reviews will confirm that.

Interestingly, the 99DLMT has 20 cores (8P + 12E), but its much lower 65W TDP and 2.1 GHz base clock, which indicate that this model might be an efficiency-oriented productivity chip. In the table below, we added our guesses as to which models match existing chips.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Part number**|** Cores / Threads**|** TDP**|** Base clock**|** Cache**|** Approximate matches** |
| 99DLMV | 8P + 8E (24) | 125 W | 3.5 GHz | 30 MB | i7-14700 / i7-13700 |
| 99DLMT | 8P + 12E (28) | 65 W | 2.1 GHz | 33 MB | i5-14600K / 13700K |
| 99DLMW | 6P + 4E (16) | 65 W | 2.6 GHz | 24 MB | i5-14400 / i5-13500 |
| 99DLMX | n/a | 65 W | 2.6 GHz | 24 MB | As above |

There's no word about pricing, but we'd expect the new chips to ring in at roughly the prices of the existing models. As points of reference, the Core i7-14700 is currently $366, or $330 for the "F" variant without integrated graphics. At the lower end of the above table, the Core i5-14400 is sitting at $208, or only $161 without an IGP.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G-140-80.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.
