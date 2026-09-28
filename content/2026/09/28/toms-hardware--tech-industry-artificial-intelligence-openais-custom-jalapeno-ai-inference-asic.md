---
title: OpenAI's custom Jalapeno AI inference ASIC is for OpenAI’s internal use, but
  company leaves the door open to broader rollout — firm says it will have its ‘hands
  full’ with Jalapeño for ‘a good long time’
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/openais-custom-jalapeno-ai-inference-asic-is-for-openais-internal-use-but-company-leaves-the-door-open-to-broader-rollout-firm-says-it-will-have-its-hands-full-with-jalapeno-for-a-good-long-time
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-28T21:14:16Z'
published: '2026-09-28T00:00:00Z'
description: OpenAI isn’t going up against Nvidia… at least not yet.
image: https://cdn.mos.cms.futurecdn.net/fG6k3NRNFC6buLLATBY3Z7-1920-80.jpg
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
people:
- Blackwell
- Jalapeño
- Kimi
- Richard Ho
- Sam Altman
- Tom
- Vera Rubin
locations:
- OpenAI
organisations:
- ASIC
- ASICs
- Broadcom
- DeepSeek
- GB300
- Get Tom's Hardware
- Google News
- Grace Blackwell
- Hot Chips
- Jalapeño
- Kimi K2.5
- Nvidia
- OpenAI
- Tom’s Hardware
- VP
- VR Ultra
---

![OpenAI&#039;s Jalapeno ASIC.](https://cdn.mos.cms.futurecdn.net/fG6k3NRNFC6buLLATBY3Z7-1920-80.jpg)

Following the reveal of OpenAI’s Jalapeño ASIC, a clear question formed: Who is this for? That’s not to say the accelerator doesn’t have a purpose, but rather that OpenAI didn’t clearly define what its ambitions were in the hardware space. On one hand, the company suggested it was building ASICs for its own purposes when OpenAI and Broadcom revealed their partnership last year. On the other hand, OpenAI laid out benchmarks comparing Jalapeño to Nvidia’s Blackwell accelerators and doubled down on a multi-generational roadmap at Hot Chips 2026. Jalapeño is built for OpenAI’s compute needs, Richard Ho, Head of Hardware at OpenAI, told *Tom’s Hardware Premium.* However, the VP says “you could use it for anybody, honestly,” and left the door open for a wider rollout. You can read the full transcript of the interview here.

“We have such a strong demand for compute within the company. It's going to take us a good long time to even fill our own demand, which is growing all the time,” Ho said. “I think that we're going to have our hands full just providing compute for OpenAI for a good long time. That's not to say that it can't be used elsewhere. I believe it could be, but I think our priority is to make sure that OpenAI's compute needs are met first and foremost.”

The competitive positioning of Jalapeño mainly comes down to the benchmarks OpenAI shared during Hot Chips, run on SemiAnalysis’ InferenceX benchmark and comparing Jalapeño to Nvidia’s GB200 and GB300. ASICs are common, but competitive performance for them isn’t common, and for good reason. They’re built to accelerate specific workloads. With Jalapeño, however, OpenAI demonstrated the chip accelerating its own open-weight GPT-OSS model, as well as DeepSeek R1 and Kimi K2.5.

Originally, OpenAI didn’t plan to show benchmarks at Hot Chips, and the company wasn’t sure if it would present at the event at all, Ho told us. The executive reiterated the story OpenAI told on the Hot Chips stage, about how a team of engineers got Kimi and DeepSeek up and running on Jalapeño in the two months between the A0 sample and the Hot Chips presentation.

![OpenAI](https://cdn.mos.cms.futurecdn.net/PyV9Xz9GPD6kkHM73at223-1200-80.jpg)

Although Ho was clear that Jalapeño is being deployed internally and will remain internal for the time being, he certainly left the door open to a wider entry into the hardware market. Speaking on the benchmarks shown at Hot Chips, Ho said: “What we really wanted to demonstrate, to put to rest, the misperception in the industry that our custom inference chip was only for OpenAI models… It’s programmable, and it’s general purpose, and it’s not hard-coded for OpenAI models.”

One possible explanation for reluctance to enter the external hardware market is supply. Ho said “there’s a new baseline for supply,” referring to the past two years of Ho and OpenAI CEO Sam Altman touring fabs and asking for more capacity. Although Ho says “[OpenAI is] in good shape” on the supply front internally, supply to feed external customers is likely a different story.

Jalapeño works for other models, but raw competitive performance wasn’t the main design goal. When I asked about the driving force behind designing Jalapeño, Ho was blunt: “It was efficiency.” The executive pointed to efficiency as a cousin of compute, noting the power-constrained modern AI data center and how a more efficient inference engine represents more effective compute.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Ho also pointed to that same pragmatic decision-making as a driving force behind designing Jalapeño, notably around codesign with OpenAI’s internal models. “[Codesign is] something that you can’t do with a third-party silicon merchant really well because there’s a lot of research IP in the models, and so you just can’t share that widely because it will leak. It will get out there no matter how many NDAs you put in place.”

If Jalapeño were destined for a wider rollout, it wouldn’t be going up against Nvidia’s Grace Blackwell platform, but the newer Vera Rubin platform. Ho said that the comparison against Blackwell was “because those were the best published results that we could find.” However, the company has run more benchmarks internally, both against Vera Rubin and for larger context windows.

The InferenceX benchmarks only looked at 8k1k benchmarks, which represent a fixed 8,000 input tokens and 1,000 output tokens. Ho said OpenAI’s internal benchmarks show that the ASIC “seems to perform even better than the existing benchmarks from some of the other devices that are available.” More interesting is the comparison to Vera Rubin, which OpenAI says looks good.

“Obviously, but the time we deploy, it’ll be [Vera Rubin], maybe even VR Ultra in some parts of the deployment schedule. We’ve done our internal ones, but obviously we don’t publish those. Those have to come from Nvidia and other people who are able to do that.… yeah, we’re doing really well on those,” said Ho.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Jake Roach](https://cdn.mos.cms.futurecdn.net/h6PRM8bTimCTnNfoAYfjAi-140-80.jpg)

Jake Roach is the Senior CPU Analyst at Tom’s Hardware, writing reviews, news, and features about the latest consumer and workstation processors.
