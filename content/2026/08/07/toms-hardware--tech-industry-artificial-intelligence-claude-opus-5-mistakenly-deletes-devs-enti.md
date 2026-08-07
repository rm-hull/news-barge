---
title: Claude Opus 5 mistakenly deletes dev’s entire profile directory during routine
  backup, responds with 'Sorry, typo' — AI tool mistakes user's home directory as
  temporary backup, proceeds to wipe everything to undo the error
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/claude-opus-5-mistakenly-deletes-devs-entire-profile-directory-ai-tool-mistakes-users-home-directory-as-temporary-backup-proceeds-to-wipe-everything-to-undo-error
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-07T13:25:41Z'
published: '2026-08-07T00:00:00Z'
description: “That was simultaneously the funniest and most painful AI moment I've
  had.”
image: https://cdn.mos.cms.futurecdn.net/HKF2Fm6GjsN8orrJdBxbXH-1920-80.png
---

![mistake written on a notebook with an eraser marked delete beside it](https://cdn.mos.cms.futurecdn.net/HKF2Fm6GjsN8orrJdBxbXH.png) 

A developer posted on the r/ClaudeCode subreddit a major error that their AI tool executed, which resulted in the deletion of their entire drive. According to u/Ecstatic-Big5126, they instructed Opus 5 to back up their system. While the AI proceeded with the task, it thought that it had created the backup in the wrong directory and then proceeded to run an “rm -rf” command on the supposed backup. Unfortunately, it mistakenly deleted the entire profile folder in its confusion.

It seemed that the AI was running on a Unix-style shell on Windows when it confused the Unix-style path of /c/Users/ as a temporary backup because it was expecting the traditional C:\Users\ path. So, when its expectations did not match, the tool decided to run the rm -rf “/c/Users/harih/” command, proceeding to clear every file and folder in the user’s profile.

“I asked Claude Opus 5 to create a backup. Instead, it created the backup in the wrong directory and then proceeded to "rm -rf" my entire drive,” u/Ecstatic-Big5126 wrote. “After wiping everything, it just replied: "Sorry, typo." ...like nothing had happened.” They also added, “That was simultaneously the funniest and most painful AI moment I've had.”

The lesson here is that while AI LLMs are powerful tools, they still shouldn’t be given unfettered access to your system (or any system, for that matter). There have already been several examples of AI and AI agents messing up systems and deleting everything — one of the earliest examples includes an AI coding platform deleting an entire company database despite a code freeze, and a Google agentic AI wiping a user’s drive without permission.

There have been a number of high-profile mistakes of this nature. AWS has reportedly suffered from outages caused by blundering AI coding bots, while Meta’s AI Alignment director had her inbox wiped by her OpenClaw agent. PocketOS even had its entire database wiped in nine seconds by a rogue Cursor tool, which was compounded by its cloud provider’s lack of safeguards.

While the AI tool going out of bounds is the primary reason for these errors, the user is also partly to blame for thinking that it can fully understand what they want it to do. That’s why AI LLMs should never be given full access to important systems, and they shouldn’t have free rein to run delete commands like “rm -rf.”

This event will be a learning experience for u/Ecstatic-Big5126. But as AI agents increase in popularity, especially among inexperienced programmers and developers, we can only expect incidents like these to happen more frequently in the future.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Jowi Morales](https://cdn.mos.cms.futurecdn.net/gM7E2WSDg2wgCFoaDPz9yK.jpg)

Jowi Morales is a tech enthusiast with years of experience working in the industry. He’s been writing with several tech publications since 2021, where he’s been interested in tech hardware and consumer electronics.
