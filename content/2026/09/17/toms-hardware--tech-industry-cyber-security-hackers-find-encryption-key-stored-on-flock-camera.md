---
title: Hackers find encryption keys stored on stolen Flock camera despite company's
  denials — group extracts more than 27,000 clips, 1.6 million images captured in
  a span of 21 days from the device
source_url: https://www.tomshardware.com/tech-industry/cyber-security/hackers-find-encryption-key-stored-on-flock-camera-group-extracts-more-than-27-000-clips-1-6-million-images-captured-in-a-span-of-21-days-from-device
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-17T13:24:33Z'
published: '2026-09-17T00:00:00Z'
description: Flock claims that images are only briefly stored on its cameras before
  being forwarded to the company’s servers, but a group of hackers determined that
  this wasn’t the case.
image: https://cdn.mos.cms.futurecdn.net/8Ht5WmB2A95EErFNdy8QmN-1920-80.png
---

![a Flock camera with a street in the background](https://cdn.mos.cms.futurecdn.net/8Ht5WmB2A95EErFNdy8QmN.png) 

Flock says that its cameras are protected by on-device encryption, and even though a security researcher noted some flaws in its system, the company said that physical access is still required to exploit them and that the images are only briefly retained on the device before they’re forwarded to the cloud. However, *404 Media* says that a hacking group called stegan0gram found out that this wasn’t the case after they took down a Flock camera positioned over a roadway and analyzed the data stored inside it.

While the hacking group failed to access the most sensitive data stored on the Flock camera, they were still able to access its Android operating system and found two storage partitions, labeled “vendor” and “media.” The latter was found to contain an encryption key that unlocked another partition containing all the media files from the camera. *404 Media* said that that particular Flock camera captured about 1.6 million images across 21 days, detecting around 50,200 vehicles and, more concerningly, 11 people. There were also 27,321 video clips saved on the device — MP4 files with a 1024 x 768 resolution that lasted about a second or two.

Abilities like reading license plates and describing vehicle characteristics like color, make, and model are done on Flock’s servers, but these cameras still retain some edge AI capabilities. This includes detecting people, vehicles, bicycles, and plate-like shapes, which it then crops and sends to the company servers, alongside the original images. Although the software was found to have some facial detection capabilities, the publication said that this was the stock capabilities included in the operating system and wasn’t used by the camera.

This discovery by the hacking group raises another issue with Flock’s system, which is facing a lot of controversies when it comes to privacy and misuse. For example, several police officers have been arrested for using it to stalk romantic partners, while another incident over a mistyped license plate resulted in the unnecessary “ambush” of a car reviewer. Because of this, some towns and cities have ended their contracts with the company, while other people are taking things into their own hands to blind the controversial cameras.

Nevertheless, some critics say that those who are against the deployment of these systems should refrain from damaging or sabotaging these devices, as doing so will only make the authorities feel that these systems are needed. “I think that type of vigilantism will only crystallize the police and the state at large in their belief that this tool is necessary,” former Pawtucket, Rhode Island, police officer Noel Pichardo told the news website. “The longer the state continues to ignore the groanings of their constituents who are against this type of surveillance, the more this will happen.”

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Jowi Morales](https://cdn.mos.cms.futurecdn.net/gM7E2WSDg2wgCFoaDPz9yK.jpg) 

Jowi Morales is a tech enthusiast with years of experience working in the industry. He’s been writing with several tech publications since 2021, where he’s been interested in tech hardware and consumer electronics.
