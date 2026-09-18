---
title: 'Made in China, flying for Britain: Who really knows what’s inside our defense
  tech?'
source_url: https://www.techradar.com/pro/made-in-china-flying-for-britain-who-really-knows-whats-inside-our-defense-tech
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-15T11:26:43Z'
published: '2026-09-15T00:00:00Z'
description: Chinese tech in Royal Navy Drone incident serves as a warning
image: https://cdn.mos.cms.futurecdn.net/JpXukHGqkZ8gapEzDQNqRW-1920-80.jpg
categories:
- Technology & Software
---

![Concept art representing cybersecurity principles](https://cdn.mos.cms.futurecdn.net/JpXukHGqkZ8gapEzDQNqRW.jpg) 

![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png) 

Reports that cameras intended for Royal Navy drones contained Chinese-made components sending “heartbeat” signals to China sound like the opening of a spy thriller. The reality is more mundane, but arguably more useful as a warning.

Partner at Avella Security.

There is currently no evidence that Ministry of Defence data, imagery or classified systems were accessed or exfiltrated. Routine cyber testing reportedly identified third-party camera components sending automated heartbeat communications to an IP address in China, after which internet connectivity to the affected camera subsystems was removed and the vulnerabilities closed.

So, based on what we know today, this is not a story about confirmed data theft. It is a story about something potentially much more widespread. How little organizations can know about what is happening several layers down in their technology supply chains.

## When insignificant data becomes intelligence

A heartbeat signal sounds fairly innocuous. A device is effectively saying: “I’m alive.”

The danger is assuming that because the data looks insignificant, it has no intelligence value.

Basic telemetry can potentially disclose device presence, uptime and temporal patterns. You could see when something comes online, how long it remains active and whether there are patterns in when it is being used.

None of that necessarily tells you much in isolation. Intelligence, however, rarely comes from one perfect piece of information. It comes from joining lots of apparently insignificant pieces together.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Combine those signals with OSINT, SIGINT, routing metadata or knowledge of exercises and deployments and they could potentially contribute to a much richer picture.

That does not mean this incident exposed Royal Navy locations, personnel or operational movements. There is no public evidence to support that conclusion.

But it shows the question is more than “Did sensitive information leave the system?” We also need to ask “What could somebody infer from the information that did?”

With cameras and other connected sensors, there is another consideration. If you discover an unexpected external communications path, you need to understand what it can do. What has already travelled across it is only part of the picture. You also need to know what the component could potentially transmit.

## ‘Buy British’ misses the point

The instinctive response to supply-chain concerns is often greater sovereignty. But telling defense companies to simply “buy British” misunderstands how modern technology is built. Pull apart a supposedly trusted product and the processors, cameras, communications modules, microcontrollers and firmware inside it may originate from suppliers scattered around the world.

Modern defense capability has effectively become a giant systems-integration exercise conducted across global technology supply chains.

Defense organizations may have a strong understanding of their Tier One suppliers. However, visibility can deteriorate considerably at Tier Two, Tier Three and beyond, precisely where specialist manufacturers, smaller technology providers and software dependencies enter the system.

You can perform assurance to the nth degree. The problem is doing it across every component in every system without making innovation painfully slow and expensive.

That is particularly difficult for startups. Switching from a commercial component to a sovereign or trusted alternative can mean higher costs and longer lead times, but also hardware redesign, software changes, testing and recertification.

## Ukraine has changed the economics

This tension is becoming more important because modern conflict is simultaneously pushing defense towards technologies that benefit from rapid commercial development.

Ukraine has demonstrated the military value of relatively inexpensive unmanned systems that can be produced, modified and replaced quickly. They do not eliminate the need for sophisticated missiles or high-end platforms, but they are changing the economics of warfare.

Future militaries will need exquisite capability, but they will also need technology that can be manufactured at scale and adapted rapidly as battlefield conditions change.

Commercial off-the-shelf components help make that possible.

That creates a fundamental tension at the heart of strategic autonomy. The global technology ecosystem that allows defense companies to innovate quickly and relatively cheaply can create exactly the dependencies governments are attempting to reduce.

## Scrutinize what can see, think and communicate

Risk should be determined by what a component can actually do, not simply which country appears on the label.

The questions I would ask are: what can it see? What can it do? Can it communicate independently? Can its behavior be changed?

A connected, programmable camera warrants considerably greater scrutiny than a passive component. Cameras, radios, sensors and communications modules deserve particular attention because they can collect or process information, run firmware and potentially create communications paths of their own.

Programmable sub-components are another area of concern because their behavior can potentially be altered through software or firmware.

As defense moves further into AI, the same principle will increasingly need to extend beyond physical hardware. Assurance will need to consider where models came from, what data they depend on, who can update them and how their integrity is maintained.

## Design for things you cannot see

Supply-chain assurance should not be the only defense. Architecture matters too. If a component does not need internet access, why give it internet access?

If a camera only needs to communicate with another system locally, restrict it to that. Network segmentation, telemetry suppression, tightly controlled communications paths and air-gapping where appropriate can all reduce the consequences of unexpected behavior.

There is also a strong argument for a shared repository of vetted components from trusted manufacturers and vendors. This could include a Bill of Materials (BOM): a formal, nested inventory of software and hardware components. The Cybersecurity and Infrastructure Security Agency (CISA) promotes BOMs to improve supply-chain security, increase transparency and accelerate vulnerability management.

But such a repository cannot become a static approved shopping list. Firmware changes. Manufacturers substitute components. Vulnerabilities emerge. Supply chains move. Trust must therefore be continuously maintained rather than awarded once. This ongoing assurance is ultimately what identified the Royal Navy issue.

Perfect knowledge and assurance of every component is neither realistic nor economically viable if it makes defense innovation impossibly slow.

What we need instead is explicit, risk-based assurance of trusted manufacturers and vendors. Understand which components and software present the greatest threat, scrutinize them accordingly, and use architectural controls and ongoing assurance to reduce exposure elsewhere.

Strategic autonomy goes far beyond where a platform was assembled or which flag sits above the company that built it. What this incident highlights is the risk when an unvetted external communications path exists inside technology intended for a military platform. Sometimes good cybersecurity comes down to asking the simplest question: why is this thing talking to the internet at all?

*This article was produced as part of**TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:**[https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
