---
title: Robot vacuum flaw lets one stolen certificate run root commands on other Shark
  robovacs in the same AWS region — unpatched flaw exposes live camera feeds, stored
  home maps, and Wi-Fi credentials
source_url: https://www.tomshardware.com/tech-industry/cyber-security/shark-robot-vacuum-flaw-lets-one-stolen-certificate-run-root-commands-on-others-in-the-same-aws-region
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-17T13:59:23Z'
published: '2026-07-17T00:00:00Z'
description: The flaw exposed live camera feeds, stored home maps, and Wi-Fi credentials
  held in plaintext
image: https://cdn.mos.cms.futurecdn.net/xHYaeGUrtwRYLr4vErMHoG-1920-80.jpg
---

![a smart vacuum being set up with a smart phone](https://cdn.mos.cms.futurecdn.net/xHYaeGUrtwRYLr4vErMHoG.jpg) 

A security researcher has published a method for lifting the client certificate off a Shark robot vacuum and using it to run root commands on other Shark vacuums across the same Amazon Web Services region, exposing live camera feeds, stored home maps, and Wi-Fi credentials held in plaintext. The researcher, who publishes under the handle tokay0, published the technique on Monday and says he first reported it to SharkNinja on March 1. As of the time of writing, the flaw is still unpatched, requiring a fix that sits entirely on SharkNinja's side of the cloud rather than on the robot.

 ![Microsoft data center in Mount Pleasant, Wisconsin](https://cdn.mos.cms.futurecdn.net/Vh4nY3pMCcmra2ymXah9S7.jpg) 


The problem is an over-permissive AWS IoT policy. The certificate that a Shark vacuum uses to authenticate to Amazon's cloud broker was never restricted to the device carrying it, so a certificate pulled from one unit can subscribe to fleet-wide traffic and publish commands addressed to any device the broker serves. Those commands travel in an ordinary field called Exec_Command inside the per-device state document AWS keeps in the cloud, and a management daemon on the vacuum passes anything under 1,000 bytes from it to a shell.

The researcher tested the technique only on units he bought himself, including a cross-model reverse shell on an AV1102ARUS Shark IQ Robot Vacuum XL, which he then used to pull a live feed off that robot's onboard camera. Watching a single AWS region for 24 hours, he counted 1,517,605 unique Shark serial numbers, of which 673,816, or 44%, replied to a command probe. Those are devices observed responding, not devices he tested or compromised. Certificates are pinned to their AWS region, so a key lifted in one region only reaches devices in that region.

tokay0 says SharkNinja acknowledged his report on March 12, told him on April 27 that it was under review, and on July 3 promised a completion date by July 10 that never arrived. He also says the company downplayed the severity and questioned whether a CVE was warranted, despite a published disclosure policy that commits SharkNinja to "provide regular updates until the reported vulnerability is resolved." The company had posted nothing on the flaw as of July 16.

Remediation in this scenario doesn’t require a firmware update. Per Amazon, a non-compliant IoT policy is fixed by pushing a scoped version inside the operator's own AWS account until SharkNinja rescopes the policy or reissues the certificates.

SharkNinja's timeline is pretty similar to a vulnerability we saw with DJI Romo vacuums back in February, whereby an authorization flaw exposed roughly 6,700 vacuums, handing out camera feeds, audio, and floor plans; DJI patched it within weeks, and the researcher who found it later collected a $30,000 bounty. Cloud-side failures, where a backend fails to scope device access, have driven a run of robot-vacuum breaches and fueled interest in fully offline designs that keep mapping and camera data off any vendor cloud.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Luke James](https://cdn.mos.cms.futurecdn.net/C4FAi2KzwaGLUrBqzX5aBM.png)

Luke James is a freelance writer and journalist. Although his background is in legal, he has a personal interest in all things tech, especially hardware and microelectronics, and anything regulatory.
