---
title: OpenAI says its cyber model found and patched nearly 1000 Linux kernel security
  issues
source_url: https://www.techradar.com/pro/security/openai-says-its-cyber-model-found-and-patched-nearly-1000-linux-kernel-security-issues
source_site: TechRadar UK
source_slug: techradar-uk
description: A third of the flaws were being publicly discussed
image: https://cdn.mos.cms.futurecdn.net/7DtE9RCVmUtmH2FAfvxsvM-2560-80.jpg
published: '2026-11-05T00:00:00Z'
scraped_at: '2026-11-05T17:23:14Z'
categories:
- Technology & Software
people: []
locations: []
organisations:
- AI
- Linux
- OpenAI
- TechRadar Pro
---

![Malware attack virus alert , malicious software infection , cyber security awareness training to protect business](https://cdn.mos.cms.futurecdn.net/7DtE9RCVmUtmH2FAfvxsvM-1920-80.jpg)

* **OpenAI used AI agents to analyze the Linux kernel, uncovering 948 distinct privilege-escalation vulnerabilities**
* **The automated pipeline generated exploits, validated findings, and helped create patches for Linux maintainers**
* **Researchers say AI is increasingly capable of finding and prioritizing serious software flaws at scale**

OpenAI has spent more than a million dollars to analyze the Linux kernel code, and found thousands of vulnerabilities, including countless privilege escalation flaws that could have been quite problematic for the popular operating system.

The AI company published a new in-depth report describing how it built a five-stage pipeline that helped it surface thousands of vulnerabilities, identify which ones were actually dangerous, helped create patches, and ended up securing the Linux ecosystem some more.

The pipeline covered vulnerability discovery, dynamic validation, exploitability assessment, patch generation, and human review, and once it was done, it found 948 privilege escalation flaws in the Linux kernel.

## Guerilla marketing

“The Linux kernel underpins Android devices, cloud infrastructure, supercomputers, and other systems used by billions of people,” OpenAI said.

“With more than 40 million lines of code, the kernel exposes a broad attack surface through system calls, networking, filesystems, and device drivers. We chose Linux to study how effectively frontier models could find vulnerabilities and demonstrate their security impact in a codebase of this scale and importance.”

While the efforts are certainly commendable (especially the fact that the entire ordeal cost roughly $1.21 million in API credits), the report also reads like guerilla marketing for the company’s latest cyber model. After all, the report never mentions its name, apart from the fact that it is an “upcoming cyber model” that found 900+ flaws, which is then compared to GPT 5.5-Cyber which “developed 24 local privilege escalation exploits.”

That being said, the results cannot (and should not) be ignored. The first stage used AI agents to identify security-relevant parts of the kernel and scan them for potential flaws, and within 12 hours, more than 2,300 candidates emerged. Then, OpenAI used additional agents to generate proof-of-concept (PoC) code and test each candidate. The entire process lasted 30 hours, and the system successfully reproduced 1,724 findings (roughly 75% of the initial candidates), while just 3% of the remaining findings apparently came from incorrect model analysis.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

In the next step, the agents ranked the vulnerabilities by impact, developing 1,169 working local privilege escalation exploits and 291 PoCs demonstrating information disclosure. After eliminating double entries and false positives, the researchers arrived at 948 distinct escalation flaws and built patches for them.

OpenAI said its researchers reviewed all of the generated exploits and patches before reaching out to Linux kernel maintainers. Following guidance from the Linux community, the team ranked the flaws by priority, and some seem to have already been patched. The remaining findings are currently being addressed, it was said.

## New exploitation techniques

“We provide the model with the relevant source code and prompt it with best practices in patch writing, such as performing static checks on the patch, following the software development practices used in nearby code, and performing variant analysis to make sure the patch is complete,” OpenAI explained the process.

Not all of the vulnerabilities were “brand new”, so to speak. OpenAI said Linux maintainers already patched 61 of the identified privilege elevation flaws by the time it completed its analysis, while another 43 had staging patches. Just under 300 (roughly a third) were being reported and discussed publicly, which is also worth putting into context.

On top of it all, the team examined 166 exploitation techniques and found 10 that were previously undocumented. They include kernel memory manipulation, page grooming, and privilege escalation through data-only attacks. OpenAI decided not to share the details on these flaws until they are fixed, in order not to give threat actors the upper hand.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
