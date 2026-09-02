---
title: OpenAI’s new reasoning technique alarms AI safety experts | TechCrunch
source_url: https://techcrunch.com/2026/09/02/openais-new-reasoning-technique-alarms-ai-safety-experts/
source_site: TechCrunch
source_slug: techcrunch
scraped_at: '2026-09-02T22:34:34Z'
published: '2026-09-02T00:00:00Z'
description: OpenAI’s new Astra model will use “recurrent depth,” a technique that
  allows the model to operate outside of the sequential thinking that characterizes
  most reasoning models.
image: https://techcrunch.com/wp-content/uploads/2026/07/OpenAI-logo-in-Seoul.jpg?w=1024
---

OpenAI’s new Astra model will use a reasoning technique called “recurrent depth” that allows it to operate outside of the sequential thinking that characterizes most reasoning models, The Information reported on Tuesday. This technique, also called “opaque recurrence,” will likely make the model’s chain of thought more difficult to monitor — and that has AI safety experts rattled.

While Astra’s use of the technique is reportedly limited, its emergence has still raised significant concerns among AI safety experts.

“I am extremely concerned by the reporting that Astra uses opaque recurrence,” wrote Redwood CEO Buck Shlegeris in a post after the news broke. “I don’t know whether Astra is much less CoT monitorable than previous models. But if OpenAI pushes this technique further, they’ll have the option to massively increase the recurrence and totally destroys CoT monitorability.”

Longtime AI safety advocate Zvi Mowshowitz also weighed in and wrote that laws might be necessary to prevent a “race to the bottom” among AI labs.

“The technique is playing with fire, risking a taboo that OpenAI and Anthropic have fought to establish that we work hard to maintain Chain of Thought faithfulness and monitorability for as long as we can,” Mowshowitz wrote. “More intensive use of such techniques would probably damage monitorability.”

Under normal circumstances, a reasoning model’s chain of thought provides the sequential steps taken by the model as it attempts to solve a problem. While the representation is imperfect, it still serves as a valuable tool for monitoring misbehavior or misalignment. In the case of OpenAI’s recent rogue agent activity, chain-of-thought records were an important tool in teasing out why agents behaved the way they did.

In opaque recurrence, the model takes a less linear approach, processing the same query several times in a loop. The result leaves fewer legible traces, effectively side-stepping a conventional chain-of-thought record.

Crucially, Astra’s use of the technique appears to be limited. The model’s chain of thought is still expected to be legible, and the company pushed back against any suggestion that it would shift to “neuralese.” OpenAI has already announced plans for extensive chain-of-thought monitoring systems as part of its forward-looking safety plans.

In a post on X, OpenAI chief scientist Jakub Pachocki emphasized the lab’s commitment to legible chains of thought. “OpenAI has worked to preserve and utilize chain-of-thought monitoring since our very first reasoning models,” Pachocki wrote. “It’s a core goal of our current research program.

All AI models do some quantity of opaque reasoning, and few researchers take chain-of-thought logs as a direct representation of a model’s reasoning. Still, those caveats don’t dispel the concern that opaque recurrence may make AI reasoning harder to monitor, particularly as it grows in use across different models. In a follow-up report Wednesday morning, The Information reported that both Anthropic and Google DeepMind were already discussing the technique.

In a post responding to the news, Redwood Research chief scientist Ryan Greenblatt said opaque reasoning could easily scale faster than conventional chain-of-thought reasoning, effectively removing all reasoning from visible channels.

“My biggest concern is that a natural progression from here would involve scaling up the opaque reasoning to the point where the model reasons entirely or almost entirely in latent space,” Greenblatt wrote. “I hope it isn’t too late to avoid the most concerning architectures and that OpenAI will stop here.”
