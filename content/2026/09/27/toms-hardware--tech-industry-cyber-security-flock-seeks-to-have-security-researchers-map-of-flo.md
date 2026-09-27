---
title: Flock seeks to have security researchers' map of Flock cameras taken down —
  unauthenticated flaw exposed 335,701 camera locations nationwide
source_url: https://www.tomshardware.com/tech-industry/cyber-security/flock-seeks-to-have-security-researchers-map-of-flock-cameras-taken-down-unauthenticated-flaw-exposed-335-701-camera-locations-nationwide
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-27T16:59:58Z'
published: '2026-09-27T00:00:00Z'
description: It could also potentially be used to track key personnel heading to and
  from sensitive sites like military bases, intelligence agencies, and law enforcement
  headquarters.
image: https://cdn.mos.cms.futurecdn.net/zijwMhUjw6Sbp3f8HhJuxP-1920-80.png
categories:
- Technology & Software
- Hardware
people:
- Flock
- Joshua Michael
- Tom
locations: []
organisations:
- CIA Headquarters
- Doppel
- Eglin AFB
- FBI Headquarters
- Flock Safety
- Flock Surveillance Map
- Get Tom's Hardware
- Google News
- Joint Base Andrews
- Jowi Morales
- Pentagon
---

![a Flock license plate reader mounted on a stoplight at an intersection](https://cdn.mos.cms.futurecdn.net/zijwMhUjw6Sbp3f8HhJuxP.png)

A security researcher discovered a vulnerability in Flock’s website that gave him an access token without needing login credentials. The researcher used the information gleaned to build a map of Flock cameras and share it on a website he named the Flock Surveillance Map, which now lists the location of 335,701 cameras. Flock has now issued a trademark infringement complaint with the goal of having the researcher close the website.

According to *The Intercept*, Joshua Michael used this to query ArcGIS, a third-party mapping and geospatial layer that Flock uses, to retrieve a database of Flock devices in November 2025.

Michael said that he immediately informed the company about the security flaw. He said in his email, dated Nov. 13, 2025, that “all testing was strictly non-intrusive, limited to open unauthenticated endpoints, and did not involve bypassing authentication, modifying data, or invoking any billable ArcGIS or Google operations.” However, the company did not reply to his message, and it took him two more attempts before a representative responded. Flock said in its response, “Thank you for the findings. We are internally triaging them and will reach back out with next steps soon,” but the researcher said that the company still hasn’t replied to this day.

Flock apparently fixed the vulnerability in January of this year after Michael published his findings, but the researcher was able to exfiltrate a Flock device location database before that. This information has allowed him to build the Flock Surveillance Map website, which lists 335,701 cameras, presumably updated in December 2025.

The surveillance company said that it has never been hacked, that Flock information has never been leaked, and that the Flock Safety cloud platform “has never experienced a data breach,” but Michael says that this does not reflect reality. He told *The Intercept* that it made this announcement “after I pulled their database of devices.” “That leaves two possibilities,” said the researcher. “Either they knew and chose not to disclose it for fear of bad press, or they didn’t know I exfiltrated the data at all. The first is a transparency failure. The second is a detection failure with national security implications.”

This issue once again raises questions about the company’s cybersecurity and privacy measures. Hackers have recently discovered that the Flock cameras stored encryption keys directly on the device, which allowed them to extract more than 27,000 clips stored and find that it has taken more than 1.6 million images in a span of 21 days. There were also multiple instances of misuse, in which police officers used the system to stalk romantic partners, while a car reviewer was “ambushed” in a store parking lot and detained for an hour for a mistyped police report.

What’s more alarming was that Michael pointed out that the ubiquity of the system and the vulnerabilities he uncovered so far show that it could be used to track personnel. Soldiers and civilians working in the defense industry could potentially be observed going to and from 22 sensitive sites, including Eglin AFB, CIA Headquarters, FBI Headquarters, Joint Base Andrews, and even the Pentagon, with people living within a 20-mile radius of these sites having a 57.22% to 93.94% chance of passing a Flock camera and getting recorded in the system.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

While Flock did not comment on *The Intercept’s* reporting before publication, Michael noted that he received a trademark infringement complaint on his site. Doppel, a cybersecurity company focusing on social engineering defense, reached out on behalf of the surveillance company and said that he’s using the trademark “FLOCK SAFETY” without authorization and that it may confuse its customers. Because of this, the firm requested that the Flock Surveillance Map website be taken down, despite a pop-up that appears on the website when accessed for the first time saying otherwise.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Jowi Morales](https://cdn.mos.cms.futurecdn.net/gM7E2WSDg2wgCFoaDPz9yK.jpg)

Jowi Morales is a tech enthusiast with years of experience working in the industry. He’s been writing with several tech publications since 2021, where he’s been interested in tech hardware and consumer electronics.

* Hey, since you use these two words in that specific order in one place on your website, take down the entire website. It isn't about the embarrassing data exfiltration, it is totally, 100% about the trademark infringement.Reply
* So the security company that cant even properly secure its website is going to claim "trademark infringement" because that hole exposed their bad security (even more than we already knew) AND made it readily visible just how expansive their garbage tech has become?Reply  
    
  Not a good look at all. Its just one well-deserved L after L for this company. Looking forward to their eventual crash and burn.
