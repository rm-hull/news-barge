---
title: PHP security issues could also threaten your NAS device — but not every vendor
  is able to patch just yet
source_url: https://www.techradar.com/pro/security/php-security-issues-could-also-threaten-your-nas-device-but-not-every-vendor-is-able-to-patch-just-yet
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-23T17:06:20Z'
published: '2026-10-23T00:00:00Z'
description: The php2shell flaw affects more than just websites and web apps
image: https://cdn.mos.cms.futurecdn.net/RUyYKopfxTPNGFEJTvqWBk-1366-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people: []
locations:
- Docker
organisations:
- Apple Insider
- DiskStation
- Mail Station
- PHP2Shell
- Package Center
- QNAP
- Synology NAS
- TechRadar Pro
- TerraMaster
---

![](https://cdn.mos.cms.futurecdn.net/RUyYKopfxTPNGFEJTvqWBk-1366-80.jpg)

* **Critical PHP2Shell flaws also impact internet-exposed NAS devices and PHP-based Docker workloads**
* **Major vendors are still releasing patches, leaving some Synology, QNAP, and other systems exposed**
* **Researchers urge immediate updates, removal of public exposure, and VPN-only remote access**

Websites and web servers are apparently not the only products affected by the php2shell vulnerability - Network Attached Storage (NAS) devices are at risk, too - and to make matters worse, some of the most popular manufacturers have not yet released a patch, despite the flaws being actively abused in the wild.

Research by *Apple Insider* noted that the flaw also affects software maintained by NAS manufacturers, as well as applications running independently in Docker containers, with NAS devices that are reachable through the public internet also at risk.

What's particularly concerning is that some of the biggest NAS manufacturers have said to be working on a fix, but the work is yet to be done. Synology, for example, released a new security advisory saying PHP versions 7.3 - 8.4, Mail Station, and Synology Calendar are all affected and adding that it released updated PHP packages to address the flaws. Those running Synology NAS products should head over to the company’s Package Center and download archive and look for updated PHP 8.2 and PHP 8.4 packages.

## Twofold risk

The company also stressed that there is a difference between installed PHP packages and PHP components within DiskStation manager, and added that its built-in PHP isn’t exposed to the public internet, therefore most likely not at risk.

Another major NAS manufacturer, QNAP, confirmed a wide range of affected products, including QTS 5.2.11 and older, QTS 6.1.9, QuTS hero and QuTScloud, and Note Station 3. It said it was currently working on a fix, but did not give a timeline on when the patch might become available. So far, there is no evidence of in-the-wild attacks, but the company does recommend removing the devices from the open internet, disabling unnecessary port forwarding, UPnP, and remote-access services.

Other manufacturers are also currently working on a fix, including TerraMaster, Ugreen, and Asustor, Apple Insider found. “NAS owners should check their manufacturer's security notices and available updates for their specific models,” the publication said.

For NAS owners, the risk is twofold, since PHP is found in both the operating system and Docker containers.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Those running PHP-based services in Docker should check if their container images are running affected versions of PHP, and update them as soon as humanly possible.

There is also the problem of running older devices that have reached end-of-life and are, as such, no longer supported with patches. These, security experts agree, should be removed from public access. Unsolicited inbound connections should be blocked, and the device should be kept accessible only locally. Remote access should be achieved through a secure VPN, instead of forwarding NAS management ports.

## P2PShell?

PHP2Shell is a name for a pair of vulnerabilities - CVE-2026-109618 and CVE-2026-109619 - that were recently discovered in the PHP programming language. They are considered critical and allow malicious actors to take over websites, steal data, deploy malware, and more. However, the story that has so far revolved around internet sites and web apps is now expanding into NAS devices, too.

PHP2Shell is shaping up to be the biggest security incident of the year, and possibly longer, arguably rivaled only by the Spectre/Meltdown flaws from eight years ago.

The pair of vulnerabilities - both critical in severity and both allowing for remote code execution - affects the vast majority of websites and web apps in existence today.

Knowledge of the flaws leaked four days before the patches were released, according to Amazon, and the number of exploitation attempts went from a few hundred 10 hours before publication, to millions today.

However, most of these attempts seem to have been unsuccessful. Analysis is ongoing as to why that is the case, with some researchers thinking code execution needs to get past ASLR, which is a difficult thing to do remotely. However, breaking in only seems to be a matter of time, which is why the security community urges manufacturers to release a fix as soon as possible, and owners to apply them without delay.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
