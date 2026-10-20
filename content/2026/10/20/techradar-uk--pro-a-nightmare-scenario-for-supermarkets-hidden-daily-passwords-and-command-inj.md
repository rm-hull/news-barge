---
title: Thousands of Danfoss supermarket refrigeration systems exposed online
source_url: https://www.techradar.com/pro/a-nightmare-scenario-for-supermarkets-hidden-daily-passwords-and-command-injection-flaws-leave-thousands-of-danfoss-supermarket-systems-open-to-remote-takeover
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-20T23:50:56Z'
published: '2026-10-20T00:00:00Z'
description: Hackers could spoil supermarket food supplies by hijacking the supermarket’s
  cooling systems
image: https://cdn.mos.cms.futurecdn.net/7XwhMHsBzdFcrGh5tBDhsf-1920-80.jpg
categories:
- Technology & Software
- Food & Cooking
- Business & Entrepreneurship
people: []
locations: []
organisations:
- AK-SM
- Claroty’s Team82
- Danfoss
- Nginx
- TechRadar Pro
---

![password manager example](https://cdn.mos.cms.futurecdn.net/7XwhMHsBzdFcrGh5tBDhsf-1920-80.jpg)

* **Thousands of Danfoss refrigeration controllers were discoverable through public internet scanning**
* **A hidden daily code could bypass normal administrator password verification**
* **An email configuration flaw could enable operating system command execution**

Thousands of Danfoss refrigeration management systems may face remote attacks after researchers uncovered authentication weaknesses and dangerous software flaws.

Security researchers at Claroty’s Team82 used Censys, a cybersecurity platform, to identify 2,765 publicly accessible systems.

Their investigation identified three vulnerabilities affecting the AK-SM 800A controller, which manages refrigeration equipment in supermarkets, warehouses and cold storage facilities.

## Hidden passwords expose refrigeration management systems

The AK-SM 800A provides centralized monitoring and configuration of refrigeration equipment, including temperature settings, operating schedules, alarms, and notification services.

Its browser accessible management interface allows technicians to maintain installations remotely, but internet exposure can also give attackers direct access to vulnerable systems.

Team82 discovered an undocumented authentication mechanism that could allow attackers to circumvent the administrator password through a daily generated access code.

Designated CVE-2025-41450, the flaw involves an alternative verification process that checks a specially constructed credential against a value generated using the device’s current date.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Researchers reconstructed the algorithm responsible for generating this code by examining the controller’s firmware and authentication routines.

Anyone able to reproduce the algorithm could potentially obtain administrative access without knowing the legitimate password configured on the affected device.

That access could expose configuration settings and management functions normally reserved for authorized personnel.

The consequences extend beyond unauthorized account access because refrigeration controllers help operators maintain conditions required for preserving perishable products.

A second vulnerability, CVE-2025-41451, allows command injection through the controller’s email configuration functionality.

Researchers found that an email authentication password entered through the management interface could be incorporated into an operating system command without adequate sanitization.

Malicious input could therefore introduce additional shell commands, potentially enabling remote code execution after authentication.

Combined with the hidden daily password mechanism, this weakness could provide an attacker with a route from unauthorized login to execution of commands on the controller.

## Configuration flaws threaten system availability

The investigation also identified CVE-2025-41452, which affects the controller’s externally accessible Nginx web server configuration.

Researchers discovered that an authenticated function could replace the headers.conf file and reload the server configuration without restarting the device.

An attacker with the necessary access could insert unauthorized routing directives, changing how the web server processes requests.

Team82 also found that requests reaching a maliciously configured route could trigger an unhandled exception in the sm\_app process, disrupting the management interface.

Repeatedly triggering this failure could cause a denial of service, preventing legitimate operators from accessing the controller’s web management functions.

Such disruption could complicate monitoring and maintenance, although the researchers did not establish that every attack would cause refrigeration equipment to stop operating.

Claroty’s Team82 reported the vulnerabilities privately to Danfoss through coordinated disclosure, and the manufacturer released firmware version R4.3.1 to address the identified weaknesses.

Operators using affected AK-SM 800A controllers should upgrade to version R4.3.1 or later and restrict administrative interfaces to trusted management networks or protected VPN connections.
