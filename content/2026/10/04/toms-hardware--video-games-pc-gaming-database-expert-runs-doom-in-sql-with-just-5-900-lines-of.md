---
title: Database expert runs Doom in SQL with just 5,900 lines of code — 1,300-line
  graphical renderer spans 89 different tables, full-featured SQLDoom is the sequel
  to embryonic DoomQL
source_url: https://www.tomshardware.com/video-games/pc-gaming/database-expert-runs-doom-in-sql-with-just-5-900-lines-of-code-1-300-line-graphical-renderer-spans-89-different-tables-full-featured-sqldoom-is-the-sequel-to-embryonic-doomql
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-04T17:08:13Z'
published: '2026-10-04T00:00:00Z'
description: Complete with full graphics at 60 FPS, sound, and even multiplayer.
image: https://cdn.mos.cms.futurecdn.net/osXJbTYcHoB7PvbPGLU4ij-1642-80.png
categories:
- Technology & Software
- Hardware
- Video Gaming
- Business & Entrepreneurship
people:
- Bruno Ferreira
- Lukas Vogel
- Tom
locations: []
organisations:
- BSP
- Carmack
- DoomQL
- Get Tom's Hardware
- GitHub
- Google News
- PC
- Python
- SQL
- SQLDoom
- Tech Report
- Tom's Hardware
- Vogel
---

![SQLDoom](https://cdn.mos.cms.futurecdn.net/osXJbTYcHoB7PvbPGLU4ij-1642-80.png)

It's the year of two thousand and twenty-six, and "Running *Doom* on X" is still probably the most popular software hacking hobby. From pregnancy tests to space satellites, the 1993 game has been ported to pretty much anything under the sun that has a CPU and some memory in it. Now it's time to run the game in a database, in this case CedarDB, courtesy of the SQLDoom project by Lukas Vogel, who previously authored DoomQL.

If you're wondering how the heck one runs a game in SQL, it's actually much easier than you imagine, so long as you think like a database architect. The actual frontend displaying the graphics, playing sound, and taking inputs is in Python, but that part acts only like a PC's peripherals — all the math is done inside the database.

The backend is written for the performance-focused, Postgres-compatible RDBMS CedarDB. Much like modern *Doom* ports, SQLDoom uses two paths: one running at the game's original 35 Hz for handling all the logic, and a separate thread for displaying graphics, interpolating camera position between game updates.

To start, Vogel had to convert the entities in *Doom*'s WAD package file to databases. That was easier than expected, as the data therein "is highly relational already," with Vogel presenting the example of map levels ultimately being structured in parent-child relationships that are trivial to replicate in plain tables. 1000 lines of Python was all it took.

For the main gameplay loop, Vogel was once again pleasantly surprised that the game logic was easy to convert. The resulting code was 5,900 lines of SQL, compared to the original C source code's 9,000. A lot of the savings came from the fact that whereas one has to iterate over entities with "for" or "while" loops to update values, a simple "UPDATE... WHERE" is enough in SQL to do that in just one statement — and in parallel, no less. As an added bonus, the fact that everything is a row in a database table makes for some trivial instant modifications, like changing weapon characteristics or enemy behavior on-the-fly.

The graphical renderer is also small at 1,300 lines, but it's trickier as it's the one query spanning 89 tables. Vogel notes that the pipeline is ultimately very similar to that of *Doom*. Data for Carmack's then-revolutionary Binary Space Partitioning (BSP) traversal, an implementation of binary trees, can be easily represented as a table.

Each left/right value can be converted to a bit, and ultimately the vertex order value can be reduced to just the one number. Thus, a simple "SELECT... ORDER BY" automagically sorts the walls front-to-back for you. Amusingly, I used the very same database technique when I wrote the defunct *Tech Report*'s threaded comments system. Despite his best efforts, Vogel says the floor and ceiling renderers didn't map very cleanly to SQL, as ultimately they're clever flood-fill algorithms.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

When it came to multiplayer, that's when using a database was actually *much better* than the original game. The reason is simple: maintaining synced states across many tables with copious amounts of interdependencies is literally what databases are designed for, so snapshots, authentication, access control, are all effectively free and implemented for you. To run a game tick, all you need is "START TRANSACTION," run the logic, and "COMMIT," and everything magically synchronizes.

You can peruse or download SQLDoom from its GitHub repository, or read Vogel's entertaining blog post detailing the adventure.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G-140-80.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.
