---
title: Modder builds 8,192-core GPU at home out of RISC-V microcontrollers — full
  "graphics card" draws over 2,000 watts of power, requires a 3D printer to program
source_url: https://www.tomshardware.com/maker-stem/modder-creates-8-192-core-gpu-at-home-out-of-risc-v-microcontrollers-full-graphics-card-will-draw-over-2-000-watts-of-power-requires-a-3d-printer-to-program
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-07T11:19:39Z'
published: '2026-07-07T00:00:00Z'
description: To be technically correct, it's both a graphics card and a monitor.
image: https://cdn.mos.cms.futurecdn.net/e4hjpmTtr7XMNRRsZBBYBm-2048-80.png
---

![RISC-V GPU](https://cdn.mos.cms.futurecdn.net/e4hjpmTtr7XMNRRsZBBYBm.png) 

Save for the occasional deal, GPU prices are so high these days that they might even get you wondering if you couldn't just roll your own. As it happens, renowned hardware hacker Matthias Balwierz (more commonly known as Bitluni) elected to do precisely that, enlisting the help of a total sum of 8,192 RISC-V microcontrollers (MCUs) for this enterprise.

He originally planned to create a display of some sort, but after careful consideration regarding costs and difficulty, he elected to solder an RGB LED directly to each microcontroller chip, effectively turning his GPU into a GPU-and-monitor combo, if we're getting technical. Going for a 1920x1080 resolution would require over two million chips, so Balwierz aimed for a final-project resolution of 320x200 with 64,000 chips — familiar figures to anyone who played games in the DOS days.

Balwierz opted to make boards with 16x32 "pixels" each, in a circular arrangement reminiscent of the Cray-1 supercomputer, though with far more *blinkenlights*. His option to directly solder each light onto each MCU was borne out of budgetary restrictions, as the addressable-RGB variant would also prove too expensive.

![YouTube](https://img.youtube.com/vi/qMR3IXF2sWw/maxresdefault.jpg) 

For this initial stage of the project, Balwierzstuck with "only" 8,192 chips, though he made plans for the whole shebang. Perhaps the most impressive figure is the power draw, at a total of 2,161 W, or around 655 amps at 3.3 V. Each MCU only draws 10 mA, a figure that looks innocent enough until you do the actual math. To feed power into the beast, he enlisted the help of a Corsair WS3000 ATX power supply unit along with custom-designed converters to go from 12 V to 3.3 V at high current.

As for the chips themselves, they're QingKe CH570 RISC-V units, each with a 32-bit RISC-V CPU with a limited instruction set, running at up to 100 MHz. The diminutive chip contains an impressive amount of hardware, including a USB controller, a 2.4 GHz transceiver, and Bluetooth 5.0 LE support. Each of these set Balweirz back $0.13, once again a measly looking figure that will add up to well over $8,000 in chips alone for the final 320x200 array. Each set of 32 MCUs is controlled by a beefier CH32V unit.

As habitual, Balwierz custom-designed every single PCB, power delivery circuit, interface board, and testing board himself. This is apparently the first time he's designed a six-layer PCB, and he actually ran up against design limits of the JCLPCB service. He originally planned for the whole project to use immersion cooling, but decided against that for the time being due to environmental and cost concerns, though he did spec out the appropriate acrylic container for it.

Balwierz goes over each chapter of the process in detail in his video, and one of the most clever bits is how he made a 3D-printed three-prong fork-like tool to program each MCU. He then took said tool and attached it to the 3D printer's carriage, and used a Python script issuing direct G-code to the printer to precisely aim it at each MCU in the board.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

It'll take a while before this is a functional CPU that can threat Nvidia, but we're looking forward to seeing *Doom* displayed on it. Also, it's kind of funny how one guy in a lab designed a better power delivery mechanism than the firm's 12V-2x6 connector... using just parts from AliExpress.

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.
