---
title: Thousands of GitHub repositories targeted in widespread attack — 4,800 accounts
  already compromised to steal cloud credentials
source_url: https://www.techradar.com/pro/security/thousands-of-github-repositories-targeted-in-widespread-attack-4-800-accounts-already-compromised-to-steal-cloud-credentials
source_site: TechRadar UK
source_slug: techradar-uk
description: Aikido researchers found attackers abusing stolen GitHub accounts and
  automated workflows
image: https://cdn.mos.cms.futurecdn.net/F6hCbctyQPGeK8n3hNAcgG-1920-80.png
published: '2026-11-13T00:00:00Z'
scraped_at: '2026-11-13T19:38:10Z'
categories:
- Technology & Software
- Business & Entrepreneurship
- Personal Finance & Investing
people:
- Aikido
locations: []
organisations:
- AWS
- Aikido
- Azure
- GitHub
- Google Cloud
- HashiCorp Vault
- MITRE
- TechRadar Pro
- Terraform
---

![GitHub Actions found in MITRE, Splunk, and other open source repositories](https://cdn.mos.cms.futurecdn.net/F6hCbctyQPGeK8n3hNAcgG-1920-80.png)

* **Threat actors used 4,837 compromised GitHub accounts to open pull requests across 61,764 repositories**
* **At least 1,835 repositories executed the payload and had credentials exfiltrated**
* **Authentication tokens, AWS, Azure and Google Cloud credentials, and more, targeted**

Cybercriminals were recently seen abusing multiple GitHub features to deploy infostealers and exfiltrate user’s cloud login credentials and other secrets.

Tens of thousands of repositories have already been targeted, and almost 2,000 fell prey to the attack, cybersecurity researchers Aikido said, in a recent report outlining how the attackers used stolen GitHub credentials to abuse GitHub Actions and workflows, two features designed to speed up and automate certain activities.

GitHub is a platform for developers working on open source projects. Each project has its own “repository” - a folder containing source code, configuration files, and other resources. Developers can propose changes to public repositories through a process called “pull request”, after which other developers can review and approve/decline the changes.

GitHub also has an automation service called Actions, that allows developers to automatically execute various tasks, including pull requests. These automated processes are called workflows and can be described as a set of instructions telling GitHub what to do. Here is another vital nugget of information: workflows can access sensitive credentials when required to perform these tasks.

## Using compromised accounts

According to Aikido, the threat actors used 4,837 compromised GitHub accounts to open pull requests across 61,764 repositories. The researchers did not say how the attackers obtained these accounts, or how they were compromised. The pull requests were probes, not actual attacks, and were used so the attackers can see which projects they could modify.

“We're tracking this campaign as wfx-loot based on the threat actor's name for the malware and the term used for stolen secrets,” Aikido said. The pull requests were titled docs: dependency audit notes, and were submitted from branches named wfx-docs.

Of the 60,000+ matching pull requests, more than 10,000 targeted repositories the compromised accounts did not own, but could access. After establishing write access, the attackers used one of three methods to deploy a malicious script: modifying existing GitHub Actions workflows, adding a shell script triggered by an npm installation hook, or creating a new workflow file on a temporary branch.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The payload included roughly 1,500 lines of code that was present in all three scenarios. The code searched the compromised environments for sensitive information such as GitHub Actions secrets, authentication tokens, AWS, Azure and Google Cloud credentials, Docker and Kubernetes configuration files, SSH keys, API keys for AI services such as OpenAI and Anthropic, and developers' shell histories. It also searched for .env files, private keys and credentials belonging to tools such as npm, PyPI, HashiCorp Vault and Terraform.

## Stealing credentials

The malware also tried to expand its access, exchanging stolen tokens for cloud sessions, spoofing service accounts, and even creating new credentials. It also modified AWS and Azure configurations to maintain access when victims rotated their compromised credentials.

Aikido says that at least 1,835 repositories executed the payload and had credentials exfiltrated. The attackers subsequently reverted their changes and deleted workflow execution logs, sometimes within a minute, to cover their tracks and make detection that much harder.

The wfx-look campaign apparently spilled into the software supply chain, as Aikido also found compromised PHP packages on Packagist and two affected Go module versions. However, the researchers said this might have been a side-effect of the attackers abusing automated publishing processes, rather than something they planned on doing.

Aikido advises anyone whose repository executed the malicious payload to consider all of their secrets and cloud credentials their workflows can access as compromised, and needing urgent rotation.

*Via* * BleepingComputer*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
