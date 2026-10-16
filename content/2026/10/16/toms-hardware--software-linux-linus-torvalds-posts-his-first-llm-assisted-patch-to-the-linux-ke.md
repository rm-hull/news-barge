---
title: Linus Torvalds posts his first AI-assisted patch to the Linux kernel, synthetic
  test clocks 23x performance leap — the bossman makes use of AI tooling himself after
  issuing clear pro-AI directives
source_url: https://www.tomshardware.com/software/linux/linus-torvalds-posts-his-first-llm-assisted-patch-to-the-linux-kernel-after-issuing-clear-pro-ai-directives-the-bossman-makes-use-of-ai-tooling-himself
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-16T11:16:45Z'
published: '2026-10-16T00:00:00Z'
description: That seemingly didn't stop the pro- and against-AI camps in the kernel
  from continuing to bicker, though.
image: https://cdn.mos.cms.futurecdn.net/8ukjVdLc3rtpkr4AXLkY9j-2041-80.jpg
categories:
- Technology & Software
- Hardware
people:
- Bruno Ferreira
- Linus Torvalds
- Tom
locations:
- Mount Pleasant
- Wisconsin
organisations:
- Google News
- LLM
- Microsoft
- PC
- Tom's Hardware
- Torvalds
---

![Robot hand on text](https://cdn.mos.cms.futurecdn.net/8ukjVdLc3rtpkr4AXLkY9j-1920-80.jpg)

After a few revisions of his position on AI-assisted contributions to the Linux kernel, Linus Torvalds has posted his own first LLM-assisted patch. The development branch purports to fix an old issue with massive cache contention when many CPUs are reading the same file — a scenario potentially encountered when using shared libraries, databases, and web servers. Several developers had already made attempts over the years at fixing the issue, all with varied results, none quite ideal as an all-encompassing solution.

![Microsoft data center in Mount Pleasant, Wisconsin](https://cdn.mos.cms.futurecdn.net/Vh4nY3pMCcmra2ymXah9S7-1200-80.jpg)

Torvalds posted his own draft for solving the problem in early 2024, and has used it on his own laptop since that time. However, he recently took the plunge and decided to "try to actually *solve* this thing using an LLM." He's now posted his solution in a development branch, and claims that he's seen a 23x performance improvement in a dedicated synthetic benchmark, though he notes that actual real-world impact will be far less significant, as "no real load" will witness those figures. If we had to guess, this improvement would benefit server workloads far more than desktop machines.

Over time, Torvalds has broadly taken a pro-AI stance on LLM tooling, at least within the purview of the tightly controlled, review-heavy environment of the Linux kernel code. Last July, he stated he's "willing to absolutely put [his] foot down" on AI haters, pointing out that an automated code review tool the kernel team uses outperforms humans, and that it caught basic programming mistakes that shouldn't have been submitted in the first place.

The team is even changing its policy to no longer require that patch authors disclose they used an AI tool when generating their code. Torvalds once again took an assertive stance, reiterating that users should treat LLMs as yet another tool, likening it to compilers or editors. In his view, he simply expects that "people do their best and [...] understand what they are doing."

Some might say that few people in the world are better-suited to properly employ an LLM than Torvalds, and by extension, kernel maintainers. There's an entire universe of difference between a senior master programmer using the LLM to speed up the boring parts of his work, and some newbie with a credit card going "claude make linux faster plz no mistakes."

However, It's not all roses. Thanks to how adept AI agents have become at recognizing common security flaw patterns, the Linux security mailing list became "unmanageable" earlier in the year. Linux has been fixing CVEs at an astonishingly rapid pace of around 2,000 per release. Still, the team's hand is being forced into dropping older hardware drivers, as they're often the target of numerous security reports, despite their negligible install base.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G-140-80.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.
