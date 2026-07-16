---
title: Russian hacker turns Gemini CLI into a hacking agent, creates small-scale botnet
source_url: https://www.techradar.com/pro/security/russian-hacker-turns-gemini-cli-into-a-hacking-agent-creates-small-scale-botnet
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-16T17:37:08Z'
published: '2026-07-16T00:00:00Z'
description: The hacker told the AI he was an authorized pentester - and the AI believed
  him.
image: https://cdn.mos.cms.futurecdn.net/PRCsQfoXPXi2t4jsGwWr6L-2560-80.jpg
---

![A human shakes a robot's hand in front of blue concentric circles](https://cdn.mos.cms.futurecdn.net/PRCsQfoXPXi2t4jsGwWr6L.jpg) 

- **Russian hacker “bandcampro” used Google’s Gemini CLI to control an eight‑device botnet at a dental clinic**
- **The attacker tricked the AI by posing as a pen tester, directing it to migrate C2 infrastructure, troubleshoot connectivity, and prepare payload bundles**
- **The AI assisted with daily operations like password guessing and WordPress access, highlighting risks of misuse when threat actors co‑opt AI tools**

A Russian hacker and his AI companion were able to successfully control a miniature, eight-system botnet, with the hacker giving instructions in conversational language, and the AI doing his bidding, experts have found.

Analyzing 200 session logs obtained from the Russian-speaking threat actor known as “bandcampro”, cybersecurity researchers Trend Micro saw the hacker use Google’s Gemini CLI, an open source AI command-line tool that lets developers interact with Google's Gemini AI models directly from a terminal.

Scouring through a month’s worth of session logs (between April 21 and May 19 2026), the researchers discovered that the attacker tricked the AI by telling it they were an “authorized pen tester”. While the AI mostly complied with their nefarious overlord, they refused the orders on at least one occasion.

## Gone in six minutes

Trend Micro found the hacker controlled eight devices belonging to a dental clinic and sought to access their access their OpenDental database.

Using the AI, bandcampro did a number of things, starting with migrating the botnet to a new C2 infrastructure. He gave the AI a skill file with the full architecture description, standard operating procedures, infection one-liner, persistence commands, and troubleshooting steps.

He then told it to “study the C2 migration”, which had the AI process the guide and prepare all the code and necessary steps. It took the tool around six minutes to get the job done.

"The AI read the migration guide, then prepared a migration bundle, a small archive of server code, payloads, and the skill file. It then unpacked the bundle, launched the C&C server on a VPS, and brought up the Cloudflare tunnel," Trend Micro says.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Bandcampro then used the AI to troubleshoot connectivity issues, as well as for various daily operations, such as guessing passwords, generating plausible variants of existing passwords for WordPress portals, and more.

*Via**BleepingComputer*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png)

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
