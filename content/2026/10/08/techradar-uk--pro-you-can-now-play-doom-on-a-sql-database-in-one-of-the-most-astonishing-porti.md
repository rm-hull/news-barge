---
title: SQLDoom turns database queries into a Doom engine
source_url: https://www.techradar.com/pro/you-can-now-play-doom-on-a-sql-database-in-one-of-the-most-astonishing-porting-projects-weve-ever-seen
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-09T01:14:05Z'
published: '2026-10-08T00:00:00Z'
description: Someone finally answered an internet complaint about a famous 90s shooter,
  and the fix turned into something nobody saw coming
image: https://cdn.mos.cms.futurecdn.net/tC3HZkHYzR4SiVWSTi4AZD-1920-80.png
categories:
- Technology & Software
people:
- Vogel
locations:
- CedarDB
- DoomQL
- Europe
- United States
organisations:
- CedarDB
- Doom
- DoomQL
- GitHub
- Lukas Vogel
- SQLDoom
- TechRadar Pro
- The Register
---

![Doom in an SQL database](https://cdn.mos.cms.futurecdn.net/tC3HZkHYzR4SiVWSTi4AZD-1920-80.png)

* **Vogel ported Doom to run entirely inside a SQL database**
* **The port draws 640×480 full-color frames from about 1,300 lines of SQL**
* **Missing BSP-tree traversal in DoomQL prompted Vogel to start a second version**

Developer Lukas Vogel has ported Doom to run entirely inside a SQL database, with both the game logic and rendering handled through queries.

The project, called SQLDoom, stores level geometry and game state in CedarDB tables, while a lightweight Python script handles timing, input, and display output.

The result produces 35 full-color frames per second at 640×480 resolution, using roughly 1,300 lines of SQL code divided across 89 query blocks.

## An earlier attempt fell short of real Doom

An earlier effort called DoomQL was launched last year and relied on raycasting with grayscale text characters, so it resembled Wolfenstein 3D more than Doom.

The raycasting skipped the BSP-tree traversal that helped distinguish Doom’s rendering approach, prompting Vogel to develop a second version.

For SQLDoom, the developer required both the rendering system and game loop to operate entirely through SQL, with output limited to exact-color tables or bitmaps.

“Rendering Doom in a database is obviously a bad idea,” Vogel said in a blog post about the project.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Building the new version meant recreating key parts of Doom’s rendering process using database operations rather than conventional game-engine code.

Handling the level geometry was relatively straightforward because a sort key calculated when each map loads lets a single ordering clause determine which wall sections are drawn.

Floors and ceilings presented a tougher problem. Doom’s original engine uses visplanes and state changes, neither of which translates neatly to column-by-column SQL rendering.

Vogel replaced that system with what he called a “pretty hacky” approach, looping through a sequence of sorted panels to fill those surfaces.

## Speed figures and server tests give mixed results

Vogel reports about 60 fps on a laptop with a Ryzen 7 7840U chip, though busy scenes can fall to 35 fps.

He said table overhead was substantial, yet the port still ran faster than his simpler DoomQL effort from last year.

"I intended it as a tech demo, but it just feels like the real Doom, even though it doesn't share a single line of code with any existing Doom port,” Vogel said.

The port also supports deathmatch play, with public online servers hosted in Europe and the United States open for multiplayer matches.

Reviewers who tried the online demos described sluggish performance, with one outlet suggesting the servers rather than the port itself were responsible.

Vogel argues a database keeps one steady record of game state, with “no partially applied updates, physics bugs, or disagreements over whether the rocket actually hit”

The Register noted the work doubles as a showcase for CedarDB, a database system that compiles complex queries into machine code.

Anyone wanting to try it can run the GitHub code locally with CedarDB and Doom's original WAD data, or join a free hosted match online.

Via The Register
