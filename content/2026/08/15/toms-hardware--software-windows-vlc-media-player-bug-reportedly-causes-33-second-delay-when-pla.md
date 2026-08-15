---
title: Devs blame Windows for VLC media player bug that causes 33-second delay when
  playing MP3 files — creators allege Microsoft Defender blocking plugin cache is
  to blame
source_url: https://www.tomshardware.com/software/windows/vlc-media-player-bug-reportedly-causes-33-second-delay-when-playing-mp3-files-on-windows-developers-say-microsoft-defender-is-to-blame
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-15T16:38:14Z'
published: '2026-08-15T00:00:00Z'
description: Another Windows flaw
image: https://cdn.mos.cms.futurecdn.net/eEtLR2fZ2Wuz7PEoxUuNKk-1919-80.png
---

![VLC media player running an MP3 file on Windows 11](https://cdn.mos.cms.futurecdn.net/eEtLR2fZ2Wuz7PEoxUuNKk.png) 

Popular open-source media player VLC has run into an unusual issue on Windows 11 that causes it to take as long as 33 seconds to start playing a simple MP3 file, the side effect of a recent unexplained change to Windows. The issue was publicized after game developer Jonathan Blow said he had stopped using VLC in favor of Microsoft's Media Player because of the delay. He also used the incident to criticize the state of open-source software running on Windows.

Responding to Blow's complaint, the developers behind VLC player fired back and claimed that the media player itself was not responsible. According to the VLC team, the bug is primarily due to a Microsoft Defender issue introduced through a Windows 11 update that conflicts with VLC's plugin cache.

This is because of a « bug » from Microsoft Defender in one update of Windows 11, who magically made VLC plugins cache quarantined by Windows.Reinstalling VLC or regeneration of the plugin cache will fix this.Calling open source software embarrassing when it is a Windows… [https://t.co/IFLrXFZFsvAugust](https://t.co/IFLrXFZFsvAugust) 12, 2026



"This is because of a « bug » from Microsoft Defender in one update of Windows 11, who magically made VLC plugins cache quarantined by Windows. Reinstalling VLC or regeneration of the plugin cache will fix this. Calling open source software embarrassing when it is a Windows update that broke it is quite disrespectful," the account responded.

The cache is an important part of how the media player works, as it relies on plugins for codecs, demuxers, and input/output modules. Instead of putting everything into a single executable, VLC loads these components as and when required and uses a cache to avoid having to scan the entire plugin directory every time it loads. The issue seems to occur when Microsoft Defender quarantines or blocks VLC's *plugins.dat* cache file. As a result, VLC can take a noticeable amount of time to process its plugin system before finally beginning playback. We also tried to replicate the issue on a Windows 11 machine; however, VLC launched normally, and we did not experience any noticeable delay when playing an MP3 file.

The easiest way to fix this is to reinstall VLC or regenerate the plugin cache. The VLC Windows installer includes a dedicated executable file to reset the cache files. This can be accessed by either heading to the VLC installation folder and running *vlc-cache-gen.exe* or its shortcut within the Start menu called "VLC media player - reset preferences and cache files." Do note that this also removes any customized preferences, such as audio settings like equalizers, keyboard shortcuts, subtitles, etc.

A more reliable solution is to add an exception for the VLC installation folder in Microsoft Defender itself. This should prevent Microsoft Defender from interfering with VLC's cache files and avoid the same issue from recurring. While the workaround seems relatively simple, it is still far from being ideal. One should not have to jump through hoops just to play an MP3 file. While Microsoft is yet to comment on the issue, it remains to be seen whether a future Windows Defender update will address the underlying cause.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Kunal Khullar](https://cdn.mos.cms.futurecdn.net/NDK3ae3zDxAx2BJnMXxBJV.jpg)

Kunal Khullar is a contributing writer at Tom’s Hardware. He is a long time technology journalist and reviewer specializing in PC components and peripherals, and welcomes any and every question around building a PC.

- 
Its not just MP3 files it is any media that VLC can play. I figured out the solution just after the last update of VLC when the problem first occurred. I was annoyed that it was Windows Defender that was causing the problem, Microsoft needs to sort this out.Reply
- 
Reply*"We also tried to replicate the issue on a Windows 11 machine; however, VLC launched normally, and we did not experience any noticeable delay when playing an MP3 file."*
 I also see zero issue. Music, video, whatever.
 Win 11 Pro, fully updated.
VLC v 3.0.23
- 
Reply
 It creates a blind spot, where some malware could then compromise executable code without being detected. However, unless it's a targeted attack to take advantage of this specific issue, malware will likely also attack other files and be detected then.The article said:A more reliable solution is to add an exception for the VLC installation folder in Microsoft Defender itself. This should prevent Microsoft Defender from interfering with VLC's cache files and avoid the same issue from recurring. While the workaround seems relatively simple, it is still far from being ideal.
 
It's been a while since I've done software development on Windows, but we used to exclude the build location of our projects, because antivirus programs would otherwise cause build times to grow unreasonably large.
