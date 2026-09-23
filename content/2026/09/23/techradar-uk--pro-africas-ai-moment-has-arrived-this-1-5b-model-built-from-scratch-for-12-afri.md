---
title: A homegrown African AI model is beating bigger rivals
source_url: https://www.techradar.com/pro/africas-ai-moment-has-arrived-this-1-5b-model-built-from-scratch-for-12-african-languages-beats-google-meta-and-alibaba-while-being-8x-smaller
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-23T22:07:12Z'
published: '2026-09-23T00:00:00Z'
description: Africa's 1.5B AI model is taking on much larger systems with less computing
  power and surprisingly strong results
categories:
- Technology & Software
- Business & Entrepreneurship
image: https://cdn.mos.cms.futurecdn.net/B7rSuocnva8Sqvm2X4FHq-1920-80.png
---

![Vambo&#039;s AI MORENA, a large language model designed for African languages](https://cdn.mos.cms.futurecdn.net/B7rSuocnva8Sqvm2X4FHq.png)

* **MORENA beat 26 tested models despite having only 1.5 billion parameters**
* **The model from Vambo AI was built specifically around African languages from scratch**
* **MORENA uses fewer tokens to represent African text than major rivals**

Vambo AI has released MORENA, a 1.5B parameter language model covering 12 languages spoken across Africa, plus English, French and code.

The developers say it beats models from Google, Meta, Alibaba and HuggingFace on African language modelling and translation while being up to 8x smaller.

On a key benchmark, this LLM scored 1.408 bpb — the best of 26 models tested — beating its closest rival, which carried over five times as many parameters yet still scored only 1.423 bpb.

## Training without a borrowed foundation

The model covers Nigerian Pidgin, Igbo, Yoruba, Hausa, Kiswahili, ChiShona, isiZulu, isiXhosa, Kinyarwanda, Setswana, Afrikaans, and isiNdebele.

Most projects serving these languages continue training an existing Llama variant, which forces them to keep a vocabulary meant for English and programming text.

Vambo AI instead fixed the tokenizer, the data mixture, and the language list before training began, after comparing several vocabulary sizes for cost and efficiency.

MORENA's vocabulary encodes African text with 1.39 times fewer tokens than Gemma 3 and 1.53 times fewer than Llama 3.2 on identical passages.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

African text still costs 0.249 tokens for each byte against 0.234 for English, roughly 6% more, and the team cannot fully explain the difference.

The nearest competitor, Lugha-Llama-8B, an Africa-adapted Llama 3.1 variant, scores 1.423 bpb and loses to MORENA in eight languages out of 12.

The 12B Gemma system, by comparison, consumes roughly 11 times the compute of MORENA while producing a weaker score on the same text.

The chat-tuned instruct version scores 1.441 bpb, trailing Lugha-Llama-8B overall but leading it in five shared languages while using about 20% of its parameters.

The instruct model, after seeing three sample translations, renders English into five languages from Africa at 45.8 chrF++, statistically level with one dedicated translation system.

It trails a larger translation model by about 1.4 points, while general models of similar size typically land in a range from 9 to 14.

## A family built on 22,000 GPU hours

MORENA used 251.7B tokens during pretraining, followed by another 63B tokens during its mid-training stage.

Over 22,000 A100 GPU hours were reportedly required during development, with the associated computing resources valued at roughly $40,000.

According to the developers, this project was supported by UNDP, AIHub4SD, and CINECA, providing computing resources and other assistance during development.

This project also includes smaller releases, with versions containing 0.5B and 0.2B parameters available alongside the principal 1.5 billion model.

The 0.5B variants reportedly exceed every external system tested across 11 of the 12 languages covered by the project.

The 0.2B nano version is intended for speech-recognition rescoring, keyboard applications, and text normalisation tasks.

This nano version also costs 58 times less than Lugha-Llama-8B for each byte processed and generates 104 tokens each second on one A100 GPU.

A CPU-compatible build of the model also runs offline on a laptop, which suits settings where reliable GPU access is not guaranteed.

That gives the developers several model sizes for different computing requirements, rather than relying exclusively on the largest release.

MORENA also supports conversational applications, translation, and connections to other AI tools through its instruction-focused release.

Via Glitch Front

![Google logo on a black background next to text reading &#039;Click to follow TechRadar&#039;](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg)

***Follow TechRadar on Google News***and** add us as a preferred source** * to get our expert news, reviews, and opinion in your feeds.*

![Efosa Udinmwen](https://cdn.mos.cms.futurecdn.net/nwRLdPUNG4rWu4Y6nthHDV.png)

Efosa has been writing about technology for over 7 years, initially driven by curiosity but now fueled by a strong passion for the field. He holds both a Master's and a PhD in sciences, which provided him with a solid foundation in analytical thinking.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
