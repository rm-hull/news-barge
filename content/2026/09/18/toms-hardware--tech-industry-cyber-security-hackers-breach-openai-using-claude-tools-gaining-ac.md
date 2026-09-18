---
title: Hackers breach OpenAI using Claude tools, gaining access to employee accounts
  and the company's internal codebase — attackers initiated a 'harmless' pull request
  as proof of the hack
source_url: https://www.tomshardware.com/tech-industry/cyber-security/hackers-breach-openai-using-claude-tools-gaining-access-to-employee-accounts-and-the-companys-internal-codebase-initiating-a-harmless-pull-request-as-proof-of-the-hack
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-18T19:00:37Z'
published: '2026-09-18T00:00:00Z'
description: Researchers receive a $6,500 bounty after reporting the vulnerabilities
image: https://cdn.mos.cms.futurecdn.net/YUDxAZxxyWFMPWzwJRmWvH-2560-80.jpg
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
---

![generic hack screen](https://cdn.mos.cms.futurecdn.net/YUDxAZxxyWFMPWzwJRmWvH.jpg) 

A team of white-hat hackers from cybersecurity startup Hackron AI has successfully hacked OpenAI using Claude tools. In an X post on September 18, the team claimed they breached OpenAI's internal codebase on July 25 and gained access to the ChatGPT and Codex accounts of some OpenAI employees. They established proof of the hack via a pull request to OpenAI's private repository before reporting the vulnerabilities to OpenAI. The company reportedly fixed the issue within 14 hours of the report and paid the researchers a $6,500 bounty.

On July 25, our team hacked OpenAI. It took us less than 72 hours.Two vulnerabilities chained together gave us access to ChatGPT and Codex accounts belonging to OpenAI employees. We demonstrated the impact with a harmless PR in OpenAI’s internal monorepo.The full chain:…September 18, 2026


Operating as hackers under OpenAI’s bug bounty program, Hacktron researchers uncovered critical vulnerabilities that granted them access to internal employee tools and the ability to compromise private software repositories. The researchers exploited a single sign-on (SSO) misconfiguration and a Remote Code Execution (RCE) flaw in Discourse, a third-party platform that powers OpenAI’s community discussion forum. The chain of attack was as follows: HEIF upload → libheif heap overflow → RCE → OpenAI SSO flaw → ChatGPT/Codex takeover → connected GitHub → internal PR.

First, the researchers uploaded a malicious HEIF (High Efficiency Image File) image to the forum as a profile picture. When Discourse’s server-side software tried to process the image using an outdated libheif package, it triggered a heap overflow memory vulnerability, causing the library to crash and mismanage internal system memory. The researchers carefully orchestrated the memory crash to achieve remote code execution. After gaining access to the forum's local server environment, the researchers intercepted the server’s environmental configurations and session handling, discovering an SSO flaw in which the forum's authentication system did not adequately validate or isolate user sessions from other OpenAI services.

Armed with session tokens hijacked from the local forum server database, the hackers exploited the SSO flaw to impersonate a real OpenAI employee, allowing them to bypass traditional login screens and infiltrate a highly privileged internal account linked to OpenAI's development teams. As many tech companies unify authentication across corporate apps, the hijacked employee account was directly linked to OpenAI’s corporate enterprise systems, including GitHub, Slack, and email accounts. The researchers were able to access OpenAI’s massive private codebase, where they initiated an internal Pull Request as definitive proof of the exploit.

Similar to an incident last month in which China-linked hackers used AI to carry out the first-ever end-to-end autonomous cyberattack on Taiwan's government, the Hacktron hack also used artificial intelligence. The researchers constructed the exploit pipeline using Anthropic's Claude Opus 5 model, after attempts with Opus 4.8 failed. After they found the unpatched libheif library on OpenAI's forum, they fed the raw server data into the model, asking it to write an exploit for the bug.

The model analyzed the memory structure and successfully calculated how to trigger the heap buffer overflow. It generated the precise, weaponized code required to create the malicious HEIF image. The human hackers uploaded it to the forum — triggering the Remote Code Execution — then manually executed the rest of the “attack.” An important clarification is that they used an authorized, cybersecurity-configured version of Claude, which relaxes certain cyber restrictions for authorized researchers.

After gaining access, the researchers say they immediately halted testing and reported the vulnerabilities to OpenAI and Discourse — both of which have fixed their sides of the issue — without studying or downloading OpenAI's source code. From the initial finding to full resolution took 72 hours, after which OpenAI rewarded the researchers with a $6,500 bounty. The incident further highlights ongoing concerns over the risk of AI-powered cyberattacks. Recently, rogue OpenAI agents autonomously breached HuggingFace. US frontier AI companies are now warning against sophisticated distillation attacks.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Etiido Uko](https://cdn.mos.cms.futurecdn.net/BBrMt7jWtSo2Dc3iKoroyD.jpg) 

Etiido Uko is a news contributor for Tom's Hardware covering the latest updates in big tech and the PC industry. He is a mechanical engineer and senior technical writer with over nine years of experience in documentation and reporting. He is deeply passionate about all things engineering and technology, and is an expert in gadgets, manufacturing, robotics, automotive, and aerospace.
