---
title: Experts have found a trojan able to rig online live betting platforms
source_url: https://www.techradar.com/pro/security/experts-have-found-a-trojan-able-to-rig-online-live-betting-platforms
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-23T21:06:56Z'
published: '2026-07-23T00:00:00Z'
description: A company building betting software was targeted
image: https://cdn.mos.cms.futurecdn.net/LjsHPauSLhKbcYzTG2rmEX-1995-80.jpg
---

![Online games](https://cdn.mos.cms.futurecdn.net/LjsHPauSLhKbcYzTG2rmEX.jpg) 

- **JFrog found Newtonsoftt.Json.Net, a trojan NuGet package mimicking the popular Newtonsoft.Json library**
- **Malware specifically targeted Digitain’s crash‑game backend, rigging outcomes with insider knowledge of its codebase**
- **Issue was quickly fixed but attackers remain unidentified**

Security researchers JFrog have discovered a unique trojan targeting one specific company, while letting everyone else who’s infected walk away unharmed.

Named Newtonsoftt.Json.Net, the trojan is a typosquatted NuGet package variant of the hugely popular JSON library called Newtonsoft.Json. The legitimate package is one of the most-used code libraries in the .NET programming world, needed by almost every project in existence. It is a small piece of software that helps .NET applications read, understand, and exchange data between different systems.

According to JFrog, someone published an almost identical package, copied the real author’s name, license, and made it work as intended. For almost anyone who installed it, it worked entirely normal. However, for developers working on Digitain’s crash-game backend, it’s a whole different story.

## Rigging the games

Digitain is an Armenian software company providing online sports betting and gaming software platforms to gambling companies around the world.

On the infected machine running Digitain’s real crash-game code, the malware swaps in a rigged number instead of a fair one, using a formula based on the date and time.

What this means is that the results of the gambling game are rigged, allowing the attackers to know, in advance, which rounds are manipulated and place their bets accordingly.

The malware also sets up a private confirmation channel to report back for every rigged round, allowing the attackers to know if the cheat code still works or not.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

JFrog did not identify the attackers, but they did stress that it was most likely an insider.

Apparently, only someone with inside knowledge of Digitain’s codebase (for example a current or former employee, or a contractor) could have built such an exploit, since it required knowledge of the exact internal function name inside Digitain’s game engine that decides the crash-game outcome.

The researchers reached out to Digitain on July 7 2026 and were notified, two days later, that the issue had already been escalated to the team and, in the meantime, fixed.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
