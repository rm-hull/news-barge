---
title: '''The attacks we found only scratch the surface of what is possible'': Experts
  say so-called ''Proactive SIM'' cards can hijack smartphones, IoT devices and even
  EV chargers'
source_url: https://www.techradar.com/pro/security/the-attacks-we-found-only-scratch-the-surface-of-what-is-possible-experts-say-so-called-proactive-sim-cards-can-hijack-smartphones-iot-devices-and-even-ev-chargers
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-18T20:36:13Z'
published: '2026-08-18T00:00:00Z'
description: Standardized SIM command from the modem era lets a hostile card run code
  inside an EV charger
image: https://cdn.mos.cms.futurecdn.net/uLTVZ33PJNJAQnchjt5Ngn-2560-80.jpg
---

![SIM card going into an iPhone](https://cdn.mos.cms.futurecdn.net/uLTVZ33PJNJAQnchjt5Ngn.jpg) 

- **Researchers find a standardized SIM command is exposed on nine of 26 tested devices and used it to achieve code execution on a commercial EV charger**
- **The exposure is concentrated in machine-to-machine hardware rather than phones, affecting six of eight cellular modules but only three of 18 handsets, with no iPhone or Pixel among them**
- **Every attack requires the attacker to already control the SIM, and while Qualcomm has produced a hardened configuration disabling the interface by default, no vendor had published a public advisory yet**

A malicious SIM card can instruct the device it sits in to run commands of an attacker's choosing, and on the cellular modules embedded in electric vehicle chargers, industrial routers, and car telematics units, essentially allowing it to take the entire device over.

Researchers from the University of Birmingham and the German security firm Fuzzware demonstrated this against a commercial Autel EV charger, achieving code execution driven entirely SIM card-issued commands.

## One malicious SIM card to rule them all?

The work focuses on a standardized feature called Proactive SIM, which as a feature, is not malicious; it's a standard in a cellular specification that lets a SIM push commands to a device rather than acting as a passive identifier for one's identity on a network.

The problem is one specific command in that set, RUN AT, which asks the modem to execute an AT command, the modem control language dating to the 1981 Hayes Smartmodem that every vendor has since extended with its own additions.

The support extender essentially gives a SIM module its own general-purpose console on devices that lack safeguards to prevent such an attack.

Tomasz Piotr Lisowski and Dr Marius Muench of Birmingham, working with Fuzzware's Kristian Covic, built a toolkit called CATana to find out what a hostile card could do with that console.

The team tested 26 devices, 18 smartphones and eight cellular modules, and found the SIM AT interface exposed on nine of them. The exposure is overwhelmingly concentrated in machine-to-machine hardware: six of the eight modules accepted the command, compared with just three of the 18 phones: the Oppo Find X5, the Oppo Reno 14 F 5G, and the Asus Zenfone 9. This makes it not exactly a Simjacker-esque exploit but still one that needs to be taken seriously.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

All nine devices that accepted the command run a Qualcomm chip or modem, but five others that do were not vulnerable to the attack. The researchers first shared the reports with Google, Oppo, Quectel, Semtech, and Qualcomm in March 2026, and with the GSMA in May. Qualcomm has since built a hardened configuration that switches the interface off by default, which the researchers say will be the default on future devices.

The attack vector, however, is limited because, to leverage it, the attacker must already control the SIM itself. Knowing a victim's contact number is not enough; the attacker needs physical access to the SIM slot. The exploit is real and concerning, but it has limited utility compared to a remote one for smartphones.

The IoT side is more concerning, however: unattended equipment with an accessible SIM tray can now potentially be exploited, and physical swaps might be easier than with something more personal, like one's personal phone. The card essentially talks to the equivalent of a Linux computer, one that the paper calls a rich attack surface for hostile SIM cards.

For now, the irony is that while modern smartphones have largely retired the surface this attack vector exploits, the machine-to-machine world has not, and the equipment least likely to receive a firmware update is the equipment most exposed currently.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Rahim Amir](https://cdn.mos.cms.futurecdn.net/9xKZFBamtEZKSChRvywbPB.png)

Rahim Amir is a UAE-based tech writer who enjoys building PCs as much as he enjoys writing about them. He has been professionally writing about PC hardware since 2023, focusing on buyer’s guides, hardware reviews, and sponsored content and features related to tech.

Having built hundreds of gaming PCs and being an avid gamer in his spare time, Rahim tends to have stronger opinions about hardware than most. This is particularly on display when he gets his way with powerful, but minimalistic RGB builds even as Small Form Factor (SFF) PCs come a close second.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
