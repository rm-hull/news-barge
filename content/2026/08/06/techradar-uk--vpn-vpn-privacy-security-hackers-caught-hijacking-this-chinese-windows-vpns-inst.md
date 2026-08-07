---
title: Hackers caught hijacking this Chinese Windows VPN's installers to spread malware
source_url: https://www.techradar.com/vpn/vpn-privacy-security/hackers-caught-hijacking-this-chinese-windows-vpns-installers-to-spread-malware
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-07T00:55:46Z'
published: '2026-08-06T00:00:00Z'
description: QuickFox Windows installers found to be secretly dropping a persistent
  backdoor to spy on specific business and crypto users
image: https://cdn.mos.cms.futurecdn.net/EEXAxCUDKAq3frELz3rVYY-1920-80.jpg
---

![A group of hackers all wearing black with hoods pulled up over their heads with an open laptop in front of them. The background is a Chinese flag](https://cdn.mos.cms.futurecdn.net/EEXAxCUDKAq3frELz3rVYY.jpg) 

- **Fortinet experts found malicious code in QuickFox VPN's Windows installer**
- **The attack actively avoided personal gaming computers**
- **QuickFox has since removed the malicious components from version 3.59.6**

Cybersecurity researchers have uncovered a severe supply chain attack targeting QuickFox, a popular Chinese Windows VPN application.

According to a new report from Fortinet’s FortiGuard Labs, attackers trojanized the software's installers for over a year to quietly deploy malicious backdoor implants onto users' machines.

As Fortinet's experts explain, QuickFox "is a VPN proxy and game accelerator typically employed by Chinese users to speed up access to Chinese-based resources, often to improve video game user experience."

However, experts found that malicious actors altered the application's underlying code to deliver a highly targeted malware campaign. The threat actors modified an HTML file within the app's installer to automatically download and execute malicious JavaScript.

To avoid raising suspicion, this malicious code was pulled from a fake domain intentionally registered to mimic QuickFox’s legitimate infrastructure. Fortinet notes that the campaign had been active since at least August 2025, with QuickFox removing the malicious code with version 3.59.6.

TechRadar has not independently verified Fortinet's findings, but we have reached out to QuickFox for comment and will update this article if we receive a reply.

## A highly targeted backdoor

 ![QuickFox's app logo](https://cdn.mos.cms.futurecdn.net/sdg89w5jqoix37UtxDByia.png) 


The malware didn't infect everyone who downloaded the compromised VPN software. Instead, it used clever guardrails to filter out standard consumers.

If the malicious script detected Steam — the popular distribution service for online games — running on the victim's device, it immediately stopped the infection process to avoid personal gaming computers.

However, if it found tools used by developers, IT administrators, or cryptocurrency users, such as Visual Studio Code, Telegram, or various cryptocurrency wallets, it proceeded with the attack. This behavior suggests the hackers were explicitly hunting for high-value corporate environments and professionals rather than casual gamers.

When a target was deemed suitable, the script abused a legitimate Microsoft utility to secretly install the FDMTP implant and inject the malware. This persistent backdoor allowed attackers to collect sensitive system information, including IP addresses, active processes, MAC addresses, and usernames.

Because FDMTP is highly modular, it also enabled the hackers to remotely download and execute additional malicious plugins, granting them long-term access to compromised machines.

While macOS builds contained the modified file, the infection process only executed on Windows endpoints. Android and iOS apps were completely unaffected.

## How to stay safe

While Fortinet researchers have not confidently attributed the attack to a specific group, they noted significant technical crossovers with Twill Typhoon, a known threat actor.

The good news is that the threat now appears to be contained. According to the cybersecurity firm, "QuickFox has removed the described malicious components from their Windows installer from v3.59.6," following responsible disclosure.

If you have used QuickFox on a Windows machine over the last year, you should immediately update to the latest version directly from the vendor and run a full antivirus scan on your system.

Organizations are also advised to check their networks for any unusual activity or unrecognized file transfers originating from QuickFox installations.

*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds. Make sure to click the Follow button!*

![Rene Millman](https://cdn.mos.cms.futurecdn.net/DXDNjzRkphApxN8f5SooCA.png)

Rene Millman is a seasoned technology journalist whose work has appeared in The Guardian, the Financial Times, Computer Weekly, and IT Pro. With over two decades of experience as a reporter and editor, he specializes in making complex topics like cybersecurity, VPNs, and enterprise software accessible and engaging.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
