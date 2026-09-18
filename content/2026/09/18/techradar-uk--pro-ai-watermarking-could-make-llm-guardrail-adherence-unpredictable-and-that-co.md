---
title: AI watermarking could make LLM guardrail adherence unpredictable
source_url: https://www.techradar.com/pro/ai-watermarking-could-make-llm-guardrail-adherence-unpredictable-and-that-could-be-a-big-problem-for-the-eu-ai-act
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-18T12:59:24Z'
published: '2026-09-18T00:00:00Z'
description: Researchers have revealed how AI watermarking could actually change how
  an LLM behaves, making it less secure.
image: https://cdn.mos.cms.futurecdn.net/Hc6oTvWTHfb3ETNovTaDxG-1920-80.jpg
---

![AI writer](https://cdn.mos.cms.futurecdn.net/Hc6oTvWTHfb3ETNovTaDxG.jpg) 

- **AI watermarking aims to prove the authenticity of any text**
- **New study finds it also changes LLM behavior – and in a bad way**
- **EU AI Act could mean more models have watermarks despite side effects**

New Lasso research has revealed that AI watermarking could actually unintentionally change how LLMs behave following the testing of Google DeepMind's SynthID-Text.

The company's researchers found that SynthID-Text can change whether models refuse harmful requests, their susceptibility to prompt injection, which tools AI agent choose and more.

However, at its core, SynthID-Text and other similar watermarking is only designed to hide a machine-readable indicator as to whether text was AI-generated or human-written.

## Researchers find that AI watermarking can unintentionally change AI behavior

The "watermarking procedure can therefore affect both what the model says and what an agent does," Lasso concludes, referring to the side effect as "sampling drift."

One of the biggest concerns highlighted by the paper is that, even without an attack, watermarking changed some of the models' refusal decisions, making them more willing to answer potentially harmful prompts. Combined with prompt injection, Lasso found the consequences more amplified.

Despite the unintended consequences, Anthropic recently announced that future generations of Claude would use AI watermarking similar to Google DeepMind's, stressing that one of the key drivers was to adhere to the EU AI Act. With that in mind, AI watermarking is set to become far more mainstream across other model providers, making these mishaps far more common and leading to further security concerns.

Ultimately, Lasso urges developers to rerun benchmarks, safety evaluations and other tests to check for any unintended consequences, rather than just applying it blindly to existing configurations.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

"These findings make reassessment important whenever watermarking is introduced or its configuration or key changes," Lasso concludes, stressing that the work shouldn't be taken as an argument against AI watermarking for provenance.

Additionally, the research presents a new angle on AI watermarking, because until now researchers have largely focused on whether watermarks can be both applied and detected effectively. Few have uncovered such security-focused consequences as this one.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Craig Hale](https://cdn.mos.cms.futurecdn.net/GV8qRsHBkpSAQxiYKjTt6H.jpg) 

With several years’ experience freelancing in tech and automotive circles, Craig’s specific interests lie in technology that is designed to better our lives, including AI and ML, productivity aids, and smart fitness. He is also passionate about cars and the decarbonisation of personal transportation. As an avid bargain-hunter, you can be sure that any deal Craig finds is top value!

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
