---
title: Colibrì proof-of-concept gains frontier-level 1.5-TB AI model — novel approach
  runs on only 25GB of RAM and shows promise for local AI setups
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/colibri-proof-of-concept-gains-frontier-level-1-5-tb-ai-model-novel-approach-runs-on-only-25gb-of-ram-and-shows-promise-for-local-ai-setups
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-11T13:48:42Z'
published: '2026-07-11T00:00:00Z'
description: It's slow, yes, but it's a start.
image: https://cdn.mos.cms.futurecdn.net/D2ddTrisPHZsxxEUuFfLgM-2121-80.jpg
---

![AI Chatbot](https://cdn.mos.cms.futurecdn.net/D2ddTrisPHZsxxEUuFfLgM.jpg) 

Running LLMs and agents in home lab setups is steadily gaining popularity due to the rising cost of AI bot subscriptions and concerns about data privacy. Unfortunately, an Nvidia NVL72 rack is ever so slightly out of the financial reach of most people, so enthusiasts have to make do with models that can run in limited amounts of memory. Italian engineer Vincenzo (aka JustVugg) seemingly wanted to have his cake and eat it, __so he created ColibrÌ__ to run the 744-billion-parameter 1.5-TB GLM-5.2 model on a modest CPU, a mere 25 GB of RAM, and a 1 GB/s virtual NVMe drive.

 ![Nvidia](https://cdn.mos.cms.futurecdn.net/z53fPgXjpKHTpeGv3RHpqj.png) 


Let's get the elephant out of the way: Colibrì's speed on Vincenzo's setup is only about 0.05 to 0.1 tokens per second on average, a measure that's unusable for practical conversation — imagine just one question taking hours to answer. Higher-end setups provide far better figures, but for now, they still don't meet the 20-30 tokens per second required for real-time use.

Having said that, GLM-5.2 is a Mixture-of-Experts (MoE) model with frontier-level capability, at least somewhere in viewing distance of the finest offerings from Anthropic, OpenAI, *et al*. This means that the quality of the answers ought to be excellent, and Vincenzo himself says his limited testing produced some impressive results. The way Colibrì works is simple enough to describe, and yet hard to do right: loading the model in slices to RAM. We're going to oversimplify for clarity's sake.

An MoE model like GLM-5.2 includes hundreds of expert sub-models to answer different topics, and these are chosen *per token*, not per query — meaning that when you ask a question, your words get split into tokens (chunks). For each token, the bot activates the best experts for it. The experts might always be the same for the entire question, but more often than not, a query might reel in tens of experts, possibly going into triple digits.

Whereas normally large chunks of the model, or the entire model, are loaded onto interconnected datacenter GPUs, Colibrì takes advantage of the MOE architecture and repeatedly loads/unloads the experts required per token, allowing even a cheap machine to use a large model at a steep performance penalty. For speed and simplicity's sake, Colibrì's expert-selection code is a single C file with very few dependencies. Additionally, the GLM-5.2 model is quantized down (simplified with lossy encoding) to take up less space to begin with.

If you're thinking that loading and unloading data for every piece of a question's words is going to be a hard hit on storage I/O and memory bandwidth, you're exactly on the right track. In this type of setup, NVMe storage speed is the first major bottleneck, but the proverbial funnel varies across configurations. Give it enough storage bandwidth, then you're up against RAM limitations. Fix that, then you need more CPU cores, and so on.

Colibrì is currently a proof-of-concept and doesn't yet run on GPUs, though it's worth noting that even then, shuffling data to/from the card will almost certainly be the biggest constraint. Even still, the project has barely been released, and it's already proving quite popular. Vincenzo is collecting benchmark data and running fixes as we speak, so be sure to__ visit the repository__ to contribute if you can. Maybe at some point it'll be feasible to run a really clever model on high-end consumer hardware at a decent enough clip.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.

- 
It appears to be taking the benefits of a mixture of experts model to an illogical extreme, although maybe it can be made useful with more optimizations.Reply
 
 Normally I would just say save up your pennies for Strix/Gorgon/Medusa Halo or DGX Spark, which seem to be good at running big MOE models.
 
 But now I'm wondering if Intel has something worthwhile. Specifically a socketed Nova Lake-S desktop APU with 12 Xe3P cores. Even if it's limited to 128-bit memory, maybe you can min/max it to have better price/performance than Halo boxes. You could even use something like this Colibri project.
 
 And then there's Nova Lake-AX.
