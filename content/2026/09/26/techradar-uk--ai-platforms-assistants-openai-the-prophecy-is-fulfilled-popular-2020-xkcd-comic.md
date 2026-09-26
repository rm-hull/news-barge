---
title: '''The prophecy is fulfilled'': Popular 2020 XKCD comic predicted ''HEIF Heist''
  OpenAI hack and even mentions ImageMagick in spooky coincidence'
source_url: https://www.techradar.com/ai-platforms-assistants/openai/the-prophecy-is-fulfilled-popular-2020-xkcd-comic-predicted-heif-heist-openai-hack-and-even-mentions-imagemagick-in-spooky-coincidence
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-26T04:55:04Z'
published: '2026-09-26T00:00:00Z'
description: xkcd joked in 2020 that ImageMagick would "break for good" one day
image: https://cdn.mos.cms.futurecdn.net/bqTLGsRATg4oc47RW3PJbi-2560-80.jpg
categories:
- Technology & Software
people:
- Hacktron
- ImageMagick
- Randall Munroe
locations:
- Nebraska
- OpenAI
organisations:
- Anthropic
- Astro
- CEOs of OpenAI
- ChatGPT
- Debian
- Discourse
- GitHub Enterprise
- Hacktron AI
- ImageMagick
- Meta
- Ruby on Rails
- Slack
- TechRadar Pro
- UN
---

![OpenAI logos](https://cdn.mos.cms.futurecdn.net/bqTLGsRATg4oc47RW3PJbi.jpg)

* **Hacktron chained a libheif heap overflow, reached through ImageMagick on OpenAI's Discourse forum, leveraging an OpenAI SSO flaw to briefly take over employee ChatGPT and Codex accounts**
* **The researchers themselves invoked XKCD #2347, whose 2020 alt text happens to name ImageMagick as the dependency that will one day break**
* **ImageMagick served as only the pathway to the actual vulnerable component, libheif, an obscure decoder pulled in indirectly across Slack, Meta, and GitHub Enterprise amongst other mediums**

When Hacktron AI recently disclosed its months-long libheif research, the researchers reached for a familiar picture that also, to some degree, hints at what let them break into OpenAI in the first place.

They pointed readers to xkcd #2347, Randall Munroe's 2020 iconic web cartoon of all modern digital infrastructure balanced on a single load-bearing block that some random person in Nebraska has been thanklessly maintaining.

The comparison is relatively easy to follow, and it has a bonus easter egg that one can take as pre-empting the hack.

## An alt-text that that seems ironically prophetic in 2026

The easter egg in question is one you have to look for; if you hover over the original comic, you get the alt text "Someday ImageMagick will finally break for good, and we'll have a long period of scrambling as we try to reassemble civilization from the rubble."

The irony is that six years after the comic was originally posted, ImageMagick was sitting in the exact spot the breach ran through, making its teaser something you could call an unintended prophecy bound to fruition.

The details are unglamorous but worth considering as AI safety continues to take center stage in public discourse, including recent addresses by the CEOs of OpenAI and Anthropic at the UN.

Hacktron found that OpenAI's community forum, community.openai.com, runs on Discourse. The latter's usual image checker, FastImage, doesn't understand HEIF and quietly hands tasks to ImageMagick's magick command for conversion, which in turn calls libheif, the library that actually decodes the format.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The version shipped to the forum was deployed via Debian and had a heap buffer overflow issue that was fixed the previous year without being labeled a potential security risk, allowing it to serve as a doorway for the Hacktron team.

The team then chained multiple exploits in an elaborate hack that culminated in leveraging a secondary SSO (Single Sign-On) misconfiguration at OpenAI's end, which essentially allowed the forum to serve as a gateway to ChatGPT and Codex accounts for anyone with a community account who signed in through the forum.

This allowed them access to ChatGPT's internal GitHub, where they made what they describe as a harmless pull as a proof of concept and notified OpenAI. OpenAI patched it 14 hours later, awarded the team a $6,500 bug bounty, and Discourse patched it after rating the underlying image bug 8.8 on the CVSS scale and adding sandboxing around image processing as a defense-in-depth measure.

The exploit is not exclusive to OpenAI: the same libheif and libde265 decoders reach production through ImageMagick, libvips, Sharp, standard distribution packages, and prebuilt container images. Hacktron traced them across Slack, Meta, GitHub Enterprise, Ruby on Rails, and Node.js frameworks, including Next.js, Astro, and Gatsby, suggesting that potential fallout, if not patched, is far broader than one AI company.

Hacktron's approach involved using Anthropic's Claude Opus 4.8 before switching to Opus 5, spending under $3,000 in tokens across a three-person team, and having an exploit ready in just two months. To its credit, the team had to trick Anthropic's AI into doing the task by framing their own test forum as a capture-the-flag challenge, and it eventually acquiesced.

The exploit itself wasn't something that couldn't be done without AI, but it let a much smaller team work at a pace normally expected of a much larger one. Apparently, asking your AI chatbot nicely with a bit of trickery in tow can deliver exceptionally good results in some cases.
