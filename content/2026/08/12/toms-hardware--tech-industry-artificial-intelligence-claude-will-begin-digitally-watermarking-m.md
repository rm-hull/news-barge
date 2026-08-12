---
title: Claude will begin digitally watermarking marking AI-generated text and images
  — Anthropic details how it'll comply with the EU's Artificial Intelligence Act
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/claude-will-begin-digitally-watermarking-marking-ai-generated-text-and-images-anthropic-details-how-itll-comply-with-the-eus-artificial-intelligence-act
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-12T13:38:21Z'
published: '2026-08-12T00:00:00Z'
description: Text will carry a hidden "statistical pattern," but image pixel watermarking
  is notably absent.
image: https://cdn.mos.cms.futurecdn.net/zjfSQKUXKQ67NcVL4GFPQU-1920-80.jpg
---

![A representation of a digital fingerprint being scanned](https://cdn.mos.cms.futurecdn.net/zjfSQKUXKQ67NcVL4GFPQU.jpg) 

The identifiability of AI-generated content is critical as more and more people use text and images from these services, and the European Union's Artificial Intelligence Act (AIA) set a deadline of August 2, 2026 for AI service providers to start implementing identifiability measures. To that end, Anthropic has published a guidance article detailing how new versions of Claude will comply with article 50 of the law specifically.

The legislation is accompanied by a Code of Practice with suggestions for implementation, and in keeping with that code, all new Claude models will watermark text and add provenance data to generated files, namely images (of SVG, PNG, and JPG file types). Anthropic's guidance is a bit late to the party, as OpenAI and Google already published their own versions a while back.

When it comes to text, unlike steganography in images that hides data in the picture content, the lab says that watermarking is performed by biasing the selection of tokens (parts of words) during generation. When the generated text is analyzed, it'll fit a determined statistical pattern, revealing the watermark. Anthropic says it'll provide detection tools that look for these patterns in "forthcoming technical documentation."

Text that is copied-and-pasted and only lightly edited should retain the identifiable pattern. Anthropic says that the quality and meaning of the generated text won't suffer as a result of the marking process. Slices of text under 200 tokens are exempt under the Code of Practice, as they don't carry sufficient data to reliably watermark.

As for images, the aforementioned file types support additional metadata attached to the picture itself, and Claude will start adding a provenance certificate using the C2PA standard. In simplified terms, the files will carry an associated digital certificate that will be invalidated if the file is altered in any way.

Attentive readers might note there's no mention of actual image watermarking, and indeed Anthropic made no mention of that feature, although it's a requirement of the Code of Practice for images, alongside the provenance information. It's expected the firm will implement image watermarks at some point, otherwise, just copy-pasting the picture content would make it untraceable.

Anthropic also says that it's working to add these capabilities to existing Claude models — as required by the AIA, with a deadline of December 2, 2026. The company's guidance starts by describing "models launched in the EU," but subsequent paragraphs clarify that "marking will apply to output from supported models wherever Claude is offered, worldwide."

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

The text further notes that direct quote content may be erroneously watermarked as part of a response, and that the lack of a text watermark is no indication that the content wasn't AI-generated or processed. The AIA also requires service providers to offer tools to detect watermarks, and Anthropic says it'll "share details in forthcoming documentation."

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.

- 
I'm curious, because I has the dumb, whether this watermark would "appear" in documents created directly by Claude, or does it ride along with any generated text that is copy/pasted? For example, if I have a document that 75% me, and 25% AI-generated text that I copy/pasted, is someone on the other side going to be able to identify the AI-generated text via this watermark?Reply
