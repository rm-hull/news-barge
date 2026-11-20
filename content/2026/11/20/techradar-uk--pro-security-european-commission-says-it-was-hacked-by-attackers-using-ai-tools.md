---
title: European Commission says it was hacked by attackers using AI tools — says it
  is taking' the necessary steps in response to a detected cyber campaign'
source_url: https://www.techradar.com/pro/security/european-commission-says-it-was-hacked-by-attackers-using-ai-tools-says-it-is-taking-the-necessary-steps-in-response-to-a-detected-cyber-campaign
source_site: TechRadar UK
source_slug: techradar-uk
description: ARTEX has another major victim
image: https://cdn.mos.cms.futurecdn.net/x4SmwpYXk8yGgDmYCVeckL-2560-80.jpg
published: '2026-11-20T00:00:00Z'
scraped_at: '2026-11-20T11:35:53Z'
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Sysper
- Thomas Regnier
locations:
- US
organisations:
- AI
- ARTEX
- Autumn-27
- CERT-EU
- Censys
- Corporate Management Board
- Cybersecurity Service for the Union Institutions, Bodies, Offices and Agencies
- EU
- European Commission
- Microsoft
- NSA
- Playbook
- Politico
- ScopeSentry
- TechRadar Pro
- Vshell
---

![A hand about to touch a phone. Superimposed on top of it is a pink triangle with exclamation mark inside it. Behind it is a computer display with code on it](https://cdn.mos.cms.futurecdn.net/x4SmwpYXk8yGgDmYCVeckL-1920-80.jpg)

* **A cyberattack disrupted European Commission systems, including HR and medical reimbursement platforms, and forced some applications offline**
* **Officials are investigating whether any employee data was stolen while working to restore affected services**
* **Researchers linked the intrusion to abuse of the AI-powered penetration testing tool ARTEX, though no attribution has been confirmed**

The European Commission has confirmed being at the receiving end of a powerful cyberattack. The unnamed attackers forced a few apps offline, but whether or not any staff data was stolen, remains to be seen.

News of the breach broke on *Politico*, which said the attack lasted for ten days and was concentrated on a few apps - Sysper, the Commission’s human resources platform that employees use to access payroll information, leave requests, and work hour logs, and MyPMO, a medical reimbursement system. Sysper was brought back online only to crash again, it was said, and the Commission’s translation services were also briefly struck, too.

The attack was rather disruptive, since the Commission’s staff was unable to input salary or time off information, and even forced the agency’s most senior officials to get together and discuss. *Politico* said employees still got paid, despite a reported “lack of communication” and apparent “general issues” affecting the system’s overall functionality.

## Using ARTEX

“The Commission believes it has contained most of the attack, but the full extent of any damage remains unclear,” an EU official, granted anonymity because of the sensitivity of the issue, told *Politico’s* political newsletter, 'Playbook'. “The systems may be coming back online. The answers are taking a little longer.”

According to the Cybersecurity Service for the Union Institutions, Bodies, Offices and Agencies (CERT-EU), the attackers used ARTEX, a legitimate penetration testing tool hijacked for malicious purposes.

“Some actors misuse such tools and have targeted the Commission,” the EU official added. *Politico* said the Commission took down “several applications” as a precaution, but it’s unclear if this refers to Sysper and MyPMO, or other apps.

“The European Commission has taken the necessary steps in response to a detected cyber campaign,” Commission spokesperson Thomas Regnier told Playbook. “Individual systems were targeted and, in line with our standard practice, we have informed those concerned.”

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

ARTEX is the brainchild of a developer called Autumn-27. They first built ScopeSentry, a Chinese asset discovery and vulnerability scanning platform, then added an AI layer on top and called it ARTEX. In other words - it is an LLM-powered version of ScopeSentry that syncs assets found by the tool’s domains, subdomains, IPs, ports, and endpoints.

## Ongoing investigation

The pentesting tool was released in July 2026 and was soon adopted by cybercriminals. When news of hacks first emerged, the developer distanced themselves from the illicit activity and stressed the tool was built for testing within authorized asset scopes. They then turned it into a closed-source tool with no further releases, but since the code was released to the wild, many copies, translations, and rebrands started circulating online.

In fact, researchers Censys recently claimed they found around 1,500 instances on the internet, widely available to anyone. Of those, roughly 10% were also running at least one tool commonly used in cyberattacks, such as Vshell, or Adaptix C2. The researchers also found 32 publicly accessible directories on ARTEX hosts, some of which exposed exploit binaries, post-exploitation tools, and other sensitive files.

The Commission is now trying to establish whether any data was stolen. So far, no threat actors claimed responsibility for the attack, and the data has not yet surfaced on the dark web. No one posted samples or demanded money in exchange.

Still, the attack is being taken rather seriously. Politico says the Commission “convened its highest-level internal crisis-management body”, the Corporate Management Board, for an urgent meeting to discuss “ongoing cyber incidents”.

Over the last couple of weeks, we’ve seen numerous, high-profile cyberattacks take place: Microsoft was struck, the NSA, the US banking system, and many, many others. Many people believe these attacks are the result of AI agents going rogue or, at the very least, cybercriminals now having the tools to mount extremely damaging attacks rather easily (and cheaply).

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
