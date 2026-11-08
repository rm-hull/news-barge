---
title: The end of an era as Linux 7.5 purges the last 30-year-old Intel MMX optimizations
  from Pentium age — open-source OS retires ancient 1997 Pentium instructions to streamline
  code
source_url: https://www.tomshardware.com/software/linux/the-end-of-an-era-as-linux-7-5-purges-the-last-30-year-old-intel-mmx-optimizations-from-pentium-age-open-source-os-retires-ancient-1997-pentium-instructions-to-streamline-code
source_site: Tom's Hardware
source_slug: toms-hardware
description: Linux developers are preparing to make Intel’s ancient MultiMedia eXtensions
  irrelevant, with the last MMX code now set to be removed from the kernel.
image: https://cdn.mos.cms.futurecdn.net/rXG5LfQBM4KrVowgfX4A3g-1920-80.jpg
published: '2026-11-08T00:00:00Z'
scraped_at: '2026-11-08T17:56:03Z'
categories:
- Technology & Software
- Hardware
people:
- Mark Tyson
- Tom
locations: []
organisations:
- 3DNow
- AMD
- Centaur
- Get Tom's Hardware
- Google News
- Linux
- MMX Intel
- Pentium
- SSE
- SSE2
- Tom's Hardware
- Transmeta
- Wikipedia
---

![Intel Pentium MMX](https://cdn.mos.cms.futurecdn.net/rXG5LfQBM4KrVowgfX4A3g-1920-80.jpg)

Linux developers are preparing to make Intel’s ancient MultiMedia eXtensions an irrelevance. Intel introduced MMX in the Pentium era, but a patch expected to merge into mainline Linux 7.5 will remove the last remaining optimized software from the open-source OS. Expected to be released in 2027, the new kernel will wipe MMX-optimized code from its software RAID XOR code, explains Phoronix.

Admittedly, there wasn’t much left in Linux in terms of MMX optimizations. But few folks will be running the most modern kernels on Pentium MMX and Pentium II chips in 2026. And most other MMX-optimized code disappeared from the OS half a decade ago, when some MMX-optimized memory management code was removed. Note that, if you are a determined late-90s Pentium devotee, you can still use software RAID, but it will lack the MMX fast path.

This is a classic case of Linux code housekeeping. With this change, the kernel will lose over 800 lines of code and replace them with just 12.

## Remembering MMX

Intel first introduced MMX Pentium chips in January 1997. Though I vaguely remember these processors being marketed as being enhanced by ‘MultiMedia eXtensions,’ Wikipedia insists that “MMX is officially a meaningless initialism[6] trademarked by Intel.”

In a subsequent trademark battle with longtime foe AMD, a document produced in court indicated that MMX stood for ‘Matrix Math Extensions.’ AMD relied on this to sidestep the trademark, as an initialism cannot be trademarked, according to the encyclopedic source.

Eventually, all rival x86 processors managed to integrate MMX instructions – so as not to be pushed into the shade during the multimedia boom. A surprisingly large number of non-Intel chips ended up offering MMX, too. Along with Pentium MMX chips, AMD, Centaur, Cyrix, Rise, and Transmeta eventually offered MMX CPUs.

After MMX's marketing success, AMD pioneered 3DNow! instructions, and about a year later, Intel fired back with SSE and SSE2.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Mark Tyson](https://cdn.mos.cms.futurecdn.net/56vqMYLDaKRHPhHZgbADFR-140-80.jpg)

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.

* The Wikipedia phrasing seems misleading.  
    
  In today's 2026 software sure MMX probably does not do much. However at the time and for many years, I think MMX was benchmarked on and benchmarked disabled and had been show to produce worthwhile gains. Reply
