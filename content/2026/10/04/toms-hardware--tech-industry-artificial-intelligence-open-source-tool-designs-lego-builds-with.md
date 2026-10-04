---
title: Open-source tool designs LEGO builds with more than 2,000 real pieces — their
  programs output detailed CAD files, but no models have been built yet
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/open-source-tool-designs-lego-builds-with-more-than-2-000-real-pieces-their-programs-output-detailed-cad-files-but-no-models-have-been-built-yet
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-04T11:09:52Z'
published: '2026-10-04T00:00:00Z'
description: Claude designed Sakura Garden, with a five-story pagoda, a koi pond,
  and cherry trees in 2,175 pieces.
image: https://cdn.mos.cms.futurecdn.net/9QRFisZJCpz9R7tVzm2UbT-2498-80.png
categories:
- Technology & Software
- Hardware
- Home, Garden & DIY
people:
- Carlos Antelo
- Claude Opus
- Shane Downing
- Tom
locations:
- Cathedral
- Sakura Garden
organisations:
- AI
- Antelo
- Anthropic
- BrickGPT
- CAD
- Carnegie Mellon University
- Copper Bean
- Docker
- GPT-6 Astra
- Get Tom's Hardware
- GitHub
- Google News
- JSON
- Kiln
- LDView
- LDraw Nova
- LEGO
- LegoGPT
- OpenAI
- OpenRouter
- Sakura Garden
- Shane Downing
- Tidal Observatory
- Tom’s Hardware
- World of Warcraft
---

![Sakura Garden, an AI-designed LEGO model with a five-story pagoda, torii gate, koi pond, and cherry trees, open in the ldraw-nova web app&#039;s 3D viewer](https://cdn.mos.cms.futurecdn.net/9QRFisZJCpz9R7tVzm2UbT-1920-80.png)

AI models can now design LEGO builds with thousands of real pieces, creating programs that output detailed CAD files, with the assistance of open-source LDraw Nova. It can leverage general models like GPT-6 Astra and Claude Opus 5.5 to design elaborate builds from a prompt, such as the 2,175-piece Sakura Garden. The models use Python tools to write programs, which output the builds without placing every brick. None of the designs have been built with real bricks yet, though; developer Carlos Antelo says he “didn’t even try.”

![LDraw Nova - Open Source AI LEGOs© - YouTube](https://img.youtube.com/vi/YDjjxGqWpgU/maxresdefault.jpg)

“Give an AI agent a model idea. Guide it, let it build it,” according to the GitHub project’s README. The Sakura result arose from a prompt to Claude Opus 5.5 asking for “the most beautiful model that comes to your mind.” Antelo posted the project on Friday afternoon as the first release after getting the toolkit to work after three earlier attempts.

![A LEGO cathedral designed by GPT-6 Astra, with twin towers, a blue rose window, and gray roofs, on a gray baseplate](https://cdn.mos.cms.futurecdn.net/sxLirF4m4PAiGu5xSDLMHc-1200-80.png)

LDraw, according to Antelo, is a text format where each LEGO piece placed is positioned with one line. LDView, LeoCAD, and Studio can open it, one file per model. An agent writes a plan in JSON that fully describes the model and submodels, creates a Python program from it, then generates the LDraw source output. When the model is rendered as an image, the agent can inspect, adjust, and render again, looping until the model is considered complete. In this way, it avoids “(evil!) geometry math,” as agents are “better at generating Python code.”

LDraw Nova runs as a Docker web app that works with AI providers including OpenAI, Anthropic, and OpenRouter. The web app’s gallery credits each build to the model that made it, with its prompt: Sakura Garden and an unfinished Atlas Crane to Opus 5.5, a Cathedral and the Tidal Observatory to Astra, and the Copper Bean apartments to Opus 5 “(not 5.5!).” The project itself was built with the assistance of OpenAI’s Astra and Anthropic’s Claude Opus 5.5.

Building the larger models for real would mean collecting thousands of parts, a task Antelo figures would be difficult. The project has limitations, too, as “physics modeling is something Nova is currently lacking,” which means collisions are handled, but stability is not. It isn’t free to run, either: his “wild” estimate for Astra building one Technic mechanism is around $5 in token costs.

Likewise, his experience thus far is that only frontier models can currently generate large and accurate builds, and the process remains time-consuming. VR support for the Meta Quest 3 headset exists but has “many issues, performance issues.” The project as a whole differs from Carnegie Mellon University’s LegoGPT, now BrickGPT on GitHub, which was trained on more than 47,000 LEGO structures and, in contrast, checks its designs for validity and physical stability as it generates them.

The tool can use more than one type of model: jev-rerank, a “semantic search tool with re-ranking backed by TypeSafe’s Jev System One AI model,” was used for Astra’s Cathedral build. The Jev decision model reranks the part searches, but it’s optional. If no TypeSafe API key is provided, the agents fall back to full-text search. This model was successfully used recently in multiple automated Pokémon Red playthroughs.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

While Antelo recommends higher-end AI models for the project, one of his goals is “tooling that can be used by low-end agents to iteratively build.” Minifigures and Technic machines and engines are also on the project’s to-do list. Using AI agents to do tasks through programming is not new but is becoming more sophisticated, as seen in a run posted Friday in which Astra cleared World of Warcraft’s orc starting area from one prompt.

Antelo built the project to get AI agents “capable of designing buildable, physical things.” For now, the bricks only exist in CAD, but he’s considering 3D-printing a small model.

AI agents can work with 3D printing, too, through Model Context Protocol servers: Kiln can upload a file to a printer and start the print, while OctoEverywhere’s server lets an agent check on a print and pause, cancel, or resume it. This could bridge the gap between an AI model making lines of code and the production of something tangible. In time, physical AI through robots could even do the building part, but where’s the fun in that? In the meantime, you can try to design the LEGO set that’s always lived in your head.



Follow Tom's Hardware on Google News to get our latest news, analysis, & reviews in your feeds.

![Shane Downing](https://cdn.mos.cms.futurecdn.net/Zosi9VrDytS9FkgJiHvc69-140-80.png)

Shane Downing is a Contributing Writer for Tom’s Hardware, covering consumer storage, PC hardware, and AI.
