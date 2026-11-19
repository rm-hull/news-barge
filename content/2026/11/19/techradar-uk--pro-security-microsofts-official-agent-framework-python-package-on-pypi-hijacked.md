---
title: Microsoft's official Agent Framework Python package on PyPI hijacked to push
  login-stealing malware
source_url: https://www.techradar.com/pro/security/microsofts-official-agent-framework-python-package-on-pypi-hijacked-to-push-login-stealing-malware
source_site: TechRadar UK
source_slug: techradar-uk
description: Attackers push two versions in roughly half an hour
image: https://cdn.mos.cms.futurecdn.net/JqCaVi7J7avcuKZHmHeMgF-970-80.jpg
published: '2026-11-19T00:00:00Z'
scraped_at: '2026-11-19T20:30:30Z'
categories:
- Technology & Software
people: []
locations: []
organisations:
- AI
- AWS
- Aikido Security
- Azure
- Docker
- GitHub Actions
- Hugging Face
- Microsoft
- OpenAI
- PyPI
- Python
- Socket
- TechRadar Pro
- Wiz
---

![Python](https://cdn.mos.cms.futurecdn.net/JqCaVi7J7avcuKZHmHeMgF-970-80.jpg)

* **Attackers compromised Microsoft’s Agent Framework package on PyPI and inserted malware designed to steal credentials and cloud tokens**
* **Malicious versions targeted Azure, AWS, GitHub, OpenAI, Docker, and other developer platforms before being removed**
* **Developers who installed the affected releases should rotate secrets, investigate environments, and treat systems as compromised**

Threat actors broke into Microsoft’s official Agent Framework Python package on PyPI and used it to disseminate infostealing malware to hundreds of thousands of developers that rely on it daily. Fortunately, the attack was spotted and stopped rather quickly - although that doesn’t mean there were no victims.

The Microsoft Agent Framework Python package is an open source toolkit that helps developers build AI agents and applications where multiple AI agents can work together to complete different tasks.

It provides the building blocks for creating AI assistants that can use tools and follow instructions, as well as to interact with other agents and handle more complex tasks.

## Gone in 31 minutes

For a relatively new tool, Agent Framework is gaining plenty of traction, with monthly downloads reaching almost 200,000 these days.

On November 17, 2026, someone released version 1.26.1 containing an infostealer that executed automatically when Python boots up, even in environments where the Agent Framework package was not imported. It kept its dependency on the earlier package (1.26.0), meaning the framework would function properly while the malware would do its work in the background.

The tool was designed to steal login credentials and other secrets from environment variables, as well as to nab local configuration files and other running processes. It targeted Azure, AWS, GitHub, Docker, Hugging Face, OpenAI, and numerous other services. What’s more, it tried to steal Azure managed identity access tokens, as well as Azure DevOps OIDC tokens.

PyPI took exactly 31 minutes to spot the intrusion and quarantine the malicious version. However, two minutes later, a second attack took place. Version 1.26.2 added GitHub Actions OIDC token requests, as well as searches of GitHub runner directories. The interesting thing about the second attack is that the threat actors somehow maintained access to Microsoft’s PyPI account even after the first cleansing. PyPI removed the second version approximately eight minutes after upload.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

We don’t know if the attack was successful and if any developers lost their secrets as a result. According to PyPIStats.org, the tool has approximately 6,900 downloads a day, or around 287 an hour. Therefore, the malicious versions were potentially downloaded around 150 times.

If you were among those who downloaded versions 1.26.1 or 1.26.2, remove it immediately and treat the system it was installed on as potentially compromised. It’s also worth mentioning that simply downgrading to a clean version is not enough, since the secrets were probably already exfiltrated. Therefore, make sure to check the environment for suspicious files, particularly the .pth files associated with the attack, and consider rebuilding affected environments from the ground up.

## What to do in case of an infection

Also, all passwords should be considered exposed, including API keys, access tokens, and other secrets - make sure to revoke and replace them. Furthermore, make sure to review your Azure, AWS, GitHub, and other service accounts for suspicious activity, including unexpected logins or access requests. Finally, anyone using the package in automated build systems, particularly GitHub Actions, should investigate those environments as well.

The attack was spotted and documented by a number of security researchers, including Wiz, Aikido Security, Socket, and others. According to some researchers, the first malicious release used agent\_framework\_meta.pth to execute the credential stealer in agent\_framework\_meta/\_telemetry.py during Python startup, while the second restored the original package initializer and moved the malicious code to af\_runtime\_diag.pth and af\_runtime\_diag.py.

Both versions were sending harvested information to the same server, located at [https://webhook[.]site/d381fd80-ec62-42ad-8f5c-d1b15103c9bb](https://webhook[.]site/d381fd80-ec62-42ad-8f5c-d1b15103c9bb).

No threat actors claimed responsibility for the attack and we don’t know how they gained access to Microsoft’s official PyPI project. The Windows maker has not issued a comment or a statement.

*Via* * BleepingComputer*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
