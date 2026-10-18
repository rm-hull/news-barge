---
title: UCLA researchers built a $400 humanoid robot around cheap phone technology
source_url: https://www.techradar.com/pro/phonebot-uses-an-old-usd50-android-smartphone-brain-with-its-cameras-as-eyes-tech-frankenstein-is-an-open-source-humanoid-robot-platform-for-makers
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-18T20:37:36Z'
published: '2026-10-18T00:00:00Z'
description: This open-source humanoid robot walks, tracks people, and gets back up
  using inexpensive hardware and a smartphone instead of dedicated sensors
image: https://cdn.mos.cms.futurecdn.net/NrNz34KY7yBu3XmCiyowEg-1920-80.png
categories:
- Technology & Software
- Science
people: []
locations:
- Los Angeles
organisations:
- PhoneBot
- TechRadar Pro
- UCLA
- University of California
---

![PhoneBot, a compact humanoid robot that reuses cheap smartphones for sensing and computing.](https://cdn.mos.cms.futurecdn.net/NrNz34KY7yBu3XmCiyowEg-1920-80.png)

* **PhoneBot uses cheap Android smartphones for vision, sensing, and walking control**
* **UCLA researchers built a humanoid robot with approximately $400 in hardware**
* **Four Android phones handled PhoneBot’s core sensing and computing tasks**

Researchers at the University of California, Los Angeles (UCLA), have developed PhoneBot, a compact humanoid robot that reuses cheap smartphones for sensing and computing.

The open source platform costs approximately $400 for its robotic hardware, excluding the phone, making it considerably cheaper than several existing small humanoid research systems.

PhoneBot stands 483 mm tall, weighs 1.8 kg, and uses 13 servo motors to control its legs and rotating torso during movement.

## Old smartphones handle vision, computing and robot control

Instead of requiring dedicated cameras, motion sensors and an expensive onboard computer, PhoneBot relies on the smartphone's existing hardware for these functions.

Its camera tracks people, while the built-in inertial measurement unit supplies motion information that helps the robot maintain balance and execute learned walking movements.

A separate computer inside the robot handles motor communications, receiving wireless commands from the smartphone over Wi-Fi and translating them into joint movements.

The robot has six actuated joints per leg, covering the hips, knees, and ankles, alongside another joint that rotates the torso and mounted smartphone.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

This arrangement lets the camera turn toward people without requiring the robot to rotate its entire body, supporting tracking and other vision-based interactions.

The researchers tested four Android phones, including an older Honor 9 released in 2017 and three inexpensive handsets costing approximately $50 to $80.

All four devices supported the application's core functions, including motion sensing, walking control, visual detection and human interaction, although certain features differed between models.

The application runs locomotion policies through TensorFlow Lite, while the phone's camera supports person detection and pose estimation, alongside other perception functions.

## Training helps balance walking and reduces hardware costs

The team trained PhoneBot's walking controller using reinforcement learning in simulation, rewarding desired movements while penalizing unstable posture and excessive motor loading.

Early experiments produced uneven walking patterns, with the robot relying disproportionately on one leg, prompting researchers to introduce mirrored training samples.

This method effectively teaches the controller using corresponding left and right movements, improving gait symmetry without requiring additional simulated physics steps.

Across five independent training runs, mirrored learning reduced joint-angle symmetry error from 0.254 radians to 0.003 radians during subsequent evaluations.

The researchers also measured left-right torque imbalance falling from 0.205 to 0.034, while mechanical-power imbalance declined from 0.339 to 0.040.

Physical demonstrations included walking, recovering from a face-down position, and directing the smartphone camera toward people without continuously turning the robot's feet.

PhoneBot remains limited by its low-powered servos, which restrict the weight it can carry and the dynamic movements it can perform reliably.

Its current walking controller was trained on flat ground, while the platform lacks arms for manipulating objects, leaving uneven-terrain mobility unresolved.

This is an open-source project so researchers can reproduce the platform, modify its components, and investigate smartphone-based robotics.

The research is currently published on arXiv, an online repository where researchers share scientific papers before or alongside formal peer-reviewed publication.
