---
title: Retired Microsoft Engineer details the story about the famous leaked FCKGW
  Windows XP key — copy protection used 10MB of encrypted Microsoft Bob for validation
source_url: https://www.tomshardware.com/software/windows/retired-microsoft-engineer-details-the-story-about-the-famous-leaked-fckgw-windows-xp-key-copy-protection-used-10mb-of-encrypted-microsoft-bob-for-validation
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-17T13:24:34Z'
published: '2026-09-17T00:00:00Z'
description: Next. Next. Click. FCKGW-RHQQ2-YXRKT-8TG6W-2B7Q8. Enter.
image: https://cdn.mos.cms.futurecdn.net/H4E9BVRtDNfdDadU857N8-1008-80.png
---

![Windows XP CD](https://cdn.mos.cms.futurecdn.net/H4E9BVRtDNfdDadU857N8.png) 

Anyone old enough to be messing with PCs in the early to mid-2000s probably has the following burned into their mind: FCKGW-RHQQ2-YXRKT-8TG6W-2B7Q8. That's neither a magic spell nor a password for a cabal — it's the best-known Windows XP key, letting anyone install and run the operating system with its incantation and just the one CD. Ever wondered how or why Microsoft let such an apparent gaping hole in its copy protection? Former engineer Dave Plummer explained in an X post.

First off, there were actually two versions of the original Windows XP media: Retail and Volume. The former was for anyone who just bought the OS off the shelf, while the latter was reserved for Microsoft partners and OEMs that needed to easily install it on thousands of machines without needing to individually activate every single one at install time.

Retail and Volume media had different keys, too, and the installer would validate the key you input against specific data on the disk, "encrypted so hard that even today it hasn't been decrypted [...]" (Someone will take those words as a challenge). The magical piece of cryptic data was nothing other than the whole 10 MB of... Microsoft Bob. The short-lived assistant was technically the antecessor of the much-maligned and memed-upon Clippy, and did its best in 1995 to introduce newbies to basic computing tasks.

Regular Joes and Janes weren't supposed to be anywhere within a stone's throw of a Volume disc, though, as those were strictly enterprise-only. The final version of the CD, called Release to Manufacturing, or RTM, was complete in August 24, 2001 — two months before the official launch on October 25. The discs were available to OEMs and partners before the release date so those companies could have their wares ready with Windows XP on them.

Plummer notes that "very few" organizations had access to the Volume image and the corresponding Volume License Key (VLK) and believes that someone at a major OEM, potentially Dell or Intel, leaked the Volume media and the key together before the official release. The pirate group Devils0wn then quickly spread it online for everyone to enjoy

Later on, when Service Pack 1 arrived, the FCKGW key was among the 640 blacklisted from the operating system due to leakage. Service Pack 2 and its Windows Genuine Advantage checks went a couple steps further and blocked updates entirely on machines with a blacklisted VLK. Plummer states that Microsoft didn't want to cause unnecessary trouble for customers, hence its *laissez-faire* attitude and choice to stick to just blacklisting affected keys.

Many theories over the years proposed that the FCKGW key worked because Microsoft's key generation algorithm was very basic, a notion outright dismissed by Plummer. He plainly states that algorithm was written by "ACTUALLY smart guys with heads so big that they bumped the doorjamb on the way into your office."

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

The truth of the situation was far simpler: as is usual with computing, ultimately the problem was between the keyboard and the chair. It's a good a time as any to reminisce about that compact disk you totally don't have on a bookshelf somewhere with the FCKGW key written on it with a Sharpie.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png) 

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.

- 
Just a heads-up, there's a typo in the articleReply
 
 The short-lived assistant was technically the **antecessor** of the much-maligned and memed-upon Clippy, and did its best in 1995 to introduce newbies to basic computing tasks.
