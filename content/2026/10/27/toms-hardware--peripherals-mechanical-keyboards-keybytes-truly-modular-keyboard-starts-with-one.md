---
title: Keybytes ‘truly modular keyboard’ starts with one key and is assembled like
  Lego — each magnetic key module has its own RISC-V microcontroller for the ultimate
  in customizability
source_url: https://www.tomshardware.com/peripherals/mechanical-keyboards/keybytes-truly-modular-keyboard-starts-with-one-key-and-is-assembled-like-legos-each-magnetic-key-module-has-its-own-risc-v-microcontroller-for-the-ultimate-in-customizability
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-27T15:25:33Z'
published: '2026-10-27T00:00:00Z'
description: Connect as many or as few keys as you like to the Keyword hub in any
  arrangement you like. But it might end up costly.
image: https://cdn.mos.cms.futurecdn.net/YF4CFmJXyPYLqfV6fRe9zL-1920-80.jpg
categories:
- Technology & Software
- Hardware
people:
- Alspaugh
- Mark Tyson
- Tom
locations:
- GitHub
organisations:
- AKA Nathan Alspaugh
- Cherry MX
- Get Tom's Hardware
- GitHub
- Google News
- I2C
- Keybits
- Keybytes
- Keyword
- Lego
- MIT
- Tom's Hardware
- notaroomba
---

![Keybytes keyboard project](https://cdn.mos.cms.futurecdn.net/YF4CFmJXyPYLqfV6fRe9zL-1920-80.jpg)

Developer notaroomba (AKA Nathan Alspaugh) has published details of his Keybytes project on GitHub. In essence, this is a modular project where a Keyword hub is magnetically connected to Keybit keys, and each key has its own microcontroller. Hence the number of keys and their layout are entirely up to the user, with a modular design akin to building Lego.

We’ve seen oodles of imaginative and truly excellent mechanical keyboards over recent years, but Keybytes probably offers the greatest flexibility with regard to layout and key selection we’ve ever seen.

![Keybytes keyboard project](https://cdn.mos.cms.futurecdn.net/Z9qc2bfei6ssAt7hdPgCrL-900-80.jpg)
![Keybytes keyboard project](https://cdn.mos.cms.futurecdn.net/ijKQ3ZYhFZgLQKcsAigMuL-900-80.jpg)
![Keybytes keyboard project](https://cdn.mos.cms.futurecdn.net/Z9qc2bfei6ssAt7hdPgCrL-900-80.jpg)
![Keybytes keyboard project](https://cdn.mos.cms.futurecdn.net/ijKQ3ZYhFZgLQKcsAigMuL-900-80.jpg)

It starts with a Keyword, which is the main board that the Keybits connect to. This central component houses a stacked pair of PCBs. The top board packs an Arm Cortex M4-powered microcontroller, Bluetooth antenna, and flash memory. The lower board offers USB-C, charging, and a buck-boost converter.

Adding keys seems like a cinch. Every Keybit, one of the modular keys, contains a CH32V003 RISC-V microcontroller. Moreover, it features pogo pins on all 4 sides of every key for power and I2C. The case is magnetic so you can connect it to any aspect of the Keyword and other Keybits. Atop the Keybit, a Cherry MX switch is installed. We guess you can follow the GitHub MIT-licensed plans for this project and use your preferred variety of mechanical switches.

On the GitHub project page, there are no more than two Keybits together with a Keyword, so you don’t get to see what crazy layout plans he’s hoping to conjure up. However, it is still early days. Per the project journal, Keybytes only became a thing back in March this year, and it was only over the weekend that the developer got to finally boast “it finally works!!”

![Keybytes keyboard project](https://cdn.mos.cms.futurecdn.net/x2GsjUw4sLYZUWCcD7Fq3M-1200-80.jpg)
![Keybytes keyboard project](https://cdn.mos.cms.futurecdn.net/KyJFnGPgByhx6S5sGdvwvL-1200-80.jpg)
![Keybytes keyboard project](https://cdn.mos.cms.futurecdn.net/x2GsjUw4sLYZUWCcD7Fq3M-1920-80.jpg)
![Keybytes keyboard project](https://cdn.mos.cms.futurecdn.net/KyJFnGPgByhx6S5sGdvwvL-1508-80.jpg)

*Both the Keyword and the Keybit modules are 1U sized (19.05 x 19.05mm).*

Alspaugh, a student at MIT, has shared all the assets, files, and details you might need to make your own Keybytes keyboard. The GitHub repository says that everything is released under the permissive MIT license.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

It might quickly become expensive for individuals to put together a usable layout with, say, 60 keys. Getting the PCBs made, buying and soldering all the components, and 3D printing all the custom bits and pieces is also a considerable task when your proposed keyboard layout is more than a handful of shortcut keys. In the aforementioned journal, Alspaugh actually mentions that he priced up a “full sized keyboard (2 keywords and like 110 keybits) and it's around $900 assembled.”

Keyword has a status light, but the Keybits lack any kind of lighting. My wishlist for Keybytes 2.0 includes customizable RGB lighting, and I would also like to propose Dialbits, a Fingerprintbit, and a matching Touchpadbit.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Mark Tyson](https://cdn.mos.cms.futurecdn.net/56vqMYLDaKRHPhHZgbADFR-140-80.jpg)

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.
