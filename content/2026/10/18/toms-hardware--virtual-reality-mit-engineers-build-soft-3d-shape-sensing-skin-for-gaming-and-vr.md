---
title: MIT engineers build soft 3D shape-sensing skin for gaming and VR — tracks 3D
  movement and touch with sub-half-centimeter error
source_url: https://www.tomshardware.com/virtual-reality/mit-engineers-build-soft-3d-shape-sensing-skin-for-gaming-and-vr-tracks-3d-movement-and-touch-with-sub-half-centimeter-error
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-18T15:49:25Z'
published: '2026-10-18T00:00:00Z'
description: Although it still works with a few fibers cut, a garment would need many
  more, much thinner ones.
image: https://cdn.mos.cms.futurecdn.net/AoiE9uB5AeDWhPjLmoTh43-2560-80.jpg
categories:
- Technology & Software
- Hardware
people:
- Kaitlyn Becker
- Qifan Yu
locations: []
organisations:
- Get Tom's Hardware
- Google News
- I2C
- MIT News
- Shane Downing
- Tom’s Hardware
---

![Illustration of an arm in a sleeve striped with optical fibers, linked by lines of light to a wireframe of the sleeve’s shape.](https://cdn.mos.cms.futurecdn.net/AoiE9uB5AeDWhPjLmoTh43-1920-80.jpg)

MIT engineers have built a soft, wearable shape-sensing sheet with self-tracking movement that could be useful for controlling games, virtual reality, and physical therapy applications, reports *MIT News*. The technology, which leverages optical fibers to track the sheet’s own 3D shape, keeps its error below half a centimeter in lab tests. Qifan Yu, an MIT mechanical engineering graduate student on the team, put rigid-sensor designs at around 1 to 2 cm and called the result “at least on par with existing technologies.” The sheet also still works even when damaged, but the fibers remain thicker than ideal for garments.

The news follows a paper, “Toward fully soft and multifunctional shape sensing via optical waveguide arrays,” recently published in *Advanced Intelligent Systems*. It details that the waveguides respond to bending in both directions, “bi-directional,” with the array laid out to discern shapes. Combined fiber responses mean fewer sensing elements are needed, and that can also improve damage resilience. The fibers respond to pressure, so they can sense external force, such as a press on the forearm in a physical therapy demo.

Normally, a plain fiber, a transparent core inside a light-trapping cladding, will have less light reach the far end when bent; measuring the light output helps measure the bend. MIT’s changes here include using a flexible rubber core instead of glass, with black-dyed cladding. One side is roughened intentionally so that bending the fiber toward that side, or toward the opposite side, causes different amounts of light to be lost. This enables directional sensing.

Many such fibers are embedded in a silicone sheet, with an LED at one end of each fiber and a light sensor at the other. The sensing surface is fully soft, but the sheet doesn’t stretch as a whole. An external circuit board handles the data collection with an algorithm translating it into a full sheet and 3D shape. The 14 waveguides are each 160 mm long in two layers of seven, zig-zagged within a 16 x 16 x 0.5 cm silicone sheet. The electronics remain at the edge, including analog-to-digital converters that feed microcontrollers over I2C. The reconstruction runs in MATLAB about three times a second, a rate that includes sensor sampling, data logging, and plotting.

To pick the layout, the team first simulated sheets with different waveguide arrangements: it generated the light output each fiber would give for a known shape, ran those readings through the reconstruction algorithm to estimate a 3D shape, and compared the estimate with the known one. One zig-zag spacing pattern had the closest fit. In simulations, between 3 and 20 waveguides per layer were used at angles of 0 to 35 degrees on six target shapes, with 10% added noise, over 30 trials each. The researchers discovered that angling the waveguides improved accuracy more than adding additional ones.

Resilience was tested with a few fibers cut or disconnected, with the rest still able to reconstruct the overall shape. In simulation, the error stayed under 0.3 cm with up to three of the 14 waveguides disabled, and rose to about 1 cm or more from five on.

A real sheet was then built on the pattern findings and put to the test with diagonal folding. For accuracy, the sheet was laid over three 3D-printed molds of known shapes, with the metric being the root-mean-square distance between real and reconstructed surfaces: 0.37, 0.28, and 0.45 cm. The force sensing does not have a calibrated force reading to tell how hard, and this detection runs separately from the shape mode. Each wearable demo was done by one author on their own body, with a simpler scaling method for wrist and elbow angles, because stretching at those joints throws off the shape algorithm, with no comment on comfort.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Three 3D-printed molds above plots overlaying each target shape with the sheet&amp;rsquo;s reconstruction, labeled RMSE 0.37 cm, 0.28 cm and 0.45 cm](https://cdn.mos.cms.futurecdn.net/jmknUwScupLEMzR9xMsXFn-1200-80.png)

Yu said the setup targets fully soft sensing surfaces, so it’s potentially safer around people. Kaitlyn Becker, an MIT assistant professor of mechanical engineering and co-author, said the team hopes to build tools that help physical therapists track and quantify a patient’s progress over time, comparing sessions more precisely. Outside of this, the tech could also be used in virtual reality to mimic motion or could be used for the teleoperation of robots, or even just soft robots.

As thinner fibers would have a wider applicability, the researchers plan to target a thinner sheet first. The 1 mm thick fibers of today could get as thin as tens of micrometers, thinner than a human hair. A higher fiber count could then make for smart garments. They also suggested future work could focus on a faster solver rather than the general-purpose one in MATLAB, more waveguide layers and narrower waveguides for better detail with thinner sheets, a separate sheet to gauge force and shape simultaneously, and stretchable electronics.



*Follow* * Tom’s Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Shane Downing](https://cdn.mos.cms.futurecdn.net/Zosi9VrDytS9FkgJiHvc69-140-80.png)

Shane Downing is a Contributing Writer for Tom’s Hardware, covering consumer storage, PC hardware, and AI.
