---
title: Google exec runs Windows 11 on a $1,999 iPhone Duo with Gemini 4 Carbon, but
  it might not be the easiest way to go about it
source_url: https://www.techradar.com/pro/google-exec-runs-windows-11-on-a-usd1-999-iphone-duo-with-gemini-4-carbon-but-it-might-not-be-the-easiest-way-to-go-about-it
source_site: TechRadar UK
source_slug: techradar-uk
description: Windows 11 now runs on Apple's foldable iPhone Duo
image: https://cdn.mos.cms.futurecdn.net/8fSZ5osisap2bjsFpu5UkE-2190-80.jpg
published: '2026-11-17T00:00:00Z'
scraped_at: '2026-11-18T00:56:53Z'
categories:
- Technology & Software
people:
- Ammaar Reshi
- Varun Mohan
locations: []
organisations:
- ARM64
- Anthropic
- Antigravity
- App Store
- Apple
- Argon
- Carbon
- EDK2
- Gemini
- Google AI Studio
- JIT
- Mac
- Microsoft Edge
- NTDEV
- OpenAI
- Red Hat
- Reshi
- StikDebug
- TXM
- TechRadar Pro
- Tiny11
- Trusted Execution Monitor
- UEFI
- UTM SE
- Windows Latest
- WindowsiOS
- iPhone
---

![Gemini](https://cdn.mos.cms.futurecdn.net/8fSZ5osisap2bjsFpu5UkE-1920-80.jpg)

* **A Google AI Studio product lead got retail Windows 11 ARM64 running locally on a non-jailbroken iPhone Duo using Gemini 4 Carbon**
* **The demo landed one day after Google broadly launched Carbon and its swarm agent feature**
* **The approach needs a Mac, your own Windows image, and a debugger at launch, and a future iOS update could break it**

Apple's first foldable phone has been on sale for less than a month, and someone has already turned it into a tiny Windows laptop.

Ammaar Reshi, who leads product and design for Google AI Studio, posted a video on X showing Windows 11 running on his iPhone Duo.

With the phone half-folded, the top screen shows the Windows desktop and the bottom half becomes a keyboard and trackpad; Unfold it and Windows fills the 7.6-inch inner display.

## An unfolded pocket PC with a public codebase

The code is public on GitHub as WindowsiOS, with 341 stars and 56 forks as of this writing. It is genuinely impressive systems engineering. One could also view it as a Google product lead showcasing a Google model and a Google coding tool, one day after that model became broadly available, built on open source work, with its own documentation called "foundational".

According to the project's README, WindowsiOS boots retail Windows 11 24H2 ARM64 (build 26100) on a non-jailbroken iPhone Duo running iOS 27, without Apple's Hypervisor framework, which the project says is off-limits to apps on stock iOS.

Instead, it uses a just-in-time binary translator that recompiles ARM64 guest code into ARM64 host code, paired with a software memory management unit. Around that sits an emulated PC-class platform: UEFI firmware, ACPI tables, an NVMe drive, USB 3.0, a VirtIO network adapter, and an Intel HD Audio controller built from scratch so Windows drivers bind without extra installs.

Windows Latest reports Reshi confirmed this is neither Remote Desktop nor cloud streaming, and the video shows Microsoft Edge and Google's own Antigravity IDE running inside Windows on the phone.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Windows on an iPhone is not new. In 2024, the Tiny11 developer NTDEV got a stripped-down Windows 11 booting on an iPhone 15 Pro through UTM SE, the PC emulator that Apple approved for the App Store after initially rejecting it.

The difference is that UTM SE has no JIT, so it interprets every guest instruction at runtime, adding a significant speed loss. On iOS 26 and 27 devices, Apple's Trusted Execution Monitor (TXM) tightly polices memory that is both writable and executable, which initially broke the JIT workarounds emulators relied on.

Community tools such as StikDebug now attach a debugger to pre-approve those memory regions, and WindowsiOS's launch script uses the same technique to enable faster boot time and operation.

The detail most coverage has seized on is development speed; when Varun Mohan, who leads Google's Antigravity team, replied, "This is breaking my brain!" and asked how long the agents had run, Reshi answered: "Agents cooked for 2 hours with Swarm!"

That refers to /swarm, a preview feature Google launched on November 10 alongside wider availability of Gemini 4 Carbon, describing it as "turning a single prompt into a coordinated team of agents." The approach is not unlike what current AI incumbents OpenAI and Anthropic offer via their own SDKs to coders.

For more context, Carbon is the second Gemini 4 model after Argon, aimed at long-horizon coding and cybersecurity, and /swarm runs inside Antigravity, Google's agent-first development platform. So the viral exchange, somewhat ironically, is two Googlers discussing a Google feature launched the previous day on a public forum.

The approach, though possible, is intended for a relatively narrow audience and could be patched quickly; Apple has historically been a reluctant observer when it comes to running 3rd-party OSes on its own platforms, even when restrictions are honored.

The documented process requires an Apple Silicon Mac with Xcode and a set of build tools, your own Windows 11 ARM64 image, EDK2 firmware and Red Hat's VirtIO network drivers, an offline provisioning step in WinPE, a roughly 12GB disk image, and a debugger attachment from the Mac at launch. It has been verified on a single device model, and there is no installable app package, meaning some manual tinkering is required.

*Windows Latest* found the project hard to dislike but judged it as "not a particularly practical idea," and it is hard to argue otherwise, frankly. The more telling story is how fast open-source iOS virtualization has moved in a single week: macOS on an iPhone on November 6, Windows on a foldable iPhone by November 11 2026.

AI agents clearly accelerated the second step, but they did not take the first, which it builds on, and the approach is anything but easy for the average user. Anyone who just wants Windows on an iPhone currently has an official option in Microsoft's Windows App, which streams a cloud PC rather than running one locally.
