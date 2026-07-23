---
title: A malicious Chrome extension for Adobe Acrobat could let hackers access private
  WhatsApp chats
source_url: https://www.techradar.com/pro/security/a-malicious-chrome-extension-for-adobe-acrobat-could-let-hackers-access-private-whatsapp-chats
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-23T14:26:54Z'
published: '2026-07-23T00:00:00Z'
description: Researchers find a universal cross-site scripting-class cross-origin
  data disclosure vulnerability
image: https://cdn.mos.cms.futurecdn.net/3hRUaAPv8gwJBWYX8h3HqT-1280-80.jpg
---

![Google Chrome logo on a mobile phone's screen](https://cdn.mos.cms.futurecdn.net/3hRUaAPv8gwJBWYX8h3HqT.jpg) 

- **Guardio Labs found CVE‑2026‑48294 in Adobe Acrobat Chrome extension, enabling cross‑site data disclosure**
- **Attackers could steal WhatsApp Web chats if victims opened malicious landing pages with extension active**
- **Adobe patched the flaw in version 26.7.2.0; update recommended for 314M extension users**

If you have Adobe Acrobat’s extension for Chrome, and you like chatting through WhatsApp Web, there is a potential security vulnerability you might want to address.

Security researchers from Guardio Labs discovered a “universal cross-site scripting (UXSS)-class cross-origin data disclosure vulnerability”, which is another way of saying that a website could use the flaw to read the contents of a different website, loaded in a separate tab.

The vulnerability was found in the Adobe Acrobat Chrome extension and is now tracked as CVE-2026-48294. It was given a severity score of 7.4/10 (high), and affects versions 26.5.2.2 and earlier. Guardio Labs dubbed it “HermeticReader” because of what it exploits.

## "Insultingly ordinary" setup

The extension comes with different integrations, such as Google Drive or, in this case - WhatsApp Web. The WhatsApp integration component, internally known as "Hermes" is where the bug was found.

In theory, an attacker could create a new landing page and share it with the victim via email, instant messaging, SEO poisoning, or other methods. If the victim 1) has the vulnerable version of the Adobe Acrobat Chrome extension installed; 2) has WhatsApp loaded in a separate tab; and 3) opens the malicious landing page, it could trigger the extension’s vulnerable code path and allow the attackers to access everything the victim has on their WhatsApp.

Some sources argue that threat actors could use this vulnerability to pull one-time passcodes delivered via WhatsApp.

"The setup is almost insultingly ordinary: an attacker-controlled page, dressed to look like the kind of page you land on via search results, marketing emails, etc.," Guardio Labs wrote in its analysis.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

"The visitor, who already has the Adobe Acrobat extension installed, opens that page. The page wakes up a dormant engine inside the extension, reaches directly into WhatsApp Web. Seconds later, the rendered WhatsApp Web view - the chat list, contact names, messages, the profile name, the text of whatever conversation is open - the whole WhatsApp in the attacker's hands."

Adobe has since publicly acknowledged the issue and thanked Guardio Labs’ researchers for their help. It has also fixed the problem in version 26.7.2.0 that’s currently available for download. The extension has more than 314 million users.

*Via**The Hacker News*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
