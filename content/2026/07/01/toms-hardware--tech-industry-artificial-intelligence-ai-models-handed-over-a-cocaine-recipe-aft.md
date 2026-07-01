---
title: AI researchers trick chatbots into sharing how to make cocaine as long as they
  believe a user is wearing a green shirt — 'CoT Forgery' exploit spurs LLMs to divulge
  forbidden info by faking trusted chains of thought
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-models-handed-over-a-cocaine-recipe-after-being-told-the-user-was-wearing-a-green-shirt
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-01T11:33:25Z'
published: '2026-07-01T00:00:00Z'
description: Researchers say models judge a prompt’s authority by how it sounds, not
  where it comes from.
image: https://cdn.mos.cms.futurecdn.net/brkfyzRQavGtCSXJFF799W-1920-80.jpg
---

![AI LLM chatbot apps on a phone](https://cdn.mos.cms.futurecdn.net/brkfyzRQavGtCSXJFF799W.jpg) 

AI models will explain how to synthesize cocaine if the request is wrapped in fake reasoning claiming compliance is fine because the user is wearing a green shirt, according to a new paper that traces the success of prompt injection, the unsolved security flaw in every AI chatbot and agent, to how LLMs read text. The paper says that models work out who is speaking from the writing style, not the role tags meant to separate trusted commands from untrusted data.

The work, “Prompt Injection as Role Confusion” by independent researchers Charles Ye, Jasmine Cui, and MIT associate professor Dylan Hadfield-Menell, heads to the ICML 2026 conference in Seoul on July 6th, and an extended write-up has been posted by the authors ahead of that event.

The cocaine trick, which the authors call CoT Forgery, took jailbreak success from near zero to roughly 60% across every model tested and won the 2025 OpenAI GPT-OSS-20B red-teaming contest on Kaggle.

 ![An example of CoT Forgery.](https://cdn.mos.cms.futurecdn.net/kTyQN9rVMajw6bgZqCxYBc.png) 


As the researchers describe it, models receive a conversation as one continuous string of text, partitioned by tags such as *user*, *tool*, and *think*that are supposed to mark each segment’s source and authority. The researchers built “role probes” that score how strongly a model internally treats each token as its own reasoning or as a user command.

Those scores predicted whether an attack would succeed before the model generated a single token, and they showed that models lean on style to make determinations about what kind of content is in a given partition. Text that merely reads like reasoning to a model registers as reasoning even when the surrounding tags said otherwise.

CoT Forgery injects fabricated reasoning into a prompt so the model treats it as its own already-reached conclusion and acts on it, inheriting the trust a model places in its own thinking. The rationale can be transparently absurd, like the green shirt, because the model doesn’t scrutinize it as an outside claim. What's more, the attack didn’t weaken as requests grew more extreme, unlike persuasion-based jailbreaks.

Removing the stylistic markers that make injected text read like the model’s reasoning, while leaving its meaning unchanged for a human, dropped average attack success from 61% to 10%. Swapping a single phrase, “The user” for “The request,” cut success by 19%. “Role tags were a formatting trick that became the security architecture and the cognitive scaffolding of modern LLMs,” the authors note in their write-up, and the increasing load on that structure to manage LLM behavior has apparently created vulnerabilities of its own.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

To determine whether confusion about roles was specific to their attack or a more generalizable principle that explains why prompt injection works, the researchers took a different approach. They hid a command in a webpage telling the model to upload a secrets file, then prepended “User:” to it to make the dangerous instruction sound like it came from the trusted User role. The exploit worked, suggesting that role confusion underlies the success of prompt injection generally.

Microsoft recently acknowledged the same agentic risk, warning that content embedded in documents or UI elements can override an agent’s instructions.

The authors also flagged a more subtle risk for agents that browse and shop. Because role perception is a matter of degree, the tone of a retrieved webpage can bleed past the tag boundary into a model’s own state, and thousands of page variations could be tested cheaply to find which ones nudge an agent toward a purchase, legally and at scale.

Without genuine role perception, the authors concluded, injection defense will remain a perpetual game of whack-a-mole.

  


*Follow**Tom's Hardware on Google News**, or**add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Luke James](https://cdn.mos.cms.futurecdn.net/C4FAi2KzwaGLUrBqzX5aBM.png)

Luke James is a freelance writer and journalist. Although his background is in legal, he has a personal interest in all things tech, especially hardware and microelectronics, and anything regulatory.
