---
title: TypeSafe AI's Jev offers an alternative to LLMs that's 193x faster and 445x
  cheaper
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/typesafe-ais-jev-offers-an-alternative-to-llms-that-claims-to-be-193x-faster-and-445x-cheaper-system-one-type-model-is-bespoke-for-probabilistic-decision-making
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-21T15:05:04Z'
published: '2026-09-21T00:00:00Z'
description: Last week saw the debut of TypeSafe AI's Jev, its first "System One"
  model. Rather than chatting with users like conventional LLMs, it's strictly designed
  for statement evaluation and decision-making, for programming purposes.
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
image: https://cdn.mos.cms.futurecdn.net/vfV9baSvzWu3FXSFbYgY7m-1920-80.jpg
---

![Render of a question mark](https://cdn.mos.cms.futurecdn.net/vfV9baSvzWu3FXSFbYgY7m.jpg)

Now and then, something novel appears in the AI world, amid near-constant releases of brand-new models. Last week saw the debut of TypeSafe AI's Jev, its first "System One" model. Rather than chatting with users like conventional LLMs, it's strictly designed for statement evaluation and decision-making, for programming purposes.

Jev is the brainchild of ex-OpenAI engineer Diogo Almeida, who co-wrote ChatGPT's core training techniques. According to TypeSafe's math, Jev should be both faster and more efficient than frontier AI models like GPT-6 Astra, by several orders of magnitude and purportedly up to 194x faster and 445x cheaper. Consequently, the company pins Jev's intelligence-per-dollar as "off the charts," though only practical use will tell.

TypeSafe says the main reasons for this are twofold. First, System One models are trained with its Reinforcement Learning for Calibrated Decisions (RLCD) and geared towards producing structured answers rather than producing prose. Then, presumably because there's no previous context required, individual questions in the same request can be processed *in parallel*, in opposition to LLMs' continual generation of text.

![TypeSafe Jev speed](https://cdn.mos.cms.futurecdn.net/JfJT3PLqKJARu2FFWGmdzG.png)

When you query a normal LLM, you get an open-ended text conversation; Jev simply produces answers to specific questions, all answered with a confidence factor. It's made for code, and thus machines, to use. Your code interacts with Jev's API by providing a state — a given situation and its associated data — and asks Jev to assess specific statements. The state is supplied on each individual request, and there's no global knowledge database or retained memory.

For example, a company could show Jev a list of a customer's credit card transactions, some basic customer account info, the last thing the customer wrote, and pose the question "Is the customer requesting a refund?" The answer will be yes or no, with a confidence rating. If the confidence is above, say 85%, you can proceed to ask the customer which method they prefer, with a multiple-choice of "refund", "store credit," or "unclear." Jev then offers a probability distribution for each of the refund options. Your code can then try to process the refund or ask for further clarification.

![Jev question/reply](https://cdn.mos.cms.futurecdn.net/ySokpbtyHFTUscWKXFcsY6.png)

Jev's output (and optionally input) is in a predefined data format that's essentially plain JSON. Unlike interacting with LLMs, there are no extraneous words, long-winded thinking, or necessity to ask the model for brevity. Likewise, there's no need for global contextual prompts or saved memories, often necessary to try and coax LLMs to behave as if they were minimally deterministic. Beyond providing the state and questions, operations like input parsing, date handling, or database reading remain in your own code and are of no concern to Jev.

At first sight, this might look like a more straightforward interface to an LLM, but it's fundamentally different. Jev does not need or even want the entire context leading up to the question — providing extraneous information actually lowers the accuracy, and the context window is capped at a meager 64,000 tokens. Since the bot always produces a confidence percentage, it doesn't hallucinate in the familiar chatbot sense of creating statements and data out of nowhere.

![Jev question/reply](https://cdn.mos.cms.futurecdn.net/qEJszYUbRB73bksHZwsHX6.png)

The developer, rather than Jev, is responsible for making decisions based on the answers' confidence factors. Jev can still misclassify information, fall victim to adversarial attacks, or answer literal wording rather than meaning.

It's expected that the most common use case for Jev (and presumably future System One models) will be to wrap logic workflows around posted questions, as always having a confidence factor available makes it easy to integrate it into the decision steps of something like "if we're fairly certain the user requested a refund, and they prefer store credit, and we can see that they buy more PC gear around September, also offer them a 20% deal on an RTX 5090." The documentation has other usage examples like intent routing or citation checking.

Jev's strength isn't in acting like an agent or reasoning through a broad problem — TypeSafe makes it clear that open-ended tasks are better suited to an LLM, perhaps even integrated into code that also involves Jev. An example would be a monitoring system where Jev can use its provided info to assess if there's a serious system issue, and if so, bring in an LLM to examine logs, look for a cause, and produce a report. Likewise, Jev isn't trained on customer data and doesn't make inferences from anywhere other than the provided state (and its own training).

I'm by no means an AI engineer, but my developer layman's opinion is that **if** Jev works reasonably as promised, it might fix one of the major roadblocks to deeply integrating AI in software: dealing with chatbot LLMs, which, for practical purposes, are annoyingly amorphous blobs that may or may not behave and produce the desired output — never mind*correct* output — and slowly and expensively at that. Having a simple assessment/response/confidence interface that one can easily and cleanly integrate into code without requiring specific training or carefully crafted textual incantations feels far more natural and easy to use.

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.
