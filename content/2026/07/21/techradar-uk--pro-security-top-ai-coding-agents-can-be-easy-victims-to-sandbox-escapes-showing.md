---
title: Top AI coding agents can be easy victims to sandbox escapes, showing they aren't
  as secure as they claim to be
source_url: https://www.techradar.com/pro/security/top-ai-coding-agents-can-be-easy-victims-to-sandbox-escapes-showing-they-arent-as-secure-as-they-claim-to-be
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-21T14:17:38Z'
published: '2026-07-21T00:00:00Z'
description: What if a host component outside the sandbox reads AI coding agents'
  output?
image: https://cdn.mos.cms.futurecdn.net/mfPaYGQmks2VALWFFBnSej-2000-80.jpg
---

![A robot hand touching a locked digital shield blocking a human from accessing data](https://cdn.mos.cms.futurecdn.net/mfPaYGQmks2VALWFFBnSej.jpg) 

- **Pillar researchers demonstrated sandbox escapes in AI coding agents**
- **Exploits let attacker‑written configs run with trusted host privileges**
- **Agentic security needs its own threat model, researchers claim**

AI coding agents can be tricked into turning on their operators and assisting attackers in compromising the underlying systems, experts have warned.

Cybersecurity researchers Pillar have examined different methods of achieving the same results, finding that over the course of a couple of months, Cursor, Codex, Gemini CLI, and Antigravity were all able to reproduce sandbox escapes and boundary bypasses.

In theory, a threat actor could create a repository containing malicious content (for example, a README file, a dependency, or similar) and trick the developer into using it. The malicious instructions tell the agent to create or modify a project configuration file, but since everything happens inside the workspace, no alarms are triggered.

## Fixing the problems

Then, a host component outside the sandbox (Git integration, an IDE extension, or local daemon) reads that modified configuration, executing attacker-written commands. Consequently, the code now runs with the privileges of the trusted host component, rather than the restricted AI agent. Voila - the original sandbox boundary is effectively bypassed.

Three of the four platforms mentioned in the report have fixed the disclosed issues, Pillar said.

Cursor patched multiple vulnerabilities in version 3.0.0, with one assigned CVE-2026-48124 and another tracked through a GitHub Security Advisory. Codex CLI fixed it in version 0.95.0 but stressed that it’s still awaiting a CVE. Gemini CLI was affected by the Docker daemon issue, which the report says has also been fixed through advisory GHSA-v4xv-rqh3-w9mc.

For Antigravity, Google acknowledged both reported sandbox bypasses as valid security findings but labeled them “Other valid security vulnerabilities” and downgraded their severity. Apparently - it considers exploitation rather difficult.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

“When it comes to agents, the sandbox boundary that developers expect in coding tools -- one that keeps the agent inside the sandbox and the user outside -- breaks down,” Pillar concluded. “The boundary we kept finding was both messier and porous, because If an agent gets to write the future inputs of systems, it was never sandboxed in the first place.”

“This is why agentic security requires its own threat model.”

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
