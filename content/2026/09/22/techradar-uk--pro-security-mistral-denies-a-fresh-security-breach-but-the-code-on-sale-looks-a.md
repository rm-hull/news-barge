---
title: Mistral denies a fresh security breach, but the code on sale looks a lot like
  May's leak
source_url: https://www.techradar.com/pro/security/mistral-denies-a-fresh-security-breach-but-the-code-on-sale-looks-a-lot-like-mays-leak
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-22T21:56:40Z'
published: '2026-09-22T00:00:00Z'
description: Mistral denies it was hacked again
categories:
- Technology & Software
- Business & Entrepreneurship
image: https://cdn.mos.cms.futurecdn.net/4AyzfXeFQkSE3gFjYpNsAQ-1672-80.png
locations:
- Monero
people:
- Mistral
- Rahim Amir
organisations:
- CyberSec Guru
- FrenchBreaches
- Google News
- HackRead
- MAI-2026-002
- Microsoft Threat Intelligence
- Mini Shai-Hulud
- Mistral AI
- PC
- PCs
- RGB
- SFF
- Seller
- TanStack
- TeamPCP
- TechRadar Pro
- Telegram
- The CyberSec Guru
---

![The Logo for Mistral AI](https://cdn.mos.cms.futurecdn.net/4AyzfXeFQkSE3gFjYpNsAQ.png)

* **Seller claims to be offering Mistral AI's full source code and says the company was breached again after May 2026 attack**
* **Mistral says an investigation found no evidence of new unauthorized access but has not stated whether the listed code is genuine**
* **No customer data has surfaced in analyzed samples, and nobody has shown files created after the May incident**

A seller on a cybercrime forum says French giant Mistral AI has been hacked again and is offering what they call the company's full source code for sale.

The September 16 2026 post by an account using the handle "mrwho" consists of a listing titled "Selling mistral.ai Source Code" on an English-language cybercrime forum, according to The CyberSec Guru, pricing the material in Monero only before it attempted to steer potential buyers to Session or Telegram.

Mistral AI's own team has refuted this, stating it has "found no evidence to support this claim."

## Not Mistral's first hacking-centric PR problem

Mistral's earlier hacking incident is undisputed - in May 2026, the Mini Shai-Hulud supply chain campaign, attributed to the TeamPCP group, spread from compromised TanStack packages to hundreds of npm and PyPI projects.

Mistral's own security advisory MAI-2026-002 says an automated worm led to compromised versions of its SDKs being published for a few hours on May 11 and 12, and that an affected developer device was involved. Microsoft Threat Intelligence found that a poisoned Mistral AI Python package fetched a second-stage credential stealer that allowed the attack to exploit users.

Mistral went further in statements to reporters than in its advisory. It told *BleepingComputer* that attackers had compromised a codebase management system and "contaminated some of our SDK packages for a brief period," while insisting that hosted services, managed user data, and research and testing environments were untouched. It also told*HackRead* that only certain non-core repositories were accessed.

TeamPCP, meanwhile, advertised roughly 450 repositories, about 5GB in total, for $25,000, and threatened to dump them for free if no buyer appeared within a week. One can therefore contend that this could be the same dump being remarketed by a different account, and the seller's profile is already suspect.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

*The CyberSec Guru* noted that the account joined in September 2026 and had four posts and a reputation score of 30, despite displaying a top-tier "GOD User" rank. That profile could fit a scam in the making, but as the outlet pointed out, it could also fit a broker fronting for someone else or a freshly minted alias.

*HackRead* published 24 sample repository names from TeamPCP's May post. FrenchBreaches, which examined the 339-file tree mrwho shared in September, lists several of the same names. At least four of these appear in both: mistral-inference-private, mistral-inference-internal, mistral-finetune-internal, and mistral-common-internal.

This makes it hard to tell whether the purported 'hack' is just a rehash of an existing dump from Mistral's previous breach or a second successful hacking attempt. There is a straightforward test, however: If the September archives contain commits, files, or credentials dated after May 12, or secrets that were still valid after Mistral's cleanup, the seller's claim of a second breach gains real weight. If everything predates the May incident, this is a resale, which is embarrassing for Mistral but not a new security failure.

Of course, locating the archives or examining them would involve paying the ransom in crypto, as required by what could potentially be a scam in the making- a tremendous leap of faith for an account that was created earlier this month, making this essentially a lottery ticket at best for any security researcher attempting to take a closer look.

![Google logo on a black background next to text reading &#039;Click to follow TechRadar&#039;](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg)

***Follow TechRadar on Google News***and** add us as a preferred source** * to get our expert news, reviews, and opinion in your feeds.*

![Rahim Amir](https://cdn.mos.cms.futurecdn.net/9xKZFBamtEZKSChRvywbPB.png)

Rahim Amir is a UAE-based tech writer who enjoys building PCs as much as he enjoys writing about them. He has been professionally writing about PC hardware since 2023, focusing on buyer’s guides, hardware reviews, and sponsored content and features related to tech.

Having built hundreds of gaming PCs and being an avid gamer in his spare time, Rahim tends to have stronger opinions about hardware than most. This is particularly on display when he gets his way with powerful, but minimalistic RGB builds even as Small Form Factor (SFF) PCs come a close second.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
