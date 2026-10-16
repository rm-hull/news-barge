---
title: '''Remarkably close to the minimum permitted by physics'': this superconducting
  memory bit runs at an estimated 5x the limit, but at -269°C the fridge shrinks its
  claimed million-fold edge over today’s chips considerably'
source_url: https://www.techradar.com/pro/remarkably-close-to-the-minimum-permitted-by-physics-this-superconducting-memory-bit-runs-at-an-estimated-5x-the-limit-but-at-269-c-the-fridge-shrinks-its-claimed-million-fold-edge-over-todays-chips-considerably
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-16T23:34:22Z'
published: '2026-10-16T00:00:00Z'
description: A single superconducting whirlpool can flip a bit for about 5x the energy
  physics demands
image: https://cdn.mos.cms.futurecdn.net/4ARu4ZX7vVKepMN6WsZgUm-1280-80.jpg
categories:
- Technology & Software
- Science
people:
- Rolf Landauer
- Yonathan Anahory
locations:
- Bechhoefer
organisations:
- Ehrich
- Hebrew University
- Hebrew University of Jerusalem
- IBM
- Landauer
- Nature Communications
- Proesmans
- TechRadar Pro
---

![Quantum computing](https://cdn.mos.cms.futurecdn.net/4ARu4ZX7vVKepMN6WsZgUm-1280-80.jpg)

* **Hebrew University physicists estimate a single superconducting vortex can act as a memory bit at about five times Landauer's limit, at 4.2 kelvin**
* **The fivefold figure is a simulation-based estimate anchored to continuous-drive measurements, not a measured erasure, however**
* **The release's million-fold edge over conventional computers disregards refrigeration costs**

Every time a computer erases a bit, it pays an energy toll that physics will not waive; IBM physicist Rolf Landauer pinned down the minimum in 1961: kT ln 2, a figure that scales with temperature and works out to about 2.9 zeptojoules at room temperature.

No real chip comes close, making that gap a favorite target as computing's electricity bill keeps climbing.

Physicists at the Hebrew University of Jerusalem now say they have come within about five times of that floor using a single superconducting vortex, a nanoscale whirlpool of electrical current.

## Storing a bit in a whirlpool might be a slightly controversial play

The work, published in *Nature Communications* on September 24 and publicized in a university release on October 11, is a clever measurement, but it has limitations: the device works only at liquid-helium temperatures, and one of the paper's three peer reviewers has opposed the final version.

In a thin superconducting film, a magnetic field can punch through in tiny tubes, each ringed by circulating current and carrying one quantum of flux, and these vortices snag on defects.

The team, led by Yonathan Anahory, used a 55-nanometer niobium film patterned into a strip 10 micrometers wide and cooled to 4.2 kelvin. Sweeping a steady current through the strip nudged individual vortices into spots where the film's natural disorder offers two neighboring resting places only a few nanometers apart. The positioning matters here, acting effectively as a store of value: left or right becomes zero or one.

They then rocked each vortex with an alternating current and tracked it with a SQUID-on-tip microscope, a magnetic sensor built onto a tapered glass probe. The part of the motion that lags behind the push reveals how much energy is lost each cycle.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Anahory said the result puts the bit at roughly five times Landauer's limit, “bringing it remarkably close to the minimum permitted by physics.” The release covers the energy as measured for the actual test, not the cooling aspect, which could significantly reduce the efficiency story here.

The paper adds another caveat here: Its abstract concedes that “our experimental method requires a steady sinusoidal drive incompatible with Landauer’s erasure protocol” and attributes the near-limit figure to numerical analysis.

The lab measured dissipation while vortices were wiggled back and forth continuously; the cost of a true erasure, forcing a bit of unknown value into a known state, was estimated with simulations anchored to that data. The fivefold number is the authors' estimate for a working bit driven at 150 kHz, spelled out in their replies to reviewers.

This has, however, spurred a peer review fight, also published by Nature Communications, which lists the unusually blunt referee reports alongside the paper.

Reviewer #2 rejected the first draft, said the second could run only with extra experiments, and recommended against the final version, opening with “Authors write that they measure work. It is not true.” The reviewer argued that force, displacement, and work were estimated or inferred rather than observed, and asked for two sanity checks: show the vortex being pushed into one well and staying there, and show its spontaneous hopping changing with temperature, as thermal activation predicts.

The authors declined both, citing scanning drift that limits static imaging to about 20 nanometers and noting that changing temperature also reshapes the pinning landscape.

Reviewer #3 backed publication, calling the work original and sound and warning that the extra experiments could delay it indefinitely. Reviewer #1 judged the technique ill-suited to erasure at useful speeds and encouraged a more modest title.

## Speed is the tradeoff

Not only is the cost of cooling unaccounted for, with real-world refrigeration costs not being factored in, but the bigger problem is also speed. Landauer's limit is only reachable if you take your time, and work by Proesmans, Ehrich, and Bechhoefer shows that the extra cost of erasure rises as operations speed up.

The Hebrew University estimate applies at 150 kHz, or essentially one operation every 6.7 microseconds, while superconducting logic chips were clocked at 6 GHz more than a decade ago.

Going slower does not help either. By the authors' own noise data, the two wells central to the near-limit result let the vortex hop on its own roughly 3,000 to 7,000 times a second at 4.2 K.

The authors argue that this is fine as long as operations run much faster than the hopping. But it means the most efficient wells hold information for well under a millisecond, and the paper does not show a single well that is both near the limit and able to keep data for long.

The tradeoff, therefore, is one between speed, cost, and durability, and given that the use case is data storage, it is a tough call to make. Vortex memory is not entirely new; the Hebrew University contribution is energy accounting, and its claim to a first is narrow, though it uses a single vortex.

The Hebrew University team has produced a careful, somewhat contested estimate of how cheaply a single vortex can be shuffled between two spots, and a reminder that sitting close to the physical limit and being efficient at the wall socket are very different things.
