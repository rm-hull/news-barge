---
title: OpenAI says actors linked to China-based Moonshot AI spearheaded a campaign
  to extract its models’ hidden reasoning — logged 16,000 extraction requests across
  4,000 accounts before cutoff
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/openai-says-actors-linked-to-moonshot-ai-spearheaded-a-campaign-to-extract-its-models-hidden-reasoning-logged-attempts-peaked-at-16-000-users-over-two-days
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-01T13:10:36Z'
published: '2026-10-01T00:00:00Z'
description: OpenAI disrupted the campaign from July and has tightened its protections.
image: https://cdn.mos.cms.futurecdn.net/ZAD3iv3s8sBSmZNAoBfxGj-1104-80.png
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
people:
- Claude
- Greg Brockman
- Kimi K3
locations: []
organisations:
- Anthropic
- Get Tom's Hardware
- Google News
- Moonshot AI
- OpenAI
- Shane Downing
- Tom’s Hardware
---

![A glowing doorway on a dark landscape, ringed by streaks of orange and blue light](https://cdn.mos.cms.futurecdn.net/ZAD3iv3s8sBSmZNAoBfxGj-1104-80.png)

OpenAI said in a company blog post that people associated with China-based Moonshot AI were at the core of an effort to pull hidden reasoning from its models. The post says that a “coordinated campaign” to extract “protected reasoning” from its models, which was “consistent with adversarial distillation,” occurred in July. OpenAI isn’t sure whether all of the operators it saw were a single actor.

Activity began on July 1st, “initially at a low volume.” After that came “high-volume spikes” on July 24 and 25, with 16,000 requests using an extraction pattern. The requests came from over 4,000 users. The activity attempted extraction but was “not necessarily successful,” and the campaign was “fully disrupted by July 28.” The post did not clarify any measure of success rate, which models were specifically targeted, or how many of the users were Moonshot-linked.

OpenAI defines protected reasoning as “the model’s internal record for working through a task” and adversarial distillation as the “systematic and unauthorized use of one model’s outputs or reasoning” to train or improve another model. This data is encrypted to hide the model’s chain of thought and is handed to the client as an encrypted block. The client sends that block back with each request, so the provider doesn’t have to store it. One method the operators tried took the encrypted reasoning from one conversation and asked a model in another to decrypt it.

OpenAI says the encryption, in this case, was not broken. There was no direct access to stored user conversations, and no database was compromised. One fix closed a pathway that let someone who already had another user’s encrypted reasoning replay it and recover its contents. Separately, it added checks to detect and hold streamed output that might expose reasoning. It also strengthened protections for hidden reasoning across users, workspaces, organizations, and model families, and worked with third-party providers to disrupt accounts whose activity moved through their services.

Independent security researchers had also brought “related cross-model and conversation-compaction vulnerabilities” to OpenAI through responsible disclosure, and the company confirmed the attack paths they found were real. The paper “Stealing Reasoning Traces from Proprietary LLM APIs,” dated Aug. 10, is explicitly linked by the post. Testing OpenAI, Anthropic, and Google, the researchers fed a frontier model’s encrypted reasoning to a corresponding weaker model, which then wrote it out in plain text. The researchers ran their test in early July and, after the providers acknowledged their report, they were “unable to launch the same attacks.”

OpenAI is not alone in facing such threats. Earlier this month, Anthropic’s report “Detecting and countering misuse of AI: September 2026” detailed a single ten-day period in which Moonshot relayed almost 300,000 customer requests to Anthropic using a proxy network of 5,380 fraudulent accounts. The report also says Moonshot saved Claude’s reasoning signatures and, in new sessions, got Claude to convert them back into full reasoning traces, which Anthropic calls “cross-session replay attacks.” In July, Moonshot denied that Kimi K3 was created from a distillation, and at the time OpenAI President Greg Brockman said it was “too early” to tell whether Moonshot had distilled OpenAI’s models.

OpenAI’s next step, meanwhile, is to ensure partner-hosted deployments have the same protections as first-party tools. Additional checks are needed to prevent tool-output attacks. It shared its findings with the Frontier Model Forum and government information-sharing channels, noting that “systems that support portable or replayable reasoning artifacts may face related risks.” The company expects distillation attempts to grow more sophisticated as frontier models improve and as attackers look for cheaper ways to mimic them. The work to protect against those attempts is ongoing.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.



*Follow* * Tom’s Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Shane Downing](https://cdn.mos.cms.futurecdn.net/Zosi9VrDytS9FkgJiHvc69-140-80.png)

Shane Downing is a Contributing Writer for Tom’s Hardware, covering consumer storage, PC hardware, and AI.
