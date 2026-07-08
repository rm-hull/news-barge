---
title: Hidden backdoor in Tenda routers goes unpatched as company ignores warnings
  from cybersecurity researchers — Chinese company's firmware allows admin access
  without a password
source_url: https://www.tomshardware.com/tech-industry/cyber-security/hidden-backdoor-found-in-tenda-routers-goes-unpatched-despite-warnings-from-cybersecurity-researchers-affected-firmware-allows-admin-access-without-a-password
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-08T17:49:59Z'
published: '2026-07-08T00:00:00Z'
description: Firmware vulnerability affects several router models
image: https://cdn.mos.cms.futurecdn.net/uX8ghCJT8DyjkPQPLQVehC-2041-80.jpg
---

![Router sitting on a table.](https://cdn.mos.cms.futurecdn.net/uX8ghCJT8DyjkPQPLQVehC.jpg) 

The CERT Coordination Center (CERT/CC), a U.S. government-backed cybersecurity group at Carnegie Mellon University's Software Engineering Institute, disclosed a firmware flaw on July 6 that can hand attackers full administrative control over several Tenda networking devices. The vulnerability, tracked as CVE-2026-11405, is an undocumented authentication backdoor in the affected models' firmware that bypasses the normal login process and grants access to the devices' web management interface without valid credentials. Compounding the risk, there is currently no security patch available, as Tenda — a Shenzhen-based budget networking brand with a large presence in India and other markets — is yet to respond despite CERT/CC reaching out on the issue.

CERT/CC lists five affected firmware versions spanning the FH1201, W15E, AC10, AC5, and AC6 router families. The advisory, which credits an anonymous researcher for the finding, does not describe this list as exhaustive. The list covers only the specific builds the researcher reported to CERT/CC, as there is no vendor-confirmed scope. According to the advisory, the flaw resides inside the routers' built-in web server, where an undocumented authentication routine allows administrative access without requiring the configured administrator credentials.

Like most consumer routers, Tenda devices provide a password-protected web management interface for configuring Wi-Fi settings, firewall rules, DNS servers, firmware updates, port forwarding, parental controls, and other core networking features. Because these interfaces control most aspects of a router's operation, they are typically protected by authentication mechanisms designed to prevent unauthorized users from making changes that could compromise an entire home or business network.

According to the advisory, the affected firmware initially performs authentication as expected, verifying the administrator password with a standard MD5-based check. However, when that verification fails, the login routine quietly follows a second, undocumented code path. Instead of immediately rejecting the login attempt, the firmware retrieves another password stored internally under the configuration key sys.rzadmin.password and compares it directly against the user-supplied password using the standard C library function strcmp().

If the supplied password matches this hidden value, the firmware immediately creates a valid administrator session with full privileges. Even more concerning, the associated username is never validated, meaning any username can be used as long as the hidden password is supplied. As a result, the mechanism effectively bypasses the router's configured administrator account altogether.

While CERT/CC did not disclose the hidden password itself, the existence of an undocumented secondary authentication path significantly weakens the security model of affected devices. Unlike conventional authentication vulnerabilities that stem from implementation errors, this is a separate login path rather than a flaw in the existing one, granting administrative access through credentials that are neither documented nor exposed through the router's management interface. Whether that path was placed there deliberately or left in as a forgotten development feature is unclear. CERT/CC draws no conclusion on intent, and Tenda's silence settles nothing.

Successful exploitation grants an attacker unrestricted control over the router's configuration. With administrator access, an attacker could modify network settings, change DNS servers to redirect internet traffic, disable security protections, replace administrator credentials, or enable additional remote access features. As routers serve as the gateway between local devices and the internet, compromising one can expose every connected system on the network to further attacks.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Pending official Tenda firmware updates, CERT/CC recommends disabling remote web management wherever possible to prevent attackers from reaching the administrative interface over the internet. The organization also advises limiting local network exposure, noting that while changing a router's default LAN IP address may reduce opportunistic discovery by automated scanning tools, it does not protect against determined attackers performing targeted network reconnaissance.

The disclosure echoes the concerns the Federal Communications Commission (FCC) cited when it added certain foreign-made networking products to its Covered List in March, preventing new models from receiving the authorization required for import and sale in the U.S. The FCC argued that compromised consumer routers can provide attackers with a foothold into home and small-business networks. An undocumented administrator backdoor in widely sold networking equipment — combined with the absence of a vendor patch or response — illustrates the type of supply-chain security risk regulators seek to address.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Etiido Uko](https://cdn.mos.cms.futurecdn.net/BBrMt7jWtSo2Dc3iKoroyD.jpg)

Etiido Uko is a news contributor for Tom's Hardware covering the latest updates in big tech and the PC industry. He is a mechanical engineer and senior technical writer with over nine years of experience in documentation and reporting. He is deeply passionate about all things engineering and technology, and is an expert in gadgets, manufacturing, robotics, automotive, and aerospace.
