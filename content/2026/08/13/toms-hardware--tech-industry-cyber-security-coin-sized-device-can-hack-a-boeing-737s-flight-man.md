---
title: Coin-sized device can hack a Boeing 737’s Flight Management Computer, mess
  with takeoff weights, or even divert an aircraft — gadget connects to an easily
  accessible port that overrides commands from the pilots, uses in-flight Wi-Fi
source_url: https://www.tomshardware.com/tech-industry/cyber-security/coin-sized-device-can-hack-a-boeing-737s-flight-management-computer-mess-with-takeoff-weights-or-even-divert-an-aircraft-gadget-connects-to-an-easily-accessible-port-that-overrides-commands-from-the-pilots-uses-in-flight-wi-fi
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-13T13:39:09Z'
published: '2026-08-13T00:00:00Z'
description: While it does not let hackers control the plane remotely, it could potentially
  confuse pilots and add to their workload while in-flight.
image: https://cdn.mos.cms.futurecdn.net/iDhuQoouJooKPrfFBcrGQ5-1920-80.png
---

![a Boeing 737 taking off behind an airport security fence](https://cdn.mos.cms.futurecdn.net/iDhuQoouJooKPrfFBcrGQ5.png) 

A group of researchers from the University of California San Diego (UCSD) and Oberlin College have developed a tiny device about the size of a coin that directly attaches to an external port on a Boeing 737 that connects to its Flight Management Computer (FMC) and Multipurpose Control Display Unit (MCDU). According to *Wired*, this gadget, which goes into one of the ports that aircraft mechanics use to test and diagnose avionics, is small enough to fit under its dust cap and go unnoticed during routine inspections. It then overrides the signals between the MCDU — the terminal in the cockpit that allows pilots to see and input data — and the FMC, the actual computer that controls the plane’s navigation, autopilot, performance calculations, and more.

The idea began when researchers were experimenting with hacking cars remotely in the mid-to-late 2010s, when they wondered if aircraft could be vulnerable to these types of attacks as well. Since an entire commercial aircraft is quite expensive, the group settled on looking for bargain-bin used aircraft parts until they were finally able to build a complete avionics stack to do their experiments on. Another UCSD professor, Aaron Schulman, was working on a different research project about credit card skimmers when the group realized that the communication bus that some skimmers were tapping into to steal payment information could potentially work similarly on a jet. “We realized that it's a reasonable threat for someone to plug a device into a bus and read stuff off of it and potentially even gain control of it,” Schulman told *Wired*. “We were like, ‘Wait a minute, we’ve got to rethink everything.’”

This was where the researchers discovered that a port in one of the Boeing 737’s two Electronics and Equipment (E&E) bays, located either in front of or behind the nose wheel well, connected to a bus that carried the data between the FMC and MCDU. This port, typically used for testing and diagnostics, isn’t protected by anything except for a dust cap and could easily be accessible by anyone authorized to work on or be around the aircraft. What’s more concerning is that the device can connect to the internet via in-flight Wi-Fi, allowing the researchers to tap into the plane’s avionics remotely.

Some of the changes they were able to make included intercepting, altering, and spoofing data and commands that go between the FMC and MCDU. This includes changing the outside air temperature readings and the aircraft weight inputted into the system, which could mess with the aircraft’s takeoff performance. If the temperature that the FMC has is higher than what the MCDU shows, or if the weight is lighter than what is actually measured, then the engine power set that the FMC will set for the takeoff might not be enough to get it off the ground.

This is actually the biggest threat to aircraft, as incidents of mistyped takeoff weight (by 100 tons) have resulted in tail strikes for LATAM 8073 in 2024 and Emirates 407 in 2009. A more egregious accident happened in 2004, when the crew of MK Airlines 1602 typed the empty weight of their Boeing 747 instead of its actual weight, resulting in the plane striking an earthen berm and causing it to disintegrate and crash into the ground. However, these events have caused the industry to implement stricter measures to prevent these crashes from happening again, including independent computations on their electronic flight bags (EFBs) and warning messages on the Electronic Flight Display (EFD), which is independent of the MCDU.

Another thing that a potential attacker can do is to silently change the plane’s flight plan, causing it to divert from its intended routing. They can do this by making minor changes that might be imperceptible to the pilots, causing the flight to go astray over time. Despite these threats, pilots are trained to deal with conflicting data from the MCDU and override the FMC as necessary. Incidents in the past, like the disappearance of MH370, have ensured that multiple systems exist so that a malfunctioning or compromised FMC will not lead to disaster. For example, an aircraft deviating from its assigned route and altitude will be contacted by ATC, as we have seen in this small aircraft crash that began when the pilots were confused by GPS jamming.

Because of these safety layers, Boeing told *Wired*, “Our technical experts are confident that the layers of protection in place on the airplane, including within the system design and the operating environment, provide sufficient mitigation to significantly limit the feasibility and risk of real-world attacks.” Still, it doesn’t mean that aircraft manufacturers should just ignore this threat. The researchers initially suggested permanently blocking the service port, followed by better isolation of electrical systems, or the addition of cryptography to prevent a device such as this from spoofing the plane’s systems. However, they also feared that Boeing would not do anything, as major changes like this are expensive and could take years to implement. We see this in some aircraft that still carry passengers or freight to this day but are kept updated through 3.5-inch floppy disks.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Jowi Morales](https://cdn.mos.cms.futurecdn.net/gM7E2WSDg2wgCFoaDPz9yK.jpg)

Jowi Morales is a tech enthusiast with years of experience working in the industry. He’s been writing with several tech publications since 2021, where he’s been interested in tech hardware and consumer electronics.
