---
title: Does a VPN protect your privacy when using ChatGPT or Claude?
source_url: https://www.techradar.com/vpn/vpn-privacy-security/does-a-vpn-protect-your-privacy-when-using-chatgpt-or-claude-what-network-encryption-can-and-cant-hide-from-ai
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-10T17:21:31Z'
published: '2026-10-10T00:00:00Z'
description: A VPN masks where you are – not what you share
image: https://cdn.mos.cms.futurecdn.net/zEFXeYTtHV8bCodc2TArfH-2560-80.jpg
categories:
- Technology & Software
people:
- Claude AI
locations: []
organisations:
- AI
- ISP
- LM Studio
- Lumo
- OpenAI
- Proton AG
- Proton Mail
- Proton VPN
---

![Claude AI](https://cdn.mos.cms.futurecdn.net/zEFXeYTtHV8bCodc2TArfH-1920-80.jpg)

A VPN is great at hiding where you are and what your internet provider sees. However, when you’re chatting with ChatGPT or Claude, your privacy depends on something far more complicated than a tunnel through the internet.

Even the best VPNs won’t stop AI companies from reading, storing, and learning from everything you type. In this article, we’ll unpack exactly what data these platforms see, why encryption has limits, and what you can actually do to protect yourself.

## What chatbots see (and what a VPN actually hides)

![A ChatGPT window on a laptop screen](https://cdn.mos.cms.futurecdn.net/xQyyeCX9ERbvTpYWrgMFL9-1200-80.jpg)

Without a VPN, OpenAI (ChatGPT) and Anthropic (Claude) can typically see a lot about your connection. Your IP address reveals your approximate geographic location. Device metadata follows alongside that, including your browser type, operating system, and unique device identifiers.

According to OpenAI’s privacy policy, the company collects your IP address; device information, including unique identifiers; cookie data; and your location, along with your email address and payment information.

Anthropic does the same. Their policy covers location, connection details, and device usage patterns, especially on the mobile app. Different wording, same result: both companies can see roughly where you are and what you’re using to talk to them.

A VPN helps with some of this. It successfully masks your real IP address from the AI platform and encrypts your traffic so your ISP can’t see that you’re using AI services. However, this is where the protection stops. Once your encrypted tunnel ends at the VPN server, the AI company still sees everything that arrives at their doorstep.

## The limits of encryption: What a VPN can’t hide

![VPN apps on iPhone](https://cdn.mos.cms.futurecdn.net/XNYgnsfepi2BJUWk9bhNSa-1200-80.jpg)

This is the critical part many people miss. A VPN protects your data while it travels across the internet, but that protection ends the moment your prompt arrives on OpenAI or Anthropic’s servers. Your message has to be decrypted for the AI to process it.

Once decrypted, your data sits on the AI company’s systems, governed by their policies rather than yours. A VPN does nothing to hide the content of your prompts, any files or images you upload, your account details and conversation history, or your payment information.

The encryption protects the connection between you and their servers, not what happens afterward. No matter how strong the VPN tunnel is, everything you type is fully readable on the other end.

## What AIs remember and how to actually stay private

Here’s where things get tricky. Most consumer chatbots keep your conversations on file indefinitely and may use them to train future models. You have to manually adjust settings and delete chats yourself if you want them gone.

For ChatGPT specifically, OpenAI may use your content to improve services unless you opt out. You can navigate to Settings > Data Controls, then toggle off the option to improve the model for everyone. However, even with this disabled, chats may still be stored for safety and legal reasons.

Claude works similarly. Anthropic requires all consumer users to choose whether their chats can be used for training, and the toggle is on by default. If enabled, data can be retained for up to five years, compared to 30 days if you decline.

You can disable the setting anytime in your account preferences or use Incognito mode to keep conversations out of your saved history. Paid business tiers come with stricter privacy agreements by default.

## The verdict and privacy-first alternatives

A VPN is a solid first step for network security in that it hides your location from AI providers and keeps your ISP from monitoring your activity. However, it won’t stop AI companies from reading, remembering, and learning from your prompts.

If privacy matters to you, adjust your settings by turning off data training in both ChatGPT and Claude, use ChatGPT’s temporary chats or Claude’s Incognito mode, and avoid sharing sensitive information.

For genuinely private AI interactions, consider Proton AG’s Lumo. Built by the team behind Proton Mail and Proton VPN, it uses zero-access encryption so only you can decrypt saved conversations, keeps no logs on their servers, and doesn’t train on your data unless you opt in. It runs on European infrastructure under GDPR and Swiss privacy laws.

One step further than this is to run open-source models offline with tools like Ollama or LM Studio, keeping everything local so nothing ever leaves your machine.
