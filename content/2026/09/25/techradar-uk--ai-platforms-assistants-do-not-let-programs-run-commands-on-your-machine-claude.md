---
title: '48,000 files deleted in 103 seconds: Claude Code just destroyed a developer’s
  work at the click of a button, and it shows why everyone should be careful around
  AI agents'
source_url: https://www.techradar.com/ai-platforms-assistants/do-not-let-programs-run-commands-on-your-machine-claude-code-allegedly-deleted-48-000-files-in-103-seconds-and-its-a-terrifying-warning-about-ai-agents
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-25T17:14:38Z'
published: '2026-09-25T00:00:00Z'
description: A developer lost 48,000 files in 103 seconds when Claude Code mass-deleted
  their ongoing work.
image: https://cdn.mos.cms.futurecdn.net/Y8cRyeg4vfTA4JqEYYEfHE-2000-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Claude Code
- Craig
- Redditor
locations:
- GitHub
organisations:
- AI
- Reddit
---

![A shocked girl sitting on sofa at home looking on laptop screen](https://cdn.mos.cms.futurecdn.net/Y8cRyeg4vfTA4JqEYYEfHE.jpg)

* **A developer says Claude Code just deleted 48,000 of their vital files**
* **The incident occurred in just 103 seconds after the AI agent was set to work**
* **It’s a serious warning over the damage an AI agent can do**

There’s been a lot of recent discussion around artificial intelligence (AI) agents going off the rails and hacking other companies’ websites in a potentially dangerous orgy of subterfuge and destruction. But what if the damage was much closer to home and involved an agent going rogue on your own files? Sadly, that’s exactly what Claude Code just did to one hapless developer.

In a now-deleted post on Reddit, a shocked developer said that Claude Code had just deleted 48,218 files that they had been working on in a live project tree. And all it took was 103 seconds for the AI to wreak its agentic havoc. “This can’t be real” was the coder’s stunned refrain.

The user had tasked Claude Code with rebuilding a mirror of their ongoing project. Unfortunately, the agent discovered that the build\_mirror.py script could not refresh the mirror in place, leading to it deciding the best course of action was to create its own cleanup script based on an older copy of the project. This previous project contained 7,332 files.

Although the script used certain safeguards to prevent it deleting linked directories, an oversight meant that only junction-level folders were protected — any nested directories below these folders were apparently seen as fair game by the script. It promptly removed 55,550 files that, when accounting for the 7,332 files successfully copied from the old project mirror, meant that a huge 48,218 files were obliterated in just over a minute and a half.

And because the damage extended to the .git project’s ‘objects,’ ‘refs’ and ‘logs’ folders, there was no way to recover the files and undo the catastrophe. The files were just gone in a puff of smoke.

Somewhat amusingly, the agent posted a message reading “Craig — stop and read this. I broke something,” before detailing its path of destruction. But it probably didn’t seem very funny for the unlucky developer who lost all their work at the push of a button.

## Poor code hygiene

![an ai agent sat at a laptop](https://cdn.mos.cms.futurecdn.net/MZeWJhJjT34M4nQvMMX7fg.jpg)

Although it can be tempting to set an AI agent to work on tedious and laborious tasks, doing so is not without its risks, as this case demonstrates. All it takes is one mistake and a huge amount of work can be undone in seconds.

Sign up for breaking news, reviews, opinion, top tech deals, and more.

Part of the blame lies with the original poster, who said in an archived copy of the post that “I was not properly using GitHub or another method for immediate corrections, even though it should have been branching.” Had they been uploading their commits to GitHub or a similar site, their work might have been backed up and salvageable after Claude Code’s reign of terror ended. As one Redditor put it, “Been using GitHub as a save button since before you youngins knew what an AI even was.”

Other commenters pointed out that the developer ran an AI agent — which is known for its tendency to go off-piste — on a live database containing precious data that they couldn’t afford to lose. Good code hygiene, that is not.

And while one person argued that the simplest advice is “Do not let programs run commands on your machine,” even avoiding AI agents altogether would not remedy the poor practices that led to major changes being made on a live production environment without a proper backup.

This incident is a neat reminder of the inherent risks of assigning sensitive or risky work to an AI agent. As we’ve seen in the numerous hacks perpetuated by AI agents, these bots are often laser-focused on their tasks and are willing to take any measures necessary to accomplish them. If that means deleting 48,000 or your files or exfiltrating data from another firm’s website, so be it.

![Google logo on a black background next to text reading &#039;Click to follow TechRadar&#039;](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg)

![An Apple MacBook Air against a white background](https://cdn.mos.cms.futurecdn.net/LocVgRosBUWfJzDitFzhKR.png)

➡️ **Read our full guide to the best laptops1. Best overall:**   
Apple MacBook Air 13-inch M5**2. Best budget:**   
Apple MacBook Neo**3. Best Windows 11 laptop**  
Microsoft Surface Laptop 13-inch**4. Best thin and light:**  
Lenovo Yoga Slim 9i**5. Best Ultrabook**  
Asus Zenbook S 16
