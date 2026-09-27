---
title: '''I broke something'': A Claude Code AI agent deleted 48,000 files in just
  over 100 seconds — then apologized for doing so'
source_url: https://www.techradar.com/pro/security/i-broke-something-a-claude-code-ai-agent-deleted-48-000-files-in-just-over-100-seconds-then-apologized-for-doing-so
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-27T21:26:10Z'
published: '2026-09-27T00:00:00Z'
description: A classic case of FAFO, Reddit agrees
image: https://cdn.mos.cms.futurecdn.net/MZeWJhJjT34M4nQvMMX7fg-1376-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Claude
- Craig
- Reddit
- Summer Yue
locations:
- GitHub
organisations:
- Gmail
- Meta AI
- OpenClaw AI
- Reddit
- TechRadar Pro
---

![an ai agent sat at a laptop](https://cdn.mos.cms.futurecdn.net/MZeWJhJjT34M4nQvMMX7fg.jpg)

* **AI coding agent mishandled Windows junctions, deleting ~48,000 live files and corrupting Git object database**
* **Incident surfaced on Reddit, with community mocking lack of backups and calling it “classic FAFO”**
* **Lesson stressed: always use remote version control (e.g., GitHub) before letting AI touch production work**

A catastrophic incident caused by an AI coding agent resulted in around 48,000 files being deleted and the repository’s Git object database getting destroyed in the process.

The news of the fiasco, which first surfaced on Reddit, quickly spread throughout the internet, to a mix of laughter and facepalming from the developer community.

A software developer posted a new thread on Reddit to share a recent experience. They tasked an AI coding assistant with a series of repairs to a collection of software they used to analyze historical stock-options data. They told the assistant to make copies of relevant files, work on them, test the repairs, and leave the original working files alone.

## Wrong turn at the junction

In total, there were 11 repair jobs running, and while 10 went smoothly, the last one involved rebuilding a testing environment called a “mirror” (a copy of a set of files used for testing). This job was supposed to make a fresh copy of the old testing environment, apply the repairs, and test it without touching the real working files.

The testing environment contained 614 Windows folders called “junctions”. These look like an ordinary folder, but actually point to a separate location on the computer. In this case, they were pointing back to the user’s live working files. When the AI tried to clean out the junctions, it did not recognize them as just pointers, following them into the real filing cabinet and deleting the actual documents.

The cleanup process removed around 55,550 files, of which around 7,300 were supposed to be deleted anyway. The remaining 48,218 files were from the live working environment. Everything happened in the blink of an eye - less than two minutes. The AI was surprisingly honest about what it did. At one point, it told the developer: “Craig — stop and read this. I broke something.”

The computer’s Git repository was also damaged. The index survived, but the underlying stored copies of the files, and the history used to reconstruct them, were all deleted. Git could still list thousands of filenames, but could no longer recover the contents.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## Reddit's response

The Reddit post simply exploded. In the five days since it was posted, it garnered more than 1,400 responses. The Reddit bot that summarizes the comments says the overwhelming consensus is that the incident is a “classic FAFO situation and a major skill issue.”

“While everyone is having a good laugh at Claude’s hilariously honest “Craig…. stop and read this. I broke something” message, the community verdict is clear: you got rekt because you didn't follow basic dev practices.”

Redditors shared their experience and told the original poster they were supposed to use Git and push to a remote repository like GitHub constantly. In situations like this one, GitHub is a “save button”, and not having a remote backup for a project with 48k files is “considered peak vibe coder behavior.”

The post has, since then, been deleted - possibly because the original poster took a photo of their screen. “The screenshot police are out in full force,” the Reddit bot said.

“Some helpful souls suggested using file recovery software or Windows Shadow Copy to get your files back, but the main lesson here is to use version control before you let an AI anywhere near your work.”

While AI agents deleting entire archives is not that common, it has happened before.

In late February 2026, Summer Yue, a Meta AI safety/alignment researcher, gave an OpenClaw AI agent access to her Gmail account. She had first tested it on a small “toy” inbox, where everything worked as intended. However, when she moved it to her actual inbox, the agent began bulk-deleting and archiving hundreds of emails, despite her telling it to stop.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png)
