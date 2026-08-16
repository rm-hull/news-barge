---
title: '‘Groundbreaking technology often enters the market at a premium before scaling’:
  Touch-sensitive e-skin could soon be commonplace in robotics'
source_url: https://www.techradar.com/pro/groundbreaking-technology-often-enters-the-market-at-a-premium-before-scaling-touch-sensitive-e-skin-could-soon-be-commonplace-in-robotics
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-16T12:56:56Z'
published: '2026-08-16T00:00:00Z'
description: Electronic skin could give robots the sensation they’ve been missing.
image: https://cdn.mos.cms.futurecdn.net/oKL6AAKzCE6tNmSqKv7ZoM-1920-80.jpg
---

![Robot run at 2025 Humanoid Half marathon](https://cdn.mos.cms.futurecdn.net/oKL6AAKzCE6tNmSqKv7ZoM.jpg) 

Despite mammoth advanced in artificial intelligence and computer vision, and a slew of humanoid robots either being piloted or hitting parts of the market, there’s still one major challenge that machines need to overcome.

It’s tactility, sensation, knowing how to hold an object. Picking up a strawberry, for example, a robot might not know how much pressure to apply, whether it’s secure, slipping, or about to be crushed. It’s something that we humans can feel through our skin, but it’s much harder to replicate on a machine level.

But it’s a work in progress, because there are companies out there like Touchlab who are working to give these skin-like characteristics to robots in a bid to make them more useful around the home, in care or in manufacturing. And it’s a lot more complex than we could ever imagine.

In Touchlab’s instance, it actually relies on quantum tunnelling technology to measure pressure, force and direction through a material that’s thinner than human skin, and with response times of less than a millisecond.

## E-skin technology exists, but deployment is a challenge

Although the solution is laid out on the table, moving from pilot to production is a different ball game. Durability, reliability, affordability, adaptability… they’re all considerations that stand between theory and real-world use cases.

Touchlab is addressing some of these concerns with off-the-shelf components that already exist for established platforms, using bespoke engineering only where necessary.

It’s also seeking to reduce latency by bringing processing to the edge so that the robot only transmits the data necessary for the task, being that the e-skin can detect and collect huge amounts of micro-data.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

With robots now rolling out across workplaces, care environments and, likely soon, homes, the ability to sense contact is becoming as important as the ability to see.

I speak with Touchlab’s team to understand how we can go from pilot to production in a realistic way.

- **Why do robots need the sense of touch, and how is Touchlab trying to achieve this?**

Computer vision allows a robot to predict, but touch is what confirms. Without tactile feedback, robotics remains trapped in a classic paradox: a machine can calculate complex equations in milliseconds, yet struggle to pick up a strawberry, handle soft medical instruments, or turn a valve without either crushing the object or dropping it. Without tactile sensing, a robot is functionally numb.

Touchlab solves this by developing biomimetic electronic skin (e-skin) that is actually thinner than human skin. Powered by quantum tunneling technology, our e-skin measures 3D forces, direction, and pressure in real-time. Crucially, it detects incipient slip—meaning the robot senses that an object is beginning to slip before it actually drops, enabling instantaneous, sub-millisecond grip adjustments just like the human nervous system.

- **I tried the technology at Future Lab... I tried to control a robotic arm with haptic feedback and it felt a bit clunky with cables and restrictions. Why is it so hard to make it smoother?**

Teleoperation is a classic engineering balancing act! First, there is a natural learning curve—controlling a high-degree-of-freedom robotic arm through a haptic glove isn't always intuitive on the very first attempt. It usually takes a bit of practice time and muscle memory to get the hang of the subtle force dynamics.

Second, running live demonstrations at high-traffic public events like Future Lab introduces specific hardware constraints. To ensure hundreds of visitors with completely different hand sizes can safely participate, setup requires universal-fit, heavy-duty tethered rigs and robust cabling.

Longer-term, our roadmap moves away from bulky, tethered operator suits entirely. By embedding our e-skin directly onto the robot and pairing it with onboard AI, the robot handles slip detection and dexterity autonomously—removing the need for an operator to wear restrictive physical gear.

- **Right now, the focus is on your proprietary robot fingertip tech. What's the plan going forward? Do you plan to license it or sell it as a finished product? How will you deal with various robotic architectures?**

Every robot platform is unique—whether it’s a humanoid deployed into hazardous industrial environments or a cobot assisting nurses in hospital wards. Touchlab is uniquely positioned to design, develop, and manufacture bespoke tactile devices tailored to specific OEM architectures.

At the same time, we offer scalable, off-the-shelf tactile components that are pre-integrated (both electronically and mechanically) with a wide variety of popular robot end-effectors. We provide volume-based discounts alongside strategic hardware loan and collaboration programs for robotics companies aligned with our vision. Over the past seven years, we have become extremely adept at rapidly building reliable integrations to suit diverse customer requirements.

- **What are currently the biggest technological barriers Touchlab is encountering? What does the end game look like, and will we ever digitize our largest organ, the skin?**

Our ultimate end game is for Touchlab’s tactile technology to become as ubiquitous as MEMS sensors— integrated into every commercial robot interacting with objects and humans. We envision full "finger-to-toe" tactile coverage powered by specialized edge computing and tactile orchestration software that mirrors the human somatosensory system.

Regarding barriers: the challenge isn't just technical; it's navigating western market adoption timelines for deeply transformative hardware. While digitizing human skin at scale presents manufacturing and durability hurdles, Touchlab can already deliver sensors matching or exceeding human-level spatial resolution, readout frequency, and sensitivity. The real task is packaging this capability into rugged, cost-effective formats ready for mass market deployment.

- **How is Touchlab designing the user interface to reduce operator fatigue during long shifts?**

We focus on shared autonomy. Rather than forcing a human operator to manually sense and adjust every micro-force vector, our e-skin handles low-level reflexes (like slip prevention) locally on the robot. The human operator directs higher-level tasks, while the robot's tactile system autonomously maintains optimal grip— dramatically reducing both physical strain and cognitive fatigue.

- **High-density e-skin generates massive amounts of data. How do you handle bandwidth and network transfer without overloading systems?**

High-density sensing does not automatically equal richer functional data, and often comes at the cost of hardware robustness. For our commercial products, we optimize spatial and temporal sensor density specifically for manipulation tasks, keeping data payloads lightweight.

For advanced R&D, we utilize distributed edge computing and are pioneering event-based asynchronous sampling in tactile sensing (similar to event-based vision cameras). Because our e-skin does not rely on heavy image-based data streams, it operates with extremely low latency and modest network bandwidth— making long-distance remote teleoperation surprisingly efficient.

- **Because e-skin can identify objects and textures, what protocols protect tactile data security and privacy?**

Tactile data on its own does not contain personally identifiable information. However, when integrated with video, audio, and LiDAR streams, multi-modal data security becomes critical.

For example, during our deployment with the Valkky medical robot in a Finnish hospital, all data transferred across hospital networks was strictly encrypted. Identifiable multi-modal data remained entirely on-premises on air-gapped storage devices and was fully anonymized before being processed for research or system analytics.

- **E-skin is often seen as a high-end luxury. What is your roadmap for driving down production costs for commercial robotics?**

Much like the early days of automobiles, groundbreaking technology often enters the market at a premium before scaling. While Touchlab is capable of producing full human-spec density today, deploying that level of complexity everywhere would make commercial robots cost-prohibitive.

Our strategy focuses on pragmatic engineering: delivering touch sensing tuned precisely to real-world task requirements at an accessible price point. We are actively collaborating with industry bodies to establish standardized performance metrics for tactile data, driving down manufacturing costs and making e-skin a standard baseline for all commercial robotics.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.* 

![Desire Athow](https://cdn.mos.cms.futurecdn.net/oEw3XiohQwun9z7gMxKzkB.jpg)

Désiré has been musing and writing about technology during a career spanning four decades. He dabbled in website builders and web hosting when DHTML and frames were in vogue and started narrating about the impact of technology on society just before the start of the Y2K hysteria at the turn of the last millennium.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
