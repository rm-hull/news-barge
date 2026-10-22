---
title: Security breach at AI aggregator exposes over 18 million files, including some
  very embarrassing chat records
source_url: https://www.techradar.com/pro/security/security-breach-at-ai-aggregator-exposes-over-18-million-files-including-some-very-embarrassing-chat-records
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-22T17:18:16Z'
published: '2026-10-22T00:00:00Z'
description: An AI aggregator kept an open database unprotected on the internet
image: https://cdn.mos.cms.futurecdn.net/2GxzxstGJJpm8aJiATXE26-2560-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Claude
locations:
- Brazil
- Hong Kong
organisations:
- 302.ai
- AI
- Cybernews
- TechRadar Pro
- Univerads Technology
- Univerads Technology Limited
---

![Two robotic faces in green and red indicating a good bot and a bad bot representing the positive and negative impacts of AI and chatbots.](https://cdn.mos.cms.futurecdn.net/2GxzxstGJJpm8aJiATXE26-1920-80.jpg)

* **Researchers found 22.7TB of exposed data from AI aggregator 302.ai, including chat logs and personal information**
* **Leaked records contained user prompts, AI responses, metadata, and sensitive corporate documents**
* **Incident highlights the risks of sharing confidential data with third-party AI platforms and services**

Security experts who were screaming “don’t share sensitive data with public AI” from the rooftops have been properly vindicated by an AI aggregator called 302.ai.

Researchers from *Cybernews* claim this company leaked terabytes of sensitive user and corporate data, including personally identifiable information (PII), confidential business documents, and a lot more.

## Every hacker's dream

An AI aggregator is a platform that brings together multiple AI models and tools in one place. Users then get to switch between them without having to visit each provider separately.

For example, an AI aggregator might let a user start with Chat-GPT and switch to Claude with a push of a button, all through a single interface and a single subscription or API.

Although there are different use cases for AI aggregators, the number one is being able to compare the responses quickly and easily.

302.ai was launched six years ago by a company called Univerads Technology Limited, based in Hong Kong.

*Cybernews* says it kept an unencrypted, non-password-protected, publicly available Azure storage bucket that contained 17.6 million files. The entire archive was 22.72TB heavy, most of which went on image files (almost 9TB). Video took up 7.7TB, while audio took up 5.6TB. The rest - around 500GB, were user chat logs.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Totaling more than 144,000, these logs were stored in .json files and exposed plenty of personal information, including user prompts, replies from the AI bot, which model was used, how much it cost in tokens, timestamps, and other metadata. Users also seem to have provided plenty of data themselves, including their names, birth dates, genders, postal addresses, and other contact information.

Some of the information leaked this way was quite embarrassing, too. “What we found was that some companies used the service for enterprise tasks. For example, we found multiple chat logs from a customer support chatbot owned by a prominent sex doll manufacturer,” the team wrote.

This kind of private, even intimate, data is a goldmine for cybercriminals. They can use it to create highly customized and personalized phishing emails, knowing exactly which company to impersonate, what kind of context to mention, and how to phrase the lure email, to get the victim to react. That reaction usually ends up in business email compromise, wire fraud, or ransomware infections.

## Database gets locked down

*Cybernews*’ researchers reached out to Univerads Technology, but did not hear back. In the meantime, the company locked down the database and it is no longer leaking sensitive files.

However, key questions remain unanswered: Does Univerads maintain this database, or was the job outsourced to a third party? When did the company first start collecting this data? How long did the archive stay unprotected? *Cybernews* found it in early August 2026, and saw it locked down a month later. Did anyone else find it before the*Cybernews* team did? Are there any indications that the files were copied or viewed by a third party? Is there any evidence of misuse or data spilling into the dark web?

It is highly unlikely these questions will be answered. Given the company’s prompt response and the closure of the database, it’s safe to assume that there was no ill intention, and that the leak is purely unintentional.

Accidental data spills such as this one are, unfortunately, very common. Many organizations either don’t know, or simply forget, that it is their responsibility to secure the data they generate and store in the cloud. As a result, new reports of large leaks emerge almost every week, some of which affect entire populations of certain countries, such as Brazil.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
