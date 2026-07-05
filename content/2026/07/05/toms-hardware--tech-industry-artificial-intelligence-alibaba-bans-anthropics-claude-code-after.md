---
title: Alibaba bans Anthropic's Claude Code after an alleged hidden China-detection
  backdoor is uncovered — employees told to switch to Qoder as the rift between the
  firms widens
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/alibaba-bans-anthropics-claude-code-after-an-alleged-hidden-china-detection-backdoor-is-uncovered-employees-told-to-switch-to-qoder-as-the-rift-between-the-firms-widens
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-05T14:02:09Z'
published: '2026-07-05T00:00:00Z'
description: Ban lands three weeks after Anthropic accused Alibaba's Qwen lab of running
  the largest known distillation attack on Claude.
image: https://cdn.mos.cms.futurecdn.net/LyXhaFLnFmGeSh8PqYKPuh-1920-80.jpg
---

![Alibaba HQ](https://cdn.mos.cms.futurecdn.net/LyXhaFLnFmGeSh8PqYKPuh.jpg) 

Chinese tech giant Alibaba has banned its employees from using Anthropic's Claude Code for all work purposes, effective July 10, after security researchers alleged the AI coding agent contained hidden code designed to detect whether users were based in China or affiliated with Chinese AI labs. According to a July 3 South China Morning Post report, the Chinese tech giant said Claude Code had been "added to a list of high-risk software with security vulnerabilities" following a comprehensive evaluation, citing what it described as back-door risks.

Employees have reportedly been instructed to adopt Qoder, Alibaba's in-house AI coding platform, as the replacement. According to reports from Chinese outlets citing company insiders, the directive reportedly goes further than Claude Code itself, as staff have allegedly been told to uninstall all Anthropic products, including the Sonnet, Opus, and Fable model families. The move is the latest escalation in a feud that ignited last month, when Anthropic accused operators linked to Alibaba's Qwen AI lab of running the largest known model distillation attack against Claude.

The trigger for the ban was a June 30 post on the r/ClaudeAI subreddit by a user who claimed to have reverse-engineered Claude Code while restoring a disabled remote-control feature. According to the write-up, obfuscated detection logic had shipped silently since version 2.1.91, released on April 2, with no mention in the release notes. Whenever a proxy was detected, the code reportedly checked whether the system timezone matched Asia/Shanghai or Asia/Urumqi and inspected the proxy URL against a hardcoded list of Chinese domains and AI lab identifiers, reportedly including Alibaba, Baidu, Ant Group, and ByteDance.

What elevated the discovery from routine telemetry to scandal was the exfiltration method. Rather than sending an overt signal, the tool allegedly encoded its findings steganographically, tweaking the date format and swapping a punctuation character in the system prompt sent back to Anthropic's servers — invisible to the user, but machine-parseable on Anthropic's end. The Reddit author called the covert transmission of system and proxy data "a fundamental violation of user trust," saying they simply wanted transparency from Anthropic.

Anthropic has not issued a formal statement, but Thariq Shihipar, an engineer on the Claude Code team, addressed the findings on X, describing the mechanism as "an experiment we launched in March" intended to prevent account abuse by unauthorized resellers and to protect against distillation. Shihipar said the team had been meaning to remove the code for a while, and that the pull request stripping it out was merged on July 1, the day after the Reddit post.

The timing of Alibaba’s Claude ban fits right into the wider rift between the Chinese tech giant and the U.S. artificial intelligence frontrunner. On June 10, Anthropic sent a letter to leaders of the U.S. Senate Banking Committee accusing operators affiliated with Alibaba's Qwen lab of using nearly 25,000 fraudulent accounts to generate 28.8 million exchanges with Claude between April 22 and June 5, in what it characterized as an industrial-scale attempt to distill the model's software engineering and reasoning capabilities. Distillation, training a smaller model on the outputs of a more capable one, sits in a legal and ethical gray zone that the industry has yet to resolve. Alibaba has denied wrongdoing and has not addressed the allegations in detail.

Anthropic followed the Senate letter with sweeping account restrictions, reportedly cutting off numerous Chinese users without notice. The company already maintains the industry's hardest line on access to China, stating it is the only frontier AI firm that restricts service to Chinese-owned entities, even through subsidiaries incorporated abroad. This stance is precisely why Chinese developers reach Claude Code through proxies in the first place, and why a proxy-triggered detection routine reads, to Chinese eyes, as a tool built to hunt them specifically.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

The episode slots into a U.S.-China AI relationship that has spent 2026 swinging in both directions at once. Washington had earlier placed export restrictions on AI chips to China. It loosened hardware controls this year, clearing roughly 10 Chinese firms, including Alibaba, to buy H200S in quantities of up to 75,000 units per customer. However, Beijing simultaneously discouraged Chinese firms from buying approved American silicon, citing its own security concerns, as part of a deliberate push toward an indigenous AI stack.

Software access now appears to be following a similar trajectory of restrictions. Anthropic is blocking China at the account level; now, China's largest tech company has banned Anthropic at the workplace level. Earlier, OpenAI banned numerous China-linked accounts accused of artificially amplifying backlash against U.S. data center electricity prices.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Etiido Uko](https://cdn.mos.cms.futurecdn.net/BBrMt7jWtSo2Dc3iKoroyD.jpg)

Etiido Uko is a news contributor for Tom's Hardware covering the latest updates in big tech and the PC industry. He is a mechanical engineer and senior technical writer with over nine years of experience in documentation and reporting. He is deeply passionate about all things engineering and technology, and is an expert in gadgets, manufacturing, robotics, automotive, and aerospace.
