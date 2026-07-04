---
title: Agentic AI tools now need real safeguards against this kind of indirection.
source_url: https://www.techradar.com/pro/security/agentic-coding-tools-have-access-to-everything-they-need-for-this-security-experts-warn-claude-code-can-be-exploited-simply-by-trying-to-be-helpful
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-04T20:14:57Z'
published: '2026-07-04T00:00:00Z'
description: Researchers hid an entire cyberattack inside a DNS record, and Claude
  Code ran it while just trying to fix an error
image: https://cdn.mos.cms.futurecdn.net/eZs7VDaqqgXt5TBmcicAmS-1920-80.jpg
---

![Claude Tag](https://cdn.mos.cms.futurecdn.net/eZs7VDaqqgXt5TBmcicAmS.jpg) 

- **Claude Code ran the dangerous command while treating it as routine recovery**
- **A single fake error message triggered the entire hidden attack chain**
- **Static scanners and firewalls saw nothing more than normal DNS resolution**

Researchers at Mozilla's 0din team have shown how Claude Code can be manipulated into opening a hidden reverse shell on a developer's device.

The exploit required no malicious code inside the cloned project, since every visible file passed ordinary review without raising suspicion.

Instead, the dangerous instruction arrived later, fetched at runtime from a DNS text record that no scanner would ever inspect.

## How a Routine Setup Error Became an Entry Point

The attack began with an unremarkable Markdown file explaining how to install a package called Axiom, a common monitoring tool.

Running the tool without initialising it produced a plain error message instructing the user to execute a specific setup command.

The research team noted this pattern closely resembles ordinary developer troubleshooting, which is precisely why it evaded suspicion so effectively.

Claude Code, attempting only to be helpful, followed that written instruction automatically, treating the documented fix as ordinary routine error recovery.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

That single command triggered a hidden shell script which quietly queried a DNS text record controlled entirely by the remote attacker.

The record decoded into a base64-encoded reverse shell command, which executed silently and connected straight back to the attacker's remote server.

Persistence was also possible once inside, since the attacker could plant an SSH key or schedule a hidden cron job.

A single repository link shared in a job posting or chat message could expose every developer who simply opened it.

## Why standard security tools failed to notice

Regular security tools, such as antivirus software or firewall protection, failed to notice this flaw since none of the individual steps looked suspicious on their own.

Static code-scanning tools only registered a routine DNS lookup, which did not indicate anything malicious underway.

Network monitoring registered nothing more than ordinary domain name resolution, and the agent itself viewed the command as a pre-authorised setup.

0din stressed that coding agents need to inspect exactly what setup script will actually run before executing anything at all.

It concluded that developers should never assume an unfamiliar repository is trustworthy, regardless of how ordinary its setup files appear.

This case suggests that agentic AI tools built on large language models may need far stronger runtime safeguards.

Until such agents can meaningfully evaluate what a command actually executes, similar indirect attacks will likely remain difficult to prevent.

The broader lesson extends beyond Claude Code, since most agentic AI systems share similar blind spots toward indirect prompt injection.

For now, treating unfamiliar automation as a genuine risk remains the single most reliable safeguard available to most individual developers.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Efosa Udinmwen](https://cdn.mos.cms.futurecdn.net/nwRLdPUNG4rWu4Y6nthHDV.png)

Efosa has been writing about technology for over 7 years, initially driven by curiosity but now fueled by a strong passion for the field. He holds both a Master's and a PhD in sciences, which provided him with a solid foundation in analytical thinking.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
