---
title: Nvidia's new Synthetic Video Detector can identify fake AI videos with up to
  92% accuracy — microservice based on cutting-edge research looks to combat misinformation
  in broadcasts with just 22ms processing time
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidias-new-synthetic-video-detector-can-identify-fake-ai-videos-with-up-to-92-percent-accuracy-microservice-based-on-cutting-edge-research-looks-to-combat-misinformation-in-broadcasts-with-just-22ms-processing-time
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-21T10:33:08Z'
published: '2026-07-21T00:00:00Z'
description: That's for uncompressed video, however. Compression drops accuracy down
  to 82%.
image: https://cdn.mos.cms.futurecdn.net/TqRBtTVuFNuTyayvtrdhPb-960-80.jpg
---

![NVIDIA AI for Media Helps Newsrooms Detect Synthetic Video](https://cdn.mos.cms.futurecdn.net/TqRBtTVuFNuTyayvtrdhPb.jpg) 

We live in an age where artificial intelligence increasingly dominates the internet, making it harder to distinguish real content from fake news. Any picture or video you see today could be AI-generated and the traditional markers that would give it away are fading rapidly. There are tools that help identify if something has been made with AI, and Nvidia — arguably the main beneficiary of the AI race — has just released its own, called the "Synthetic Video Detector" (SVD).

SVD is an Nvidia Inference Microservice (NIM) part of the company's AI for Media Private Access Program, so it's not publicly available to consumers, but a demo exists. Anyhow, SVD's job is simple: detect whether a video is real or if was generated using AI. It can analyze videos at scale, breaking them down frame-by-frame to spot anomalies. It's based on cutting-edge research that won awards at computer vision conference ICCV.

Instead of looking at the video file as a whole, SVD splits it into cropped frames, each carrying a 504x504 resolution. These frames are then passed through two powerful Vision Transformers made by Meta: DINOv2 and DINOv3. A job of a vision transformer is to learn to form patterns without needing human-labeled data. They're commonly used for image classification, image retrieval, object detection, and depth estimation.

As such, once the frames go through these transformers, their distinct spatial features are quickly assessed, and each one is assigned a score between 0 and 1 — 0 representing a fully real image and 1 representing a completely fake image. The scores are tallied at the end to form an average, which tells the user whether the video is real or not based on a percentage score out of 100.

This way, news agencies, broadcasters, and media outlets can authenticate footage they receive much quicker and with better certainty. SVD is even designed to work with the reality of social media compression since videos uploaded online will have their imperfections masked. But the transformers can still detect patterns that the human eye cannot, seeing past surface-level anomalies to instead focus on intrinsic artifacts.

 ![Nvidia Synthetic Video Detector accuracy benchmark](https://cdn.mos.cms.futurecdn.net/KcwngYNZMvrAAUVhVwrcuC.jpg) 


As visible in AI GVD bench above, uncompressed video still delivers the best results with SVD showing an insane 92% accuracy rate. At 15% compression, the model drops down to 87% accuracy, while a 50% compression rate still achieves a very impressive 82% accuracy in detecting AI-generated content. Since this is a microservice, it has exceptional latency as well, processing 1080p video in just 22ms on Nvidia RTX GPUs and 30ms on Nvidia's workstation models.

 ![Trying out Nvidia's Synthetic Video Detector](https://cdn.mos.cms.futurecdn.net/AXJ9rbw5FqoLS5fzfUiCz4.png) 


That being said, SVD requires the NVENC encoder, so datacenter cards like the B100 cannot run it natively. Nvidia said it's already working with Wowza to bring real-time synthetic video detection into livestreaming workflows. A demo version is available to try right now at build.nvidia.com but beware that it takes a long time to process since it happens in the cloud, the max file size limit is only 100MB, and it often just times out.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Hassam Nasir](https://cdn.mos.cms.futurecdn.net/SxxNFHt95eGK37mKPhJpdZ.jpg)

Hassam Nasir is a die-hard hardware enthusiast with years of experience as a tech editor and writer, focusing on detailed CPU comparisons and general hardware news. When he’s not working, you’ll find him bending tubes for his ever-evolving custom water-loop gaming rig or benchmarking the latest CPUs and GPUs just for fun.
