---
title: Startups want to rent your idle gaming PC for AI tasks — Startups pitch an
  'Airbnb for AI inference,' but profitability remains unproven
source_url: https://www.tomshardware.com/pc-components/gpus/startups-pitch-an-airbnb-for-ai-inference-that-pays-gamers-for-their-idle-pcs
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-02T12:45:48Z'
published: '2026-09-02T00:00:00Z'
description: Your idle RTX 4090 could moonlight as a chatbot.
image: https://cdn.mos.cms.futurecdn.net/ZnmibWeDaW8opTxR9rVBfE-2560-80.jpg
---

![Nvidia GeForce RTX 4090](https://cdn.mos.cms.futurecdn.net/ZnmibWeDaW8opTxR9rVBfE.jpg) 

If, like mine, your gaming rig spends most of its life doing nothing these days, a pair of startups would be willing to pay you something close to minimum wage for its downtime. Abu Dhabi-based Far Labs and Austin-based Evolving Edge are building marketplaces to farm AI inference out to idle consumer hardware, according to an *IEEE Spectrum* report.

Far Labs plans to launch its Far AI platform in the coming weeks, claiming latency of 100 ms or less, while Evolving Edge is running an open beta. "Imagine Uber or Airbnb, but for AI inference computing tasks," Ilman Shazhaev, founder and CEO of Far Labs, told the outlet. Both companies are targeting smaller open-source models rather than frontier-scale workloads, and they’re joining established players, including the Utah-based Salad platform, which lists more than 60,000 daily active consumer GPUs on its network.

Far Labs’ proprietary scheduler splits a model into pieces spread across multiple machines, and an orchestrator and a load balancer then reassemble the partial outputs into a response. Evolving Edge distributes jobs with Ray, the open-source framework used inside conventional data centers.

Letting a stranger’s workload onto a personal machine obviously comes with some risks for hosts, such as malicious code ending up on the device or the person on the other end gaining access to local files. The two firms’ solution to this is isolation, with inference running as a sandboxed workload with encrypted communication and hard limits on GPU, CPU, memory, storage, and network access. Customers get no direct access to the host machine, and Evolving Edge has open-sourced its node software so hosts can audit what runs on their hardware.

Salad sells consumer-GPU compute to customers for prices starting at $0.02 per hour, and the card’s owner only sees a slice of that… pie after the platform takes its cut. We examined Salad in 2021, back when its network mined Ethereum, estimating that the company had generated roughly $3.6 million from users' PCs while distributing $500,000 in rewards, which works out to about 14 cents on the dollar for the people supplying the silicon.

Electricity costs then chew through whatever's left. An RTX 4090 draws 350W to 450W under sustained load, roughly $40 to $50 a month at $0.15 per kWh if the card runs around the clock, so a rig earning less than that is effectively paying for the privilege of having a job. However, *IEEE Spectrum's* report doesn't include payout rates for either new platform.

Both founders make the point that distributed networks ride out failures that otherwise cripple centralized clouds. John Federico, founder and CEO of Evolving Edge, cited the AWS outage last October that left Internet-connected smart beds stuck in their upright positions, and told *IEEE Spectrum* his network could lose 100 of 250,000 nodes “and it wouldn’t matter.”

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

All that aside, distributed AI compute has a credibility problem to overcome. A research preprint from June claimed that Pearl, a blockchain marketed as converting cryptocurrency mining into AI work, ran the equivalent of 320,000 RTX 3090-class GPUs on random matrix math while producing no useful AI computation. Far Labs and Evolving Edge route real customer inference jobs rather than token rewards, which puts them a step ahead of that model, but their cost and latency figures are unsubstantiated claims until, and if, the networks operate at scale.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Luke James](https://cdn.mos.cms.futurecdn.net/C4FAi2KzwaGLUrBqzX5aBM.png) 

Luke James is a freelance writer and journalist. Although his background is in legal, he has a personal interest in all things tech, especially hardware and microelectronics, and anything regulatory.

- 
How is it if it costs $40 to $50 per month in electricity and you are getting .02 per hour anywhere near minimum wage? Seems like they aren't getting any hosts if you would just be giving your machine up mostly at a loss of not only your resources but your time since you wouldn't even be able to use your machine for gaming if the only possible way to make a profit was to run 24hrs. NopeReply
- 
These startups must have hired the underpants gnomes as consultants.Reply
 
 Currently the big AI companies are having issues not being able to recover the electrical costs of the AI models they are selling. They are losing even more for costs related to building the data center and buying all the machines. There is no way these startups can think to cover the cost of the consumer electricity.
 
That might be the real scam though. They try to get stupid people who think their pc runs for free and pay them a couple pennies a hour. They take all the money they can get before people figure it out. There are massive numbers of stupid people. So many people think door dash is free extra money because they have no clue how to calculate the costs of using their car to do these deliveries.
