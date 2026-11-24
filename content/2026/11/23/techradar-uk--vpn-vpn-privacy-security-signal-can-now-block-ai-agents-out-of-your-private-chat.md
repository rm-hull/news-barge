---
title: Signal can now block AI agents out of your private chats — but not on your
  Mac
source_url: https://www.techradar.com/vpn/vpn-privacy-security/signal-can-now-block-ai-agents-out-of-your-private-chats-but-not-on-your-mac
source_site: TechRadar UK
source_slug: techradar-uk
description: While blocking in-app screenshots on iOS 27 and flagging AI screen reads
  on Android, macOS users still have to exclude Signal from Siri manually
image: https://cdn.mos.cms.futurecdn.net/mTkfstP2UnsXt7BdGA5vde-2560-80.jpg
published: '2026-11-23T00:00:00Z'
scraped_at: '2026-11-24T02:12:00Z'
categories:
- Technology & Software
people:
- Meredith Whittaker
- Siri AI
locations:
- Poland
organisations:
- Apple
- Gemini Intelligence
- Google
- Meta
- Microsoft Recall
- Muse AI
- No Trace
- Reuters
- Signal
- Siri AI
- TechRadar
- The Hacker News
---

![Signal logo on the AppStore displayed on a phone screen and Signal logo in the background are seen in this illustration photo taken in Poland on January 14, 2021. ](https://cdn.mos.cms.futurecdn.net/mTkfstP2UnsXt7BdGA5vde-1920-80.jpg)

* **Signal now blocks in-app screenshots by default on iOS 27**
* **On supported Android, screen security turns on if AI tries to read chats**
* **Mac users remain exposed to Siri AI, with Signal citing Apple's OS limits**

Signal is blocking AI assistants from snooping on your private messages on iPhone and Android, though Mac users are still left exposed.

In a November 20 blog post, Signal President Meredith Whittaker announced that the encrypted messaging app is restricting operating-system AI agents from capturing chats via screenshots. The targets include Apple's Onscreen Awareness with Siri AI in iOS 27 and Google's Gemini Intelligence on Android.

Even if you rely on end-to-end encryption and the best VPN to shield your internet traffic, neither tool stops an AI agent scanning text already decrypted on your display. Whittaker called these deep OS integrations "an existential threat to Signal, and our ability to responsibly uphold our mission."

The update arrives days after a Reuters investigation revealed that Meta's data-hungry Muse AI agent bypassed its official connector to read unlinked Signal chats. As The Hacker News reports, Muse abused Android push notifications and macOS screenshot and accessibility tools to pull message text.

## How Signal blocks AI agents, and what it cannot stop

> In order to protect your privacy in Signal from the latest agentic AI assistants on mobile operating systems, we are rolling out a new default to restrict screenshots in the Signal app. You can re-enable screenshots in your settings. [https://t.co/KHQF3bgaamNovember](https://t.co/KHQF3bgaamNovember) 20, 2026

Once an AI assistant grabs what is on your screen, Signal loses control. As Whittaker warned in her blog post: "All of this is outside of Signal's control once the data has been captured, and imperils the privacy of all the participants in a conversation."

On **iOS 27**(Signal 8.37 or later), Signal now blocks in-app screenshots by default through a new** Block Siri AI**setting. On** Android**(Signal 8.35.1 or later), Signal cannot reliably detect screenshot attempts across every vendor build, so it automatically turns on** Screen security** only when it detects an assistant trying to read the screen.

According to Signal Support, iPhone users can adjust or pause protection for 10 minutes under **Settings > Privacy > Block Siri AI**, while Android users manage it via** Settings > Privacy > App security > Screen security**. Signal cautions: "However, doing so will potentially expose your (and your contacts') Signal content to these AI agents, and break our privacy guarantees."

Does blocking screenshots actually keep AI out of your chats? Not completely.

Signal admits its fix cannot cover every Android build and "restricting screenshots does not address other more sneaky ways AI agents could potentially access application data, such as retrieving content already present on a user's device via the filesystem."

Signal made a similar trade-off last year when it blocked Microsoft Recall on Windows 11.

![Leave No Trace logo](https://cdn.mos.cms.futurecdn.net/Z7QHFc4GHoMhdps5XmntoC-1200-80.png)

**NEW**:** Leave No Trace** — A weekly newsletter on digital privacy and online surveillance.

Leave No Trace investigates the companies and governments putting our digital freedom at risk — and the people fighting back.

📩 Subscribe now to get every edition delivered to your inbox every Friday, launching this September.

## Why Mac users are still exposed to Siri AI

If you message on a Mac, Signal cannot protect you automatically.

In a footnote to her post, Whittaker wrote plainly: "We cannot reliably block screenshots on macOS."

Apple's operating-system architecture is to blame, Signal says, alongside missing developer documentation. While macOS offers protections against continuous screen recording, Signal notes those controls do not apply to single screenshots, and older APIs were deprecated in favor of tools that "only work for streaming media and other DRM-protected content."

TechRadar contacted Apple to comment on this, but we are still waiting for a response at the time of publication.

However, that echoes Whittaker's earlier warnings about AI agents breaching the boundary between apps and the operating system.

Signal is now urging Apple, Google, and Microsoft to give developers a documented way to opt apps out of AI data access altogether.

For now, Signal tells macOS 27 users to open **System Settings > Siri** and manually add Signal to**Excluded Apps**, while Apple previews more granular Mac data-access controls for apps that use AI agents.

Sign up for breaking news, reviews, opinion, top tech deals, and more.
