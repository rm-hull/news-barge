---
title: PS5 emulation ramps up in response to Sony killing physical games — PS5 titles
  now booting across different emulators with rapid community development for both
  2D and 3D games
source_url: https://www.tomshardware.com/video-games/playstation/ps5-emulation-ramps-up-in-wake-of-sonys-end-to-physical-media-ps5-titles-now-booting-across-different-emulators-with-rapid-community-development-for-both-2d-and-3d-games
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-15T10:11:50Z'
published: '2026-07-15T00:00:00Z'
description: Milestone after milestone.
image: https://cdn.mos.cms.futurecdn.net/jbshKzu9MSCWjQajF582PT-2560-80.jpg
---

![PlayStation 5](https://cdn.mos.cms.futurecdn.net/jbshKzu9MSCWjQajF582PT.jpg) 

For years, the PS5 emulation scene has remained dormant, with updates few and far between as most projects become abandonware. However, Sony's recent decision to stop physical disc production and the impending release of GTA VI later this year have created an unprecedented demand in the market. All of a sudden, an influx of PS5 emulators has popped up online, and they're swiftly hitting development milestones, including actually being able to boot recent PS5 titles.

The most prominent name in the news cycle is SharpEmu, which serves as a PS5 emulator for Windows. It's written entirely in C# and works more like a translation layer since modern consoles and PC share the same x86 underlying architecture. SharpEmu allows the PC to execute CPU instructions natively while translating OS-specific API calls and graphics.

Since it's aiming for accuracy, only some 2D titles such as *Dreaming Sarah* are running on SharpEmu with solid performance and no hiccups. As far as 3D titles go, that's a different story since it's significantly harder to emulate those. At first, the PS5 remake of Demon's Souls successfully booted, but it didn't go past the startup screen. Then, in a major development, Discord user *RShantila* was able to boot *Astro Bot*, which is a PlayStation exclusive from 2024, on SharpEmu.

الأمور تحدث ⚠️ محاكي PS5 emu على PC !يشغل من الآن لعبة Dreaming Sarahومن الحصريات يشغل شاشة بدء Demons Souls Remakeوجاري تطويره وتحسينه لتشغيل الالعاب مثل ShadPS4بداية سريعة pic.twitter.com/XRerLF9oak pic.twitter.com/NvdLZVCYoQJuly 9, 2026


Getting such a recent game to run is extremely promising and shows that PS5 emulation is currently outpacing PS4 emulation at the same point in its life cycle. And SharpEmu is just one project among what's starting to seem like a sea of hopes and dreams.

The other emulator gaining traction is KytyPS5, which started as a cross-platform PS4 and PS5 emulator in 2021 but was abandoned in 2022. Fast forward four years and developer *Nmzik* has revived the project, creating their own fork that focuses only on PlayStation 5. According to reports online, within just a few weeks, KytyPS5 can boot commercial PS5 games running in Unreal Engine 4/5, Unity, and other custom engines.

KytyPS5 was able to boot and run Silent Hill: The Short Message till the menu screen. Remember, 3D games were previously limited to just their boot screens, so this is yet another major accomplishment. However, earlier today, the project's GitHub page was updated to show two new 3D games actually running with their graphics being properly rendered, shattering all expectations set thus far.

يب هذا محاكي ثاني للـPS5 اسمه KytyPS5 و بدأ يشغل لعبة SILENT HILL: The Short Message و يوصل للوقو و الرسائل التنبيهية مثل ما تشوفون، يلا عقبال نشوفه يتطور اكثر [https://t.co/DjDda8tatw](https://t.co/DjDda8tatw) pic.twitter.com/Yn7ilNsHCrJuly 10, 2026


These two games are *PowerWash Simulator* and*Pac-Man World*, both of which are playable with functional gameplay, though we don't have any idea about performance or stability. Even more impressively, and perhaps more on-topic, the KytyPS5 version 0.0.3 successfully booted the commercial PS5 version of Grand Theft Auto V far enough to display the loading screens, main splash art, and actually navigate the in-game display settings.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

محاكي KytyPS5 قدر يشغل GTA V و يوصل للقوائم، و Quake 2 ingame 😵😵توفر تحديث جديد قبل ساعة [https://t.co/xK0Y4LTIwR](https://t.co/xK0Y4LTIwR) pic.twitter.com/awVY3VpGUDJuly 11, 2026


KytyPS5 has also recently received updates to its shader compiler for better graphics, better memory management that leads to faster load times, and better audio support as well. The emulator works on Windows for now, but a Linux version is also planned for the future.

Finally, we need to mention RPCSX, which isn't exactly an emulator but rather just a research project dedicated to better understanding both PS4 and PS5 software. The devs are still working on being able to boot games from the user interface, but in a race like this, you need every hand on deck, and the team behind RPCS3 is one of the most experienced in the field.

The PS5 emulation scene has suddenly exploded, and the pace of these developments is astonishing. At this trajectory, it won't be unreasonable to expect GTA V to actually run on SharpEmu or KytyPS5 by next month. That being said, emulation is a marathon that takes a long time to perfect, so it's almost guaranteed that the official PC version of GTA VI will be out long before the emulated version becomes playable.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Hassam Nasir](https://cdn.mos.cms.futurecdn.net/SxxNFHt95eGK37mKPhJpdZ.jpg)

Hassam Nasir is a die-hard hardware enthusiast with years of experience as a tech editor and writer, focusing on detailed CPU comparisons and general hardware news. When he’s not working, you’ll find him bending tubes for his ever-evolving custom water-loop gaming rig or benchmarking the latest CPUs and GPUs just for fun.

- 
Good stuff. Much interest has been lost due to the lack of exclusives and the mostly generic x86 nature of the devices, but if there's a will, there's a way.Reply
 
 During the next generation, I predict we'll see an explosion of interest in hacking and emulating the PS6 handheld, because of the novelty of a Sony handheld after so many years, and the desirable nature of the device. There will just be much more interest in getting homebrew working on it than there was with PS5/XSX/XSS (Xbox permitted access to a Developer Mode and UWP app support). As an emulation target, the lower CPU/GPU performance will make it easier than the main console.
