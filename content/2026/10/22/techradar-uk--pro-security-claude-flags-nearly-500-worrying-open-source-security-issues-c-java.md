---
title: Claude flags nearly 500 worrying open source security issues — C, Java, and
  Python code all at risk as one flaw wasn't spotted for 21 years
source_url: https://www.techradar.com/pro/security/claude-flags-nearly-500-worrying-open-source-security-issues-c-java-and-python-code-all-at-risk-as-one-flaw-wasnt-spotted-for-21-years
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-22T21:33:45Z'
published: '2026-10-22T00:00:00Z'
description: Hunting for individual vulnerabilities will get us nowhere, Anthropic
  argues
image: https://cdn.mos.cms.futurecdn.net/UVoJtVCqMw4zd4UHG7SaYa-1200-80.jpg
categories:
- Technology & Software
people:
- Claude
locations: []
organisations:
- AI
- Anthropic
- OSS-Scanner
- OpenSSH
- TechRadar Pro
---

![coding](https://cdn.mos.cms.futurecdn.net/UVoJtVCqMw4zd4UHG7SaYa-1200-80.jpg)

* **Anthropic used Claude to analyze 25 open source projects and uncovered nearly 500 security issues**
* **Research found exposed pre-authentication code paths, conflicting security settings, and long-hidden flaws**
* **AI identified attack-surface reductions that removed unnecessary code exposure before vulnerabilities could be exploited**

Anthropic recently used Claude to analyze 25 major open source projects written in C, C++, Java, PHP, and Python, in search of security issues. It found almost 500 of them, including security controls turned off by conflicts in settings, sensitive code accessible before authentication, and even a vulnerability that sat in the code for 21 years.

This wasn’t a standard hunt for vulnerabilities. In its report, Anthropic argues that looking for individual vulnerabilities is a Sisyphean task that scales poorly and never guarantees security. Instead, it thinks defenders should turn towards reducing software attack surfaces by restricting unnecessary access to potentially exploitable code.

“A defender who reduces unnecessary attack surface in their code reduces the risk from all of the unknown vulnerabilities in that code at once—including any that are already being quietly exploited,” Anthropic said.

The 25 projects it scanned contained more than five million lines of code. Claude created an inventory of more than 17,000 configuration options, 3,842 of which related to security-relevant controls and features.

## Misconfigured security controls

The company’s research focused on three ways code may get unnecessarily exposed: features accessible in the default configuration when they’re not needed, different settings which, when combined, erode security, and unnecessarily complex and sensitive code running before security checks.

The analysis showed all 11 projects, which were designed to serve authenticated users, contained code that was reachable when it shouldn’t have been. These include 93 pre-authentication attack surfaces in default configurations, 37 instances of code executing before authentication, and 61 combinations of different configurations that eroded pre-authentication controls.

In total, the 25 analyzed projects contained 162 configuration combinations that were accepted without their documentation explaining how they were supposed to behave. In some cases, security controls were being disabled. In others, there were various inconsistencies and problems.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

One configuration flaw was sitting undetected for more than two decades, Anthropic found. While one setting made clients prove their identity through certificates, another one disabled it entirely (even though it was designed to delay the check, not kill it). Even though these were conflicting options, they were accepted without warning.

## OpenSSH exposed thousands of lines of code

Anthropic singled out OpenSSH as its case study for the report. The software, widely used to provide secure remote access, contained a daemon that could reach 4,500 lines of experimental code that implements a post-quantum signature algorithm before checking if it was permitted by the server’s configuration to begin with.

As it turned out, the algorithm was disabled by default, but its parsing code was accessible to unauthenticated clients. Anthropic disclosed its findings to OpenSSH, who came back with a fix in version 10.6, in which some 20% of the code was now unreachable by unauthenticated clients.

The company said it combined these techniques into a reusable Claude skill which will soon be integrated into OSS-Scanner, its free, opt-in security scanning service for open-source projects. The skill will examine default configurations, code that is reachable before security checks, as well as settings configurations that are in conflict with one another.

Anthropic added that the system will validate the findings through a dynamic program tracing, and will test proposed changes against existing behavior. Potentially disruptive changes will be left for humans to review.

“It is perhaps impossible to measure how many unknown vulnerabilities are in any given codebase,” the researchers concluded. “And there is plenty of data that shows attackers can and will find those vulnerabilities with enough time (particularly if equipped with frontier AI models).” Therefore, AI could help developers systematically limit unnecessary exposure, making software that much harder to attack.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
