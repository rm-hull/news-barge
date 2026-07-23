---
title: AMD’s new X100 chip lineup puts Strix Halo into robots – APUs for physical
  AI bring Zen 5 CPU, RDNA 3.5 GPU cores to compete with Intel’s Panther Lake
source_url: https://www.tomshardware.com/pc-components/cpus/amds-new-x100-chip-lineup-puts-strix-halo-into-robots-apus-for-physical-ai-bring-zen-5-cpu-rdna-3-5-gpu-cores-to-compete-with-intels-panther-lake
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-23T21:06:52Z'
published: '2026-07-23T00:00:00Z'
description: AMD takes on Intel (and Nvidia) in the robot wars.
image: https://cdn.mos.cms.futurecdn.net/pXkThAfC4PkTjFgvWAPXYF-2560-80.jpg
---

![AMD X199 chip.](https://cdn.mos.cms.futurecdn.net/pXkThAfC4PkTjFgvWAPXYF.jpg) 

AMD is bringing its Strix Halo APUs into the world of physical AI. The new X100 series of processors come with similar specs as the various Ryzen AI Max models floating around in client devices, but they’re tailored for 24/7 operation, with a 10-year lifecycle in embedded applications like robotics.

There are three SKUs that align with the three __original Strix Halo models__ (not the updated versions with 40 CUs). The top-end X199 comes with 16 Zen 5 cores and 40 RDNA 3.5 CUs. The X188 steps down to 12 cores and 32 CUs, while the X168 comes with eight cores and the same 32 CUs. AMD hasn’t shared detailed specifications for each model, but the company says the range goes up to a 5.1 GHz boost clock and 128 GB of unified memory. They also include an XDNA 2 NPU with up to 50 TOPS, a configurable TDP between 45W and 120W, and operating temperature between -40 degrees Celsius up to 105 degrees.

![AMD X100 lineup.](https://cdn.mos.cms.futurecdn.net/hEUbwL3Ha2sH65yFnXJNdX-1200-80.jpg) 

![AMD X100 lineup.](https://cdn.mos.cms.futurecdn.net/sgNqFMqK6nFXGvjSqVXicX-1200-80.jpg) 

![AMD X100 lineup.](https://cdn.mos.cms.futurecdn.net/E6Hy6GArDQNabwASywUSdX-1200-80.jpg) 

![AMD X100 lineup.](https://cdn.mos.cms.futurecdn.net/hEUbwL3Ha2sH65yFnXJNdX-1280-80.jpg) 

![AMD X100 lineup.](https://cdn.mos.cms.futurecdn.net/sgNqFMqK6nFXGvjSqVXicX-1280-80.jpg) 

![AMD X100 lineup.](https://cdn.mos.cms.futurecdn.net/E6Hy6GArDQNabwASywUSdX-1280-80.jpg) 

AMD’s range bites back at Intel, which launched a range of __Panther Lake SoCs for physical AI__ at the beginning of the year. Both make an argument for SoCs in robotics, reducing latency when the CPU, AI accelerator, and memory are fragmented across separate chips. The X100 range is just physically larger than Panther Lake, packing much more silicon on the SoC for more powerful deployments.

 ![AMD X100 performance.](https://cdn.mos.cms.futurecdn.net/6ghhN5hWNXDpjhQ38jgRpb.jpg) 


The company shared a range of benchmarks comparing the flagship X199 against Intel’s Core Ultra X7 358H, a 16-core chip with Intel’s Arc B390 iGPU that has 12 Xe3 cores. AMD claims a lead of 1.2X and 1.3X, respectively, in GeekBench 6.1 and PassMark, as well as 1.5X in an unofficial SPECrate 2017 run looking at integer workloads. In graphics, AMD unsurprisingly takes the edge with 1.4X faster Vulkan and 1.7X faster OpenGL performance (both measured with GFXBench 5 on Ubuntu), as well as a 1.6X lead in Unigine Heaven Extreme.

On the physical AI front, AMD claims a 1.4X improvement in Time to First Token (TTFT) and 3.5X faster tokens per second in Llama-bench, with a Vulkan backend running at a 45W TDP. These results need a massive dash of salt, however.

AMD tested the Ryzen AI Max 395+ “configured to reflect Ryzen AI Embedded X199 specifications.” It tested on the Maple reference board with a 5.1 GHz CPU clock, 2.9 GHz GPU clock, and sustained 45W TDP. The X7 358H, meanwhile, was tested in an MSI Prestige 16 Flip AI+ with an enforced TDP limit of 30W. AMD then “projected” 45W performance on the Intel chip “using scaling factors derived from public benchmark data.”

It’s not exactly an apples-to-apples comparison, in other words. There’s some sort of proxy stand-in or extrapolation of data across all of the benchmarks here, so keep that in mind as we work through the rest of AMD’s X100 announcements.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

## AMD X100 Kria SOM and robotics developer platform

![AMD Kria AI developer box.](https://cdn.mos.cms.futurecdn.net/U3UDXxuAcJyg2cLnss9niV-1200-80.jpg) 

![AMD Kria SOM.](https://cdn.mos.cms.futurecdn.net/9sPH3tmCzcVsbEbQQLkUx4-1200-80.jpg) 

![AMD Kria SOM.](https://cdn.mos.cms.futurecdn.net/s45LUio7r6BTgATjZEDmv4-1200-80.jpg) 

![AMD Kria SOM.](https://cdn.mos.cms.futurecdn.net/hMcDhjXEysRMmMAfXCdTw4-1200-80.jpg) 

![AMD Kria AI developer box.](https://cdn.mos.cms.futurecdn.net/U3UDXxuAcJyg2cLnss9niV-1280-80.jpg) 

![AMD Kria SOM.](https://cdn.mos.cms.futurecdn.net/9sPH3tmCzcVsbEbQQLkUx4-1280-80.jpg) 

![AMD Kria SOM.](https://cdn.mos.cms.futurecdn.net/s45LUio7r6BTgATjZEDmv4-1280-80.jpg) 

![AMD Kria SOM.](https://cdn.mos.cms.futurecdn.net/hMcDhjXEysRMmMAfXCdTw4-1280-80.jpg) 

utside of the chips themselves, AMD is offering X100 models as part of a Kria System on Module (SOM) or an integrated robotics developer platform. The Kria X100 board measures 120mm x 120mm and conforms to the standardized COM-HPC form factor. If you’re a developer that wants to develop for the board, AMD is offering its Kria AI robotics developer platform.

It’s a fully-integrated box, leveraging the X100 Kria SOM alongside AMD’s Spartan UltraScale+ FPGA baseboard. AMD says it’s a “turnkey” solution for robotics development, including specialized connectivity for cameras and industrial networking, along with robotic sensors. The platform is available in early access now, and AMD says it’ll be in full production in Q4 of this year. .

 ![Performance of AMD X100.](https://cdn.mos.cms.futurecdn.net/eoLNumc5tdpiRbWARkX8WE.jpg) 


AMD shared some benchmarks for the X100 Kria, as well, comparing it to Nvidia’s Thor T5000. These benchmarks weren’t run internally at AMD. They were commissioned by AMD and ran by Open Navigation and Mimix. Critically, the benchmarks didn’t test an X100 Kria board, or at least, not exactly in the form it will take once it’s inside a robot or AMD’s developer box.

Instead, AMD is comparing Nvidia’s Jetson AGX Thor developer kit to a GMKtech EVO-X2 AI mini PC with a Ryzen AI Max+ 395 “configured to reflect Ryzen AI embedded x199 specifications.” Naturally, the thermal and power environment of these chips will heavily influence performance.

![AMD robotics software stack.](https://cdn.mos.cms.futurecdn.net/mBrQkcLnRjntonQVkLULpK-1200-80.jpg) 

![AMD robotics software stack.](https://cdn.mos.cms.futurecdn.net/we7EBuNfwPr58GwWXNTHqK-1200-80.jpg) 

![AMD robotics software stack.](https://cdn.mos.cms.futurecdn.net/bmepgwKxZTqfZzHVTuknqK-1200-80.jpg) 

![AMD robotics software stack.](https://cdn.mos.cms.futurecdn.net/WmPRGByPmpxxkRxSksb4sK-1200-80.jpg) 

![AMD robotics software stack.](https://cdn.mos.cms.futurecdn.net/mBrQkcLnRjntonQVkLULpK-1280-80.jpg) 

![AMD robotics software stack.](https://cdn.mos.cms.futurecdn.net/we7EBuNfwPr58GwWXNTHqK-1280-80.jpg) 

![AMD robotics software stack.](https://cdn.mos.cms.futurecdn.net/bmepgwKxZTqfZzHVTuknqK-1280-80.jpg) 

![AMD robotics software stack.](https://cdn.mos.cms.futurecdn.net/WmPRGByPmpxxkRxSksb4sK-1280-80.jpg) 

AMD is continuing its attempt to siphon developers away from Nvidia’s CUDA platform for development, as well. It’s HIPIFY tool converts CUDA code to AMD’s HIP C++ portable code, and the company claims it can now handle 70-80% of the “effort” of porting on its own. AMD tested on a Ryzen AI Max+ 395, once again configured to match the X199, and it ported 15 CUDA applications, comprising 1,199 lines of code, to arrive at that 70% to 80% range.

X100 Kria lives at the “brain” of the robotics platform, but AMD envisions an end-to-end solution for humanoid-style robots with its Spartan UltraScale+. Zynq UltraScale+, and Versal AI Edge Gen 2 FPGAs and SoCs

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Jake Roach](https://cdn.mos.cms.futurecdn.net/h6PRM8bTimCTnNfoAYfjAi.jpg)

Jake Roach is the Senior CPU Analyst at Tom’s Hardware, writing reviews, news, and features about the latest consumer and workstation processors.
