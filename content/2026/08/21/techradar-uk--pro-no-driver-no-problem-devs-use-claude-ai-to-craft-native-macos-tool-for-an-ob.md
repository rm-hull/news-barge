---
title: No driver, no problem — devs use Claude AI to craft native macOS tool for an
  'obscure' Windows-only printer
source_url: https://www.techradar.com/pro/no-driver-no-problem-devs-use-claude-ai-to-craft-native-macos-tool-for-an-obscure-windows-only-printer
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-21T20:36:29Z'
published: '2026-08-21T00:00:00Z'
description: '"Cannot access printer? It''s here!"'
image: https://cdn.mos.cms.futurecdn.net/ywSwn3oGxXv4PfcRPZmTrc-2560-80.jpg
---

![Man coding programmer, software developer working on digital tablet with binary, html computer code on virtual screen](https://cdn.mos.cms.futurecdn.net/ywSwn3oGxXv4PfcRPZmTrc.jpg) 

- **India-based developer Kuber Mehta uses Claude Code to create a macOS driver for the HP Laser 1008a**
- **Previously, only the official drivers for Windows and Linux were available for the relatively obscure 2023 laser printer**
- **The AI-generated driver was created over a series of meticulous prompts, and is now available via GitHub**

The days of avoiding hardware that is incompatible with your operating system could be over. A developer based in India has created a macOS driver for a largely unknown HP printer using Claude Code, the agentic command-line coding tool developed by Anthropic.

Released in 2023, the HP Laser 1008a was issued with drivers for Windows and Linux, but not macOS. By using AI to generate a driver for macOS, developer Kuber Mehta has demonstrated that incompatible hardware could soon be a thing of the past.

Mehta has shared the code on GitHub and has also posted about the process on social media, and also compiled a transcript of the exchange, which has been published online for reference.

## HP’s Samsung printer

just Claude writing a MacOS driver for my obscure HP printer built only for Windows support pic.twitter.com/ORjLugJiRFAugust 17, 2026


Describing the issue in the introduction to the transcript, Mehta explains that the HP Laser 1008a is a “rebadged Samsung, host-based printer that speaks a proprietary raster language (SPL3), and it has no macOS driver and no AirPrint.”

No SPL3 drivers have been published for macOS previously, so the process relied on a conversation with Claude Code and reference to the Windows and Linux drivers.

The GitHub intro adds that the HP Laser 1008a and siblings in the series (1003 and 1006 a/w) have another problem: “They do not speak PostScript or PCL.” Anyone familiar with the world of printer drivers will recognize the challenge faced by Mehta, which makes the use of Claude Code even more impressive.

Using Claude Code with the Opus 4.8 model, the driver was compiled in 30-40 prompts. This might have been even quicker had the AI not made various assertions that required correcting.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The process moved through “install the drivers” to establishing the print language by analysing the printer’s error pages, via direct contact with the device and “running HP's real rastertospl codec inside a Linux container to produce genuine SPL3, to a reboot-safe background daemon.”

From here, Mehta and Claude Code moved to the published, MIT-licensed installer, which patches the macOS open-source printer driver package SpliX, adding support for the SPL3 printers (by default, SpliX handles SPL2 and SPLc drivers).

## Building from AI

While already a developer, Kuber Mehta admitted learning about macOS drivers from the process, perhaps an unforeseen benefit of using generative AI tools for coding.

The GitHub repo outlines some revisions that have been made to the initial release, which is now “a tiny native IOKit helper” that dispenses with Python, pyusb, and libusb and can be swiftly installed from the Terminal.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Christian Cawley](https://cdn.mos.cms.futurecdn.net/zBDYnjPnB2XPvhKbYX9Kuc.png)

Christian Cawley has extensive experience as a writer and editor in consumer electronics, IT and entertainment media. He has contributed to TechRadar since 2017 and has been published in Computer Weekly, Linux Format, ComputerActive, and other publications.

He currently heads up the team at smart home website Matter Alpha, and writes about retro gaming at Gaming Retro.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
