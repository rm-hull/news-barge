---
title: RTX 5060 Ti survives car crash after being bent in half — short PCB saves the
  day, single memory chip resolder restore full performance
source_url: https://www.tomshardware.com/pc-components/gpus/rtx-5060-ti-survives-car-crash-after-being-bent-in-half-short-pcb-saves-the-day-single-memory-chip-resolder-restore-full-performance
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-02T13:48:45Z'
published: '2026-08-02T00:00:00Z'
description: Because it had a rather short PCB.
image: https://cdn.mos.cms.futurecdn.net/bKsJKYMfdxvAhpTzPujWbK-1920-80.png
---

![Repairing a bent RTX 5060 Ti that was in a car crash](https://cdn.mos.cms.futurecdn.net/bKsJKYMfdxvAhpTzPujWbK.png) 

Buying a new GPU is always a joyous occasion, but the celebration was cut short for an unfortunate customer in China. Right after buying an AX Gaming RTX 5060 Ti, they got into a serious car crash that ended up totaling the car — and the card along with it. Fortunately, the driver was safe, and somehow the GPU survived, too, with no major electronic damage. Despite being bent in half, the card ended up only requiring minor repair work and was brought back to life quickly by*Brother Zhang*.

![遭追尾！全新5060，弯折变形，能否成功挽救！ - YouTube](https://img.youtube.com/vi/P_bxGLvXRdY/maxresdefault.jpg) 

Visually, the card didn't look salvageable, and midrange GPUs like these often don't make for feasible repair jobs either because of the high labor cost. The backplate and cooler were completely destroyed, so Brother Zhang separated them from the actual PCB. Luckily, this variant of the 5060 Ti used a very short PCB that just barely touched the point of curvature, so the internals were mostly fine.

The technician checked all the power rails for a short circuit but saw no abnormal resistance, which confirmed the core and memory weren't dead. He then proceeded to quickly test the GPU with its bare PCB, and it booted successfully. Brother Zhang devised a makeshift cooler that consisted of the bent fin stack straightened back to the best of his abilities, and two 120mm fans strapped on top via zip ties. This seemed enough to keep the card cool.

![Repairing a bent RTX 5060 Ti that was in a car crash](https://cdn.mos.cms.futurecdn.net/4B2cgM9Md6WxqU6bcH8BSK-1200-80.png) 

![Repairing a bent RTX 5060 Ti that was in a car crash](https://cdn.mos.cms.futurecdn.net/ouu4wpqqGFwHak72SF9wVK-1200-80.png) 

![Repairing a bent RTX 5060 Ti that was in a car crash](https://cdn.mos.cms.futurecdn.net/4B2cgM9Md6WxqU6bcH8BSK-1280-80.png) 

![Repairing a bent RTX 5060 Ti that was in a car crash](https://cdn.mos.cms.futurecdn.net/ouu4wpqqGFwHak72SF9wVK-1280-80.png) 

However, as soon as he tried to install drivers, the PC would black screen and hard crash, showing consistent signs of instability. At this point, Brother Zhang reopened the card and inspected the PCB. He inspected the flex point and decided to resolder the memory module closest to the edge of the board since it experienced the most torque. A simple removal and reapplication fixed the issue, and the card was detected correctly as a 5060 Ti with the full 8GB of VRAM.

 ![Repairing a bent RTX 5060 Ti that was in a car crash](https://cdn.mos.cms.futurecdn.net/NB7dd9smitFGpbLo7SER9L.png) 


Brother Zhang rechecked for any short circuits to ensure no solder bridges were created during the BGA work before moving on to benchmarking. In Furmark, the temps peaked and stabilized at 64°C with no visual artifacts. He then ran a full 3DMark loop to test the PCIe 5.0 x8 link speeds — the card passed with a high 98.9% stability score. It drew around 92% of its maximum power limit during the run, with core temps peaking at around 67°C. This 5060 Ti was officially a survivor.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Hassam Nasir](https://cdn.mos.cms.futurecdn.net/SxxNFHt95eGK37mKPhJpdZ.jpg)

Hassam Nasir is a die-hard hardware enthusiast with years of experience as a tech editor and writer, focusing on detailed CPU comparisons and general hardware news. When he’s not working, you’ll find him bending tubes for his ever-evolving custom water-loop gaming rig or benchmarking the latest CPUs and GPUs just for fun.
