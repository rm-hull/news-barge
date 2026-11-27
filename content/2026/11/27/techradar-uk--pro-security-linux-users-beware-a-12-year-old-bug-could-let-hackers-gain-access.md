---
title: Linux users beware — a 12-year-old bug could let hackers gain access to everything
  you hold dear
source_url: https://www.techradar.com/pro/security/linux-users-beware-a-12-year-old-bug-could-let-hackers-gain-access-to-everything-you-hold-dear
source_site: TechRadar UK
source_slug: techradar-uk
description: Heap buffer overflow bug discovered
image: https://cdn.mos.cms.futurecdn.net/XPeygQKsauMqATxQynZwWL-1920-80.jpg
published: '2026-11-27T00:00:00Z'
scraped_at: '2026-11-27T21:10:06Z'
categories:
- Technology & Software
people:
- Jérémy Jean
locations: []
organisations:
- ANSSI
- CISA
- Dirty Frag
- KEV
- Microsoft
- NFS
- NFS2ROOT
- NFSD
- OpenSec
- Qualys
- TechRadar Pro
- US Cybersecurity and Infrastructure Security Agency
---

![INUX - word on Computer keyboard keys](https://cdn.mos.cms.futurecdn.net/XPeygQKsauMqATxQynZwWL-1920-80.jpg)

* **A critical Linux kernel flaw dubbed NFS2ROOT allows remote attackers to gain root privileges through vulnerable NFS server deployments**
* **The vulnerability reportedly existed for more than a decade and affects systems running exposed NFS services on internet-accessible hosts**
* **Researchers urge immediate kernel updates, warning that public exploit code is available and exploitation attempts are likely to follow**

It’s no longer trendy to label vulnerabilities “2shell” - we’ve moved on to “2root” now - and Linux users in particular should be on their guard, experts have warned.

The first one is NFS2ROOT, a heap buffer overflow vulnerability in the Linux kernel’s Network File System (NFS) server (nfsd), which allows threat actors to gain root privileges on a vulnerable Linux device remotely.

The bug, now tracked as CVE-2026-99362, and was given a severity score of 9.8/10 (critical) was discovered by security researcher Jérémy Jean of ANSSI, who also submitted a fix in August 2026.

## No evidence of abuse (yet)

But it being a critical-severity flaw is not the worst part - this bug has been hiding in the Linux kernel’s NFS server for 12 years. It was first introduced with Linux kernel version 3.16, which was released in March 2014, and has since affected all versions older than 6.12.117, 6.18.61, 7.3.2, or 7.4-rc1 if nfsd (v4.1 or 4.2) is loaded and running. Another prerequisite is that TCP port 2049 needs to be accessible over the Internet.

According to *BleepingComputer*, security researchers OpenSec shared a full remote-root exploit and a patch with the NFSD maintainers in late September 2026, and explained what successful exploitation looks like.

As per the researchers, threat actors could send a custom-built request that causes the NFS server to write data beyond its allocated memory buffer. This lets the attackers read kernel memory, bypass the KASLR protection mechanism, and place a callback that executes commands in areas of memory that were then released. As soon as the attackers close the NFS connection, the kernel runs the command with root privileges, granting them root access.

In other words, remote actors can corrupt kernel memory and thus gain root access in attacks that don’t require any user interaction and are generally perceived as low in complexity.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

So far, there are no reports of NFS2ROOT being abused in the wild, and the US Cybersecurity and Infrastructure Security Agency (CISA) have not yet added it to its Known Exploited Vulnerabilities (KEV) catalog. Still, OpenSec urges security teams to apply the latest kernel security updates from their Linux distribution vendor as soon as possible, as it anticipates abuse to pick up in the coming days and weeks.

There are a few workarounds and mitigations, too, including restricting access to the NFS server over TCP port 2049, or disabling NFS sharing entirely in /etc/nfs.conf.

"Port 2049 sits open on file servers, NAS appliances, build farms and Kubernetes storage nodes. Since 2014, the Linux kernel listening on it has let anyone who can reach it write into kernel memory before logging in," OpenSec said. "Kernel hardening does not remove the overflow. Patch every host."

## Big year for privilege escalation in Linux

To monitor for potential attacks, IT teams should check for kernel warnings from nfsd4\_check\_resp\_size, shells spawned by kernel workers on a file server, bursts of short NFSv4.1 sessions from one source, and kernel oopses with nfsd4\_\*, svc\_\* or call\_usermodehelper\* frames, OpenSec also stressed.

2026 has been a big year for high-severity Linux kernel privilege escalation vulnerabilities. This year, we’ve seen both Copy Fail (CVE-2026-31431) and Dirty Frag (CVE-2026-43284 and CVE-2026-43500), two bugs with a vulnerability rating of 7.8 and 8.8, respectively. Microsoft also reported seeing Dirty Frag being abused in the wild in May 2026, claiming it was being used to escalate privileges after initial system compromise.

Qualys also discovered CVE-2026-46333 in May 2026, a flaw that affects the kernel's ptrace access-control logic and allows unprivileged local users to steal sensitive credentials or execute commands as root.

Microsoft recently revealed it had found eight more flaws, for which they built working local privilege-escalation exploits, including a use-after-free flaw in the kernel's shared hash-table implementation (CVE-2026-64563).

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
