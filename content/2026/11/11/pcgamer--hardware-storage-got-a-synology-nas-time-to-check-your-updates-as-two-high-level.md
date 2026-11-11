---
title: 'PSA: Update your Synology NAS to fix some nasty security vulnerabilities'
source_url: https://www.pcgamer.com/hardware/storage/got-a-synology-nas-time-to-check-your-updates-as-two-high-level-vulnerabilities-let-neer-do-wells-read-and-write-files-and-conduct-ddos-attacks/
source_site: PC Gamer
source_slug: pcgamer
description: Big oof.
image: https://cdn.mos.cms.futurecdn.net/csYBBfR3NRUwQc6kRSL7vh-1920-80.jpg
published: '2026-11-11T00:00:00Z'
scraped_at: '2026-11-11T19:35:02Z'
categories:
- Technology & Software
people:
- Henry
locations:
- GameSir
organisations:
- ASAP
- DiskStation Manager
- Elgato Facecam
- NAS
- PC Gamer Circuit Breaker
- Razer BlackShark V34
- Razer Viper
- SQL
- Secretlab Magnus Pro XL3
- Secretlab Titan Evo2
- Shure
- Synology
- Wireless5
---

![KCD 2 lockpicks - Henry picking a chest](https://cdn.mos.cms.futurecdn.net/csYBBfR3NRUwQc6kRSL7vh-1920-80.jpg)

Another day, another cybersecurity update. This time, it's the turn of immensely popular NAS provider Synology to advise its users about some now-fixed gaping holes. The company has updated its DiskStation Manager (DSM) operating system, patching out two security vulnerabilities in various product versions.

Just another patch? Not quite. The first of these vulnerabilities has a CVSS3 base score of 9.8 out of 10, which makes it of "critical" severity (via International Cyber Digest on X). According to the company:

"An improper neutralization of special elements used in an SQL command vulnerability in the Auth API in Synology DiskStation Manager (DSM)... allows remote attackers to read or write arbitrary files and conduct denial-of-service attacks."

That's a pretty big security hole if I've ever seen one, particularly for those storing extremely important data on their home NAS setup. The second one gets a lower severity rating of 8.6, but also manages to allow attackers to skip the login process.

Synology describes the second vulnerability as "An authentication bypass using an alternate path or channel vulnerability in the rsync in Synology DiskStation Manager," which can again lead to unwanted reads, writes, and DDOS shenanigans.

> ‼️BREAKING: A critical flaw in Synology NAS devices lets attackers read and write any file on them without logging in. The SQL injection bug in their login system scores 9.8 out of 10. A second flaw, in rsync, skips the login too. Synology patched both today. Update ASAP. [https://t.co/LlS328SBf4November](https://t.co/LlS328SBf4November) 11, 2026

The company also notified users late last month of ransomware attacks related to a 2024 security advisory, for what looks to be a series of separate vulnerabilities. One way or the other, the latest updates look to have rolled out to many users already, but it's still worth checking to make sure you're on the newest builds to plug all these leaks.

After all, auto updaters are far from perfect. 2026 has been a year characterised by cybersecurity issues, and it'd really put the tin lid on it if your home NAS was broken into by some unscrupulous character. A reminder to keep on top of your updates no matter the device, methinks. Stay safe out there, folks.

The PC Gamer Circuit Breaker newsletter breaks down the latest PC gaming tech, and finds you the best deals on the best products

![Secretlab Titan Evo gaming chair in Royal colouring, on a white background](https://cdn.mos.cms.futurecdn.net/7rTxS5WgHWFPDRsqLd28vh-140-80.png)

**1. Best gaming chair: Secretlab Titan Evo2. Best gaming desk: Secretlab Magnus Pro XL3. Best gaming headset: Razer BlackShark V34. Best gaming keyboard: Asus ROG Strix Scope II 96 Wireless5. Best gaming mouse: Razer Viper V4 Pro6. Best PC controller: GameSir G7 Pro7. Best steering wheel: Logitech G Pro Racing Wheel8. Best microphone: Shure MV6 USB Gaming Microphone9. Best webcam: Elgato Facecam MK.2**
