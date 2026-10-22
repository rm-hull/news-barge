---
title: Microsoft admits its Windows update to fix 'Always on VPN' issue didn't actually
  work
source_url: https://www.techradar.com/vpn/vpn-privacy-security/microsoft-admits-its-windows-update-to-fix-always-on-vpn-issue-didnt-actually-work
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-22T17:15:02Z'
published: '2026-10-22T00:00:00Z'
description: IT admins are stuck with temporary workarounds as the tech giant admits
  the bug was "mistakenly updated to Resolved status."
image: https://cdn.mos.cms.futurecdn.net/vUENLgpmE9SAJMUqFSigSF-2000-80.jpg
categories:
- Technology & Software
- Careers & Productivity
people: []
locations: []
organisations:
- IT
- Microsoft
- Microsoft's
- VPN
---

![Windows 11 on a laptop](https://cdn.mos.cms.futurecdn.net/vUENLgpmE9SAJMUqFSigSF-1920-80.jpg)

* **Microsoft has confirmed that the Windows 11 'Always On VPN' connection issues introduced in September remain unfixed.**
* **The tech giant admitted the bug was mistakenly flagged as resolved in the October 13 patch.**
* **IT admins must continue pinning VPN profiles to a single protocol until a permanent fix arrives in the coming weeks.**

Microsoft’s October Patch Tuesday was supposed to mark the end of a highly frustrating month for Windows 11 users relying on Always On VPN. However, the company has now walked back its initial claims, admitting that the highly anticipated fix was a total failure.

In a service bulletin sent to IT administrators this week, Microsoft confirmed that the nasty glitch, which leaves enterprise VPN connections hanging indefinitely or entirely unable to connect, remains fully active.

The issue was originally introduced during the September 2026 security updates and continues to wreak havoc across enterprise networks that depend on secure remote access.

With the bug still running rampant, users relying on the best VPN services for seamless remote work will have to make do with Microsoft's suggested temporary workarounds.

A permanent fix is reportedly still several weeks away, leaving network administrators in a precarious position.

## An unresolved headache

The problem primarily affects users utilizing Microsoft's native Always On VPN technology with automatic protocol selection configured. Always On VPN is a critical remote access tool designed to build an encrypted link back to corporate networks quietly in the background.

Trouble starts when an initial connection attempt fails. The system tries to fall back to a secondary method, automatically switching between IKEv2 and SSTP protocols.

Right now, this fallback process is entirely broken. Affected clients will simply hang at a "Connecting" status or flat-out fail to get through. In some instances, subsequent retry attempts will throw an error reading, “The specified port is already in use.”

We previously reported that the KB5127648 and KB5127646 cumulative updates released on October 13 had supposedly cured the fault, while simultaneously introducing bizarre new Wi-Fi authentication issues. Now, it appears those updates failed to deliver on the VPN front altogether.

As reported by *The Register*, the tech giant has been forced to confess its error. Microsoft explained to administrators that the bug had been “mistakenly updated to Resolved status on October 13, 2026.” The company’s official KB5127648 support page has since been scrubbed of any mention of the VPN repair, with the changelog now quietly noting that the fix will be included in a later release.

## Temporary mitigation

For now, Microsoft has downgraded the bug's status from "Resolved" back to "Mitigated," apologizing to IT admins for the confusion.

According to early reports, a permanent repair is slated for an upcoming update that Microsoft expects to ship within the next several weeks.Until that release lands, IT administrators simply cannot treat the October Patch Tuesday builds as a cure.

The sole safeguard currently available is to restrict affected Always On VPN profiles to a single protocol. By manually pinning the connection to either SSTP or IKEv2 and disabling the auto-fallback feature, administrators can prevent the bug from triggering in the first place.

*The Register* notes that, “The issue affects Windows 11 versions from 24H2 through 26H2.” If your organization relies heavily on these recent builds for remote connectivity, your IT department will need to ensure this temporary mitigation remains firmly in place until Microsoft can successfully deploy a working patch.

Sign up for breaking news, reviews, opinion, top tech deals, and more.
