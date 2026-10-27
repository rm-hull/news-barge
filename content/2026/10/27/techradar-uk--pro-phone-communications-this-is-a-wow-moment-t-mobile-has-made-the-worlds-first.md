---
title: '''This is a wow moment'': T-Mobile has made the world''s first AI-RAN call,
  and it could mean huge changes for the next generation of staying in touch'
source_url: https://www.techradar.com/pro/phone-communications/this-is-a-wow-moment-t-mobile-has-made-the-worlds-first-ai-ran-call-and-it-could-mean-huge-changes-for-the-next-generation-of-staying-in-touch
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-27T22:13:58Z'
published: '2026-10-27T00:00:00Z'
description: It won't arrive on your device any time soon though
image: https://cdn.mos.cms.futurecdn.net/YxbVxk7yFhoVTjFFA6J8QH-2560-80.jpg
categories:
- Technology & Software
people:
- Ankur Kapoor
- Fierce
- Gabriel Brown
- Jensen Huang
- John Saw
- Pallavi Mahajan
locations:
- Bellevue
- Bonn
- New York City
- Oulu
- Washington
organisations:
- 5G anyRAN
- AI
- AI-RAN Innovation Center
- ARC
- Deutsche Telekom
- Ericsson
- Fierce Network
- GPU
- Light Reading
- Nokia Massive MIMO
- Nvidia
- Omdia
- RAN
- T-Mobile CTO
- TechRadar Pro
---

![The T-Mobile Logo on a white background](https://cdn.mos.cms.futurecdn.net/YxbVxk7yFhoVTjFFA6J8QH-1920-80.jpg)

* **T-Mobile, Nokia, and Nvidia claim the first AI-RAN call through a commercial cell site in Bellevue, Washington**
* **The call ran Nokia's radio software on Nvidia GPUs, but no AI performance data was provided**
* **Commercial AI-RAN gear is due in 2027, with 6G networks expected around 2030**

T-Mobile, Nokia, and Nvidia say they have completed the world's first AI-RAN (Artificial Intelligence - Radio Access Network) call, routed through a commercial cell site in Bellevue, Washington.

The call ran over T-Mobile's live production network using a Nokia Massive MIMO radio, Nokia's 5G anyRAN software and servers built on Nvidia's Aerial RAN Computer (ARC) platform.

This wasn't a lab rig with test handsets, either, but a real-world setup that held; according to Nvidia's announcement, the site connected to T-Mobile's existing 5G Standalone core and a commercial smartphone.

## What is an AI-RAN and why is it relevant now?

The radio access network (RAN) is the part of a mobile network your phone actually talks to: the antennas, radios, and baseband computers that process signals at each cell site. That processing has traditionally run on custom chips.

AI-RAN moves it onto accelerated hardware, in this case Nvidia GPUs running Nokia's CUDA-based radio software, so the same box can run AI models that fine-tune the radio link and, in theory, rent out spare capacity to other AI jobs.

The prize on offer is spectral efficiency, or more data squeezed through the same slice of airwaves. In a blog post about the call, Nokia's chief technology and AI officer Pallavi Mahajan writes, "With AI-RAN, we are on a path to 2x spectral efficiency."

Nokia's July 2026 platform launch claims gains of more than 20% efficiency gains so far, without saying where they were measured, and puts 50% on the calendar for 2027 and more than 100% for 2028.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Interestingly, while the tests worked in principle, details remained limited on actual throughput, latency, or efficiency figures from any of the three major players. Put simply, the call shows Nokia's radio stack can run on Nvidia silicon in a live network without dropping anyone.

It doesn't yet show that the AI makes your calls any better. The most concrete numbers for the Nokia and Nvidia platform, ironically, came from a lab: Deutsche Telekom reported typical uplink throughput gains of 10% to 15% from AI-based channel estimation in initial tests in Bonn and Oulu, with a field trial still to come.

The timing is also awkward for those pushing GPUs as an eventuality here; A day before Nokia's post, T-Mobile chief network officer Ankur Kapoor published results from AI-managed beamforming trials with Ericsson in New York City, with the AI model running on Ericsson's own silicon rather than Nvidia GPUs. At peak hours, T-Mobile reported a 16% improvement in downlink user throughput and 12% better spectral efficiency.

Those figures are company-reported, and when Fierce Network asked how many sites were involved, T-Mobile did not specify a number.

Despite this, Omdia senior principal analyst Gabriel Brown told Light Reading, "This is a wow moment," adding that the gains came from software updates to equipment already in the field. T-Mobile and Ericsson had already reported close to 10% better spectral efficiency from a separate AI scheduler in May, again with no GPUs involved.

T-Mobile is clearly backing both horses, as it opened its AI-RAN Innovation Center with Nvidia, Ericsson, and Nokia in 2024. Kapoor's post argues that "AI-RAN is a continuum, not a single product," and he told Fierce the carrier is developing AI-RAN software with both vendors.

For anyone actually making calls, nothing changes yet. Your voice sounds the same, and any benefit arrives as extra capacity in crowded places rather than as a new feature. Nokia's AI-RAN products enter pilot deployments around the end of this year, with commercial availability slated for 2027.

T-Mobile CTO John Saw, who favored field trials, said they would help the carrier get "a sense of what the total cost of ownership is," and is aiming to keep expectations in check. When asked about Nokia's spectral efficiency claims, he told Fierce that "the proof is going to be in the pudding." The Bellevue test shows the plumbing works, but scale has yet to be played out.

Whether the AI earns its keep is arguably a more crucial test, and it has yet to play out. But that hasn't stopped Jensen Huang from framing it a few days ago: telecom networks were built for conversations, and "Now, they will also carry the world's intelligence."

Every cell site that gets a GPU is a sale for Nvidia as it chases its next multi-billion-dollar growth idea, betting on reprogrammable AI infrastructure and continuing to target custom ASICs in multiple industries.
