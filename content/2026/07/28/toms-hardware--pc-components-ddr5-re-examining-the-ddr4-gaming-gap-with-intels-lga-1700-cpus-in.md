---
title: Re-examining the DDR4 gaming gap with Intel’s LGA 1700 CPUs in mid-2026 — performance
  drops of 14% on average, and up to 25% in some games
source_url: https://www.tomshardware.com/pc-components/ddr5/re-examining-the-ddr4-gaming-gap-with-intels-lga-1700-cpus-in-mid-2026-performance-drops-of-14-percent-on-average-and-up-to-25-percent-in-some-games
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-28T10:44:29Z'
published: '2026-07-28T00:00:00Z'
description: The DDR4 tax is becoming more severe.
image: https://cdn.mos.cms.futurecdn.net/xZejVJBcPpXAbgR7KzudjL-2000-80.jpg
---

![DDR4 vs DDR5](https://cdn.mos.cms.futurecdn.net/xZejVJBcPpXAbgR7KzudjL.jpg) 

Unless you already have a kit of DDR5, or deep pockets for PC hardware, you’re stuck right now. Despite seeing some of the __best CPUs for gaming__ released just in the past year, the DDR5 tax represents a major hurdle to building or upgrading your PC. Intel’s LGA 1700 CPUs hold an unintended solution, offering support for both DDR4 and DDR5. We wanted to see if this on-ramp to a next-gen platform was really as smooth as it looks at first glance.

The idea is simple. If you already have a DDR4 kit, you can upgrade to a relatively new CPU while keeping the door open for a transition to DDR5 without buying a new chip. It’s inexpensive, and a bit more of a practical solution than upgrading to DDR5 with a single DIMM and worrying about pairing it with another later.

Our testing shows how much of a performance difference there is with DDR4 in games. We’re focused on games here for a few reasons. First, in non-gaming applications, memory speed is highly dependent on the specific workload you’re running. Games, despite using different engines, are largely similar workloads that stress the hardware in similar ways. Further, those workloads are continually evolving as new games, new technologies, and new hardware targets are released.

We kept our testing focused on Intel’s LGA 1700 CPUs because they’re the only options that give us a true apples-to-apples comparison between DDR4 and DDR5. We don’t have any AMD CPUs in our test pool because there aren’t any chips that support both DDR4 and DDR5. This isn’t intended to be a competitive analysis between AMD and Intel. That conversation opens up a much broader conversation about total platform cost.

## Testing DDR4 vs. DDR5 on Intel’s LGA 1700 CPUs

To test DDR4 and DDR5’s gaming performance, we ran Intel’s main LGA 1700 stack through a 15-game gauntlet of benchmarks. Notably, we don’t have results for the Core i9-12900K, as our sample has a janky memory controller that won’t boot on DDR5 systems. You can read a full breakdown of how (and why) we tested in the way we did in the section below.

We ran all of the games through our 16-game benchmark suite, though we cut *Doom: The Dark Ages* from the results here. An update for the game rolled out mid-way through testing and skewed our results, so we’re omitting it. The 15 remaining games still paint a clear picture of the performance difference between DDR4 and DDR5.

As usual, we tested with the RTX 5090 Founder’s Edition at 1080p with a mixture of High and Ultra settings. We test at 1080p to maximize the differences between CPUs, and it remains the most widely-used resolution for gaming. Deltas between CPUs will decrease as the resolution climbs and the GPU becomes a larger influence in performance.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Below is our geomean from testing across the suite. Given that we’re looking to compare a single CPU’s performance with DDR4 and DDR5, we’ve highlighted some CPUs with the same color (13700K is always dark red, for instance, while 14700K is always dark blue).

 ![DDR4 vs DDR5](https://cdn.mos.cms.futurecdn.net/VHReuc9HgcHQygr6kAxpQL.png) 


The chart above is a bit difficult to parse, mainly because we’re often jumping several entries to get to a comparison point. For the stack of chips we tested, here’s a clearer overview of the performance difference with DDR4:

| 
 | 
 | 
| Core i9-14900K | -14% | 
| Core i7-14700K | -13.2% | 
| Core i5-14600K | -13.1% | 
| Core i9-13900K | -11.3% | 
| Core i7-13700K | -13.5% | 
| Core i5-13600K | -11.4% | 
| Core i7-12700K | -9.3% | 
| Core i5-12600K | -9.5% | 

As we’ll get into with the individual game tests below, the drop in performance between DDR4 and DDR5 can be much larger than the comparison in our geomean (and, in turn, smaller in other games). What’s important for the overall performance drop is the trend as we move to newer chips. You can see a 9% drop grow to 14%, as DDR4 becomes a more significant bottleneck when the processor it’s feeding becomes more powerful.

That trend is one of the main driving forces behind our look at DDR4 and DDR5 gaming performance today. We looked at __DDR4 and DDR5 performance extensively__ near the Alder Lake launch, and even more recently last year, __evaluating performance across a wide range__ of applications. The testing here is focused solely on gaming to answer a critical question of building a PC today: Are you really giving up that much gaming performance with DDR4?

The answer is, yes, you’re giving up around 11% to 14% of your gaming performance overall when the memory is the only variable that changes. That’s a consistent drop, as well. Older titles care see less of a benefit from DDR5 generally, but we saw a steady decrease of around 11-14% across the games we tested, with some titles pushing above a 20% drop.

 ![DDR4 vs DDR5](https://cdn.mos.cms.futurecdn.net/Xe7QqvwAixg9UqgyMXC9PL.png) 


*007 First Light* is the newest game we tested, and it outpaces our averages. The 14900K sees a 16.5% drop with DDR4, while the 13600K drops 12.7% of its performance. Especially among the most powerful CPUs here, you can see DDR4 level off performance in a way that’s undesirable. The 14900K, for instance, is just 1.7% faster than the 13900K with DDR4, but it’s 4.6% faster with DDR5.

 ![DDR4 vs DDR5](https://cdn.mos.cms.futurecdn.net/6o9NdqbLnK4L4nSTzmb6SL.png) 


Similarly, in *Crimson Desert,* you can see the 13700K lose 13.7% of its performance with DDR4, and the 14600K drop 13.2% of its performance. It’s worth noting that neither of these games are particularly sensitive to memory speed. You can see in our recent __Ryzen 7 5800X3D re-review__ that even a boost from 3D V-Cache doesn’t give CPUs with a robust memory chain an automatic advantage.

 ![DDR4 vs DDR5](https://cdn.mos.cms.futurecdn.net/guWQGpSGWocuGxFVrNgSNL.png) 


Perhaps the most consequential of the newer games we tested is *Marvel Rivals,* not only because it shows a much larger gap between DDR4 and DDR5, but also because it’s the most-played game in our test suite by a long shot (short of *Counter-Strike 2*). For weaker chips like the 12600K, the gap is 13.9%, just slightly above our geomean. For the more powerful 14700K, however, it shows a gap of 25.3%. Even the 14600K drops 17.4% of its performance with DDR4.

 ![DDR4 vs DDR5](https://cdn.mos.cms.futurecdn.net/CpYVrMFpMrQ7Rw4mcs7tRL.png) 


*Counter-Strike 2* is less extreme, perhaps as a consequence of having such a high floor for average frame rates. You can see that the Alder Lake chips don’t care much about DDR4, with the Core i7-12700K performing identically across both memory standards. That gap grows with more powerful CPUs, however, with the 14700K creeping up toward a 10% delta.

 ![DDR4 vs DDR5](https://cdn.mos.cms.futurecdn.net/3H4NpGeNcwGk8UQWpqL93L.png) 


In *Spider-Man 2,* we can see more consistent drops across the stack of chips we tested, with most CPUs dropping around 18% of their average performance with DDR4. That’s true even on the weaker 12700K, which lost 15% of its performance. The 14900K, meanwhile, was 18.7% slower with DDR4.

 ![DDR4 vs DDR5](https://cdn.mos.cms.futurecdn.net/4ncQQ6xryZj6TE3hRs9kQL.png) 


Even in an older, GPU-heavy title like *Cyberpunk 2077,* we can see a consistent drop. You can see in this game that we become completely bound by the GPU at the top of the rankings, but that’s a level these chips can’t hit when paired with DDR4. The 14700K drops about 14% of its performance, and the 13600K, about 13% of its performance.

![DDR4 vs. DDR5](https://cdn.mos.cms.futurecdn.net/zZoBxWxSJFjEUfb6nRxVHh-1200-80.png) 

![DDR4 vs. DDR5](https://cdn.mos.cms.futurecdn.net/S3RzevxJYbaYdJBmtJwrpg-1200-80.png) 

![DDR4 vs. DDR5](https://cdn.mos.cms.futurecdn.net/BYSYnpaQ3XwfpxsLUBf66h-1200-80.png) 

![DDR4 vs. DDR5](https://cdn.mos.cms.futurecdn.net/r736awPZhmgHXTe8abLJ3h-1200-80.png) 

![DDR4 vs. DDR5](https://cdn.mos.cms.futurecdn.net/zrhrJqKxcz3MYz38wwr93h-1200-80.png) 

![DDR4 vs. DDR5](https://cdn.mos.cms.futurecdn.net/BPi47SmALjn8Rsi6yAkw2h-1200-80.png) 

![DDR4 vs. DDR5](https://cdn.mos.cms.futurecdn.net/vwtbhuhDsbgjvammb8sv2h-1200-80.png) 

![DDR4 vs. DDR5](https://cdn.mos.cms.futurecdn.net/VyQcGkT5yPrF9hQ9kzif2h-1200-80.png) 

![DDR4 vs. DDR5](https://cdn.mos.cms.futurecdn.net/Ymo3pFg6pc5zWmGErTyC2h-1200-80.png) 

![DDR4 vs. DDR5](https://cdn.mos.cms.futurecdn.net/zZoBxWxSJFjEUfb6nRxVHh-1280-80.png) 

![DDR4 vs. DDR5](https://cdn.mos.cms.futurecdn.net/S3RzevxJYbaYdJBmtJwrpg-1280-80.png) 

![DDR4 vs. DDR5](https://cdn.mos.cms.futurecdn.net/BYSYnpaQ3XwfpxsLUBf66h-1280-80.png) 

![DDR4 vs. DDR5](https://cdn.mos.cms.futurecdn.net/r736awPZhmgHXTe8abLJ3h-1280-80.png) 

![DDR4 vs. DDR5](https://cdn.mos.cms.futurecdn.net/zrhrJqKxcz3MYz38wwr93h-1280-80.png) 

![DDR4 vs. DDR5](https://cdn.mos.cms.futurecdn.net/BPi47SmALjn8Rsi6yAkw2h-1280-80.png) 

![DDR4 vs. DDR5](https://cdn.mos.cms.futurecdn.net/vwtbhuhDsbgjvammb8sv2h-1280-80.png) 

![DDR4 vs. DDR5](https://cdn.mos.cms.futurecdn.net/VyQcGkT5yPrF9hQ9kzif2h-1280-80.png) 

![DDR4 vs. DDR5](https://cdn.mos.cms.futurecdn.net/Ymo3pFg6pc5zWmGErTyC2h-1280-80.png) 

You can browse through our remaining benchmarks using the gallery above, but most games tell a similar story. The gap between DDR4 and DDR5 persists, of course, but there’s another angle to look at the data. DDR4 flattens off performance, creating a bottleneck with faster CPUs. That could be justification for buying a *weaker* chip if you can only afford DDR4 memory right now.

 ![DDR4 vs DDR5](https://cdn.mos.cms.futurecdn.net/3RomyNhdHojGQutLdXuXRL.png) 


Outside of performance, one important aspect of using a DDR4 system compared to DDR5 is power consumption. With DDR4, power consumption of the CPU increases, as you can see in the chart above. The jump is generally only a few watts, but it’s worth noting nonetheless. In games, we’re well below the operating temperature of all the chips in our test pool, but when pushing toward maximum power draw, DDR4 will post yet another limitation.

## How (and why) we tested DDR4 vs. DDR5 now

DDR5 is way too expensive, and Intel’s LGA 1700 CPUs represent a unique value proposition given the unprecedented increases in memory prices over the past several months. The idea is that you can upgrade to a newer platform while sticking with DDR4, giving you a stopgap for an eventual DDR5 upgrade. It seems Intel recognizes this value proposition, as well, as it’s reportedly slated to launch Raptor Lake Next CPUs on the LGA 1700 socket.

We tested the main stack of chips, short of the Core i9-12900K, as described above. We didn’t test variants like KS releases to keep our testing focused, as well as lower-end SKUs like the 12100F or 14400. The memory controllers in these lower-end chips are weaker, sustaining lower DDR5 speeds, so expect less of a difference in performance with them.

Below, you can see the test benches we used. In addition to keeping hardware consistent, we use a frozen OS image with an identical software stack. We’re running the same version of the same apps on the same OS update, with identical drivers.

In the BIOS, we enabled XMP for both kits of memory. We also tested with Resizeable BAR turned on, and Virtualization-Based Security (VBS) turned off. Most motherboard vendors off a profile with the power limits removed on Intel CPUs, which can push the processor outside of warrantied specifications. We stuck with the default “Performance” profile for our testing here.

| 
 | Row 0 - Cell 1 | 
| Motherboard | |
| RAM | |
| 
 | Row 3 - Cell 1 | 
| Motherboard | |
| RAM | |
| 
 | Row 6 - Cell 1 | 
| Gaming CPU | Nvidia GeForce RTX 5090 Founder’s Edition | 
| Cooler | Corsair iCue Link H150i RGB | 
| Storage | 2TB Sabrent Rocket 4 Plus | 
| PSU | |
| Other | Arctic MX-4 TIM, Windows 11 Pro, Alamengda open test bench | 

## Is DDR4 still worth it?

It makes sense that we’ve seen a shift back toward DDR4. Although DDR4 prices have risen in lockstep with DDR5 prices, they started from a much lower base. A kit of DDR4 today is not much more expensive than a DDR5 kit of similar capacity a year ago. And, with estimates that the memory shortage could persist through 2030, there’s a strong argument for going with a DDR4 system if you’re in need of an upgrade.

The performance trade-off alone isn’t as big of a problem as it appears at first glance. You’re going to lose about 15% of your average gaming performance with Intel’s LGA 1700 CPUs (particularly Raptor Lake chips). You’ll spend more than twice as much on a 32GB kit of DDR5-6000 as you will on a 32GB kit of DDR4-3200, as you can see in our __RAM price tracker__. And, you might already have a DDR4 kit, cutting that cost completely out of an upgrade. Dollars spent for performance gained, DDR4 makes complete sense.

However, performance isn’t the only factor at play, and that’s the unfortunate reality of using a DDR4 platform right now. It’s a dead end, both for performance and upgrade potential. As we saw in our recent testing of the Ryzen 7 5800X3D, there’s a performance wall in games with DDR4, one which the 5800X3D often runs up against. The memory is a bottleneck, and it doesn’t seem like there’s a way around that problem without upgrading to DDR5.

We also aren’t seeing any new DDR4 CPUs, at least right now. AMD re-released the Ryzen 7 5800X3D, and there are murmurs of Raptor Lake Next. But given the current landscape, we don’t expect a CPU that will radically change the performance you can get out of a DDR4 platform.

Instead of sticking with DDR4 for a better CPU, the best course of action right now is to bite the bullet on DDR5 and buy a weaker CPU, particularly if gaming performance is your main concern. Given that memory prices are out of control, there are excellent deals on DDR5 CPUs right now, allowing you to offset the cost of an upgrade and giving you a kit of DDR5 to carry forward in future builds.

As an example, __AMD’s recently-released Ryzen 7 7700X3D__ is $80 cheaper than the re-released Ryzen 7 5800X3D, despite coming in nearly 20% faster in average gaming performance. The $230 Ryzen 5 7600X3D shows similar gains, and it’s even more affordable.

In Intel’s camp, the __Core Ultra 7 270K Plus__ and Core Ultra 5 250K Plus represent some of the best all-around value in the CPU world right now, with compelling gaming performance and chart-topping application performance, all for around $300.

You will spend more on a cheaper CPU and a kit of DDR5. There’s no indication that the memory shortage is ending soon, however. We’ve actually seen prices continue to increase despite the surge leveling off. Opting for DDR5 today buys you better gaming performance, but more importantly, it gives you a kit of memory that you can continue to use as new CPUs and platforms are released.

![Jake Roach](https://cdn.mos.cms.futurecdn.net/h6PRM8bTimCTnNfoAYfjAi.jpg)

Jake Roach is the Senior CPU Analyst at Tom’s Hardware, writing reviews, news, and features about the latest consumer and workstation processors.
