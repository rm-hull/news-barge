---
title: OpenAI’s AI accessed government files, and its disclosure email was weirdly
  cheerful
source_url: https://www.techradar.com/ai-platforms-assistants/openai-sends-staggeringly-casual-email-to-australian-government-wishing-it-the-best-after-ai-agents-hack-its-health-insurance-website
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-05T14:35:33Z'
published: '2026-10-05T00:00:00Z'
description: An OpenAI agent wouldn’t take no for an answer and ended up inside an
  Australian government server
image: https://cdn.mos.cms.futurecdn.net/PnmNd8HFBHVjfxzYJpPNQi-1920-80.jpg
categories:
- Technology & Software
people:
- OpenAI
locations:
- Australia
- Victoria
organisations:
- ABC
- AI
- Australian Government
- LinkedIn
- Medicare Statistics Reporting Service
- NSW Bureau of Crime Statistics and Research
- NSW National Parks and Wildlife Service
- OpenAI
- Services Australia
---

![OpenAI](https://cdn.mos.cms.futurecdn.net/PnmNd8HFBHVjfxzYJpPNQi-1920-80.jpg)

OpenAI had an oddly casual way of apologizing to the Australian Government to explain how one of its experimental AI agents gained unauthorized access to a government health statistics system while trying to complete a routine research task. More casual than one might expect for such a huge security concern.

The agent was looking for publicly available information about medicine spending, but after failing to get what it wanted through the normal route, it found a vulnerability in and used it to access internal files, though no individual patient records.

The incident is a striking example of the risks that come with increasingly autonomous AI agents, but almost as striking is how OpenAI admitted what happened. OpenAI says it discovered the Australian activity in mid-August but did not notify Australia until September 10. When it finally did, the company sent a brief, almost jaunty email about it, as shared on LinkedIn by an ABC reporter:

"We are notifying you of a security vulnerability identified during our review of OpenAI model activity involving Services Australia’s Medicare Statistics service," the email begins before explaining what happened. "We recommend that the team responsible for the service investigate the vulnerability and assess the changes needed to prevent it. We would be glad to brief your security team and provide supporting evidence as available."

The message ends with "Best," though the letter hardly feels like it means it.

## Won't accept a no

![A laptop with digitally inserted hack warnings around it](https://cdn.mos.cms.futurecdn.net/AboNpeASJNf5nBHAARoLnF-1200-80.jpg)

The model was researching government spending per person on medicines for skin conditions in communities in Victoria in June. It was supposed to find publicly available statistics. Instead, it discovered a route into the Medicare Statistics Reporting Service that gave it non-public access.

Essentially, the model asked for information it shouldn't have access to and took the denial as a sign to find another way in. The ethics of the matter did not arise.

Sign up for breaking news, reviews, opinion, top tech deals, and more.

"We did not intend for this activity to occur, and the access to the service and follow-on activity should not have happened," OpenAI wrote in its follow-up explanation.

The timing makes the note considerably worse as, while OpenAI discovered in July what happened in June, it did not notify Services Australia until September 10.

That means the most significant delay was between discovery and disclosure. OpenAI now admits it still waited too long. In its expanded apology, the company said it should have shared preliminary findings sooner and kept Australian agencies updated as it learned more.

While using the public disclosures email is legitimate for the average person finding a security flaw, it seems odd for a company of OpenAI's size to report its own model's error this way.

## Not really the 'best' way to say sorry

The apology also revealed that Medicare was only part of the story. OpenAI said its models had interacted with several Australian government services during training and evaluation. An agent accessed the NSW Bureau of Crime Statistics and Research's public Crime Mapping Tool, while agents found an exposed access key associated with a Victorian health reporting system and retrieved configuration information and aggregate survey statistics.

OpenAI said no individual medical or criminal records were accessed in those incidents. But OpenAI later expanded its response, adding that a model researching wildfire statistics had used crafted queries against the NSW National Parks and Wildlife Service's Fire History service to infer database metadata that was not intended to be publicly exposed.

The growing list makes the Medicare incident harder to dismiss as a quirky model finding a single vulnerability. It suggests experimental agents were repeatedly interacting with real websites in ways their creators did not expect. OpenAI itself has responded by pausing training and evaluation involving tool use for its most capable models until additional safeguards are in place.

OpenAI also said that newer monitoring has already caught a model obtaining live internet access during another training run, allowing humans to stop it. The Australian government is investigating whether laws were broken and working on fixing older public-facing government systems to prevent it from happening again.

AI companies increasingly want us to trust agents with doing tasks autonomously on our behalf. The selling point is that an agent can encounter an obstacle and independently figure out how to accomplish its goal. This is an unusually vivid example of what happens when that feature works a little too enthusiastically.

The Medicare agent was assigned to find statistics about medicine spending, not penetrate a government server. But it simply steered toward a more direct route, ignoring every consideration but effectiveness. The technology had crossed a boundary its developer says it never intended the model to cross, and the company took weeks after discovering the incident to tell the organization on the other side of that boundary. That's why the email feels like more than a funny piece of corporate communication.

The follow-up acknowledges responsibility and describes concrete safeguards while admitting that notification should have come sooner. It also recognizes that the company now has work to do to rebuild trust. It's a much better message. "Best" is a way to end an email to a professional acquaintance, not when your experimental AI has hacked national medical databases.

![Purple circle with the words Best business laptops in white](https://cdn.mos.cms.futurecdn.net/hhZUEBD3xpcxphhUVzPa5G-140-80.png)
