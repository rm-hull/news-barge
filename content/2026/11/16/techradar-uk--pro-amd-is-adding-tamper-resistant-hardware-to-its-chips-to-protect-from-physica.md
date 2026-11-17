---
title: AMD is adding tamper-resistant hardware to its chips to protect from physical
  attacks
source_url: https://www.techradar.com/pro/amd-is-adding-tamper-resistant-hardware-to-its-chips-to-protect-from-physical-attacks
source_site: TechRadar UK
source_slug: techradar-uk
description: AMD is building backside protection into the silicon
image: https://cdn.mos.cms.futurecdn.net/7Wnzu6tGp6ew9yyA3nEQk9-1200-80.png
published: '2026-11-16T00:00:00Z'
scraped_at: '2026-11-17T03:47:06Z'
categories:
- Technology & Software
people: []
locations:
- Silicon
organisations:
- AMD
- Altera
- Arm
- CEA-Leti
- CRC
- EPYC
- Electronics Journal
- FPGAs
- Intel
- Lattice
- SEV-SNP
- Starbleed
- TU Berlin
- TechRadar Pro
- Versal TR
- Worcester Polytechnic Institute
---

![AMD Versal Gen 2 chip](https://cdn.mos.cms.futurecdn.net/7Wnzu6tGp6ew9yyA3nEQk9-1200-80.png)

* **AMD's Versal TR adaptive SoCs bond a sensor die to the silicon backside that detects physical attacks and blocks boot if removed**
* **Post-quantum ML-DSA and SLH-DSA acceleration arrives after rivals Altera and Lattice already shipped post-quantum secure boot**
* **Samples are not due until the second half of 2027, and AMD itself says tamper-resistant does not mean tamper-proof**

AMD has unveiled a family of adaptive chips with their own built-in bodyguard.

The company's new Versal tamper-resistant devices bond a sensor-based protection die to the back of the main compute die, where it shields the silicon, watches for physical attacks, and stops the chip from booting if it is tampered with or removed.

The chips, specifically the 2VE3358TR, 2VE3558TR and 2VE3858TR, are all variants of the Versal AI Edge Series Gen 2 adaptive SoCs that AMD first unveiled alongside Arm in 2024, and will look to cater to the likes of defense systems, data center networking, financial technology and critical industrial infrastructure.

## A second die guarding the side that nobody watches?

One might ponder why the backside is suddenly important: most high-performance chips are flip-chip packaged, mounted face down, so the transistors sit against the package while the bare silicon substrate faces up.

Silicon is transparent to near-infrared light, so an attacker who removes the lid and thins the substrate can observe switching transistors through it, or fire a laser to inject faults, without ever disturbing the metal layers where traditional on-die mesh shields sit.

Electronics Journal notes that defending this surface has generally relied on board- or enclosure-level measures, such as active meshes and potting. AMD knows this terrain from the receiving end: In September 2026, an AMD security bulletin covering its older 7-series FPGAs described a researcher recovering partial bitstream plaintext via contactless optical probing of the die's backside.

AMD's response was somewhat blunt then: that kind of access is "outside the threat model" for those parts, and customers in high-risk deployments were advised to consider tamper-responsive enclosures, conformal coatings or potting.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

It was not the first such case in recent times: AMD's February 2026 bulletin on Leakback CRC, a paper that reconstructed full netlists by optically probing the same family's readback CRC circuitry, drew the same out-of-scope verdict. The 7-series has history here, too: the Starbleed flaw disclosed in 2020 broke its bitstream encryption in a way researchers said could only be fixed by replacing the chip.

Versal TR's answer is to move that protection inside the package; The protection die is attached using what AMD calls 3D active-on-active technology, meaning both stacked dies carry active circuitry rather than one acting as a passive cap, and it covers the entire backside of the device.

AMD's product page for the parts describes a full-die sensor array and "cryptographic binding" between the two dies. AMD has not explained that term, but it seems to imply that the shield is paired to its own compute die, so an attacker could not simply swap in a substitute.

AMD frames the pitch around consolidation; customers that need this level of protection today often build it in-house from enclosures, ASICs and other components, the company says, which adds cost, specialist engineering, verification work and the risk of a board re-spin.

Each TR part has a footprint-compatible standard counterpart that is available now, and the spec tables show identical logic, AI Engine and I/O resources on both, with backside protection and cryptographic binding as the only listed difference. Teams can develop on regular silicon and later swap in the TR device without rerunning synthesis or place and route.

AMD calls Versal TR the industry's first adaptive SoC or FPGA-based device with built-in protection against silicon backside attacks, a claim its footnote says rests on the company's own November 2026 analysis of competing parts.

In all fairness, backside shielding is not a new idea: CEA-Leti unveiled a backside shield for secure chips in 2017, a metal serpentine sandwiched in polymer that typically triggers data erasure when disturbed. What has held such approaches back is cost. Researchers at Worcester Polytechnic Institute wrote in 2024 that detection-based backside defenses are highly effective but expensive and highly customized. AMD's real contribution, if it delivers, is turning that into a catalog part.

The backside die might be the headline for most publications, but the TR parts also harden the front door. Versal already ships with tamper monitoring, and AMD's technical reference manual lists power-supply glitch detection, voltage and temperature alarms, and debug-port activity among its triggers.

## A persistent glitching problem as mitigation, not resolution rule the roost

The TR devices improve the existing glitch detector and add a new orthogonal one that also catches glitches that hit two voltage rails at once. This is somewhat warranted because voltage glitching has a somewhat proven track record against AMD silicon. In 2021, TU Berlin researchers used it to pull keys from the AMD Secure Processor in Zen-based EPYC chips, and in 2023 a team from the same university turned it on AMD's firmware TPM.

After the latter, AMD said it was "continually innovating new hardware-based protections in future products." Yet when researchers reported extending the technique to a Zen 4 Ryzen 8600G in 2025, AMD's bulletin stated that physical attacks, such as voltage fault injection, fall outside the threat model for the affected products.

The approach AMD has applied here, however, makes the chips tamper-resistant rather than tamper-proof, and the chipmaker is extremely explicit about its limitations. Its footnote states that "tamper-resistant" does not mean "tamper-proof," that the protection applies only to specified physical attack methods, and that the threat model and limitations are set out in product documentation, which the product page does not publicly link to.

Versal TR also sits awkwardly beside AMD's stance on its server chips. When researchers broke SEV-SNP with a sub-$50 DDR4 interposer called Battering RAM in 2025, both AMD and Intel maintained that their trusted enclaves are not designed to resist physical attacks, while the researchers said the work exposed "the fundamental limits of the scalable memory encryption designs" both companies use.

That position has held: in September 2026, AMD said a newer physical fault injection attack on DDR5 servers falls outside SEV-SNP's published threat model and that it "does not plan to assign a CVE or release mitigations." Nothing in this announcement changes the EPYC threat model.

For the defense, fintech, and infrastructure customers AMD is courting, the appeal is plain: an off-the-shelf part that could replace a custom potted assembly, with a development path that starts on silicon available today.

Whether the protection die holds up against well-funded labs with failure analysis equipment is a question only independent testing can answer. That testing cannot begin until samples arrive in the second half of 2027, by which point competing Altera and Lattice customers will have had post-quantum secure boot for about a year.
