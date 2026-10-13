---
title: ChatGPT's answers could soon contain invisible watermarks — here's why OpenAI
  wants to change the way AI text works
source_url: https://www.techradar.com/ai-platforms-assistants/chatgpt/chatgpt-will-soon-start-secretly-watermarking-its-answers-heres-what-that-means-for-the-text-you-copy-and-share
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-13T17:03:03Z'
published: '2026-10-13T00:00:00Z'
description: OpenAI is preparing to watermark ChatGPT's text — and you might never
  even notice it's there.
image: https://cdn.mos.cms.futurecdn.net/EoGmdNQvdM9usyKCgheR6K-1920-80.jpg
categories:
- Technology & Software
people:
- Claude
locations:
- UK
- US
organisations:
- Anthropic
- ChatGPT
- EU
- European Union
- OpenAI
---

![A split image of a ChatGPT logo and an EU flag.](https://cdn.mos.cms.futurecdn.net/EoGmdNQvdM9usyKCgheR6K-1920-80.jpg)

I wrote earlier this year about Claude’s decision to comply with the EU AI Act, which requires all AI-generated text to be identifiable as AI, and start to insert a watermark into its text. Rather than limit this to EU customers, however, Anthropic decided to roll the feature out globally, which seemed a bit of an overreaction at the time.

OpenAI has now announced that it is following suit, but limiting the geographical areas of impact to the EU only. It is going to start inserting watermarks into generated text, but only for ChatGPT customers who live in the EU. That means that US and UK users won’t be affected at all.

OpenAI announced the change on October 5 saying: “Over the coming weeks, we will add an invisible watermark to eligible ChatGPT and Codex text output in the European Union.”

## Inserting the watermark

To insert the watermark, which involves subtly changing the word choice for generated text, OpenAI is using a system of its own called textGrain. A note on the OpenAI website says: “Our text watermarking technology, textGrain, adds an invisible statistical signal to the model’s word choices. Our detector looks for that signal to assess whether a passage contains an OpenAI watermark. More details about how textGrain works can be found in our technical report⁠, which will be updated with additional details in the coming weeks.”

Like many people, I find that idea that the word choice of the AI that I’m paying to use is now being influenced by a watermarking algorithm, not by what’s optimal for me the customer, to be deplorable. I’m not saying that the resulting text will automatically be worse because of the watermark, but it certainly won’t be optimal.

It also sounds like it’s an easily broken solution that is full of holes. To detect AI text that’s produced using textGrain's watermarking a special AI detection tool needs to be used, which it’s currently unavailable to the public. OpenAI says it is providing detector access to researchers and expert organizations and that approved researchers and expert organizations can apply starting today.

“The tool will report whether it detects an OpenAI watermark”, continues the OpenAI article “without identifying the user or revealing their prompts or conversations. Given the risk of missed watermarks and false positives, we are not making it publicly available at launch.”

Sign up for breaking news, reviews, opinion, top tech deals, and more.

So if the detector tool isn’t being made public it begs the question, what is this supposed to accomplish?

![A close up of ChatGPT on a phone, with the OpenAI logo in the background of the photo](https://cdn.mos.cms.futurecdn.net/SSrgDUXsJwUVxtvheg4YCM-1200-80.jpg)

## A box-ticking act?

The OpenAI article specifically says that detectors are prone to errors. That “shorter or more constrained text is harder to detect”, and that “editing can weaken the watermark”. It already sounds flawed, but what happens if you try and circumvent it completely by asking ChatGPT not to write in a way that can be detected, or to not use textGrain. Will it do it?

All of which leads me to conclude that the move by OpenAI looks a lot like a box ticking exercise to comply with the EU AI Act, which it is forced to do, since it requires generative AI providers to make generated text identifiable in a “machine-readable way”

It’s reassuring to hear that the changes are only going to be implemented inside the EU and that the text will remain private when the detector is used, but I suspect most ChatGPT users would rather OpenAI concentrated on producing the best possible answers rather than making those answers easily identify as AI-generated.

There’s also something fundamentally strange about a system that deliberately changes the words an AI chooses, without telling you which ones, to insert a watermark that can potentially be removed simply by editing the text. If the goal is to make AI-generated content more transparent, then surely the answer should be something that actually works, rather than an invisible signal that nobody outside a select group can even check for themselves.
