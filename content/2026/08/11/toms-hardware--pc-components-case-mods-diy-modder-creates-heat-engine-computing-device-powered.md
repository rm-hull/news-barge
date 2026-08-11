---
title: DIY modder creates 'heat engine computing device' powered by a Stirling engine,
  can run Tetris, Snake, and Pong — 80 MHz processor operates on just 150 milliwatts
  of power
source_url: https://www.tomshardware.com/pc-components/case-mods/diy-modder-creates-heat-engine-computing-device-powered-by-a-stirling-engine-80-mhz-esp32-can-run-tetris-snake-and-pong-on-just-150-milliwatts-of-power
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-11T13:12:43Z'
published: '2026-08-11T00:00:00Z'
description: Stirling engine meets retro computing.
image: https://cdn.mos.cms.futurecdn.net/MG7G8ZHEJpE3LqHmMEmTiG-1280-80.jpg
---

![Build process of the DIY microcomputer powered by a Stirling engine](https://cdn.mos.cms.futurecdn.net/MG7G8ZHEJpE3LqHmMEmTiG.jpg) 

In one of the most unique DIY projects, Reddit user PickentCode has created what can be described as a completely off-the-grid "heat engine computing device." Instead of relying on solar panels or a battery pack, the creator went in a completely different direction, building a custom steampunk-inspired microcomputer which features a miniature Stirling engine to power the hand-crafted wooden console.

Originally patented in 1816 by the Scottish minister and inventor Robert Stirling, a Stirling engine converts heat directly into mechanical energy. By applying a flame to one end of a sealed cylinder, the temperature difference forces the air inside to expand and contract. This cycle pushes a piston that spins the flywheel, which can be used to power a simple generator that converts the mechanical rotation into usable electricity.

"The entire project took about a month to design, build, and program," PickentCode told *Tom's Hardware.* They first conceptualized a 3D layout using Blender before constructing the physical case out of wood. They even went ahead and utilized a DIY laser engraver to etch a portrait of Robert Stirling and his original 1816 engine patent sketch directly onto the wooden side panels. For the smaller structural elements, the electronic housings and the keycaps were custom 3D printed, while the decorative pipes winding across the frame were made from old shower tubing and some gold paint.

![Build process of the DIY microcomputer powered by a Stirling engine](https://cdn.mos.cms.futurecdn.net/MG7G8ZHEJpE3LqHmMEmTiG-1200-80.jpg) 

![Build process of the DIY microcomputer powered by a Stirling engine](https://cdn.mos.cms.futurecdn.net/ASmBD98kfdmUtTUHgtSrjG-1200-80.jpg) 

![Build process of the DIY microcomputer powered by a Stirling engine](https://cdn.mos.cms.futurecdn.net/7bYnabQH7HBJWm7bSfPijG-1200-80.jpg) 

![Build process of the DIY microcomputer powered by a Stirling engine](https://cdn.mos.cms.futurecdn.net/MG7G8ZHEJpE3LqHmMEmTiG-1280-80.jpg) 

![Build process of the DIY microcomputer powered by a Stirling engine](https://cdn.mos.cms.futurecdn.net/ASmBD98kfdmUtTUHgtSrjG-1280-80.jpg) 

![Build process of the DIY microcomputer powered by a Stirling engine](https://cdn.mos.cms.futurecdn.net/7bYnabQH7HBJWm7bSfPijG-1280-80.jpg) 

The brains of the system are an ESP32 C3 microcontroller paired with a 2.42-inch monochrome OLED display with a 128x64 resolution, alongside a 16-key keypad. The electrical output of the generator is stabilized using small capacitors wired into the circuit. One can also actively monitor the voltage output using the analog voltmeter, which is wired in parallel, and the two toggle switches mounted on the front panel can be used to turn on the main circuit and the voltmeter.

Running an electronic device, in this case a microcomputer, purely on fire comes with obvious energy limitations. The model Stirling engine can produce only 150 milliwatts of power, and to stay within this tiny power budget, the creator implemented certain hardware and software optimizations. For instance, Wi-Fi and Bluetooth were completely disabled, and the screen brightness was kept low to conserve every milliwatt. PickentCode also tuned the ESP32's CPU frequency, reducing it down to just 80 MHz when updating the screen or interpreting opcodes, going all the way down to just 10 MHz while sitting idle in the main loop.

Despite the limitations, the computer is fully functional. It runs a custom CHIP-8 virtual machine preloaded with classic gaming ROMs like Tetris, Snake, and Pong. Impressively, it also features a built-in code editor, allowing users to type in CHIP-8 opcodes directly to write and execute their own custom programs on the fly.

Stirling engines are not exactly new to the world of computing. Earlier this year, we covered a project by Windows development guru Dave Plummer who showcased a cooling solution that used a small Stirling engine to convert waste heat from an AMD Threadripper system into mechanical energy, which was used to spin the engine's flywheel. While it isn’t an actual solution to an overheating chipset, it is claimed that the flywheel can spin up to about 200 RPM in a 20C/68F environment.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Kunal Khullar](https://cdn.mos.cms.futurecdn.net/NDK3ae3zDxAx2BJnMXxBJV.jpg)

Kunal Khullar is a contributing writer at Tom’s Hardware. He is a long time technology journalist and reviewer specializing in PC components and peripherals, and welcomes any and every question around building a PC.
