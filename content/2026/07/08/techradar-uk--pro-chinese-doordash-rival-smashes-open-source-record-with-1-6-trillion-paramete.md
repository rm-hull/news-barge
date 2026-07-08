---
title: LongCat-2.0 outperformed Gemini 3.1 Pro on several coding benchmarks
source_url: https://www.techradar.com/pro/chinese-doordash-rival-smashes-open-source-record-with-1-6-trillion-parameter-llm-with-a-1-million-context-token-model-crafted-without-nvidia-hardware
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-08T03:39:43Z'
published: '2026-07-08T00:00:00Z'
description: China's chip self-reliance push produces its most ambitious homegrown
  AI model to date, yet
image: https://cdn.mos.cms.futurecdn.net/hQtTkoYUP8T6i7tWxMcj58-1920-80.png
---

![Chinese Chip](https://cdn.mos.cms.futurecdn.net/hQtTkoYUP8T6i7tWxMcj58.png) 

- **LongCat-2.0 contains 1.6 trillion parameters and a million-token context**
- **Meituan trained the model using over 50,000 domestic AI accelerators**
- **The model completed pre-training entirely without any Nvidia hardware involved**

Meituan has released LongCat-2.0, an open source large language model containing 1.6 trillion parameters and supporting a 1 million-token context window.

This scale places the model roughly on par with DeepSeek's flagship V4-pro, which launched back in April this year.

Meituan says LongCat-2.0 completed full process training on a computing cluster containing more than 50,000 domestic AI accelerators, making it the first trillion-parameter model to achieve that scale.

## Domestic hardware reaches a new training milestone

The announcement comes as China continues expanding domestic computing capabilities amid export restrictions limiting access to advanced United States graphics processors.

Unlike DeepSeek V4-pro, which relied on Chinese chips only during inference, LongCat-2.0 also completed the far more demanding pre-training stage using domestic hardware.

This means that the company has entirely avoided the use of foreign AI hardware such as those from Nvidia.

The company said the system was built entirely on large AI ASIC superpods while using Huawei's Collective Communication Library to improve communication stability across processors.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

China’s home-grown AI chips have been widely adopted for model inference amid Beijing’s push for technology self-reliance, although pre-training has remained significantly more difficult.

Meituan claims that LongCat-2.0 showed strong performance in coding and agent-based tasks while exceeding Google’s Gemini 3.1 Pro across several benchmarks, including Terminal-Bench 2.1 and SWE-Bench Pro.

Nevertheless, it acknowledged that its latest model still trails OpenAI’s GPT-5.5 and Anthropic’s Claude 4.8 Opus on broader frontier capability assessments.

“This put to rest any concerns of Atlas-950 SuperPoDs [being] unable to train large LLMs for [Zhipu AI] and DeepSeek,” said tech analyst TP Huang.

## Technical hurdles remain despite larger ambitions

Despite the successes recorded by Meituan, this does not come without the significant hurdle of replacing Nvidia hardware.

The company faced major engineering difficulties throughout development despite completing training without relying on restricted foreign graphics processors.

Meituan said memory became the primary bottleneck because each domestic accelerator offered substantially less capacity than Nvidia’s H800 chip, which remains unavailable for export to China under United States rules.

Engineers therefore built additional optimisation systems intended to maintain stable, secure, and scalable training across the cluster despite its considerable size and complexity.

Hanchi Sun, a computer science PhD researcher, described the achievement by writing, “Near frontier performance, trained on 50k Chinese domestic accelerators,” before adding, “The first ever to achieve this!”

LongCat-2.0 has not yet appeared on major independent evaluations including Artificial Analysis, Arena, Agents’ Last Exam, or CyberGym, leaving external verification of several reported capabilities outstanding.

However, the release suggests Chinese developers are attempting to reduce Nvidia dependence by expanding domestic hardware beyond inference into large-scale training.

Broader benchmark results across AI tools will ultimately determine how competitive this approach becomes going forward.

Via SCMP

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Efosa Udinmwen](https://cdn.mos.cms.futurecdn.net/nwRLdPUNG4rWu4Y6nthHDV.png)

Efosa has been writing about technology for over 7 years, initially driven by curiosity but now fueled by a strong passion for the field. He holds both a Master's and a PhD in sciences, which provided him with a solid foundation in analytical thinking.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
