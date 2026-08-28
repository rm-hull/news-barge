---
title: Security researchers find surveillance implants in Chinese-made routers sold
  worldwide — three different backdoor-like implants hidden in firmware
source_url: https://www.tomshardware.com/tech-industry/cyber-security/security-researchers-find-surveillance-implants-in-chinese-made-routers-sold-worldwide-three-different-backdoor-like-implants-hidden-in-firmware
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-28T22:14:51Z'
published: '2026-08-28T00:00:00Z'
description: The surveillance seems aimed at the domestic market, but it knocks huge
  holes in the security of the devices it's found in.
image: https://cdn.mos.cms.futurecdn.net/sb4UNrZUbaibqDXRTgybjF-2000-80.jpg
---

![Royalty free](https://cdn.mos.cms.futurecdn.net/sb4UNrZUbaibqDXRTgybjF.jpg) 

Security researchers have found three different backdoor-like implants hidden in firmware for routers manufactured by Shenzhen Zhibotong Electronics, better known as ZBT. The hardware is sold around the world under a bewildering array of brands, meaning you may not even realize you're using a ZBT router. The research, published by security firm VulnCheck, began with a Zbtlink AX3000 router. Researchers found that its firmware contained an implant that they dubbed ENDLESSDOORS, as it automatically phones home to a command-and-control server and can execute arbitrary commands as root.

ENDLESSDOORS is essentially a remote-control system embedded directly into the router's firmware. It starts automatically at boot and disguises itself as a normal Linux kernel process called kworker. The router periodically connects to a hard-coded server and announces itself. There's no meaningful authentication or encryption involved. Commands received from the server are passed directly to a shell running as root, and the implant can also establish an interactive root shell.

VulnCheck demonstrated the problem by impersonating the command server and taking control of its own test router. In other words, this isn't merely a theoretical vulnerability; if an attacker can hijack the connection to the implant's command server, they can obtain complete control of the router. The researchers found ENDLESSDOORS embedded in firmware for 20 ZBT models, including the Z8102AX, WG3526, WE826-T3-DSIM, and several other cellular routers. The same hardware is also sold under other names because ZBT manufactures routers for OEM and ODM customers. VulnCheck assigned the issue CVE-2026-66747, with a CVSS score of 9.3, but that wasn't the end of the investigation.

 ![A photograph of the Deep Orange 4G/LTE Router, which is a rebranded ZBT device.](https://cdn.mos.cms.futurecdn.net/CgW7YwHBEZEbteSqAoHYsY.jpg) 


VulnCheck subsequently bought an $88 Deep Orange cellular router from a US seller on Amazon and discovered that it was actually a white-labeled ZBT-WE826-T2. Its 2019 firmware was too old to contain ENDLESSDOORS, but instead, it contained two other implants that the firm designated DARKLANTERN and SPEAKINGSTONE.

DARKLANTERN is the particularly straightforward one. Operating as the infosrvd service, it opens a listener on the WAN via UDP port 9992 and accepts commands directly from the Internet without authentication. An attacker only needs to send a fixed 19-byte info probe to force the router to reveal identifying information like its model, firmware version, MAC address, and uptime.

Researchers found that the backdoor's meager security mechanisms could be trivially bypassed: its command payload checksum relies on a static, hardcoded salt ("mqonu.com"), and its internal MAC address filter can be entirely circumvented simply by submitting a MAC field of all zeroes. This allows any remote attacker to easily forge a packet and execute arbitrary commands as root. VulnCheck scanned the Internet and found 203 exposed DARKLANTERN instances in 22 countries, spread across 16 router models.

 ![A diagram showing the surveillance architecture of the DARKLANTERN and SPEAKINGSTONE malware.](https://cdn.mos.cms.futurecdn.net/jwZ9CNfwshp5qmsbudCWx8.png) 


Meanwhile, SPEAKINGSTONE works differently and is even more concerning. Rather than waiting for an attacker to connect to a listening port, it runs as the yunmgrd service and periodically beacons outbound to ZBT's command-and-control infrastructure over UDP port 10000. That makes it useful even when the router sits securely behind NAT or a firewall, as it relies on a custom format dubbed "zbtProtocol" to push full device fingerprints directly to the remote server. SPEAKINGSTONE is also considerably more capable than simply providing a remote shell. According to VulnCheck, its command protocol allows remote operators to execute arbitrary commands, steal WAN PPPoE credentials, rewrite a DNS hijack list, and establish a reverse SSH tunnel.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

The researchers also discovered a backup command server domain embedded in the malware that nobody had registered, so naturally, they registered it themselves. VulnCheck set up a server capable of speaking SPEAKINGSTONE's protocol at the newly registered "www.findmyipaddr.com" and watched the infected routers start calling home.

By August 21st, 392 unique devices had connected to the sinkhole. Fully 390 of those 392 were located in China, with the vast majority using China Mobile's network. Most of those devices were the same router model running the same firmware, suggesting a large-scale carrier deployment rather than random consumer infections. VulnCheck describes this particular deployment as "domestic Chinese surveillance technology."

 ![An infographic showing the global scan results of the DARKLANTERN backdoor, with the majority of infections found in the US.](https://cdn.mos.cms.futurecdn.net/3hq7f4YQVpGg2EiUaAaHgH.png) 


Now, that doesn't mean every ZBT router is a Chinese surveillance device. VulnCheck found ZBT hardware being sold under numerous independent brands worldwide, including Lippert Components, Wave WiFi, OneX in Australia, MoFI Network in Canada, Digineo in Germany, and more. Vulncheck explicitly notes that some of the firmware they examined did not contain the implants. The problem is that ZBT's OEM business makes the hardware's origin surprisingly difficult to identify. The same underlying platforms have appeared under brands including WiFlyer, Deep Orange, Cioswi, CroSkylink and KuWFi, among others.

So the really unsettling part isn't that VulnCheck found three vulnerabilities in an obscure router. It's that these aren't conventional vulnerabilities where someone accidentally forgot to bounds-check a buffer. These are pieces of software deliberately included in the router firmware that provide remote access to the device. We would normally call this malware, but ZBT has described ENDLESSDOORS as an after-sales technical-support mechanism.

VulnCheck's counterargument is pretty compelling; the firm says that whatever its intended purpose, the mechanisms don't securely authenticate the party controlling them. An attacker who can hijack the communications can potentially exercise the same privileges, and because ZBT hardware is frequently sold under other brands, simply not buying something with “ZBT” printed on the box isn't necessarily enough.

If you own one of the affected devices, of which you can find a list at VulnCheck's blog entries for the vulnerabilities (ENDLESSDOORS and the other two), the only real solution is to simply replace it, because the security holes were installed at the factory; it's not as if installing a different firmware version is going to restore trust. Even if your device isn't listed, for anyone running a cheap cellular router, travel router, RV router, or other piece of networking hardware from an obscure OEM, you need to keep in mind that the brand on the plastic probably isn't the company that wrote the firmware, and the fellow who wrote the firmware may not share your values with regard to freedom or privacy.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Zak Killian](https://cdn.mos.cms.futurecdn.net/yonJziSpjzVFahKcUonJvi.jpg)

Zak is a freelance contributor to Tom's Hardware with decades of PC benchmarking experience who has also written for HotHardware and The Tech Report. A modern-day Renaissance man, he may not be an expert on anything, but he knows just a little about nearly everything.

- 
So, those things are everywhere. One day China will know everything about us.Reply
 
 I am not sure if they would be surprised or disappointed.
 
PS: Come to think of it, that package of Ramen noodles has been acting really weird lately. Same thing with the Shu Mai dumplings in my freezer.
- 
Seems like we are being constantly bombarded by Chinese hysteria in the news as of late. We all know who owns most of the news media in the USA now and it's not China, as far as I know. You can read between the lines if you ever feel so inclined.Reply
- 
Reply
Say no more, I know exactly what you're saying. 😎Bigshrimp said:Seems like we are being constantly bombarded by Chinese hysteria in the news as of late. We all know who owns most of the news media in the USA now and it's not China, as far as I know. You can read between the lines if you ever feel so inclined.
