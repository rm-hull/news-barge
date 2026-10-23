---
title: A whole load of severe Linux kernel vulnerabilities has just been made public
source_url: https://www.pcgamer.com/hardware/a-public-outing-of-severe-and-unfixed-linux-kernel-vulnerabilities-should-have-you-thinking-of-updating-your-steamos-or-other-distros-to-beta-branches/
source_site: PC Gamer
source_slug: pcgamer
scraped_at: '2026-10-23T11:37:57Z'
published: '2026-10-23T00:00:00Z'
description: The accidental reveal of unpatched vulnerabilities as high as 9 on the
  CVSS score chart is a little worrisome.
image: https://cdn.mos.cms.futurecdn.net/7EimC87J9aoLbZEbfWBX9H-1280-80.jpg
categories:
- Technology & Software
people:
- Greg Kroah-Hartman
- Michael Larabel
locations: []
organisations:
- Linux
- Phoronix
- Trend Micro
---

![https://pixabay.com/photos/linux-laptop-screen-wallpaper-wood-1962898/](https://cdn.mos.cms.futurecdn.net/7EimC87J9aoLbZEbfWBX9H-1280-80.jpg)

If you're an enlightened sort, who has sought out the sunny uplands of a Linux operating system for your gaming rig in these exciting days of almost seamless game compatibility, then you might want to have a think about migrating your OS onto a beta branch for a while. A list of as-yet unpatched Linux kernel vulnerabilities has been sent out to a public mailing list by accident, and some of these issues score as high as 9 on the CVSS security-scare-o-meter.

The incident was reported by Phoronix yesterday, where Michael Larabel noted that overnight several new vulnerability reports had gone to a public rather than private security mailing list. The reports had seemingly come from Trend Micro's Zero Day Initiative—an initiative set up to promote extended vulnerability reporting (.pdf warning) with a bug bounty system extending to a group of external researchers.

I guess sometimes a group can be *too* extended.

Anyways, the list of vulnerabilities was jumped on by what Phoronix calls Linux's second-in-command, Greg Kroah-Hartman, who maintains the stable branch of the kernel. Kroah-Hartman responded to each of the reports individually asking them to fix their submission process.

Mostly because none of these vulnerabilities have been patched on the main kernel yet, and remain open to attack. And those attack vectors have just been made public. Eep. The more positive news, however, is that some of the cases are undergoing testing or are at least queued in beta or '-next' branches.

So there is a chance that your chosen distro might have those patches in place for the security conscious if you opt-in to a beta branch for an update. Worth a check, eh?

Phoronix lists these vulnerabilities as:

* **ZDI-CAN-33549 as a CVSS 9.0 scored vulnerability for SMB Direct remote code execution vulnerability due to integer underflow. For this one there is a patch in a Git branch of code intended for Linux v7.5 but now presumably will be expedited for getting to mainline.**
* **ZDI-CAN-33774 as a KSMBD race condition that can lead to remote code execution. Another CVSS 9.0 rated vulnerability.**
* **ZDI-CAN-33367 is a vulnerability for skbuff skb\_zerocopy in the network code that can lead to local privilege escalation. For this one Linux kernel developers received a security report from another source last week over the same issue and a patch is expected to be posted soon.**
* **ZDI-CAN-34068 as a VMWGFX VMware graphics driver bug with an out-of-bounds write leading to local privilege escalation.**
* **ZDI-CAN-34076 an uninitialized resource in the NVMET code leading to information disclosure.**
* **ZDI-CAN-32005 was also posted to the mailing list a day prior for a search-domain TCP query stack buffer overflow leading to local privilege escalation.**

![AMD Ryzen 9 9800X3D processor](https://cdn.mos.cms.futurecdn.net/5ryUJb6snbbQMdpHJu7i8W-140-80.jpg)
