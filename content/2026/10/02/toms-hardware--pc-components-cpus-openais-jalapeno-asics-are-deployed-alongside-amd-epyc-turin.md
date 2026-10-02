---
title: OpenAI’s Jalapeño ASICs are deployed alongside AMD EPYC ‘Turin’ CPUs as hosts
  — Hardware VP says Nvidia’s Vera standalone is ‘a little bit behind… on that maturity
  level’
source_url: https://www.tomshardware.com/pc-components/cpus/openais-jalapeno-asics-are-deployed-alongside-amd-epyc-turin-cpus-as-hosts-hardware-vp-says-nvidias-vera-standalone-is-a-little-bit-behind-on-that-maturity-level
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-02T18:04:23Z'
published: '2026-10-02T00:00:00Z'
description: Hardware VP Robert Ho says the choice to use Turin was “pragmatic.”
image: https://cdn.mos.cms.futurecdn.net/9mJ37sc39kgcyEigsUfgNn-2560-80.jpg
categories:
- Technology & Software
- Hardware
people:
- Jalapeño
- Nvidia
- Richard Ho
- Tom
- Vera
locations:
- Azure
- Cobalt
- Graviton
- Turin
- Vera
organisations:
- AGI
- AMD EPYC Turin
- ARM
- AWS’ Graviton
- Axiom
- CPU
- Diamond Rapids
- Get Tom's Hardware
- Google Cloud
- Google News
- Head of Hardware
- Intel
- Nvidia
- OpenAI
- SemiAnalysis
- Tom’s Hardware
- VP
- Vera and Arm
---

![An EPYC Turin CPU sitting in a socket.](https://cdn.mos.cms.futurecdn.net/9mJ37sc39kgcyEigsUfgNn-1920-80.jpg)

OpenAI’s new Jalapeño ASIC is being deployed internally alongside AMD EPYC Turin hosts, each with 1.5TB of memory. SemiAnalysis described the rack-scale deployment of Jalapeño following the reveal of the chip, which we asked Richard Ho, VP and Head of Hardware at OpenAI, about in an interview. Ho told us that the decision to use Turin was “pragmatic,” describing Nvidia’s new Vera CPU as “a little bit behind… on that maturity level.”

“The way we approached that design was really in terms of de-risking and being able to do that design fast. Vera, as a standalone, is a little bit behind on that maturity level. The Turing device is strong. It did what we needed to do, and partly our partners had some experience with it,” Ho told *Tom’s Hardware Premium.* “For the Jalapeño program, we were trying to make very pragmatic decisions. We wanted to be aggressive on the goals of the performance and the cost, but we didn’t want to take unnecessary risks. That felt like a good design decision that would fit within the parameters of how we make these design decisions."

There are many Arm-based CPUs on the market, many of which are deployed internally at different hyperscalers, such as Google Cloud’s Axiom and AWS’ Graviton, but Vera and Arm’s own AGI have been described as agentic CPUs, purportedly accelerating the complex reasoning involved in agentic loops compared to their x86 counterparts from AMD and Intel. We asked Ho about this dynamic, and why Turin was the right choice given the close working relationship between OpenAI and Nvidia, who responded with the quote above.

Arm has long touted the virtues of the AArch64 ISA compared to x86, going as far as to claim that its own AGI CPU provides more than twice the performance of modern x86 platforms. That claim is based on internal estimates, not real benchmarks, however. The company has been naturally bullish on AGI’s adoption in the market, though even with an impressive $2 billion in commitments, analysts say the market penetration will still be in the low single digits after two years.

![Nvidia Vera CPU](https://cdn.mos.cms.futurecdn.net/rcRrMvi7TMFtUaXGwYUCh7-1200-80.jpg)

With the explosion of server CPU demand this year and evolving agentic workloads, Nvidia has been at the forefront of messaging, comparing its Arm-based Vera to the x86 competition, boldly claiming a 1.8x improvement over a competing AMD Turin chip; a figure that’s extracted from an overall benchmark suite showing Vera just 3% ahead of AMD’s EPYC 9755.

Many semi-custom Arm designs, from Graviton to Azure’s Cobalt, have focused on core density and efficiency for cloud workloads. Vera and AGI are a shift toward messaging against peak performance. In early Vera benchmarks, Nvidia’s CPU looks impressive, though we’ve yet to see the chip in action in a wide variety of workloads, much less benchmarked against AMD’s upcoming Venice CPUs or Intel’s Diamond Rapids.

What’s interesting about OpenAI’s decision to use Turin is that it’s one of Arm’s deployment partners for AGI, as well as among the list of customers “exploring the Vera CPU,” according to Nvidia. OpenAI, other frontier labs, and hyperscalers keep a wide variety of hardware in their fleet. Pairing Jalapeño specifically with Turin came down to reducing risk, with Ho pointing to the maturity of the platform.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Broadly, x86\_64 is more mature than AArch64; ARM has been around since the mid-1980’s, though a proper 64-bit extension didn’t arrive until 12 years after it was introduced on x86. And although Arm has worked its way into data centers over the past two decades, there’s still a much deeper x86 foundation reaching back several decades.

It doesn’t seem Ho’s comments were specifically on the delineation between AArch64 and x86, however. Rather, the comments are focused on the dynamic between Turin and Vera, with the latter being Nvidia’s first foray into a custom CPU core for the data center. Although the early benchmarks of Vera are impressive, it nonetheless represented an unnecessary risk for OpenAI’s rack-scale Jalapeño deployment.

Ho’s comments about OpenAI’s partners having experience with Turin expose where the thinking for the hardware team was at, as well. There are some differences in the practicality of servicing the host system between Turin and Vera, most notably the fact that Vera is board-mounted while Turin chips are socketed; swapping chips isn’t common in a server regardless, but it’s easier with Turin.

Given that OpenAI has a fleet of hardware available, it’s possible Jalapeño will be deployed with a different host system in the future, potentially paired with Arm’s AGI or Nvidia’s Vera. For now, however, Turin was the right choice.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Jake Roach](https://cdn.mos.cms.futurecdn.net/h6PRM8bTimCTnNfoAYfjAi-140-80.jpg)

Jake Roach is the Senior CPU Analyst at Tom’s Hardware, writing reviews, news, and features about the latest consumer and workstation processors.
