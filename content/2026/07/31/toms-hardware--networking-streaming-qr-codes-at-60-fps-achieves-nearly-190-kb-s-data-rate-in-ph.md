---
title: Streaming QR codes at 60 FPS achieves nearly 190 KB/s data rate in phone-to-phone
  tests — browser-based method requires no app, no networking, no pairing, and no
  permissions beyond camera access
source_url: https://www.tomshardware.com/networking/streaming-qr-codes-at-60-fps-achieves-nearly-190-kb-s-data-rate-in-phone-to-phone-tests-browser-based-method-requires-no-app-no-networking-no-pairing-and-no-permissions-beyond-camera-access
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-31T14:30:09Z'
published: '2026-07-31T00:00:00Z'
description: Dev wanted a simple method for transfering audio files between devices
  on different networks.
image: https://cdn.mos.cms.futurecdn.net/fXQe58AnUePbo8yhUABSuY-1920-80.jpg
---

![Decimen Optical Transfer: fountain-coded QR file transfer](https://cdn.mos.cms.futurecdn.net/fXQe58AnUePbo8yhUABSuY.jpg) 

A developer has created a proof-of-concept data transfer system that shuns any dedicated app requirement and neatly sidesteps mandatory networking, pairing, or giving permissions beyond camera access. Instead, the method transmits information between devices by streaming data via rapidly updating QR codes at up to 60 FPS via the browser your smartphone already has. The test info shared by developer bashalarmistalt on GitHub backs claims that these transfers can run at up to 190 KB/s. This low-friction two-device screen-to-camera data transmission technique is dubbed Decimen Optical Transfer: fountain-coded QR file transfer.

The GitHub project is linked to by Redditor Alstroph, who seems to be the same person. We’ve chosen to embed the Reddit post about the Decimen Optical Transfer solution above, as it includes an illustrative video of a QR code-driven data transfer.

Bashalarmistalt/Alstroph says they used Claude Code to build this cached web app, which simply runs on both smartphones within the browser, with camera permissions given. They explain that they came up with the idea behind Decimen Optical Transfer to create “a phone-to-phone file transfer option without requiring the phones to be on the same network.” After a modicum of chin stroking, they settled upon the possibility of using “rapidly flashing QR codes” to brew up this proof-of-concept.

Far more detailed information about the project is available in the GitHub repository, linked above. There we also read that the use of ‘fountain codes’ was instrumental to the technique, ensuring missed frames and retransmission quirks don’t hinder the data transfer process. Also, it is explained that every streamed QR code frame is self-describing, as a “20-byte header carries the session ID, sequence number, block count/size, file length, and a hash.”

Hints are provided for tuning Decimen Optical Transfer performance with the PoC solution. The dev used an iPhone and the Apple ProMotion camera with stacked codes; they achieved ~128 KB/s handheld data transfers. The data rate could climb to ~186 KB/s speeds if both the sender and receiver devices were positioned absolutely stationary.

The Decimen Optical Transfer software is distributed under the generous MIT license. Bashalarmistalt is aware that there have been several prior projects but asserts the concept behind their Claude Code-aided solution was arrived at independently. We’ve also covered QR code-based data storage tech numerous times. For example, Cerabyte famously uses microscopic QR codes for its ultra-long-life ceramic storage.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Mark Tyson](https://cdn.mos.cms.futurecdn.net/56vqMYLDaKRHPhHZgbADFR.jpg)

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.
