---
title: Game Compressor can save you hundreds of GB across your game library — as storage
  prices remain high, utility leverages Windows' built-in LZX compression for substantial
  space savings
source_url: https://www.tomshardware.com/pc-components/storage/game-compressor-can-save-you-hundreds-of-gigs-across-your-game-library-usd6-utility-leverages-windows-built-in-lzx-compression-for-substantial-space-savings
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-25T13:57:32Z'
published: '2026-07-25T00:00:00Z'
description: A breath of fresh air in these storage-troubled times.
image: https://cdn.mos.cms.futurecdn.net/Sa3JjkGH2ibKFh5khdocHo-1024-80.png
---

![Game Compressor](https://cdn.mos.cms.futurecdn.net/Sa3JjkGH2ibKFh5khdocHo.png) 

With NAND prices flying into the stratosphere, buying a large SSD has become a cold-sweat-inducing event, with even the cheapest 2 TB models now approaching $250 — and desirable performant models going for well beyond that. With no end to either memory or storage shortages in sight, the next best option for gamers is to save on used disk space — and the recently-upgraded Game Compressor utility is a fine tool for that end.

Depending on the game in question, savings can be massive, with *ARK Survival Evolved* reportedly going down from 169 GB to 91 GB (54% of the original size) and*Crimson Desert* slimming down by 32 GB. Not every game bears high compressibility, but if even just one of your titles goes down by tens of gigabytes, that's enough to install another. This is handy on most every PC, and even more so for handhelds and machines where disk space is at a premium.

## How do you log in to your PC?

The application, which costs $5.99 / 5.99€ on Steam, leverages Windows' built-in LZX folder and file compression to transparently compress on-disk games — sometimes with massive savings. I've used NTFS compression for over two decades with no ill effects, and I occasionally enjoy improved game load times. That might sound counterintuitive, but with a compressed game, there's less I/O data to shuffle around. The only cost is a little bit of CPU overhead, which is almost guaranteed to be available as almost no games can fully utilize all the system's cores.

While it's easy to say that Game Compressor is just a UI for Windows' built-in functionality, the amount of convenience is impressive. You first set up a number of watched folders, of which presumably the ones for Steam games will be filled in. After Compressor scans which games are available, it will actually preview what kind of space savings you can expect, to save you the hassle of going through a long-running task for no benefit.

Once you select your games to compress, the tasks go into a queue, and can be paused or cancelled at any point — a convenience the Windows command line doesn't offer. You can also selectively decompress games later, and there's a log of operations just in case something goes awry. As you might expect, Compressor tries to detect which files (such as videos) aren't worth squeezing further.

One of Game Compressor's neat tricks is that it can monitor games that have received patches to reapply compression. Normally if, say, a 50GB game file gets a patch, it could be decompressed post-patch — this way, the space savings are kept in place.

Just about the only "con" to this notion is that it's not advisable to use compression on DirectStorage-enabled games, because that API relies on IO-to-VRAM operations and adding a CPU decompression step could introduce stuttering. Those titles are few and far between, though.

Some of you may be scoffing at this article and pointing out that ever since Windows 10, the "compress" command supports LZX compression. But paying just $5.99/5.99€ for Game Compressor will save your time, add visibility into compression status, and automatically recompress patches. If you'd rather strike a middle ground, there's also the open-source CompressGUI — which is also pretty nifty, though not quite as feature-filled.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.

- 
As soon as it becomes a product, people pay attention as if it's the newest best thing since sliced bread. Exactly the same functionality described in this article has been available with an open source utility called CompactGUI - for literally years. Or maybe it's just because Toms was paid to advertise?Reply
- 
I can't figure out how this is any different from enabling compression on the game folder using Windows, and doing so completely free of charge.🤷♂️ If I remember correctly, this option was introduced along with NTFS in Windows NT 3.1 in 1993. And it's also been included in the Windows license for free ever since.Reply
- 
Reply
 Thanks, I just saved myself 5 bucks!psyconz said:As soon as it becomes a product, people pay attention as if it's the newest best thing since sliced bread. Exactly the same functionality described in this article has been available with an open source utility called CompactGUI - for literally years. Or maybe it's just because Toms was paid to advertise?
 
 
 You must not have read as far as paragraphs 3-4 then? It mentions the existing native option along with the drawbacks that the native compression does not show you a preview of compression results or continuously monitor games and re-compress after patches.StrangerNN said:I can't figure out how this is any different from enabling compression on the game folder using Windows, and doing so completely free of charge.🤷♂️ If I remember correctly, this option was introduced along with NTFS in Windows NT 3.1 in 1993. And it's also been included in the Windows license for free ever since.
- 
Reply
 Yeah, as Jabberwocky79 implied - from memory, standard NTFS compression through the folder or file properties window is a different and lesser type of compression compared to LZX - that is, on modern systems which have plenty of spare CPU cycles compared to their IO bandwidth. I can't remember the exact details. I do know by using LZX back when I still used Winblow$ a few years ago, I saved a ton of space over default compression. And as the article states, it's 'transparent' in terms of user experience, so it made sense to use it at the time.StrangerNN said:I can't figure out how this is any different from enabling compression on the game folder using Windows, and doing so completely free of charge.🤷♂️ If I remember correctly, this option was introduced along with NTFS in Windows NT 3.1 in 1993. And it's also been included in the Windows license for free ever since.
- 
Compact GUI seems to be truly useful.Reply
 
 Some have mentioned Cyberpunk folder with it's ca. 70 GB. Are there any constraints to using Compact GUI on the WHOLE Steam folder instead of per folder usage??
 
 I did search for answer for this but got no results.
 
 Edit: How about the whole games folder under Steam (aka "common"" which contains all games), currently 1/1 TB.
