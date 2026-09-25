---
title: '''Decades-old'' bugs found affecting Windows, Android, macOS and Linux — but
  the OS makers don''t see it as a big deal'
source_url: https://www.techradar.com/pro/security/decades-old-bugs-found-affecting-windows-android-macos-and-linux-but-the-os-makers-dont-see-it-as-a-big-deal
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-25T13:40:46Z'
published: '2026-09-25T00:00:00Z'
description: Microsoft even said it was by design
categories:
- Technology & Software
image: https://cdn.mos.cms.futurecdn.net/JpXukHGqkZ8gapEzDQNqRW-1920-80.jpg
---

![Concept art representing cybersecurity principles](https://cdn.mos.cms.futurecdn.net/JpXukHGqkZ8gapEzDQNqRW.jpg)

* **Graz University researchers found decades‑old flaws in file‑notification subsystems across Linux, Windows, macOS, and Android**
* **Side‑channel attacks can infer keystrokes, visited websites, or even steal credentials via unprivileged access**
* **Linux shipped partial mitigations (CVE‑2025‑68788); Microsoft and Apple acknowledged but did not patch, demo expected at ACM CCS 2026**

Researchers have found a vulnerability in all major operating systems which could, in certain scenarios, allow threat actors to steal login credentials, or track which websites the target is visiting. OS makers, on the other hand, don’t seem all too phased about it.

The bug is described as a side-channel attack - a type of attack in which threat actors simply observe how the system operates and extract valuable secrets through indirect clues. For example, by monitoring how much power the chip takes at any given moment in time, attackers can observe and extract passwords.

It was discovered by security researchers from Austria’s Graz University of Technology: Sudheendra Raghav Neela, Xufan Zhao, Jeanette Angelika Wultsch, Hannes Weissteiner, Florian Draschbacher, Stefan Gast, and Daniel Gruss.

## Notifying the system

This particular side-channel vulnerability was found in the file-notification subsystem running in pretty much every OS in existence today. The subsystem is built to notify applications when files on a system change. Not what has changed, just that a change occurred. The bug is allegedly quite old, too.

"We found decades-old bugs on [these operating systems], all rooted in the file-notification subsystems that every modern OS ships to inform applications when files change," said Sudheendra Raghav Neela, a doctoral student at TU Graz, in an email to *The Register*.

On Linux, the subsystem is called inotify and it’s been affected since 2005. On Android it’s FileObserver (affected since 2008), and on Windows - ReadDirectoryChangesW - flawed since the year 2000. On MacOS, it’s called FSEvents, vulnerable since 2007.

In the paper, the researchers claim file event information can help attackers conclude what other users on a computer are doing. They can launch an inter-keystroke-timing attack, inferring what users are inputting (both locally and remotely), reveal which websites they visit, and possibly even steal login credentials through UI redress.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The problem stems from the fact that unprivileged users are allowed to access the file notification subsystem. This primarily relates to files that can be read by multiple users, but apparently, there are quite a few files on a system that fall into that category.

## No patch

"On Linux, watching a readable directory leaks events on files inside it you cannot even read: watching /dev/input gives a notification on every keystroke, which we turn into a local inter-keystroke timing attack with a 93.1–100% [keystroke accuracy] score across seven users and a remote (SSH) one at 100%,” Neela said.

The percentage range means the attack won’t work in all cases, which is more-or-less standard with side-channel attacks. They are notoriously difficult to pull off, which is also likely why most OS makers barely flinched at the news.

All of them were notified of the findings roughly a year ago, and most of them never bothered to address it. Linux introduced some mitigations, including CVE-2025-68788, which prevents inotify from generating certain “access” and “modify” events for special files. The fix was shipped to multiple kernels and Linux distros, but it addresses only part of the broader attack techniques that the researchers described.

Microsoft and Apple apparently acknowledged the findings, but apart from that - did very little. Microsoft told the researchers the behavior of ReadDirectoryChangesW was "by-design", although the feature is undocumented. They believe the ability to monitor file paths across users is not a vulnerability worthy of a patch. The report does not mention Apple doing anything about it, either.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png)

![Google logo on a black background next to text reading &#039;Click to follow TechRadar&#039;](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg)
