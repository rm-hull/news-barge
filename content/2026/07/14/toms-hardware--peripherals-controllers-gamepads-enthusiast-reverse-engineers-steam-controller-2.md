---
title: Enthusiast reverse-engineers Steam Controller 2 puck, creates DIY 'OpenPuck'
  that works without Steam Input — custom firmware can emulate Nintendo, PlayStation,
  and Xbox controllers
source_url: https://www.tomshardware.com/peripherals/controllers-gamepads/enthusiast-reverse-engineers-steam-controller-2-puck-creates-diy-openpuck-that-works-without-steam-input-custom-firmware-can-emulate-nintendo-playstation-and-xbox-controllers
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-14T14:08:41Z'
published: '2026-07-14T00:00:00Z'
description: Turn your Steam Controller into something much more powerful.
image: https://cdn.mos.cms.futurecdn.net/afqXySTxPCEC6t4PTDCq7m-1920-80.jpg
---

![Valve Steam Controller](https://cdn.mos.cms.futurecdn.net/afqXySTxPCEC6t4PTDCq7m.jpg) 

Valve's new Steam Controller lacks native XInput support, but you can still emulate it as long as Steam is running in the background. An enthusiast named *Safijari* has just engineered a more seamless solution, creating his own DIY "OpenPuck" that lets the Steam Controller emulate other gamepads on the fly. It can emulate Xbox, PlayStation, and even Nintendo layouts, and do so away from your PC.

![OpenPuck for Steam Controller 2 Intro - YouTube](https://img.youtube.com/vi/gSaqO9oqq9s/maxresdefault.jpg) 

OpenPuck serves as open-source firmware for a microcontroller, allowing you to easily flash and convert that dev board into a DIY Steam Controller puck. The firmware intercepts raw data from the Steam Controller and translates it on-device, enabling fully-fledged, real-time emulation without the need for Steam Input.

There are other options out there, but the creator used a Pro Micro NRF52480 from Amazon that has the appropriate Bluetooth and 2.4 GHz radios. Once primed in DFU mode, all you need to do is plug the board into your computer via USB-C, drag and drop the Arduino sketch onto it, and the microcontroller turns into an OpenPuck right away. You can 3D print a case to make the assembly look more polished, too.

 ![Valve Steam Controller](https://cdn.mos.cms.futurecdn.net/EbkkWpXmr3u9SSVfX4Bom7.jpg) 


The sketch is available on the project's GitHub page. Once you've flashed your controller, head to the configurator to manage the puck. It's a simple website that uses the WebUSB API to manage the controller, allowing you to switch between the different modes, which include Switch Pro, Xbox, DualSense (PS5), and DualShock 4 (PS4). The project description claims the puck only has a 1ms latency.

The Switch mode works natively on a Switch console with gyro and haptics support, but you can also emulate a Hori Pad that disables those extra features. The PlayStation modes only work on PC, but there's a special DualShock 3 mode that can work natively on a PlayStation 3 console as well, with gyro and haptics (Sixaxis). Of course, the default Steam Controller mode is also there.

You can switch between some of these different controller modes by pressing all four back buttons together and hitting either A, B, X, or Y, but the PlayStation modes require you to use the web configurator. Once everything is set up, however, the Steam Controller runs just like an official Switch, Xbox, or PlayStation controller without Steam even being open in the background.

 ![The different emulation modes of the OpenPuck](https://cdn.mos.cms.futurecdn.net/RVivYPHjz2Cv5uUBh85PCS.png) 


There's even a bonus "ReversePuck" sub-project that allows a Steam Deck to act as an external controller, supporting all of the Steam Controller's features (except grip). If you flash a second NRF52840 Pro Micro and plug it into a Steam Deck, you can stream the Steam Deck's built-in controls across the room over 2.4GHz to your OpenPuck-equipped PC, giving you access to essentially another Steam Controller.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Hassam Nasir](https://cdn.mos.cms.futurecdn.net/SxxNFHt95eGK37mKPhJpdZ.jpg)

Hassam Nasir is a die-hard hardware enthusiast with years of experience as a tech editor and writer, focusing on detailed CPU comparisons and general hardware news. When he’s not working, you’ll find him bending tubes for his ever-evolving custom water-loop gaming rig or benchmarking the latest CPUs and GPUs just for fun.
