---
title: Hackers are using 'LLMjacking attacks' to hijack company AI usage and run up
  huge cloud bills
source_url: https://www.techradar.com/pro/security/hackers-are-using-llmjacking-attacks-to-hijack-company-ai-usage-and-run-up-huge-cloud-bills
source_site: TechRadar UK
source_slug: techradar-uk
description: Businesses can run up $100,000 bills in minutes
image: https://cdn.mos.cms.futurecdn.net/4d3FzfBhbeGTkD9mnMpEdM-2560-80.jpg
published: '2026-11-03T00:00:00Z'
scraped_at: '2026-11-03T17:00:26Z'
categories:
- Technology & Software
- Business & Entrepreneurship
people: []
locations: []
organisations:
- GTIG
- GitHub Personal Access Tokens
- Google
- Google’s Threat Intelligence Group
- TechRadar Pro
- UNC6993
---

![A close up of a person&#039;s eyes and face. They are wearing glasses and in one eye there&#039;s. a reflection of a digital brain](https://cdn.mos.cms.futurecdn.net/4d3FzfBhbeGTkD9mnMpEdM-1920-80.jpg)

* **Cybercriminals are stealing AI API keys and cloud credentials to hijack expensive LLM services and infrastructure**
* **Stolen access is used to run AI workloads, create proxy services, and rack up massive bills for victims**
* **Google warns “LLMjacking” is evolving into a specialized cybercrime ecosystem with dedicated monetization operators**

Threat actors are using large language models (LLM) to support almost every stage of a cyberattack, from researching potential victims to developing malware and automating various attacks. However, using AI is not cheap, and for those eager to use frontier models, costs can stack up relatively quickly.

But cybercriminals are used to stealing things, so why not steal someone else’s tokens, too?

A new report from Google’s Threat Intelligence Group (GTIG) says that different hacking groups are doing exactly that and that the practice - known as LLMjacking - has been steadily growing more popular over the last couple of years.

Most groups start by focusing either on publicly exposed LLM endpoints, or on obtaining valid LLM application programming interface (API) keys. In many cases, the crooks would use exposed or stolen cloud identity tokens (IAM credentials, Service Account keys, GitHub Personal Access Tokens, and active session tokens) to establish an initial foothold into the target organizations’ infrastructure.

From there, they would “systematically work” to escalate privileges, solidify their access, and identify targets for further compromise.

## LLMjacking

The endgame is LLMjacking, which GTIG describes as “the monetization and resource-hijacking of foundation models, which actors achieve through token proxying, automated model streaming, and GPU hardware provisioning.” In other words, someone else is using your AI subscription while you get the bill.

The bills can cause quite the headache, too. With cryptojacking, for example, token mining is relatively slow and steady, and a certain amount of time needs to pass for the charges to really stack up. With LLMjacking, however, costs can go into six digits in six minutes.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

“Upon acquiring LLM API access keys, UNC6993 attempted to generate additional API keys and enable associated services within victim cloud projects, quickly accumulating over $100,000 in billing charges,” Google says in the report.

“Another threat actor subscribed victim accounts to Pay-As-You-Go agreements, selecting premium foundation models and launching high-volume inference streams. To bypass rate limits, the threat actor deployed a "burn and rotate" strategy, continuously creating and deleting short-lived service accounts while auditing the cloud provider’s billing interface to monitor financial impact.”

In some cases, threat actors also used the acquired access to host their own proxy endpoints and agentic workloads. Google says that one threat actor enabled agents, deployed publicly accessible reverse proxies, and used custom Node.js proxy bundles to expose endpoints compatible with multiple frontier LLMs rebranded under a persona known as D1337-KAIROS.

This actor deployed a containerized backdoor which queried an upstream LLM to reason through instructions and execute commands locally.

## A growing ecosystem

The LLMjacking ecosystem is young, but growing fast and maturing even faster. Google says that there is already a division of labor between hacking groups that establish initial access to compromised environments, and operators who manage downstream monetization infrastructure. The latter are called “LLM Mixers” and they operate as a routing gateway that proxies, aggregates, and resells unauthorized LLM access to underground subscribers.

“In one investigation, GTIG observed two distinct operational clusters coordinating to compromise and monetize enterprise LLM infrastructure, demonstrating the sophisticated specialization emerging in this space,” Google said.

By using open source API gateways and custom relay infrastructure, the attackers were able to pool stolen credentials, meter usage, and hide where the requests really originated from.

Google is now sounding the alarm, saying it expects threat actors to “increasingly prioritize” LLMjacking at the expense of other resource theft practices. It urges organizations to increase their visibility of LLM platforms, prioritize detection of modifications to LLM accounts and services, and treat any unauthorized enablement as a critical security event. It also advised organizations to enforce the principle of least privilege and make sure accounts and users only have permissions they absolutely need to get the job done.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
