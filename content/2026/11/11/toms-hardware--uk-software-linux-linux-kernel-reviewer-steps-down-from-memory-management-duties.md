---
title: Linux kernel reviewer steps down from memory management duties due to influx
  of AI slop patches — 'the amount of time wasted on AI slop is already too much,
  and we're only at the start of this,' volume of submissions coupled with low manpower
  forces the step back
source_url: https://www.tomshardware.com/uk/software/linux/linux-kernel-reviewer-steps-down-from-memory-management-duties-due-to-influx-of-ai-slop-patches-the-amount-of-time-wasted-on-ai-slop-is-already-too-much-and-were-only-at-the-start-of-this-volume-of-submissions-and-low-manpower-forces-the-step-back
source_site: Tom's Hardware
source_slug: toms-hardware
description: Linux kernel memory-management code reviewer steps down due to influx
  of AI slop patches — volume of submissions coupled with low manpower forces the
  step back
image: https://cdn.mos.cms.futurecdn.net/kon7SwBMMWzk9ubzEnMVjY-1000-80.jpg
published: '2026-11-11T00:00:00Z'
scraped_at: '2026-11-11T19:36:22Z'
categories:
- Technology & Software
- Hardware
people:
- Bruno Ferreira
- Linus Torvalds
- Lorenzo Stoakes
locations: []
organisations:
- AI
- Get Tom's Hardware
- Huge Pages
- PC
- THP
- Tom's Hardware
---

![penguin](https://cdn.mos.cms.futurecdn.net/kon7SwBMMWzk9ubzEnMVjY-1000-80.jpg)

The Linux Kernel is probably one of the best ecosystems to observe regarding the impact of AI in programming. The critical importance of its code and its maintainers' quality standards mean that patches, including but not only AI slop, go through rigorous review and are often discarded. Still, the amount of AI-produced code is often far higher than what the human reviewers can deal with. Lorenzo Stoakes, a lead Linux reviewer for memory management, has elected to step down from some of his former duties for exactly that reason.

Stoakes announced his decision today in a thread on the Linux kernel mailing list (LKML). He'll be leaving the core, reclaim, Rust, THP (Huge Pages), and miscellaneous sections of the kernel memory management section, while staying on for his remaining duties, including KVM. The partial departure appears amicable, and the developer doesn't appear to be angry or bitter. He says that his decision was due to the mounting pressure on his inbox, that he'll wrap up the patch series he's currently working on, and he'll occasionally pitch in regardless.

However, the underlying cause is also clear: "Of course the AI wave has been horrible, and is getting significantly worse. At first it was once in a while that I'd see slop. Then it was at least once a week. Then every few days. Nowadays it's pretty much half of what I see, if not more."

This is a sentiment echoed by many programmers in the open-source community, and the latest in a running series of AI-provoked project departures, submission rules adjustments, and strategic shifts. AI-assisted programming has arguably been both a boon and a curse for open-source software. The project's open nature means that anyone can find a bug and report it or fix it, or add functionality — all of which are good things.

However, that also means that literally *anyone* can contribute, and in a world ridden with low-effort AI slop and untold amounts of AI agents, that's... suboptimal. Open-source projects are arguably the hardest-hit because they very rarely have the adequate manpower or funds to keep the code up to date, much less deal with the output of a million robotic monkeys on a million digital typewriters.

Linus Torvalds, creator and headmaster of Linux, has taken a pro-AI stance, supported not only by the speed of additional contributions, but also the fact that bots often don't make mistakes that even seasoned developers do. This topic has been the subject of a lot of LKML discussion, and the current stance is that AI-assisted code commits don't need to be marked as such.

The problem, then, has arguably become one of filtering: it's easy enough to be accepting of AI contributions when your day isn't spent waddling through mud to find the one gold nugget, which is what Stoakes was seemingly weary of.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Back in July, he'd already brought up concerns about the "recent wave of slop in [memory management]," adding that "the amount of time wasted on AI slop is already too much and we're only at the start of this." Even as recently as a month ago, he said that "what kills the project is having 1,000 slop submissions that 2 or 3 people have to do something with."

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G-140-80.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.
