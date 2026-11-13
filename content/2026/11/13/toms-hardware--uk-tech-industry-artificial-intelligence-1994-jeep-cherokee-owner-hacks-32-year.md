---
title: 1994 Jeep Cherokee owner hacks 32-year-old car with Claude AI to pass California
  smog tests — enthusiast reverse-engineered the ancient ECU for diagnostics and control
source_url: https://www.tomshardware.com/uk/tech-industry/artificial-intelligence/1994-jeep-cherokee-owner-hacks-32-year-old-car-with-claude-ai-to-pass-california-smog-tests-enthusiast-reverse-engineered-the-ancient-ecu-for-diagnostics-and-control
source_site: Tom's Hardware
source_slug: toms-hardware
description: An AI enthusiast managed to get his old 1994 Jeep Cherokee to pass the
  California smog tests thanks to the help of AI, a little electronics wiring skill,
  and $15 of components.
image: https://cdn.mos.cms.futurecdn.net/BZRHW5BTLyqX6i4nsjHfrH-1920-80.jpg
published: '2026-11-13T00:00:00Z'
scraped_at: '2026-11-13T19:40:32Z'
categories:
- Technology & Software
- Hardware
people:
- Claude
- Codex
- Faiakes
- Mark Tyson
- Muhammad Zulali
- Tom
locations:
- California
- Cherokee
- Kensington
- Maryland
- USA
organisations:
- AI
- Arduino Nano
- Cherokee
- Chrysler
- Codex
- ECU
- EEPROM
- GPLv3
- Get Tom's Hardware
- Google News
- Jeep
- Tom's Hardware
---

![1984-1996 series Jeep Cherokee photographed in Kensington, Maryland, USA. 1996 two-door shown.](https://cdn.mos.cms.futurecdn.net/BZRHW5BTLyqX6i4nsjHfrH-1920-80.jpg)

An AI enthusiast managed to get his old 1994 Jeep Cherokee to pass the California smog tests, all thanks to the help of AI and a little electronics wiring skill. This 32-year-old car had only a primitive engine computer, but after connecting it to a laptop via an Arduino Nano board, many settings could be read and eventually controlled.

![Claude reverse engineered my 32-year-old Jeep. Then it started controlling it. - YouTube](https://img.youtube.com/vi/WPj3aQ-xxpI/maxresdefault.jpg)

The above video documents Muhammad Zulali’s journey from the Jeep failing consecutive smog tests, to managing to hook it up and get readings from the ECU, to tuning and fixing the engine emission issues. All the while, Claude provided guidance, and Codex wrote any required code.

This rather old Jeep was failing the California smog tests due to producing too much NOx at certain test speeds. It initially failed at 25mph. Then, after Zulali made some adjustments to the oxygen mix, it failed at both 25mph and 50mph. Yes, it got worse.

Zulali admits he was effectively making adjustments blind, and subsequent regulatory pollution tests cost nearly $100 each time. That’s clearly a big problem, but we have AI to help us in 2026. Actually, it was AI and a $3 microcontroller, contributing to a total bill of materials of no more than $15.

The first hurdle facing the possible AI solution was the question of how to interface an old car and a new laptop. Claude told the Jeep owner that the engine communicated on a Chrysler SCI bus at ~7,800 baud, which was electrically inverted compared to a typical serial port. An Arduino Nano can handle the required inversion and hook up the data to a modern computer. The Nano was breadboarded, with a few necessary wires, three of which connected to the 6-pin diagnostic plug in the Cherokee.

![xj-scanner wiring diagram](https://cdn.mos.cms.futurecdn.net/sa5S3oMAbCuefugWZgacoH-1200-80.jpg)

The first connection attempt was a success, but only coolant temperature and battery voltage were charted by the system to begin with. Zulali wanted more data points plus some controls to fix the smog test problem. After a couple of red herrings regarding the engine “running rich” with 22% extra fuel, based on other car model data, the Jeep owner got Claude to collect data from test drives. The AI logged engine data and fault codes during a drive at 25 mph and at 50 mph to see what was happening. It was also let loose to control things like fuel pressure.

With what looked like a credible diagnosis and solution in hand, Zulali wanted to reflash the car’s main ECU with AI-tweaked code that would mean it could pass all the California smog tests. Unfortunately, this car’s computer was just a few months too old to feature reflashable firmware. Instead, the Jeep owner got Codex to inject and run custom code inside a nearby EEPROM.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

“Claude did most of the diagnostic work and Codex did pretty much all of the memory work,” admits Zulali. “I just did the wiring and the driving.” He added that he didn’t need the services of a mechanic or a Chrysler dealer tool for this feat.

In addition to the video, the Cherokee emissions fixer has created a GitHub repository for this project, dubbed xj-scanner. It is free software distributed under the GPLv3 license.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Mark Tyson](https://cdn.mos.cms.futurecdn.net/56vqMYLDaKRHPhHZgbADFR-140-80.jpg)

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.

* Faiakes said:Well done to the gentleman but I'll have to ask.  
    
  Why, apart from financial difficulty, continue to use a 32 year old emmisions factory?  
    
  Isn't the weather terrible enough as it is?Parts are cheap and abundant for those old Cherokees. They're also easy for owners and independent mechanics to maintain. No need to visit a dealership or buy an entire assembly of things to repair something. Registration (possibly historic) and insurance should be significantly cheaper too. They're perfect if you don't drive often or for long distances, and they also excel at driving through/over difficult conditions. Just beware the noise, uncomfortable seats, and neverending battle against rust. Reply
