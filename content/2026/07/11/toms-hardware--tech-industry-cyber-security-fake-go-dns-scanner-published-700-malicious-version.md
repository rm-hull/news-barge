---
title: Fake Go DNS scanner spread malware through over 200 GitHub repos — 'Operation
  Muck and Load' has published 700 malicious modules since January
source_url: https://www.tomshardware.com/tech-industry/cyber-security/fake-go-dns-scanner-published-700-malicious-versions-before-researchers-traced-it-to-222-github-repos
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-11T13:47:43Z'
published: '2026-07-11T00:00:00Z'
description: Socket traced the module to 222 repos across 190 accounts staging Vidar,
  RATs, and XMRig miners, with encrypted payload locations hidden on Pastebin, Telegram,
  and YouTube.
image: https://cdn.mos.cms.futurecdn.net/2Z9rxwcvZrC34RGiyKN9Tj-1920-80.png
---

![GitHub](https://cdn.mos.cms.futurecdn.net/2Z9rxwcvZrC34RGiyKN9Tj.png) 

Supply-chain security firm Socket has __published research findings__ describing a Go module that posed as a DNS and subdomain scanner while acting as a first-stage Windows malware loader. The firm then traced it to a network of 222 GitHub repositories across 190 accounts. The module published its first version on January 24 this year and has since accumulated more than 1,200 versions, over 700 of them malicious. Socket tracks the campaign as “Operation Muck and Load” and reported the module to the Go security team, which blocked it from the Go module proxy.

 ![Microsoft data center in Mount Pleasant, Wisconsin](https://cdn.mos.cms.futurecdn.net/Vh4nY3pMCcmra2ymXah9S7.jpg) 


Go derives a pseudo-version from the commit timestamp and hash for any commit that lacks a semantic version tag. Socket attributes the sprawl to the threat actor's own GitHub Actions workflow, saying its timed commits could each be resolved as a version, inflating a scanner utility's release history into the hundreds.

Across the confirmed repositories, Socket found the same workflow: it sets the Git email to [ischhfd83@rambler.ru](mailto:ischhfd83@rambler.ru), sets the visible commit username to the current repository owner, and then force-pushes a rewritten log file every minute. That split generated owner-attributed activity across disposable accounts while leaving one reusable fingerprint. Socket counted a repository only when both the email and the workflow appeared together, resulting in 222 repositories as the confirmed minimum.

The module's main.go launches a hidden PowerShell command that downloads content from muckcoding.com, decodes it with certutil, and runs the result with execution-policy bypass. Socket describes the decoded script as a multi-layer loader using Base64 encoding and XOR decryption, with a Turkish-language comment in one layer that translates to "run directly, no other step is needed."

Rather than hardcoding a payload URL, the resolver retrieves text from public platforms, searches it for the marker string "LastW," then decrypts the trailing blob with a hardcoded key to recover the actual download location. Primary dead drops include Pastebin and a paste service called Rlim, with fallbacks across YouTube, Instagram, Telegram, Google Docs, and GitCode. If defenders remove one paste or block the final archive URL, the actor can update the resolver content without touching the first-stage loader.

The resolved URL points to a password-protected 7-Zip archive hosted as a GitHub release asset. The loader extracts it into a directory named to resemble a legitimate Microsoft Photos install and launches Microsoft.exe from that path with a hidden window. Decoded payload stages map to AsyncRAT, Quasar, and Remcos-style RAT detections alongside infostealer behavior.

Socket confirmed at least 14 unique malware files across the analyzed set, including Trojan loaders and downloaders, __Vidar infostealer__, dropper and spyware payloads, and XMRig-related Monero cryptominers. One Loader.exe appeared byte-identically across four separate repositories.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Lure themes span MetaMask and Trust Wallet integrations, seed-phrase utilities, Binance and PayPal automation, Telegram and Discord bots, and game cheats for PUBG, Valorant, and Escape from Tarkov. One PUBG repository, nrevv1lad/Pubg-DESYNC-Menu, presented itself as an external cheat with an installation guide while hosting a Vidar-linked Loader.exe in its source tree.

Socket assesses with high confidence that Operation Muck and Load belongs to the same cluster that Sophos documented in June last year. Sophos researchers Matt Wixey and Andrew O'Donnell traced 141 GitHub repositories, 133 of them backdoored, to the same [ischhfd83@rambler.ru](mailto:ischhfd83@rambler.ru) address. Sophos also identified "Muck" as one of the actor's aliases, a label now embedded in the muckcoding.com and muckdeveloper.com domains.

Neither GitHub nor the Go team has commented beyond the proxy block.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Luke James](https://cdn.mos.cms.futurecdn.net/C4FAi2KzwaGLUrBqzX5aBM.png)

Luke James is a freelance writer and journalist. Although his background is in legal, he has a personal interest in all things tech, especially hardware and microelectronics, and anything regulatory.
