---
title: Hacker turns 25 cents into 46 billion fake Bitcoins to steal $770,000 — Symbiosis
  DeFi exchange bit by lack of basic bounds checking in smart contract
source_url: https://www.tomshardware.com/tech-industry/cryptocurrency/hacker-turns-25-cents-into-46-billion-fake-bitcoins-to-steal-usd770-000-symbiosis-defi-exchange-bit-by-lack-of-basic-bounds-checking-in-smart-contract
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-18T12:59:35Z'
published: '2026-09-18T00:00:00Z'
description: I, too, would love for my bank to charge me negative fees.
image: https://cdn.mos.cms.futurecdn.net/gHmhFGMn3m34gQvLf5YwE5-2048-80.jpg
categories:
- Technology & Software
- Hardware
- Personal Finance & Investing
---

![Bitcoin drop](https://cdn.mos.cms.futurecdn.net/gHmhFGMn3m34gQvLf5YwE5.jpg) 

Symbiosis is one of the many useful DeFi networks that let users trade across almost any crypto pair without having to talk to an exchange. It's been operating for five years, and links some 50-odd chains together. The ecosystem's reliance purely on smart contracts (code that's hosted on the blockchain, visible to anyone) is fully logical but paradoxically creates an accountability problem. This was demonstrated on September 11, when Symbiosis got hacked to the tune of at least $770,000, or 9.97 BTC.

Smart contracts are published on the blockchains themselves and are open-source by definition. This means anyone can find a bug, and Symbiosis' thief found two: an undisclosed privilege escalation exploit that let them fake network administrator privileges, plus a Coding-101 failure of not checking if a transaction fee was a positive number.

The method was simple: being an admin, the thief set the transaction fee to a negative value, then issued 12 transactions. With the transaction fee now negative, instead of deducting from the moved amount, it added to it. The thief only spent 330 satoshi (the smallest unit of BTC), about 25 cents, but he managed to issue 46 billion syBTC — BTC wrapped in Symbiosis' network. For reference, the maximum theoretical amount of BTC in circulation is 21 million.

These syBTC tokens meant nothing by themselves as they weren't backed, but they were tradable. And trade the thief did, selling syBTC against matching wrapped pairs including BTCB, cbBTC, WBTC, and RBTC, draining those pools, and causing $770,000 worth of BTC in damage. It's known that they only converted about $336,000 into cash via Uniswap before being cut off.

The rest of the wrapped BTC tokens were flagged by security firms and exchanges, making it difficult for the thief to use. That's of little comfort for the victims, though, until such time as the thief returns the tokens by themselves or by law. Some of them, like Coinbase's cbBTC, are issued by centralized entities and can be nullified and re-minted after a legal process, but others like RBTC cannot.

For the uninitiated, DeFi (decentralized finance) pools can be broadly described as automated trading pots. They run on existing blockchain networks like Ethereum or Solana, via smart contracts, and let users trade directly against the money in the pool, with no third party in between. Depositors providing liquidity to the pool get a cut of transaction fees whenever other users trade for it.

Example: lock 1 ETH, and you get a small amount whenever someone buys or sells ETH, effectively netting you "interest" on held currency with next to zero effort. The trader didn't have to interact with anyone: just with a piece of code, the smart contract. To make the transactions work, DeFi networks "wrap" other tokens in their own variations, like BTC turning into syBTC.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Symbiosis says it intends to repay the incurred debts, stating that "a portion will be returned from the evacuated funds, and each LP will be offered an individual compensation plan." In practice, this ultimately means that Symbiosis is going to talk to the big wrapped-BTC holders in its pool and offer them an IOU, interest-bearing debt package, or some variation/combination thereof. In these situations, it's somewhat expected, but not guaranteed, that big holders take the deal, as forcing liquidation would end the network entirely and net them pennies on the virtual dollar.

The project also said it's going to rewrite the Bitcoin-side logic and has requested an independent audit before implementing the new code. Likewise, it claims it requested a full audit of the "entire system." Symbiosis also says that "capable AI models have lowered the cost of finding bugs like this," a perfectly valid argument — and yet one that isn't likely to find much purchase given the code's high-risk nature involving money, plus the base fact that someone missed a basic negative-value check in only what's likely only a few thousands lines of code total.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png) 

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.
