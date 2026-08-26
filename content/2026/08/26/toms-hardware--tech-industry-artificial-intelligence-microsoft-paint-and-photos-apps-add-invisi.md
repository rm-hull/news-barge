---
title: Microsoft Paint and Photos apps add invisible watermark to AI-generated content
  — developer reverse engineers GUID embedding
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/microsoft-paint-and-photos-apps-add-invisible-watermark-to-ai-generated-content-developer-reverse-engineers-guid-embedding
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-26T13:11:47Z'
published: '2026-08-26T00:00:00Z'
description: Server-issued GUID watermark gets applied to all images generated via
  Paint or Photos AI features, even those that are made locally on Copilot+ PCs.
image: https://cdn.mos.cms.futurecdn.net/Lprea3UQKgEfTJQJKLT4qa-1920-80.jpg
---

![Use Image Creator in Paint to generate AI art](https://cdn.mos.cms.futurecdn.net/Lprea3UQKgEfTJQJKLT4qa.jpg) 

Developer Xusheng Li has uncovered some previously unknown functionality deep within Microsoft’s Paint and Photos apps. The findings concern GUID watermarks. While these programs clearly add Copilot logo watermarks to images where LLM image generation has played a part in the process, Li also uncovered an invisible watermark and the process behind embedding it. To be clear, both these watermarks are merely to identify/verify imagery where AI has had a role in the creation, so GUID should not be confused with the recent controversies over Microsoft’s GDID traceable device-specific telemetry.

Li says that simple curiosity spurred him to investigate the AI features of the Paint app in Windows 11. The image generation functionality being capable of calling a remote API was expected. However, the dev got more curious when four apparent model files were found in the app path for local processing. Specifically, one of the local files was an ONNX-like model, the other 3 were encrypted ONNX-like files…

With all four files unencrypted and open to probing, investigations led to watermarker.dll being uncovered. Initially, Li thought it was just for visible watermarking tooling, leaving a Copilot logo on the bottom right of the image. It calls the AddPerceptibleWatermark function to do this. However, with curiosity stoked by the DLL file’s larger-than-expected size, the dev decided to ask AI to analyze the file. The AI found there was also a function to embed an invisible watermark.

The invisible watermarking function is called WmkWriteWatermark. Microsoft’s embedding process basically insists on this invisible watermark in its Stable Diffusion image generation output. If WmkWriteWatermark fails for any reason, the generation process will result in an error.

## Coalition for Content Provenance and Authenticity (C2PA) credentials

Li provides some further technical insight into the hidden watermark. Most strikingly, he asserts that the watermarking information mixes a server-issued GUID into the pixels. That isn’t the end of the identifying data bundling. “Paint does more than alter the pixels,” notes the dev. “It also attaches C2PA Content Credentials to the saved file. The code responsible for this lives in ProvenanceHelper.dll, backed by provenancesdk.dll.”

In conclusion, even on devices where local image generation occurs, the prompt is still sent to Microsoft servers for moderation, says Li. Moreover, the dev indicates this watermarking is mandatory, and if the process fails, Paint will abort the entire image generation process. In Photos, there is the same GUID mechanism in place when AI is used, but it will still return the image and just log an error if the watermarking process has issues.

It is thought that all this hidden processing “might be related to Article 50 of the EU AI Act, whose transparency rules took effect on August 2, 2026, and require AI-generated content to carry a detectable, machine-readable mark—but not a prompt-specific GUID.”

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Mark Tyson](https://cdn.mos.cms.futurecdn.net/56vqMYLDaKRHPhHZgbADFR.jpg)

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.

- 
Its a fine thing to make AI images easily identifiable as such. Most image generation apps do this and in a way that survives most post gen manipulation. Stable Diffusion has a cool article about how it works... it's a surprisingly complicated process.Reply
 
That said, I'm not a fan of sending local data off box for unknown purposes.
