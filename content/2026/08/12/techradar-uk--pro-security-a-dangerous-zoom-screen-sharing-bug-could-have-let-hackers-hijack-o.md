---
title: A dangerous Zoom screen-sharing bug could have let hackers hijack other devices
  on a call
source_url: https://www.techradar.com/pro/security/a-dangerous-zoom-screen-sharing-bug-could-have-let-hackers-hijack-other-devices-on-a-call
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-12T13:38:56Z'
published: '2026-08-12T00:00:00Z'
description: Patch Zoom now or possibly pay a big price
image: https://cdn.mos.cms.futurecdn.net/q7LJWDP3HaKLzyUesaBUh7-1920-80.jpg
---

![The Zoom app running in macOS.](https://cdn.mos.cms.futurecdn.net/q7LJWDP3HaKLzyUesaBUh7.jpg) 

- **AI‑found Zoom flaws enabled device takeover through malicious annotation messages**
- **Exploits worked across all platforms and required only joining a video call**
- **Researchers warn AI now enables rapid, nation‑state‑level exploit development**

Experts have warned that Zoom, one of the most popular collaboration tools in the world, carried multiple vulnerabilities that allowed malicious actors to take over people’s devices, entirely.

What makes these vulnerabilities particularly dangerous is that the victims need not do much to be compromised - participating in a video call with the attacker is enough.

The bugs were said to be present in every version of Zoom, on every device and operating system - Windows, Mac, iPhone, Android, and Linux, in all versions up to and including 7.0.5 - with patches available now, so be sure to update immediately.

## AI-powered security

The flaws were discovered by security researchers A Security, which focuses on “autonomous offensive security”, using AI agents to simulate real-work attacks, identify vulnerabilities, and chain them into exploitable attack paths.

The company “simply” used publicly available frontier models and within 24 hours and fewer than 20 prompts, went from finding the flaws to building a working exploit.

The flaws are described as memory corruption bugs exploiting Zoom’s annotation feature. That feature, built on a proprietary protocol (meaning it has no public documentation or specifications, as opposed to being open source), meant that the Zoom client parsed everything it received, including specially crafted, malicious messages.

During the call, a malicious actor could send a message to each visitor that would corrupt their device’s memory and execute weaponized code, all without the victim knowing, being prompted to do anything, or clicking anything at all.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The vulnerability can be exploited regardless of if the attacker hosted, or simply joined, a call. All participants, regardless of their status in the call, were equally at risk. There were no visual cues indicating the compromise whatsoever.

Once the threat actor runs the malware on the victim’s device, they can do all sorts of things, from stealing sensitive files, to switching on the device’s camera or microphone. They can also deploy stage-two malware, steal login credentials and crypto wallet information, access the inbox, and more.

A Security responsibly disclosed their findings to Zoom, who labeled the vulnerabilities as CVE-2026-53413, CVE-2026-53414, and CVE-2026-53415, and all given a severity score of 9.0/10 (critical).

Furthermore, all Zoom Workplace clients on all supported platforms before version 7.1.5 and 7.0.6 using end-to-end encryption settings are considered vulnerable. A Security recommends updating the client to the latest version.

## Lowering the barrier

In its writeup, A Security stressed the simplicity and ease with which it managed to find the bugs and develop the exploits. It warned that AI has dramatically lowered the barrier for entry, and argued that in the pre-AI era, exploits like these were “reserved” for nation-state threat actors with virtually limitless resources:

“This class of capability would previously have only been available to nation-state threat actors, but the model requiring elite teams, months of effort, and weapons-grade budgets has collapsed,” the researchers warned. “Today, a single researcher was able to develop a nation-state-level exploit in less than a day.”

To add insult to injury, these flaws were found using “publicly available frontier models” such as GPT-5.6 Sol, Claude Opus 5, and the likes. Besides the frontier models, these companies also have dedicated cybersecurity programs where they offer specialized models with fewer guardrails and more flexibility for both offensive and defensive actions.

Earlier this week, OpenAI said that its Daybreak project now offers GPT-5.6-Cyber, a model built on GPT‑5.6 Sol and trained to improve capabilities on several specialized cybersecurity tasks such as finding zero-day vulnerabilities and developing exploit chains.

Daybreak came as a direct response to Anthropic’s Project Glasswing. This is an offering that came with Mythos Preview, an AI model that proved unusually capable at cybersecurity tasks. Allegedly, Mythos can autonomously identify and exploit zero-day flaws across major operating systems and browsers, as well as develop complex exploit chains. Because of those capabilities, Anthropic did not release Mythos Preview broadly. Instead, it made the model available to a limited group of organizations.

While some expressed their skepticism over Mythos, saying Anthropic is engaging in __fear-based marketing__, others have backed the company, saying Mythos proved exceptionally useful at identifying and fixing flaws. Microsoft, for example, is one of the original Project Glasswing partners, and ever since it started using it, the number of flaws patched through its Patch Tuesday cumulative update __quadrupled__.

Mozilla is also among those showering Mythos with praise, saying earlier this year that it is “__every bit as capable__” as the world’s best security researchers.

If A Security managed to find such dangerous flaws with publicly available models, there’s no telling what these dedicated models can do.

*Via**The Hacker News*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
