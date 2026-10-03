---
title: ChatGPT-6 Astra plays World of Warcraft 'blind' and clears the orc starting
  zone in 40 minutes with no deaths — AI agent navigates by parsing raw server network
  packets and SQL files
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/gpt-6-astra-plays-world-of-warcraft-blind-and-clears-the-orc-starting-zone-in-40-minutes-with-no-deaths-ai-agent-navigates-by-server-network-traffic-with-pulled-quest-data
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-03T11:41:18Z'
published: '2026-10-03T00:00:00Z'
description: OpenAI's model used the open-source agent-wow client to play on a private
  World of Warcraft server.
image: https://cdn.mos.cms.futurecdn.net/ujZwJwwyt3MAzvTPaTAe34-1920-80.png
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
people:
- Claude
- Tom
locations:
- Codex
- Icecrown Citadel
- Orgrimmar
- Sen’jin Village
- WoW
- Wowhead
organisations:
- AzerothCore
- Get Tom's Hardware
- GitHub
- Google News
- OpenAI
- Orc
- Portal
- Shane Downing
- Tom’s Hardware
- WoW
- World of Warcraft
- YouTube
---

![An orc in purple robes stands beside a glowing totem on a street in Orgrimmar](https://cdn.mos.cms.futurecdn.net/ujZwJwwyt3MAzvTPaTAe34-1920-80.png)

OpenAI's GPT-6 Astra AI model was able to clear the Orc starting area in World of Warcraft (WoW) in 40 minutes with 0 deaths, agent-wow's developer says. The model played the zone without seeing a single rendered frame, relying on network traffic and quest data pulled from the server's own files. The approach used a single prompt in Codex with agent-wow, an open-source client, to play on a private server. The corresponding YouTube video says that the agent “starts as a level 1 Orc, completes every quest in the Valley of Trials, and finishes the run in Sen’jin Village.”

![Asus RTX 5080 Noctua Edition](https://cdn.mos.cms.futurecdn.net/Wh9EZgD8NG9yUioNNgPB3d-1200-80.png)

Agent-wow is an “AzerothCore WoW client designed for autonomous AI agent players,” according to the GitHub repo description. The client does not “define any gameplay mechanics such as movement, combat, or in-game interactions” and instead only exposes a “module system for agents to build” whatever they need to play. AzerothCore is open-source server software that runs WoW 3.3.5a, “the final build of Wrath of the Lich King,” and agent-wow talks to it over the game’s network protocol. The client does not connect to any live WoW server and instead can be run on local private servers for experimentation.

The developer ran OpenAI’s flagship model, released early last month, with extra high reasoning effort, one below the highest or maximum. The developer chose WoW for its mix of long-term strategy and short-term tactics, with an end goal of filling “an entire server with AI agents [to] see if they can clear Icecrown Citadel on heroic difficulty.”

The agent built a single module to grab 28 types of server messages, by our count, which are kept in memory. A Python script polls those messages to build the agent’s picture of the world and sends messages back to act in it. The developer expected a higher-level implementation, but “In practice, it was more than capable of working at the protocol layer.”

![GPT-6 Astra Clears the Orc Starting Zone in World of Warcraft | agent-wow - YouTube](https://img.youtube.com/vi/8NmmFdREk5s/maxresdefault.jpg)

For quest data, the agent turned to data mining, pulling quest givers, turn-ins, and spawn points from AzerothCore’s SQL files. The developer says this is “arguably similar to how a human might spend hours on Wowhead to research quests,” referring to a popular WoW info site. Going straight to the server’s own files arguably beats that, since they’re the data the server itself runs on, while a fan site’s data may not always match. The project’s public workspace instructions also list AzerothCore’s source code as a resource for agents, though the developer doesn’t say whether this run used them.

Some planning was used in the agent’s approach. According to the developer, it worked through prerequisite quest chains in order, sold junk, equipped upgrades, and trained abilities before the zone’s final cave, and picked up both cave quests at once to complete them together.

For pathfinding, the agent built a C++ helper that plots a route between a starting point and a destination with AzerothCore’s own navigation mesh files, or mmaps. The Detour pathfinding library finds the route, and the helper returns its waypoints as coordinates, or an error if there’s no complete path. The developer acknowledges that “from my research into heuristics-based bots, pathfinding is always one of the main challenges,” but calls the agent’s pathfinding abilities “optimal.” In fact, the agent was able to “exploit map bugs” at locations where collision properties may have been lacking.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

This is not the first game the model has tackled. Early last month, shortly after its release, it played the game Portal with screenshots and knowledge of the player’s position. This WoW run used no screenshots at all and only covered the first zone, while the Portal run went through the entire game over about 24 hours.

Recently, developers have deployed various techniques to play Pokémon Red, such as using a custom small model and a Jev decision model harness with Claude coaching. Next up for the developer: discovering whether a single agent can reach level 80 completely on its own, and whether multiple agents can team up to complete content through the game’s social features.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Shane Downing](https://cdn.mos.cms.futurecdn.net/Zosi9VrDytS9FkgJiHvc69-140-80.png)

Shane Downing is a Contributing Writer for Tom’s Hardware, covering consumer storage, PC hardware, and AI.
