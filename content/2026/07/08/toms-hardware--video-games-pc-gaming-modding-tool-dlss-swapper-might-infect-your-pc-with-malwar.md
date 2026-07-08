---
title: Modding tool 'DLSS Swapper' might infect your PC with malware if you download
  the wrong files — App creator warns against using random, user-submitted DLLs
source_url: https://www.tomshardware.com/video-games/pc-gaming/modding-tool-dlss-swapper-might-infect-your-pc-with-malware-if-you-download-the-wrong-files-app-creator-warns-against-using-random-user-submitted-dlls
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-08T14:49:40Z'
published: '2026-07-08T00:00:00Z'
description: After a recently uploaded DLL was found to contain malware.
image: https://cdn.mos.cms.futurecdn.net/cGBvPbQmkStyzNV7pnJLBo-1920-80.jpg
---

![A representation of Nvidia DLSS upscaling](https://cdn.mos.cms.futurecdn.net/cGBvPbQmkStyzNV7pnJLBo.jpg) 

DLSS Swapper is an open-source app that does exactly what it sounds like — it swaps out the appropriate DLSS files for any game, helping downgrade or upgrade its native DLSS version. While the tool itself is safe, along with the verified files it hosts, users can also upload their own DLLs to the app's GitHub repo. Unfortunately, it seems like some of these files can contain malware, disguised as helpful solutions.

WARNING: There are people uploading DLLs into the DLSS Swapper / Manifest Builder repositories with comments like "this fixed it for me".DO NOT download these files, they are likely malware.July 8, 2026


To understand how this can even happen, we need to look at the way DLSS Swapper is set up. The app uses a manifest file to dig out DLLs from verified DLSS, FSR, and XeSS libraries. The verification process is thorough, and you won't see any file pop up in-app until its security hashes match official sources. However, it can also detect unknown files from new game releases installed on a user's computer.

These files are automatically uploaded to the repository as "issues," and the app also includes an option to upload your own DLL to help out fellow gamers. As you can probably guess by now, this is where the problem lies. These files are not vetted and remain in a grey area. DLL files are basically executable code, so if any of them were modified to include malware, you wouldn't even be able to detect it before it's too late.

The file would've already executed malicious code and installed a crypto-miner, for instance, in the background that hogs your PC's resources until you finally notice something's off. As such, the creator issues a clear warning to not download random files that show up on the GitHub repo, especially if they include comments that claim some sort of miracle cure. Stick to only the sources you trust if you must go outside of the officially supported libraries.

Previously, the developer already warned against the fake DLSS Swapper website posing as the real thing. Let this serve as your reminder that the app's GitHub page is the only place you should download DLSS Swapper from. Moreover, keep in mind that hardware support is just as important as software support, so if you have an older GPU that doesn't support the latest upscaling tech, a DLL swap cannot magically fix that.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Hassam Nasir](https://cdn.mos.cms.futurecdn.net/SxxNFHt95eGK37mKPhJpdZ.jpg)

Hassam Nasir is a die-hard hardware enthusiast with years of experience as a tech editor and writer, focusing on detailed CPU comparisons and general hardware news. When he’s not working, you’ll find him bending tubes for his ever-evolving custom water-loop gaming rig or benchmarking the latest CPUs and GPUs just for fun.
