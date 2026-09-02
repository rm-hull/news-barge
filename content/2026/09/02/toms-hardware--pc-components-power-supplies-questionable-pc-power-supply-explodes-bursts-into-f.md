---
title: Questionable PC power supply 'explodes,' bursts into flames the moment it's
  plugged into a socket in viral video — video captures moment repair shop worker
  avoids disaster
source_url: https://www.tomshardware.com/pc-components/power-supplies/questionable-pc-power-supply-explodes-bursts-into-flames-the-moment-its-plugged-into-a-socket-viral-video-captures-moment-repair-shop-worker-avoids-disaster
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-02T12:45:18Z'
published: '2026-09-02T00:00:00Z'
description: He miraculously avoided injury.
image: https://cdn.mos.cms.futurecdn.net/N6pUSFLfhABPeontnADweb-1920-80.png
---

![Power supply caught fire during testing](https://cdn.mos.cms.futurecdn.net/N6pUSFLfhABPeontnADweb.png) 

The power supply is the lifeblood of your PC, responsible for regulating power that goes into the entire system and, thus, determining how well it runs. Clearly, one PSU in Vietnam did not live up to this expectation, as CCTV footage from a shop shows it bursting into flames as soon as it's plugged into the socket. Even though it caught on fire, thankfully, no one was injured as the tester acted quickly to cut it off from the wall.

Details are scarce, but we know the footage comes from some sort of service center in Vietnam. The power supply in question is the VSP MEGA MAX VS750D, and it doesn't appear to be new because the person pulls it out of the box without any packaging material around it. The OP confirms our suspicion in one of their comments, saying it came in for an RMA request from a customer.

The tester already had the power cord ready to go, and the moment he plugged the other end into the PSU, sparks flew out, and it caught on fire. The tester was startled, understandably so, but quickly regained his composure and came back to yank the cord out of the PSU. He then proceeded to pick it up in his hands to blow out the fire, which was followed by a flurry of smoke coming out of the unit. Heroic? Maybe. Reckless? Definitely.

Throughout the endeavor, this person was also barefoot. For those who don't know, carpets build up static electricity through friction as you move around. This is not dangerous to you, but the electricity builds up and can discharge itself into an electronic component. This sudden shock, known as ESD, can very much short out an expensive PC part if you're on a carpeted floor.

Since the footage shows wooden flooring, the only concern here would be lava-hot debris falling out of the PSU and onto his foot. Besides, power supplies are generally shielded from ESD because they're completely enclosed in a metal case. Unfortunately, this specific VSP unit is quite terrible. It has an 80+ White rating and is ranked at Tier E in the PSU tier list. The aftermath of the incident further proves this notion.

 ![The aftermath of the PSU that caught on fire](https://cdn.mos.cms.futurecdn.net/5b5nrXofVpDHCpsRebDrQK.webp) 


The original poster did not provide the actual reason behind the PSU burning up, but you can see how scorched it is in the picture above. Some people in the comments speculate that the PCB wasn't properly isolated inside the case, shorting out the PSU. That is plausible because a short on the 12V rail alone can pull up to 1,800W of power (150A) without tripping a circuit breaker.

However, in the footage, the PSU catches on fire before the tester even has the chance to turn it on. The 12V rail would be completely dead without a motherboard explicitly turning on the system, or if you were to short the 24-pin connector yourself. Moreover, modern units with Active PFC feature auto-sensing input (including even this cheap VPS model), but since Vietnam already operates on 220V mains, this is not a voltage mismatch issue either.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Therefore, the cause is likely tied to a bridge rectifier failing to properly convert AC to DC, or a MOSFET failing to chop voltage into pulses so it can be stepped down to the 12V, 5V, or 3V rails by the transformer. Either would lead to a short internally, which is why we saw sparks before flames in the footage. We can't confirm any of this, of course, especially because the video is so low-quality, but it's our best guess.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Hassam Nasir](https://cdn.mos.cms.futurecdn.net/SxxNFHt95eGK37mKPhJpdZ.jpg) 

Hassam Nasir is a die-hard hardware enthusiast with years of experience as a tech editor and writer, focusing on detailed CPU comparisons and general hardware news. When he’s not working, you’ll find him bending tubes for his ever-evolving custom water-loop gaming rig or benchmarking the latest CPUs and GPUs just for fun.
