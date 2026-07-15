---
title: '''PCIe Gen7 development has already started,'' says Silicon Motion''s Alex
  Chou — Nvidia''s Storage Next initiative is becoming a focal point'
source_url: https://www.tomshardware.com/pc-components/ssds/pcie-gen7-development-has-already-started-says-silicon-motions-alex-chou-nvidias-storage-next-initiative-is-becoming-a-focal-point
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-15T17:34:42Z'
published: '2026-07-15T00:00:00Z'
description: SMI has big plans for data centers.
image: https://cdn.mos.cms.futurecdn.net/okYjABvduGkexdn6PMXnTE-1920-80.jpg
---

![Silicon Motion's Alex Chou](https://cdn.mos.cms.futurecdn.net/okYjABvduGkexdn6PMXnTE.jpg) 

Nowadays, storage devices for consumer and data center applications differ rather dramatically, as do approaches to product design as well as go-to-market strategies. Therefore, to get a more or less comprehensive overview of the storage market in general, you must observe both ends of the spectrum. To complement our interview with Nelson Duann at Computex, we also sat down with his colleague Alex Chou, who is in charge of Silicon Motion’s enterprise storage business.

Alex Chou is an interesting person to talk to. Before joining Silicon Motion, he spent some 18 years at Broadcom, where he led the wireless connectivity business, also initiating the Enterprise Switch, PoE, and 10-G Base-T PHY business with a product marketing focus. Before that, he worked at UMC Capital, ARK Logic, and Western Digital, where he developed graphics accelerators. He deeply understands the industry and uses his knowledge to expand SMI's business into the data center segment. As he is the first general manager of Silicon Motion's enterprise business unit, it is safe to say that all the success that the company has faced in the new segment so far can be attributed to Alex Chou.

**Anton Shilov:** Can you introduce yourself to our readers, please?

**Alex Chou:** My name is Alex Chou. As you know, Silicon Motion has two business units: the client business and the enterprise business. I am responsible for the enterprise business unit. My responsibilities include defining new products, leading development teams, bringing products to market, and working with OEMs, cloud service providers, and other customers to promote our technology and differentiation.

## Getting into enterprise SSD business

*Historically, Silicon Motion was focused on NAND controllers for client applications as well as embedded graphics processors and USB display controllers. Following the restructuring in the early 2020s, SMI formed a separate business unit to offer enterprise-grade SSD controllers, though it took the company some time to land its first tangible orders. By now, the company has yet to grab a 10% market share, yet it has clients among cloud service providers (CSPs), hyperscalers, and OEMs, significant achievements given Silicon Motion is a relatively new market entrant.*

**Anton Shilov:** It has been a challenging year for much of the industry, particularly for memory-related segments. Yet Silicon Motion reported first-quarter revenue of $342.1 million, up 23% sequentially and 105% year-over-year, while SSD controller sales increased by roughly 40% to 45%. Can you explain what drove those results, particularly on the enterprise side?

**Alex Chou:** It depends on how you define a difficult year. If you look at the results, I would argue that this has actually been one of the best years the storage industry has seen.

Silicon Motion is fundamentally a controller company. We build controllers that work with NAND from all major memory suppliers. On the enterprise side, we are still relatively new compared to some established competitors, but we have secured a number of new projects and have started delivering products to customers.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

We have invested heavily in PCIe Gen5, Gen6, and Gen7 enterprise SSD controllers. Today, our Gen5 products are beginning to ramp into volume production with multiple OEM customers. That ramp is contributing to our growth.

**Anton Shilov:** Do you have an estimate of your market share in the enterprise SSD controller market?

**Alex Chou:** That depends on how you define the market. Some people measure market share by unit shipments, while others look at exabytes shipped because SSD capacities continue to increase.

We have only recently begun shipping enterprise products in volume. If you listened to our CEO's comments during the earnings call, we expect enterprise shipments to increase significantly in the second half of the year. We are still in the early stages of our ramp, but we are making good progress with several key customers.

If you look beyond the initial ramp and think about the full-year run rate, I believe we can build from there and target a much stronger position next year. Longer term, our goal is to exceed 10% market share in the $4B enterprise SSD controller market, but this year is really about getting through qualification, customer testing, and the early production ramp in 2 half of this year.

Our goal is to continue expanding our share. We are only beginning the ramp [of our data center-grade SSD controllers] today, but we expect our share to increase meaningfully as deployments grow.

**Anton Shilov:** Who are your primary customers? SSD manufacturers, OEMs, or hyperscalers?

**Alex Chou:** We primarily work with OEMs. We sell controllers and firmware solutions to SSD manufacturers and OEMs. Some customers use our complete controller-and-firmware solution, while others develop their own firmware.

At the same time, we work directly with hyperscalers and cloud service providers to explain the advantages of our products and ensure they understand our technology roadmap.

Enterprise SSDs are used in several different segments. Traditional compute servers represent one market. High-density storage systems used for AI and large-scale data storage are another. We also see growing interest in storage systems located near GPUs, where latency becomes particularly important.

One area where we differentiate ourselves is quality of service. We have developed a patented traffic-shaping engine that helps maintain latency consistency under heavy workloads and multi-tenant environments. That capability is particularly attractive to hyperscalers and cloud service providers.

**Anton Shilov:** Do you see the enterprise SSD market splitting into different categories depending on workload?

**Alex Chou:** Yes. We see at least three major categories emerging.

The first is traditional compute-attached enterprise SSDs, which are used in conventional servers and storage systems. The second is very high-density storage for AI and hyperscale environments, where capacity, throughput, and cost efficiency are critical. The third is storage located closer to GPUs, where the requirements are very different because latency and quality of service become much more important.

That third category is particularly interesting. In AI systems, the storage subsystem is no longer just feeding CPUs. It increasingly has to support GPUs directly, especially for workloads involving very large datasets or KV-cache offload. In those environments, low latency and predictable performance matter much more than they did in traditional storage deployments.

## Storage Next, PCIe 6 and PCIe 7 SSD controllers

**Anton Shilov:** Is that where Nvidia's Storage Next vision comes in?

**Alex Chou:** Yes. Storage Next is one of the major industry developments we are watching very closely.

The idea is that storage will move closer to the GPU and become part of a much more tightly integrated data path. In some cases, the goal is not just to maximize bandwidth, but to ensure that latency remains low and deterministic enough for AI workloads that continuously move data between accelerators, system memory, and storage.

This is one of the reasons we have invested heavily in QoS and latency control. Through our traffic-shaping technology, we can manage access patterns and reduce latency spikes when multiple tenants or applications share the same SSD. In a cloud environment or an AI storage environment, that becomes very important.

 ![Silicon Motion](https://cdn.mos.cms.futurecdn.net/GD4vgi3dmmbtJnsoQjpktX.jpg) 


**Anton Shilov:** So, the challenge is no longer just raw throughput, but how predictably the SSD behaves under load?

**Alex Chou:** Exactly. Bandwidth still matters, but in many enterprise and AI environments, consistency matters just as much.

When multiple applications, multiple VMs, or multiple users share the same storage device, you need to control latency and quality of service carefully. If performance becomes unpredictable, it can affect the entire system.

That is why we have focused on a traffic-shaping mechanism that can prioritize and isolate workloads more effectively. We believe that kind of latency management will become a key differentiator for enterprise SSD controllers going forward.

**Anton Shilov:** How does that affect your roadmap for future controllers?

**Alex Chou:** It affects it quite a bit. Our upcoming controllers are not designed only for higher sequential bandwidth. They are also being designed for newer enterprise requirements such as OCP 2.7 compliance, stronger security, better QoS, and support for more advanced deployment models.

**Anton Shilov:** Are you already sampling your PCIe 6.x controllers?

**Alex Chou:** On the Gen6 side, our controller design is essentially complete; we have an FPGA [emulating algorithms], and we expect tape-out very soon. If everything goes according to plan, we expect first silicon back in the second half of 2026.

That controller not only supports a faster host interface, but also supports new features and requirements we see from AI infrastructure and hyperscale customers.

**Anton Shilov:** So, the PCIe Gen6 SSD platform is not just a speed upgrade for Silicon Motion?

**Alex Chou:** Correct. PCIe Gen6 obviously provides more bandwidth, but for us the more important part is that the surrounding system requirements are changing as well. Security, QoS, cloud deployment models, and AI storage architectures are all evolving at the same time, so the controller has to evolve with them.

**Anton Shilov:** Let us talk about the roadmap in more detail. You said the PCIe Gen6 enterprise controller is close to tape-out. What comes after that?

**Alex Chou:** PCIe Gen6 is the next major step for us, and the design is essentially complete. We expect to tape out very soon and, assuming [everything works correctly], receive first silicon in the second half of 2026.

But internally, we are already working beyond PCIe Gen6. PCIe Gen7 development has already started. In fact, the overall architecture for our Gen7 enterprise controller platform has already been defined. That means we are not just planning the interface speed increase; we are also defining the surrounding architecture, feature set, and deployment model that will be needed in the next generation of enterprise and AI systems.

**Anton Shilov:** So, SMI's PCIe Gen7 controller is no longer just a concept?

**Alex Chou:** Correct. PCIe Gen7 is already in active development. The current plan is to have internal samples in 2H, 2027 and to move toward production in that same general timeframe.

As controller development becomes more complex, you cannot wait until the market is ready before starting work. By the time a new interface reaches the market, the controller has to be nearly finished already. So, we are always working at least one generation ahead, and in practice often two.

**Anton Shilov:** As NAND becomes denser and more complex, error correction also becomes a bigger issue?

**Alex Chou:** That is a major part of controller development now. As NAND moves to higher layer counts and denser cell structures, the controller has to do more work to maintain reliability, endurance, and data integrity.

One of the areas we are working on is stronger LDPC. On the enterprise side, LDPC with a 16KB collaborative codeword is already used with SM8466, SMI’s first Enterprise PCIe Gen6 controller, and it is part of the roadmap because future NAND will require more robust error correction. That is one of the reasons enterprise controller architecture keeps becoming more complex generation after generation. You are no longer designing only for interface speed. You are also designing for signal integrity, power, security, QoS, error correction, and support for future NAND generations that may behave very differently from today's devices.

**Anton Shilov:** Will LDPC with 16KB collaborative codeword be enough for next generations of 3D NAND with hundreds of active layers?

**Alex Chou:** A 16KB LDPC engine already consumes a significant amount of silicon area and is quite sophisticated. For PCIe Gen7 controllers, our goal is to optimize and improve that engine from multiple angles rather than simply keep expanding it. We still need our architects to make the final call on exactly which improvements we will implement, but at this point we are more likely to refine and enhance the current design than to move beyond 16KB LDPC.

## SSD controller development strategy

**Anton Shilov:** Speaking more generally, SSD controllers are increasingly becoming full platforms rather than just controllers, because integration matters so much. Do you expect close collaboration between controller vendors, NAND makers, and SSD manufacturers to become even more important as the industry moves to next-generation storage devices?

**Alex Chou:** I may not fully understand your question, but let me explain how we approach it.

At Silicon Motion, we design the controller architecture and build the firmware stack with a rich feature set. For example, we have developed our own [PerformaShape] traffic-shaping engine to improve QoS. That is the foundation of the platform.

From there, we have to look at how NAND evolves from one generation to the next. As we move from PCIe Gen5 to Gen6 to Gen7, controller performance has to scale accordingly. If you want to saturate the PCIe interface and deliver, say, 7 million IOPS today and much higher performance in future generations, you have to understand exactly where NAND is going.

That is why my team meets regularly with Samsung, SK hynix, SanDisk, Kioxia, and all other NAND vendors to review their roadmaps. Silicon Motion is part of that ecosystem, and because of those relationships, we usually get early visibility into future NAND generations and often receive early samples so we can bring up our controllers and make sure they take advantage of new NAND as quickly as possible.

That matters even more in the current supply environment. Because we work with all NAND suppliers, hyperscalers and cloud service providers can come to us and ask for a solution that is not tied to a single memory vendor. A company like Samsung naturally builds around its own NAND, but we have the advantage of being able to support multiple suppliers. That gives customers much more flexibility when supply is tight.

So yes, we have a core controller architecture and a common firmware base, but one of our strengths is that we work very closely with NAND vendors on future generations and make sure our platform can take advantage of faster interfaces, higher die counts, and new NAND capabilities as they arrive.

## XL-Flash and storage-class memory

**Anton Shilov:** What about storage-class memory? Are there any developments there? As far as I can tell, adoption of Kioxia’s XL-Flash has been limited.

**Alex Chou:** That’s a very good question. I am actually going to visit Kioxia, so I should have a better sense of their plans after that. At the moment, Kioxia is essentially the only company still pushing XL-Flash, so they are trying to build something around it.

The challenge is that it is not just about the technology itself. You need a broader ecosystem to support it, and that is what makes the situation more complicated. We are watching it closely and trying to understand whether it is something we really need to support, but at this point I do not have a definitive answer. We are still evaluating it.

**Anton Shilov:** Have you heard anything similar from other suppliers? Quite a few memory makers used to talk about storage-class memory or similar technologies in their roadmaps.

**Alex Chou:** Based on what we know, not really. If you look back at last year’s Flash Memory Summit, several NAND makers were talking about higher-performance flash and storage-class-memory-like concepts. That created a lot of buzz at the time, and we looked into it, just as we have looked into XL-Flash, to understand whether there was a real ecosystem forming around it.

But there is much less discussion around those ideas now. One reason is simple: memory vendors do not really need those products at the moment because they can sell conventional NAND at very high prices and still generate strong returns.

**Anton Shilov:** In other words, they can just sell QLC 3D NAND and be perfectly happy.

**Alex Chou:** Exactly.

**Anton Shilov:** On the other hand, Nvidia wants storage devices capable of 100 million IOPS.

**Alex Chou:** Yes, that is where Storage Next comes in.

**Anton Shilov:** Has anyone actually come close to 100 million IOPS yet?

**Alex Chou:** I would say Storage Next gains many attentions. XL-Flash could be one possible approach to address that kind of requirement. But these are other options aiming to address high-performance and low latency needs.

What matters more is that Storage Next has a much stronger ecosystem behind it because Nvidia is actively driving it. There are regular meetings around it, and our architect has been involved from the very beginning. We have been tracking it closely and trying to make sure our future controller architecture can support it if and when the market materializes.

At the same time, Nvidia itself appears to recognize that 100 million or 200 million IOPS may not be realistic in the near term. The target seems to be moving closer to something like 50 million IOPS, which is more achievable. So yes, we are watching it very closely, and we are building in the flexibility to support it if needed.

In storage, having a technically interesting idea is not enough. The industry has to agree on how to use it, how to deploy it, and how to integrate it into systems. Storage Next currently has more momentum because the ecosystem behind it is much stronger.

**Anton Shilov:** So, you see Storage Next as more commercially relevant than storage-class memory, at least for now?

**Alex Chou:** Yes. At least today, Storage Next looks more immediate and more actionable.

We are already participating in those discussions and thinking about what future controller requirements will look like in that environment. That includes not only bandwidth, but also latency behavior, QoS, and the role storage plays in systems where GPUs are increasingly central to the data path.

That does not mean other technologies disappear. It just means that if you ask where the market is actively moving right now, the answer is much more on the Storage Next side than on the storage-class-memory side.

**Anton Shilov:** So, in practice, you make sure your controller works with all relevant NAND types, while the memory vendor mainly has to make sure the media itself complies with the interface requirements?

**Alex Chou:** When we design a controller, we already cooperate closely with NAND suppliers. Our architects look at all of the major vendors to understand whether there are any special requirements we need to account for. Then we handle another layer of optimization in firmware to make sure we can support all of those devices properly.

If you look deeper into enterprise NAND, most products also use interface chips internally to connect large numbers of dies. Those interface chips can differ from vendor to vendor, so we need to understand their configurations as well, including die counts, planes, and other architectural details. The goal is to make sure the controller and firmware together can support all of those different combinations.

So far, our architecture has been able to support NAND from SanDisk, Kioxia, SK hynix, and the other major vendors. Even if the interface chips differ, we try to keep the overall hardware design as flexible as possible.

There are really three elements involved: the controller itself, the hardware board, and the firmware. Ideally, you do not want a completely different board design for every NAND supplier. Fortunately, the industry has standardized a lot of the pinouts and module interfaces, which makes it possible to use a common hardware design and swap in NAND from different suppliers with the right firmware support.

We spend a lot of time making sure we can support all of those different combinations.

**Anton Shilov:** So you are effectively building controllers with a fairly clear view of what future NAND generations will look like.

**Alex Chou:** Exactly. We want to make sure that when the next generation of NAND arrives, we are ready to support it as broadly as possible.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Anton Shilov](https://cdn.mos.cms.futurecdn.net/uMZ5kNphxA2Ut6whdLaSQV.png)

Anton Shilov is a contributing writer at Tom’s Hardware. Over the past couple of decades, he has covered everything from CPUs and GPUs to supercomputers and from modern process technologies and latest fab tools to high-tech industry trends.
