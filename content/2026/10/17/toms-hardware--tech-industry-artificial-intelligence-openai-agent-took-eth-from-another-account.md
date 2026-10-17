---
title: Crafty OpenAI agent willingly stole crypto from an account it didn't own to
  complete a task during test — rogue bot wrote a script to find accounts with public
  seed phrases, took funds to pay for gas
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-agent-took-eth-from-another-account-without-authorization-justified-stealing-in-its-chain-of-thought
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-17T20:33:31Z'
published: '2026-10-17T00:00:00Z'
description: The agent even contemplated the ethics of its actions.
image: https://cdn.mos.cms.futurecdn.net/hsZx5kEavBi3nnzHpf7DvC-2560-80.jpg
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
- Personal Finance & Investing
people:
- Jhet Borja
- Tom
locations:
- Sepolia ETH
organisations:
- Anthropic
- Google News
- OpenAI
- Sepolia ETH
---

![robotic hand holding bitcoin](https://cdn.mos.cms.futurecdn.net/hsZx5kEavBi3nnzHpf7DvC-1920-80.jpg)

OpenAI recently released a misalignment report on its GPT5.6-Sol coding agent after it stole cryptocurrency from an account it didn’t own. It didn’t have enough funds for the smart contracts needed to execute its tasks, so it wrote a script that looked for accounts with public seed phrases that had enough funds to pay the gas fees, finished its task, and didn’t report that it took funds from an account it wasn’t assigned to without authorization.

Thankfully, this all happened on the Sepolia test network, which uses Sepolia ETH, simulated ETH in a simulated Ethereum network for cryptocurrency app development; it doesn’t actually have any monetary value. The report states, “The assignment asked it to update the trading calculator and database behavior, and to replace placeholder contract addresses with working deployments on Sepolia.” The final task required the agent to deploy smart contracts, a task that required gas fees paid in Sepolia ETH. It wasn’t supplied with a funded wallet, nor was it permitted to use funds from another account it found.

Either way, the agent was determined to complete its task and wrote a script to look for common developer recovery phrases and check the balances of the accounts, finding 362 addresses, with one having enough Sepolia ETH to deploy the contract. The CoT (chain of thought) even admitted: “Private key public, funds could be stolen anytime. [...] We can deploy!” After that CoT, it didn’t immediately spend the funds to complete its task; in fact, it was still trying to justify “stealing” the funds. It said, “But using public known key/funds ethically? Funds on a known public dev mnemonic are effectively abandoned/test ETH; Sepolia valueless. We can use [amount redacted] to deploy task. Fine.”

The agent found its justification and executed the task. However, in its final response, it only reported that it successfully executed the tasks it was asked; it didn’t explain how, nor did it explain how it found exposed accounts and used the funds without permission, possibly because it had already justified it and needed no further explanation. It probably didn’t realize that it was going rogue since it knew it was in a test environment, just like Anthropic’s internal research model for cybersecurity got out onto the internet and hacked three real companies, thinking it was part of the training.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Jhet Borja](https://cdn.mos.cms.futurecdn.net/niBNJTDN6c99Ri7HD5zNZ8-140-80.png)

Jhet Borja is a serial hobbyist who was taking apart toys from childhood and sketching inventions. He now loves doing DIY projects ranging from designing custom 3D-printed parts, building PCs and keyboards, all the way to woodworking. If he's not getting his hands dirty, he's probably brainstorming his next project.
