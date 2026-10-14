---
title: Security flaws found in top open source AI gateway — LiteLLM vulnerabilties
  could affect millions of users
source_url: https://www.techradar.com/pro/security/security-flaws-found-in-top-open-source-ai-gateway-litellm-vulnerabilties-could-affect-millions-of-users
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-14T17:10:13Z'
published: '2026-10-14T00:00:00Z'
description: LiteLLM users told to patch immediately
image: https://cdn.mos.cms.futurecdn.net/4d3FzfBhbeGTkD9mnMpEdM-2560-80.jpg
categories:
- Technology & Software
people: []
locations:
- AI
- LiteLLM
organisations:
- AI
- Anthropic
- CPR
- CVE-2026-35029
- Check Point Research
- GitHub
- LiteLLM
- OpenAI
- TechRadar Pro
---

![A close up of a person&#039;s eyes and face. They are wearing glasses and in one eye there&#039;s. a reflection of a digital brain](https://cdn.mos.cms.futurecdn.net/4d3FzfBhbeGTkD9mnMpEdM-1920-80.jpg)

* **Two LiteLLM flaws let low-privileged users gain administrative control and execute malicious code**
* **Attackers could also steal AI provider API keys through a server-side request forgery bug**
* **Organizations should upgrade to LiteLLM 1.83.9+ and rotate potentially exposed credentials**

Security researchers recently discovered two vulnerabilities in a popular AI gateway that allowed threat actors to take complete control of the system, steal sensitive files and AI provider API keys, and execute malicious code remotely.

The AI gateway in question is called LiteLLM. It is an open source solution allowing users to connect their applications to large language models (LLM) from different providers, including the likes of OpenAI and Anthropic.

The connection goes through a single interface, where users can route requests, manage API keys, control user access, and monitor things like usage and costs.

Right now, LiteLLM supports some 140 AI providers and has become quite popular - it has more than 90 million monthly downloads on GitHub, and more than 61,000 stars.

## LiteLLM

However, security experts from Check Point Research (CPR) recently found two bugs in LiteLLM.

The first one is an access control bug in the way LiteLLM enforces permissions. It is tracked as CVE-2026-35029 and was given a severity score of 8.7/10 (high). According to CPR, the bug allows users with minimal privileges to reach admin functions controlling the gateway’s core configuration which, in turn, allows them to read files stored on the server, overwrite admin credentials, download and run malware, and more.

The second one is a server side request forgery bug, allowing gateway users to direct LiteLLM to send API requests to third-party servers. In theory, threat actors could send API requests to servers under their own control, and since these carry AI provider authentication keys, this would deliver the credentials directly to the attackers. In turn, they could use the credentials to use other organizations’ AI accounts and rake up their bills. The bug is tracked as CVE-2026-59823 and was given a severity score of 5.3/10 (medium).

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

“The credentials a gateway holds provide direct, billable access to AI providers with no further authentication required,” CPR explained. “Given LiteLLM’s scale of adoption, a flaw in this component has the potential to affect a very large number of AI deployments at once.”

## Vulnerable versions and patches

CPR says that all organizations running LiteLLM versions earlier than 1.83.9 are exposed to both vulnerabilities. Security teams should also check for LiteLLM instances running indirectly, since the gateway is embedded in many platforms and internal tools used to build AI applications. As such, it could be present in environments where it was never deployed as a standalone solution.

LiteLLM has released a fix for both bugs included in version 1.83.9, and users are advised to install this one as soon as possible. Besides that, CPR advises users review who has access to the gateway, since any account could be used to exploit these flaws. AI provider API keys stored in LiteLLM should be rotated if there is any indication the gateway way accessed by unauthorized users, and permissions should be verified in practice.

“Confirm that users with limited roles are actually limited, because the gap between configured and enforced permissions is where flaws like CVE-2026-35029 cause the most damage,” CPR warns.

“Include LLM gateways in security assessments by extending penetration tests and vulnerability assessments to cover AI tooling alongside web applications and cloud infrastructure.”

According to the researchers, both bugs are a “well understood class” of errors, meaning AI infrastructure suffers from the same risks as enterprise software. That means organizations need to approach AI gateway security “with the same rigor they apply to any other business critical system.”

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
