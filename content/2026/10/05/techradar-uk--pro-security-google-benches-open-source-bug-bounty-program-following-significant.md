---
title: Google benches open source bug bounty program following ‘significant rise’
  in AI submissions
source_url: https://www.techradar.com/pro/security/google-benches-open-source-bug-bounty-program-following-significant-rise-in-ai-submissions
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-05T22:02:08Z'
published: '2026-10-05T00:00:00Z'
description: Another bug bounty program choked to death on AI slop
image: https://cdn.mos.cms.futurecdn.net/6t9Lsf3QWte55CdyiDs97L-2560-80.jpg
categories:
- Technology & Software
people:
- 1Password
- Linus Torvalds
locations: []
organisations:
- 1Passwords Off-by-1 Labs
- AI Generative Artificial Intelligence
- GitHub
- HackerOne
- Linus Torvalds Google
- Microsoft
- Microsoft’s Patch
- OSS VRP
- Open Source Software Vulnerability Rewards Program
- TechRadar Pro
---

![A robot&#039;s hand typing on a laptop keyboard](https://cdn.mos.cms.futurecdn.net/6t9Lsf3QWte55CdyiDs97L-1920-80.jpg)

* **Google paused OSS bug bounty submissions after a surge of AI-generated, invalid reports**
* **AI boosts vulnerability discovery but often produces flawed, incomplete, or hallucinatory findings**
* **Rising AI-driven bounty spam has also overwhelmed curl maintainers and Linux security reviewers**

Google has revealed it is pausing one of its bug bounty program and it’s all AI’s fault.

The company said its Open Source Software Vulnerability Rewards Program (OSS VRP) is being flooded with bogus and irrelevant submissions to the point where it was simply unmanageable.

As a result, the company is pausing accepting all submissions until the end of the year, taking the time to reassess the process and come up with new solutions.

## Bug hunting in the age of AI

Generative Artificial Intelligence is supercharging defenders, discovering vulnerabilities at machine speed, making software better and more resilient against exploits and zero-day vulnerabilities.

A few frontier models, including the famed Mythos and GPT-5.6-Cyber, have allowed companies to discover a hundred times more vulnerabilities in less time than ever before.

The best example is Microsoft’s Patch Tuesday. In March 2026, the company addressed 79 flaws in its products, and in April (around the time it started using Mythos) - almost double (167). From that day on, the number of patched bugs grew significantly month-over-month: 200 in June, 400 in August, and 966 in September. In just half a year, Microsoft started fixing more than ten times as many flaws.

However, machines still cannot be trusted to discover and patch vulnerabilities entirely on their own. In early August, security researchers from 1Passwords Off-by-1 Labs set out to see just how good AI was at discovering and fixing flaws and found that half (49.3%) of the patches failed to fix at least one existing exploit path. A fifth (20.1%) fixed the original issue but changed application behavior, while 2.3% introduced new security issues. Funny enough, 2.2% failed to fix the vulnerability while also introducing additional exploit paths, as well.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Even among the patches that might be considered (26% of clean ones and 20.1% of those that changed app behavior), more than a third were fragile and not entirely addressing the underlying problem. 1Password concluded that missing context was the number one challenge, finding that when given proper background information, AI was able to produce significantly better results.

Despite not being able to provide their AI with wider context, many security researchers still use AI for vulnerability discovery. Simple prompts, very little analysis, and even less human oversight, results in “discoveries” that are incorrect, unsubstantiated, and sometimes outright hallucinated. As a result, Google is (temporarily) stepping away from bounty submissions:

“We are temporarily no longer accepting OSS VRP product vulnerability submissions. This does not impact OSS VRP supply chain reports, or any outstanding reports. As an alternative, we encourage you to find impact across our other VRP programs and submit there instead, or pursue the Patch Rewards Program,” Google said in a short tweet, published on October 1 2026.

“Why is this happening? This pause is due to a significant rise in automated submissions, the vast majority of which are not valid. We will continue to reformat and work on this aspect of the OSS VRP and commit to giving an update in Q1 2027.”

## HackerOne and Linus Torvalds

Google is not the first company whose bug bounty program choked to death on AI slop. In late January 2026, the developers of curl, the open source command-line tool and software library, announced killing their HackerOne bug bounty program due to being flooded with fake problems and vulnerabilities.

In an advisory published on GitHub, it was said that the program is being sunsetted at the end of January, 2026.

“Up until the end of January 2026 there was a curl bug bounty. It is no more,” the document reads. “The curl project no longer offers any rewards for reported bugs or vulnerabilities. We also do not aid security researchers to get such rewards for curl problems from other sources either.”

A few months later, in May, lead maintainer of the Linux security mailing list, Linus Torvalds said it was “almost entirely unmanageable” due to researchers using AI to flood it with useless reports.

“The continued flood of AI reports has basically made the security list almost entirely unmanageable, with enormous duplication due to different people finding the same things with the same tools,” he said. “People spend all their time just forwarding things to the right people or saying "that was already fixed a week/month ago" and pointing to the public discussion”.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
