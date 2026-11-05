---
title: Combined flaws let anyone into Alpine Linux and other distros by typing anything
  over 256 characters as a password — emergency fixes for OpenSSH and musl-libc issued
  for millions of systems, patch immediately
source_url: https://www.tomshardware.com/tech-industry/cyber-security/combined-flaws-let-anyone-into-alpine-linux-and-other-distros-by-typing-anything-over-256-characters-as-a-password-emergency-fixes-for-openssh-and-musl-libc-issued-for-millions-of-systems-patch-immediately
source_site: Tom's Hardware
source_slug: toms-hardware
description: Combined OpenSSH and musl-libc flaws let anyone into Alpine Linux and
  other distros by typing anything over 256 characters as a password — emergency fixes
  issued for millions of systems, patch immediately
image: https://cdn.mos.cms.futurecdn.net/BptY8MpPGXGUqczAtupMHF-2048-80.jpg
published: '2026-11-05T00:00:00Z'
scraped_at: '2026-11-05T23:36:44Z'
categories:
- Technology & Software
- Hardware
people:
- Bruno Ferreira
- Rich Felker
- Tom
locations:
- Buildroot
- Docker
- Kubernetes
- Proxmox
- Yocto
organisations:
- Dropbear
- Get Tom's Hardware
- Google News
- OpenSSH
- OpenWRT
- PC
- SSHhole
- Tom's Hardware
---

![Security vulnerability](https://cdn.mos.cms.futurecdn.net/BptY8MpPGXGUqczAtupMHF-1920-80.jpg)

The internet is still reeling from the PHP engine vulnerability and all other security vulnerabilities found over the past few weeks, and we're not done. Today's special is quite spicy: you can get into Alpine, OpenWRT, and other Linux distros without needing a password, thanks to a combined bug with OpenSSH and musl libc. Just randomly type over 256 characters on the password prompt and you'll be let in through the SSHhole.

It works if you set an empty password for system users, which is the default on multiple distros. The bug is present, though not necessarily enabled, across Buildroot, Yocto, and Void Linux. OpenWRT uses Dropbear for authentication by default, but users can install OpenSSH instead.

The largest concern is by far Alpine, though, as it's pretty much the default choice for what could amount to millions of installs across Docker/Kubernetes/Proxmox containers and endless dependencies thereof, servers, cloud VMs, and embedded devices, among many others. Alpine comes with the requisite conditions set and password authentication enabled by default, which is why it needs immediate patching.

Broadly speaking, the vulnerability combination is: OpenSSH, musl, password authentication not explicitly disabled, not using PAM, and the one arbitrary user with a password set, using a SHA-512/256 hash.   
Patch your systems immediately, as per the project's advisory note. Meanwhile, the easiest mitigation is explicitly setting "PasswordAuthentication" to "no" in your OpenSSH configuration file and restarting the service.

While in practice the vast majority of Alpine and similar installs aren't reachable from the internet, any attacker inside a network, including but not limited to corporate setups, home labs, cloud networks, and VPNs, can let themselves in. Likewise, all it takes is one valid user account, not too hard to get in a large enough corporate environment, and then an attacker is inside the network. Scanning and testing the vulnerability is also trivial.

OpenSSH has already published a fix and an advisory post, as did musl author Rich Felker. Both parties seem to believe the other is at fault, but looking from the outside, blame is shared.

If you've ever looked in the /etc/passwd or /etc/shadow files, you may have noticed a single asterisk as a placeholder for the password hash for accounts with no password — meaning "no password should work." The SSHhole website has all the details, but the snafu happens both when musl's crypt() function returns "\*" as an error condition instead of a null value as per usual conventions, and then OpenSSH uses it to compare to a password hash, when it shouldn't. An overly long input then triggers the chain of mistakes.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G-140-80.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.
