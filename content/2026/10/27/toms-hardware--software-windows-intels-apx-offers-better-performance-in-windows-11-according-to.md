---
title: Intel's APX offers 'better performance' in Windows 11 according to new Insider
  setting — Microsoft begins early enablement for Advanced Performance Extensions
  on Nova Lake CPUs
source_url: https://www.tomshardware.com/software/windows/intels-apx-offers-better-performance-in-windows-11-according-to-new-insider-setting-microsoft-begins-early-enablement-for-advanced-performance-extensions-on-nova-lake-cpus
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-27T15:33:08Z'
published: '2026-10-27T00:00:00Z'
description: Advanced Performance Extensions, or APX, will bring improved performance
  to some apps, but there are no chips that support it just yet.
image: https://cdn.mos.cms.futurecdn.net/35VQkXsW8WPQ29LfnDrSZS-1259-80.png
categories:
- Technology & Software
- Hardware
people:
- Oliver Haslam
- Tom
locations:
- Nova Lake
organisations:
- APX
- ARM
- Diamond Rapids
- GCC
- GPU
- Google News
- Intel
- LLVM
- MSVC
- Microsoft
- Oliver Haslam
- RAM
- Windows Insiders
---

![Windows 11](https://cdn.mos.cms.futurecdn.net/35VQkXsW8WPQ29LfnDrSZS-1259-80.png)

A new "Advanced Performance Extensions (APX)" option has been spotted in a version of Windows 11 made available to Windows Insiders on October 23, with the feature set to enable a boost in application performance on compatible chips. At the moment, those chips don't exist. But when they do, this feature is the one that you'll want to flick on if you're using one of them. The new toggle was reported by *Neowin* after it was first spotted by a poster on the X social network. The feature debuted in build 29295 as an Experimental build, so it's unlikely that it will make its way to the version of publicly available Windows 11 anytime soon.

Intel announced APX back in 2023, confirming that it features 16 additional general-purpose registers and three-operand instruction formats with a new data destination register for many integer instructions. Doubling the number of general-purpose registers from 16 to 32 will allow code compiled with APX to run with 10% fewer loads and 20% fewer stores than Intel 64's baseline, says Intel. APX has been available in the GCC compiler since version 14, with subsequent versions up to GCC 17, which is targeting a 2027 code freeze, adding additional support. LLVM and MSVC have preliminary support, as well. Although enablement has been going steady for the past two years, developers will still need to recompile their applications with the proper flags for APX-capable CPUs to leverage those instructions.

> Here is how the new "Advanced Performance Extensions (APX)" setting would appear on compatible hardware on 29695 [https://t.co/o5wrhnruJHOctober](https://t.co/o5wrhnruJHOctober) 23, 2026

Not that there's any real need to rush just yet. The fact that no APX-capable chips are on sale yet means that enabling the feature in Windows 11 build 29295 does nothing currently. But it's clear that Microsoft is getting its ducks in a row ahead of time. Intel's Nova Lake Core Ultra 400-series chips are expected to be the first to feature APX support, but they won't break cover until early 2027. Even then, it's likely that the 28-core version will debut first, with the 52-core model made to wait until later in the year. These are consumer chips, of course, with Intel's Xeon 7 'Diamond Rapids' bringing APX support and up to 256 cores to the data center, also in 2027.

The good news is that you might not have to buy a new chip to enjoy improved Windows 11 performance. Five years after Windows 11's debut, Microsoft has already said that it's working to make its operating system play more nicely with machines with just 8GB of RAM. But what Microsoft gives with one hand, it soon takes away: an expansion of the Windows 11 Memory Integrity feature will reduce gaming performance on some systems.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Oliver Haslam](https://cdn.mos.cms.futurecdn.net/3XaHYJa7vPsa7PG8i5U8F5-140-80.jpg)

Oliver Haslam has written about technology of all shapes and sizes for over 15 years, both online and in print. He's fascinated by how personal computing continues to change as tower PCs give way to foldable phones and beyond.

* I've read a few academic studies that have compare code with 16 vs 32 registers, that make me believe that the difference will be marginal overall.  
  *Some* algorithms with deeply nested loops that can't be vectorised or off-loaded to a GPU are the most likely to benefit.  
    
  The calling convention stays the same. It won't be like the jump from "32-bit" to "64-bit" code when the number of registers increased from 8 to 16. Reply
* It will only make sense, if they look how the ARM is doing it.  
    
  Instead only one AX real dataregister in x86, then they should make 8 x AX real dataregisters,  
  meaning you can do alegebra on 8 variables in a function with no overhead. Reply
