---
title: MIT engineer releases open-source 'Keybytes' magnetic mechanical keyboard
source_url: https://www.techradar.com/pro/this-truly-modular-keyboard-can-be-built-like-a-lego-set-meaning-you-can-add-as-many-keys-as-you-like
source_site: TechRadar UK
source_slug: techradar-uk
description: MIT student unveils 'Keybytes' open-source keyboard using magnetic keys
  and RISC-V chips — but building one could set you back $900
image: https://cdn.mos.cms.futurecdn.net/D5fnjmBue6VPp6Cyw2ZDB8-1600-80.jpg
published: '2026-11-01T00:00:00Z'
scraped_at: '2026-11-01T05:55:38Z'
categories:
- Technology & Software
- Science
people: []
locations: []
organisations:
- Cherry MX
- GitHub
- Keybit
- MIT
- Nathan Alspaugh
- TechRadar Pro
---

![Keybytes, an open-source keyboard project that lets users create custom keyboards](https://cdn.mos.cms.futurecdn.net/D5fnjmBue6VPp6Cyw2ZDB8-1600-80.jpg)

* **Keybytes lets users assemble custom keyboards from magnetically connected individual keys**
* **Every Keybit contains its own RISC-V microcontroller for individual key operation**
* **A full-size Keybytes configuration could cost approximately $900 to assemble**

MIT student Nathan Alspaugh has developed Keybytes, an open source keyboard project that lets users create custom layouts by connecting individual keys to a central controller.

The design uses magnetic connections and dedicated microcontrollers to support flexible arrangements.

Keybytes consists of two main elements: the Keyword controller and individual Keybit modules, which connect magnetically to form a personalised keyboard.

## Magnetic keys allow custom layouts

Each Keybit contains a RISC-V microcontroller, allowing individual keys to operate independently rather than relying entirely on one central processor.

Every Keybit measures 19.05 x 19.05mm, corresponding to a standard 1U keyboard unit.

Its four-sided pogo pin connections carry power and I2C communications, allowing modules to connect through different edges and accommodate varied arrangements.

The central Keyword module contains two stacked circuit boards, with an Arm Cortex M4 microcontroller.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The Keyword controller contains two stacked circuit boards, with its upper board housing an Arm Cortex-M4 microcontroller, a Bluetooth antenna and flash memory.

Its lower board provides USB-C connectivity, charging functions and a buck-boost converter for power management.

Each Keybit accommodates a Cherry MX mechanical switch, giving builders the option of selecting compatible switches for their preferred typing experience.

The magnetic connections allow keys to attach around the Keyword controller or alongside other modules, removing the fixed layout restrictions found in conventional keyboards.

Alspaugh has published the project files, design assets and construction details on GitHub under the permissive MIT licence.

This allows others to examine the design, build their own units and modify the hardware according to their requirements.

## Building a full keyboard could cost $900

Despite its flexibility, Keybytes remains an early-stage project, with Alspaugh reporting that the basic system had only recently reached a working state.

Publicly available project documentation currently shows limited combinations of modules rather than a completed, full-size keyboard layout.

The developer estimated that assembling a full-size version using approximately 2 Keyword controllers and 110 Keybits would cost around $900.

That figure indicates how quickly expenses could accumulate when each additional key requires its own circuit board, microcontroller, and other electronic components.

Builders must also account for printed circuit board production, component purchases, soldering, and custom 3D-printed enclosures.

These requirements could make large layouts considerably more demanding than smaller configurations designed around a handful of shortcuts.

The current design also has limitations in its lighting options, since the Keyword includes a status indicator while individual Keybits lack dedicated illumination.

Future versions could add features such as customisable RGB lighting, rotary controls, fingerprint recognition modules or a compatible touchpad. These remain proposed additions rather than confirmed developments.
