---
title: Russian chipmakers demo homegrown RISC-V and Arm chips with retro games — NES
  clone runs on Baikal microcontroller
source_url: https://www.tomshardware.com/tech-industry/semiconductors/russian-semiconductor-players-shows-off-bespoke-cpu-and-soc-designs-arm-and-elbrus-architectures-on-display
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-15T11:29:30Z'
published: '2026-10-15T00:00:00Z'
description: Russia's homegrown chipmaking continues apace despite sanctions.
image: https://cdn.mos.cms.futurecdn.net/pM5BCD8fJywaDVZrTjPrCY-840-80.jpg
categories:
- Technology & Software
- Hardware
people:
- Bruno Ferreira
- Dmitrii Kuznetsov
- Tom
locations:
- Sochi
organisations:
- Arm
- Get Tom's Hardware
- Gigabit Ethernet
- Google News
- Hypercom-U
- MCST
- ME26
- MP21
- PC
- RAM
- RISC-V
- Rangers
- Rust
- Tom's Hardware
---

![MCST Elbrus chip](https://cdn.mos.cms.futurecdn.net/pM5BCD8fJywaDVZrTjPrCY-840-80.jpg)

Geopolitics and sanctions have mostly cut off the Russian public from Western hardware — at least officially. In recent ages, the country's homegrown chip designs are Arm, RISC-V, and Elbrus architectures. A handful of interesting designs were on display at the Microelectronics 26 (ME26) forum in Sochi, using retro gaming as a demonstration point. A couple of years back, the government even issued an order to create a high-end gaming console, albeit with relatively little success. The result of that initiative didn't appear to be on display at the event.

> На выставке МЭ26 в Сочи показывали сразу несколько игровых применений русских процессоров Байкал: консоль и визитка на Ушке BE-U1000 Элвис: полноценная приставка на Гиперком У (бывш. СКИФ) МЦСТ: «игровые» ПК на Эльбрусах Не серьёзно, но занимательно #riscv #innoru #pureru [https://t.co/QGlRTMnvLROctober](https://t.co/QGlRTMnvLROctober) 11, 2026

The report comes from Dmitrii Kuznetsov, a RISC-V and Rust enthusiast who displayed photos from the event. The first units on display use Baikal Electronics' BE-U1000 microcontroller. According to our digging, the chip packs a CPU with three CloudBear cores (32-bit RISC-V) — two BR-350s clocked at 200 MHz, along with a BM-310 at 100 MHz.

Given the microcontroller nature, embedded resources are intentionally sparse, with 256 KB of flash and 192 KB of SRAM — though there's support for external flash. A host of I/O interfaces, including USB 2.0, I2C, I2S, UARTs, and 48 GPIO lines, round out the 10x10 mm QFN-88 package. These parts are seemingly aimed at robotics, automation, IoT, sensors, and similar applications.

There was a business card-sized controller-and-console on display with a BE-U1000 chip, along with an "Ushka" console styled like the original NES (with matching controllers). The game on display appears to be *Chip 'n Dale: Rescue Rangers*.

![tsmc](https://cdn.mos.cms.futurecdn.net/p2QqhVFP7dTRWfeVBCYBYV-1200-80.jpg)

Next up, there's the Elvis Hypercom-U, a SoC packing four Arm Cortex-A53 CPU cores at up to 1.2 GHz, dual ELcore-50 DSPs, a PowerVR GE8300 GPU, and dedicated video, image, and navigation processing blocks. The main silicon can be paired with up to 8 GB of LPDDR4, and supports USB 3.0, Gigabit Ethernet, Wi-Fi, and Bluetooth connectivity, and HDMI output.

This product is apparently aimed at multimedia, navigation, SBCs, and smart cameras. At the show, a board with the Hypercom-U was shown playing the original *Super Mario* as a demonstration.

Finally, there were MCST's Elbrus-based PCs, though the tweeter offered few details on which were on display. For context, Elbrus is a Russian-developed chip architecture, often poised as the basis for high-end desktop and server applications.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Our best guess is that the machines at the forum were based on the leading-edge Elbrus-16S chip with 16 cores at up to 2 GHz and up to 8 channels of DDR4-3200 RAM. The chip is manufactured on a 16 nm process and comprises 12 billion transistors. There are dual-processor server prototypes with up to 2TB of RAM using this design.

The other chip likely being demoed is the Elbrus-2S3, a chip targeted at mini-PCs and laptops. We've covered the Rostec MP21 previously, a Raspberry Pi-like machine with 8GB of RAM and SSDs up to 480GB. The 16-nm SoC is fairly decent, clocked at up to 2 GHz and capable of 196 GFLOPS. There's support for DDR4-3200 and PCIe 3.0, but power consumption can be fairly nasty, as the MP21 board can chew around 40W.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G-140-80.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.
