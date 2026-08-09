---
title: Experts warn this fake Claude install guide can be used to empty crypto wallets
source_url: https://www.techradar.com/pro/security/experts-warn-this-fake-claude-install-guide-can-be-used-to-empty-crypto-wallets
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-09T19:31:25Z'
published: '2026-08-09T00:00:00Z'
description: An unusually well-orchestrated attack
image: https://cdn.mos.cms.futurecdn.net/kQgz8fSBJp3j2YakUJFn4N-2560-80.jpg
---

![Claude AI](https://cdn.mos.cms.futurecdn.net/kQgz8fSBJp3j2YakUJFn4N.jpg) 

- **Huntress reverse-engineers MacSync, a six-stage macOS stealer and remote access Trojan delivered through a fake Claude Code install guide hosted on a real claude.ai share URL and promoted via a paid Google ad**
- **The lure needed almost no forgery: the page sat under Anthropic's own certificate, and the platform's safety banner repeated the attacker's chosen display name, "Apple Support," back to the reader as fact**
- **The final stage rewrites installed Ledger and Trezor apps in place so a normal launch leads to a fake recovery message that harvests the seed phrase, draining the wallets of unsuspecting victims**

Looking online for instructions on how to install Claude Code on a Mac could lead to you having your crypto wallet hijacked in the process

The victim ran a Google search, clicked the first result, a paid Google advertisement, and landed on a tidy step-by-step guide hosted on claude.ai, badged as shared by Apple Support, telling them to open Terminal and paste a single command.

What followed, according to a reverse-engineering write-up published by security firm Huntress was a six-stage macOS kill chain called MacSync: a stealer, a remote access trojan, a signed helper built to farm one specific system permission, and finally Trojanized copies of the victim's own cryptocurrency wallet apps, rewritten in place to phish the recovery phrase.

## A complex, intricate approach that resulted in a stolen wallet

The victim had pulled their machine offline before Huntress could extract the malware from disk, so the researchers reconstructed the loader's request and instead downloaded every stage from the attacker's own delivery servers.

The results showed a sophisticated campaign that had to fake little to appear legitimate.

Anthropic lets any user publish a conversation to a public share URL. The operator maliciously used that feature exactly as designed. The lure page sat on claude.ai itself, over HTTPS, under Anthropic's own security certificates. There was no lookalike domain to squint at, no certificate warning to click past, and nothing in the address bar to give the game away.

The staging went much further than that. Whoever published the share set their display name to "Apple Support," and Anthropic's own safety banner, which sits directly above the content, duly reported that the reader was looking at a copy of a chat between Claude and Apple Support.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The platform repeated the attacker's chosen name back to the reader as established fact, further cementing their 'credentials'. The conversation itself was written to read like vendor documentation, promising that the install leaves personal files untouched and makes no system-level modifications without approval.

That same design decision has surfaced before for entirely different reasons. *Wired* had reported earlier private Claude conversations were turning up in Google and Bing results, because a share link is an ordinary public web page that search engines crawl like any other.

Users accidentally exposing their own chats and an operator deliberately planting a fake install guide are two outcomes of the same property: whatever gets published to a share URL is public, indexable, and served under Anthropic's certificate.

It is also not a one-off. Huntress has previously documented the same delivery pattern with AMOS through poisoned ChatGPT and Grok conversations, a separate remote access trojan through fake Claude desktop malvertising, and fake installers for other AI tools hosted on GitHub.

The lure has changed somewhat, but the shape has not, and users need to exercise caution when clicking links or following commands from untrustworthy sources on the internet, even if they appear to come from a source that Google was paid to place above the correct answer.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Rahim Amir](https://cdn.mos.cms.futurecdn.net/9xKZFBamtEZKSChRvywbPB.png)

Rahim Amir is a UAE-based tech writer who enjoys building PCs as much as he enjoys writing about them. He has been professionally writing about PC hardware since 2023, focusing on buyer’s guides, hardware reviews, and sponsored content and features related to tech.

Having built hundreds of gaming PCs and being an avid gamer in his spare time, Rahim tends to have stronger opinions about hardware than most. This is particularly on display when he gets his way with powerful, but minimalistic RGB builds even as Small Form Factor (SFF) PCs come a close second.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
