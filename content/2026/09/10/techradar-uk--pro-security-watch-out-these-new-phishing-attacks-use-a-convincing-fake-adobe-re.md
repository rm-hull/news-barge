---
title: Beware — these new phishing attacks use a convincing fake Adobe Reader pages
  to trick victims into installing malware
source_url: https://www.techradar.com/pro/security/watch-out-these-new-phishing-attacks-use-a-convincing-fake-adobe-reader-pages-to-trick-victims-into-installing-malware
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-10T19:06:38Z'
published: '2026-09-10T00:00:00Z'
description: Crooks are deploying cheeky browser-in-the-browser techniques
image: https://cdn.mos.cms.futurecdn.net/ncL98vteKnP9dydmNAHGqN-1920-80.png
---

![PDF](https://cdn.mos.cms.futurecdn.net/ncL98vteKnP9dydmNAHGqN.png) 

- **Huntress warns of phishing campaign abusing Adobe branding with browser‑in‑the‑browser trick** 
- **Victims lured into fake update pages, unknowingly installing rogue ScreenConnect clients** 
- **Attackers gain persistent remote access; defenders urged to restrict RMM installs and monitor IoCs**

Security researchers Huntress have warned of an ongoing phishing campaign that abuses Adobe’s brand while deploying clever browser-in-the-browser (BitB) techniques to trick the victims.

The goal is to deliver rogue ScreenConnect clients which would grant the attackers persistent access to target devices.

In its report, Huntress says it could not find the lure itself and thus could not report what the scam looks like. However, it saw the victims clicking on a link in the email and then being redirected to a typosquatted domain https[://]adoube[.]vu that spoofs an Adobe landing page.

## We heard you like browsers…

This is where we get to the scam’s unique twist. Usually, phishing lures would simply redirect victims to a malicious website which could be identified simply by looking at the address bar. If the domain differs from the legitimate one, the scam falls apart. To work around that problem, scammers came with a solution called “browser in the browser”.

Using either HTML, CSS, or JavaScript, the crooks would create an entire fake browser window, including the address bar, URL, padlock icon, and more, inside the actual webpage content itself. Therefore, if the victim isn’t all too careful, they might look at the fake address bar, see a legitimate URL, and believe they are visiting the correct website.

In this fake browser window, the fraudsters display a blurred .PDF document. Overlaid is a message saying the documents are “secured” and created with “the latest version of Adobe.” The only way to read them, the message continues, is to “update or download Adobe PDF Reader.” Expectedly, there is a big “View Files” button just under the notification, leading to a different, equally fake BitB page, showing the download progress. In the background, something gets downloaded.

Victims might think they’re getting a PDF reader, while in reality they’re getting a rogue version of ScreenConnect.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## Poisoned ScreenConnect instances

On its own, ScreenConnect is not malware, or dangerous in any other way. It is a legitimate remote access and support software, similar to TeamViewer, AnyDesk, or Remote Desktop, allowing IT professionals remotely connect to and control computers and other devices. These variants, however, are tainted to enable threat actors to obtain persistent remote access to their targets’ endpoints, Huntress explained.

“The first initial remote client installed was the rogue ScreenConnect Client configured to communicate with instance-uxh86b-relay[.]screenconnect[.]com. The attacker used a legitimate ScreenConnect Trial Relay domain to further avoid detection,” the researchers said. “This initial malicious ScreenConnect Client used the native Windows command shell and curl to retrieve and install a second malicious ScreenConnect Client configured to communicate with attacker-controlled IP. Both clients established service-based persistence for continued remote access.”

After installation, the attackers used the second ScreenConnect session to run HideCursor.exe, an executable, as the name suggests, that helps the attackers hide their mouse activity.

Huntress’ researchers don’t know what the endgame is, since the threat actors were spotted and shut down in this stage of the attack. The researchers also did not share the details about the target, such as the size of the organization, or the industry it operates in. Therefore, it is impossible to even speculate on the nature of the attack and if the threat actors aimed to install ransomware.

Still, the researchers stressed the importance of training employees to “treat unexpected software update prompts and file-viewing pages with caution”, and to make sure they know how to verify downloads through trusted channels. IT teams should also restrict who can install remote-management tools, maintain an approved inventory of RMM software, and alert on new or unapproved ScreenConnect clients, unusual relay connections, and executables launched from the user Downloads folders.

Finally, businesses should monitor for Indicators of Compromise (IoC) listed on this page.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
