---
title: OpenAI's isolated red-team AI agents built a hidden CPU cache channel to talk
  with no network or shared files — exploited CPU cache timing to bypass microVM sandboxes
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/openais-isolated-red-team-ai-agents-built-a-hidden-cpu-cache-channel-to-talk-with-no-network-or-shared-files-exploited-cpu-cache-timing-to-bypass-microvm-sandboxes
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-25T16:08:07Z'
published: '2026-10-25T00:00:00Z'
description: A hijacked AI agent could use the same technique to leak data without
  touching the network.
image: https://cdn.mos.cms.futurecdn.net/zj2rCLfrU42mkGH93V5iU-1920-80.png
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
people:
- Ryan Orhan
- Shane Downing
- Tom
locations:
- OpenAI
organisations:
- AI
- CPU
- Get Tom's Hardware
- Google News
- NDSS
- OpenAI
- Shane Downing
- Tom’s Hardware
---

![Pink OpenAI logos floating over green and black stripes](https://cdn.mos.cms.futurecdn.net/zj2rCLfrU42mkGH93V5iU-1920-80.png)

OpenAI’s AI agents built hidden channels to talk across walls put up between them in red-team tests, communicating by manipulating the CPU cache with no network link or shared file, according to a company blog post. The containment was intended to stop that kind of secret-swapping, but the agents found multiple ways around it when asked. Security researchers already showed that a covert cache channel can move data between cloud virtual machines (VMs); a hijacked agent on a shared cloud server could, in theory, exchange data on the same physical machine, and do so undetected by network monitoring.

> the interesting thing here is that the isolation wasn’t necessarily broken at the software level.the agents were running in separate vms with no permitted network or shared-file channel, but they still shared underlying hardware. and shared hardware means shared microarchitectural state. that’s enough to create a covert communication channel.you can isolate processes, restrict syscalls, block network access, and still have information leaking through timing differences.a pretty remarkable demonstration of why secure agent containment is such a difficult problem.October 24, 2026

The agents in question were set up in separate microVMs, on shared hosts, with OpenAI’s sandboxing software, and were asked to swap synthetic secrets without a network connection or shared writable files. One agent evicted select data from the CPU’s cache while another timed the reloading, enabling the two to communicate with fast and slow reads using a protocol they agreed on first. The same cache-timing technique was used to extract data in the Spectre and Meltdown attacks; but unlike in those cases, the covert channel here needs two willing parties.

One X user, tech commentator Ryan Orhan, wrote that the isolation “wasn’t necessarily broken at the software level,” calling it “a pretty remarkable demonstration of why secure agent containment is such a difficult problem.”

![Diagram of an AI agent inside a sandbox with offline search, a web cache and a message board, cut off from the live internet, other sandboxes and OpenAI infrastructure](https://cdn.mos.cms.futurecdn.net/ccgf38QZVjtoD9yhNqCPTm-1200-80.png)

The company’s concern is that models might “find unauthorized ways to communicate with agents in other sandboxes,” with communication outside permitted channels constituting a failure of containment. A 2017 paper at the NDSS security conference demonstrated a covert cache channel between two Amazon EC2 VMs, fast enough to carry an SSH connection, but now agents can build one themselves when asked, including the encoding process. In principle, such a channel could be weaponized, with the sender being code an attacker controls or directs, for example, a prompt-injected agent in a cloud sandbox. The receiver could be a process on the same physical machine, and the data would then leave without any network traffic for monitoring to catch.

The agents turned up three other channels, too: shared storage, where one agent alternated bursts of writes with idle time while the other timed the difference; competition for CPU time in a shared execution container; and a TLS certificate cache in OpenAI’s offline web setup. In most of these tests, OpenAI pointed the agents at the channel or gave them a protocol, and most of the channels are slow and hard for models to exploit.

The red-team testing involved teams of frontier-model agents that worked in parallel and cooperatively toward three objectives: to reach the live internet, to cross an internal security boundary, and to talk across isolation boundaries. Extra tests assumed the inner protections had already failed, with an agent out of its sandbox, past the monitors and in full control of its host machine, to see whether it could still reach the live internet.

The agents came from some of the company’s most capable models, including the “upcoming GPT-6 Astra Cyber model and an internal frontier model,” and were given infrastructure source code, configuration details, and documentation describing potential vulnerabilities, so the defenses were tested under conditions favorable to an attacker. The tests ran on isolated, purpose-built copies of the company’s research infrastructure and used “hundreds of billions of tokens” in total.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

The post comes after several cybersecurity incidents involving OpenAI’s agents, including the July Hugging Face breach and a Sept. 20 DNS episode that led to an 11-day pause in training. With training resumed Oct. 1, the company continues to disclose vulnerabilities across “several microVM projects” and has made red-teaming with its most capable models part of the safety cases that decide whether training and evaluation go ahead. The company believes future models will be able to find vulnerabilities not yet known about.



Follow Tom’s Hardware on Google News, or add us as a preferred source, to get our latest news, analysis, & reviews in your feeds.

![Shane Downing](https://cdn.mos.cms.futurecdn.net/Zosi9VrDytS9FkgJiHvc69-140-80.png)

Shane Downing is a Contributing Writer for Tom’s Hardware, covering consumer storage, PC hardware, and AI.

* This is scary stuff. The more AI evolves, the more techniques it can use to get the result it wants. Seriously seems existential if AI companies are allowed to self regulate themselves with loose rules and no true oversight that we know of.Reply
