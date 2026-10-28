---
title: A security flaw in these widely used barcode scanners could open up warehouses
  and stores to cyberattack
source_url: https://www.techradar.com/pro/security/a-security-flaw-in-these-widely-used-barcode-scanners-could-open-up-warehouses-and-stores-to-cyberattack
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-28T19:25:46Z'
published: '2026-10-28T00:00:00Z'
description: A simple barcode scanner could be the gateway to a large-scale cyberattack
image: https://cdn.mos.cms.futurecdn.net/4ZfeZkmNTqyXyHPQxVPADT-2560-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Kaspersky
- Sergey Sidorov
locations: []
organisations:
- Industrial Security Services
- Interact Analysis
- Kaspersky
- PDR
- Portable Data Terminals
- TechRadar Pro
- WMS
- Warehouse Management Systems
---

![](https://cdn.mos.cms.futurecdn.net/4ZfeZkmNTqyXyHPQxVPADT-1920-80.jpg)

* **Researchers find Bluetooth flaws in warehouse barcode scanners that could provide a foothold into enterprise networks**
* **Attackers could spoof scanner input, inject keystrokes, and potentially pivot to ransomware or data theft**
* **Kaspersky urges stronger device authentication, network segmentation, and stricter security controls for warehouse infrastructure**

Cybercriminals could use barcode scanners in warehouses to break into IT infrastructure and wreak havoc, security researchers have claimed, urging organizations to take preemptive measures and secure their warehouse grounds before it’s too late.

Kaspersky researchers set out to see if there are any hidden attack vectors on warehouse infrastructure and are now claiming they found one through a barcode scanner model “from a major manufacturer”.

## Opening the floodgates

In a report shared with TechRadar Pro, Kaspersky said the vulnerable device has two components: the handheld scanner, and the base station, which is then connected to a workstation, or a separate business system.

The two components communicate via Bluetooth, but apparently there are no authentication methods between the two.

So, in theory, a malicious actor could obtain the Bluetooth address of the base station through passive eavesdropping on Bluetooth traffic. Then, through the established Bluetooth connection, they could send a malicious payload to the base station which simulates keyboard strokes. The base station would “think” the keystrokes are legitimate, coming from the user of the handheld device, and forward them to the connected workstation or separate business system.

“This attack pattern was observed across devices from multiple vendors,” Kaspersky said in its report.

Through this method, a theoretical attacker could gain an initial foothold on a computer within the warehouse network. Obviously, the scanner is only the entry point and not the actual target. The target is the wider network, where malicious actors could conduct reconnaissance, exfiltrate sensitive information, or deploy malware and ransomware.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

“Modern retail and logistics are profoundly digital, from enterprise-wide management platforms down to every device in a worker’s hands. This pervasive connectivity means that any technology at any tier can become an entry point for a cyberattack capable of destabilising the entire ecosystem — as our research shows, even a single barcode scanner”, said Sergey Sidorov, Head of Industrial Security Services at Kaspersky.

“The warehouse sector, and the broader retail industry, should treat cybersecurity as a top priority across every layer of their operations,”

## Are other devices vulnerable, too?

Kaspersky says the same scenario can be applied to other warehouse devices like Portable Data Terminals (PDR), or thermal printers, to gain access to Warehouse Management Systems (WMS) and similar infrastructure.

Therefore, the researchers are urging companies to secure their environments by verifying every new device before it connects to the network, disabling any unused Bluetooth interfaces, enforcing strong authentication mechanisms, segmenting warehouse networks so that only essential connections are permitted, applying security updates to both devices and the WMS as soon as possible, restricting account permissions to the minimum required, and regularly conducting full‑scale attack‑path exercises.

Unfortunately, we don’t know the name of the manufacturer, or how many devices in a series could be susceptible. The researchers are saying the risk is quite large, since these devices are “widely used” in warehousing, retail, and multiple other sectors.

Global e-commerce sales are expected to reach $6.88 trillion this year, making up more than a fifth (21.1%) of total retail sales worldwide.

At the same time, according to logistics research firm Interact Analysis, there are more than 180,000 warehouses in the world, so the attack surface could be significant. But warehouses are not the only sector at risk here. Barcode scanners and related handheld terminals are also widely used in retail stores, manufacturing facilities, hospitals, pharmaceutical operations, and transportation networks.

There is no reliable way to estimate how many organizations are vulnerable, but the possibility of using an everyday operational device to gain access to a connected workstation makes the findings relevant to a broad range of industries.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
