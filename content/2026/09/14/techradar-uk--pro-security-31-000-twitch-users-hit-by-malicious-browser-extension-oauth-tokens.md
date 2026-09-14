---
title: 31,000 Twitch users hit by malicious browser extension — OAuth tokens leaked
  via Russian proxy network
source_url: https://www.techradar.com/pro/security/31-000-twitch-users-hit-by-malicious-browser-extension-oauth-tokens-leaked-via-russian-proxy-network
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-14T20:17:26Z'
published: '2026-09-14T00:00:00Z'
description: The extension has since been updated
image: https://cdn.mos.cms.futurecdn.net/33ooyG4FCgVjDs8W6RpowC-2000-80.jpg
---

![Twitch logo under a magnifying glass in internet browser](https://cdn.mos.cms.futurecdn.net/33ooyG4FCgVjDs8W6RpowC.jpg) 

- **Socket found Twitch extension*JeeBot*harvesting OAuth tokens via proxy servers**
- **Tokens excluded only for 10 Russian streamer channels, suggesting deliberate design**
- **Developer issued fixes, but users should revoke exposed tokens for safety**

A browser extension for Twitch was harvesting people’s OAuth tokens and sending them to a Russian-owned server. The move was deliberate, but whether or not it was malicious is not that easily determined.

Security researchers Socket recently found an extension for both Chrome and Firefox, called “Twitch Enhanced Viewer | JeeBot”. It has roughly 30,000 users on Chrome, and some 600 on Firefox.

On the Chrome Web Store, it is advertised as a “modern tool for streamers and viewers who value quality, convenience, and control.” Apparently, it makes streaming and viewing clearer, allows viewing content in 2K, hides banner ads and unwanted elements, and even offers an AI bot to make it easier to interact with the stream.

## Hardcoded exemptions

According to the researchers, the extension is designed to retrieve Twitch’s video stream playlists through its own proxy servers. However, instead of simply forwarding the requests, the extension also attached users’ OAuth tokens, and since they were placed in the URL, the token also ended up in the proxy server’s request logs.

After being called out for it, the extension’s developer (HISHIMIRO/jeetbot.cc) released a new version 85.8.7 (for Firefox, the Chrome one is currently under review) which apparently fixes this flaw: when playlists are retrieved, the user’s OAuth token is no longer sent to the proxies. It would seem like this was an honest mistake that was remedied upon responsible disclosure. However, here is what Socket had to say about the way the tokens were being retrieved:

"Current builds (v85.x) forward the token inline as an &auth= query parameter on a network-layer redirect to the operator's proxy," Socket explained. "The token is forwarded for every channel the user watches, except a hardcoded allowlist of ten Russian streamer channels, whose sessions are exempted from forwarding."

If there was a list of 10 Russian streamer channels who were exempt from OAuth token retrieval, it’s safe to assume that the developer knew very well what they were doing.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

It is good that the extensions were upgraded, but if you are using it, you should also revoke the exposed Twitch token, to be on the safe side.

*Via**The Hacker News*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
