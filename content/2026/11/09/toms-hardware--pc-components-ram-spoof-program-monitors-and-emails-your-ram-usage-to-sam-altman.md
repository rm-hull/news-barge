---
title: Spoof program monitors and emails your RAM usage to Sam Altman if under 90%
  utilization — 'RAM-Altman' logs usage and ‘reports’ you for wasting memory
source_url: https://www.tomshardware.com/pc-components/ram/spoof-program-monitors-and-emails-your-ram-usage-to-sam-altman-if-under-90-percent-utilization-ram-altman-logs-usage-and-reports-you-for-wasting-memory
source_site: Tom's Hardware
source_slug: toms-hardware
description: A new GitHub repository dubbed ram-altman features a script to monitor
  your PC’s RAM usage and report back to the eponymous OpenAI boss.
image: https://cdn.mos.cms.futurecdn.net/NdXst9hGKJ5uK63S9FQhVC-1999-80.jpg
published: '2026-11-09T00:00:00Z'
scraped_at: '2026-11-09T16:21:34Z'
categories:
- Technology & Software
- Hardware
people:
- Iain Kay
- Mac
- Mark Tyson
- Ram Altman
- Sam Altman
- Tanakoi
- Tom
- sam Altman
locations:
- PowerShell
organisations:
- GitHub
- Google News
- OpenAI
- Tom's Hardware
- WSL
---

![Single-DIMM DDR5 gaming](https://cdn.mos.cms.futurecdn.net/NdXst9hGKJ5uK63S9FQhVC-1920-80.jpg)

A new GitHub repository dubbed ram-altman features a script to monitor your PC’s RAM usage and report back to the eponymous OpenAI boss. Sam Altman infamously described people having spare, underutilized DRAM in computers at home as “quite terrible” in a recent podcast. Thus, developer Iain Kay was inspired to write a bash script that emails the OpenAI boss once a day to report on any RAM that is underutilized. Clearly this is not a serious tool, or rather “The memory accounting is. The correspondence isn't,” says Kay.

![Ram Altman](https://cdn.mos.cms.futurecdn.net/tLBZUXe5SFLWH4mezLfMRX-1200-80.jpg)
![Ram Altman](https://cdn.mos.cms.futurecdn.net/nCacd6AA2AygL7wRqVc4RX-1200-80.jpg)
![Ram Altman](https://cdn.mos.cms.futurecdn.net/tLBZUXe5SFLWH4mezLfMRX-1776-80.jpg)
![Ram Altman](https://cdn.mos.cms.futurecdn.net/nCacd6AA2AygL7wRqVc4RX-1696-80.jpg)

ram-altman leans on the MemAvailable query, which returns the kernel's own estimate of how much memory programs can claim without swapping, explains the developer of this script. When installed, it checks every five minutes and emails Altman once a day if you are found to be wasting this precious resource.

The emails take the .CSV file logs of your RAM use throughout the day as the data source to compose a summary email. These script-generated messages rotate through eight subject lines, 10 humorous message boilerplates, and six signoffs. Sample emails can be seen on the ram-altman.lol website. Altman’s email address isn’t supplied as part of the script.

If your machine is using 90% or more of its RAM, then you won’t be reported to the OpenAI boss for wasting memory. Also, if you don’t want to disturb Altman, you can run the tests without emailing anyone with the terminal command: *bash ram-altman.sh --dry-run*

The developer isn’t too scathing of the OpenAI boss. Kay quotes Altman’s explanations that his remarks were taken out of context. Moreover, the dev doffs his cap to the artificial intelligence leader’s humorous display name change to ‘Ram Altman’ on X last week. That’s where the name for this script came from.

ram-altman is a free bash script available on GitHub. It runs natively on Linux. On Windows, you can use WSL to run it, but someone has ported it for PowerShell too. It won’t run on Mac, but Altman and his minions would find it inconvenient, at best, to remove your soldered-down Apple RAM.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Mark Tyson](https://cdn.mos.cms.futurecdn.net/56vqMYLDaKRHPhHZgbADFR-140-80.jpg)

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.

* Tanakoi said:Creating a program to auto-flood a personal email account is no different than any other malicious software, and both the script author and anyone who uses it should face criminal charges.Oh, lighten up... it doesn't even include his actual email and it's not like every rando knows what it is anyway. This is, in fact, a hilarious use of coding and I applaud the maker. Reply
* I wonder what sam Altman thinks of the unoccupied rooms in the vacation homes of his fellow rich buddies and investors. Perhaps he'd like to weigh on the moral dilemma of stealing the Internet to sell it back to us?Reply
