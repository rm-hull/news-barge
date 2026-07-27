---
title: Experts warn 2.2 million cars could be at risk of hijacking via Bluetooth
source_url: https://www.techradar.com/pro/security/experts-warn-2-2-million-cars-could-be-at-risk-of-hijacking-via-bluetooth
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-27T03:57:20Z'
published: '2026-07-27T00:00:00Z'
description: Worrying connected California carjack detected
image: https://cdn.mos.cms.futurecdn.net/UdHTZzTLLETcncr7PYcnoK-2560-80.jpg
---

![A hand over a concealed car door handle](https://cdn.mos.cms.futurecdn.net/UdHTZzTLLETcncr7PYcnoK.jpg) 

- **2.2 million vehicles are susceptible to a Bluetooth-based attack in the state of California**
- **The vulnerability is due to dealer-installed security systems**
- **Researchers at the University of California San Diego found that the Acrisure-built security devices all rely on the same secure key**

A vulnerability has been found in KARR and SWDS automobile security systems manufactured by Acrisure that enables remote control via Bluetooth. The vehicles had the security systems installed by car dealers in California, specifically as anti-theft and tracking devices. Thanks to this hack, however, it seems that vehicles can be unlocked, with some further control given to the attacker.

Researchers at the University of California San Diego found that the 2.2 million automobiles were purchased from Southern Californian dealers since 2017, although the secondary market means that the vehicles could be elsewhere in the US, and even as far afield as Japan.

Worryingly, the researchers also found a publicly-accessible database holding information about all vehicles with the security system equipped.

## How Bluetooth controls these cars

![2 Million Cars with Anti-Theft Systems Installed by Dealers are at Higher Risk of Theft - YouTube](https://img.youtube.com/vi/xS_4dNRGkoA/maxresdefault.jpg) 

The researchers determined that the automobiles were purchased from Honda, Toyota, Mazda, Ford, and Jeep dealerships, and the affected vehicles have the “KARR-SWDS” label on the driver-side window, with the anti-theft device mounted under the dashboard.

Usage is straightforward: a mobile app connects to the KARR security system over Bluetooth and includes functions such as locking and unlocking doors, controlling the horn, and flashing the headlamps. It can also prevent the car from starting, although this only works if it isn’t already running.

The problem is with the implementation, which the researchers discovered relied on the same secure key on the KARR security systems. Once cracked, all cars equipped with the same device were believed to be open to attack.

Changing the secure key isn’t an option, and neither is disabling the Bluetooth. Of particular concern is that researchers found that even if the buyer doesn’t pay for a subscription for the app and the KARR system, the hardware is still in place. Worse, it has the same access to the vehicle’s doors, ignition, horn, and headlamps.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

“Removing the devices is not trivial,” UCSD compsci PhD candidate and paper co-author Yibo Wei said in the report on the research (which is fully released in August). “You have to open up the dashboard and cut and reconnect the wires that are deeply intertwined with the car’s computers and ignition system.”

## The patch is in

Jerry Yu, also co-author, wrote “Instead of smashing a window to get access to a vehicle, thieves could simply connect remotely via Bluetooth to the device inside the vehicle, and make it unlock car doors.”

KARR has told media outlets that only vehicles installed “with certain Bluetooth-related components” are affected, and the company has issued a firmware update.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Christian Cawley](https://cdn.mos.cms.futurecdn.net/zBDYnjPnB2XPvhKbYX9Kuc.png)

Christian Cawley has extensive experience as a writer and editor in consumer electronics, IT and entertainment media. He has contributed to TechRadar since 2017 and has been published in Computer Weekly, Linux Format, ComputerActive, and other publications.

He currently heads up the team at smart home website Matter Alpha, and writes about retro gaming at Gaming Retro.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
