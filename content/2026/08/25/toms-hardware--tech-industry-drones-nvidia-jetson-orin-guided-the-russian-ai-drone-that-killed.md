---
title: Nvidia Jetson Orin-guided Russian AI drone killed three civilians in Ukraine,
  forensic teams say — first documented case of civilian deaths caused by a Russian
  drone using fully autonomous targeting
source_url: https://www.tomshardware.com/tech-industry/drones/nvidia-jetson-orin-guided-the-russian-ai-drone-that-killed-three-civilians-in-ukraine-forensic-teams-say
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-25T13:07:42Z'
published: '2026-08-25T00:00:00Z'
description: The unencrypted module let Ukrainian investigators read the drone's terrain
  maps and targeting code.
image: https://cdn.mos.cms.futurecdn.net/YqyE7WKzDBtHaoJrTAM6zg-1920-80.jpg
---

![Nvidia Jetson](https://cdn.mos.cms.futurecdn.net/YqyE7WKzDBtHaoJrTAM6zg.jpg) 

A Russian Molniya drone carrying an Nvidia Jetson Orin module crashed and killed three civilians at a gas station in Zaporizhzhia last month after choosing its final target without a human pilot, according to a *New York Times* investigation that cites Ukrainian air defense commanders, drone experts, and the forensic team that examined the wreckage.

Kateryna Bondar, a senior fellow at the Center for Strategic and International Studies, told the paper it's the first documented case of civilian deaths caused by a Russian drone using fully autonomous targeting. The dead were Tetiana Bubynets, a 19-year-old accounting student, and two men aged 41 and 48.

Human operators launched the drone toward the gas station, per the report, but the final aim point was selected onboard by software trained to recognize objects such as propane tanks. The aircraft failed to clear an apartment building on its approach, struck a wall, and detonated near people sheltering below, rather than striking its chosen target.

The strike drone flew in a group of roughly half a dozen aircraft, none of which emitted radio traffic, Ukrainian air defense officials said. Modules recovered from this attack and from intact test drones carried no encryption, so investigators could examine both the terrain imagery loaded for visual navigation and the code specifying which object classes the drone had been trained to attack. "Machines are making decisions to strike," Col. Serhiy Minaiev, Zaporizhzhia's air defense commander, told the *NYT*. Russia is understood to have begun AI-guided test flights of the mass-produced, fixed-wing Molniya in May, after months of self-targeting trials with the V2U.

Nvidia confirmed to the *New York Times* that modules photographed in the recovered drones were Jetson Orin minicomputers, hardware that sells for a few hundred dollars. "Our Jetson Orin modules are consumer-grade products sold to students, developers, and startups for a wide range of beneficial applications," an Nvidia spokesperson told*Tom's Hardware*. "They are not available in Russia and are not designed for military purposes. Pre-owned Jetsons are available through many reseller channels. Although we cannot track products after they are sold, if we determine that any customer is violating U.S. export controls, we will take appropriate action."

Ukrainian investigators have now linked the Jetson Orin to four Russian weapon families. A teardown by Ukraine's GUR intelligence agency last June found one seated on a Chinese Leetop A603 carrier board inside the V2U loitering munition, in combat use since February 2025. Weeks later, a Ukrainian general said the module powered object recognition in the upgraded Shahed MS001, and earlier this month Ukraine reported the same silicon in the S-71M Monochrome cruise missile. Data-center AI accelerators fall under U.S. export controls; edge modules like the Jetson Orin, with variants starting at $249, don't.

Mykhailo Fedorov, Ukraine's recently ousted defense minister, told the *NYT* that Kyiv tested its own fully autonomous system against fuel storage and military equipment in occupied Crimea in recent months, and Ukrainian quadcopters killed Russian soldiers in autonomous mode as far back as 2024. In Zaporizhzhia, defenses now include roughly 240 miles of anti-drone netting and plastic sheeting propped at odd angles around propane tanks to throw off image recognition.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Luke James](https://cdn.mos.cms.futurecdn.net/C4FAi2KzwaGLUrBqzX5aBM.png)

Luke James is a freelance writer and journalist. Although his background is in legal, he has a personal interest in all things tech, especially hardware and microelectronics, and anything regulatory.
