---
title: VMware tells users to patch critical security flaws now — vCenter issues could
  let hackers grab access to your systems
source_url: https://www.techradar.com/pro/security/vmware-tells-users-to-patch-critical-security-flaws-now-vcenter-issues-could-let-hackers-grab-access-to-your-systems
source_site: TechRadar UK
source_slug: techradar-uk
description: Broadcom issued a fix for five flaws, including a critical-severity one
image: https://cdn.mos.cms.futurecdn.net/XztdngjRmFS6xK2nNWp7Nm-1920-80.jpg
published: '2026-11-20T00:00:00Z'
scraped_at: '2026-11-20T20:06:53Z'
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Mandiant
locations:
- Armory Castle
organisations:
- Armory Castle
- Armory Castle Security
- BeyondTrust Remote Support
- BleepingComputer
- Broadcom
- CISA
- GTIG
- Google
- Google’s Threat Intelligence Group
- KEV
- Mandiant
- RPC
- SDDC Manager
- TechRadar Pro
- US Cybersecurity and Infrastructure Security Agency
- VMware vCenter
- VMware vCenter Server
---

![Padlock against circuit board/cybersecurity background](https://cdn.mos.cms.futurecdn.net/XztdngjRmFS6xK2nNWp7Nm-1920-80.jpg)

* **Broadcom patched a critical VMware vCenter authentication-bypass flaw that can grant attackers administrative access**
* **Researchers linked active exploitation to a China-aligned threat group targeting internet-facing infrastructure**
* **Organizations are urged to patch immediately, as compromise of vCenter can provide broad control over virtualized environments**

Broadcom has released an emergency update for VMware vCenter Server to patch a critical-severity vulnerability apparently being used in the wild by cybercriminals associated with the Chinese government.

The company has issued a security advisory covering five vulnerabilities: an authentication bypass in VMware Directory service in vCenter, three issues in SDDC Manager (SQL injection, authenticated command injection, local privilege escalation), and a SAML token signature bypass in VMware Tools for Windows.

“The vCenter issue permits an attacker with network access to vCenter to bypass authentication and gain unauthorized access to the system,” the advisory explains. “You are affected if you are running any version of VMware vCenter.”

## Exploited in the wild

The vulnerability is tracked as CVE-2026-123890, and was given a severity score of 9.8/10 (critical). It was patched on November 19 2026, and Broadcom now advises everyone to apply the fix without delay. It says there are no official workarounds or mitigations, but stressed that network restrictions and firewall controls could reduce the attack landscape somewhat.

Broadcom did not say the bug was being exploited in the wild, but reporters from *BleepingComputer* saw Google’s Mandiant documenting real-life attacks alongside Google’s Threat Intelligence Group (GTIG) reporting seeing Armory Castle, a group affiliated with the Chinese government, leveraging the bug in early September 2026.

"Successful exploitation results in a remote authentication bypass which creates an authenticated session established as [administrator@vsphere.local](mailto:administrator@vsphere.local)," the researchers said. "Using the authenticated administrator session, the attacker can execute arbitrary commands and acquire files, including the data.mdb database, by leveraging the vCenter Server Directory Service (vmdird) RPC interface vmdirdbcp."

The US Cybersecurity and Infrastructure Security Agency (CISA) has not yet added this bug to its Known Exploited Vulnerabilities (KEV) catalog. However, since reports of in-the-wild abuse are coming from reputable sources, chances are it will be added sooner or later.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

VMware vCenter Server is a centralized management platform through which organizations can manage their virtualized infrastructure, including virtual machines and ESXi hosts, all from a single interface. As such, it is a particularly valuable target for attackers, since compromising it can provide access to large portions of an organization’s IT environment.

Should they gain admin privileges, threat actors would be able to access sensitive data, manipulate virtual machines, deploy malware, and move laterally throughout the compromised network. In other words, rather than compromising individual servers one by one, threat actors who gain control of vCenter could obtain extensive visibility and control over an organization's virtual infrastructure.

## Armory Castle

Security researchers are saying Armory Castle specializes in exploiting vulnerabilities in internet-facing infrastructure, primarily network-edge devices and systems allowing remote access. They target high-value organizations in which they aim to establish persistent access.

Looking at previous operations, Armory Castle is most likely a well-resourced team with sophisticated vulnerability research capabilities (as is fitting for a nation-state attacker), custom malware, and advanced stealth capabilities.

In fact, researchers are saying that the VMware vCenter abuse is actually stage two of an attack that started on BeyondTrust Remote Support. Since late August, the attackers were using a zero-day in the tool, now tracked as CVE-2026-102764, to gain initial access and pivot into internal Linux systems, from which they targeted VMware infrastructure. The end goal, it seems, is to exfiltrate as much sensitive data as possible.

Mandiant says using two zero-day bugs in the same campaign shows just how knowledgeable and experienced the attackers are. Both Broadcom and Mandiant urged VMware users to install the security updates as soon as possible and set up additional security controls to make sure their infrastructure does not get compromised.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
