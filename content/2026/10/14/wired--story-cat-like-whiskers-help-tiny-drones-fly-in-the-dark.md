---
title: Cat-Like Whiskers Help Tiny Drones Fly in the Dark
source_url: https://www.wired.com/story/cat-like-whiskers-help-tiny-drones-fly-in-the-dark/
source_site: Wired
source_slug: wired
scraped_at: '2026-10-14T11:48:31Z'
published: '2026-10-14T00:00:00Z'
description: 'Researchers took lessons from nocturnal animals to help rescue drones
  overcome a key challenge: flying in the dark.'
image: https://media.wired.com/photos/6ace7f14e7efb271b8268bc8/191:100/w_1280,c_limit/2026_Q3_Web_TUDelft_Drones_0182.jpeg
categories:
- Technology & Software
- Science
people:
- Chao-Shan Ye
- Salwa Hamaza
locations:
- Netherlands
organisations:
- Delft University of Technology
---

After a disaster like a landslide, an earthquake, or a major fire, rescue workers have to locate survivors as soon as possible, and they are increasingly using drones for this critical task—especially ultra-compact drones that can fit into the crevices of a collapsed structure. There are, however, some serious limitations to the technology.

Weighing less than a stick of butter, ultra-compact drones don’t have as much compute or power capacity as larger models, and this restricts the power of their sensors. That means if a building is filled with smoke or the disaster happens at night, the drone’s cameras and lidar will cease to function. Even a clear pane of glass can be an obstacle the drone might not sense.

Now, a research team at Delft University of Technology in the Netherlands—drawing inspiration from the whiskers of nocturnal animals—has developed a lightweight, tactile sensor for drones to navigate even when they can’t “see.” Some nocturnal animals, like mice and to some extent cats, can explore their surroundings using just the sensations of the environment around them on their whiskers, enabling them to move without vision. The research team wondered whether drones could do the same.

In the world of drone development, tactile navigation is a novel concept that comes with its own challenges. “For tactile sensing to work on drones, it needs to be lightweight, low-latency, and low-power,” Salwa Hamaza, a professor at Delft University of Technology, explained in a press release. Luckily, nature already did some of that innovating.

The “whiskers” Hamaza and her team crafted for the drone consist of delicate wires made of nickel-titanium, each measuring 0.4 millimeters in diameter—about the thickness of four sheets of paper. The antennae, however, were longer than the drone itself. To a palm-sized drone, the researchers attached two whiskers, each nearly 8 inches long with three small pressure sensors at the base. These can assess the bending of the wires, from which the drone estimates its distance from and position in relation to nearby barriers. All calculations necessary for this navigation are processed by a microcontroller onboard the drone, without relying on an external computer.

It may not sound too complicated, but even determining the angle at which to mount the wires was a challenge. Animals that navigate via whisker generally do not fly. Having a long protrusion, even if very light and delicate, can make the drone unstable. When moving along a wall, the researchers saw that resistance from the whisker could cause the drone to rotate and crash.

The researchers compared a total of 72 flights, testing six different angles at three different speeds. The drone flew without major incident when the whiskers were mounted at 30 degrees, 45 degrees, and 60 degrees. Of these, the 45-degree angle was adopted because it resulted in the least deviation in the drone’s orientation. They also took into account the fact that a 60-degree angle reduces the forward sensing range.

The researchers also encountered several hurdles in processing the information taken in by the whiskers. One was distinguishing between actual contact signals and disturbances caused by the drone itself, such as vibrations from the propellers. Even when filtering this noise out, about 38 percent of the drone’s detections were false positives.

The issue seemed to be drift, a phenomenon where sensor readings gradually shift over time. The research team, therefore, developed a correction algorithm that continuously estimates the trend of drifts over time—based on sensor readings when the drone is not touching anything—while in flight. When combined with the filter, false positives reportedly dropped to 0 percent.

These tests were largely done in an environment with three transparent walls arranged in a row. Whenever the tactile sensor touched a wall surface, the drone flew parallel to the wall, maintaining a distance of 60 to 100 millimeters from the surface until it reached the edge. The drone was even able to navigate when the wall was at an angle to it, something a drone with laser sensors would not be able to do.

However, in a real-world situation—like the rubble of a disaster—obstacles are not so neatly arranged. Even in your average room, a drone following a wall could easily get stuck in a corner or overlook barriers to the side. The researchers, therefore, encoded an exploration method that prioritizes moving through unexplored areas by probabilistically estimating the shape of walls. Using this method, the drone successfully found a 2.5-foot-wide exit in a small room with glass walls in 90 percent of tests.

And there is room for improvement, figuratively and literally, given that this touch system only uses a small fraction of the drone’s 192 KB of memory. “We wanted to show that touch does not have to come at the cost of size or computational power,” Chao-Shan Ye, a doctoral student at Delft University of Technology, added in the press release. “Our entire tactile perception pipeline runs onboard using just 34 KB of memory, allowing a tiny drone to sense and respond to its environment in real time.”

*This story originally appeared on* WIRED Japan*and has been translated from Japanese.*
