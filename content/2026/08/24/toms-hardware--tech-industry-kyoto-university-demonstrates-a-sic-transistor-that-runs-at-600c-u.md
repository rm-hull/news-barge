---
title: Kyoto University builds transistor that survives 600C temperatures, compatible
  with standard fabs — Standard ion implantation and bottom-gate design fix leakage
  and voltage drift
source_url: https://www.tomshardware.com/tech-industry/kyoto-university-demonstrates-a-sic-transistor-that-runs-at-600c-using-standard-ion-implantation
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-24T11:48:23Z'
published: '2026-08-24T00:00:00Z'
description: The bottom-gate JFET holds its threshold voltage to within 0.1V at 400°C.
image: https://cdn.mos.cms.futurecdn.net/YdZbVjBsghJp5q9fsqEwpT-1920-80.png
---

![Kyoto University demonstrates a SiC transistor that runs at 600°C using standard ion implantation](https://cdn.mos.cms.futurecdn.net/YdZbVjBsghJp5q9fsqEwpT.png) 

A research team at Kyoto University has built a silicon carbide (SiC) transistor that operates at 600°C (873 K) using ion implantation, the doping step used across commercial chip fabs, and cut the gap between its designed and measured threshold voltage to under 0.1V at 400°C, down from more than 2V in the conventional layout. The work, announced earlier this month by Mitsuaki Kaneko, Shunya Shibata, and Tsunenobu Kimoto and published in *APL Electronic Devices*, pairs a bottom-gate transistor with a double-well isolation structure to keep an ion-implanted SiC junction field-effect transistor stable at temperatures where silicon stops working above roughly 250°C.

The bottom-gate layout puts the gate electrode beneath the channel, which captures the dopants that scatter deeper than intended during implantation, a channeling effect that had thrown conventional top-gate JFET thresholds off by more than 2V. With the channeling tail compensated, the design-to-measured threshold voltage gap dropped to under 0.1V at 400°C.

The double-well structure isolates each device inside a pn junction instead of leaning on the semi-insulating SiC substrate underneath, which loses its insulating behavior as it heats and bleeds leakage current through the wafer. Kaneko's group reported the remaining leakage sits close to the theoretical floor set by SiC's own material properties, so there's little room left to improve it at the device level.

In contrast, NASA Glenn Research Center has run SiC JFET integrated circuits carrying more than 175 transistors for over a year at 500°C in air, and 60 days on a simulated Venus surface at 460°C and 9.3 MPa with no shielding, per the agency's published testing. Those chips are built from epitaxial JFET-resistor devices on a bespoke process. The Kyoto researchers reached a higher device temperature through ion implantation, a method already standard across mainstream fabs, which fits existing mass production.

SiC is already scaling as a power-device wafer material, but high-temperature logic is a separate and far smaller niche. It isn't the only wide-bandgap material chased for these conditions either, with researchers recently showing devices that hold up from 500°C down toward absolute zero in other compounds.

The transistor is normally-on, so it conducts with no gate voltage applied and draws standby power. Efficient logic needs complementary pairs built from normally-off devices, which this isn't. Kimoto's group has already demonstrated complementary SiC JFET logic gates at 350°C, and its next step is to design normally-off devices in the new structure to build low-power complementary circuits. Long-duration reliability at temperature and heat-tolerant packaging are just two challenges the researchers will need to overcome before any of it reaches a gas turbine, or Venus.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Luke James](https://cdn.mos.cms.futurecdn.net/C4FAi2KzwaGLUrBqzX5aBM.png)

Luke James is a freelance writer and journalist. Although his background is in legal, he has a personal interest in all things tech, especially hardware and microelectronics, and anything regulatory.
