---
title: Lenovo's 'encrypted' fingerprint USB drive is just an unencrypted SD card in
  a fancy case — AI-assisted follow-up finds a backdoor and hardcoded keys in other
  ‘secure’ USB products
source_url: https://www.tomshardware.com/tech-industry/cyber-security/lenovo-fingerprint-usb-stick-sold-as-aes-256-encrypted-had-a-plain-sd-card-inside-ai-assisted-follow-up-finds-a-backdoor-and-hardcoded-keys-in-other-secure-usb-products
source_site: Tom's Hardware
source_slug: toms-hardware
description: The fingerprint only switched the USB connection on; nothing on the card
  was encrypted.
image: https://cdn.mos.cms.futurecdn.net/m5tLgsKmfPcc5fZ3Ygd8Wc-1200-80.jpg
published: '2026-11-01T00:00:00Z'
scraped_at: '2026-11-01T13:14:27Z'
categories:
- Technology & Software
- Hardware
people:
- KakaSoft
- SecZure
- Shane Downing
- Tom
- Xusheng Li
- YutianDun
locations:
- China
- Mount Pleasant
- Wisconsin
organisations:
- AI
- Codex
- Get Tom's Hardware
- Google News
- HackingPassion
- KakaSoft
- Lenovo ThinkPlus
- Microsoft
- Netac
- Shane Downing
- Tom’s Hardware
- USB Copy Protection
---

![Circuit board from a Lenovo ThinkPlus fingerprint USB stick, with a microSD card in a socket beside the USB-C plug.](https://cdn.mos.cms.futurecdn.net/m5tLgsKmfPcc5fZ3Ygd8Wc-1200-80.jpg)

Security researcher Xusheng Li found that a Lenovo ThinkPlus FU100 fingerprint USB stick, sold as an AES-256-encrypted device for data security, ended up being just a plain SD card internally, HackingPassion reports. The fingerprint reader only enabled the USB connection, and nothing on the card was actually encrypted. An AI-assisted follow-up last week discovered what Li calls backdoor accounts on another maker’s drive, as well as hardcoded keys in other supposedly secure USB storage products.

![Microsoft data center in Mount Pleasant, Wisconsin](https://cdn.mos.cms.futurecdn.net/Vh4nY3pMCcmra2ymXah9S7-1200-80.jpg)

The FU100 is “just an SD card in a fancy case,” Li said in a March conference talk. It is, as a result, trivial for anyone with physical access to get to the drive’s data. One of his takeaways: “‘Hardware security’ can be pure marketing.” This isn’t the first time drive makers’ own encryption has failed, and it won’t be the last.

The original ThinkPlus FU100 analysis happened last year, with an interim fix using epoxy over the card. A later fix by Lenovo, put out early this year for the FU100, FU200 and TU800 drives, as well as the TSD303 SSD, requires owners to call a China service line, then either send devices back for replacement or get an on-site firmware upgrade. Lenovo advises backing up data first and strongly recommends wiping the drive before sending it in, which is quite an inconvenience. Lenovo rated the advisory’s severity as high, and one of its three CVEs covers the configuration software, which could let a local, logged-in user bypass device authentication and enroll an untrusted fingerprint.

The same research also turned up a different flaw in Lenovo’s TSD303 external SSD. Its data actually was encrypted, but the drive sent the correct password back over USB in plain text for the software to compare, making it easy to capture. The first fix came three months after the initial report, using block cipher encryption with a key derived from a timestamp-like value. Lenovo’s software could derive that key, and the first software fix is vulnerable if taken apart, making it not useful for protecting data if a device is stolen. A later fix, late last year, has the drive check the typed password itself, so the correct one never leaves the drive.

The same software development kit used for the drive covered nine other devices from multiple vendors, most of which could also reveal passwords to a savvy actor. In addition, two left data unencrypted on a microSD card. The full list of vendors was blacked out on Li’s slides.

AI agent use for driving reverse-engineering tools continues to increase. AI has also been exposing more security flaws recently. Li used OpenAI’s Codex, an AI programming-centric tool, with his employer’s reverse-engineering tool against other vendors’ protection schemes. Netac’s tool took about seven minutes to break, as Codex found a fixed key built into the program, along with the user’s password written to diagnostic logs.

Copy protection differs from direct access, as the intent is to allow the recipient to view files, just not make copies of them. KakaSoft’s USB Copy Protection has an internal password the program builds itself, which Codex rebuilt to decrypt a test file without the user’s password in around 26 minutes. Nexcopy’s Copy Secure took about 10 minutes, with its key unlocked by a certificate built into the viewer app. Separately, SecZure’s YutianDun has two hidden “backdoor” accounts with simple passwords, discovered with time-travel debugging, stepping through a timeline trace. However, Li’s comments suggest that malicious intent cannot be assumed.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Li gave no warning to KakaSoft, Nexcopy, or SecZure, arguing that a drive already in an attacker’s hands can’t easily be recalled or updated. He said that “client-side validation is never secure” and you should always verify security claims on your own. Netac had no patch as of Li’s March talk. An example of things done right would be an open-source USB stick that does encryption properly, even though it is built on a microSD card, deriving its key from the user’s password, so reading the card alone gets an attacker nothing.



Follow Tom’s Hardware on Google News, or add us as a preferred source, to get our latest news, analysis, & reviews in your feeds.

![Shane Downing](https://cdn.mos.cms.futurecdn.net/Zosi9VrDytS9FkgJiHvc69-140-80.png)

Shane Downing is a Contributing Writer for Tom’s Hardware, covering consumer storage, PC hardware, and AI.
