---
title: Meta Muse runs agents on AMD EPYC Turin hosts with two cores and 8GB of memory
  — AI agent can pass terminal commands to Ubuntu host system
source_url: https://www.tomshardware.com/pc-components/cpus/meta-muse-runs-agents-on-amd-epyc-turin-hosts-with-two-cores-and-8gb-of-memory-ai-agent-can-pass-terminal-commands-to-ubuntu-host-system
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-25T16:46:01Z'
published: '2026-09-25T00:00:00Z'
description: The 9D25 that hosts Muse comes with 128 cores and 256 threads.
image: https://cdn.mos.cms.futurecdn.net/9mJ37sc39kgcyEigsUfgNn-2560-80.jpg
categories:
- Technology & Software
- Hardware
people:
- Evan Hoffman
- Muse
- Tae Kim
- Tom
locations:
- Muse
- Turin
organisations:
- AI
- AMD EPYC Turin
- GPU
- Get Tom's Hardware
- Google News
- LLM
- Meta
- Muse VM
- SSH
- Tom’s Hardware
- VMs
---

![An EPYC Turin CPU sitting in a socket.](https://cdn.mos.cms.futurecdn.net/9mJ37sc39kgcyEigsUfgNn.jpg)

Meta's new AI agent Muse is powered by AMD EPYC Turin host systems, with each sandbox sporting two dedicated cores and 8GB of memory. Blogger Evan Hoffman and analyst Tae Kim both discovered that Muse will run some rudimentary Ubuntu commands if prompted, passing along the output to help identify things like the specs of the host system. More concerning is that Muse seems able to execute commands that might be unsafe, with Hoffman claiming that Muse offered to set up SSH to Muse's private VM.

> Imagine if one billion people used a personal AI agent. That's a lot of CPUs and memory pic.twitter.com/ibozUi3a07September 24, 2026

Both Kim and Hoffman asked Muse about the VM's specs, and in both instances, Muse revealed that it's running on AMD EPYC 9D25 CPUs, a high-density Turin chip with up to 128 cores. The VMs are running on Ubuntu 24.04 and using Linux kernel 7.0. The systems hosting Muse don't include GPUs. The AI agent revealed that Meta uses separate GPU servers for inference, isolating the agent to CPU-only sandboxes.

The agent suggests that each user gets their own private sandbox that's persistent, which allows us to do some math on how many people an individual tray can host. Assuming a 2P system that offers up to 512 vCPUs with 2TB of memory, hosting up to 256 Muse users. Muse has reportedly passed over 500,000 daily active users as of a few days ago, which would come out to somewhere around 2,000 server trays with dual EPYC 9D25 CPUs and 2TB of memory.

This is just some rough napkin math; don't take it as law. It's possible Meta has CPU-only servers deployed with multiple different chips to host Muse, and it's also possible there's overhead in the configuration. Turin chips support up to 6TB of memory with high-density DIMMs, for instance. Still, EPYC hosts seem popular for this use case, mainly because of their core density, as even a dual-core sandbox can add up quickly when multiplied across hundreds of thousands (or even millions) of users.

Muse isn't completely open. Hoffman shared an example where an attempted command failed due to improper permissions when Muse tried to query the kernel buffer. Presumably, sudo (admin) commands would be blocked as well.

> I feel like I could definitely reverse SSH tunnel into my muse's container. I already had it offer to SSH to my private VM and say I need to add its pubkey. Someone good at hacking could really have a field day.September 25, 2026

However, there might still be some security loopholes. Hoffman says that Muse offered to set up SSH into the private Muse VM. With a reverse SSH tunnel — where the destination machine initiates the connection, bypassing the firewall — an attacker may be able to execute more damaging commands. That hasn't happened yet, however.

Muse is currently available as an app for Android, iOS, and MacOS. Other platforms can access it in a browser with a Meta account.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Jake Roach](https://cdn.mos.cms.futurecdn.net/h6PRM8bTimCTnNfoAYfjAi.jpg)

Jake Roach is the Senior CPU Analyst at Tom’s Hardware, writing reviews, news, and features about the latest consumer and workstation processors.

* The LLM is most certainly only seeing its sandbox that it uses for commands and scratchpad. And whatever hypervisor its running on probably isn't devoting 8GB ram to each one until it's actually needed.Reply  
    
  Plus 2TB RAM isn't all*that* much, especially for a large corporation. That's a single 1U rack server worth.
