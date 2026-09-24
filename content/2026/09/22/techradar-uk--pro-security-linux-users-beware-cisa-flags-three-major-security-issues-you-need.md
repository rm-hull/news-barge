---
title: Linux users beware — CISA flags three major security issues you need to patch
  right now
source_url: https://www.techradar.com/pro/security/linux-users-beware-cisa-flags-three-major-security-issues-you-need-to-patch-right-now
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-22T04:44:37Z'
published: '2026-09-22T00:00:00Z'
description: Two flaws have available mitigations, too
categories:
- Technology & Software
image: https://cdn.mos.cms.futurecdn.net/MRcAF4wnJU8Qb7Bv7Lb9yd-1920-80.jpg
locations:
- Bosnia and Herzegovina
- Sarajevo
people:
- Sead
organisations:
- ARP
- Al Jazeera Balkans
- CISA
- CVE-2026-53266
- DirtyAH6
- FCEB
- Federal Civilian Executive Branch
- Google News
- PPPoEject
- Red Hat
- Represent Communications
- SNAT
- TLS
- TUNderflow
- TechRadar Pro
- US Cybersecurity and Infrastructure Security Agency
---

![Linux penguin logo on wood](https://cdn.mos.cms.futurecdn.net/MRcAF4wnJU8Qb7Bv7Lb9yd.jpg)

* **CISA added three Linux kernel flaws (CVE‑2025‑39682, CVE‑2026‑53266, CVE‑2025‑39964) to KEV catalog**
* **Red Hat confirmed active exploitation; agencies given rare three‑day patch deadline expiring Sept 21, 2026**
* **Bugs enable DoS, privilege escalation, or data corruption; patches available, limited mitigations for two flaws**

The US Cybersecurity and Infrastructure Security Agency (CISA) has added three Linux flaws to its Known Exploited Vulnerabilities (KEV) catalog, signaling abuse in the wild and giving government agencies a deadline to patch or stop using the flawed product entirely.

The three bugs in question are tracked as CVE-2025-39682 (severity score 9.8/10 - critical), CVE-2026-53266 (severity score 8.8/10 - high), and CVE-2025-39964 (severity score 7.8/10 - high). All three have already been patched in the Linux kernel. CVE-2025-39682 was fixed in stable releases 6.1.149, 6.6.103, 6.12.44 and 6.16.4, while CVE-2025-39964 was fixed in 5.10.245, 5.15.194, 6.1.154, 6.6.108, 6.12.49 and 6.16.9. CVE-2026-53266 has been fixed upstream and backported to supported stable/distribution kernel branches, including 5.10.259, 6.1.176 and 6.12.94.

The first issue is an improper check for unusual or exceptional conditions vulnerability in the TLS receive patch which could allow unauthenticated threat actors to launch memory disclosure or denial-of-service (DoS) attacks. The second one (CVE-2026-53266) is an out-of-bounds write vulnerability in the ebtables Source Network Address Translation (SNAT) Address Resolution Protocol (ARP) rewrite patch which allows local attackers to escalate privileges or mount DoS attacks.

The last one (CVE-2025-39964) is a race condition flaw that allows concurrent writes to the same AF\_ALG socket, which allows local malicious actors to crash the system or corrupt cryptographic operation results, leading to data integrity issues and possible DoS states.

## Attacks in the wild

Red Hat acknowledged that all three are being abused in real-life attacks. “This CVE is high risk and there are known public exploits leveraging this vulnerability. Address this vulnerability with high priority,” it said in all three advisories.

However, there are no details as to who is currently using these exploits, against whom, and to what cause. There are currently no separate reports of cyberattacks referencing any of the abovementioned vulnerabilities.

However, CISA still reacted. All three flaws were added on September 18, 2026, and all three have a small three-day deadline for patching that expires on September 21. Usually, CISA would grant Federal Civilian Executive Branch (FCEB) agencies a three-week deadline to patch up, with just exceptionally dangerous flaws getting a shorter window. That being said, these flaws are likely extremely dangerous.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## In theory...

In a hypothetical scenario, a threat actor could target a Linux system using kernel TLS (kTLS) by sending a specially-crafted TLS record that triggers CVE-2025-39682 and causing either a crash, or even arbitrary code execution. Attackers that already have a low privilege foothold on the target endpoint could use CVE\_2025-39964 to escalate privileges, while on systems using the affected bridge/netfilter configuration, CVE-2026-53266 could be used for privilege escalation, as well.

According to the Red Hat advisory, there is a chance that CVE-2025-39682 is remotely triggerable, but only when the system is using the affected kTLS receive path. The other two flaws are exclusively local vulnerabilities.

Besides fixes, two out of the three flaws also have possible mitigations. For the improper check one, users should prevent module tls from being loaded. For the out-of-bounds write one, users are advised to disable ARP hardware address rewriting in ebtables SNAT rules, or remove ebtables SNAT rules that operate on ARP traffic on bridge interfaces. The final vulnerability, currently does not have a working mitigation, and the only way to stay secure is to apply the provided patches.

Linux kernel vulnerabilities are generally considered serious, but the severity still depends on the flaw and how the affected kernel is deployed. Earlier this year, security researchers disclosed four local privilege escalation flaws, called DirtyAH6 (CVE-2026-80844), TUNderflow (CVE-2026-81000), PPPoEject (CVE-2026-68121), and DiagSpill (CVE-2026-74469).

*Via* * The Hacker News*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png)

![Google logo on a black background next to text reading &#039;Click to follow TechRadar&#039;](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg)

***Follow TechRadar on Google News***and** add us as a preferred source** * to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
