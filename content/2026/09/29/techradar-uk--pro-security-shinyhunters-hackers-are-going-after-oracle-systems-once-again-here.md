---
title: ShinyHunters hackers are going after Oracle systems once again - here's what
  we know
source_url: https://www.techradar.com/pro/security/shinyhunters-hackers-are-going-after-oracle-systems-once-again-heres-what-we-know
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-29T12:58:04Z'
published: '2026-09-29T00:00:00Z'
description: Mitigations are no longer mitigating
image: https://cdn.mos.cms.futurecdn.net/37uyEphcLreEFNUVCQzurn-2560-80.jpg
categories:
- Technology & Software
people:
- Mandiant
locations: []
organisations:
- CISA
- EMHub
- Environment Management Hub
- GTIG
- Google
- Google’s Threat Intelligence Group
- KEV
- Mandiant
- Oracle PeopleSoft
- Oracle Security Alert
- PSEMHUB
- PeopleSoft Environment Management Hub
- ShinyHunters
- TechRadar Pro
- UNC6240
- US Cybersecurity and Infrastructure Security Agency
- WAF
---

![World Password Day 2025](https://cdn.mos.cms.futurecdn.net/37uyEphcLreEFNUVCQzurn-1920-80.jpg)

* **ShinyHunters bypass PeopleSoft mitigation rules, reviving exploitation of a critical zero-day vulnerability**
* **The campaign has expanded globally, targeting organizations across technology, healthcare, government, and other sectors**
* **Oracle’s original patch remains effective, while organizations should investigate systems and rotate potentially exposed credentials**

ShinyHunters have found a way to bypass a mitigation for a zero-day they previously exploited - so now, not only are they back to abusing the same bug, they’ve even expanded their scope to target a much larger pool of organizations.

In June 2026, it was reported that ShinyHunters, the infamous data extortionists, found a Java deserialization vulnerability in Oracle’s PeopleSoft Environment Management Hub (PSEMHUB) servlet that allowed them to achieve web shell deployment or fileless command execution on vulnerable servers.

Oracle PeopleSoft is a suite of enterprise business software used mainly by large organizations, universities, governments, and corporations to manage things like human resources, finance, supply chain, and student administration.

This remote code execution (RCE) bug caused by unsafe deserialization of Java objects in PSEMHUB was exploited for days, targeting higher education institutions, stealing their sensitive files, and enabling extortion campaigns.

Oracle fixed the issue on June 10 2026, bringing the tool to versions 8.61 and 8.62. The bug was assigned an identifier CVE-2026-35273 and was given a severity score of 9.8/10 (critical). The US Cybersecurity and Infrastructure Security Agency (CISA) added the bug to its Known Exploited Vulnerabilities (KEV) catalog on June 12, giving federal agencies a three-day deadline to patch up.

## ShinyHunters Return

The company also provided mitigation measures for organizations that were unable to install the patch at the time. However, Mandiant and Google’s Threat Intelligence Group (GTIG) are now reporting that ShinyHunters found a way to bypass these mitigations, and are back to exploiting the flaw against organizations running unpatched versions of the software.

“This new wave of activity stems from UNC6240 modifying its exploit to bypass web application firewall (WAF) rules blocking the vulnerable Environment Management Hub (PSEMHUB) endpoint,” the two organizations said in a new report, stressing that the campaign has now expanded globally.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

“The threat actor bypassed these string-based WAF rules by URL-encoding a single character in the request path, requesting /%50SEMHUB/ in place of /PSEMHUB/,” the researchers said. “Many WAF and reverse proxy rules match the literal path before URL decoding, while the PeopleSoft application server decodes the request and routes it to the vulnerable servlet. This allows the threat actor to reach the endpoint on systems whose operators may have believed their WAF rules had mitigated the exposure.”

At first, ShinyHunters were focused mostly on higher education institutions. This time around, though, they’re casting a much wider net, deploying web shells on “dozens of systems globally” including technology, IT services, healthcare, agriculture, transportation, and government.

“Mandiant recommends that organizations running Oracle PeopleSoft take the following immediate actions,” the researchers added.

ShinyHunters are known extortionists. They are using the PeopleSoft vulnerability to gain persistent access and steal credentials, allowing them to move laterally through target environments and exfiltrate sensitive data such as HR or payroll.

## Patching works

The good news is that the patch still works. If an organization applied Oracle’s fix for CVE-2026-35273, this WAF bypass should not matter, because it only works around the mitigation, not the underlying vulnerability fix. Therefore, both Google and Mandiant advise, first and foremost, that organizations apply the Oracle Security Alert issued when the zero-day was first disclosed.

Businesses should also disable the Environment Management Hub (EMHub) service in multi-server configurations, or remove the PSEMHUB application entirely, in single-server configurations.

To check whether they were targeted or not, they should search PIA WebLogic access logs for requests to /PSEMHUB) and any percent-encoded variant, and should inspect <PS\_CFG\_HOME>/webserv/<domain>/applications/peoplesoft/PSEMHUB.war/ for files that are not part of the shipped product.

Finally, they should rotate all credentials the PeopleSoft application service account can read, and monitor outbound traffic from PeopleSoft hosts to the network indicators listed here.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
