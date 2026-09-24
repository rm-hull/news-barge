---
title: Researchers can make headphones leak audio through a wall, but the 30-meter
  claim has a few caveats
source_url: https://www.techradar.com/pro/security/researchers-can-make-headphones-leak-audio-through-a-wall-but-the-30-meter-claim-has-a-few-caveats
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-22T04:44:08Z'
published: '2026-09-21T00:00:00Z'
description: Encryption can't stop InjectEave because the audio leaks after it's been
  decoded, but it does have its limitations.
categories:
- Technology & Software
image: https://cdn.mos.cms.futurecdn.net/9ui8vuAvNqX2Bubaxvks8J-1920-80.jpg
locations:
- Baltimore
- Guangzhou
- Moscow
- US
people:
- Rahim Amir
organisations:
- Google News
- HK PolyU
- Hong Kong Polytechnic University
- Hong Kong University of Science and Technology
- InjectEave
- PC
- PCs
- RGB
- SFF
- TechRadar Pro
---

![Headphones](https://cdn.mos.cms.futurecdn.net/9ui8vuAvNqX2Bubaxvks8J.jpg)

* **HKUST (Guangzhou) and HK PolyU researchers' InjectEave beams a radio carrier at devices so their own circuits leak analog audio**
* **The leaked audio has already been decrypted by the device itself, making encryption offer no protection against such an approach**
* **The 30m headline needed a pricey amplifier pushing output to 10 W, while standard ranges of 1 to 6m were measured by detecting a test tone**

Researchers at the Hong Kong University of Science and Technology and the Hong Kong Polytechnic University have shown that everyday headphones, a desk phone, and a handful of smart-home gadgets can broadcast what they are doing simply by using a radio signal.

The technique, called InjectEave, was presented at USENIX Security 2026 in Baltimore, and multiple outlets have since covered the researcher's claim that the attack "can recover headphone audio from up to 30 meters away, including through walls".

The claim may be accurate, but it has limitations, including the need for specialized equipment that is often very noticeable in most settings.

## An impressive technical show with plenty of limitations in tow

Conventional electromagnetic eavesdropping waits for a device to leak. That works poorly for audio, because speech sits below 20 kHz while a device's wiring radiates efficiently only at megahertz or gigahertz frequencies.

InjectEave chooses to close the gap by transmitting a carrier signal at the target. According to the paper, nonlinear components such as amplifiers, analog-to-digital converters, switching MOSFETs, and power converters mix the secret signal onto that carrier, and the device's own traces and cables radiate the result back to a receiver.  
Because the leak happens in the analog path, after audio has been decoded, the project page states that "InjectEave is immune to digital defenses such as encryption, masking, and randomization." Encryption in any form on a wireless headset is irrelevant, since the attack directly targets the signal driving the speaker, not the radio link.

The team demonstrating this used a USRP B210 software-defined radio, two antennas, a Siglent spectrum analyzer, and a laptop to set up their proof of concept, which could, as they noted, "eavesdrop on the majority of these devices from over 2m away and through walls, with a maximum distance of 30m for recovering intelligible headphone audio".

This isn't the first time the technique has been used, even as the researchers have built on it considerably; the idea originates from "The Thing," a Soviet bug given as a gift to the US ambassador in Moscow in 1945, which was passively powered remotely as a listening device.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

InjectEve, however, does not involve planting anything; instead, it leverages existing work on interference-induced leakage and impedance-based backscatter, and distinguishes itself by recovering coarse digital data rather than continuous analog waveforms, allowing users to 'listen in' without added steps.

The same approach applies to wired headphones, which are also prone to leaking microphone audio; researchers concluded that their sound cards were the primary source of the leaks, which were being sent back over very short distances.

The threat is somewhat tempered by the fact that it can capture what users hear but, with wireless headphones, cannot hear what the user is saying. The attacker also has to transmit continuously and use a high-powered (10W) transmitter to reach the full 30-meter range, even though capturing and rendering speech is harder than the tones the test used to prove the approach worked.

The attacker also needs to know the target model and profile a matching unit first, although they managed to get a profile to transfer cleanly across three identical UGreen headsets, suggesting this might be easier than one would assume.

The researchers say they reported the findings to the affected manufacturers but, "as we have not yet received a response," withheld the table's frequencies and stripped injection control logic from their released code. One shouldn't be too hopeful, however, as no software update can fix an analog leak, and it is relatively limited in practical abuse cases.

![Google logo on a black background next to text reading &#039;Click to follow TechRadar&#039;](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg)

***Follow TechRadar on Google News***and** add us as a preferred source** * to get our expert news, reviews, and opinion in your feeds.*

![Rahim Amir](https://cdn.mos.cms.futurecdn.net/9xKZFBamtEZKSChRvywbPB.png)

Rahim Amir is a UAE-based tech writer who enjoys building PCs as much as he enjoys writing about them. He has been professionally writing about PC hardware since 2023, focusing on buyer’s guides, hardware reviews, and sponsored content and features related to tech.

Having built hundreds of gaming PCs and being an avid gamer in his spare time, Rahim tends to have stronger opinions about hardware than most. This is particularly on display when he gets his way with powerful, but minimalistic RGB builds even as Small Form Factor (SFF) PCs come a close second.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
