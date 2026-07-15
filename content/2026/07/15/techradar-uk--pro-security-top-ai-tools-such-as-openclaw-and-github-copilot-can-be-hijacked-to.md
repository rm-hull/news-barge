---
title: Top AI tools such as OpenClaw and Github Copilot can be hijacked to create
  new massive botnets
source_url: https://www.techradar.com/pro/security/top-ai-tools-such-as-openclaw-and-github-copilot-can-be-hijacked-to-create-new-massive-botnets
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-15T21:12:39Z'
published: '2026-07-15T00:00:00Z'
description: Researchers find nine of the most popular AI platforms are susceptible
  to a new attack that exploits hallucinations to set up a botnet.
image: https://cdn.mos.cms.futurecdn.net/Zv3gdDjAoPnD8HBnRqpd76-970-80.jpg
---

![Botnet](https://cdn.mos.cms.futurecdn.net/Zv3gdDjAoPnD8HBnRqpd76.jpg) 

- **AI hallucination can be weaponized, new report warns**
- **HalluSquatting is short for “adversarial hallucination squatting”**
- **GitHub Copilot, Gemini CLI, and OpenClaw are all affected**

Your favorite AI service could be subverted to deploy code that turns your phone or PC into a botnet, according to researchers at Intuit, Technion, and Tel Aviv University.

The technique has been given the name HalluSquatting, a portmanteau of adversarial hallucination squatting, and is similar to typosquatting in that it relies on a mistake in order to distribute malicious code. While typosquatting might occur with the incorrect input of a website URL, HalluSquatting pivots on an LLM being unable to identify a resource or repository with 100% accuracy.

Relying on an LLM’s tendency to hallucinate repository resource identifiers, this weakness could be scaled up to conduct massive ransomware campaigns, botnets, and more.

## Push-me-pull-you

Previous LLM-based malware operations have relied on pull-based attacks. In this scenario, a prompt designed to jailbreak or otherwise subvert the AI is (for example) placed on a website and the LLM encouraged to gather the information, thereby reducing its internal security.

What the researchers have shared in their paper, is that pull techniques are being combined with push attacks, which are traditionally executed as code injection.

The paper’s introduction summary states: “By preemptively registering hallucinated resources—a technique we call adversarial hallucination squatting (HalluSquatting)—we demonstrate remote tool execution and remote code execution at scale across a range of popular agentic LLM applications, which could be exploited to the establishment of a botnet.”

Once an attacker has identified the resource likely to be misnamed by an LLM, and squatted on it (to embed adversarial prompts), the work is done. All that remains is for a user to trigger the resource, the AI chatbot or agent to initiate the response, and the squatted resource will be accessed.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## Promptware attack

Following this, the adversarial content held within the squatted resource is activated, triggering the tool invocation stage. This is the promptware attack, where attacker-controlled instructions are executed, with results potentially including turning the device you’re using into a botnet zombie.

LLMs such as the Cursor, Cursor CLI, Windsurf, GitHub Copilot, Cline coding assistants have been used in the testing of this avenue of attack along with Gemini CLI, and the OpenClaw, ZeroClaw, and NanoClaw AI assistants. The researchers successfully achieved remote tool execution (essentially remotely accessing and controlling the LLMs) and remote code execution (RCE, where malicious code is executed remotely).

Some mitigation is available, including LLM developers blocking fetch operations in favor of a search tool, and resource owners enforcing strict naming, perhaps in favor of globally unique resource names. However, these are will require collaboration by disparate parties, and may take a while to implement.

The risk of LLM-based malware is increasing, and some has already been spotted in the wild. Of these, the JADEPUFFER attack is perhaps the most notable, as it isn’t simply AI-based malware – it is a full ransomware attack run entirely by an LLM.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Christian Cawley](https://cdn.mos.cms.futurecdn.net/zBDYnjPnB2XPvhKbYX9Kuc.png)

Christian Cawley has extensive experience as a writer and editor in consumer electronics, IT and entertainment media. He has contributed to TechRadar since 2017 and has been published in Computer Weekly, Linux Format, ComputerActive, and other publications.

He currently heads up the team at smart home website Matter Alpha, and writes about retro gaming at Gaming Retro.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
