---
title: 'Exclusive: Future of battlefield AI must be built for disconnection'
source_url: https://www.techradar.com/pro/resilience-comes-from-designing-for-disconnection-not-assuming-more-connectivity-the-future-of-battlefield-ai-systems-lies-in-both-coordination-and-local-capability
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-06T12:07:33Z'
published: '2026-09-06T00:00:00Z'
description: I spoke to Andreas Hellander of Scaleout to learn more about how battlefield
  AI systems and frontline technologies can be made more resilient.
image: https://cdn.mos.cms.futurecdn.net/3xYAE75gYrzr4hTu3ssyhj-1920-80.jpg
---

![Robotic hand interacting with a digital display showing various military equipment, defense systems, drones and cybersecurity elements and data visualization in a dark environment.](https://cdn.mos.cms.futurecdn.net/3xYAE75gYrzr4hTu3ssyhj.jpg) 

As the US moves to integrate more AI systems into every arm of its military, the situations on the ground in the Middle East are raising some serious problems for maintaining the compute and connectivity needed to keep systems online.

Drones, sensors, AI-assisted targeting and decision-making all rely on these systems in one way or another, and the destruction of a single frontline AI data center can seriously damage an army’s capacity to function.

But these problems go beyond hardware. How does a drone adapt its mission parameters without being able to communicate? How can AI models continue inference without access to critical battlefield data? And what compromises must be made to prepare battlefield AI for these conditions?

## Battlefield AI should continue functioning, even when comms go down or hardware is disabled

While the conflict circling the Strait of Hormuz may be a hugely expensive endeavour, Iran is providing valuable lessons for warfighters. Relying on traditional data centers in the Middle East has already shown its weaknesses. These sprawling warehouses make easy targets for cheap missiles, and entire systems can be taken offline from a single hit.

Palantir has already begun deploying shipping containers filled with Nvidia hardware as an alternative to the traditional data center. These containers can be deployed on frontlines and can connect directly into operational workflows, offering decentralized compute where it is needed most.

Scaleout is a company building infrastructure for edge AI and federated learning that trains models on distributed, sensitive data without centralising it. The company has worked with NATO - most recently the Swedish Air Force - and defense primes such as BAE Systems.

Andreas Hellander is the CEO and co-founder of Scaleout. He holds a PhD in Scientific Computing and an MSc in Biotechnology Engineering, and is an Associate Professor at Uppsala University, where he built one of the top research groups at the Department of Information Technology before founding Scaleout.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

I spoke to Andreas to learn more about how battlefield AI systems can be made more resilient, and how drones, sensors, and other frontline technologies can continue functioning when conditions go downhill.

- **What happens when parts of a battlefield AI's computing and hardware are taken offline? What redundancies are in place to keep communications between systems operational?**

The aim is not to promise an unbreakable connection; it is to stop the loss of one component from taking down the whole capability. In our architecture, a disconnected node continues local inference using its last approved model, caching detections and telemetry until a link returns.

Multiple aggregation points can be used above the edge. If one becomes unavailable, clients can be reassigned and training can proceed with those still reachable. That creates graceful degradation rather than an all-or-nothing failure. We do not supply the tactical communications network itself; our job is to ensure the AI workload does not assume that any radio, satellite or other link will always be available.

- **What are the trade-offs between a highly centralized battlefield AI network and a more distributed approach, especially concerning data gathering, targeting, battlefield coordination and logistics?**

Centralisation provides a consistent operational picture, substantial compute and a clear place to enforce security, model approval and command policy. It supports theatre-wide coordination and logistics, but also concentrates risk: losing one link or facility can remove a disproportionate share of the capability, while moving large or classified datasets may be slow, prohibited or impossible.

A distributed system keeps analysis close to the sensor, reducing latency and allowing local functions to continue during disconnection. The trade-off is fragmentation. Targeting based on a partial or stale picture is risky, and local logistics decisions may not be optimal for the wider force. The best design is usually hybrid: central coordination when available, with clearly bounded local capability when it is not. Authority remains with the relevant command-and-control and human decision process.

- **How do these AI drones and sensors adapt to the battlefield and what differences are there in the behavior of an AI drone that can still communicate and one that has lost communication?**

It is important to separate running a model from retraining it. Small platforms typically perform inference in flight, while controlled retraining and approval happen on a ground node or more capable edge computer. Onboard learning exists in research, but uncontrolled mid-mission retraining creates serious assurance problems.

A connected platform can share detections, receive tasking and contribute to a wider operational picture. After losing its link, a drone follows its pre-approved failsafe: depending on the mission, it may continue a bounded task, return, hold or land. Onboard processing can keep perception and navigation working, but the platform loses external context, new instructions and fleet coordination. Disconnection should be a designed operating state with explicit limits, not an improvised emergency mode.

- **How is the data collected by these drones and sensors used to help battlefield AI systems adapt to new conditions, threats, and tactics?**

The useful data is often the hardest to move, so we send the model to the data rather than centralising the footage. Active-learning software identifies the frames most likely to improve it, such as uncertain detections, unfamiliar objects or changed conditions. A person still labels the selected material; the software reduces the searching, not the need for human judgement.

The model is then fine-tuned locally and tested against a benchmark. A candidate can also run beside the current model in shadow mode before an operator approves it. Where policy and connectivity allow, sites exchange protected model updates rather than raw training footage, combining them into a shared model. Federated learning reduces data movement, but the updates still need to be secured, validated and audited.

- **What are the main challenges you encounter when deploying AI drones and sensors? What capabilities are available for militaries to source the required compute and energy production close to the front lines?**

The hardest constraints are usually power, heat, weight, weather, vibration, electronic warfare, inconsistent data and safe software updates across a mixed fleet. Integration and accreditation can be as demanding as the machine learning.

The compute is commercially available: low-power modules such as NVIDIA Jetson for small platforms, and ruggedised GPU servers or containerised edge units for ground sites. Energy is tougher. Every processor competes with propulsion, sensing and communications, while generators, batteries and distribution equipment add logistical burden and new points of failure. In our public demonstration with BAE Systems Bofors, the perception workload ran on onboard compute at -18°C without connectivity. The principle is to use the smallest practical footprint and assume both power and bandwidth are scarce.

- **There is an increasingly blurred involvement of commercial companies providing services for military use, such as AWS data centers in the Middle East and drone production in the UK for Ukraine. How are companies providing services to the military adapting to the pressures of potentially being deemed a legitimate military target?**

Speaking for Scaleout, rather than for the sector as a whole, we design our platform so that a customer’s operation does not depend on Scaleout remaining continuously available. It runs in the customer’s own infrastructure, works air-gapped, and does not require a licensing call-home or persistent connection to our systems or a public cloud.

That matters in any contested or disconnected environment: reliance on a remote provider can become an operational vulnerability. Our approach has therefore been to keep control and continuity local to the customer, rather than make our own infrastructure a critical dependency.

The wider question of how commercial providers are viewed in a conflict is one for policymakers, legal experts, and the companies involved. We would not want to speculate about other providers’ risk assessments or operating models.

- **What is the future trajectory of these systems? Will each individual drone and sensor have its own connectivity that can feed data back through a global satellite network? Will these systems be able to operate autonomously for multiple days or weeks without human input?**

Connectivity will improve, including through low-Earth-orbit satellites, but connecting every sensor directly to space is unlikely to be the universal answer. Terminals consume power and spectrum, add cost and can create an electronic signature. A more resilient pattern combines local mesh links, opportunistic synchronisation and selected gateways to satellite or other long-range communications.

Longer disconnected operation is realistic, but endurance is often limited by batteries, weather and maintenance rather than AI software. There is also a critical distinction between operating without a connection and operating without human authority. The first is a resilience property; the second is a policy, legal and ethical decision. The future is therefore not simply more autonomy, but verifiable control: knowing which model ran on each platform, what produced it, where its limits were and who approved it.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Benedict Collins](https://cdn.mos.cms.futurecdn.net/jEvqGv8wvH7PWZ4XPURyyB.jpg) 

Benedict is a Senior Security Writer at TechRadar Pro, where he has specialized in covering the intersection of geopolitics, cyber-warfare, and business security.

Benedict provides detailed analysis on state-sponsored threat actors, APT groups, and the protection of critical national infrastructure, with his reporting bridging the gap between technical threat intelligence and B2B security strategy.

Benedict holds an MA (Distinction) in Security, Intelligence, and Diplomacy from the University of Buckingham Centre for Security and Intelligence Studies (BUCSIS), with his specialization providing him with a robust academic framework for deconstructing complex international conflicts and intelligence operations, and the ability to translate intricate security data into actionable insights.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
