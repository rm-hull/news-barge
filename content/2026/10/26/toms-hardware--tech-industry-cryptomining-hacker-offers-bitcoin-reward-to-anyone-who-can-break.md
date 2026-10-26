---
title: Bitcoin reward offered to anyone who could break into an unpatched server running
  PHP, hacker cracks site and claims bounty — PHP2Shell challenge tested claims that
  AI makes exploiting vulnerabilities easy
source_url: https://www.tomshardware.com/tech-industry/cryptomining/hacker-offers-bitcoin-reward-to-anyone-who-can-break-into-an-unpatched-server-running-php-still-remains-unhacked-php2shell-challenge-tests-claims-that-ai-makes-exploiting-vulnerabilities-easy
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-26T12:56:08Z'
published: '2026-10-26T00:00:00Z'
description: A Bitcoin hacking challenge is daring security researchers to exploit
  critical PHP vulnerabilities and steal the cryptocurrency, putting claims about
  real-world exploitability to the test.
image: https://cdn.mos.cms.futurecdn.net/nR46h5GnedCeKyZtVqZr3L-1920-80.jpg
categories:
- Technology & Software
- Hardware
- Personal Finance & Investing
people:
- Bruno
- Claude AI
- Joe Grand
- KillaBoi
- Michael
- Newton Gitonga
locations: []
organisations:
- Anthropic
- BTC
- Bitcoin
- CoinCentral
- Crypto News Flash
- Get Tom's Hardware
- GitHub
- Newton Gitonga
- Notebookcheck
- PHP
- PHP2Shell
- RoboForm
---

![Bitcoin price](https://cdn.mos.cms.futurecdn.net/nR46h5GnedCeKyZtVqZr3L-1920-80.jpg)

A hacker has successfully breached a vulnerable server, claiming a prize pot worth $2,021.22 in Bitcoin after exploiting PHP2Shell vulnerabilities, a posting on the Steal My Bitcoin website has shown. The challenge's creator confirmed the win on October 25, ending an experiment designed to test claims that exploiting critical software vulnerabilities is becoming easier.

The challenge, hosted on the website a day earlier and announced through a forum post, initially offered approximately $502 worth of Bitcoin. Donations subsequently increased the pot to 0.02511679 BTC, worth $2,021.22 at the time of the win. The creator's website recorded the successful claim at 15:47 UTC on October 25, after the challenge had been running for approximately 19.28 hours.

The experiment follows the disclosure of CVE-2026-109618 and CVE-2026-109619, two critical PHP vulnerabilities that can allow remote code execution under certain conditions. The flaws received critical severity ratings, and fixes were released on October 21. Turning the vulnerabilities into a reliable attack, however, requires more than simply running a publicly available exploit against an arbitrary server.

The challenge's creator, posting under the name ‘cloudlandsdev’, had said the project was designed to see whether anyone could use the vulnerabilities to compromise the server and claim its Bitcoin. “Made this because I'm curious if anyone out there has figured out how to actually use this PHP RCE, we spent the last few days panicking. Have fun!” the creator wrote.

PHP2Shell refers to two vulnerabilities in PHP’s request-handling and memory-management processes. Under vulnerable configurations, an attacker could potentially exploit these flaws to execute code with the privileges of the web server account.

The experiment quickly attracted attention, but the resulting traffic also became a problem. In an update, the creator said visitors were exhausting the server's available computing resources shortly after each capacity increase. Limited storage also prevented the server from retaining all its logs, complicating efforts to document a successful attempt.

The winner, ‘KillaBoi’, published a proof of concept on GitHub describing the attack against the live challenge and providing a local test environment. The exploit took advantage of PHP's handling of multipart uploads and session data, where, by pushing a PHP worker beyond its memory limit, the attacker could leave internal state in an inconsistent condition. Subsequent requests then exposed memory contents through session cookies, providing information about the locations of PHP's memory structures and executable code.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Notably, the attacker used those addresses to construct a forged PHP data structure that triggered command execution during cleanup. The final request returned evidence that the command had run inside the PHP process. Although the server was successfully compromised, the recovered private key did not match the advertised prize address. However, on-chain data shows the funds were subsequently sent to an address “bc1qr4…lk7a9”, labeled as a Kraken cold wallet.

Bitcoin recovery efforts have previously involved reverse-engineering software rather than exploiting a live server. In 2024, hardware hacker Joe Grand, known as ‘Kingpin”, and researcher Bruno recovered access to 43.6 BTC belonging to an owner identified as Michael, who had forgotten a 20-character wallet password.

The researchers reverse-engineered an older version of RoboForm's password generator and identified a flaw that made the password predictable. They recovered the wallet in November 2023, when the Bitcoin was worth approximately $1.6 million. Its value had climbed to nearly $3 million by the time the recovery was reported in May 2024.

A more recent case involved a Bitcoin holder who recovered five BTC worth roughly $400,000 in May 2026 after losing access to the wallet for years. The pseudonymous owner, known as ‘cprkrn’, said Anthropic's Claude AI helped identify a backup file from December 2019, which could be decrypted using a password the owner had previously written down in a notebook. The backup contained the keys needed to access the Bitcoin.

The latest event comes as security teams face pressure to patch PHP installations following the public disclosure of PHP2Shell. A separate report on the vulnerability disclosure controversy detailed how premature publication disrupted the coordinated release process. That said, for now, evidence of the latest successful attack suggests that exploiting these PHP vulnerabilities may not be that hard after all.

![Newton Gitonga](https://cdn.mos.cms.futurecdn.net/J7W2ymR6m9nJpuFnKQwsGf-140-80.jpg)

Newton Gitonga is a tech journalist covering gadgets, PC hardware, AI, data centers, and the wider tech industry. His interest in technology started early, taking apart things around the house to see how they worked, often to his dad’s frustration. His curiosity sometimes got the better of him, including a few failed attempts to fix laptops, one of them a gifted Dell XPS. He has previously written for Notebookcheck, ZyCrypto, CoinCentral, and Crypto News Flash.
