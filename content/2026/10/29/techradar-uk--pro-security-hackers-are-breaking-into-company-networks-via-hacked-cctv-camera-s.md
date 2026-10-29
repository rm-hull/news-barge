---
title: Hackers are breaking into company networks via hacked CCTV camera software
source_url: https://www.techradar.com/pro/security/hackers-are-breaking-into-company-networks-via-hacked-cctv-camera-software
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-29T18:34:30Z'
published: '2026-10-29T00:00:00Z'
description: Companies urged to treat cameras and their management platforms as potential
  entry points
image: https://cdn.mos.cms.futurecdn.net/orPkbTPEcv9Z2g5J2ATLYX-2560-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Harlan Carvey
- Huntress
- Lindsey O'Donnell-Welch
locations: []
organisations:
- 3R Global
- CMS
- Huntress
- TechRadar Pro
---

![cctv](https://cdn.mos.cms.futurecdn.net/orPkbTPEcv9Z2g5J2ATLYX-1920-80.jpg)

* **Attackers abused camera management software to gain initial access and establish persistence on networks**
* **Campaign used DLL sideloading and reverse shells to evade detection and maintain control**
* **Researchers urge treating camera systems as security-sensitive assets and monitoring them for abnormal activity**

Security researchers have warned of an ongoing campaign targeting an apparent vulnerability in camera management software. The vulnerability is being used for initial access, allowing threat actors to establish a foothold on company infrastructure.

The warning bells were sounded by security outfit Huntress, whose researchers Harlan Carvey and Lindsey O'Donnell-Welch said that in September and October 2026, they observed a “handful of incidents” originating from camera management software.

In all cases the attackers abused a legitimate camera management system to side-load a malicious DLL file and gain access to the underlying system.

## Who watches the watchmen?

Surprisingly, the team could not determine which camera software was being targeted, nor by whom.

“Huntress analysts were unable to determine the full name or creator/vendor of the software, as the file did not contain an embedded File Version Information section,” they said.

However, they did find an executable containing a few notable strings, which led them to believe a Korean company called 3R Global could be involved. They couldn’t confidently say that the Camera Management System (CMS) executable was downloaded from that company’s website, though.

Unfortunately, without knowing the exact name of the software being targeted, it is impossible to tell how many victims there were, or how big the attack surface is. Huntress’ “handful” designation does very little to explain just how dangerous this vulnerability is.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

While the lack of key data limited their visibility into exactly how the threat actors were compromising the software, they could see what they were doing once they were inside - launching a reverse shell and side-loading malicious DLLs.

Once the initial access had been established, the attackers would drop a file named rs.win32.exe to the endpoint and would launch it via a command line. The command line would supply a remote IP address and port, and include an admin username.”This led us to see this as a reverse shell,” they said.

From there, they would drop a file called WpcMon.exe - a legitimate Microsoft Windows Parental Control Monitor file, used for parental-control and activity-monitoring features. In this case, however, the file is used to load malicious DLLs called IPHLPAPI.DLL and samcli.dll. On the surface, both appear to be legitimate zlib compression libraries, but in fact, they were changed to provide beaconing, contacting the external C2 server from time to time.

## Huntress watches the watchmen watching the watchmen

“Part of the infection process also included creating persistence by adding a reference to the newly installed WpcMon.exe in a value beneath the user's Run key,” the researchers explained. “Threat actors typically add a program path to a user's Run registry key so Windows automatically launches their payload whenever that user signs in.”

Side-loading malicious DLL files is a popular infection technique. Instead of deploying an obviously malicious program (which might get flagged by antivirus products), the attackers drop a DLL file containing weaponized code, and then get a legitimate program (such as the parental control software) to run it. Since the process starts with a legitimate executable, it is more difficult to identify as malicious.

It does not guarantee evasion of security software, though.

Defenders should treat cameras and their management platforms as potential entry points into the broader business environment, Huntress warned. They should inventory the software, restrict its access, and monitor for unusual processes and outbound connections.

The researchers also advise defenders to use application control to prevent unapproved executables and DLLs from running in user-writeable paths, and to investigate the sequence of CMS.exe, rs.win32.exe, abnormal WpcMon.exe, and unapproved outbound connections.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
