---
title: Leaked 256-core Zen 6c EPYC CPU destroys Zen 5 in early single-threaded benchmarks
  hints at 24% IPC gain — early single-threaded benchmarks point to huge AMD Zen 6
  improvements
source_url: https://www.tomshardware.com/pc-components/cpus/leaked-256-core-zen-6c-epyc-cpu-destroys-zen-5-in-early-single-threaded-benchmarks-hints-at-24-percent-ipc-gain-early-single-threaded-benchmarks-point-to-huge-amd-zen-6-improvements
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-26T20:34:22Z'
published: '2026-10-26T00:00:00Z'
description: There are many confounding factors in this comparison, but it's a very
  interesting dataset nonetheless.
image: https://cdn.mos.cms.futurecdn.net/fqE7uiQeMahN3tCxTd8qRV-1999-80.jpg
categories:
- Technology & Software
- Hardware
people:
- Tom
- Wendell
- Zak Killian
- Zen
locations:
- Venice
organisations:
- AMD
- BTW
- CCD
- CPU
- Epyc
- Get Tom's Hardware
- Google News
- HotHardware
- IPC
- NPU
- PC
- RAM
- The Tech Report
- Tom's Hardware
- Zak
---

![A photograph of someone holding an AMD Venice processor without its mounted heatspreader.](https://cdn.mos.cms.futurecdn.net/fqE7uiQeMahN3tCxTd8qRV-1920-80.jpg)

AMD's Zen 6 processors are out! Well, the EPYC 9006 family of server CPUs is out, anyway. These aren't chips that mere mortals like you and I can reasonably acquire, so there aren't really many third-party benchmarks out there yet, but somebody ran GeekBench 7 on one, and you know what that means: time for some wild speculation, such as the supposed 15% single-threaded IPC increase you might have seen reported this week. However, it isn't *quite* that clear yet. Well-known enthusiast and occasional leaker HXL (@9550pro) spotted the EPYC 9996 result, and now Russian enthusiast "three twenty six" (@326powah) has done a direct comparison with his Ryzen 7 9700X at the same clock.

Let's lay out the details: the AMD EPYC 9996 is an absolutely gargantuan server processor with 256 "Zen 6c" cores spread across eight "Monarch" CCDs with 32 cores apiece. Each CCD has 128MB of L3 cache, which is reportedly split into two 64MB domains for each 16-core CCX. This gives us 4 megabytes of L3 cache per CPU core, which happens to be the exact ratio that AMD has maintained since Zen 2. Meanwhile, 326's Ryzen 7 9700X is a desktop CPU with eight Zen 5 CPU cores and 32MB of L3 cache, giving it the same cache-per-core ratio yet an overall smaller local cache for the CPU cores, to say nothing of the 1GB of L3 cache on the full EPYC 9996.

Yes, 1GB of L3 cache. That enormous CPU is also served by a 1024-bit memory bus, likely running at 12,800 MT/s, giving it a colossal 1.64 TB/second of memory bandwidth. However, the specific benchmarks we're comparing here are single-threaded benchmarks, and as a result, they aren't likely to be bottlenecked by memory bandwidth on either machine; even 326's relatively pedestrian DDR5 memory at 6000 MT/s CL34 is more than sufficient for a single-threaded, lightly vectorized workload like Geekbench 7. Matching the CPU core clock rates at 4.1 GHz actually gives us a pretty decent core-to-core comparison of performance, even if all factors are not equal.

![A cropped version of a Geekbench 7 single-core benchmark comparison, showing the new EPYC Venice processor beating a Ryzen 7 9700X desktop CPU.](https://cdn.mos.cms.futurecdn.net/dW6AtZikRQ52dYnJxYHdVS-1024-80.png)

So how does it come out? Frankly, it's a massacre. That's true whether we look at the Windows 11 results he posted first or the CachyOS Linux results that he posted later, although the Zen 5 part doesn't get embarrassed *quite* as badly in Linux. The Dell PowerEdge R9815 server hosting the big EPYC part scored 2847 in the single-threaded test; 326's Ryzen desktop scores 2483 in Linux and 2318 in Windows.

Looking at the Gala-to-Honeycrisp Linux results, the biggest performance gulf is some 24% in the HTML5 Browser test, which is normally quite sensitive to memory latency. That could easily be caused by the massive L3 cache of the EPYC CPU. Other tests aren't so easily dismissed by configuration mismatches, though. The 19% gain in asset compression, the 21% gain in video encoding, and the 17% gain in photo editing all point to real architectural differences between Zen 5 and Zen 6 that seem quite promising for its desktop debut next year.

What's fascinating is that these results won't have been affected much by the considerable SIMD horsepower of the Zen 6 CPU core, as Geekbench—at least historically speaking—makes relatively light use of CPU SIMD, and in fact, this specific test is marked as "AVX2," meaning it definitely isn't using the muscular AVX-512 units present in either CPU. In fact, most of these tests are actually measuring CPU integer arithmetic and memory subsystem performance more than raw CPU number-crunching power, so Zen 6 coming out so far ahead here is really interesting.

![A cropped version of a Geekbench 7 single-core benchmark comparison, showing the new EPYC Venice processor beating a Ryzen 7 9700X desktop CPU.](https://cdn.mos.cms.futurecdn.net/JxFPe52zfaYTDu5sAa6aKV-1024-80.png)

Obviously, you shouldn't take this as gospel that "Zen 6 has 15% higher IPC than Zen 5," though that's arguably a plausible conclusion; there are just too many confounding factors to say that so far. Indeed, another one of those factors is that this isn't the Zen 6 CPU core that we'll be getting in desktop CPUs. The EPYC 9996 is a high-density part that uses Zen 6c, the specialized dense core design meant for increased area efficiency at the cost of its ability to scale to high clocks. After all, 4.1 GHz isn't exactly a high clock rate these days, and particularly not for chips manufactured on a bleeding-edge 2nm-class manufacturing process.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

That's the part that should get you excited. Zen 5 had a very modest IPC uplift over Zen 4 (including even some regressions), and combined with a similarly modest clock rate gain, it wasn't a very exciting release for most desktop users. Zen 6 seemingly may have a significant IPC advantage as well as, if rumors hold, a fairly extreme clock jump over the current-generation parts. If that holds, this may be another leap like from Core 2 to Core i7, and these parts are confirmed to be coming to an AM5 socket near you. We'll be waiting with bated breath for the launch early next year. Hopefully there's RAM to buy by that point.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Zak Killian](https://cdn.mos.cms.futurecdn.net/yonJziSpjzVFahKcUonJvi-140-80.jpg)

Zak is a freelance contributor to Tom's Hardware with decades of PC benchmarking experience who has also written for HotHardware and The Tech Report. A modern-day Renaissance man, he may not be an expert on anything, but he knows just a little about nearly everything.

* It's nice to finally get a potentially independent glimpse into Zen 6 performance, but I'm not getting my hopes up before I see some more serious 3rd party benchmarking & analysis of Venice.  
    
  In the lead up to every new AMD CPU release, it seems the fan community has a way of talking themselves into unrealistic performance expectations. I'd rather keep expectations low and be pleasantly surprised.  
    
  BTW, based on much earlier numbers AMD officially released, I had estimated an IPC gain of 10-11%. So, that's a counterpoint to hopefully help relax expectations. Even that much would be quite nice, when compounded by a clock speed boost and core count increase. Reply
* bit\_user said:In the lead up to every new AMD CPU release, it seems the fan community has a way of talking themselves into unrealistic performance expectations. I'd rather keep expectations low and be pleasantly surprised.  
    
  BTW, based on much earlier numbers AMD officially released, I had estimated an IPC gain of 10-11%. So, that's a counterpoint to hopefully help relax expectations. Even that much would be quite nice, when compounded by a clock speed boost and core count increase.It probably won't be too long before someone like Wendell gets their hands on Zen 6 Epyc and the IPC picture will become clear. Probably averaging somewhere between 10-15%. Assume lower to be safe.  
    
  +50% cores and +50% L3 cache is locked in, we're good there. It will be interesting to see the effects of 144 MiB X3D for gaming.  
    
  The real mystery remains the turbo/all-core clock speeds. If those are impressive, that's how we could plausibly arrive at a 2x MT increase between the 9950X and 24-core Zen 6.  
    
  Then there are some minor details, like new instruction sets (probably won't be used by many initially), rumored removal of the iGPU, rumored addition of an NPU, memory controller improvements (ideally it should have good support for CQDIMMs), etc. Reply
