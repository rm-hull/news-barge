---
title: Two major security flaws are affecting more than six million WordPress websites
source_url: https://www.techradar.com/pro/security/two-major-security-flaws-are-affecting-more-than-six-million-wordpress-websites
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-07T19:53:07Z'
published: '2026-09-07T00:00:00Z'
description: They were already used in more than 440,000 attacks
image: https://cdn.mos.cms.futurecdn.net/PxxKy74xA4GapoubYuoRtK-2560-80.jpg
---

![Wordpress brand logo on computer screen. Man typing on the keyboard.](https://cdn.mos.cms.futurecdn.net/PxxKy74xA4GapoubYuoRtK.jpg) 

- **Wordfence discloses two critical flaws in Elementor Pro and Super Forms**
- **Bugs allow unauthenticated arbitrary file uploads, enabling remote code execution; both patched recently**
- **Exploitation attempts already exceed 440,000**

More than six million WordPress users are at risk of website takeover, researchers have claimed after discovering two major vulnerabilities being exploited in the wild.

Security researchers Wordfence disclosed finding two flaws, one in Elementor Pro, and one in Super Forms - two popular WordPress plugins.

Elementor Pro is a commercial plugin that allows users to build websites using drag-and-drop elements instead of code. With it, they can add advanced widgets, templates, different forms, popups, and more. It is quite a popular solution with more than six million websites actively using it.

## Two bugs, hundreds of thousands of attacks

According to Wordfence, up until recently, it was vulnerable to an “unrestricted file type upload” bug in all versions up to, and including, 4.2.1. “This makes it possible for unauthenticated attackers to upload files that may be executable, which makes remote code execution possible,” the researchers explained. “This requires that the targeted site has published a page containing an Elementor Pro Form widget with at least one non-required File Upload field.”

The bug is tracked as CVE-2026-32475, carries a severity score of 9.8/10 (critical), and was patched in mid-August 2026. So far, Wordfence alone blocked more than 190,000 exploit attempts.

At roughly the same time, the researchers also reported finding a flaw in Super Forms, a form builder plugin that lets users create and manage forms using a drag-and-drop interface. This plugin, with some 13,000 active installations, contained a bug that allowed arbitrary file upload in all versions up to, and including, 6.3.313.

“This makes it possible for unauthenticated attackers to upload files that may be executable, which makes remote code execution possible,” the researchers explained.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

This one is tracked as CVE-2026-14894, also carries a severity score of 9.8/10 (critical) and it, too, was patched a few weeks ago. For this flaw, Wordfence observed more than 250,000 exploitation attempts meaning that cumulatively, these two resulted in 440,000 attacks already.

Given the widespread adoption of these plugins, and the fact that the flaws are being actively leveraged, users are advised to apply the fixes without delay.

*Via**The Hacker News*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
