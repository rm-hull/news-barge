---
title: New AI phishing engine plugs into six chatbots to rewrite blocked scams
source_url: https://www.techradar.com/pro/security/while-attackers-use-ai-to-create-better-phishing-lures-todays-cybercrime-tools-do-much-more-experts-warn-themailer-ai-phishing-kit-runs-on-claude-and-chatgpt-and-constantly-evolves-until-it-gets-past-your-spam-filter
source_site: TechRadar UK
source_slug: techradar-uk
description: Self-hosted AI phishing toolkit tests scam emails against spam filters
  and automatically rewrites blocked messages until they land in your inbox
image: https://cdn.mos.cms.futurecdn.net/88Btws2w53ivfStaAhDZgR-1920-80.jpg
published: '2026-11-22T00:00:00Z'
scraped_at: '2026-11-23T01:37:11Z'
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Claude
locations: []
organisations:
- AI
- DMARC
- GMX
- Gmail
- Inbox Loop
- Letter Builder
- Microsoft
- Mistral
- SPF
- TechRadar Pro
- Telegram
- TheMailer
- Varonis Threat Labs
- Yandex
---

![Hacker](https://cdn.mos.cms.futurecdn.net/88Btws2w53ivfStaAhDZgR-1920-80.jpg)

* **TheMailer uses six AI models to generate increasingly convincing fraudulent emails**
* **A $6,000 phishing toolkit automates attacks against businesses and unsuspecting individuals**
* **Criminals can rewrite fraudulent emails repeatedly until spam filters accept them**

Artificial intelligence has made fraudulent emails more convincing, but cybercriminals are increasingly using automated platforms to manage entire phishing operations.

A newly identified tool called TheMailer combines commercial AI tools with automated email testing, personalization, and repeated content adjustments.

Its capabilities allow operators to modify fraudulent messages whenever security systems prevent their delivery to intended recipients.

## TheMailer combines commercial AI models with automated phishing operations

Researchers at Varonis Threat Labs identified TheMailer as a self-hosted platform that connects to several commercial AI services through operators' individual API credentials.

The software connects to AI services such as Claude, ChatGPT, Grok, Gemini, Mistral, and DeepSeek, allowing criminals to choose which service generates their messages.

The platform has appeared in advertisements on an underground cybercrime forum since March 2026, attracting more than 24,000 views.

Its advertised lifetime licenses reportedly cost between $3,000 and $6,000, depending on the purchased package and availability of additional AI capabilities.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Unlike conventional phishing software, TheMailer incorporates AI into several stages of campaign preparation, delivery, and subsequent communication.

Its Letter Builder generates HTML messages from brief instructions, while another feature transforms legitimate correspondence into templates for impersonating established businesses.

One particularly concerning capability is its Inbox Loop, which repeatedly evaluates whether test messages reach their intended destinations.

When a message enters a recipient's spam folder, artificial intelligence modifies its contents before another delivery attempt occurs.

The platform also includes an option described as “Remove AI patterns,” which attempts to eliminate characteristics associated with machine-generated writing.

Its operators can additionally specify a “professional banking tone” when requesting changes to particular messages.

## Automated customization makes conventional email detection more difficult

TheMailer also separates recipients according to their email providers, including Gmail, Microsoft, GMX, and Yandex, allowing operators to customize messages accordingly.

Its Autopilot module incorporates provider-specific filtering information and sending restrictions when preparing different versions of fraudulent communications.

One screenshot examined by Varonis showed a collection containing 145,133 email addresses, predominantly associated with Japanese businesses and universities.

The platform also includes account testing, automated exchanges between sending accounts, and tools for collecting and answering responses.

Its attachment generator introduces another dimension by creating personalized PDF documents, calendar invitations, and SVG files for individual recipients.

For example, an invoice attachment can receive a filename incorporating the recipient's name, making different copies appear individually prepared.

Additional features include concealed redirects, randomized message headers, proxy-supported delivery, and direct connections to recipient mail servers.

The platform reportedly advertises its services through Telegram, accepts cryptocurrency payments, and provides installation assistance to purchasers.

Varonis researchers also identified references to financial platforms, account security notifications, hotel booking communications, and German, French, and Russian-language email services.

These examples indicate that the software accommodates different impersonation scenarios rather than relying exclusively on financial institutions.

The changing nature of these campaigns creates difficulties for security systems that depend heavily on recognizing identical message templates.

Because individual recipients can receive separately generated versions, blocking previously identified wording becomes less dependable.

Organizations therefore need email authentication through SPF, DKIM, and DMARC, alongside monitoring for suspicious domains and concealed destination links.

Employee training must also address unexpected account warnings, urgent payment requests, and suspicious login instructions, regardless of how professionally messages are written.
