---
title: Linus Torvalds rebukes anti-AI stances in the Linux kernel code review process,
  says 'Linux is not one of those anti-AI projects' — creator embraces AI as just
  a tool and 'clearly a useful one'
source_url: https://www.tomshardware.com/software/linux/linus-torvalds-rebukes-anti-ai-stances-in-the-linux-kernel-code-review-process-says-linux-is-not-one-of-those-anti-ai-projects-creator-embraces-ai-as-just-a-tool-and-clearly-a-useful-one
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-16T17:37:00Z'
published: '2026-07-16T00:00:00Z'
description: The flashpoint was the Sashiko code review tools.
image: https://cdn.mos.cms.futurecdn.net/2X4Y7yST9zumKE45j4EDM8-2048-80.jpg
---

![Linus Torvalds](https://cdn.mos.cms.futurecdn.net/2X4Y7yST9zumKE45j4EDM8.jpg) 

AI-generated slop code has been a plague for some open-source projects, namely but not only Gentoo Linux, Curl, and Ghostty, limiting or outright banning LLM-created contributions. And yet, just like both the models themselves get better and the people using them become more considerate, the landscape may be changing. Linus Torvalds, Linux's creator and kernel manager, has seemingly taken an accepting stance of AI-assisted tooling.

In a long comment on the Linux kernel mailing list, Torvalds spelled it out fairly clearly: "I realize that some people really dislike AI, but this is an area where I'm willing to absolutely put my foot down [...] Linux is not one of those anti-AI projects, and if somebody has issues with that, they can do the open-source thing and fork it. Or just walk away."

This discussion came regarding the usage of Sashiko, an opt-in (per-mailing-list) and apparently quite effective multi-stage code review tool that analyzes kernel patches. The project page says the tool can find 53.6% of bugs on proposed patches, and argues that that metric already puts it above human level, as the patches in question already supposedly went through human review. The false positive rate "is harder to measure," being pinned "within 20%." Crucially, Sashiko only comments on patches, and does not take action by itself.

Developer Laurent Pinchart suggested that Sashiko's output be triaged before comments were sent out to patch authors, basing the notion on the Software Freedom Conservancy's guidelines on AI-generated code. Google's Roman Gushchin, one of Sashiko's creators, pointed out that doing that would undermine the utility of the tool, and that Pinchart's position was quite anti-LLM — a sentiment echoed by Linus Torvalds in his reply.

Torvalds put it clearly: "AI is a tool, just like other tools we use. And it's clearly a useful one. It may not have been that 'clearly' even just a year ago, but it's no longer in question today," a statement that reflects his changing stance on the matter since he initially dismissed AI tools as overhyped back in 2024. He also noted that Linux is not a "social warrior" project, and that it's always been about improving technology.

To drive the point home, he remarked that the tool "keeps finding embarrassing bugs," adding that he "will very loudly ignore people who try to argue against other people from using it," while highlighting the software's rapid evolution.

Perhaps quite poignantly, Torvalds remarked that resistant developers could use some self-awareness, as "it's not like natural intelligence is always all that great either," underscoring the fact that while AI tools may not be perfect, they generally only need to be good enough for their respective use cases. The fact that Sashiko seemingly finds errors in code that underwent human review is quite illustrative.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.
