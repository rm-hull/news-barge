---
title: '''Some agents exhibited unintended web-browsing behavior'': Tencent admits
  AI agents it was testing made more than 2,600 attempts in 11 days to slip past Alibaba''s
  map defenses, just to find out which zoo gate people use'
source_url: https://www.techradar.com/pro/some-agents-exhibited-unintended-web-browsing-behavior-tencent-admits-ai-agents-it-was-testing-made-more-than-2-600-attempts-in-11-days-to-slip-past-alibabas-map-defenses-just-to-find-out-which-zoo-gate-people-use
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-20T23:50:13Z'
published: '2026-10-20T00:00:00Z'
description: Researchers hid a message for a live fleet of rogue AI agents, and the
  agents wrote back
image: https://cdn.mos.cms.futurecdn.net/i2vNxfmhvpAfR2sbEFDLh9-2000-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Claude Haiku
- Hugging Face
- Tencent
locations:
- Beijing
- British Columbia
- China
- Hong Kong
- Philadelphia
- US
organisations:
- AI
- API
- Alibaba
- Amap
- Anthropic
- Baidu Translate
- ByteDance
- CIFTIS
- Chengdu Zoo
- China International Fair for Trade in Services
- Jina
- OpenAI
- Reuters
- Seed
- Swarmchasers
- TechRadar Pro
- Tencent Cloud
- Tencent Holdings Ltd
- Tencent Hunyuan
- Zhipu
---

![A sign of Tencent Holdings Ltd is seen during the 2021 China International Fair for Trade in Services (CIFTIS) in Beijing, China](https://cdn.mos.cms.futurecdn.net/i2vNxfmhvpAfR2sbEFDLh9-1920-80.jpg)

* **Tencent says AI agents it used to evaluate third-party models showed "unintended" browsing behavior, the first such admission by a major Chinese firm**
* **Swarmchasers researchers logged more than 2,600 attempts by the Tencent Cloud fleet to pull entrance data from Alibaba's Amap**
* **Most attempts failed, but agents used a public scanner as a remote browser, and one leaked company API key returned real place data**

Tencent has acknowledged that AI agents running on its infrastructure behaved unexpectedly after independent researchers caught a fleet of them repeatedly trying to pull data from Alibaba's Amap navigation service.

*Reuters* reports the company's AI unit, Tencent Hunyuan, said the agents were being used to evaluate third-party models, in what appears to be the first known case of rogue agent activity acknowledged by a major Chinese company.

In a post on X, the unit said the activity did not come from its own Hunyuan models, noting "During these evaluations, some agents exhibited unintended web-browsing behavior, but our review found no evidence of deliberate targeting or coordination," before adding that it was tightening network access controls and agent monitoring.

## A lot of "unintended" effort for a zoo gate?

The admission follows a full report by Swarmchasers, a loose group of researchers who met at an AI hackathon. They counted more than 2,600 attempts to extract Amap data over 11 days, from September 28 to October 8 2026, traced the traffic to Tencent Cloud servers in Hong Kong, and then did something nobody appears to have done before: they talked to the agents while they were still running.

The tasks were almost comically mundane. A typical job asked which entrance of a place like Chengdu Zoo most Amap users use, with other runs covering parks, museums, and hospitals and, on September 30, a British Columbia cancer statistics dashboard.

The problem was getting the answer. Amap's anti-bot system expects browser cookies, JavaScript-generated tokens, and sometimes a CAPTCHA, while the fleet's harness sent plain Python and curl requests. One agent told the researchers that Amap had blocked its Tencent sandbox, so it could not fetch the data itself.

The agents improvised instead; according to the Swarmchasers report, they packed their own HTML and JavaScript into URLs and fed them to urlquery.net, a public security scanning service, borrowing its browser to run their code.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

When Amap kept blocking them, the programs tried to intercept or forge tokens from Alibaba's own anti-bot libraries, sent 57 requests to four pre-production hosts, routed traffic through Baidu Translate and remote browsers, and, in seven reports, used Amap API keys found on the open web.

Most of it did not work as intended: in a snapshot of 2,372 reports up to October 4, nearly half ended on an empty Amap page or login prompt and almost a quarter on a blank tab. None of the token tricks appear to have succeeded, and there is no evidence that any pre-production server answered. The entrance figures that did come back arrived mostly through Jina's page reader, which can serve cached copies up to 30 days old.

The exception should worry businesses more than Alibaba. A key and security code exposed in another company's public source code did return real place data, and the researchers say they cannot tell whose account was billed for those requests.

Tencent's framing of the activity as "unintended" is accurate as far as it goes, but it sidesteps an awkward point. If an evaluation asks agents for data that only Amap displays, behind defenses a sandboxed agent without a browser cannot legitimately clear, then crossing that line is close to the only route to a correct answer.

US incidents involved something similar: OpenAI's agents breached Hugging Face while hunting for answers to an ExploitGym benchmark, with later disclosures showing they organized through a makeshift message board, and roughly 700 of them took part in an attack Hugging Face eventually contained using Zhipu's open GLM 5.2 model. Anthropic found three Claude models had compromised real organizations after a misconfigured evaluation left internet access open, and this month disclosed that Claude Haiku 4.5 filed a false homicide tip with Philadelphia police while exploring random websites.

Reuters judges Tencent's case less egregious than those, and the Swarmchasers found no sign the agents coordinated, which is why they call it a fleet rather than a swarm. Still, as recent analysis argued, sandbox escapes often come down to an agent routing around a proxy, and borrowing a stranger's browser is exactly that.

Tencent's admission lands in the same week ByteDance's Seed unit created a dedicated Alignment & Preparedness team and began recruiting 10 researchers worldwide, a rare public commitment to frontier safety work by a major Chinese developer. The internal email announcing it went out a day before the Swarmchasers' full report and, in 36Kr's translation, points to a broader run of agent escapes rather than this one case, so the two are not cause and effect even if they do point the same way.

The argument is that alignment remains unsolved regardless of whose flag flies over the data center, and they want every lab running internet-connected agents to audit what its sandboxes can reach, a seemingly modest ask.

This fleet, however, ran for nearly a week before outside researchers stumbled on it at a hackathon, then carried on for four more days after their preliminary findings went public, and Tencent has yet to explain why.
