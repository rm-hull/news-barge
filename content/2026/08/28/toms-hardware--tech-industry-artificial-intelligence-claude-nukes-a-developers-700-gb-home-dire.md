---
title: Claude nukes a developer's 700 GB home directory while testing deletion safeguards;
  automatic model safety downgrade may have contributed to the screw-up — Anthropic
  safety harness downgraded model to Opus 4.8 before fatal variable collision
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/claude-nukes-a-developers-700-gb-home-directory-while-testing-a-script-to-ensure-it-wouldnt-do-so-automatic-model-downgrade-may-have-contributed-to-the-screw-up
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-28T11:15:54Z'
published: '2026-08-28T00:00:00Z'
description: Who watches the watchmen?
image: https://cdn.mos.cms.futurecdn.net/rooXvESoBpBpBGCkrJPnwC-2059-80.jpg
---

![Robot arm beam](https://cdn.mos.cms.futurecdn.net/rooXvESoBpBpBGCkrJPnwC.jpg) 

Stories of AI agents running amok and following instructions literally, creatively, or a surprising mix of both are becoming common. In the case of developer Sebastien Guillemot, Claude ran an exceedingly effective cleanup operation: The bot managed to free 700 GB of disk space, but it was in the form of Guillemot's entire data folder and one week's worth of work, and it occurred after the model was automatically downgraded due to security concerns.

The developer frequently uses AI agents, and became a bit annoyed that a lot of them didn't clean up after themselves, leaving copious amounts of junk behind in the /tmp directory. Proving the old adage that once you have a hammer, everything looks like a nail, Guillemot asked Claude Fable to write a script that would sandbox each agent under its own folder in /tmp and run a cleanup after they were done. The main problem, naturally, was not deleting files that were actually in use.

 ![Claude destroying a developer's home directory](https://cdn.mos.cms.futurecdn.net/Aq2KPbGLAEoiXoEGXZ8ntP.png) 


Fable suggested adding logic to detect running agents and delay deleting their slice of /tmp, but Guillemot then told the bot the resulting code was far too complicated. Perhaps because the script involved hard deletion of data, Fable took it upon itself to perform an adversarial review, meaning the agent ran a new copy of itself to safety-check its own findings. Anthropic's harness then deemed the script risky enough to downgrade the model to Opus 5 and then Opus 4.8.

Opus 4.8 proceeded to run the safety test, attempting to match the targets of the deletion command against /tmp and the user's home directory to ensure a deletion command wouldn't be run against them. They were correctly identified as dangerous. However, since this was a code test, and you need to clean up after a test, the cleanup step deleted the user's home directory — it reused the same variable name for both the test itself and cleanup.

Guillemot stopped the process, but not in time. Adding insult to injury, after the agent wiped Guillemot's work, it did in fact leave /tmp behind. Some users suggested a few tools like Termaxa and other workarounds for these situations, but the fact that these tools need to exist in the first place is somewhat ironic.

The fact that the harness dropped to a lower-end model due to safety concerns likely contributed to the problem, too. Given that Fable 5 outperforms Opus 4.8 in coding tasks, it might have caught the contradiction with the variable names in the test.

The developer got most of his data back thanks to collecting information from git, nix, session logs, and so forth. Yet there's some irony: all these agents running, and not one daily backup.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.
