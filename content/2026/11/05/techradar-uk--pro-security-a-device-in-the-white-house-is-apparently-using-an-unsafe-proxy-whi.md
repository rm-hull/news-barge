---
title: A device in the White House is apparently using an unsafe proxy — which attackers
  could use it 'to reach internal systems'
source_url: https://www.techradar.com/pro/security/a-device-in-the-white-house-is-apparently-using-an-unsafe-proxy-which-attackers-could-use-it-to-reach-internal-systems
source_site: TechRadar UK
source_slug: techradar-uk
description: Someone in the White House “probably installed a sketchy free app on
  their phone"
image: https://cdn.mos.cms.futurecdn.net/UtBhmnGFmNskmYUU3kmSaY-2560-80.jpg
published: '2026-11-05T00:00:00Z'
scraped_at: '2026-11-05T17:29:23Z'
categories:
- Technology & Software
people: []
locations:
- Antarctica
- Ascension
- Chagos Islands
- Falkland Islands
- Pitcairn
- Saint Helena
- South Atlantic
- South Georgia
- Svalbard
- Tokelau
- Tristan da Cunha
- White House
organisations:
- Elon Musk
- Executive Office of the President
- IT
- Layer3 Intel
- Spur
- Sure Saint Helena
- Synthient
- TechRadar Pro
---

![watch biden inauguration day 2021](https://cdn.mos.cms.futurecdn.net/UtBhmnGFmNskmYUU3kmSaY-1920-80.jpg)

* **Researchers spot White House network traffic being routed through dozens of residential proxy services**
* **Findings suggest a device on government infrastructure may have been enrolled in a proxy network**
* **Security experts warn proxy services on sensitive networks could enable abuse, anonymity, and potential lateral movement**

The IT network at the White House was seen routing traffic for at least 28 residential proxy services, meaning there is a strong chance government infrastructure is being abused by (malicious) third parties, cybersecurity experts are warning.

Security researchers at Layer3 Intel published a new report, saying they saw 236 instances of residential proxy traffic originating from AS2650. That is the name of an autonomous system registered to the Executive Office of the President, the federal agency that hosts the White House network.

The researchers observed the traffic between October 5 and November 3 2026, and said that in 26 of the 30 days of observation, six IP addresses kept appearing.

## Dozens of proxies

“This is public access,” the researchers said. “Anybody can obtain it by signing up to a public residential proxy service, paying a few dollars and sending requests through it.”

Residential proxy is a service with a self-explanatory name: paying customers can route their internet traffic through devices connected to residential internet connections (households, essentially), making it appear as though their requests originate from those connections rather than their own. They are not malicious per se, and have legitimate uses, but they’ve become popular among cybercriminals looking to hide their identities, evade security controls, and distribute malicious traffic.

Now, according to Layer 3 intel, 28 different residential proxy providers were able to route traffic through the White House network. The researchers cross-checked the IP addresses against public databases maintained by residential proxy detection companies Spur and Synthient, and both identified them as proxy exits.

Apparently, the researchers did not set out to analyze the White House’s network. Instead, they said they were testing a newly launched platform that “gives researchers a global view of residential proxy and anonymized internet activity,” and stumbled upon the activity while requesting rotating access through residential proxy services.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The cybersecurity community did not seem all too surprised with the news. In a Reddit discussion, IT experts shared their experience with senior leadership, both in public and private sector organizations, saying many were happily sacrificing security for convenience, opting not to install 2FA, or leaving their devices and email inboxes wide open.

One reader suspected someone in the White House “probably installed a sketchy free app on their phone, and now strangers are browsing the internet through the building's connection.”

The timing of the activity is also worth a mention. Around half of the observed connections happened between 5pm and midnight, Eastern time, with almost no activity recorded during the early morning. Layer3 Intel surmised that a device was regularly connecting to the White House network during evening hours, potentially one compromised by a residential proxy SDK.

## Reaching internal systems

“That pattern suggests a person rather than a public guest Wi-Fi network: someone regularly on the White House network late into the evening, whose device is infected with a proxy SDK,” the researchers explained.

The researchers also pointed out that poorly secured proxy SDKs can allow internal network access and lateral movement. “This is how past botnets have spread,” they said. “If an SDK on this network has the same kind of flaw, anyone buying proxy access could use it to reach internal systems.”

There are plenty of other unanswered questions, too. For example, the researchers acknowledged that the data only shows network exits, not specific devices. Therefore, they don’t know if the activity is coming from a personal device, a guest network, or an entirely different source.

The White House discovery was not the only unusual thing Layer3 Intel laid out in its report. They also reported seeing residential proxy activity in some of the most remote players on the planet: Saint Helena, Ascension and Tristan da Cunha, a remote South Atlantic territory. The researchers saw 413 IP addresses and more than 32,000 observations on these locations, involving Elon Musk’s Starlink internet, as well as local internet service provider Sure Saint Helena.

The researchers also detected activity related to residential proxy networks in Antarctica, the Falkland Islands, the Chagos Islands, Tokelau, South Georgia, Pitcairn and Svalbard.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
