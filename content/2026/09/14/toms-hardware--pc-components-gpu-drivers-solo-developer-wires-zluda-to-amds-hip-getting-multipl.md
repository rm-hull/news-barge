---
title: Solo dev enables running CUDA on AMD hardware in Windows, getting multiple
  CUDA libraries running on a gaming Radeon RX 9060 XT GPU in Windows — CUDA-exclusive
  workloads on AMD hardware in Windows possible without virtualization or dual-booting
source_url: https://www.tomshardware.com/pc-components/gpu-drivers/solo-developer-wires-zluda-to-amds-hip-getting-multiple-cuda-libraries-running-on-a-radeon-rx-9060-xt-in-windows-cuda-exclusive-workloads-on-amd-hardware-in-windows-is-possible-without-virtualization-or-dual-booting
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-14T14:59:08Z'
published: '2026-09-14T00:00:00Z'
description: It's too early to consider the CUDA moat officially drained, but this
  is definitely a yank on the plug.
image: https://cdn.mos.cms.futurecdn.net/FKEfLV3WiguWYAz37vRmyW-2560-80.png
categories:
- Technology & Software
- Hardware
- Video Gaming
locations: []
people:
- Tom
- Zak Killian
organisations:
- AMD
- CUDA
- GPU
- Get Tom's Hardware
- Google News
- HotHardware
- LibTorch/ZLUDA
- NCCL
- NVIDIA
- PC
- PPO
- Speedstu
- The Tech Report
- Tom's Hardware
- ZLUDA
- Zak
- cuDNN
---

![AMD GPU](https://cdn.mos.cms.futurecdn.net/FKEfLV3WiguWYAz37vRmyW.png) 

With the latest ROCm updates, AMD finally brought robust, official PyTorch and HIP SDK support to Windows for consumer GPUs, fully supporting the Radeon RX 7000 and the RX 9000 series. For native, supported frameworks, AMD on Windows is finally a viable reality, but what happens when you want to run a proprietary application, an older repository, or a specialized AI tool that absolutely refuses to support anything but NVIDIA's CUDA? That's where a new project, Speedstu's "CUDA-for-AMD-Windows," could save the day. It proves that running rigidly CUDA-exclusive workloads on AMD hardware in Windows is possible without virtualization or dual-booting.

To be clear, this project is not a brand-new runtime. Instead, it is a highly automated and reproducible PowerShell setup that bridges the gap between ZLUDA, the well-known, formerly AMD-funded translation layer, and AMD's native HIP/ROCm SDK for Windows. Through a series of clever scripts, the toolkit automatically detects the user's GPU architecture, grabs a specifically pinned version of ZLUDA (v6-preview.69), and, at least in theory, seamlessly maps it to the ROCm math libraries already present in Windows.

 ![A screenshot of the CUDA for AMD Windows GitHub documentation.](https://cdn.mos.cms.futurecdn.net/rC9CpYp3oSDdGA9JvAuhWG.png) 


The result is that the developer successfully intercepted and mapped the CUDA driver API as well as the cuBLAS, cuSPARSE, and cuFFT libraries directly over to their AMD equivalents. As a proof-of-concept, the author even trained a 2.2-million-parameter PPO reinforcement-learning network end-to-end using unmodified CUDA libraries on an AMD Radeon RX 9060 XT, which happens to be the only officially supported GPU at this time.

Even with AMD's official ROCm support on Windows, the local developer community frequently runs into dependency hell when trying out experimental GitHub repos or specialized AI tools that hardcode CUDA as a requirement. For developers who want to experiment with these CUDA-only tools natively on their Windows daily driver machines without dealing with WSL2 passthrough issues or waiting for the original author to write a HIP port, this project offers a highly desirable translation pipeline. It acts as a sort of hacky adapter for software that stubbornly demands an NVIDIA card.

Benchmark testing included in the project's documentation offers some interesting findings. In a controlled A/B test running a 2.2M-parameter reinforcement learning workload on a Radeon RX 9060 XT, the "public upstream path," which relies purely on official ZLUDA releases and AMD's stock HIP SDK 6.4, achieved a median throughput of 13,278 steps per second (SPS). By contrast, an optional "recovered custom overlay" apparently built from salvaged legacy ZLUDA binaries ran slightly worse at 12,876 SPS, making it roughly 3% slower. While the clean official setup is faster, the author notes that "a later rewrite removed LibTorch/ZLUDA from PPO and achieved substantially higher throughput," indicating that there is still a performance hit for this stack of translators.

| CUDA for AMD Windows Official benchmarks (BENCHMARKS.md) |  |  |  | 
|---|---|---|---|
| Metric | Public upstream | Recovered custom | Custom delta | 
|---|---|---|---|
| Overall SPS, median | **13,278.46**| 12,875.80 |**-3.03%** | 
| Overall SPS, mean | **13,172.49** | 12,649.83 | -3.97% | 
| Collection SPS, median | **63,306.00** | 59,360.67 | -6.23% | 
| Consumption SPS, median | **16,806.36** | 16,445.66 | -2.15% | 
| Inference time, median | **0.5863 s** | 0.6293 s | +7.33% | 
| PPO learn time, median | **3.2076 s** | 3.2958 s | +2.75% | 

Now, before anyone declares the CUDA moat officially drained, it is crucial to set realistic expectations. First, this is a solo open-source project, not an enterprise-grade solution. The author is extremely transparent about its narrow scope, as crucial machine learning libraries like cuDNN, TensorRT, and NCCL do not resolve yet. This means compatibility is strictly workload-dependent; if your specific AI tool relies heavily on cuDNN, this setup will fail. Furthermore, it's worth pointing out that ZLUDA itself is currently being maintained as a "weekend hobby project" after losing its commercial backing a second time. Relying on this pipeline for production-level work remains a massive risk. This repository is a tinkerer's tool, not a corporate IT deployment strategy.

Despite these limitations, "CUDA-for-AMD-Windows" is pretty exciting, as it proves that the barrier to entry for running CUDA-exclusive software on AMD GPUs isn't an insurmountable hardware flaw, but a relatively tractable translation tooling problem. Because the project is entirely open-source, its potential extends far beyond this initial proof-of-concept. With community contributions, we could see expanded hardware detection and clever patches to get more stubborn CUDA libraries resolving properly.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Zak Killian](https://cdn.mos.cms.futurecdn.net/yonJziSpjzVFahKcUonJvi.jpg) 

Zak is a freelance contributor to Tom's Hardware with decades of PC benchmarking experience who has also written for HotHardware and The Tech Report. A modern-day Renaissance man, he may not be an expert on anything, but he knows just a little about nearly everything.
