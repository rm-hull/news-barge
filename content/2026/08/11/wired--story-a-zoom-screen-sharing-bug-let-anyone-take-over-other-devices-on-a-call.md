---
title: A Zoom Screen-Sharing Bug Let Anyone Take Over Other Devices on a Call
source_url: https://www.wired.com/story/a-zoom-screen-sharing-bug-let-anyone-take-over-other-devices-on-a-call/
source_site: Wired
source_slug: wired
scraped_at: '2026-08-11T13:13:24Z'
published: '2026-08-11T00:00:00Z'
description: Researchers say it took fewer than 20 prompts for a public AI tool to
  find a flaw (now fixed) allowing anyone on a Zoom call to hijack another participants’
  device.
image: https://media.wired.com/photos/6a7a45ba595802741eff3e7c/191:100/w_1280,c_limit/Security_Zoom%20Screensharing%20Bug_v1.jpg
---

As AI models gain advanced capabilities to find vulnerabilities in software, develop ways to exploit them, and even carry out autonomous hacking sprees, researchers offered a sobering new example on Tuesday, disclosing vulnerabilities in the video conferencing platform Zoom that could have been exploited to take over targets’ devices. Anyone on a call that involved screen sharing, whether participants or the host, would have been vulnerable to a silent attack that could be carried out with no indication and no interaction from the victim.

Researchers from the digital defense firm A Security say the bug was discovered in early June using publicly available AI models, and that it took fewer than 20 prompts to uncover the vulnerabilities and create a working attack. Zoom issued a security advisory on Tuesday, including details about fixes the company has already begun rolling out to address the flaws, which affected devices running all operating systems that Zoom supports—Windows, macOS, Linux, iOS, and Android.

“What is interesting for us and what we believe is dangerous is the democratization of these capabilities—the barrier to entry is dropping rapidly,” A Security cofounder Omer Gull told WIRED ahead of the disclosure. “Before it would have taken a team of five people maybe six months with a lot of refining and iteration to find this. Now people can reach the same results with under 20 prompts. And Zoom is an important type of target because people assume trust when using it. They don’t see it as a threat.”

The vulnerabilities were specifically in the protocol used to facilitate real-time annotation during screen sharing. The researchers say that their AI bug hunting systems specifically delved into this component because, like human bug hunters, they have been trained that convoluted and obscure functions often contain overlooked vulnerabilities. This is particularly true with proprietary, closed source software. An established company like Zoom presumably does extensive code review and vetting on all components and functions, but without the benefit of public, open review, esoteric yet complex features like annotation are more likely to contain mistakes.

Zoom did not respond to multiple requests for comment from WIRED about the A Security findings.

The bugs are now patched, with Zoom issuing both server and client-side fixes—or patches for both Zoom’s own servers and the applications that run on customer devices. But the researchers emphasize that it was alarming to contemplate bugs that could have been exploited to take over a target device simply by getting someone onto a Zoom call. Joining a call is in itself a gesture of trust, but given how ubiquitous video calling is in both personal and professional contexts—and given that Zoom in particular is also widely used for events and semi-public activities like webinars—people typically have their guard down when joining a Zoom.

“If you just get on a Zoom with us, we can take over your device,” A Security cofounder Yossi Torati told WIRED on a call. (It was, incidentally, hosted on Microsoft Teams.) “The worst case scenario is that we can take over an enterprise just by having this vulnerability in our hands. If I’m an attacker I can be on a call with someone from a company, take control of their computer and their credentials, and then use them to move laterally in the enterprise.”

Practitioners often call security a “cat and mouse game,” but as AI bug hunting proliferates, this delicate dance has become an all out race.
