---
title: Red Hat's open-source AI may become an all-important tool for astronauts
source_url: https://www.techradar.com/pro/nasa-and-red-hat-are-building-an-open-source-medical-system-to-diagnose-sick-astronauts-on-the-iss-could-a-star-trek-tricorder-be-next
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-04T19:12:39Z'
published: '2026-07-03T00:00:00Z'
description: The open-source tool turning astronauts into their own doctors during
  deep space missions far from Earth
image: https://cdn.mos.cms.futurecdn.net/Q7TKhesndya4sXxhv3cw6e-1920-80.png
---

![In this image, ultrasound procedures help provide for medical diagnoses on the International Space Station.](https://cdn.mos.cms.futurecdn.net/Q7TKhesndya4sXxhv3cw6e.png) 

- **NASA's AI medical tool works where Earth-based doctors simply cannot reach**
- **Deep space has no signal — so NASA built its own offline doctor**
- **RamaLama runs AI models the same way containers run software — predictably**

Astronauts aboard the International Space Station (ISS) currently rely heavily on Earth-based doctors whenever medical issues emerge hundreds of kilometres overhead.

That arrangement works reasonably well in low Earth orbit, where communication delays remain short enough for near real-time consultation sessions.

It becomes far less practical once crews travel beyond Earth orbit, where signals can take minutes rather than seconds to arrive.

## An AI doctor built to work without an internet connection

Researchers at NASA's Johnson Space Center in Houston are now testing a clinical decision support system called Crew Medical Officer Digital Assistant, or CMO-DA.

The system is designed to help astronauts diagnose and treat medical conditions during deep space missions, where real-time communication with Earth-based doctors could be limited or entirely impossible.

Powering it is RamaLama, a Red Hat-backed open source tool built to simplify how developers run and serve AI models across diverse hardware environments.

According to Red Hat, RamaLama treats AI models like container images, running them in isolated, security-first environments using Open Container Initiative-compliant containers that are portable and predictable across hardware.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

This approach allows the CMO-DA to perform what the team calls multimodal inference — processing both large language models for complex medical reasoning and Vision Language Models for image-based symptom analysis.

The system can therefore evaluate both written symptom descriptions and visual data without requiring any connection to a terrestrial cloud server.

That offline capability is not a convenience feature but a mission-critical requirement, since deep space communication delays make cloud dependency genuinely dangerous for crew health outcomes.

Testing is currently running on HPE hardware — specifically the terrestrial twin of the Spaceborne Computer already aboard the ISS — giving researchers a reliable Earth-based replica of the actual deployment environment.

By using open-source tools throughout, NASA researchers have built a system that is reproducible and auditable, which the team describes as essential for human safety in mission-critical environments.

## From Earth testing to the ISS and beyond

Once the terrestrial testing phase is complete, the CMO-DA will be demonstrated to NASA leadership for evaluation of further deployment aboard the International Space Station.

The next iteration of the system will integrate Red Hat Enterprise Linux AI, known as RHEL AI.

This is to provide a stable, hardened foundation for scaling and managing containerized AI applications in remote and extreme environments.

RamaLama itself was built with a stated goal of making AI "boring" — meaning reliable, predictable, and unglamorous in the best possible sense for mission-critical applications.

The same architecture being tested for astronaut health could eventually serve as a blueprint for delivering medical support in the most remote areas on Earth.

Whether the CMO-DA eventually evolves into something resembling Star Trek's handheld Tricorder remains unknown.

What is known is that an open source AI tool is already diagnosing symptoms aboard a replica of hardware currently orbiting Earth.

*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds. Make sure to click the Follow button!*

*And of course you can also*follow TechRadar on TikTok***for news, reviews, unboxings in video form, and get regular updates from us on*WhatsApp***too.*

![Efosa Udinmwen](https://cdn.mos.cms.futurecdn.net/nwRLdPUNG4rWu4Y6nthHDV.png)

Efosa has been writing about technology for over 7 years, initially driven by curiosity but now fueled by a strong passion for the field. He holds both a Master's and a PhD in sciences, which provided him with a solid foundation in analytical thinking.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
