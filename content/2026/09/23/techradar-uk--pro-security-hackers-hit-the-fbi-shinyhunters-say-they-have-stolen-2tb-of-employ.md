---
title: Hackers hit the FBI — ShinyHunters say they have stolen 2TB of employee data,
  but the attack isn't looking for money, just an apology
source_url: https://www.techradar.com/pro/security/hackers-hit-the-fbi-shinyhunters-say-they-have-stolen-2tb-of-employee-data-but-the-attack-isnt-looking-for-money-just-an-apology
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-23T19:39:35Z'
published: '2026-09-23T00:00:00Z'
description: ShinyHunters are looking to improve their standing in the public eye
categories:
- Technology & Software
image: https://cdn.mos.cms.futurecdn.net/Ri2dNNTvgmKGsMuhNDCavZ-2560-80.jpg
---

![Dark web monitoring](https://cdn.mos.cms.futurecdn.net/Ri2dNNTvgmKGsMuhNDCavZ.jpg)

* **ShinyHunters defaces FBI’s jobs site, claiming a PeopleSoft zero‑day let them steal 2TB of HR data**
* **Group says attack is not for ransom but to dispute FBI’s May PSA alleging harassment and swatting tactics**
* **Experts warn exploit itself is highly valuable; FBI site reclaimed, investigation ongoing into breach claims**

The ShinyHunters extortion group is currently doing brand management in the most ShinyHunters way possible - by hacking into the FBI and stealing the agency’s sensitive files.

The Bureau’s jobs site was defaced and replaced with the usual ShinyHunters content - an ASCII image of the group’s logo, and a message saying “This site has been seized by ShinyHunters. Rooting your systems since ‘19 :)”.

But instead of putting the FBI on its data leak site and threatening to release stolen files if a ransom isn’t paid, ShinyHunters started speaking to the press, telling *The Register* it found a zero-day vulnerability in the Oracle PeopleSoft human resource management system, which allowed them to remotely execute arbitrary code on the underlying server.

They used this ability to (allegedly) steal more than 2TB of sensitive data from the FBI’s servers, including names, addresses, phone numbers, and information on spouses for current, former, and prospective FBI employees.

“We hold data on all FBI employees and applicants,” the spokesperson told *The Register*, noting they had compromised human resources, MedLink, and Criminal Justice Information Services.

## Brand management

The FBI has yet to comment, and so do both Oracle and AWS, but what’s most peculiar about this incident is that it doesn’t seem to be financially motivated.

So far, everything ShinyHunters’ have been doing was for the money. They would break into a company, steal their files, and then pressure the victims into paying a ransom demand in exchange for deleting the stolen information. This time around, the group claims the goal of the attack is to force the FBI to change the record on how it operates.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

“This is NOT financially motivated,” the group told *The Register*. “We want the FBI to correct or retract their statements they made, which included substantial false allegations.”

The statements were made in a security bulletin published on May 15 this year, right after the Canvas attack. In early May 2026 Instructure, the edtech giant behind the popular Canvas learning system, confirmed suffering a cyberattack and losing sensitive customer data. It was later disclosed that some of the world’s top universities, including Harvard, Oxford, and MIT, were among the victims.

The attack was so disruptive that Instructure’s CEO was called to testify in front of the US House Committee on Homeland Security a few weeks later.

On May 15, the FBI issued a public service announcement (PSA) saying ShinyHunters “commonly use harassment strategies” to exert pressure on victims, including “sending threatening text messages and phone calls to victims and their family members, and in some cases, swatting.”

Swatting means calling the police to report criminal activity so severe that the SWAT team is sent. This is usually done to live streamers as a practical, albeit life-threatening, joke.

“Threat actors may falsely claim to have sensitive or compromising information, including embarrassing photographs or videos of victims, which frequently do not exist. Following these pressure tactics, SH actors have sometimes posted exfiltrated data to various iterations of the SH data leak site on the Tor network,” the PSA concluded.

“I have been doing my very best to combat these allegations,” ShinyHunters told the media. “And this is the best way to do it.”

## No money?

Not everyone is sold on the idea that ShinyHunters isn’t doing this for the money.

In a statement shared with TechRadar Pro, CTO of Suzu Labs, Denis Calderone, said the claims should be taken with a grain of salt: “I have a hard time believing terabytes of FBI personnel data just sit on a shelf. Foreign intelligence services would love to have it, and having the FBI on their resume makes every future extortion demand more believable, and if the PeopleSoft zero-day is real, the exploit may be worth more than the data. Meanwhile, agents and their spouses could have their home addresses posted publicly within a week if this threat is followed through.”

Calderone also stressed that instead of focusing on the incident, people should be paying more attention to the zero-day.

“If you run PeopleSoft, don't wait for a patch. Get it off the public internet wherever you can, put what has to stay public behind a WAF, and make sure admin components like the /PSEMHUB/ path in their screenshot aren't reachable from outside. Hunt for the June indicators and for SSH attempts against the psoft and oracle accounts. Then ask yourself what your applicant portal can reach. At the FBI, a website built for strangers to upload resumes allegedly led straight into GovCloud.”

The FBI has since reclaimed its website, which now says it is under maintenance.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png)

![Google logo on a black background next to text reading &#039;Click to follow TechRadar&#039;](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg)

***Follow TechRadar on Google News***and** add us as a preferred source** * to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
