---
title: Another top router maker accused of firmware having backdoors — Chinese giant
  Zbtlink halts downloads to fix issue
source_url: https://www.techradar.com/pro/security/another-top-router-maker-accused-of-firmware-having-backdoors-chinese-giant-zbtlink-halts-downloads-to-fix-issue
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-07T00:56:29Z'
published: '2026-08-06T00:00:00Z'
description: Zbtlink denies allegations, but still moved to address them
image: https://cdn.mos.cms.futurecdn.net/k7eZeuNMn4MG3KGYmaJHD9-2560-80.jpg
---

![Someone cutting a network cable linked to a router](https://cdn.mos.cms.futurecdn.net/k7eZeuNMn4MG3KGYmaJHD9.jpg) 

- **VulnCheck CTO Jacob Baines reported Zbtlink routers shipped with a built‑in backdoor dubbed**-** ENDLESSDOORS**-**, allowing remote root commands and reverse shells**
- **Zbtlink denied malicious intent, calling it an after‑sales maintenance feature, but quietly pulled vulnerable firmware and promised patches**
- **Researchers warn all firmware images are hijackable; mitigation advice is to replace devices or enforce strict egress controls and treat LAN as untrusted**

Chinese networking firm Zbtlink has been accused of shipping its products with a backdoor - and while the company denies the allegations, it has still apparently moved to address the issue.

CTO of cybersecurity company VulnCheck, Jacob Baines, recently published an in-depth report stating a Zbtlink device he runs “continuously attempts to reach a command-and-control server on the internet.”

“Zbtlink routers phone home, waiting for orders. Not because they were hacked. Because they were shipped that way.”

## Detention and escape attempts

Baines dubbed the flaw “ENDLESSDOORS” and says it was uploaded to GitHub in early 2015 and “never touched again”. “It can send the client individual shell commands or tell the client to spawn a reverse bash shell.”

“The vocabulary of this protocol is two phrases: run this as root, and give me a root shell,” he further explained, saying that anyone along the path can hijack the client/server communication. VulnCheck researchers tried it, and apparently - succeeded.

Baines said that every firmware on the company’s download page (roughly two dozen images) is all “hijackable in the same way”, and said the company decided not to “responsibly disclose” the vulnerability since that assumes the vendor did not intend the behavior. "That assumption doesn't hold here."

In response to the allegations, Zbtlink told***The Register* VulnCheck mischaracterized the code.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

“This feature is solely intended for after‑sales maintenance and serves no other purposes,” the company told the publication. “It is generally retained only on sample units to assist customers with software debugging and will not be included in mass‑production shipments.”

*The Register* didn’t see it as a credible explanation since, in the meantime, the company posted a warning on its downloads page:

“We have detected firmware security vulnerabilities affecting selected router firmware releases. As a precautionary measure, the impacted firmware versions have been temporarily taken down from download channels. Our engineering team is working intensively to develop and validate secured patched firmware.” This warning was allegedly posted sometime in the past seven days.

Baines gave a list of suggestions how to mitigate the risk but ended up saying that “for anything carrying real traffic, our advice is to replace the device, or at minimum move it behind strict egress control and treat its LAN as untrusted.”

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
