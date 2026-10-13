---
title: Hackers turn business backup servers into crypto mines after sneaking malware
  disguised as Microsoft Edge
source_url: https://www.techradar.com/pro/security/hackers-turn-business-backup-servers-into-crypto-mines-after-sneaking-malware-disguised-as-microsoft-edge
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-13T17:00:09Z'
published: '2026-10-13T00:00:00Z'
description: Servers used as a failsafe in case of a cyberattack, became targets of
  cyberattacks themselves
image: https://cdn.mos.cms.futurecdn.net/yaTc7yRkfydWWSj2tD8dGH-1920-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Huntress
locations:
- Hong Kong
organisations:
- AI
- Ahsay Cloud Backup Suite
- AhsayCBS
- CBS
- Huntress
- IT
- IoCs
- Java Server Page
- MSP
- Monero
- Task Manager
- TechRadar Pro
- XMRig
---

![Reprensentational image depitcting a mine worker toiling to mine cryptocurrency](https://cdn.mos.cms.futurecdn.net/yaTc7yRkfydWWSj2tD8dGH-1920-80.jpg)

* **Attackers exploited critical AhsayCBS backup software flaws to compromise organizations’ backup servers**
* **Intrusions deployed webshells and disguised XMRig cryptominers for persistence and stealth**
* **Researchers urge immediate patching, restricted access, and full system reimaging if compromised**

In a particularly brazen hack, threat actors were seen targeting the servers that businesses use as backups in case of a cyberattack.

The vulnerabilities used in this attack have since been mitigated, but since the attack is currently ongoing, organizations using this particular backup method are urged to apply the fixes immediately and secure their premises.

## AhsayCBS backup utility

At the core of this incident is a backup utility called Ahsay Cloud Backup Suite (or AhsayCBS), a server-based backup management platform developed by a company of the same name, based in Hong Kong.

Businesses, managed service providers (MSP), and IT admins use it to manage backups for their devices and clients across a range of virtual and physical servers, databases, and various software environments, with the tool widely used by IT service providers to manage their clients' data.

Security researchers Huntress noted that on October 4, 2026, two flaws in AhsayCBS were publicly disclosed: CVE-2026-105113, and CVE-2026-105134. The former is a medium-severity vulnerability affecting the checkSysPwd function, and can lead to improper authentication. The latter is a critical-severity flaw affecting the Replication Receiver component, which could lead to unauthenticated remote code execution as NT AUTHORITY/SYSTEM on the host.

“The API contains an authentication bypass that could allow for a random token to substitute valid credentials,” the researchers explained. “After exploitation, a threat actor configured a malicious receiver and dropped a Java Server Page (JSP) webshell into the application directory served by the CBS application.”

Just three days later, threat actors started exploiting these bugs - the first one to bypass authentication, and the second one to gain code execution and deploy webshells on exposed systems. The webshells served primarily as droppers, deploying a range of stage-two executables.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## Mining crypto

Huntress also saw threat actors deploy a popular cryptominer called XMRig. This is a legitimate open-source miner that uses the computer’s hardware, electricity, and internet, to mine the Monero currency and deposit it to the attackers’ wallets.

Monero is the go-to currency for unsolicited crypto mining since it is designed as a privacy-first coin that is very difficult to trace across the blockchain.

The attackers went to lengths to hide XMRig on these backup servers. They disguised them as a Microsoft Edge process and installed them as fake Edge update services. They also made sure it hid when someone looked.

A script (apparently written by AI) shuts down the miner whenever Task Manager is opened. The same script would close Task Manager after an hour.

Backups are perceived as one of the strongest protections against ransomware attacks. Virtually all cybersecurity organizations and thought leaders are advising organizations deploy backups and frequently maintain and control them, to make sure they are not outdated or otherwise corrupted. The fact that they can be compromised with relative ease should be cause for alarm. Businesses who were struck could consider themselves lucky to have only gotten an XMRig infection and not a full-blown ransomware encryptor.

That being said, as of October 8, at least five organizations were already targeted, Huntress said. Therefore, it is essential all organizations using AhsayCBS apply the provided patch as soon as possible. All versions of the utility, through 10.3.4 are impacted, it was said.

Besides applying the fix, organizations should also restrict AhsayCBS management interface web access, since the exploit targets the external accessible web app service on the host. “Access should be limited to trusted IP addresses only or require VPN,” Huntress says. “If any of the IoCs listed in this blog have been uncovered, companies should carry out a full host re-image from a trusted backup; as attackers have been able to hide secondary backdoors for extended persistence.”

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
