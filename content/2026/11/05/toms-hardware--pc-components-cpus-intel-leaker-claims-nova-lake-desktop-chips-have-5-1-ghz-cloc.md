---
title: Intel leaker claims Nova Lake desktop chips have 5.1 GHz clock limit beyond
  90°C — high clock speeds could demand significant cooling for next-gen chips
source_url: https://www.tomshardware.com/pc-components/cpus/intel-leaker-claims-nova-lake-desktop-chips-have-5-1-ghz-clock-limit-beyond-90-c-high-clock-speeds-could-demand-significant-cooling-for-next-gen-chips
source_site: Tom's Hardware
source_slug: toms-hardware
description: A known Intel leaker claims that Intel's next-generation processors will
  top out at 5.1 GHz if the CPU core temperatures aren't kept below 90°C.
image: https://cdn.mos.cms.futurecdn.net/B4avSRi36yewaj7Wyj3k5Q-1920-80.jpg
published: '2026-11-05T00:00:00Z'
scraped_at: '2026-11-05T17:28:25Z'
categories:
- Technology & Software
- Hardware
people:
- Jaykihn
- Tom
- Zak Killian
locations:
- Arrow Lake
- Nova Lake
- Raptor Lake CPUs
organisations:
- AMD
- APX
- Arrow Lake
- Get Tom's Hardware
- Google News
- HotHardware
- Intel
- Jaykihn
- N2P
- PC
- Red Team
- Ryzen
- TSMC
- TVB
- The Tech Report
- Tom's Hardware
- Zak
---

![An Intel Core CPU, seemingly floating in dark water.](https://cdn.mos.cms.futurecdn.net/B4avSRi36yewaj7Wyj3k5Q-1920-80.jpg)

According to new information from reasonably reliable Intel leaker Jaykihn, Intel's upcoming Nova Lake desktop CPUs will have an unusual limiter applied. He claims that the next-gen desktop parts from Intel will "universally limit the maximum core frequency to 5.1 GHz when above 90°C." That doesn't mean the parts will top out at 5.1 GHz, which would be disastrous, but it does mean that you're going to need some darn good cooling to reach high clock rates on Nova Lake desktop CPUs.

![A hand holding the Ryzen 7 9850X3D.](https://cdn.mos.cms.futurecdn.net/Xh2MupWrRjJPiLLuopmKRB-1200-80.jpg)

Let's be clear about what he's saying. He's not saying that Nova Lake CPUs can't go above 5.1 GHz. He's also not saying that Nova Lake CPUs have their thermal limit at 90°C. While Jaykihn doesn't provide any clock rate information, he does imply that the chips will go above that, possibly quite significantly, as long as the thermals are kept in check, and he does say that the "Tjmax" value of Nova Lake is 100°C. Notably, that's a drop from 105°C in Arrow Lake, although prior-gen Raptor Lake CPUs had the same 100°C peak.

> Preliminary. Nova Lake -S desktop processors will universally limit the maximum core frequency to 5.1GHz when above 90C. This is separate behavior from traditional TJMax thermal throttling at 100C. Alike TJMax, this temperature threshold cannot be shifted upwards.November 4, 2026

The mechanism that this most clearly resembles is Intel's own Thermal Velocity Boost. TVB, if you're not familiar, is the feature that allows high-end Intel CPUs to hit their highest clock rates. Put simply, TVB simply says that if the chip isn't overheating, it can go 100-300 MHz higher than its rated Turbo Boost Max speed. It's a little confusing, because these TVB clock rates are often quoted as the "Max Turbo Frequency"; Intel even does this itself. But TVB clocks are not the same as standard turbo clocks, and a lot of users who don't have exotic cooling probably never actually see these speeds in practice since they do require optimal conditions.

Does this mean that the practical limit of Nova Lake desktop CPU clocks is 5.1 GHz? Well, that depends on how hard these parts are to cool. Remember, we're dealing with chips fabricated on a 2nm-class process; in this case, it's reportedly TSMC's N2P for the compute tiles, while the peripheral chiplets are all on Intel's own 18A or 18A-P. This has consequences, as N2P is reportedly much denser than 18A, but it also lacks back-side power delivery, which means that the thermal resistance of the individual dies is considerably lower. Combined with much lower power consumption from a real node step, it may turn out that Nova Lake is actually quite easy to keep cool.

Ultimately, that is going to depend in part on how much Intel decides to push the "fMax", or maximum frequency. Rumors have put AMD's Zen 6 desktop Ryzen processors above 6 GHz for peak clock rates; if that's true, Intel could be looking at as much as a 20% clock rate disadvantage at 5.1 GHz. Obviously, as noted above, the chips are expected to have a higher fMax than that, but it remains to be seen how easily users can keep the parts cool enough to make use of the extra clock rate headroom given this new limit. Both Intel's flagship Core Ultra 9 285K and the Red Team's extant Zen 5-based Ryzen 9 9950X can reach 5.7 GHz before overclocking.

![Intel XTU software with Intel Core Ultra 7 270K Plus](https://cdn.mos.cms.futurecdn.net/jG4uVkknkR8tYDgFWMQis7-1200-80.png)

For tuners, a frustrating detail is that this 5.1 GHz hard clock limit apparently "cannot be raised." That means folks doing system tuning on Nova Lake will be strongly encouraged to undervolt to reduce the thermal output of their processors and help them maintain high performance. That's unusual, as historically Intel allows users to adjust the thermal throttle point of their processors when overclocking. That may potentially still be the case on processors unlocked for overclocking, of course; Jaykihn is reporting based on leaks and engineering samples rather than final released products.

Even if Nova Lake doesn't scale clocks much over Arrow Lake, it could still be quite a bit faster than the previous generation. Recall that the new chips will come with new core architectures and new technologies, including APX core extensions and bLLC, Intel's long-awaited response to AMD's 3D V-Cache. Forecasts are indicating that gaming performance could be as much as 33% faster than Arrow Lake, which would be huge. However, this 5.1 GHz limit could be a downer for people who are interested in the rumored 52-core version of Nova Lake. We'll find out how much it matters when the Core Ultra 4000 series launches either very late this year or very early next year, although we wouldn't expect the 52-core flagship or bLLC versions until next summer.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Zak Killian](https://cdn.mos.cms.futurecdn.net/yonJziSpjzVFahKcUonJvi-140-80.jpg)

Zak is a freelance contributor to Tom's Hardware with decades of PC benchmarking experience who has also written for HotHardware and The Tech Report. A modern-day Renaissance man, he may not be an expert on anything, but he knows just a little about nearly everything.

* Ok! So?  
    
  Well hopefully this will keep you guys from running intel CPUs insanely out of spec in your benchmarks...although I already see you guys limiting intel to that 5.1 and claiming it's "out of the box" ,man, we are just reviewers man, we can't set up a decent system...  
    
  I hope it doesn't just limit the clocks but actually turns all the settings to the default.  
  hotaru251 said:i mean....thats fine?  
    
  You wouldnt want to run a cpu past 90c long term anyways.This will let you run it at whatever the tjmax is (prob. 105) forever, just not at full tilt. Reply
