---
title: OpenAI says ChatGPT Sol helped uncover critical PHP flaws that could affect
  70% of websites — AI-assisted researchers turned a two-year-old bug that stumped
  human developers into working exploits in two weeks
source_url: https://www.tomshardware.com/tech-industry/cyber-security/openai-says-gpt-5-6-sol-helped-uncover-critical-php-flaws-that-could-affect-70-percent-of-websites-ai-assisted-researchers-turned-two-year-old-bug-that-stumped-human-developers-into-working-exploits-in-two-weeks
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-22T11:47:27Z'
published: '2026-10-22T00:00:00Z'
description: OpenAI says defenders must proactively strengthen defenses before bad
  actors begin to exploit AI's extreme capabilities.
image: https://cdn.mos.cms.futurecdn.net/bqKbbbB3ZdRgDH7Pz95FKT-1920-80.jpg
categories:
- Technology & Software
- Hardware
people:
- Claude Mythos
- Ryan A
- Tom
locations:
- Calif
organisations:
- Anthropic
- Etiido Uko
- Get Tom's Hardware
- Google News
- OpenAI
- PC
- PHP Foundation
- Tom's Hardware
- Wiz
---

![OpenAI](https://cdn.mos.cms.futurecdn.net/bqKbbbB3ZdRgDH7Pz95FKT-1920-80.jpg)

OpenAI announced in a press release on Oct. 21 that researchers working under its “Patch the Planet” cybersecurity initiative used its AI model GPT-5.6 Sol to uncover critical security vulnerabilities in PHP (an open-source programming language that runs an estimated 70% of the internet). After the discovery, the company says it coordinated a coalition of researchers, PHP maintainers, security providers, and government cybersecurity agencies to fix the issues over two months. The company attributed the lengthy timeline to the task's complexity, which required major changes to the PHP engine.

![Nvidia](https://cdn.mos.cms.futurecdn.net/z53fPgXjpKHTpeGv3RHpqj-1200-80.png)

The PHP Foundation has released patched versions PHP 8.2.35, 8.3.36, 8.4.27, and 8.5.12 to fix the vulnerabilities. PHP 8.1 and older versions will not receive official fixes. The coordinated release was originally scheduled for Oct. 22, but was brought forward to Oct. 21 following premature disclosures on Oct. 20, which led to public outcry.

OpenAI says every site using PHP can now safely upgrade its version to stay secure. The company highlights the incident — which it considers one of the biggest cybersecurity discoveries of 2026, given PHP’s ubiquity — as an example of the Defender's Window concept in action. OpenAI introduced the concept after its models hacked Hugging Face; it describes a critical, narrow timeframe during which organizations can use advanced frontier AI models to find, patch, and strengthen their cybersecurity defenses before those same AI-driven attack capabilities become widely available to malicious threat actors.

Operating as part of the Patch the Planet program, researchers from Calif, a California-based cybersecurity firm and the program's founding partner, began auditing PHP with OpenAI tools on July 30, 2026, at the PHP Foundation's request. The Foundation had known about the underlying flaw since 2024 but couldn't identify an exploitation method or a fix. Calif researcher Ryan A. first identified the exploitable vulnerability on Aug. 11, followed by OpenAI researchers that same day. Subsequently, another cybersecurity firm, Wiz, independently identified an additional vulnerability.

The two vulnerabilities, tracked as CVE-2026-109618 and CVE-2026-109619, involve flaws in how PHP manages computer memory and handles errors. The first occurs when PHP runs out of allocated memory while processing a request, potentially leaving behind incomplete internal data that the engine may later mistakenly treat as valid. The second involves a related problem in which a fatal error leaves PHP pointing to memory that has already been freed, allowing subsequent requests to access or corrupt it. Under certain conditions, attackers can exploit these weaknesses remotely — without needing login credentials — to execute malicious code on affected servers, potentially taking control of websites.

Using AI, the researchers also demonstrated that the flaws could expose sensitive information stored in server memory, including passwords, authentication tokens, and API keys. Most concerning, the vulnerabilities exist in PHP's core engine, meaning websites can be affected even if their application code has no security flaws. Both vulnerabilities received a critical severity score of 9.2 out of 10.

OpenAI says human developers and security teams examined the underlying code but couldn't fully resolve the flaws, allowing them to persist for two years after discovery. Meanwhile, AI-wielding researchers demonstrated practical ways to exploit it within two weeks. Conversely, one could argue that the flaws would never have been exploitable without AI, making them effectively harmless.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

However, OpenAI is challenging this view with its Defender's Window concept. The company argues that powerful, revolutionary technology will inevitably be used by bad actors. It therefore maintains that it is a collective responsibility to act proactively to address any potential exploitable flaws. Anthropic's Claude Mythos recently identified 'thousands of zero-day vulnerabilities' in 'every major operating system and every major web browser.’



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Etiido Uko](https://cdn.mos.cms.futurecdn.net/BBrMt7jWtSo2Dc3iKoroyD-140-80.jpg)

Etiido Uko is a news contributor for Tom's Hardware covering the latest updates in big tech and the PC industry. He is a mechanical engineer and senior technical writer with over nine years of experience in documentation and reporting. He is deeply passionate about all things engineering and technology, and is an expert in gadgets, manufacturing, robotics, automotive, and aerospace.
