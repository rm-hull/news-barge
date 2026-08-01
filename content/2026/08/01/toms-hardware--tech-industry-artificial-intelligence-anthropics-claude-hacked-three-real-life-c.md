---
title: Anthropic's Claude hacked three real-life companies during security capabilities
  test — test environment with internet access and unwitting targets' lax cybersecurity
  practices led to bots running rampant
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-claude-hacked-three-real-life-companies-during-security-capabilities-test-test-environment-with-internet-access-and-unwitting-targets-lax-cybersecurity-practices-led-to-bots-running-rampant
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-01T13:48:40Z'
published: '2026-08-01T00:00:00Z'
description: Impressive hacking skills on display, but the incidents illustrate a
  lack of 101-level cybersecurity practices
image: https://cdn.mos.cms.futurecdn.net/XuGPNAabZgP3ChkaveBMUn-2291-80.jpg
---

![Bot opening lock](https://cdn.mos.cms.futurecdn.net/XuGPNAabZgP3ChkaveBMUn.jpg) 

Whether driven by a desire for transparency or to keep __OpenAI from hogging the spotlight__ when it comes to advertising advanced AI models, __Anthropic revealed__ that Claude also hacked into three production systems belonging to unsuspecting targets during cybersecurity capabilities testing. Two of the affected companies didn't know they had been hacked, while a third one is unreachable.

 ![Microsoft data center in Mount Pleasant, Wisconsin](https://cdn.mos.cms.futurecdn.net/Vh4nY3pMCcmra2ymXah9S7.jpg) 


The alleged incidents reportedly happened during the previous quarter and involved several versions of Claude: Opus 4.7, Mythos 5, and "an internal research test model." Similar to what happened when OpenAI Sol hacked into Hugging Face, Anthropic was running Claude through cybersecurity capture-the-flag scenarios where the bot was told to find a piece of information somewhere in its network. Anthropic says there were 141,006 test runs, and the three incidents occurred over six problematic runs. As expected, the tests ran with most AI safeguards disabled.

The problem is, the network was not isolated, a newbie mistake that some might even find suspicious. This was due to an alleged "miscommunication" between Anthropic’s virtual __test lab firm Irregular__, which gave the bots full access to the internet. For safety's sake, the Claudes were apparently told they were in an isolated environment, which didn't help much.

The first time, Claude Opus 4.7 had to find a piece of data belonging to an imaginary company. As it turns out, there was actually a real company whose website domain matched the fake one. With internet access, it gained application and infrastructure credentials and grabbed "several hundred rows" of data from a production database.

For two out of four runs where hacking took place, Claude didn't see any problem and "rationalized that the real company must be part of the exercise," but soldiered on. The other two times, it just kept going. Anthropic notes this was the only case of the three where the bot continued to operate after the realization the company actually existed for the aforementioned reason. However, the firm's interpretation is open to discussion.

The second, and potentially more interesting, was a *bona fide* supply-chain attack, this time perpetrated by Mythos. The fake data available to the bot included an installation script for a hypothetical developer that included installing Python packages. Much like a human would, Claude noticed the obvious attack vector and, once again, due to having internet access, inferred that publishing a booby-trapped package in the PyPI repository would do the trick. Unfortunately, it was the real one that the whole world uses.

In speedrun form for brevity: Claude needed a PyPI account, meaning it needed an email and a phone number. It tried buying one but found itself short of both pockets and funds; but it found another free email provider without that requirement, registered the PyPI account, and uploaded a malware package to PyPI. The package was seemingly only up for one hour but was downloaded and run on 15 systems.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

In a twist of irony, one such system belonged to a security vendor that scans PyPI for malware, and lo and behold, promptly failed to find Claude's booby-trap and ran it. Once Claude presumably had remote code execution privileges, it used the credentials it found for further infiltration. The amusing bit is that Claude had no idea this company existed and didn't target it; the downloads just happened because the package was up and live for a short while.

According to Anthropic, the bot did detect it was acting on the real internet and even said that publishing a package like this was "NOT okay." However, it talked itself into believing it was in a test environment as it didn't recognize the real SSL certificates for the connections. It even believed the 2026 calendar date on the systems "proved" the environment was staged. It even recognized the systems that installed the malware as part of the experiment.

As for the third incident, Anthropic isn't saying much, other than Claude scanned 9,000 real live potential alternative targets once it noticed the intended one wasn't reachable. One of them reportedly had a live page with debugging information and was vulnerable to plain ol' SQL injection. Interestingly, this time around, once Claude noticed that the servers it was accessing resided on a cloud environment and not on the local network, it stopped the attack.

For its part, Anthropic recognizes that despite Claude following the instructions for the objectives, the fact that it stopped by itself once it found the target was real in only one of the cases is food for some thought. The firm says it's talking to METR for a third-party review, and it needs to "better co-design evaluation environments."

Oddly enough, Anthropic believes Claude probably wouldn't have gone online "if the prompt had clearly explained which systems were in and out of scope for the evaluation," while also stating the incidents were "closer to a harness and operational failure than a model alignment failure."

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.
