---
title: Devs say Chinese AI company silently uploaded hundreds of megabytes of local
  workspace data, company apologizes — Z.AI, the firm behind the GLM models, didn’t
  ask for user consent and made 564 attempts to exfiltrate 313MB archive
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/devs-say-chinese-ai-company-silently-uploaded-hundreds-of-megabytes-of-local-workspace-data-z-ai-the-firm-behind-the-glm-models-didnt-ask-for-user-consent-and-made-564-attempts-to-exfiltrate-313mb-archive
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-21T15:03:59Z'
published: '2026-09-21T00:00:00Z'
description: Beijing-based company asserts it has now resolved this issue and plans
  to open source the ZCode codebase.
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
image: https://cdn.mos.cms.futurecdn.net/gGkxVzJScccmKJX8gKSrZA-1920-80.jpg
locations:
- China
- U.S.
people:
- Claude Code
- Feng Ruohang
- Ferstar
- Gemma
- Mark Tyson
- Tom
organisations:
- Alibaba Cloud
- Elon Musk’s xAI
- Ferstar
- GLM
- Get Tom's Hardware
- Google News
- Grok Build
- SCMP
- South China Morning Post
- Tom's Hardware
- Z.ai
- ZCode
- Zhipu AI
---

![ZCode home page](https://cdn.mos.cms.futurecdn.net/gGkxVzJScccmKJX8gKSrZA.jpg)

The second-largest AI company in China is having to work frantically to patch up its reputation, reports the South China Morning Post. Z.ai’s firefighting exercise began after a number of prominent devs raised flags about their local files and data being uploaded to online servers without their consent.

Z.ai has started to publicly address all the security and privacy concerns that have been stoked by the dev/blogger findings in recent days. On Friday, it apologized and said it had fixed the uploading of user files and data without consent. Moreover, it has been assuring users that any data uploaded to its cloud service has been destroyed. Lastly, and good for longer-term trust, Z.ai says that it is planning to open-source ZCode’s codebase and invite third-party assessors to review it.

Z.ai is also known as Zhipu AI, but you may also be familiar with it for its GLM models, which are available alongside the likes of Gemma, Qwen, Nemotron, DeepSeek, and many more on Hugging Face. Like similar companies, Z.ai offers a coding assistant, and it is this ‘ZCode’ tool that was caught silently uploading large amounts of data without permission.

The SCMP quotes two devs/bloggers who noticed what was happening and alerted their followers about the suspicious activity. One of them, known as Ferstar, reckons that ZCode compressed 313MB of their files into a directory to upload to Alibaba Cloud storage. When it was caught, it had apparently tried and failed to upload this compressed and encrypted file 564 times... A smaller 15KB file had successfully been siphoned.

Though the temporary files were squashed and encrypted, filenames were still visible. Thus, Ferstar was pretty certain the contents included a commercial project he was working on, even though he couldn’t extract the files to verify their contents. Another tech blogger known as Feng Ruohang reported a similar experience. Making matters worse, the upload mechanism within ZCode is enabled by default, with no ‘off’ option, says the source report.

There’s no indication of how long this sneaky file-uploading situation has existed. However, the SCMP also quotes an unnamed software engineer at a leading Chinese robotics company who indicates that Z.ai’s tools have been banned within the company due to security concerns.

As far as sneaky data pilfering and similar abuses, U.S. companies certainly don’t have a spotless record. Reports indicate Elon Musk’s xAI, specifically the Grok Build tool, was up to similar shenanigans earlier this year. Claude Code users have also grumbled about their data being transmitted without consent, as well as suffering from vulnerabilities that might allow hackers unauthorized access to user data.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Mark Tyson](https://cdn.mos.cms.futurecdn.net/56vqMYLDaKRHPhHZgbADFR.jpg)

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.
