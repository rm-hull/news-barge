---
title: $10 Quake shareware CD locked copies of all id Software games behind a flawed
  encryption scheme — pay-over-the-phone system only held up for 39 days after 1996
  release, leaving developer with 150,000 discs it couldn't sell
source_url: https://www.tomshardware.com/video-games/retro-gaming/usd10-quake-shareware-cd-locked-copies-of-all-id-software-games-behind-a-flawed-encryption-scheme-pay-over-the-phone-system-only-held-up-for-39-days-after-1996-release-leaving-developer-with-150-000-discs-it-couldnt-sell
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-19T13:09:38Z'
published: '2026-08-19T00:00:00Z'
description: Nice software you have there; shame if anyone was to QCRACK it
image: https://cdn.mos.cms.futurecdn.net/KeSsu2KwokVwaR4LSBRDFL-1920-80.png
---

![a person playing Quake III on a computer from 2001](https://cdn.mos.cms.futurecdn.net/KeSsu2KwokVwaR4LSBRDFL.png) 

![](https://cdn.mos.cms.futurecdn.net/TLXiX9HLvb9cMwKhSSLXYg-200-100.png) 

Back before fast broadband internet came to most homes, game developers released their latest titles through shareware CDs so gamers could try them out before buying. And that's what id Software did when it released *Quake* in 1996.

As recounted by Google software engineer Fabien Sanglard, the company put both a shareware version and the complete version of *Quake* on a CD for just $10. But because the shareware version*and* the complete game only took up 22MB of a 640MB CD, the remaining 618MB had practically no use. id Software came up with the idea of including full, encrypted versions of all its other titles of the time on the CD, too.

If you wanted to unlock any of the full games on the disc, you just needed to call the “Quake Unlock Center," present a challenge code displayed by a program on the CD, and hand over your credit card details (or your parents'), after which the person on the other end would give you a code to unlock your game of choice.

That was a brilliant concept on the surface, as gamers who picked up *Quake* could just as easily buy any other id game they wanted without having to go to a local retailer. It also meant cutting out the middleman, allowing the developer to get the bulk of the proceeds of the sale.

Unfortunately, the developer underestimated the threat of hackers and crackers to this model. Freeloaders took to breaking the CD’s encryption as soon as it was released. It took hacker group GNOMON just 39 days to release a tool—QCRACK.exe—that could generate serial numbers for all the games on the CD, making for an incredible return on investment for that $10.

It turned out that id and TestDrive, a DRM company it had contracted to create the shareware disc, had relied on a form of security by obscurity. Even though the serial number that the agent handed back to anyone buying the game over the phone was semi-random due to the rotating challenge code the unlocking program asked buyers to present along with their payment, it could also be generated using data permanently molded onto the disc.

And in the days before online authentication, that hard-coded data proved to be the downfall of the entire scheme. The app that unlocked the full version of the games worked by checking whether the serial number the owner typed in matched one generated from the hard-coded local data. If one were to derive the scheme used to retrieve serial numbers according to the challenge code, one could bypass the need for payment entirely.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

And that's exactly what the GNOMON hackers did in a little over a month. The hacking group did not reveal how it built the cracker, and the inner workings of the crack were only revealed in 2018 through reverse-engineering performed by Ruben Molina.

No matter how the GNOMON figured out id Software’s protection, this revelation was an absolute disaster for the company. In the end, it had to stop the distribution of the shareware CDs, meaning it ended up with 150,000 discs that it couldn't sell because of the existence of the crack.

The Quake crack shenanigans show that the race between game publishers and pirates has been going even before the advent of the internet. Even today, the infamous Denuvo DRM has already been cracked in all single-player games that it protected, rendering it effectively useless. Still, the company is likely taking steps to harden its DRM app in this cat-and-mouse game between anti-tamper software and pirates.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Jowi Morales](https://cdn.mos.cms.futurecdn.net/gM7E2WSDg2wgCFoaDPz9yK.jpg)

Jowi Morales is a tech enthusiast with years of experience working in the industry. He’s been writing with several tech publications since 2021, where he’s been interested in tech hardware and consumer electronics.
