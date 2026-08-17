---
title: Ransomware gang crashes own attack — with no-one to blame but themselves
source_url: https://www.techradar.com/pro/security/ransomware-gang-crashes-own-attack-with-no-one-to-blame-but-themselves
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-17T16:40:38Z'
published: '2026-08-17T00:00:00Z'
description: Akira disables EDR tools, but kills the encryptor, as well
image: https://cdn.mos.cms.futurecdn.net/x4SmwpYXk8yGgDmYCVeckL-2560-80.jpg
---

![A hand about to touch a phone. Superimposed on top of it is a pink triangle with exclamation mark inside it. Behind it is a computer display with code on it](https://cdn.mos.cms.futurecdn.net/x4SmwpYXk8yGgDmYCVeckL.jpg) 

- **Akira ransomware tried Safe Mode boot to disable defenses but broke its own encryptor**
- **Defender later flagged and quarantined payload, leaving attackers with only stolen data**
- **Huntress advises VPN brute‑force alerts, MFA, SIEM logging, and Safe Mode monitoring**

A recent ransomware attack saw the operators Akira (figuratively) shoot themselves in the foot - and they still walked away with sensitive data, albeit limping.

Akira is a well-known ransomware group, considered one of the most active cybercriminal organizations on the internet. Its modus operandi is simple in theory: they look for an exposed VPN instance (for example, one with a default or weak password), access the domain controller, enumerate Active Directory, steal sensitive data, and deploy an encryptor.

With the encryptor they leave a ransom note, instructing the victim to reach out and negotiate a payment in exchange for the decryption key and for deleting the stolen documents and information.

However, in a recent attack, they tried to first disable the device’s antivirus and endpoint detection and response (EDR) solutions. The process backfired, resulting in the security solutions successfully spotting and quarantining the encryptor.

## The good and the bad of Safe Mode with Networking

A new report published by security researchers Huntress said that after establishing persistence on a device, Akira rebooted it into Safe Mode with Networking. This Windows startup mode boots the OS with only the essential drivers and services, excluding important components such as antivirus programs or EDR agents. At the same time, it grants internet access which, for Akira, is the perfect combination.

“This means Defender real-time protection was down too,” Akira explained. “For the entire Safe Mode window, the host had no working EDR, and AV was blinded. This is MITRE ATT&CK T1688: Impair Defenses: Safe Mode Boot, a technique that ransomware families like Snatch and AvosLocker have used for years. However, this is the first time we have seen Akira use it.”

What Akira didn’t bank on was Safe Mode with Networking also preventing its encryptor from running. “Safe Mode boots with a stripped-down environment and constrained virtual memory, and the Akira process tree appears to have starved it, getting the "Out of Virtual Memory" pop-up and the cascade of PowerShell hard errors line up exactly with the moment the payload tried to kick things off.”

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The operators had no other choice but to boot the device back up normally, at which point a scheduled Defender scan detected the encryptor, flagged it, and ultimately quarantined it.

“The takeaway is a little uncomfortable. While Safe Mode blinded our controls, it may also have prevented the encryption it was meant to enable. That's a lucky side effect of the attacker's own mistake in these circumstances, not a defense you can plan around,” Huntress warned, stressing that not every victim might get such a lucky break.

“Ultimately, this could be a case of winning the battle, but not the war. It's possible that a host with more physical memory or a larger page file might give akira.exe enough virtual memory to encrypt the endpoint in Safe Mode. Akira's developers or affiliates could retool the encryptor to reduce its memory demands or make its Safe Mode launch sequence more reliable, meaning that the same failure may not occur in a future intrusion.”

## How to defend against Akira ransomware

To defend against Akira, Huntress recommends users set up alerts on bursts of failed VPN logins against multiple usernames from one source. It works well because Akira starts its breach with a brute-force attack against the VPN. It also says users should correlate those failures with a successful login from the same IP or ASN within a short window.

The second step is to turn on multi-factor authentication (MFA) on every VPN account. Users should also disable or IP-allowlist the SSL VPN during active attacks and, if compromised, rotate all AD and VPN credentials. “Treat everything in that Get-ADUser dump as exposed,” the researchers warn.

EDR should be deployed to every host, as well as SIEM and ingest VPN + Windows Event Logs. “The first VPN logons were visible hours before any detonation—this time advantage is only possible if the logs are on SIEM.”

Finally, users can set up alerts on boot-configuration changes and Safe Mode boots, to catch Akira red handed.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
