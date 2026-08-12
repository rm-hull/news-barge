---
title: '‘I think that Claude is about to start hemorrhaging customers'': Anthropic
  is watermarking ordinary text in a way you can’t see — and EU rules could push ChatGPT
  and Gemini to follow'
source_url: https://www.techradar.com/ai-platforms-assistants/claude/new-models-will-mark-ai-generated-content-from-day-one-claude-will-now-hide-an-invisible-watermark-inside-ordinary-words-heres-how-thats-even-possible-and-how-eu-rules-could-push-openai-and-google-to-follow-suit
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-12T13:39:17Z'
published: '2026-08-12T00:00:00Z'
description: Claude will start watermarking everything it writes
image: https://cdn.mos.cms.futurecdn.net/SQriLkNFMAWuNK8Fz7yhFL-1920-80.jpg
---

![Claude AI](https://cdn.mos.cms.futurecdn.net/SQriLkNFMAWuNK8Fz7yhFL.jpg) 

To comply with the EU AI Act's Article 50(2) Code of Practice on Transparency of AI-Generated Content, Anthropic has announced that “New models will mark AI-generated content from day one”.

This is a remarkable step for Claude, because it not only applies to any images it generates, which are relatively easy to watermark, but also to any text it generates.

Anthropic says that Claude models will have an “imperceptible watermark” embedded directly into generated text at the model level. It says the mark should survive copying/pasting and minor edits.

Anthropic has not yet publicly explained the exact algorithm or released a detector, so we can only speculate for now about how it might be doing this and its effectiveness.

## Hemorrhaging customers

Personally, I think that Claude is about to start hemorrhaging customers, unless the marking is relatively easy to circumvent, or all the other major AI players immediately follow suit.

If every piece of text it produces will now be easily identified as AI, then Claude becomes useless as a tool to a lot of people who are currently using it to generate text and are not being entirely honest about where that text came from.

And then there’s the issue of using Claude to proofread your human-written text — will your text now be flagged as AI if you accept Claude’s editing advice?

Sign up for breaking news, reviews, opinion, top tech deals, and more.

Your initial reaction to that might be “Good! You should be forced to reveal when AI has written something, and it’s about time people started writing on their own again!”, and you’d be entirely justified in that opinion.

But while it remains the only one of the big three AIs that’s doing this, I think we’ll see a lot of people switch to either ChatGPT or Gemini, because they don’t want to be revealed as using AI in their work.

 ![Claude AI](https://cdn.mos.cms.futurecdn.net/kQgz8fSBJp3j2YakUJFn4N.jpg) 


## How is watermarking plain text even possible?

We don’t know exactly how Anthropic is doing its marking with text yet, but my best guess is statistical watermarking during token generation rather than hidden Unicode characters or metadata. Imagine that at every point Claude is choosing among several perfectly reasonable next words:

e.g. The movie was **excellent / superb / terrific / impressive**.

Normally it chooses according to the model's probability distribution. A watermarking system can secretly divide possible tokens into preferred and non-preferred groups using a key. Claude then gives a tiny statistical nudge toward the preferred group.

One word tells you nothing. But across 500 or 1,000 words, a detector with the key can ask if the text is choosing the preferred tokens significantly more often than chance would allow. If yes, then there's statistical evidence it came from the watermarked model.

So, the watermark is more like a faint statistical fingerprint distributed across hundreds of choices, which would also explain how it can survive a copy-and-paste. You’re essentially copying the fingerprint along with the words.

## But can you crack the code?

Since Anthropic hasn’t released an AI text detector yet, it’s impossible to know how easy this code will be to break just by changing a few words. For instance, if you put your 1,000-word Claude article into another LLM and wrote “*Rewrite this completely in different words while preserving the meaning*”, would it then be impossible to detect as AI?

I’d also be interested to know how long a piece of text has to be before it can be marked in this way, and as soon as a detector is made available, I’ll be testing it.

Perhaps the bigger issue is that Claude has done this to comply with Article 50(2) of the EU AI Act. From August 2, 2026, providers of generative AI systems that produce text, images, audio, or video are required to make those outputs machine-readable and detectable as artificially generated or manipulated, insofar as that is technically feasible. Existing systems get a limited transition period until December 2, 2026 for this particular requirement.

A note on Anthropic’s statement confirms that the watermarking additions will be applied retroactively to all existing Claude models, not just any new models it produces.

Anthropic's new system is explicitly a response to those rules, and it says the watermark will apply globally, not just when Claude is being used in Europe. Broadly speaking, OpenAI and Google face the same requirement if they want to offer qualifying generative-AI systems in the EU.

They don't necessarily have to copy Anthropic's method of using statistical text watermarking, but they will need to produce output that is machine-readable and detectable, and the technical solution should be effective, interoperable, robust and reliable as far as technically feasible.

I’ve contacted OpenAI and Google for comment, and will update this article if I receive it. For now, I think if Anthropic embarks on this path as the only one of the major three AI chatbots to do so, it could have a disastrous effect on its customer base.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Graham Barlow](https://cdn.mos.cms.futurecdn.net/LRCfnbWncUizq2Z6gECPWj.jpg)

Graham is the Senior Editor for AI at TechRadar. With over 25 years of experience in both online and print journalism, Graham has worked for various market-leading tech brands including Computeractive, PC Pro, iMore, MacFormat, Mac|Life, Maximum PC, and more. He specializes in reporting on everything to do with AI and has appeared on BBC TV shows like BBC One Breakfast and on Radio 4 commenting on the latest trends in tech. Graham has an honors degree in Computer Science and spends his spare time podcasting and blogging.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
