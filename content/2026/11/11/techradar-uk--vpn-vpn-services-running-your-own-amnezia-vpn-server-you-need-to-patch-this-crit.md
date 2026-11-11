---
title: Running your own Amnezia VPN server? You need to patch this critical Linux
  flaw now
source_url: https://www.techradar.com/vpn/vpn-services/running-your-own-amnezia-vpn-server-you-need-to-patch-this-critical-linux-flaw-now
source_site: TechRadar UK
source_slug: techradar-uk
description: Self-hosted Amnezia servers running Xray need a kernel update, a reboot,
  and a fresh Xray install to close a critical Linux hole
image: https://cdn.mos.cms.futurecdn.net/Z8cccYZxkX5QXvAauhJhAn-837-80.jpg
published: '2026-11-11T00:00:00Z'
scraped_at: '2026-11-11T10:51:28Z'
categories:
- Technology & Software
people:
- Claude
- Xinyang Ge
- Xray
locations:
- Amnezia
organisations:
- Amnezia VPN
- AmneziaWG
- Anthropic
- MPTCP
- No Trace
- Xray
---

![Amnezia VPN logo on black background](https://cdn.mos.cms.futurecdn.net/Z8cccYZxkX5QXvAauhJhAn-837-80.jpg)

* **Amnezia VPN has published a three-step guide to protect self-hosted servers from a critical Linux kernel flaw**
* **Servers running the Xray protocol face the highest risk**
* **Amnezia Premium, Free, and Business users don't need to do anything**

Amnezia VPN has warned people who run their own servers through its app that a critical Linux kernel flaw leaves them exposed, and those using the Xray protocol need to rebuild their setups to stay safe.

The bug, tracked as CVE-2026-98432, sits in the code Linux uses to accept new IPv4 TCP connections and has been present since Linux 4.4. The kernel's security team gave it a severity score of 9.8 out of 10.

Even the best VPN is only as secure as the server it runs on, and that's the problem here. Amnezia VPN says its Premium, Free, and Business services are unaffected because the provider has already updated and audited its own infrastructure. Self-hosted users, however, have to act themselves.

![Amnezia VPN — censorship-resistant VPN]([https://cdn.mos.cms.futurecdn.net/ACV243wPtwVxT5MsrphvZQ-200-80.png.webp](https://cdn.mos.cms.futurecdn.net/ACV243wPtwVxT5MsrphvZQ-200-80.png.webp) "Amnezia VPN — censorship-resistant VPN")

**Amnezia VPN — censorship-resistant VPN**  
Amnezia VPN is an affordable, privacy-focused service that prioritizes essentials like security and censorship unblocking over unnecessary extras. All its apps are open-source, albeit more basic than some competitors. It offers both Free and Premium protection, with the latter billed at $28 for six months and $48 for a year. You have 14 days to decide if you like it or not, risk-free, thanks to its money-back guarantee.

## Why Xray servers are most at risk

The flaw is what's known as a race condition — a software bug that tricks an operating system into mishandling its own memory during an internet connection. It was reported by Anthropic researcher Xinyang Ge, and on October 27, Anthropic said an unreleased Claude model had written a working exploit for it.

With zero user interaction and no passwords needed, the exploit could fully take over a vulnerable server in roughly 53 minutes.

The attack targets servers using an advanced networking feature called MPTCP (Multipath TCP) — and that is where Xray comes in.

Xray is the engine behind censorship-resistant protocols like VLESS, and Amnezia rates it as high risk. Because Xray is built with a programming language called Go, it automatically enables MPTCP by default. As a result, server administrators could be leaving this vulnerability wide open in the background without ever realizing it.

![Leave No Trace logo](https://cdn.mos.cms.futurecdn.net/Z7QHFc4GHoMhdps5XmntoC-1200-80.png)

**NEW**:** Leave No Trace** — A weekly newsletter on digital privacy and online surveillance. Leave No Trace investigates the companies and governments putting our digital freedom at risk — and the people fighting back.

📩 Subscribe now to get every edition delivered to your inbox every Friday, launching this September.

## What self-hosted users should do

Amnezia's fix takes three steps and requires version 5.1.0.6 or later of the app.

That release adds a button to update packages on the server directly, which Amnezia says it built in response to this flaw. It follows the provider's Xray-core refresh in September and an earlier mandatory update for Premium and Free users.

> 🔒 Urgent Security Update for Xray Servers Fixed the Linux vulnerability CVE-2026-98432? We’ve put together a step-by-step guide to help you update system packages, reinstall Xray, and secure your self-hosted server. Don’t delay — protect your server today: [https://t.co/APqgAGanlwNovember](https://t.co/APqgAGanlwNovember) 6, 2026

In the app, go to **Settings**, then** Servers**, select your server, and** remove Xray** from the Protocols tab.

Next, open the **Management tab**, choose** Update server packages**, and** reboot** when prompted. The reboot is what loads the patched kernel.

Return to the Protocols tab and **install Xray again**, which now uses the patched version 26.10.31.

Your server will go offline during the reboot, and existing Xray connections will stop working, so you'll need to share access with your users again.

The update button also doesn't guarantee a fixed kernel, and on some Ubuntu versions the patch is still only in the "-proposed" testing channel. Until a future app release fixes it, any later reboot leaves the server vulnerable again until you repeat the Xray reinstall.

If you can't patch the kernel yet, Amnezia suggests a firewall rule that blocks IP options, or removing Xray and switching to the UDP-based AmneziaWG.

Sign up for breaking news, reviews, opinion, top tech deals, and more.
