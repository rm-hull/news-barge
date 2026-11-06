---
title: Random 257-character long string is all it takes to gain root privileges on
  some Linux distros
source_url: https://www.pcgamer.com/software/linux/all-that-stands-between-a-hacker-and-admin-privileges-on-some-linux-distros-is-a-257-character-long-string-of-literally-anything/
source_site: PC Gamer
source_slug: pcgamer
description: Only a small, niche number of distros, though.
image: https://cdn.mos.cms.futurecdn.net/FzqWo3fsvLDFRpTumixHaY-1034-80.jpg
published: '2026-11-06T00:00:00Z'
scraped_at: '2026-11-06T23:06:47Z'
categories:
- Technology & Software
people:
- Fedora
- Ozgun Kultekin
locations: []
organisations:
- GitHub
- NAS
- OpenSSH
- PAM
- PC Gamer
- SSH
- Sshhole.com
- Ubuntu
---

![An Ubuntu Linux terminal showing attempt to ssh using FIX MOJANG BEDROCK spam.](https://cdn.mos.cms.futurecdn.net/FzqWo3fsvLDFRpTumixHaY-1034-80.jpg)

Some implementations of secure shell (SSH), one of Linux's most trusted and secure connection protocols, have been found vulnerable to the most peculiarly simple methods of bypass: spamming characters.

On some distros, simply type 257–1,024 characters and you get access to the root (admin) login. Thankfully, the list of vulnerable distros is quite small and niche, and OpenSSH has already issued a workaround/fix.

In some new release notes, OpenSSH explains that "this release contains a critical security workaround that affects Linux systems that use the musl libc and PAM disabled."

"Sshd(8): avoid password authentication bypass that is exploitable through sshd(8) that affects some Linux systems when built and run with PAM support disabled. We consider the root cause of this bug to be outside sshd, but it is exploitable via sshd and can be avoided there."

SSH itself is a longstanding and ubiquitous networking protocol that anyone who has dabbled even lightly in Linux networking projects will be familiar with. It's what manages comms between Linux machines. If you've ever used a Raspberry Pi remotely, for instance, you'll likely have logged into it using SSH. Same goes for a NAS. It's also used by devs to push/pull/manage GitHub files.

Thankfully, it's not SSH in general that has the problem but just a small number of distros that use SSH.

According to an explanation on sshhole.com—a website written by Ozgun Kultekin who discovered the bug—this is an issue with "musl Linux."

Keep up to date with the most important stories and the best deals, as picked by the PC Gamer team.

This refers to any Linux OS that uses the musl C library rather than the standard Glib C library, which is a fancier way of saying: not many distros.

Most distros don't use musl, but a few do. Perhaps most prominently, Alpine Linux, a minimal, security-focused distro. As OpenSSH clarifies, it's also not just musl Linux distros in general, but only those running SSH servers that have Pluggable Authentication Module (PAM) support disabled.

![A stock illustration showing a human hand holding an asterisk from an encrypted password.](https://cdn.mos.cms.futurecdn.net/T57wYtSENm7nCAGkSewHnA-1200-80.png)

The background as to why this bug occurs and why it was overlooked is pretty complicated, involving different login security functions developed for different purposes overlapping with this specific kind of edge case being overlooked. Sshhole.com explains it better than I can.

The long and short, though, is that one function used \* (a star) as a value under the assumption that it would never be used as a password hash, because that usually cannot happen. But another completely separate function, after some further shenanigans, makes the password hash a star if it's 'invalid' because the password has too many characters.

Thus: Spam letters, get let into root.

Most Linux users are absolutely fine. As the bug researchers explains: "On debian, ubuntu, fedora or anything else with glibc? going through pam? dropbear? openbsd? you're fine."

Here are the set of conditions you need to fall under to *not*be fine:*"Is your sshd running on musl? (alpine, openwrt, buildroot, yocto)* is it not using pam? alpine's openssh-server doesn't by default, or maybe you set UsePAM no
* are password logins still on? they are by default
* is there an account with just \*as its password? key-only users, ldap users, root on alpine* and some other account with a real password?"

Though for my part, and although this might not be warranted, I'll be considering this will a justification for sticking to the bigger distros. Ubuntu, Fedora, and so on. Or Windows, I suppose. Good things are still happening over in closed-source land.

![Razer Blade 16 gaming laptop](https://cdn.mos.cms.futurecdn.net/YwnnY4PZ7TcCYKRYDho7VW-140-80.jpg)
