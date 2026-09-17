---
title: Apple eyes Nvidia NVLink to power its new custom M8 Ultra AI servers — historically
  bitter rivals reportedly team up for 2029 data center push
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/apple-eyes-nvidia-nvlink-to-power-its-new-custom-m8-ultra-ai-servers-historically-bitter-rivals-reportedly-team-up-for-2029-data-center-push
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-17T13:23:56Z'
published: '2026-09-17T00:00:00Z'
description: Time to bury the hatchet?
image: https://cdn.mos.cms.futurecdn.net/eEG2jWuyvKSPgs2K5yfekX-1920-80.jpg
---

![Nvidia Hot Chips 2024](https://cdn.mos.cms.futurecdn.net/eEG2jWuyvKSPgs2K5yfekX.jpg) 

Apple is reportedly developing AI servers based on its own M-series processors and is evaluating NVLink Fusion technology for interconnects, according to *The Information*. The machines are expected to use M8 Ultra processors and arrive in 2029, the report claims. For now, the usage of the NVLink Fusion platform is not formalized and has not been confirmed by either Apple or Nvidia, but if Apple decides to use it instead of competing solutions, this may have significantly broader market implications than just Apple using Nvidia hardware.

## Apple looking for fast interconnects

Apple is reportedly considering at least two server configurations: a smaller machine equipped with two M8 Ultra processors and a higher-end version featuring four M8 Ultra system-on-chips. Although Apple has its own UltraFusion technology for stitching two high-end SoCs together seamlessly, it looks like the company does not have a proper solution for scale-up and scale-out connectivity of its processors, which is where Nvidia's NVLink Fusion comes into play. Apparently, Apple wants to use NVLink infrastructure, which includes not only an interconnection protocol, but also switches, chiplets that add NVLink connectivity, and a software stack, for its servers. The project was reportedly initiated around a year ago and was backed by John Ternus while he headed Apple's hardware engineering organization.

Apple already builds custom servers for Private Cloud Compute, which handle AI workloads too demanding for local execution on iPhones and Macs, *The Information* claims. Most of these machines use Apple's internally developed connectivity technologies, which are reportedly too slow and costly for large-scale commercial deployments, which is why Apple is looking elsewhere.

## More than NVLink?

*The Information* specifically mentions Apple's need for connectivity technology suitable for large-scale deployments, although it does not explain exactly what this means architecturally. If the publication is referring to connecting multiple servers into larger clusters, this would normally be the job of scale-out technologies such as Ethernet or InfiniBand, rather than a scale-up fabric such as NVLink. Nvidia originally developed its NVLink fabric technology to scale-up performance of its accelerators, so the technology is optimized for accelerator-to-accelerator connectivity and enables a rack of Nvidia GPUs to function as a tightly coupled compute domain. There is a different implementation called NVLink-C2C, which is a coherent chip-to-chip interface for connecting CPUs to accelerators and CPUs to CPUs

Meanwhile, modern Apple M Pro and M Ultra processors are system-in-packages consisting of a CPU chiplet and a GPU/neural engine chiplet, which are stitched together using TSMC's SoIC-mH technology. If Apple continues to use this architecture (very likely), an M8 Ultra processor can be considered as a CPU and an accelerator. However, this raises the question of how Apple intends to connect M8 Ultra processors to NVLink and which components of the SiP would participate in the NVLink domain. One possibility is that Apple could expose the accelerator portion of M8 Ultra to NVLink through an NVLink Fusion chiplet, which effectively means it will treat it as an accelerator for a scale-up domain. Another possibility is that Apple is developing a different accelerator architecture for its servers, perhaps by simply placing the GPU/NPU chiplet onto a separate substrate/interposer and equipping it with its own memory, though there is currently no evidence that confirms such a design for a chip that is years away.

Another thing to keep in mind is that Apple is a member of the UALink Consortium, an organization overseeing development of industry-standard UALink accelerator-to-accelerator interconnections that supports up to 1,024 accelerators. While for now there is a limited choice of UALink switches, by 2029, there will be industry-standard switches offering different performance and capabilities, which makes the choice of NVLink as a scale-up fabric even stranger.

One possible explanation is that Apple is interested in considerably more than NVLink itself. NVLink Fusion is part of Nvidia's rack-scale and data center infrastructure architecture, which can combine NVLink scale-up connectivity with Nvidia's Spectrum-X Ethernet or Quantum-X InfiniBand scale-out networks, including switches equipped with co-packaged optics. Thus, Apple could potentially adopt Nvidia technology for both scale-up and scale-out connectivity instead of developing an entire data center networking stack of its own. This is merely speculation for now, but such an approach would effectively mean that Apple is building AI servers around significant portions of Nvidia's data center architecture while retaining its own processors and not using Nvidia accelerators. If this happens, this will be a testament that Nvidia is now setting de facto standards for AI data centers, no matter which AI accelerators and CPUs are used.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

## Burying the hatchet?

Without a doubt, Nvidia is a leading supplier of data center hardware, so it is logical for Apple to work with the company if the two companies are indeed working together on Apple's data center platform.

Apple and Nvidia are not exactly good partners. The feud between the two companies began in the early 2000s, when Steve Jobs accused Nvidia of infringing on Pixar's patents on which Nvidia responded that it owned more graphics IP than Pixar and therefore could sue the company. Later on, Apple and Nvidia had disagreements over GPU design decisions that the latter supplied to the former. However, then came 'Bumpgate' as Nvidia supplied Apple and other PC makers defective GPUs in 2007 – 2008, did not acknowledge the problem, and then resisted fully compensating Apple and other PC makers for their repair costs, which is when the relationship between the companies got especially dire. Apple continued to use Nvidia GPUs till 2014 or 2015, at which point it switched to AMD's Radeon, and then abandoned discrete third-party GPUs altogether.

More recently, Apple started to use Nvidia's hardware again. The latest Siri AI is primarily powered by Apple Foundation Models developed in collaboration with Google using Gemini technology. Server-side inference runs through Apple's Private Cloud Compute architecture, and many of the workloads are hosted on Nvidia Blackwell GPUs in Google Cloud. Yet, using Nvidia hardware in the cloud and adopting the company's technologies for your own platforms is a completely different thing.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Anton Shilov](https://cdn.mos.cms.futurecdn.net/uMZ5kNphxA2Ut6whdLaSQV.png) 

Anton Shilov is a contributing writer at Tom’s Hardware. Over the past couple of decades, he has covered everything from CPUs and GPUs to supercomputers and from modern process technologies and latest fab tools to high-tech industry trends.
