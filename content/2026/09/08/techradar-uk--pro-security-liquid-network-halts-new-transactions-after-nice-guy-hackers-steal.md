---
title: Liquid Network halts new transactions after 'nice guy' hackers steal nearly
  all its Bitcoin — but then return most of it after a patch is issued
source_url: https://www.techradar.com/pro/security/liquid-network-halts-new-transactions-after-nice-guy-hackers-steal-nearly-all-its-bitcoin-but-then-return-most-of-it-after-a-patch-is-issued
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-08T19:26:04Z'
published: '2026-09-08T00:00:00Z'
description: Liquid Network is still disrupted, but users can breathe a sigh of relief
image: https://cdn.mos.cms.futurecdn.net/UweTPZX99rMmYJQoBvPT44-2560-80.jpg
---

![Bitcoin](https://cdn.mos.cms.futurecdn.net/UweTPZX99rMmYJQoBvPT44.jpg) 

- **Liquid Network hack exploited a bug in SideSwap, releasing 3,998 BTC (~$313M) to attackers**
- **Hackers claimed “white‑hat” intent, returning 3,400 BTC after fixes, leaving 598 BTC missing**
- **Network remains paused as Blockstream and Federation patch vulnerabilities and prepare safe restart**

The latest twist in the Liquid Network Bitcoin hack is worthy of a short movie, if not a full-length feature film.

Apparently, the hackers are actually the good guys, who stole the money to “keep it safe” until a vulnerability in the protocol had been fully resolved. They promised to return the funds afterwards.

## What is Liquid Network?

Liquid Network was designed to solve a specific problem on the Bitcoin blockchain - being rather slow. The transactions on the network are recorded in a “block”, which is added to the chain roughly once every 10 minutes. Also, each block can only hold a limited number of transactions, which means the network can handle a smaller number of transactions per second, compared to conventional payment systems. Transactions that don’t make it into a specific block then need to wait for the next one, thus extending the confirmation time.

To solve that problem, Liquid Network was built. It runs its own Bitcoin reserve and its own blockchain, also known as a “sidechain”. When a person wants to use Liquid Network to send money quickly, they first convert their Bitcoin into Liquid Bitcoin, or L-BTC. They can then send it to another person much faster than a regular Bitcoin transaction. The recipient can keep the money on Liquid or convert it back to regular Bitcoin and move it to the Bitcoin network.

This way, Liquid provides a faster network without requiring every transaction to happen directly on the Bitcoin blockchain.

Besides speeding up Bitcoin transactions, Liquid Network also allows users (companies and other entities) to create and trade other digital assets, including tokenized securities, or stablecoins.

The project was built by Blockstream, a Bitcoin-focused technology company founded in 2014. It is run by the Liquid Federation, a group of more than 80 member companies, including exchanges, infrastructure companies, and financial institutions. A smaller group of members (15 to be exact) operate the network’s “functionaries” (servers that keep the network running), while the wider group has a governance role. Members vote on three boards (Technology, Membership, Oversight), handling ideas such as technical direction, internal rules, memberships, and more.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## What happened to it?

In early September 2026, still unidentified actors managed to generate around 4,000 L-BTC, without putting in the corresponding 4,000 BTC into Liquid. As soon as they did it, they sent the L-BTC through SideSwap, a legitimate service that is used to convert L-BTC back to Bitcoin and vice-versa. The system apparently regarded the withdrawal as legitimate because, as was later determined, a bug prevented SideSwap from distinguishing between “real” and “fake” L-BTC, and treated them all the same.

As a result, the Liquid Federation ended up releasing 3,998 real BTC (more than $313 million at press time) to the attackers. As soon as the operators realized what had happened, they halted new transactions and warned about possible disruptions until the service was restored.

Then came the movie twist: the hacker started communicating with network maintainers through on-chain Bitcoin transactions, promising to return the funds when the vulnerability is fully resolved:

“Please fix the bug first. The chain is under risk at latest commit right now. Make sure every node is patched. Then we will transfer the money back safely after confirming the fix,” one of the messages read.

Earlier today, Coindesk reported that the hackers partially kept their promise, returning 3,400 of the 4,000 BTC drained, which suggests that the flaw was remedied. The remaining 598 BTC, worth approximately $47 million, is currently unaccounted for.

“3,400 BTC of the roughly 4,000 BTC withdrawn on September 6 has been returned to the Liquid Federation wallet. The return followed confirmation from Blockstream that the affected bridge nodes have been patched,” wrote Samson Mow, former chief strategy officer at Blockstream, on X. “Approximately 598 BTC remains outstanding, and Blockstream continues to engage with the white-hat hackers.”

He added that the network remains paused while Blockstream and Federation members make additional fixes and security improvements, resolve the chain split, and prepare for a safe restart.

“Liquid wallets and services will continue to be affected during this time. No user action is needed, and please do not send Bitcoin to Liquid peg-in addresses until we confirm the network has restarted,” he added.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
