---
title: OpenAI and Cisco team up to stop AI-generated security threats before they
  get too big
source_url: https://www.techradar.com/pro/security/openai-and-cisco-team-up-to-stop-ai-generated-security-threats-before-they-get-too-big
source_site: TechRadar UK
source_slug: techradar-uk
description: Shirudo is a new AI-powered open source runtime
image: https://cdn.mos.cms.futurecdn.net/RLLf9UfbiCMURufzgkPqr9-2560-80.webp
published: '2026-11-24T00:00:00Z'
scraped_at: '2026-11-24T21:55:23Z'
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Shirudo
locations: []
organisations:
- AI
- BPF
- Cisco
- Linux Plumbers Conference
- OpenAI
- Shirudo
- TPM
- TechRadar Pro
- VM
---

![Shirudo](https://cdn.mos.cms.futurecdn.net/RLLf9UfbiCMURufzgkPqr9-1920-80.webp)

* **OpenAI and Cisco released Shirudo, an open source tool that uses AI and eBPF to shield Linux systems from known vulnerabilities before patches are deployed**
* **The platform creates temporary protections that block exploit behavior while allowing legitimate workloads to continue running**
* **Developers say Shirudo can help reduce the risk from n-day vulnerabilities by providing automated, verifiable defenses during the patching window**

OpenAI and Cisco want to make n-day vulnerabilities on Linux a thing of the past with Shirudo (Japanese for ‘shield’) a new tool which is being open sourced so the wider cybersecurity community can inspect it and contribute if they want.

Security vulnerabilities generally fall into two broad categories: zero-day flaws, and n-day flaws. Zero-days are flaws unknown to the vendor and as such have no official patch or fix. They’re called “zero-day” because the vendors have had zero days to fix the issue before threat actors started exploiting it. Following the same logic, n-day flaws are those that are known to the vendor but have not yet been patched.

This puts software users in a tricky position: do they turn off vulnerable services to protect the wider infrastructure (and thus hurt their bottom line and their reputation), or do they keep the services running in anticipation of a patch, and risk being exposed and exploited? It is this security limbo that Cisco and OpenAI are trying to solve.

## How Shirudo works

“Testing and deploying a patch can still take days or weeks,” OpenAI said in an announcement. “Protecting a service in the meantime can be challenging because an exploit and a legitimate request may rely on the same Linux operation. Blocking that operation entirely could take the service offline.”

Shirudo, which is powered by AI apparently does just that - protects Linux systems while IT teams roll out patches. Teams can set up a temporary safeguard (called shield), and test to see if it blocks behavior that exposes a vulnerability, while allowing legitimate requests through. After approval, the shield gets deployed and the service can continue unabated.

OpenAI said Shirudo uses eBPF, a Linux technology that allows small programs to run at specific points inside the operating system. That way, users can monitor for suspicious activity and apply targeted protections to otherwise running systems. eBPF shields can block vulnerable code paths without restarting the system, and security teams can monitor how a proposed shield affects applications before even enforcing it.

OpenAI also said Shirudo was designed to give AI agents “programmable controls” to investigate vulnerabilities, build targeted shields, and validate their effectiveness against exploits and real workloads, while security teams get to control what gets deployed. All shields are cryptographically signed and verified through Linux’s eBPF verifier, while kernel security controls restrict unauthorized changes.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Finally, OpenAI said the verification is backed by hardware: “Shirudo uses a Trusted Platform Module (TPM) to support a verifiable record of protections being loaded or removed. Operators can use this evidence to check whether systems meet their security requirements.”

## How to get started with Shirudo

The two companies shared a technical walkthrough from the Linux Plumbers Conference, showing how to apply the shield and verify it on the target host. They also demonstrated how Shirudo helped protect a running Elasticsearch application against the Java4Shell vulnerability by adding an input check to Java's Base64 decoder, blocking malicious input without interrupting the service.

“Shirudo is a first step toward infrastructure that can adapt to emerging threats while remaining reliable,” OpenAI and Cisco said in the announcement post. “We want to strengthen the operating system foundations needed to deploy these protections at scale, including hardening the kernel and core services, limiting workload permissions, and making updates and recovery safer.”

Shirudo is an open-source tool, allowing developers, security researchers, and infrastructure operators to inspect the code, test it, and contribute at will. It is licensed under BSD 2-Clause, with its BPF programs dual-licensed under BSD and GPL.

Those interested in testing out Shirudo should follow the VM quickstart to sign, load, and verify a test protection.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
