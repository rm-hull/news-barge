---
title: Windows has fixed an issue with 'Always on VPN' in its latest update — but
  it seems to have brought more issues with it
source_url: https://www.techradar.com/vpn/windows-has-fixed-an-issue-with-always-on-vpn-in-its-latest-update-but-it-seems-to-have-brought-more-issues-with-it
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-15T16:58:31Z'
published: '2026-10-15T00:00:00Z'
description: One step forward…
image: https://cdn.mos.cms.futurecdn.net/zeKbmPE8YTXp5kVggVjN7g-1920-80.jpg
categories:
- Technology & Software
people: []
locations:
- Aruba
- Canada
- Ottawa
organisations:
- Bleeping Computer
- IT
- MS
- Microsoft Learn
- PEAP
- Reddit
- Redditor
- Surfshark
- WiFi
---

![Windows 11](https://cdn.mos.cms.futurecdn.net/zeKbmPE8YTXp5kVggVjN7g-1920-80.jpg)

Microsoft has released a minor Windows update to address connection issues with Always On VPN, with users reporting other fixes as a seemingly unintended consequence.

As Bleeping Computer reports, users reported connection issues with Microsoft’s Always On VPN standard following a Windows update in September 2026. The tech titan has released the KB 5127646 and KB5127648 cumulative updates in order to address the problem.

Always On VPN is a connection standard built into Windows 10, Windows 11, and Windows Server that lets VPNs activate as soon as a user’s computer detects an active internet connection. It’s the underlying technology that allows some of the best VPNs to offer automatic connections on Windows computers.

In an alert shared with IT administrators in September 2026 (via Bleeping Computer), Microsoft acknowledged a bug that caused Always On VPN to fail if the computer couldn’t establish an initial internet connection.

The alert noted that repeated connection attempts could display an error reading “The specified port is already in use”, suggesting that Windows hadn’t been able to recognise a failed connection. The issue affected computers and servers running Windows 11 24H2 or newer.

Naturally, this was a problem for users and organisations who leave their VPN to activate automatically by default. And, though such failures could generate error messages, it’s possible that this bug could’ve left users unprotected against malicious tracking or data harvesting, a particular concern for large organisations.

Microsoft has also given details of a temporary fix for users and organisations that are unable to install the cumulative updates that correct this issue: “IT administrators can mitigate this issue by changing the Always On VPN profile from automatic protocol selection to a single protocol, either SSTP only or IKEv2 only, depending on their environment and configuration.”

## Redditor reports a bonus fix – but others report new issues

![Surfshark VPN apps running on a laptop and mobile during TechRadar&#039;s testing](https://cdn.mos.cms.futurecdn.net/ccTFeYpYzWf33P3oZHcGyC-1200-80.jpg)

According to user reports, it seems that Microsoft’s Always On VPN patch has improved other VPN connections, though it's unclear whether this was intentional or an unintended bonus.

Reddit user Canada\_Ottawa shared that their Surfshark connection had improved in both speed and stability overnight after installing the MS Tuesday, 2026 10 13 Windows 11 update.

The user said that their VPN connection had been unstable for “about two months” prior to this patch, especially when waking their computer from Sleep mode.

On the flip side, other online users have shared their frustration at *new* issues arising with the most recent Windows patch.

User ephycalyptus said that they could no longer connect to their company WiFi after the update, noting that the network uses Aruba access points. Commenters have suggested the update has affected 802.1x PEAP connections and NTLMv1 authentication protocols.

A forum post on Microsoft Learn suggests similar issues. User Supply-PWC writes: “After installing KB5127648, Windows 11 clients can no longer authenticate to our WPA2-Enterprise (802.1X/PEAP) wireless network. Authentication starts but never completes [...] The issue reproduces across multiple hardware vendors and wireless chipsets.”

Overall, it seems that Microsoft has fixed one problem only to set off another. We’ll be on the lookout for updates from the firm itself in the coming days.
