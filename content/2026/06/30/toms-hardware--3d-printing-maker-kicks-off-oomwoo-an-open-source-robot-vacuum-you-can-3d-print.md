---
title: Oomwoo is a new open-source robot vacuum you can 3D print yourself, sidesteps
  cloud security risks by running fully offline — project combines Raspberry Pi, 2D
  LiDAR, and a 3D-printed chassis
source_url: https://www.tomshardware.com/3d-printing/maker-kicks-off-oomwoo-an-open-source-robot-vacuum-you-can-3d-print-and-build-yourself
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-06-30T11:19:05Z'
published: '2026-06-30T00:00:00Z'
description: Raspberry Pi, ROS 2, 2D LiDAR, and a 3D-printed chassis, but no build
  instructions yet.
image: https://cdn.mos.cms.futurecdn.net/xHYaeGUrtwRYLr4vErMHoG-1920-80.jpg
---

![a smart vacuum being set up with a smart phone](https://cdn.mos.cms.futurecdn.net/xHYaeGUrtwRYLr4vErMHoG.jpg) 

Maker's Pet has launched oomwoo, an open-source robot vacuum that owners build themselves. The robot works by mapping the home with an inexpensive 2D LiDAR sensor and then navigating using ROS 2 and the Nav2 stack on Raspberry Pi, integrating natively with Home Assistant. It can be printed using a regular desktop 3D printer and runs entirely without the cloud, while the hardware, firmware, and software are all open under the Apache 2.0 license. Ilia O of Maker’s Pet is also developing oomwoo in public “from the first commit,” though the project is so early that it doesn’t have any build instructions yet.

Right now, oomwoo is at the request-for-comments stage, with the current v0 milestone covering a 3D-printed chassis, a ROS 2 Gazebo simulation, and LiDAR mapping with manual SLAM, and the compute choice between a Raspberry Pi 5, an ESP32 running micro-ROS, or both is still open. Planned deliverables run from the bill of materials and printable files to firmware and a custom PCB, with the first BoM targeted for around mid-July.

The project is structured so the community can build it in parallel: the robot is split into self-contained modules, and contributors claim one and submit work as a pull request. A convenience kit will be sold through Maker's Pet, but Ilia says that buying it won’t be a requirement, and every part can be sourced independently.

The usual route to a cloud-free robot vacuum starts with a robot you already own. Valetudo, maintained by Sören Beye since 2018 and also released under Apache 2.0, replaces a commercial vacuum's cloud connection with local-only control and Home Assistant integration. Installing it, however, means rooting the vendor firmware, which on many supported Dreame, Roborock, and Xiaomi models requires disassembly and voids the warranty, and also can’t be undone.

The inclusion of local control could be a boon for getting more tinkerers and enthusiasts on board with the vacuum, following several examples of robot-vacuum security failures over the last few years. At DEF CON 32 in August 2024, researchers Dennis Giese and Braelynn Luedtke showed that several Ecovacs models could be hijacked over Bluetooth to reach their cameras and microphones, with Giese telling *TechCrunch*the security was “really, really, really, really bad.”

Hijacked DEEBOT X2 units later shouted slurs and chased pets in several U.S. homes, and a token flaw in DJI's Romo line let one tinkerer reach roughly 6,700 vacuums worldwide, floor plans, and live feeds included. One owner went as far as reviving a remotely bricked vacuum with custom boards and Python to run it offline. oomwoo's reference design eliminates that attack surface, navigating on 2D LiDAR and bumper sensors with nothing pointed at the room.

  


*Follow**Tom's Hardware on Google News**, or**add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Luke James](https://cdn.mos.cms.futurecdn.net/C4FAi2KzwaGLUrBqzX5aBM.png)

Luke James is a freelance writer and journalist. Although his background is in legal, he has a personal interest in all things tech, especially hardware and microelectronics, and anything regulatory.
