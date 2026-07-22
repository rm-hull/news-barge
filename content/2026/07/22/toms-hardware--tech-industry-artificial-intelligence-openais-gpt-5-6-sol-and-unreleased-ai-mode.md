---
title: OpenAI's GPT-5.6 Sol and unreleased AI models break out of testing environment
  in 'unprecedented cybersecurity incident' — rogue agents hacked HuggingFace's production
  servers with 'thousands of individual actions across a swarm of short-lived sandboxes'
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/openais-gpt-5-6-sol-and-unreleased-ai-models-break-out-of-testing-environment-in-unprecedented-cybersecurity-incident-rogue-agents-hacked-huggingfaces-production-servers-with-thousands-of-individual-actions-across-a-swarm-of-short-lived-sandboxes
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-22T10:33:40Z'
published: '2026-07-22T00:00:00Z'
description: Either an impressive and frankly scary feat, or another marketing psy-op.
image: https://cdn.mos.cms.futurecdn.net/ShSMEwkvvkfPy2AxiZJ376-2048-80.jpg
---

![Menacing cyborg](https://cdn.mos.cms.futurecdn.net/ShSMEwkvvkfPy2AxiZJ376.jpg) 

Not too long ago, Anthropic CEO Dario Amodei described Claude Mythos as capable of cyber-warfare, spawning all sorts of mythology that became popular reading at investors' desks, and even at the U.S. government table, which issued an export control order for it. Now, it's OpenAI's turn to do the same, with a blog post describing how a bot cyber-gang including its upcoming GPT-5.6 Sol and an "even more capable pre-release model" all broke out of their virtual cage and eventually into Hugging Face's production infrastructure, during an attack capability test. OpenAI described the snafu as an "unprecedented cyber incident."

 ![Microsoft data center in Mount Pleasant, Wisconsin](https://cdn.mos.cms.futurecdn.net/Vh4nY3pMCcmra2ymXah9S7.jpg) 


Some may decry these revelations as marketing stunts meant to assuage increasingly suspicious investors, yet there's no denying the proven effectiveness of AI models' pattern recognition when it comes to finding vulnerabilities in software. Many professionals have even decried the industry-standard 90-day security vulnerability disclosure window as obsolete.

The usual *modus operandi,* however, involves granting a bot access to source code repositories so it can scan them for mistakes easy for our poor human eyes to miss. In the test that OpenAI described, though, Sol and its managed to find multiple vulnerabilities by analyzing its containment network and then Hugging Face's production machines, all seemingly without any initial access to source code.

OpenAI had set up an isolated environment in which Sol and its posse supposedly couldn't reach the internet. Importantly, the bots were operating "without production classifiers used to prevent models from pursuing high-risk cyber activity" — a lot of words for "no guardrails," essentially. The only network access they had was a software package installer proxy. In theory, this likely also prevented them from using any Retrieval-Augmented Generation (RAG), meaning they couldn't search for solutions online.

Given that bots have limitless patience and no need for naps, they eventually dug their own virtual tunnel to the internet at large by way of finding and exploiting a zero-day vulnerability in the package proxy software, an impressive feat if performed as described. OpenAI says it's disclosed the technical details to the vendor in question.

Once out on the internet, much like cheating students, the bots reportedly reasoned that instead of performing the ExploitGym challenges (a set of security capture-the-flag exercises for bots), they could simply find the solutions, and became "hyper-focused" on that exact goal. They deduced the data existed at Hugging Face's servers and proceeded to break into the premises using "stolen" credentials and additional unspecified zero-day vulnerabilities to gain remote code execution privileges.

Interestingly, Hugging Face's own writeup says the attack comprised "thousands of individual actions across a swarm of short-lived sandboxes, with self-migrating command-and-control staged on public services" — a live illustration of a scenario in many a science-fiction book and flick, proving once again that life imitates art. Hugging Face says that none of its customer-facing services are compromised, and that it stopped the attack using AI capabilities of its own — another familiar cliché.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

For its part, OpenAI says it's going to add controls to the bot "at the cost of research velocity," and that the incident "points to the need to further strengthen our model’s alignment, cyber protections during evaluation time, and monitoring during internal testing" — a statement that might be an obvious fact, or intended to oversell the model's capabilities. Whichever it may be, the fact is that when it comes to digital security, bots have proven quite capable. After all, even if they're not virtual Bruce Schneiers, they just need to be marginally more effective than average humans.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.
