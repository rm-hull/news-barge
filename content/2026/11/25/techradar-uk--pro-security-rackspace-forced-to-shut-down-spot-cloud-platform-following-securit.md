---
title: Rackspace forced to shut down Spot cloud platform following security breach
source_url: https://www.techradar.com/pro/security/rackspace-forced-to-shut-down-spot-cloud-platform-following-security-breach
source_site: TechRadar UK
source_slug: techradar-uk
description: Users are paying their respects on Reddit
image: https://cdn.mos.cms.futurecdn.net/7DtE9RCVmUtmH2FAfvxsvM-2560-80.jpg
published: '2026-11-25T00:00:00Z'
scraped_at: '2026-11-25T19:14:01Z'
categories:
- Technology & Software
people:
- Joe
locations: []
organisations:
- Kubernetes Secrets
- Rackspace Spot
- Reddit
- TechRadar Pro
---

![Malware attack virus alert , malicious software infection , cyber security awareness training to protect business](https://cdn.mos.cms.futurecdn.net/7DtE9RCVmUtmH2FAfvxsvM-1920-80.jpg)

* **Attackers used stolen credentials to access Rackspace Spot, exposing Kubernetes secrets, API tokens, and other sensitive cloud resources**
* **Rackspace revoked affected credentials, advised customers to rotate secrets, and investigate cluster activity for potential compromise**
* **The company later announced it would discontinue the Rackspace Spot platform, giving customers until December 8 to migrate their workloads**

Rackspace has recently announced it is shutting down its cloud platform, Rackspace Spot, allegedly after cybercriminals broke in and stole user information.

In the early hours of November 17 2026, a threat actor used stolen login credentials to access parts of Rackspace Spot. The company learned about the intrusion a day later from a customer report, and later confirmed that multiple customers had been affected.

During the intrusion, the unidentified attackers created pods in people’s clusters, read Kubernetes secrets, and listed nodes and volumes.

## What happened?

“With that access, they could have read any Secret in an affected user’s clusters, and any Spot API token or refresh token that user held,” Rackspace told the affected customers in a data breach notice emailed at the time.

Kubernetes Secrets can hold sensitive information, including database passwords, API keys, or authentication credentials. If threat actors managed to access these, they could use them to compromise other services, or systems connected to affected clusters. This is, among other things, why Rackspace urged its users to rotate their credentials, even if no data leak was confirmed.

To tackle the intrusion, Rackspace revoked affected Spot tokens and sessions, removed the pods the attackers created, and rotated the platform and storage keys involved.

The company urged its customers to reissue their Spot API tokens and replace any Spot refresh tokens stored in automation. It also told them to download fresh kubeconfigs for their cloudspaces, rotate credentials stored in their cluster Secrets, and review access logs from November 17 onward.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## Pulling the plug

A few days after the incident, the company apparently decided it was time to sunset the whole operation. In an email notice seen by *BleepingComputer*, the company gave its customers until December 8 to migrate their services and download their data.

"Following a review of the situation, Rackspace has made the decision to wind down the Rackspace Spot service. This decision is being made to provide a clear path forward for customers," the company said in the notice.

Customers have until December 8, 2026, 5PM Central Time, to move their data, after which all remaining workloads will be terminated.

The announcement did not sit well with Rackspace’s customers. Its cloud computing platform was a relatively inexpensive way to access cloud servers, virtual machines, and managed Kubernetes infrastructure. Its unique selling proposition was to offer lower cloud computing costs through a bidding system, rather than traditional fixed pricing. The company advertised savings of up to 90% compared to conventional, on-demand computing resources, with the caveat being that users must design their workloads to tolerate possible interruptions.

And tolerate them, they did. Reddit is filled with disappointed users, some of which are even urging the company to reconsider.

“I bet the vast majority of spot users would gladly pay a bit more for the service to keep it running,” one user said. “It's incomparable to anything out there right now. For the average Joe it's not the service, but for those of us who can handle our own clusters and workarounds the quirks, it's by far the best option out there.”

“Don't take this down!!!”

Others were more at peace with their fate, thanking Rackspace for the affordable compute and saying, “it was good while it lasted.” Rackspace has not commented on the calls to keep going, so we don’t know if they’re willing to reconsider.

As of November 25, 2026, no threat actors claimed responsibility for the attack on Rackspace, so we don’t know if this was ransomware or a nation-state attack. Furthermore, the data stolen in the incident doesn’t appear to have surfaced anywhere on the dark web, either for sale or for free.

*Via* * BleepingComputer*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
