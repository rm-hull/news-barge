---
title: Modder 'fixes' melting RTX 5090 power connectors with custom distributor —
  dual 8-pin mod peaks at just 40C during a 48-hour 550W stress test
source_url: https://www.tomshardware.com/pc-components/gpus/modder-fixes-melting-rtx-5090-power-connectors-with-custom-distributor-dual-8-pin-mod-peaks-at-just-40c-during-a-48-hour-550w-stress-test
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-04T17:09:51Z'
published: '2026-10-04T00:00:00Z'
description: The modder claims he could offer this solution to other owners with full
  warranty coverage
image: https://cdn.mos.cms.futurecdn.net/zSDbAK6zJvGgD5vmjfWw3m-2560-80.jpg
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
people:
- Jhet Borja
- Tom
locations: []
organisations:
- DallasGrave
- GPU
- Get Tom's Hardware
- Google News
- Nvidia
- PCB
- PNY
- PSU
- Reddit
---

![Nvidia GeForce RTX 5090 Founders Edition](https://cdn.mos.cms.futurecdn.net/zSDbAK6zJvGgD5vmjfWw3m-1920-80.jpg)

Reddit user u/DallasGrave shared a fix for his RTX 5090, one of the best graphics cards, whose 12VHPWR connector was overheating, along with an image of a module screwed onto the back of his GPU. This module is apparently a custom-made power distributor that splits the current load across more wires to lower connector temperatures. Apparently, u/DallasGrave is connected to GRAVEPC.com, which offers mainly custom cooling solutions for small form-factor PCs.

In response to a commenter asking whether this mod will be covered under PNY’s warranty, he said, “We're a PNY partner. You'll be able to buy a PNY-specific card with a similar modification directly from us with a full warranty.” This mod isn't currently on his website, however. PNY hasn't been great at honoring warranties for the 12VHPWR issue with third-party cables, as covered in this recent story about a third-party cable melting in use, so take the claim of full warranty coverage with a grain of salt.

The 16-pin connector issue plagues many Nvidia graphics cards because they draw high current through what is essentially a 12-pin connector. The four smaller pins are sensors, and the remaining 12 are split between six +12V and ground connections. The connector typically uses high-current-rated 16AWG cables, and in theory, they should handle up to 600W.

Apparently, some cases of these melting connectors are due to poor connections where the pins don't make enough contact, causing high resistance and heat buildup, and uneven current distribution is often a source of issues. This was rarely the case with older multi-8-pin connector setups, as the safety margins were higher. However, graphics cards now draw more current, and Nvidia thought it should run it through fewer wires.

The modder essentially fixed this issue by soldering additional connections to the power rails directly on the RTX 5090’s PCB and routing them to what can only be described as a power distributor. This distributor contains a PCB that the wires connect to and where the two female 8-pin connectors are placed. It is unknown whether the modder designed it himself and whether it contains any other power-delivery or protection components, such as capacitors and fuses.

The distributor appears to be custom-made to fit his specific graphics card, and the housing shows signs of resin printing. In the modder’s stress test, running the card at full load, pulling 550W for 48 hours, he says it “never crossed 40c even at the joint.”

![Soldering power wires directly to the PCB of an RTX 5090](https://cdn.mos.cms.futurecdn.net/Qqji7GJkLVnUJiotFkGWLX-1200-80.png)

The 12VHPWR connector is a terrible design; cramming that much power into only six wires creates a very sensitive system where slight misalignment and uneven current distribution could cause connector-melting temperatures. This mod is cleaner and more attractive than the other power mods we’ve covered, like this poor Galax RTX 5090, but it is still invasive, requiring wires to be soldered directly to the card’s power rails.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Jhet Borja](https://cdn.mos.cms.futurecdn.net/niBNJTDN6c99Ri7HD5zNZ8-140-80.png)

Jhet Borja is a serial hobbyist who was taking apart toys from childhood and sketching inventions. He now loves doing DIY projects ranging from designing custom 3D-printed parts, building PCs and keyboards, all the way to woodworking. If he's not getting his hands dirty, he's probably brainstorming his next project.

* I mean, the modding for this issue might not be so interesting anymore.  
    
  PSU makers are starting to make power supplies that have the anti-melt circuitry on the other side since Nvidia didn't want to do it on their cards anymore. So just buy a new power supply and give Nvidia the finger because \_they\_ did this to you.  
    
  Or better yet, sell your Nvidia card and buy a high quality product that won't melt. Reply
*For $5000+ they sure as \*\*\*\* can make a product that won't burn itself up.  
    
  Im smarter than the average bear and avoid massively overpriced shoddy products, but I understand I am very much in the minority there. Reply
