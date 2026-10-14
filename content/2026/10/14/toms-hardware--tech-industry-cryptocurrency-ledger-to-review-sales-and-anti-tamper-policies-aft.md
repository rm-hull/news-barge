---
title: Ledger to review sales and anti-tamper policies after $93 million hardware-wallet
  supply chain attack — rogue LTE chip implants reportedly stole users’ recovery phrases
source_url: https://www.tomshardware.com/tech-industry/cryptocurrency/ledger-to-review-sales-and-anti-tamper-policies-after-usd93-million-hardware-wallet-supply-chain-attack-rogue-lte-implants-reportedly-stole-users-recovery-phrases
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-14T11:51:24Z'
published: '2026-10-14T00:00:00Z'
description: '"Physical supply chain tampering is a risk for the whole industry"'
image: https://cdn.mos.cms.futurecdn.net/NS2wkDQAUwMHTW5V3sMuEH-986-80.jpg
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
- Personal Finance & Investing
people:
- Charles Guillemet
- Etiido Uko
- Ledger
- Pascal Gauthier
- Tom
locations:
- Ledger
- Malaysia
- Southeast Asia
organisations:
- Bloomberg
- CTO
- CryptoBilis
- Etiido Uko
- Google News
- LTE
- Ledger
- Official Store
- PC
- Tom's Hardware
---

![Booby-trapped Ledger wallet](https://cdn.mos.cms.futurecdn.net/NS2wkDQAUwMHTW5V3sMuEH-986-80.jpg)

Ledger is reviewing its sales policies and how its devices reach customers after the “Cryptobilis incident,” in which physical tampering along its supply chain led to $93 million in cryptocurrency theft from user wallets, according to a *Bloomberg* report on October 13. The crypto hardware manufacturer’s CTO, Charles Guillemet, confirmed in a social media post that it is also reviewing anti-tampering protection on its devices following the incident. He told users with tampered signers (hardware wallets) to contact Ledger support for shipping instructions to send the devices in for further examination. Guillemet also advised users who wanted to physically open their signers to check for tampering to review the company's guidelines on how to do so safely.

In a separate post, Ledger CEO Pascal Gauthier said, “Physical supply chain tampering is a risk for the whole industry. We are reviewing the controls that apply to our direct sales and to resellers, and we will share what we can,” confirming the company's plan to review its chain-of-custody and tamper detection practices. The company is inviting researchers and other vendors to collaborate in assessing these practices.

The incident that prompted the reviews was first noticed on Friday, October 9, when hundreds of otherwise secure wallets drained simultaneously across the Bitcoin, Ethereum, and Tron networks, triggering a massive alert across social media and blockchain security networks. Several victims came online to report losses and try to figure out what was happening. Early investigation revealed that almost all the affected wallets had been procured from CryptoBilis, an authorized third-party reseller covering Malaysia and Southeast Asia. Ledger ordered CryptoBilis to immediately halt all sales and shipments.

After further investigation, Ledger officially announced on October 10 that it had discovered a physical, unauthorized hardware implant equipped with a cellular/LTE module inside an affected user's device. It turns out that the attackers had manually installed the chips in brand-new devices at some point in the supply chain. When a new user is generating or verifying their 24-word recovery seed phrase on the wallet's screen during initial setup, the rogue chip records the OLED output or reads the raw hardware data lines carrying the text.

The integrated cellular chip then silently transmits the unencrypted recovery phrase over LTE networks directly to the attackers' external command servers, granting them full remote access to clone the private keys and drain the associated cryptocurrency funds. The hardware modification completely bypassed Ledger's standard automated “Genuine Check” software protocol, as it sat entirely outside the microchip running Ledger's standard firmware.

Ledger has stressed that its internal infrastructure, firmware code, and direct-to-consumer sales channels through Ledger's Official Store remain entirely uncompromised. The company has advised users with wallets from third-party resellers to transfer funds to a separate wallet secured by a freshly generated, uncompromised 24-word recovery phrase while it conducts further investigations. It is also restructuring its vendor verification and supply chain requirements, instructing distributors to enforce tighter tracking, source only through approved channels, and strictly ban the restocking or resale of returned units.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Etiido Uko](https://cdn.mos.cms.futurecdn.net/BBrMt7jWtSo2Dc3iKoroyD-140-80.jpg)

Etiido Uko is a news contributor for Tom's Hardware covering the latest updates in big tech and the PC industry. He is a mechanical engineer and senior technical writer with over nine years of experience in documentation and reporting. He is deeply passionate about all things engineering and technology, and is an expert in gadgets, manufacturing, robotics, automotive, and aerospace.
