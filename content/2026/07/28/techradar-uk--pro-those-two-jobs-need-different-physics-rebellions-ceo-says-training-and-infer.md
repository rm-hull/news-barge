---
title: '‘Those two jobs need different physics’: Rebellions CEO says training and
  inference need different chips'
source_url: https://www.techradar.com/pro/those-two-jobs-need-different-physics-rebellions-ceo-says-training-and-inference-need-different-chips
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-28T17:44:18Z'
published: '2026-07-28T00:00:00Z'
description: Model training still needs flagship chips, but could inference get away
  with lighter chips?
image: https://cdn.mos.cms.futurecdn.net/8LbKACFfyPRXXFvbvwwEhP-1920-80.jpg
---

![Apple AI servers](https://cdn.mos.cms.futurecdn.net/8LbKACFfyPRXXFvbvwwEhP.jpg) 

The AI race started off with a pretty clear direction – bigger and better. The first waves were characterized by building bigger models, but it’s all change in the world of artificial intelligence and with enterprises, SMBs and consumers all finding use cases for the technology, the focus has shifted.

Now, AI firms and model developers are looking to realize a much tougher goal. Efficiency. Cost per token, performance per watt, output per input, it’s all about driving maximum efficiency.

One clear divide is between training and inference. While training models still requires huge amounts of resources, inference efficiency is starting to improve, and one company (Rebellions) now believes an opening for inference-first hardware could create a new market.

The company’s racks are said to consume around 16-20kW, compared with around 120kW for leading GPU-based inference systems that, for many use cases, are sheer overkill.

Rebellions’ rack costs are also said to be around one-third of the price, making AI inference more accessible and helping enterprises to deploy AI more widely.

## This hardware shift could be the start of truly efficient AI

Memory is also another battleground, whereby huge trillion-parameter models are testing the limits of today’s hardware and the intertwined reliance on memory and compute. Something Rebellions says it’s looking to fix by working with the likes of SK Hynix and Samsung to align multiple roadmaps, instead of having to respond to shifts in architecture.

Ultimately, today’s black-and-white chip manufacturing landscape is now evolving, and Rebellions sees two key changes happening simultaneously. Firstly, training and inference hardware is starting to differ more drastically. Secondly, aligning multiple hardware roadmaps across memory, compute and more will drive more efficiency not just across deployments, but in terms of bringing new products to market.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

I spoke to Rebellions CEO Sunghyun Park allows me to understand how and why inference and training hardware are starting to separate, as well as the importance of open standards and collaboration in the drive for all-round efficiency.

- **The AI chip market seems to be splitting between training-first and inference-first architectures. Why is that happening, and why now?**

This split exists because training and inference are fundamentally different problems.

Training is how you build a model. It happens once, involves a small number of organizations, and rewards raw computational flexibility because the workload keeps shifting as research moves forward.

Inference is how you actually use a model: every query answered, every transaction processed, every decision an AI system makes in production. That happens billions of times a day across nearly every industry, and it’s where AI moves from R&D into revenue.

Those two jobs need different physics. Training requires maximum FLOPS. Inference requires efficiency, reliability, and economics that hold up when you’re serving users at scale.

The industry forced a training chip into that second job because that’s what existed. Now that inference has become the larger, more urgent market, that compromise no longer holds. Enterprises and governments are asking how fast they can deploy. That’s why the conversation is splitting now.

- **Where does Rebellions fit in that split, and what makes your approach to AI inference fundamentally different from your competitors?**

We built for inference, from day one. Most first-generation AI chip companies emerged from the 2016-2017 training boom and adapted their architectures for inference afterward.

We started in 2020 – after that wave – with inference as the only target, which meant designing around what production AI actually needs instead of retrofitting a training chip.

The numbers reflect that choice. Our racks draw 16-20kW versus roughly 120kW for leading GPU-based inference systems, about a sixth of the power, in a market where power is the binding constraint for most operators.

Acquisition cost runs around $10 million per rack versus roughly $30 million, about a third of the cost. Our chiplet-based architecture also scales out rather than betting that a single device can handle a model’s full size, which matters now that production workloads are trillion-parameter mixture-of-experts models instead of the few-hundred-million-parameter models the first generation was built around.

It’s also why our architecture is memory-centric rather than compute-centric. The chiplet approach exists to keep memory close to logic as models scale, not just to add cores.

And we have three years of production deployments behind that architecture, not pilots. That’s the hardest part to replicate: real workloads, running at scale, today.

- **A year ago, everyone in AI was talking about chiplets. Now the conversation has shifted to memory. What changed?**

The chiplet conversation was about architecture: breaking a chip into modular pieces that scale independently, rather than betting everything on a single monolithic die.

That mattered because it let the industry move past an assumption the first generation of accelerators made in 2016 and 2017, that a single device would always be big enough to run any model.

That assumption broke once mixture-of-experts and trillion-parameter models arrived.

The memory conversation is the layer underneath that. Once the architecture problem is solved, the constraint becomes physical: can you actually get enough high-bandwidth memory (HBM) to build what you’ve designed?

HBM is 3D-stacked memory, and how closely you can physically stack it to compute is as much of a bottleneck as raw supply.

Every AI accelerator company is competing for the same limited supply right now, and demand has outpaced what memory makers can produce. That’s the memory-logic co-design problem: architecture and memory supply are no longer separable decisions.

We’re in a different position because our investor relationships were built around supply, not just capital. Our memory partners are also investors, and we co-design our memory architecture directly against their roadmaps rather than simply purchasing off them.

Our chiplet architecture also develops against our foundry partner’s process roadmap. When the rest of the industry was fighting for allocation, we already had a seat at the design table through those relationships.

That’s memory-logic co-design, not just secured supply. The shift from chiplets to memory tracks has moved the real constraint: from architecture to physical supply.

- **Your stack runs on open-source frameworks like vLLM, PyTorch, Kubernetes, and OpenShift, tools many enterprises already use. Does that make adoption relatively plug-and-play, or is that an oversimplification?**

It’s mostly true, but ‘plug-and-play’ undersells how deliberate that was, and oversimplifies in one specific way.

We built entirely on open standards: vLLM, PyTorch, Kubernetes, and Red Hat OpenShift. We’re one of only two chip companies in the PyTorch Foundation, and the only AI accelerator company fully integrated with OpenShift.

A developer who already knows how to run inference on existing infrastructure already knows how to run it on ours. There’s no proprietary runtime to learn and no migration project. That part really is close to plug-and-play.

The first generation of AI chip companies each built proprietary software stacks, and hundreds of millions of dollars went into software that didn’t survive. We came to market once the open source ecosystem had matured and chose to build on it instead of forking it.

Where it oversimplifies is assuming that means zero integration work. Production deployments still require validating performance at your specific workload and scale, and that takes real engineering time, no matter how compatible the stack is.

What open standards remove is lock-in risk and retraining cost, not the deployment work itself.

- **What are the biggest challenges organizations face when trying to run AI inference outside of hyperscaler platforms?**

Most organizations aren’t built like hyperscalers, and much of the available inference infrastructure assumes they are.

The first challenge is physical. Most enterprises, telcos, and governments already have data centers. They can’t wait two to three years or spend $600 million-plus on new ones, and they can’t retrofit for liquid cooling without major cost and disruption.

So the practical question is whether inference hardware runs on what they already have: standard racks, air cooling, and existing power budgets.

The second is sovereignty. Organizations increasingly want to bring compute to where their data already lives, rather than move sensitive data to wherever compute is hosted.

That’s partly regulatory, partly operational, but either way, cloud-only inference creates a dependency a lot of operators are no longer comfortable with.

We built specifically for that gap. Our systems run at 4-5kW per server on standard air-cooled infrastructure, no facility redesign required.

SK Telecom has run on our hardware for nearly three years, scaling from a small cluster to close to 100 racks and now processing 50 million API transactions a day, entirely inside their existing network.

KT Cloud runs real-time inference on highway CCTV systems nationally. Both show you don’t need hyperscaler-scale infrastructure to run AI at hyperscaler-relevant volume.

- **Cerebras' IPO, and potential listings from others in the space, have put AI infrastructure in the spotlight. What do these IPOs signal about the market, and where might the hype be outpacing deployment reality?**

It tells the public markets that AI infrastructure is a durable, investable asset class, not just a venture-backed bet. That validation benefits the whole sector, including us: it says purpose-built AI silicon is real, differentiated from general-purpose GPUs, and worth independent capital.

Capital flowing into the sector is necessary, but it doesn’t by itself determine who wins. The companies that define the next decade of this market won’t necessarily be the most-funded ones.

They’ll be the ones with real fundamentals: production customers, deployment scale, proven economics, durable supply chain relationships. That’s a different filter than fundraising size, and it’s the one that matters once public market scrutiny starts.

We’ve been building toward that filter since 2020, with production deployments and supply relationships with our foundry and memory partners that we secured before the rest of the industry was fighting over the same allocation. The capital is a tailwind for everyone serious about inference.

Whether it gets deployed well is a separate question, and one the market will answer over the next few years.

- **Looking ahead, what trends are you watching most closely across AI infrastructure and inference over the next 12–24 months?**

The buildout happening inside existing infrastructure keeps accelerating. Most enterprises, telcos, and governments aren’t waiting for new data centers.

They’re deploying inference into facilities they already have, and I expect that to become the bigger story even though it gets less attention than hyperscaler headlines.

Additionally, memory remains the physical constraint. HBM supply hasn’t caught up with demand, and as models keep moving toward trillion-parameter mixture-of-experts architectures, that pressure increases rather than eases.

Companies with secured, strategic supply relationships will have a real advantage over the next two years, not just a cost one.

Chiplets are how we get there. We’ve already mass-produced a highly advanced 4-chiplet package – a level of integration Nvidia has struggled to reach.

Reporting this year indicated Nvidia had built and demonstrated a four-chiplet Rubin Ultra design, then canceled it in favor of a dual-die architecture over manufacturability concerns: a four-die single package pushes roughly 7.5-8x past reticle limits on yield and cost. That’s the foundation.

The next layer we’re building on is performance optimization of HMB3E (3D-stacked memory) in close collaboration with memory and compute co-designed together from the start, not bolted on after the fact.

Also on my radar is the fact that as more companies in this space go public, capital will get valued against production fundamentals rather than funding rounds.

And the efficiency point matters: as inference gets cheaper per token, demand doesn’t shrink, it expands, because new use cases become viable at lower cost. That’s been true of every computing platform in history, and I don’t expect AI inference to be the exception.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Desire Athow](https://cdn.mos.cms.futurecdn.net/oEw3XiohQwun9z7gMxKzkB.jpg)

Désiré has been musing and writing about technology during a career spanning four decades. He dabbled in website builders and web hosting when DHTML and frames were in vogue and started narrating about the impact of technology on society just before the start of the Y2K hysteria at the turn of the last millennium.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
