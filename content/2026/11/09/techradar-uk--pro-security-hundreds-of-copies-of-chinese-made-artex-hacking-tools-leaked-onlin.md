---
title: Hundreds of copies of Chinese-made ARTEX hacking tools leaked online for anyone
  to use in further attacks
source_url: https://www.techradar.com/pro/security/hundreds-of-copies-of-chinese-made-artex-hacking-tools-leaked-online-for-anyone-to-use-in-further-attacks
source_site: TechRadar UK
source_slug: techradar-uk
description: At least a tenth was used alongside other malicious tools
image: https://cdn.mos.cms.futurecdn.net/x4SmwpYXk8yGgDmYCVeckL-2560-80.jpg
published: '2026-11-09T00:00:00Z'
scraped_at: '2026-11-09T23:54:45Z'
categories:
- Technology & Software
people:
- Censys
- Claude Code
locations: []
organisations:
- ARTEX
- Autumn-27
- Censys
- Cobalt Strike
- ConnectWise Cloud Backup
- CrowdStrike
- CyberStrikeAI
- Grok
- HexStrike AI
- Microsoft
- PentAGI
- RedAmon
- Storm-0940
- TechRadar Pro
- Vshell
---

![A hand about to touch a phone. Superimposed on top of it is a pink triangle with exclamation mark inside it. Behind it is a computer display with code on it](https://cdn.mos.cms.futurecdn.net/x4SmwpYXk8yGgDmYCVeckL-1920-80.jpg)

* **Researchers found over 1,400 exposed ARTEX instances online, with many linked to offensive security tooling**
* **ARTEX combines AI agents with reconnaissance capabilities and has been increasingly adopted in real-world attacks**
* **Some operators accidentally exposed malware, exploits, credentials, and internal infrastructure through misconfigured servers**

Around 1,500 malicious instances of ARTEX were found on the internet, available to anyone who knew where to look, experts have warned.

Security researchers Censys said they identified 1,465 hosts running exposed ARTEX consoles. Of those, 155 (roughly 10%) were also running at least one tool commonly used in cyberattacks, including Cobalt Strike, Vshell, or Adaptix C2. They also found 32 publicly accessible directories on ARTEX hosts, some of which exposed exploit binaries, post-exploitation tools, and other sensitive files.

Usually, the ARTEX console does not require public-facing access, the researchers said, stressing that overall global deployment is “likely higher”.

## Hijacking ARTEX

ARTEX is a legitimate penetration testing tool hijacked for malicious purposes, meaning at least some of these instances were set up by threat actors.

The story of ARTEX is similar to that of the now infamous Cobalt Strike. It was released by a developer called Autumn-27, who also authored ScopeSentry - a tool Censys describes as a “widely used Chinese asset-discovery and vulnerability-scanning platform”.

The researchers described ARTEX as an “AI agent layer on top of that recon foundation”. In other words - it is an LLM-powered version of Scope Sentry that syncs assets found by the tool’s domains, subdomains, IPs, ports, and endpoints.

ARTEX was released in late July 2026 and quickly gained popularity. On October 7, security researchers CrowdStrike reported seeing it used in malicious attacks and a day later, the developer distanced themselves from the illicit activity and stressed the tool was built for testing within authorized asset scopes. They then turned it into a closed-source tool with no further releases. However, despite the repository being taken down, Censys claims archived copies, translations, and different rebrands are still circulating.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Since then, numerous researchers observed it being used in different attacks. The CrowdStrike report described an unidentified threat actor using ARTEX to target South Korean financial institutions. The attacker, believed to be a financially-motivated Chinese actor (as opposed to being a state-sponsored one), compromised a broker-facing loan inquiry service at one bank and an employee mobile system at another. In both instances, they walked away with sensitive data.

They used ARTEX with DeepSeek v4.1-flash as their primary AI model, while also running Claude Code and Grok. The researchers found the operation in part because the attackers left publicly accessible directories where they exposed prompts, session histories, and ARTEX configuration files.

Censys later said the directories had been left exposed in mid-August, roughly seven weeks before CrowdStrike published its findings. File names also suggested they were targeting payment and gaming services, as well.

At one point Microsoft linked it to Storm-0940, a China-aligned threat actor responsible for compromising ConnectWise Cloud Backup customer environments. Apparently, the threat actors used ARTEX to automate scanning, password spraying, and OAuth application abuse, peaking at 2,900 sign-in attempts per minute at one point. Some Microsoft’s customers were allegedly seeing privileged cloud access granted in less than three hours.

## Exposing their own infrastructure

Now, Censys says ARTEX is being paired with other offensive tools. At least 70 hosts were seen running both ARTEX and CyberStrikeAI, and others were seen deploying PentAGI, HexStrike AI, and RedAmon. Ironically enough, the researchers also found some actors had inadvertently exposed sensitive information through poorly secured directories. One installation exposed the operator’s entire home directory, including SSH configuration files and shellac command history, while others contained Windows lateral movement tools, malware implants, reverse-shell scripts, and exploit code.

Censys also stressed that not all of the exposed instances are malicious. They also said that roughly 650 of the detected hosts belonged to two groups of identically configured hosting infrastructure, leaving approximately 815 unique installations.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
