---
title: $10 programmer saves BIOS-locked Lenovo ThinkPads from the dump — exploit bypasses
  supervisor passwords to save 4th- to 8th-gen Intel models from e-waste
source_url: https://www.tomshardware.com/uk/laptops/usd10-programmer-saves-bios-locked-lenovo-thinkpads-from-the-dump-exploit-bypasses-supervisor-passwords-to-save-4th-to-8th-gen-intel-models-from-e-waste
source_site: Tom's Hardware
source_slug: toms-hardware
description: Many cheap company ThinkPads come with supervisor passwords and often
  end up as e-waste. Ukrainian YouTuber Hileeq shows how easy it is to bypass the
  password with a $10 programmer.
image: https://cdn.mos.cms.futurecdn.net/ngNTtyvcneBTnREftZgRMn-2035-80.jpg
published: '2026-11-10T00:00:00Z'
scraped_at: '2026-11-10T19:42:37Z'
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
people:
- Hileeq
- Jhet Borja
- Mark Juvan
- Tom
- Victor Voinea
locations:
- Netherlands
- Nijmegen
organisations:
- Badcaps
- CH341A
- EC
- EEPROM
- Get Tom's Hardware
- Google News
- Hileeq
- Knucklegrumble
- Lenovo ThinkPads
- NeoProgrammer
- Radboud University
- ThinkPad
- eBay
---

![ThinkPad under repair](https://cdn.mos.cms.futurecdn.net/ngNTtyvcneBTnREftZgRMn-1920-80.jpg)

Rebooted by Hileeq has shared how others can get cheap Lenovo ThinkPads and save them from becoming e-waste by using a simple BIOS unlock hack that only requires a $10 programmer and another laptop or PC. The technique is niche, known mostly by technicians, but Hileeq is the first to give this bypass mass attention with an easy-to-follow YouTube tutorial.

Rebooted by Hileeq's channel, dedicated to fixing cheap eBay finds, documents the process and what he learned while fixing the laptops. Three weeks ago, he posted a video explaining how to bypass locked Lenovo ThinkPads with Intel 4th- to 8th-generation CPUs using a cheap CH431A programmer to read, write, erase, and save EEPROM and SPI flash memory.

Companies often add supervisor passwords to the fleet of ThinkPads they hand out to their employees as an IT security measure. When these ThinkPads are disposed of, often with the storage removed and destroyed, it’s rare that the supervisor passwords are included and documented. These locked ThinkPads are then incredibly cheap because of the lack of access, ending up as e-waste most of the time. However, Victor Voinea shared a post in a Romanian forum containing his ThinkPad supervisor removal exploits.

Unfortunately, Voinea’s method generated a random password every time the exploit was run, requiring users to contact Voinea for the key specific to the generated hardware ID — and getting the password wasn’t free. However, in 2020, Knucklegrumble posted a free way to bypass the password in the Badcaps electronics repair forum. Mark Juvan, an Ethical Hacker, reverse-engineered Knucklegrumble’s exploit as his cybersecurity master’s thesis at Radboud University Nijmegen, Netherlands, which goes into deeper detail.

![Секрет ПЕРЕКУПІВ ноутбуків: ЗЛИВ інфи, де брати ДЕШЕВІ ноути! Bios PASSWORD?! - YouTube](https://img.youtube.com/vi/3_ON_tEWO1Q/maxresdefault.jpg)

The exploit begins by extracting the BIOS from the EEPROM chip on the motherboard using the CH341A programmer and plugging it into a USB port of another PC or laptop. Hileeq then uses NeoProgrammer, a utility for CH341A programmers, and dumps the BIOS, saving a copy of it on the other laptop. NeoProgrammer then applies the same auto-patching workflow Knucklegrumble created.

When the patched BIOS is flashed onto the EEPROM, the laptop can then be turned on, and Hileeq goes through some steps requiring a few keystrokes which remove the password saved in the Embedded Controller (EC), a separate IC that stores security data, among other system tasks. The original BIOS can then be flashed back into the EEPROM, and with the supervisor password removed, the laptop is now usable.

Juvan states in his paper that the exploit takes advantage of a weakness in Lenovo’s firmware verification and driver architecture. Lenovo actually provides the EmulatedEepromDxe driver needed by the exploit, and the driver allows the EEPROM to be read and written to — and the EC’s supervisor password happens to be stored where it’s treated as EEPROM memory, allowing the supervisor password to be overwritten or removed.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

The hard, complicated work has already been done by the electronics repair community, and now the process to bypass the supervisor password requires just a few steps and an inexpensive programmer tool. While the method may only be for ThinkPads with Intel 4th- to 8th-generation CPUs, this will still save plenty of usable ThinkPads from going to waste, as Hileeq’s popular post potentially encourages more people to attempt this themselves — who knows, this might cause a domino effect to unlock newer generations of ThinkPads.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Jhet Borja](https://cdn.mos.cms.futurecdn.net/niBNJTDN6c99Ri7HD5zNZ8-140-80.png)

Jhet Borja is a serial hobbyist who was taking apart toys from childhood and sketching inventions. He now loves doing DIY projects ranging from designing custom 3D-printed parts, building PCs and keyboards, all the way to woodworking. If he's not getting his hands dirty, he's probably brainstorming his next project.
