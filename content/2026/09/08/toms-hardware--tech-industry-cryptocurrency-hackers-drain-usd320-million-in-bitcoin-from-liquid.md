---
title: Hackers drain $320 million in Bitcoin from Liquid Network, emptying roughly
  95% of federation wallet — attackers claim they’re the ‘good guys’ and will return
  funds after the vulnerability is fixed
source_url: https://www.tomshardware.com/tech-industry/cryptocurrency/hackers-drain-usd320-million-in-bitcoin-from-liquid-network-emptying-roughly-95-percent-of-federation-wallet-attackers-claim-theyre-the-good-guys-and-will-return-funds-after-the-vulnerability-is-fixed
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-08T12:51:06Z'
published: '2026-09-08T00:00:00Z'
description: The nature of the exploit was "unusual"
image: https://cdn.mos.cms.futurecdn.net/q9BqLa7vM7iU63EiCE6opD-2000-80.jpg
---

![Bitcoin](https://cdn.mos.cms.futurecdn.net/q9BqLa7vM7iU63EiCE6opD.jpg) 

Hackers reportedly claiming to be good actors have drained about $320 million worth of Bitcoin from Liquid Network's federation wallet, according to a CoinDesk report. In an X post on September 6, Liquid — a Bitcoin sidechain developed by blockchain infrastructure company Blockstream — confirmed that 4,000 BTC, roughly 95% of the entire wallet's balance, had been withdrawn.

Interestingly, the post referred to those behind the exploit as “purported white-hat hackers,” echoing the hackers’ own claim, after they self-identified as “whitehats” in a message embedded in a Bitcoin transaction. They also reportedly requested an audience with Liquid via the on-chain message, promising to return the money once the vulnerability that enabled the exploit is fixed.

“Please fix the bug first,” the on-chain message said. "The chain is under risk at latest commit right now. Make sure every node is patched. Then we will transfer the money back safely after confirming the fix.” Liquid responded on-chain with its security team's contact and has reportedly moved communications to an encrypted channel. Meanwhile, the platform said it has suspended transactions and warns of service disruptions as federation members work to restore service.

Launched in 2018, Liquid is a federated sidechain designed to move Bitcoin faster and more privately than the main chain. Users lock BTC on Bitcoin and receive an equivalent token, L-BTC, on Liquid, which settles blocks roughly every minute and finalizes in about two minutes. Rather than relying on miners, the network is secured by a federation of more than 80 exchanges, brokers, and other financial firms. The block signing and the multisig wallet holding the pegged-in Bitcoin are handled by 15 rotating functionaries that require 11 signatures to move funds.

The mechanics behind the exploit are also unusual, as nothing appears to have been stolen in the conventional sense. For example, in January, the Solana-based platform Step Finance lost roughly $40 million after attackers compromised devices belonging to its executive team, gaining access to the keys that guarded its treasury wallets. According to Liquid, the coins left through the Peg-out Authorization Key (PAK), belonging to SideSwap, a decentralized exchange built on the sidechain.

However, Liquid said that the key had not been compromised, nor had any others. SideSwap gave a matching account, stating a customer sent 4,000 L-BTC to its peg-out service at 14:05 UTC, the service processed the order as it would any other, and the Liquid Federation paid out 3,996 BTC to the customer's Bitcoin address twenty-three minutes later. According to SideSwap, its systems had no way of distinguishing those coins from any other L-BTC.

The incident lands in what has already been a punishing stretch for crypto infrastructure. Recently, the trading platform Drift suspended deposits and withdrawals after a suspected $270 million hack in April. In 2025, roughly $17 billion worth of Bitcoin was stolen, driven largely by impersonation schemes and AI-assisted scams.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Etiido Uko](https://cdn.mos.cms.futurecdn.net/BBrMt7jWtSo2Dc3iKoroyD.jpg) 

Etiido Uko is a news contributor for Tom's Hardware covering the latest updates in big tech and the PC industry. He is a mechanical engineer and senior technical writer with over nine years of experience in documentation and reporting. He is deeply passionate about all things engineering and technology, and is an expert in gadgets, manufacturing, robotics, automotive, and aerospace.
