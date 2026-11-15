---
title: Google turned to AMD Epyc, not its own Axion chips, to secure its first confidential
  TPU
source_url: https://www.techradar.com/pro/google-turned-to-amd-epyc-not-its-own-axion-chips-to-secure-its-first-confidential-tpu
source_site: TechRadar UK
source_slug: techradar-uk
description: The reason says a lot about where trust in AI hardware really lives
image: https://cdn.mos.cms.futurecdn.net/MVfiXV7sRq7dWyFz2yiRHM-1600-80.jpg
published: '2026-11-15T00:00:00Z'
scraped_at: '2026-11-15T01:11:55Z'
categories:
- Technology & Software
people:
- Mark Lohmeyer
- Rick Schafer
locations:
- Venice
organisations:
- 8tx
- AI
- AMD
- Axion
- CPU
- Confidential GKE
- Confidential Space
- Confidential VMs
- Data Center Knowledge
- Epyc
- Google Cloud
- Nvidia
- Oppenheimer
- Oracle
- Outperform
- PC
- SEV
- Secure Encrypted Virtualization
- SemiAnalysis
- ServeTheHome
- TPU 8i Max
- TPUs
- TechRadar Pro
- Tom's Hardware
- Turin
---

![A Promotional Rendering Of An AMD Epyc Processor](https://cdn.mos.cms.futurecdn.net/MVfiXV7sRq7dWyFz2yiRHM-1600-80.jpg)

* **Google's new TPU 8tx pairs TPU 8t silicon with 5th Gen AMD Epyc "Turin" hosts to deliver confidential AI inference**
* **The AI juggernaut passed over its own Axion CPU, which hosts the 8t and 8i, likely because its audited confidential stack is x86-only for now**
* **The confidential TPU joins a growing number of chips even as key security details remain unpublished, even as Google and Nvidia already offer confidential GPUs to cloud customers**

Google has added two more systems to its eighth-generation TPU family, and the one built for confidential AI leverages a host processor Google didn't design.

The TPU 8tx, detailed alongside the dual-chip TPU 8i Max in a Google Cloud blog post, pairs Google's accelerator silicon with 5th Gen AMD Epyc CPUs.

AMD also announced that Epyc forms the host foundation for what both companies call the first cloud TPU system with hardware-enforced confidential computing.

## The same chip with a new trust boundary in tow?

Google's April 2026 launch split its eighth generation hardware into the TPU 8t for training and the TPU 8i for inference. Google bills this as the first time it has introduced four TPU systems in one year, but as ServeTheHome points out, the two newcomers are system configurations built on existing chips rather than new designs.

As per Taiwanese outlet INSIDE, the 8tx inherits the 8t's 12.6 petaflops of FP4 compute and 216GB of HBM, but swaps in the lower-latency Boardfly network used by the 8i. Google claims up to 2x lower latency than TPU 8t with a near-zero performance penalty, and pitches the system at regulated enterprises and governments that want to fine-tune, distill, and train agents on private data without moving it between clusters.

AMD says Epyc handles orchestration, data preparation, and the high-throughput link to the accelerators. Its Secure Encrypted Virtualization (SEV) works with the TPU to extend the protected environment out to the accelerators, checking each one's identity and security configuration before granting direct access to protected memory

Prompts, model weights, and intermediate data stay encrypted in host memory and in transit, according to AMD, with hardware isolation while the TPU runs. Google, for its part, described the result as "keeping sensitive data and model weights protected and isolated even while in active use."

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## Skipping the homegrown solution?

Google hasn't directly said why it passed over Axion, the Neoverse V2-based chip it unveiled in 2024 as its first data center processor. Its own documentation offers a strong hint, however: Google's list of supported Confidential VM configurations runs entirely on AMD SEV and Intel TDX machines, with no Axion-based C4A or N4A instances, and states that TPUs can't currently be attached to Confidential VMs at all.

AMD's release adds that Google security experts have performed deep reviews of AMD's security processor firmware, and that SEV already underpins Google's Confidential VMs, Confidential GKE, Confidential Space, and confidential Spark and Dataflow services.

It could be argued here that confidential computing is only as credible as the years spent attacking it, and Google's audited chain of trust runs through x86. Building an equivalent on Axion would mean qualifying new hardware before shipping a product whose entire selling point is the "trust" it comes with, making it a moot point.

The move however is not a win for AMD's latest silicon; ServeTheHome reported that Google chose Turin to match the TPU 8t's PCIe Gen5 x16 interface, noting that a Gen6 host such as Venice would add no accelerator bandwidth, and tying the decision to Google's 2027 qualification schedule. Venice is AMD's 2nm flagship; the 8tx runs on a chip based on a family of CPUs that launched in October 2024.

Mark Lohmeyer, who runs AI and computing infrastructure at Google Cloud, told reporters that select customers will be able to deploy the 8tx in their own data centers, Data Center Knowledge reported, noting that Oracle recently said it will offer TPUs on its cloud. INSIDE quoted Lohmeyer arguing that the technology lowers the risk of physical operators reaching sensitive data, even in third-party facilities.

As TPUs spread beyond Google's own campuses, hardware attestation becomes the mechanism that lets a model owner place weights on hardware someone else runs. That interestingly puts AMD as a crucial part at the root of Google's off-campus trust offerings, a bigger role than the 8tx's niche positioning would initially suggest.

It also revives August's rumor: A SemiAnalysis client note reported by Tom's Hardware, said "Market chatter suggests [Google] is working with AMD on a TPU project in the v10 generation," possibly with CPU cores on the same package. The 8tx confirms neither claim as its Epyc chips sit in separate sockets, and nothing announced on November 9 involves AMD in accelerator design, but it does lend credence to potential future collaborations between the chip designer and the AI juggernaut.

The news saw AMD closing at $508.58 on November 9, up 13.26%, after trading as high as $515.18 on more than twice its recent average volume and while not all of it can be attributed to this particular development even as Oppenheimer's Rick Schafer upgraded AMD to Outperform with a $600 target, calling its server and data center success "undeniable", one could argue that it was a sizeable, if not the overwhelming catalyst in play that day.

The TPU 8tx arguably won't turn AMD's Epyc into a formidable TPU business overnight, and Google has left enough unpublished that its confidential computing claims deserve scrutiny once customers can test them.

However, one does need to account for the fact that when Google needed a host CPU to stake its first confidential TPU on, it picked AMD over its own chip, and that endorsement will outlast one day's share price increase as the latter aims to broaden its AI business even as its CEO recently branded the company as "Data center-first" entity even as PC sales continue to plummet.
