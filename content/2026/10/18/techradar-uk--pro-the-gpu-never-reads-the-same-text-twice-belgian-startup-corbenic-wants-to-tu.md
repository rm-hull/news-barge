---
title: '''The GPU never reads the same text twice'': Belgian startup Corbenic wants
  to turn your server''s SSD into AI memory, but its 14x speedup owes more to reading
  less'
source_url: https://www.techradar.com/pro/the-gpu-never-reads-the-same-text-twice-belgian-startup-corbenic-wants-to-turn-your-servers-ssd-into-ai-memory-but-its-14x-speedup-owes-more-to-reading-less
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-18T21:34:47Z'
published: '2026-10-18T00:00:00Z'
description: Galahad promises exact, encrypted KV cache reuse for vLLM, SGLang, and
  Llama.cpp
image: https://cdn.mos.cms.futurecdn.net/JdkWFNHpKBbyUcYStcmsn-1920-80.jpg
categories:
- Technology & Software
people:
- AI
- Blaise
- Galahad
- Gemma
- Phison
- SGLang
- Sietse Schelpe
- Taliesin
locations:
- AI
- Blaise
- Delaware
organisations:
- AMD Ventures
- CMX
- CXL
- Corbenic AI
- CoreWeave
- GPU
- Galahad
- GitHub
- Huawei
- LMCache
- NVMe
- NVentures
- Nvidia Dynamo
- Pascari
- Phison
- RAG
- SGLang
- SSD
- Samsung
- Schelpe
- Taliesin
- TechRadar Pro
- Tensormesh
- Thunderobot
- WEKA
- vLLM
---

![Corbenic.Ai&#039;s logo](https://cdn.mos.cms.futurecdn.net/JdkWFNHpKBbyUcYStcmsn-1920-80.jpg)

* **Corbenic AI's Galahad beta saves a model's KV cache to encrypted local NVMe so servers can skip rereading text after GPU memory is cleared or after a restart**
* **Founder Sietse Schelpe tells TechRadar Pro no special hardware is needed, but the paper credits most of the 14x speedup to Blaise, a retrieval component, not SSD loading**
* **LMCache, Nvidia Dynamo and CMX, WEKA and Phison already persist KV cache to storage; Galahad's edge is exact, fail-closed reuse in one small library**

Belgian startup Corbenic AI says it can stop GPUs from rereading documents they have already processed, and its founder told TechRadar Pro the trick needs nothing more exotic than the NVMe drive already sitting in the server.

Galahad, which entered beta on October 1 2026, saves a model's key-value (KV) cache, the attention state built while a model reads a prompt, to encrypted local storage and reloads it the next time the same text appears.

In an email to *TechRadar Pro*, Corbenic introduced Galahad with the line "the GPU never reads the same text twice," and founder and CEO Sietse Schelpe summed it up as "the SSD a server already has becomes part of the AI's working memory."

## Catering to a market with plenty of alternatives in tow

The timing of Corbenic's announcement is impeccable; with data centers on course to absorb more than 70% of high-end memory chips in 2026, getting more work out of existing hardware is an easy sell. But Corbenic's own paper shows its headline 14x speedup owes more to reading less text than to loading saved work, and the company is walking into a field where Nvidia, Phison, and a well-funded open source project already offer something similar.

Galahad's approach is slightly different: In standard serving, a model answering a second question about a document recomputes that document's attention state from the first token, a step called prefill. Engines such as vLLM and SGLang already reuse that state while it sits in GPU memory, but Corbenic's paper notes it is evicted under memory pressure and lost whenever the process restarts.

Galahad's KV component, Taliesin, writes each block of text's state to disk under a fingerprint of the exact input bytes, the model, and the tenant, then loads it when those bytes reappear.

Schelpe stressed that the stored copy only comes into play once GPU memory has been cleared or the server has restarted. "So the choice is not SSD or RAM. It is SSD or computing it all again on the GPU," he told TechRadar Pro, adding that the load "happens once, before the first word of the answer."

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

He volunteered two limits: short texts are not stored because recomputing them is already fast, and network storage is much slower than a local NVMe drive. The paper sets a fail-closed rule on top: "serve without memory, never with wrong memory," so any record that fails a check is simply recomputed.

No special hardware is required, according to Schelpe, just Linux, an Nvidia GPU and a standard NVMe SSD. Asked about CXL, he said, "we tried faster storage, and it didn't make Galahad faster," which matches the paper's H100 test, where a RAM disk and a local disk delivered near-identical throughput.

On enterprise drives such as Phison's Pascari line, whose maker has been pitching flash as the answer to AI's memory bottleneck, he was refreshingly careful: "we haven't measured them, so I won't quote numbers."

Schelpe told TechRadar Pro that loading stored state from a fast SSD "is much quicker" than rereading, and that "is where our 14× comes from: 0.59 seconds per question on vLLM." The paper's own tables tell a more complicated story.

The 0.59-second result comes from a recall test with 100 facts hidden in a 96,726-token list, run on Gemma 4 31B, and it used Taliesin plus Blaise. Blaise is a second component that keeps the documents as text and hands the model only the section a question needs, about 668 tokens instead of the whole corpus. The paper itself credits Blaise with lifting the gain on llama.cpp from 3.1x to 14.5x.

With Taliesin alone, vLLM took 15.56 seconds per question, slower than its 8.11-second baseline, and SGLang took 22.02 seconds against 10.29. Only llama.cpp got faster on KV reuse alone, at 3.01 seconds against 9.25. Those comparisons are lopsided in both directions: the baseline used a 12,000-token window that saw only the last 12% of the corpus and answered 10 of 100 questions, while Taliesin let the model attend to everything and answered 98 of 100.

Schelpe positions Galahad against retrieval-augmented generation (RAG) pipelines such as RAGFlow, which split documents into chunks and pass the model whichever pieces a search ranks highest. "When the search misses, the model never sees the answer," he said, citing a benchmark in which Galahad answered 100 of 100 questions and RAGFlow 77.

Asked by TechRadar Pro why nobody else had come up with the strategy, Schelpe said rivals had chased "bigger is better" and that "there is no real glory" in building something like this, adding that he was lucky not to carry the same mental baggage. Corbenic's homepage makes the same point with the slogan "Stop building bigger models. Build the layer below."

The premise does not hold up well. LMCache, an Apache 2.0 project with around 10,900 GitHub stars, already moves KV cache into CPU memory, local SSDs and remote storage, and a 2024 post on its blog pitched it as "letting LLMs read each text only once." Nine days before Galahad launched, Samsung engineers detailed a restart-recoverable NVMe tier for the project, and its commercial backer, Tensormesh, raised $20 million in May from investors including AMD Ventures, CoreWeave, and Nvidia's NVentures.

Nvidia's Dynamo framework tiers KV cache from GPU memory through host DRAM to local NVMe and networked storage, and at CES 2026 the company unveiled a BlueField-4 context memory platform, now called CMX, built to push KV cache onto NVMe SSDs. Nvidia has even argued that storage is the next frontier of AI. WEKA sells its Augmented Memory Grid for the same job, Huawei pitches a Unified Cache Manager to avoid repeat calculations, and Phison's aiDAPTIV+ already parks KV cache on flash in consumer laptops such as Thunderobot's AI Master M7000.

## A security-centric play that still needs independent testing

Galahad's real distinction from most of its prolificly backed competition is narrower. Its paper cites LMCache and Mooncake directly and sets itself apart on exactness, with bit-identical logits as the acceptance test and any mismatch treated as a miss. "Exact, not approximate," Schelpe said, though that contrast lands hardest on techniques such as CacheBlend, which LMCache uses to reuse non-prefix chunks with selective recomputation, rather than on plain offloading.

Corbenic's launch release actually leads with security rather than speed, calling Galahad "a secure vault for working memory" that encrypts stored state, keeps each customer's data separate, and can record activity so developers can roll a server's saved memory back to an earlier point.

The concern behind the pitch is real; researchers showed at NDSS 2025 that KV cache sharing in vLLM and SGLang could let one user reconstruct another's prompts through a timing side channel, and Galahad's library counters that by refusing to start without a tenant identity and model fingerprint. Schelpe also stressed that data stays put: "There's no shared cache network, and nothing is sent to us."

On the flip side, Corbenic is a small Belgium-based team registered as a Delaware corporation, and every number in its main Galahad paper comes from experiments the founder ran himself on rented cloud GPUs, as the paper discloses. Raw logs are promised but not yet published, Blaise's selection method is withheld pending patents, and the papers are self-published arXiv preprints rather than peer-reviewed work.

Its competition includes both proprietary and open-source solutions, most of which have undergone far more testing and will likely see much broader adoption unless Galahad finds industry partners willing to integrate it.

None of that makes the idea wrong. Paying a GPU to reread the same contracts, manuals, and code on every request is a genuine waste, and Schelpe frames the contest sensibly when he calls "the real competitor: buying more GPUs." With memory and storage prices where they are, software that makes existing servers do more will find buyers, and he said early reactions have been positive, with "some nice requests and some learnings already."

What Galahad needs now is someone else's benchmark: a head-to-head with LMCache on the same Nvidia hardware, with each runtime's own prefix cache switched on, and Blaise's retrieval tested on documents it was not built around. Until then, the safest reading is that Galahad is a careful, exact take on KV persistence, and that its most eye-catching numbers come from reading less rather than remembering more.
