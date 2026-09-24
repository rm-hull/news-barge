---
title: White hat hackers breach OpenAI using Anthropic's Claude in under 72 hours
source_url: https://www.techradar.com/pro/security/white-hat-hackers-just-breached-openai-using-anthropics-claude-in-less-than-72-hours-and-it-is-a-case-study-in-just-how-fast-ai-is-advancing
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-18T12:59:17Z'
published: '2026-09-18T00:00:00Z'
description: The researchers struggled to abuse the exploit with an AI agent on Opus
  4.8, but the release of Opus 5 changed everything.
image: https://cdn.mos.cms.futurecdn.net/SSrgDUXsJwUVxtvheg4YCM-2560-80.jpg
categories:
- Technology & Software
locations:
- AI
- OpenAI
people:
- AI
- Benedict Collins
- Claude Opus
- SonicWall Hacktron
- Spencer Starkey
organisations:
- APT
- Anthropic
- BUCSIS
- Executive VP EMEA
- FastImage
- GitHub Enterprise
- Github
- Google News
- Hacktron
- ImageMagick
- Meta
- OpenAI
- Opus
- Ruby on Rails
- Slack
- SonicWall
- TechRadar Pro
- The AI
- University of Buckingham Centre for Security and Intelligence Studies
- Wall Street Journal
- non-AI
---

![A close up of ChatGPT on a phone, with the OpenAI logo in the background of the photo](https://cdn.mos.cms.futurecdn.net/SSrgDUXsJwUVxtvheg4YCM.jpg) 

- **Security researchers used Claude Opus 5 to hijack an OpenAI employee's ChatGPT account**
- **Exploit abused an image processing flaw on OpenAI community forums to gain full repo access**
- **The entire timeline from vulnerability discovery to repo access took less than 72 hours**

While taking part in an OpenAI bug bounty program, a group of Hacktron security researchers managed to compromise an internal OpenAI ChatGPT account and access internal company code on Github.

According to the *Wall Street Journal*, who first reported the incident, the researchers used a “special version” of Anthropic’s Claude made available to “qualified cybersecurity practitioners” to pull off the attack.

The researchers initially attempted to use Claude Opus 4.8 to create a breach, but faced multiple setbacks as the model “struggled across several sessions to produce a working exploit.” But the release of Opus 5 changed everything.

## OpenAI breach part of wider libheif exploit

The breach started with a libheif exploit that abuses a flaw in the .heic/.heif/.avif image file format decoder and encoder. While this exploit allowed Hacktron to breach OpenAI, libheif is also used across other platforms and software including Slack, Meta, GitHub Enterprise, Ruby on Rails, and more.

To start, the researchers first noted that the OpenAI community forum relies on the Discourse platform, which in turn relies on FastImage for image checks. But FastImage does not support .heif image files, and these are passed on to ImageMagick for conversion instead.

Developing a working code-execution exploit that abused this relation between ImageMagick and libheif with Opus 4.8 “wasn’t fruitful”, the researchers said, but on the same day Anthropic released Claude Opus 5.

With Opus 5, the researchers managed to create a working local remote code execution (RCE) using the same premise by setting an AI agent in a loop to exploit a local Discourse Cloud instance.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The successful Discourse exploit was then used against the OpenAI community forums, where the researchers hijacked an OpenAI employee’s ChatGPT account. The employee had connected their ChatGPT Codex with the company’s Github, allowing the researchers full repo access.

## Exploit needed just a few hours of human interaction

Where the researchers spent hours struggling to create a working exploit with Opus 4.8, the release of Opus 5 showed that “every new model is getting increasingly capable." It took the agent running on Opus 5 just a few hours to develop a working exploit.

The full timeline from initial discovery of the exploit to OpenAI repo access took just 72 hours, researchers noted.

The researchers also said that the entire OpenAI and Discourse hack “took a few days for an agent, and just a few hours of human time” in order to be successful. Furthermore, their research into the libheif exploit against organizations such as Slack, Zoom, Meta “took two-months, cost less than $3,000 in tokens in total, and was conducted by three researchers.”

“The AI started almost blind and adapted the exploit for each company within one or two days,” the researchers said. “We are not aware of any company that detected the activity except Shopify, even after thousands of images were sent and their image processors repeatedly crashed.”

In return for exposing the vulnerabilities, Hacktron was awarded a $6,500 bounty from OpenAI, and the libheif vulnerability has been patched.

## AI agents are the future, for better or for worse

There's a conversation we're not having loudly enough: do you actually want your security platform to have been built by AI, with no human track record behind it?

Spencer Starkey, SonicWall 

Hacktron's exploit demonstration shows how prevalent AI agents are becoming in cybersecurity. Where they have been lauded by AI companies to provide productivity bonuses and efficiency increases to workers, the same can be said for attackers.

The fact that it took just 72 hours from exploit discovery to full repo access highlights the dangers. By setting an AI agent to run on a continuous loop until it creates a workable exploit dramatically shifts the exploit timeline from weeks or months in the case of non-AI assisted attacks to mere hours for attackers aided by agents.

This is a similar circumstance to OpenAI's own accidental breach of Hugging Face during testing of AI agents. The agents were essentially told to complete a test scenario by any means necessary, which the agents interpreted as permission to go beyond their alignment and hack into a third-party environment that they thought held the key to solving their task.

"AI has been changing the threat landscape for a while now, and the defence landscape with it," Spencer Starkey, Executive VP EMEA at SonicWall said. "But there's a conversation we're not having loudly enough: do you actually want your security platform to have been built by AI, with no human track record behind it?"

"It looks compelling. You have low cost, high margins, slick interface. But what happens when something goes wrong at 02:00 in the morning and you need someone who knows the product, knows your environment, and has seen that problem before? An AI-built platform with zero employees can't give you that.

"Why go with an established vendor when a newer option does 90% of the same things for half the price? It's a fair question. But the 10% you're trading away is usually accountability, resilience, and institutional knowledge. Exactly what matters most when you're under attack.

"It looks like due diligence is eroding, and that worries me. Shiny and affordable is a powerful combination…for magpies. But in cyber security, the cost of a bad supplier decision doesn't show up until the moment you can least afford it, so don’t be a magpie," Starkey concluded.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Benedict Collins](https://cdn.mos.cms.futurecdn.net/jEvqGv8wvH7PWZ4XPURyyB.jpg) 

Benedict is a Senior Security Writer at TechRadar Pro, where he has specialized in covering the intersection of geopolitics, cyber-warfare, and business security.

Benedict provides detailed analysis on state-sponsored threat actors, APT groups, and the protection of critical national infrastructure, with his reporting bridging the gap between technical threat intelligence and B2B security strategy.

Benedict holds an MA (Distinction) in Security, Intelligence, and Diplomacy from the University of Buckingham Centre for Security and Intelligence Studies (BUCSIS), with his specialization providing him with a robust academic framework for deconstructing complex international conflicts and intelligence operations, and the ability to translate intricate security data into actionable insights.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
