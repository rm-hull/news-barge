---
title: Malicious VPN config files can let attackers run commands on Asus routers —
  company’s patch also fixes a bug that lets a logged-in attacker switch on Telnet
  with root access
source_url: https://www.tomshardware.com/tech-industry/cyber-security/malicious-vpn-config-files-can-let-attackers-run-commands-on-asus-routers-companys-patch-also-fixes-a-bug-that-lets-a-logged-in-attacker-switch-on-telnet-with-root-access
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-03T15:20:00Z'
published: '2026-10-03T00:00:00Z'
description: Asus rates the VPN-file flaw as critical, scoring at 9.4 out of 10 on
  CVSS 4.0.
image: https://cdn.mos.cms.futurecdn.net/6mmVqfQjXAQVMLwxBZ5SQV-617-80.jpg
categories:
- Technology & Software
- Hardware
people:
- Shane Downing
- Tom
locations: []
organisations:
- Asus
- Google News
- Shane Downing
- Tom’s Hardware
- VPN
- VulnCheck
---

![An Asus RT-BE92U router with four antennas on wooden furniture, next to a lamp and some books](https://cdn.mos.cms.futurecdn.net/6mmVqfQjXAQVMLwxBZ5SQV-617-80.jpg)

A “crafted VPN client configuration file” uploaded by the user or a logged-in attacker via an Asus router’s web management interface can allow an adversary to “execute arbitrary commands,” a critical security risk the company has acted to patch. A second, separate bug, which uses debug code left active, allows the attacker to bypass security checks in order to enable Telnet and may allow commands to be run “with root privileges,” potentially affecting devices connected to the router.

Asus recommends that users “only import VPN client configuration files from trusted sources.” The two CVEs, CVE-2026-14157 and CVE-2026-13313, score 9.4 and 8.9 out of 10 on the Common Vulnerability Scoring System (CVSS) 4.0 scale, which measures vulnerability severity. Asus names firmware series rather than models: 3.0.0.6\_102 for both bugs, with the 3.0.0.4\_386 and 3.0.0.4\_388 series also affected by the Telnet one.

The routers can act as a VPN client when set up with a configuration file from a VPN provider. Things go wrong when crafted text inside the uploaded files is read as formatting instructions rather than plain data. VPNs are commonly used to bypass filters and access otherwise unreachable content, but the risk here applies to owners who import VPN configuration files into the router itself, not to VPN apps on a laptop or phone.

The separate Telnet flaw relies on enabling the service first before running commands that could impact the network. Besides the firmware update, Asus recommends a strong, unique admin password with “at least 10 characters, with a mix of uppercase letters, numbers, and symbols.” To reduce risk in the meantime, Asus also advises against running “scripts, tools, or commands from untrusted sources on any device within your local network.” One risk is that “attackers may use social engineering to trick administrators,” the company says.

The VPN bug uses the same entry point as one disclosed by VulnCheck in 2024, CVE-2024-0401, which used a crafted OVPN profile. That makes Asus’s config file import, specifically through the web admin page, a recurring weak point. As a popular brand, Asus is also a likely target. The AyySSHush campaign utilized authentication bypasses, brute-force logins, and a command-injection flaw (CVE-2023-39780) to backdoor over 9,000 routers, as we reported at the time. The backdoor was even able to survive firmware updates.

With the two router fixes came one for 13 motherboards, where a “physically proximate attacker” could “read or write arbitrary system memory by inserting a specially crafted device.” This flaw impacts many of Asus’s Z390 and C246 motherboards and is rated high severity at 7.0 out of 10, lower than the router flaws. It also requires physical access.

If you are at risk or potentially at risk, find the firmware update on Asus’s support page or your product’s page. For the affected motherboards, the fix is BIOS version 1502 for the WS Z390 Pro and 2203 for the other 12 boards. Routers that have reached end of life will not receive new firmware. For those, Asus advises the user to use strong, unique login and Wi-Fi passwords.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Shane Downing](https://cdn.mos.cms.futurecdn.net/Zosi9VrDytS9FkgJiHvc69-140-80.png)

Shane Downing is a Contributing Writer for Tom’s Hardware, covering consumer storage, PC hardware, and AI.
