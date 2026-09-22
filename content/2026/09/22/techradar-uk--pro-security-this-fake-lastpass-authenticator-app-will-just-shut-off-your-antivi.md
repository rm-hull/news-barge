---
title: This fake LastPass Authenticator app will just shut off your antivirus and
  leave you open to attack
source_url: https://www.techradar.com/pro/security/this-fake-lastpass-authenticator-app-will-just-shut-off-your-antivirus-and-leave-you-open-to-attack
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-22T19:44:27Z'
published: '2026-09-22T00:00:00Z'
description: Researchers found a never-before-seen malware targeting LastPass users
categories:
- Technology & Software
- Business & Entrepreneurship
image: https://cdn.mos.cms.futurecdn.net/7Q34GM2RgrdwsWnK6jBAeP-2000-80.png
---

![LastPass](https://cdn.mos.cms.futurecdn.net/7Q34GM2RgrdwsWnK6jBAeP.png)

* **Attackers spoofed LastPass Authenticator via SEO‑poisoned GitHub pages, delivering malicious ZIP files**
* **Malware Rapuncel uses DLL sideloading, kills 145 AV products, and steals passwords, wallets, and tokens**
* **Campaign ongoing for months; LastPass vaults unaffected, but users urged to download only from trusted sources**

Be careful when downloading the LastPass Authenticator app - there are impostors out there that can disable your antivirus and wreak havoc on your computer.

LastPass recently discovered an elaborate scheme to get people infected with malware - a spoofed website, SEO poisoning, DLL sideloading, and a malware loader delivering never-before-seen payload that can kill endpoint protection and antivirus solutions.

According to the password manager, users searching for "LastPass Authenticator download" or similar keywords will get a GitHub page rather high on the search engine results pages. At a glance, the page looks almost identical to the authentic LastPass offering - however, it redirects users to a separate one, hosted on attacker-controlled infrastructure and delivering a large .ZIP file with multiple files.

Among the files are two worth paying attention to: vsdbg.exe, and vsdbg.dll. The .EXE one is renamed to look like a LastPass installer, but it’s in fact a legitimate Microsoft debugging tool. This tool is used to run the malware - the vsdbg.dll file. This is a method called “dll sideloading” where the legitimate program will look for a DLL file in the same folder it’s located, rather than the wider device library. Since the DLL is delivered together with the executable, it is the first one to be run, despite the fact that it’s malicious.

## Rapuncel

LastPass shared the malware with security researchers Delphos for analysis, and they’ve named it Rapuncel. No AV engines have been able to spot it, when it was first analyzed.

Once Rapuncel runs, it does a number of things. First, it gains admin-level access to run as SYSTEM, and then installs a kernel driver. The driver, disguised as an NVIDIA graphics component, comes with a hardcoded list of 145 antivirus and endpoint security products, and if any of them are found on the device, they are instantly terminated.

After killing antivirus solutions, the malware gets to work, stealing saved passwords from more than 25 browsers (Chrome, Edge, and other popular ones included), cryptocurrency wallet files from more than 30 wallet apps, Discord login tokens, Steam session tokens, Telegram session data, Windows credential store, all documents with words like “password”, “seed”, “wallet”, or “recovery” in their name, screenshots of every monitor connected to the device, as well as a detailed profile of the system.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Once all of this is harvested, the information is compressed into a .ZIP archive and uploaded to a server under the attackers’ control. To add insult to injury, the kernel driver was given code to intercept all web traffic, allowing the attackers to inject ads, or modify search results, at a whim.

Rapuncel comes with a persistence mechanism, as well, to make sure it continues operating even if the victim spots it. Spotting it should not be too difficult, though - if no antivirus programs are allowed to run on a computer, something is definitely not working properly.

## Active for months

Still, the malware installs itself as a Windows service that starts automatically at boot, and then loops continuously, checking for security products and killing them as soon as they’re activated. “The machine may remain fully under the attacker's control until the kernel driver is physically removed,” the researchers explained. “This process requires booting the computer into Safe Mode or using an external recovery tool, because normal Windows tools cannot safely remove software operating at that level while the system is running.”

LastPass and Delphos believe the campaign has been active for months, and that it will continue to operate despite disruption efforts:

“The LastPass lure was a single recent frame in a campaign that has been running for months and shows every sign of continuing after its current infrastructure is burned,” the researchers said. They stressed that this is “opportunistic brand impersonation” and that LastPass systems and customer vaults have not been compromised or involved in any way.

LastPass said it was one of 40 companies spoofed in this campaign and has urged users to only download apps from reputable, vetted sources.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png)

![Google logo on a black background next to text reading &#039;Click to follow TechRadar&#039;](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg)

***Follow TechRadar on Google News***and** add us as a preferred source** * to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
