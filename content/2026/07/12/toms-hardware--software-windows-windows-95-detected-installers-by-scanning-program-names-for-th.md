---
title: Windows 95 didn’t detect installers, it ‘guessed’ based on the file name, says
  veteran dev — it simply checked for words like setup, install, inst, or localized
  equivalents
source_url: https://www.tomshardware.com/software/windows/windows-95-detected-installers-by-scanning-program-names-for-the-word-setup
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-12T13:50:08Z'
published: '2026-07-12T00:00:00Z'
description: Microsoft's Raymond Chen describes the string-matching heuristic behind
  the OS's system-file recovery.
image: https://cdn.mos.cms.futurecdn.net/93zD53cHwzp5tCAWcbongY-1920-80.jpg
---

![Windows 95](https://cdn.mos.cms.futurecdn.net/93zD53cHwzp5tCAWcbongY.jpg) 

Windows 95 worked out whether a setup program had run by reading the executable's name and checking it against a short list of hard-coded words, according to Microsoft engineer and semi-official Windows historian Raymond Chen, sharing the details via his *Old New Thing* blog. A filename containing "setup," "install," or "inst" flagged the program as an installer, which triggered the operating system's routine for repairing system files that installers had damaged. Three non-English entries appeared on the same list, which Chen identified as his own guesses at Italian, Turkish, and Hungarian.

The full match list ran to six terms: setup, install, inst, imposta, ayarla, and felrak. Chen wrote that "install" was redundant, because any name containing it already contains "inst," and speculated that the shorter entry was added later to catch installers named along the lines of "blahinst" without anyone deleting the original. A program whose own name produced no match got a second test, with Windows 95 checking whether the word "Setup" appeared anywhere in the path to the executable. A separate live check ran after any multimedia driver was installed through an INF file, added because those drivers frequently overwrote system DLLs.

This heuristic gated a recovery mechanism Chen described in March. Installers of the period overwrote system files without checking versions, disregarding Microsoft's rule that a file should only ever be replaced by a newer one. An installer carrying Windows 3.1 copies of shared DLLs, for example, would bury the newer Windows 95 versions underneath them, and every program that relied on the current files would break.

Windows 95 kept backup copies of commonly clobbered files in a hidden C:\Windows\SYSBCKUP directory. It would then let each installer finish, check its work, and restore the correct versions where the installer had downgraded them. This safety net depended entirely on correctly guessing that an installer had run, so a setup routine with an unusual name slipped past it, while an ordinary program named something like instant.exe tripped it for nothing.

The file check was often deferred until the next boot rather than run immediately, with Chen explaining that some installers, unable to replace a file already in use, would drop back to MS-DOS, run a batch file to swap the file, and restart Windows, so the cleanup pass had to wait for the reboot to catch anything the batch file had altered.

## Windows 2000 debuted a new approach

Microsoft dropped this approach in Windows 2000, which introduced Windows File Protection. That system registers for file-change notifications through Winlogon restores protected files from a cache at %WinDir%\System32\dllcache, with no filename guessing and no waiting for a setup program to complete.

Then, Windows ME shipped a comparable System File Protection, and Vista onward moved to Windows Resource Protection, which guards files using access-control lists instead. The sfc /scannow command that Windows 11 users still run to repair system files descends directly from that work, having replaced a 1995 mechanism that decided when to act by scanning filenames for the word "setup."

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Luke James](https://cdn.mos.cms.futurecdn.net/C4FAi2KzwaGLUrBqzX5aBM.png)

Luke James is a freelance writer and journalist. Although his background is in legal, he has a personal interest in all things tech, especially hardware and microelectronics, and anything regulatory.
