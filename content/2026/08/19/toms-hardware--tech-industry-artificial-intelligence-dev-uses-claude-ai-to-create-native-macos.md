---
title: Dev uses Claude AI to create native macOS driver for 'obscure' Windows-only
  printer — Linux container hack enables system-wide Cmd-P printing, driver now available
  on Github
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/dev-uses-claude-ai-to-create-native-macos-driver-for-obscure-windows-only-printer-linux-container-hack-enables-system-wide-cmd-p-printing-driver-now-available-on-github
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-19T13:09:52Z'
published: '2026-08-19T00:00:00Z'
description: '''HP never shipped a working macOS driver'' for this model, says the
  dev.'
image: https://cdn.mos.cms.futurecdn.net/MEhj2kjie9xAZfBevnC5jT-1920-80.jpg
---

![HP Laser 1008a printer](https://cdn.mos.cms.futurecdn.net/MEhj2kjie9xAZfBevnC5jT.jpg) 

A developer has revealed that they used Claude Code to create a macOS laser printer driver for the HP Laser 1008a, a machine designed for Windows users. Kuberwastaken (AKA Kuber) says that “HP never shipped a working macOS driver for these,” but the Claude Code-assisted driver package now works so well they can “print from Apple Silicon macOS like a normal printer. CMD-P from any app. No terminal, no per-job scripts.”

just Claude writing a MacOS driver for my obscure HP printer built only for Windows support pic.twitter.com/ORjLugJiRFAugust 17, 2026


Kuber provides some background to the driver development on the above-linked GitHub page. The HP family of printers, which includes the Laser 1008a, were just rebadged versions of Samsung’s SPL3 lasers, they say. This is fine for Windows users, but they don’t talk to computers via more widely compatible standards such as PostScript or PCL. Nor do they work with open source SPL/QPDL drivers, or Apple AirPrint.

So, how was this driver wrangling achieved, other than handing the job off to an AI coding agent? Kuber notes that the hp-laser-1008a-macos project leverages HP's own rastertospl. This is also used by the HP Unified Linux Driver, which works with this ‘Windows printer.’ Thus the new macOS driver works by inserting this codec inside a tiny Linux container, which delivers the result over USB.

Setting up this driver is a simple one-shot, one-time process - as it should be but might not have been expected. Kuber explains that a user needs only to make sure that Homebrew (Apple's package manager), is already installed on their system. Many may already have this installed, and if so, can just open up Terminal and paste in: *git clone [https://github.com/Kuberwastaken/hp-laser-1008a-macos.git](https://github.com/Kuberwastaken/hp-laser-1008a-macos.git) && cd hp-laser-1008a-macos && ./install.sh* “That is it. It will ask for your Mac password once, set everything up, and your printer will appear as "HP Laser 1008a". Print to it from any app with Cmd-P,” boasts Kuber.

If you are a macOS user and get access to or are offered a cheap HP Laser 1008a, there’s now no need to turn your nose up at this SPL3 laser. Models including the HP Laser 1003/1006/1008 are all good with this driver, it is claimed. However, there are a few things to be aware of. Kuber notes that hp-laser-1008a-macos can be a bit slow from idle to first print, that Colima must be running, and some may have to update their USB product ID if the driver complains of “printer not found” on your model.

As per the intro, Kuber has shared this slickly working macOS printer driver on GitHub, so other developers don’t have to replicate this work.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Mark Tyson](https://cdn.mos.cms.futurecdn.net/56vqMYLDaKRHPhHZgbADFR.jpg)

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.
