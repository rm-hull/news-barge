---
title: Hackers build fake desktop apps to trick victims into handing over access
source_url: https://www.techradar.com/pro/security/hackers-build-fake-desktop-apps-to-trick-victims-into-handing-over-access
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-29T05:45:31Z'
published: '2026-09-29T00:00:00Z'
description: Finance and HR departments are being offered tools that don't exist
image: https://cdn.mos.cms.futurecdn.net/wV66hEbpJdAc4iPB7RwtkK-2560-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Allure
locations:
- US
organisations:
- Allure
- American HR
- GitHub Releases
- MSP
- ScreenConnect
- TechRadar Pro
---

![An exclamation mark inside a red warning triangle, surrounded by email symbols, superimposed on someone typing on a laptop](https://cdn.mos.cms.futurecdn.net/wV66hEbpJdAc4iPB7RwtkK-1920-80.jpg)

* **Threat actors spoofed major US HR/payroll platforms with fake desktop clients built via Lovable landing pages**
* **Victims downloaded a modified ScreenConnect build from GitHub, giving attackers hidden, unattended remote access**
* **Campaign shows ~291 downloads; likely targets payroll staff, enabling potential wire fraud through diverted payments**

Cybercriminals are impersonating large American HR and payroll platforms in attacks that are very difficult to spot, new research from Allure has claimed.

Its report revealed how the as-yet unidentified threat actors were found spoofing three major US HR and payroll platforms, likely picked primarily because they offered a cloud-based service accessible through a browser, rather than a standalone desktop app.

The crooks used Lovable (a legitimate AI-powered service for building websites and landing pages with nothing more than prompts, requiring no technical knowledge whatsoever) to create landing pages imitating the legitimate brands, but with a small (yet important) distinction - they offered a desktop client.

## No reference points

Since a legitimate desktop client does not exist, there is nothing to compare the malware to. This, Allure says, makes it very difficult for victims to determine they were being targeted. After all, it would make sense for a major HR and payroll platform to have a desktop app at one point, right?

Those that clicked the download button were served an executable from GitHub Releases, a feature of GitHub that developers use to publish specific, packaged versions of their software. You can think of it as the software equivalent of a product download page. Being a legitimate service (and one frequently used to host software like this), it yet raises no suspicions or red flags.

The executable itself is not malicious either, which is probably the cheekiest part of the attack. As such, it flies under the radar of most antivirus or endpoint protection services and can easily be installed on the device.

## "Legitimate" tools

Well if it’s not malicious, what is it? And what is the risk?

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The program victims end up installing is a variant of ConnectWise’s ScreenConnect, a remote desktop and remote IT support platform used primarily by IT departments and managed service providers (MSP). It is a legitimate tool that allows IT techs to remotely connect to computers and servers, troubleshoot problems, install software and patches, and more.

But because ScreenConnect provides remote, often privileged access to computers, it is an attractive tool for attackers, and is often used in cyberattacks of different nature.

“This build was configured to surreptitiously do the same thing without the user being aware. We extracted the client configuration and the launch parameters. The access mode is set to unattended. The victim-facing indicators are turned off: no “your machine is being controlled” banner, no system-tray icon, no connection balloon,” the researchers said.

In other words, the variant was configured to allow crooks access without notifying the victim in any way.

Allure did not identify the attackers, nor did it discuss the success of the campaign. We don’t know exactly who it targeted (apart that it aims for finance and HR departments), or how many organizations ended up installing ScreenConnect. The researchers said the GitHub downloads page shows 291 downloads, but that doesn’t necessarily have to mean 291 victims, or successful attacks. It is likely that numerous security researchers downloaded the tools, as well as sandboxes, and that many of the victims realized they were attacked before suffering any meaningful damage. Therefore, the actual number of victims is likely significantly smaller.

We also don’t know what the endgame is, although Allure suggests it might be wire fraud:

“Whoever installs it is the person who runs payroll, and unattended access to that machine is a path to diverting or draining an entire company’s payroll,” they said.

“If your company runs a cloud payroll or HR platform, the most useful thing you can do this week is check whether yours actually ships one [desktop client], and tell employees that a download the vendor does not offer is not an upgrade.”

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
