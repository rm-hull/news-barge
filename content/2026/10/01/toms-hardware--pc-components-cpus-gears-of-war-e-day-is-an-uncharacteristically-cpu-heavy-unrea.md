---
title: Gears of War E-Day is an uncharacteristically CPU-heavy Unreal Engine 5 game
  — benchmarking 25 CPUs from Intel and AMD and investigating ‘low core mode’
source_url: https://www.tomshardware.com/pc-components/cpus/gears-of-war-e-day-is-an-uncharacteristically-cpu-heavy-unreal-engine-5-game-benchmarking-25-cpus-from-intel-and-amd-and-investigating-low-core-mode
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-01T20:26:43Z'
published: '2026-10-01T00:00:00Z'
description: Unreal Engine 5 doesn’t normally stress your CPU, but Gears of War E-Day
  will.
image: https://cdn.mos.cms.futurecdn.net/2qVo9H5Fz7jR8Nxu4CGDtB-1920-80.jpg
categories:
- Technology & Software
- Hardware
- Video Gaming
people:
- Jake Roach
locations:
- Arrow Lake
- Arrow Lake Refresh
- Raptor Lake
organisations:
- AAA
- AMD
- Admin
- Alamengda
- Alder Lake
- Arrow Lake
- BIOS
- CPU
- GPU
- Get Tom's Hardware
- Intel
- MSI
- Microsoft
- Nvidia GeForce
- Nvidia GeForce RTX
- PSU
- Raptor Lake
- ReBAR
- Tom’s Hardware
- UE
- UE5
- VBS
- Virtualization-Based Security
- X3D
- Zen 5
---

![Gears of War E-Day](https://cdn.mos.cms.futurecdn.net/2qVo9H5Fz7jR8Nxu4CGDtB-1920-80.jpg)
![](https://cdn.mos.cms.futurecdn.net/fsmmX34yhrKZwE44QQk7Qg-200-100.png)

Unreal Engine 5 isn’t particularly heavy on the CPU, but *Gears of War E-Day* changes that narrative. If you have a monitoring overlay open when you load into the game, you’ll immediately notice your CPU pinned at between 80% and 90% utilization, which is a far cry from most other UE5 titles. Even stranger is that the scaling between CPUs is clear. For instance, the Ryzen 7 9800X3D netted 42% higher performance than the Ryzen 5 7600X at 1080p with the High graphics preset.

We’ve tested a lot of UE5 games with our pool of CPUs to evaluate them, not only for our rankings of the best CPUs for gaming, but also for our ongoing CPU benchmark hierarchy. Most of them haven’t made the cut, simply because of a lack of scaling. We’ve tried to include games like *Clair Obscur: Expedition 33, The Elder Scrolls IV: Oblivion Remastered,* and*Halo: Campaign Evolved,* due to the prevalence of Unreal Engine 5 in modern AAA games, but the CPU scaling just doesn’t matter.

There are some exceptions, notably *Marvel Rivals* with its dense fighting arenas, large teams, and destructible environments, and*The Blood of Dawnwalker,* which has a large, sparsely populated city in the middle of the map that will bring most CPUs to their knees. Even then, however, these UE5 games don’t show the same level of scaling as other games in our test suite, such as*Starfield* or*Baldur’s Gate 3.*

*Gears of War E-Day* is an exception. It’s not only demanding on the CPU, easily spiking even the Ryzen 7 9800X3D to full utilization at 1080p, it also shows scaling across a wide pool of chips. And further, this is true even at the game’s Ultra preset (though not the Ludicrous preset, which we’ll dig into later). This heavy CPU burden was consistent throughout the opening hours of the game, as well, regardless of scene complexity or interactions.

If you're interested in GPU performance, make sure to check out our *Gears of War E-Day* GPU benchmarks, as well.

### Gears of War E-Day CPU benchmarks

We tested *Gears of War E-Day* on the same test systems we use for CPU reviews, short of the GPU driver, which we changed for this benchmarking session (the game won’t launch without the Game Ready driver). Otherwise, everything is identical, down to the frozen OS images we use across AMD and Intel test systems.

As usual, we tested with the RTX 5090 Founders Edition at 1080p to showcase the differences between each CPU. We ran a handful of chips at 1440p, as well, to get an idea of how performance scales at a higher resolution. We omitted 4K, as our graphics analysis of the game showed that it was completely GPU-bound at that high of a resolution. Go figure.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Gears of War E-Day Benchmark.](https://cdn.mos.cms.futurecdn.net/A4SuX3xnL3CE5x3xEmrg89-1200-80.png)

Before getting to the scaling benchmarks, we looked at scene performance and preset performance in *E-Day.* The game includes a built-in benchmark, common for titles published by Microsoft, so the first step to evaluating performance is ensuring that the benchmark actually matches in-game performance. It doesn’t, but it’s not far off.

As you can see, we saw slightly higher performance with our two in-game scenes than we did in the benchmark, likely due to the benchmark’s sweeping camera angle that draws much more than you’ll ever actually see on screen. We stuck with an in-game scene (scene 2) for testing, but the benchmark is a good approximation of what’s actually in the game.

![Gears of War E-Day graphics presets.](https://cdn.mos.cms.futurecdn.net/YkrjV2rvwNX29oMk3mCdZE-1200-80.png)

For graphics settings, we went with the High preset. *Gears of War E-Day* includes five presets, and we tested the top four to see where the scaling starts and stops. The dynamic is binary. If you’re using the Ludicrous preset, the scaling between CPUs goes down drastically. We saw a 6.8% difference between the 9800X3D and 9600X with the Ludicrous preset. At the Ultra preset, that jumped up to nearly a 29% difference, which grows further at the High preset.

We eventually settled on High, as that’s the visual floor for becoming CPU-bound. Going down to Medium nets very little extra performance and slightly exaggerates the scaling between chips. High, then, is a good compromise. It shows near-maximum scaling between CPUs without being an unreasonable test case.

![Gears of War E-Day benchmarks.](https://cdn.mos.cms.futurecdn.net/KthUCCsGE9gNEtHcsWCMPK-1200-80.png)

It should come as no surprise that the Ryzen 7 9800X3D and Ryzen 7 7800X3D occupy the top two spots on our chart. *E-Day,* like a lot of titles, is accelerated by X3D chips. You can see that with the Ryzen 7 5800X3D much lower down the chart, as well. What’s interesting here is how*E-Day* scales with core count, however. Take the Ryzen 5 7600X as an example. We expect less than a 5% jump with the Ryzen 7 7700X on average, but in*E-Day,* that increase nears 9%.

Elsewhere, the 12-core Ryzen 9 models usually underperform their 8-core counterparts in games. Again, the 7900X and 7700X are in lockstep, while the 9900X is 3.5% ahead. It’s worth stressing that, based on our data, the Ryzen 9 9900X and 7900X are *slower* than the straight eight-core models from AMD’s last two generations. The fact that they’re ahead here speaks to the importance of core count in this game.

Perhaps the greatest evidence of that comes from the Intel camp. Not only do we see Intel’s main Raptor Lake and Arrow Lake stack outperforming all but AMD’s X3D Zen 4 and Zen 5 CPUs, we also see strange comparisons between Arrow Lake and Arrow Lake Refresh. The Core Ultra 5 250K Plus is typically around 5% faster than the Core Ultra 7 265K on average in games. Here, the situation is flipped, with the Core Ultra 7 265K leading by about 2%.

It’s interesting to see core count as a performance driver, which isn’t usually the case in games past six or *maybe* eight cores. Although*E-Day* scales past that point, it still plateaus around 150 FPS.

We ran a few tests at 1440p, as well, foregoing the whole pool simply for the sake of time. For scaling comparisons, the Core Ultra 7 270K Plus is about 18% faster than the Core i5-14400 at 1440p, but it’s about 36% faster at 1080p. Further, that scaling isn’t consistent. Running CPUs at 1440p with our test suite and settings, we found a ceiling around 130 FPS where performance becomes bound by the GPU. Any CPUs that performed above that mark at 1080p normalized to that 130 FPS, while CPUs below that mark offered performance at 1440p within a few frames of the 1080p performance.

When looking at a weak CPU compared to a strong one, there’s clear scaling at 1440p. However, with CPUs within similar product ranges and families, the game is mostly bound to GPU performance at the higher resolution.

![Gears of War E-Day benchmarks.](https://cdn.mos.cms.futurecdn.net/Pyitz7NxTGgeGNVehXUAyR-1200-80.png)
![Gears of War E-Day benchmarks.](https://cdn.mos.cms.futurecdn.net/mJwbT2crDNr2hCJLUGth5S-1200-80.png)
![Gears of War E-Day benchmarks.](https://cdn.mos.cms.futurecdn.net/j8RtDM7BCxiejGohxH8Y4S-1200-80.png)
![Gears of War E-Day benchmarks.](https://cdn.mos.cms.futurecdn.net/5DCYcukyj2Dzhdecw9F84S-1200-80.png)
![Gears of War E-Day benchmarks.](https://cdn.mos.cms.futurecdn.net/Pyitz7NxTGgeGNVehXUAyR-2560-80.png)
![Gears of War E-Day benchmarks.](https://cdn.mos.cms.futurecdn.net/mJwbT2crDNr2hCJLUGth5S-2560-80.png)
![Gears of War E-Day benchmarks.](https://cdn.mos.cms.futurecdn.net/j8RtDM7BCxiejGohxH8Y4S-2560-80.png)
![Gears of War E-Day benchmarks.](https://cdn.mos.cms.futurecdn.net/5DCYcukyj2Dzhdecw9F84S-2560-80.png)

Looking at other aspects of performance, there aren’t any surprises. Power use is in line with our expectations, with AMD’s Zen 4 and Zen 5 flagships sitting alongside Intel’s most powerful Raptor Lake chips. And, on the efficiency front, the Ryzen 7 9800X3D and 7800X3D easily win the day with nearly two frames per watt used. Temperatures stayed in check, as well, with even the highest chip in our test pool averaging just 65.4 degrees Celsius.

### Investigating ‘low core mode’ in Gears of War E-Day

Buried in the “System” menu of the settings in *E-Day,* there’s a curious option called Low Core Mode. The game says in the setting’s description that it can improve performance on low core count devices and handhelds, which is worthy of closer inspection. This isn’t a standard UE5 toggle — as we’ve established, the engine is not particularly heavy on the CPU at stock — and we haven’t seen similar settings, at least among most recent AAA releases.

We ran each chip through another pass of tests with this mode turned on, using the same test scene and settings, to see how it impacts performance. It universally lowered performance across our entire pool of 25 CPUs, even going down to the quad-core Core i3-14100. 1% low performance wasn’t improved either. For the sake of clarity, we’ve laid out the results in a table below so you can easily see the performance change between toggling Low Core Mode on and off.

|  |  |  |  |
| --- | --- | --- | --- |
| Low Core Mode performance |  |  |  |
| Row 0 - Cell 0 | **Stock**|** Low Core**|** Change** |
| **Core Ultra 5 225** | 116.8 | 100.3 | -14.1% |
| **Core Ultra 5 245K** | 138.7 | 111.1 | -19.9% |
| **Core Ultra 5 250K Plus** | 144.3 | 113.4 | -21.4% |
| **Core Ultra 7 265K** | 147.5 | 114.4 | -22.4% |
| **Core Ultra 7 270K Plus** | 151.6 | 120.2 | -20.7% |
| **Core Ultra 9 285K** | 149.9 | 117.3 | -21.7% |
| **Ryzen 7 2700X** | 64.2 | 48.9 | -23.8% |
| **Ryzen 5 5500** | 72.3 | 54.7 | -24.3% |
| **Ryzen 7 5700X** | 89.3 | 65.3 | -26.9% |
| **Ryzen 7 5800X3D** | 117.7 | 80.4 | -31.7% |
| **Ryzen 5 7600X** | 118.7 | 90.2 | -24.0% |
| **Ryzen 7 7700X** | 128.8 | 92.9 | -27.9% |
| **Ryzen 7 7800X3D** | 153.8 | 110.4 | -28.2% |
| **Ryzen 9 7900X** | 126.4 | 96.7 | -23.5% |
| **Ryzen 9 7950X** | 130.6 | 99.7 | -23.7% |
| **Ryzen 5 9600X** | 122.4 | 100.2 | -18.1% |
| **Ryzen 7 9700X** | 132.4 | 104.7 | -20.9% |
| **Ryzen 7 9800X3D** | 168.7 | 133.1 | -21.1% |
| **Ryzen 9 9900X** | 137.1 | 109.3 | -20.3% |
| **Ryzen 9 9950X** | 139.7 | 110.9 | -20.6% |
| **Core i3-14100** | 90.1 | 79.2 | -12.1% |
| **Core i5-14400** | 111.9 | 92.7 | -17.2% |
| **Core i5-14600K** | 140.2 | 114.7 | -18.2% |
| **Core i7-14700K** | 150.8 | 119.6 | -20.7% |
| **Core i9-14900K** | 149.3 | 121.6 | -18.6% |

With everything down to a strict quad-core tested — *E-Day*’s system requirements bottom out at hexa-core chips — we assumed the situation was settled and were content to leave Low Core Mode for others to explore further. However, we gave it one more try with the Core i3-14100, disabling two of the cores in the BIOS to see how the game would function with a dual-core chip.

![A scene from Gears of War E-Day.](https://cdn.mos.cms.futurecdn.net/ofgq3DC6fL4ELyUfWNfT7j-1200-80.jpg)

That revealed a lot about what’s going on behind the scenes with this feature. Above, you can see a screenshot we gathered when booting into the game with the dual-core 14100. The texture streaming system completely breaks. We didn’t wait for an opportune moment to capture this screenshot, either; the low-res, half-loaded assets persisted throughout the entire run.

Further, whenever we went to pause the game to adjust settings or reload the checkpoint, the game froze and hung for upwards of 30 seconds before the menu appeared. Turning on Low Core Mode resolved both the asset streaming issue and the game freezing, as well as improved performance by 30%. That’s impressive, but keep in mind that going from four cores to two on the 14100 resulted in a 59% decrease in performance, dropping from an average of 89 FPS to just 36 FPS.

![Gears of War E-Day performance on CPU.](https://cdn.mos.cms.futurecdn.net/jGP6avC2ZuqJVabz94wEa4-1200-80.png)

It appears *E-Day* switches up the streaming system with Low Core Mode. That would explain a lot, notably the heavy, all-core demand when running the game normally and the severe streaming issue we noted at two cores.*E-Day* is using some sort of asset streaming system, as most modern games do, and those assets look*very expensive.* Past a certain point, the streaming simply breaks as the CPU is overloaded with work.

Although we didn’t notice a performance improvement at four cores, keep in mind that we’re testing with the newest true quad-core on the market. The 14100 is one of the best budget CPUs, but it’s still new. The system requirements call for an older hexa-core chip at minimum. Taken together, you may run into issues with older quad-cores that necessitate the use of Low Core Mode, but those situations are few and far between. Assuming you have a relatively recent processor, or a processor with at least six cores, and ideally both, Low Core Mode will reduce your performance.

We didn’t test mobile chips, however, nor the handhelds those chips are inside of. This mode may have more practical applications there.

### Test configuration

As mentioned, we used the same platform for testing *Gears of War E-Day* that we use for a CPU reviews, which you can find in the table below. All configuration and software is duplicated across all test systems, and AMD and Intel configurations never touch each other to avoid any conflicts.

There are a few important configuration details worth highlighting outside of the broad strokes of a frozen OS image. We disable Virtualization-Based Security (VBS) for all platforms, enable ReBAR, and enable XMP/EXPO. We've tested the memory to ensure stability with our platforms.

We also disable any automatic overclocking features that are unstable or not covered by warranty. For instance, we disable AMD's Precision Boost Overdrive and Intel's Extreme power profile, as neither is covered by warranty. Intel's Core Ultra 200S Boost, on the other hand, *is* covered by warranty, so we enabled it on the Arrow Lake chips we tested. Similarly, the 9600X and 9700X from AMD have a warrantied 105W operating mode, which we use, as it improves gaming performance slightly.

|  |  |
| --- | --- |
| **Intel LGA 1851 (Arrow Lake and Refresh)** | Row 0 - Cell 1 |
| Motherboard | ASRock Z890 Taichi |
| RAM | 2x16GB G.Skill Trident Z Neo RGB DDR5-7200 |
| **Intel LGA 1700 (Raptor Lake, Alder Lake)** | Row 3 - Cell 1 |
| Motherboard | MSI MPG Z790 Carbon Wi-Fi |
| RAM | 2x16GB G.Skill Trident Z Neo RGB DDR5-7200 |
| **AMD AM5 (Zen 5, Zen 4)** | Row 6 - Cell 1 |
| Motherboard | Gigabyte Aorus X870E Elite X3D ICE |
| RAM | 2x16GB G.Skill Trident Z Neo RGB DDR5-6000 |
| **AMD AM4 (Zen 3)** | Row 9 - Cell 1 |
| Motherboard | Asus Tuf Gaming X570-Pro Wi-Fi |
| RAM | 4x8GB G.Skill Trident Z RGB DDR4-3200 |
| **All Systems** | Row 12 - Cell 1 |
| Gaming CPU | Nvidia GeForce RTX 5090 Founder’s Edition |
| Application GPU | Nvidia GeForce RTX 2080 Ti Founder’s Edition |
| Cooler | Corsair iCue Link H150i RGB |
| Storage | 2TB Sabrent Rocket 4 Plus |
| PSU | MSI MPG A1000GS, Gigabyte UD1000GM PG5 V2 |
| Other | Arctic MX-4 TIM, Windows 11 Pro, Alamengda open test bench |

![Jake Roach](https://cdn.mos.cms.futurecdn.net/h6PRM8bTimCTnNfoAYfjAi-140-80.jpg)

Jake Roach is the Senior CPU Analyst at Tom’s Hardware, writing reviews, news, and features about the latest consumer and workstation processors.

* This isnt the type of game that should be this CPU heavy.Reply  
    
  Between this CPU issue and the preference for Nvidia looks like another hard pass for me.  
  Just wont be a good experience all around with all the other BS injected into the game by the devs.
* You realize most people aren't going to run this game at 1920x1080 unless that is their limit. So yea the greatest statistical variances occur at HIgh and 1080p but it would have been nice to see what the performance numbers were at "real" world resolutions 1440 and 4K anyway and all levels of complexity.Reply
* * Reply
    I agree. Showing some more mainstream type CPUs, along with some mid to high end GPU's to add some reference points would be good.Vicecrow said:Some times i Just want a 5060 in the Review 99% people out there want to know what cpu tô pair with a 5060 RX 9060
  * * Reply
      [https://www.tomshardware.com/video-games/pc-gaming/gears-of-war-e-day-pc-graphics-performance-tested-43-gpus-take-us-back-to-the-start-of-an-iconic-sagaVicecrow](https://www.tomshardware.com/video-games/pc-gaming/gears-of-war-e-day-pc-graphics-performance-tested-43-gpus-take-us-back-to-the-start-of-an-iconic-sagaVicecrow) said:Some times i Just want a 5060 in the Review 99% people out there want to know what cpu tô pair with a 5060 RX 9060  
      The 5060 hits 55 FPS at 1080p ultra..........you can put any old CPU in and it will reach that.  
      Now if you are going to play with the settings until you get the max FPS you can possibly get with your 5060 then this CPU comparison is what you need to see which CPU in your budged might get you the best FPS.
    * Reply
      How does the 9800x3d easily win in efficiency if it loses to the intel CPU?! (5 225)Admin said:And, on the efficiency front, the Ryzen 7 9800X3D and 7800X3D easily win the day with nearly two frames per watt used. Temperatures stayed in check, as well, with even the highest chip in our test pool averaging just 65.4 degrees Celsius.  
        
      FIFY  
      the Ryzen 7 9800X3D 7800X3D and the intel ultra 5 225 easily win the day with nearly two frames per watt used with the 9800x3d being a close third  
      What in lords name is the definition of a strict quad core?!?!Admin said:With everything down to a strict quad-core tested —*E-Day*’s system requirements bottom out at hexa-core chips — we assumed the situation was settled and were content to leave Low Core Mode for others to explore further. However, we gave it one more try with the Core i3-14100, disabling two of the cores in the BIOS to see how the game would function with a dual-core chip.  
      And how is it an 8 threaded CPU?!  
      Games (all software) only see threads, you turned 8 threads into 4 threads.  
      It would be super easy to check that by just running an thread observation tool like process explorer form sysinternals (part of microsoft) it could just be that it throttles (lowers the priority of) a thread that doesn't wait for the results of other threads if those other threads can't keep up, lowering the priority makes windows stall it until any thread with a higher priority is done, this throttles the performance but you get the whole of the game instead of things not loading in.Admin said:It appears*E-Day* switches up the streaming system with Low Core Mode. That would explain a lot, notably the heavy, all-core demand when running the game normally and the severe streaming issue we noted at two cores.*E-Day* is using some sort of asset streaming system, as most modern games do, and those assets look*very expensive.* Past a certain point, the streaming simply breaks as the CPU is overloaded with work.
    * Hey Jake, I think your headline is incorrect. Unreal Engine games have traditionally always/usually been CPU heavy. Yes, GPU is often more critical if you want to hit a good framerate, but in my experience UE -- whether UE3, UE4, or UE5 -- typically shows a need for higher performance CPUs when you have a fast GPU.Reply
    * Reply
      given the cost of gpu and stuff that might change unless games optimize better as most ppl arent going to buy high end gpu's anymore.warezme said:You realize most people aren't going to run this game at 1920x1080 unless that is their limit.
