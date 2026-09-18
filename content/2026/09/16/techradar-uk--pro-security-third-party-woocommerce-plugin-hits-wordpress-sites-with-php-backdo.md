---
title: Third-party WooCommerce plugin hits WordPress sites with PHP backdoor abusing
  recently patched vulnerability
source_url: https://www.techradar.com/pro/security/third-party-woocommerce-plugin-hits-wordpress-sites-with-php-backdoor-abusing-recently-patched-vulnerability
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-16T13:27:05Z'
published: '2026-09-16T00:00:00Z'
description: Attackers are actively exploiting a recently patched flaw
image: https://cdn.mos.cms.futurecdn.net/zHBWWxpmu5iienhz4xVsXa-2560-80.jpg
categories:
- Technology & Software
---

![WooCommerce](https://cdn.mos.cms.futurecdn.net/zHBWWxpmu5iienhz4xVsXa.jpg) 

- **Defiant warned of active exploitation of WooCommerce Wholesale Lead Capture Plugin flaw (CVE‑2026‑27540)**
- **Critical unauthenticated file‑upload bug lets attackers deploy PHP webshells for site takeover**
- **Patch released in Feb 2026 (v2.0.3.2); Wordfence blocked 100,000+ attacks, users urged to update and check uploads**

A critical vulnerability in a popular WooCommerce plugin is being actively exploited to upload malware and possibly take over entire websites, security experts have warned.

The plugin in question is called Wholesale Lead Capture Plugin for WooCommerce. It adds a dedicated registration and onboarding system for wholesale and B2B customers, letting businesses collect company and other custom information, review applications, assign wholesale user roles, and automate registration and onboarding emails.

It is a premium plugin that costs between $99 and $600 and which, according to the __Wordpress store page__, has more than 20,000 active installations.

## A thousand victims

The plugin was vulnerable to an unauthenticated arbitrary file-upload flaw which, as the name suggests, allows unauthenticated parties to upload arbitrary files, including PHP webshells and executable code that can result in full site takeover. It is tracked as CVE-2026-27540 and carries a severity score of 9.0/10 (critical).

Versions 2.0.3.1 and older were said to be affected. Version 2.0.3.2, released on February 20, was said to have addressed the bug, meaning the patch has been available for almost half a year. However, WordPress security outfit Defiant said its Wordfence web application firewall blocked more than 100,000 attacks, and Wordfence added that it observed two attack spikes - one between June 4 and 17, and another one between July 1 and August 30.

In these incidents, the attackers were mostly uploading reconnaissance webshells, possibly mapping out the landscape before deploying more serious malware.

“The uploaded shell.php is a PHP webshell that reports host details and provides a browser-based upload form for writing additional malicious files to the site,” the researchers said.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

If you are running the plugin, it is advised you update it to the newest version as soon as possible, and check upload directories for unexpected, or recently created, PHP files.

*Via**BleepingComputer*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
