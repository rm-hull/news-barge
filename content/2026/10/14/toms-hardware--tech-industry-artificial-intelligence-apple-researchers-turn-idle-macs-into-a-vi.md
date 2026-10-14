---
title: Apple researchers turn idle Macs into a virtual GPU cloud with ‘Minions’ —
  researchers say the distributed scheme could scale globally and support model training
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/apple-researchers-turn-idle-macs-into-a-virtual-gpu-cloud-with-minions-researchers-say-the-distributed-scheme-could-scale-globally-and-support-model-training
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-14T11:50:57Z'
published: '2026-10-14T00:00:00Z'
description: Can start with a simple request over Slack, but teams worry about their
  data running on devices outside their group.
image: https://cdn.mos.cms.futurecdn.net/Wjvd8aPH3tzi8eZYrAmXN7-2560-80.jpg
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
- Science
people:
- Mac
- Slack
- Tim Cook
locations: []
organisations:
- AI
- Apple Intelligence
- Apple’s Machine Learning Research
- GPU
- Get Tom's Hardware
- Google Cloud
- Google News
- Mac
- Minion Server
- Minion Watchdog
- Minions
- Nvidia GPUs
- OpenClaw
- S3
- Shane Downing
- Tom’s Hardware
- WWDC
---

![A person works at an office desk on a MacBook Pro connected to two external displays](https://cdn.mos.cms.futurecdn.net/Wjvd8aPH3tzi8eZYrAmXN7-1920-80.jpg)

Apple internally uses a system known as “Minions,” a “virtual GPU cloud” made up of idle Macs, to help manage workloads, as described in a recent arXiv paper published by its researchers. The system helps take stalled AI jobs, some that once had 10-plus-hour company GPU queues, and distributes them to Macs on the network, with resulting wait times down to as little as minutes. A request from a user on the company’s Slack can get the ball rolling, although the researchers observed a common concern about teams’ data running on devices outside their group.

The paper, also shared on Apple’s Machine Learning Research site, describes the system as having a “Minion Server,” a “Minion Executor,” and a “Minion Watchdog.” The system relies specifically on Apple Silicon for AI inference, the only type of work it does. There are two kinds of jobs: embeddings with open-source Hugging Face transformer models, and text generation from large language models through Ollama, which is installed on each participating Mac.

The Minion Server works by splitting submitted tasks into subtasks, stored in a PostgreSQL database. Then, on each Mac, a Minion Executor is run to pull the next subtask over REST APIs; there is no central scheduler in this “pull-based execution model.” The Mac reads inputs from Amazon S3, grabs the model if needed, runs the subtask on its own GPU, then returns the result to S3.

![Diagram of Apple&amp;rsquo;s Minions system](https://cdn.mos.cms.futurecdn.net/JHEZ8hjMGMPj4NQvpRPqBT-1200-80.png)

Failures are caught by the Minion Watchdog, which tracks the heartbeats that Macs running work send every five minutes. Unfinished subtasks end up back in the queue when, for example, a Mac goes to sleep, drops off the network, powers off, or a user stops the executor to get control of the machine back. The owner can determine which jobs the Mac takes first, such as preferring one team’s or project’s jobs with “dynamic task binding,” or can rely on the default first-in, first-out scheme.

Our understanding is that each Mac runs a whole model on its own piece of work, and the paper does not suggest that any one model is split across Macs. Running a model entirely on one Mac’s hardware with unified memory should come as no surprise to OpenClaw enthusiasts who practice the same in their own home labs. The volunteer computing angle is also not new, reminiscent of SETI@home’s and Folding@home’s model of distributing small chunks to idle machines, based on the paper’s described architecture.

Aside from the reduction in GPU queue times, the paper also cites that requests with Minions do not require new GPU requests, the infrastructure cost is zeroed, and the scaling effort goes from manual to organic. This does not factor in the electricity costs or hardware wear.

Participation is handled informally, and team members may, for example, “send Slack messages requesting others to temporarily run the Minion Executor and target a specific project or task.” Confidentiality remains a concern even for internal work, which Apple aims to mitigate with team- and organization-scoped deployments with their own databases and separate pools of Macs.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

The new paper comes at a time when compute is increasingly a bottleneck for AI-related workloads. Apple acknowledges this in its latest quarterly filing in July, saying that it “depends on access to sufficient computing resources” in an ecosystem with “constrained supply, extended lead times, and increasing costs.” The risk that it may be unable to “secure sufficient capacity,” even with its own data centers and third-party cloud providers, appears to make the Minions approach more practical.

Apple’s Private Cloud Compute, the server side of Apple Intelligence for more complex requests, now also runs on Nvidia GPUs in Google Cloud, first announced at WWDC in June. That came after sudden and high Mac demand for local AI, with then-CEO Tim Cook saying in April that the Mac mini and Mac Studio supply may take months to catch up. Device supply discussed in the July earnings call also mentioned advanced-node constraints and increasing memory costs.

The authors say that, in future work, Minions will extend to distributed model training. More broadly, they write that if idle Macs across organizations “or potentially across the global community” can be “securely federated,” they could form a shared GPU pool. For now, the Macs act as overflow AI capacity only inside Apple.



*Follow* * Tom’s Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Shane Downing](https://cdn.mos.cms.futurecdn.net/Zosi9VrDytS9FkgJiHvc69-140-80.png)

Shane Downing is a Contributing Writer for Tom’s Hardware, covering consumer storage, PC hardware, and AI.
