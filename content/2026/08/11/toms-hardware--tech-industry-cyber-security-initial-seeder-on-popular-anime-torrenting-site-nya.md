---
title: Japanese authorities use new tool to identify initial torrent uploaders — anti-piracy
  group says it identified seeder on popular anime torrenting website without torrent
  swarm monitoring
source_url: https://www.tomshardware.com/tech-industry/cyber-security/initial-seeder-on-popular-anime-torrenting-site-nyaa-arrested-by-japanese-authorities-anti-piracy-group-claims-it-identified-user-without-torrent-swarm-monitoring
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-11T13:12:41Z'
published: '2026-08-11T00:00:00Z'
description: Arrest raises more questions than answers.
image: https://cdn.mos.cms.futurecdn.net/cBzSEAiRq8xHJmRbCmLPPT-2048-80.jpg
---

![Torrent links](https://cdn.mos.cms.futurecdn.net/cBzSEAiRq8xHJmRbCmLPPT.jpg) 

Recently, the Kyoto Prefectural Police caught one of the initial-seeders of the well-known Japanese torrent website Nyaa. Masakazu Ono, 56, from Sagamihara in the Kamigawa Prefecture, was arrested after a multi-year investigation. While this news is straightforward by itself, the interesting bit is that CODA, the Japanese anti-piracy entity that performed the initial cyber-investigation, identified Ono allegedly without joining or monitoring BitTorrent swarm traffic, with the help of the Japan Hacker Association (JHA).

CODA's description of only having "[analyzed] how data moves through torrent sites, such as index sites and tracker sites" is vague and can be parsed in a number of ways. The distinction between indexer and tracker is relevant: while an indexer is a user-visible list of torrents (usually a website), the tracker is the background service that software like qBittorrent actually connects to, and it lists everyone who's currently active in that torrent, whether sharing, downloading, or both.

Our hypothesis is that CODA kept close tabs on the Nyaa trackers to see which IP address (in this case, Ono's) consistently appeared as the first person to offer up a 100% complete set of data for a show, a theory that would fit with how long the operation took. JHA's founder, Takayuki Sugiura, was the first to decrypt the Winny P2P protocol in 2004 to find original uploader sources, and the methods used weren't too different from the aforementioned theory. It's also possible that Ono wasn't using a VPN but was logged into Nyaa, or activity at another website's cookies or CDN logs was used to establish a link to his activity at Nyaa, and from thereon, to the tracker.

An initial-seeder is someone who is the first to offer up data for others to download — in this case, shows and movies. The show that reportedly got Ono nailed was Midnight Taxi, a 2026 Japanese drama produced by NHK and WOWOW. However, the police apparently had been tracking him for quite a while and claimed that he had uploaded close to a thousand NHK recordings over the investigation's span.

The process started in 2021 when CODA first launched its Cross-Border Enforcement Project, aiming to identify Nyaa's uploaders. During three years, with the help of JHA, CODA seemingly collected enough information to get the Kyoto police involved in 2024. Three "secondary uploaders" from "reach sites" were charged in 2025, likely meaning regular users participating in the torrents, who got there through link aggregator sites. Fast-forward to a couple of weeks ago, and Masakazu Ono was formally arrested with specific charges.

The most common techniques used by law enforcement agencies are creating a tracker honeypot or participating in the torrent swarm themselves in a bid to identify who's sharing files. However, Nyaa's list of trackers is small and comprises well-known, trusted servers, so together with CODA's wording, it's unlikely this was the method used. Furthermore, Japanese law generally frowns on non-targeted data monitoring, meaning that techniques like Deep Packet Inspection (DPI) and traffic volume monitoring likely weren't used, at least until such time as Ono was identified.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.

- 
Replywell-known Japanese torrent website Nyaa The various Nyaa clones following the collapse of the original may be many things, but none of them are operated from Japan (nor was the original, for that matter).
 
 The key was the method used to identify a swarm memberThatMouse said:Isn't it pretty easy when you don't use a VPN?*without* actually directly interacting with the swarm (i.e. without actively participating in material distribution).
