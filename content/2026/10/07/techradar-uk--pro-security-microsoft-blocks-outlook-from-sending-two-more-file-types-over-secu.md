---
title: Microsoft blocks Outlook from sending two more file types over security concerns
source_url: https://www.techradar.com/pro/security/microsoft-blocks-outlook-from-sending-two-more-file-types-over-security-concerns
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-07T20:40:20Z'
published: '2026-10-07T00:00:00Z'
description: Say goodbye to .msix and .msixbundle files in your email
image: https://cdn.mos.cms.futurecdn.net/89bxEtNaSo2H7h4SqvoeRd-2560-80.jpg
categories:
- Technology & Software
people: []
locations: []
organisations:
- BlockedFileTypes
- MSIX
- MSIXBUNDLE
- Microsoft Store
- OWA
- OwaMailboxPolicy
- TechRadar Pro
- The Register
---

![A phone sitting on a laptop keyboard with the Microsoft Outlook logo on the screen.](https://cdn.mos.cms.futurecdn.net/89bxEtNaSo2H7h4SqvoeRd-1920-80.jpg)

* **Microsoft will block .msix and .msixbundle email attachments in New Outlook and Outlook Web**
* **Change aims to reduce malware delivery through application package files sent via email**
* **Organizations relying on these formats must explicitly allow them before rollout begins**

Users of New Outlook for Windows and Outlook on the Web in Exchange Online will no longer be able to download email attachments of two file types: .msix, and .msixbundle, Microsoft has confirmed, saying it’s for the users’ own safety.

“To enhance security in Outlook on the web and new Outlook for Windows, we are updating the default list of blocked file types in OwaMailboxPolicy,” a newly released advisory reads.

“As part of this update, the .msix and .msixbundle file types will be added to the BlockedFileTypes list in the default OWA Mailbox policy and any custom policies created in your tenant.”

## What are .msix and .msixbundle files?

MSIX is a file format for packaging and installing applications. It is similar to .exe and .msi installer since it contains files and information Windows needs to install an application. Microsoft introduced .msix as a more modern and secure way of distributing software, saying it comes with features that make installing and updating software more reliable.

MSIXBUNDLE is, as the name might suggest, the same but in plural. It can contain several versions of an .msix package in a single file. For example, a developer can bundle versions designed for different processor architectures (x64 and ARM, for example), and Windows will automatically install the correct one. Both formats are commonly used to distribute Windows applications, including apps delivered through the Microsoft Store.

## How big of a deal is this?

Apparently, not that big of a deal. Microsoft itself says that “most organizations are not expected to be affected by this update,” given the fact that these file types are “infrequently used.” However, they seem to be used frequently enough to warrant an update.

“This update is part of our ongoing efforts to strengthen security and help protect organizations from potentially unsafe file attachments,” Microsoft added.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Truth be told, sending application packages as email attachments is hardly the primary way businesses distribute software today. Employees usually do that through managed company portals, the Microsoft Store, package management tools, or direct downloads from software vendors. Therefore, we can assume that the majority of .msix and .msixbundle being sent through email could be malicious and weaponized.

General rollout will begin in early November 2026 and is expected to be complete by mid-November, the advisory reads. Exchange Online administrators who manage OWA mailbox policies are generally affected, as well as those who usually send or receive .msix or .msixbundle attachments in Outlook on the web or new Outlook for Windows Platforms and services. Obviously users of Outlook for the web, New Outlook for Windows, and Exchange Online, too.

So, in roughly a month, these two file types will be added to the BlockedFileTypes list in all OWA Mailbox policies across organizations, including the default policy and any custom policies created across tenants, preventing users from downloading them as attachments, or running them that way, at all.

Organizations that don’t rely on these two file types won’t need to do anything, but those that do should add them to the AllowedFileTypes property of their users’ OwaMailboxPolicy objects prior to rollout.

## Defending email users from themselves

For years now, Microsoft has been adding different file types to the “blacklist”, in an effort to prevent users from downloading and running malicious attachments sent in phishing emails. As The Register reminds, in December 2023, the company disabled ms-appinstaller protocol handler by default, after it was abused to distribute malware.

Since then, Microsoft has also blocked .py (Python files), .ps1 (PowerShell files), and .cab (cabinet files). Some people found it surprising it took Microsoft this long to remember .msix and .msixbundle types, as well.

*Via* * The Register*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
