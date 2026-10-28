---
title: The most important part of AI chatbots is being ignored
source_url: https://www.newscientist.com/article/2596083-the-most-important-part-of-ai-chatbots-is-being-ignored/?utm_campaign=RSS|NSNS&utm_content=home&utm_medium=RSS&utm_source=NSNS
source_site: New Scientist
source_slug: new-scientist
scraped_at: '2026-10-28T12:50:33Z'
published: '2026-10-28T00:00:00Z'
description: AI firms can increase the power of their chatbots without updating to
  new models. Columnist Jacob Aron explains how a simple bit of software can give
  AI a boost – and whether AI will soon be able to rewrite that code itself
image: https://www.newscientist.com/wp-content/uploads/2026/10/SEI_316613318.jpg
categories:
- Science
- Technology & Software
- Business & Entrepreneurship
people:
- Adam King
- Claude
- Jacob Aron
- Sam Altman
locations: []
organisations:
- AI
- API
- ARC-AGI
- Anthropic
- Astra
- ChatGPT
- Google
- LLM
- New Scientist
- OpenAI
- Talk to Transformer
- US Securities and Exchange Commission
---

![](https://www.newscientist.com/wp-content/uploads/2026/10/SEI_316613318.jpg?w=840)

ChatGPT was never meant to start a revolution. When it launched in November 2022, OpenAI CEO Sam Altman called it “an early demo” and expectations were low. Personally, my initial reaction was that it seemed no more capable than previous large language models (LLMs) OpenAI had released; it just had a nicer interface. Obviously, I was wrong to dismiss the importance of the interface, but in 2026 I think most people who use AI are making a similar mistake without even realising it. What you think of as ChatGPT or Claude or any other chatbot from a big AI brand is actually many pieces of software wrapped into one, and we are ignoring the most important: the harness.

To understand what a harness is and how it works, it helps to break down the multiple things we call ChatGPT. At the very bottom is the LLM, currently a version of GPT-6, but this gets switched out when OpenAI releases new model families. LLMs do one thing: given a string of text, they predict the most likely next characters. OpenAI’s first model, GPT-1, was released in 2018 as a piece of software that you had to download and run on your computer through a terminal, the text-based interface to a computer that most of us avoid. The same was true of GPT-2 in 2019, until an independent software developer called Adam King created Talk to Transformer, a now-defunct website that allowed you to enter a prompt and get a GPT-2 response in return. Back-and-forth chat wasn’t possible, but this was an early example of an interface, in this case a website, sitting on top of a model.

In 2020, OpenAI released GPT-3 and, for the first time, allowed people to access it through an application programming interface (API), its first commercial product. APIs are a standard way for one computer to communicate with another – for example, Google has a Google Maps API that lets a piece of software send a request for location data. OpenAI’s API let anyone create software that could plug in to GPT-3. At the time, I played with a few of these and found them interesting but clunky – the text they produced was often incorrect or flawed in some way, though it was cool that this level of text generation was even possible. This was essentially still a time of “raw” LLM output, with no guard rails – if you asked GPT-3 to produce hate speech or instructions to build a bomb, it would do so to the best of its ability.

Advertisement

That changed with the release of GPT-3.5 and, at the same time, ChatGPT, which was first called “Chat with GPT-3.5” until a last-minute name change. That original name reveals the way OpenAI saw ChatGPT, as simply an interface to a model, and this explains my reaction as well – the results I got from playing with ChatGPT seemed to be similar to GPT-3, just easier to use.

Actually, there was a crucial difference. With GPT-3.5, OpenAI had attempted to install guard rails that would prevent the model from producing text it deemed harmful, with software that would screen inputs and outputs. These didn’t work very well – you could get around them by asking for a malicious request to be fulfilled in the form of a poem, for example – but this was the beginning of a move away from raw LLMs to ones mediated by a harness sitting between the model and the interface.

Today, the ChatGPT product, whether that’s the app on your phone or the website, has an extensive harness that is mostly hidden from the user. It allows the model to do things like search the internet, read documents, or “reason”, meaning to continuously prompt itself through a “chain of thought” to produce better results. OpenAI also has another, more complex harness for its models, called Codex, which allows the LLM to more directly control a computer and so is particularly useful for writing computer code.

Why does any of this matter? Well, the dirty secret of the big AI firms is that their best models are, to some extent, interchangeable. The technology behind an OpenAI GPT model, a generative pre-trained transformer, is the same as the one used by Anthropic, Google or any other AI company. There are important differences in the data and computing power used to train these models, but generally they are all headed in the same direction, which is why the companies are constantly racing to claim the crown of “best” model before another one takes its place.

What really makes the difference is the harness. To illustrate this, I gave the same prompt – “Who am I?” – to the same model, GPT-6, in three different ways. Via API, I got a response beginning: “I don’t know your identify from this chat.” From chatgpt.com, without being logged in, I got a response that started “That’s a big question. 🙂”. When logged in to my personal account, the response began “You’re Jacob Aron, a senior editor at New Scientist, with a strong interest in mathematics, science, technology and the limits of what we can actually know.”

But the harness matters much more than simply knowing a few facts about the user. In the ARC-AGI test, considered to be one of the leading measures of model “intelligence”, models are tested using either a stripped-down harness that is standardised across all models, or a “provider adapter” that allows access to specific tools each AI firm has built. The difference is remarkable – for GPT-6 Astra, OpenAI’s leading public model, test scores jumped by as much as 80 percentage points when using the provider adapter harness rather than the standard one. For an earlier model, GPT-5.6 Sol, OpenAI found that just tweaking two settings in its harness tripled the resulting ARC-AGI score.

If harnesses are so important, why don’t we talk about them more often? Why don’t AI firms shout about their new harness, rather than just their latest model? I think there are a few reasons. The first is simply that they are complicated and technical – I have taken a whole article to explain them – and your average chatbot user doesn’t really need to know about it. But the second is that they are, in a way, boring. The cost of training a leading LLM is approaching $1 billion, a Herculean effort that requires number crunching across a vast army of computer processors. Once LLMs are trained, we still don’t really know exactly how they produce the results that they do, providing an air of mystery. Harnesses, on the other hand, are just ordinary software, lines of code written by humans that anyone can read.

But here is where it gets really interesting. If a harness is just code, can an AI write and improve its own harness? That is currently an open research question, both inside the AI firms and for academics. For example, in a paper published this August, one research team tested models by identifying repeated failures and proposing tweaks to their harnesses that would address the failures, seeing improvements of around 10 to 40 percentage points on benchmarks. This is why I think we are going to be hearing much more about harnesses in the near future. If the goal of the AI firms is recursive self-improvement – an AI that can build a better AI – then the harness, not the model, could be the key to achieving it.

## Further AI reading:

* OpenAI appears to have , as part of a release that saw new results in maths and physics as well. Interestingly, it is taking a slightly different approach for each of them based on feedback from academics. For the maths result, related to a problem about spinning a needle, OpenAI has released the AI output in full. It is doing the same for the computer science result, a refutation of a conjecture called the exponential time hypothesis, while also funding a conference to discuss it. The physics result is being held back until it is reviewed by external experts. It seems like OpenAI is still trying to figure out what to do about its models stepping on academics’ toes.

* Anthropic has released details of its business ahead of a planned initial public offering (IPO) on the stock market later this year. It calls AI “the most consequential technology in human history” (no surprises there) while also warning that it may pose “catastrophic or existential risks to humanity” – again, not particularly surprising given Anthropic’s public record, but it does raise eyebrows to see this language in documents filed with the US Securities and Exchange Commission.
