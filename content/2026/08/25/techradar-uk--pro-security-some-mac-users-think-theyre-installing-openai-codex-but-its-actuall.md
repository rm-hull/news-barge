---
title: Some Mac users think they're installing OpenAI Codex, but it's actually a malware
  that can steal passwords in seconds
source_url: https://www.techradar.com/pro/security/some-mac-users-think-theyre-installing-openai-codex-but-its-actually-a-malware-that-can-steal-passwords-in-seconds
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-25T13:08:00Z'
published: '2026-08-25T00:00:00Z'
description: An elaborate scheme was designed to deploy AMOS
image: https://cdn.mos.cms.futurecdn.net/UjSNcAZ5SebctebKAMQNVF-2560-80.jpg
---

![Cybersecurity ensures data protection on internet. Data encryption, firewall, encrypted network, VPN, secure access and authentication defend against malware, hacking, cyber crime and digital threat](https://cdn.mos.cms.futurecdn.net/UjSNcAZ5SebctebKAMQNVF.jpg) 

- **Crooks used Google Sites and stolen Google Ads accounts to push fake OpenAI Codex pages**
- **macOS users tricked into pasting Terminal commands, leading to AMOS infostealer infection**
- **Campaign abuses Google’s trust signals; Windows download button was a decoy, only Mac payload worked**

Cybercriminals were seen abusing Google Sites, the Google ad network, and OpenAI’s good name, in a campaign that targets macOS users with infostealers.

According to security researchers CATO CTRL, the crooks used Google Sites to create a fake version of the OpenAI Codex download site. To avoid being flagged by Google’s security systems and ultimately removed, the site itself contains no malicious code or download links, whatsoever. Instead, it hosts an iFrame that displays content hosted elsewhere.

Then, they advertised that site on the Google Ads network. Google is usually good at spotting and preventing malicious ads from running on its network, but sometimes threat actors steal legitimate accounts with good standing and use them to bypass automated scans and get the ads listed, while also spending other people’s money on the ad campaign.

## Not ClickFix

The ads were displayed to users searching for “codex macos download”, at the very top of the page. Using both Google Sites and Google Ads is a deliberate attempt to appear legitimate and trustworthy since after all, many people trust whatever Google displays as the top result without double-checking or scrutinizing the result.

Those that do click will see a website that, by all accounts, looks like OpenAI’s download site for Codex, the company’s AI coding agent. The site has download buttons for both Windows and Mac, but only the latter works. The download and installation process was designed to look “advanced” - instead of getting an executable, the victims are told to paste a command in Terminal.

Cato’s researchers call this a ClickFix attack, but ClickFix usually displays a fake problem, before offering an equally fake solution. This looks more like another way to appear legitimate because after all, several AI agents are specifically designed to be installed and run from the macOS Terminal, including OpenAI’s Codex CLI.

The end goal of the campaign is to deploy AMOS, a known macOS infostealer capable of grabbing browser data, login credentials, cryptocurrency wallet information, and more.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

*Via**SiliconANGLE*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
