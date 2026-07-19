---
title: Claude’s AI assistant could be manipulated through browser extensions
source_url: https://www.techradar.com/pro/the-bypass-is-still-six-lines-of-javascript-security-experts-warn-that-claude-for-chrome-browser-extension-could-be-hijacked-despite-it-alerting-anthropic-several-times-that-something-was-wrong
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-19T21:04:11Z'
published: '2026-07-19T00:00:00Z'
description: A tiny JavaScript bypass reportedly lets attackers push Claude into workflows
  involving Gmail, calendars, and sensitive user data
image: https://cdn.mos.cms.futurecdn.net/hkechUkk5KHAbcMTCNVxG4-1920-80.png
---

![Claude Chrome](https://cdn.mos.cms.futurecdn.net/hkechUkk5KHAbcMTCNVxG4.png) 

- **Anthropic’s Claude extension flaws allow fake clicks to launch sensitive AI workflows**
- **Researchers found vulnerable handlers unchanged across eight extension updates**
- **Synthetic clicks bypassed checks designed to confirm real user actions**

Security researchers at Manifold Security have claimed Anthropic's Claude for Chrome browser extension contains two unpatched vulnerabilities in version 1.0.80, released July 7, 2026.

According to Manifold Security, it first reported both vulnerabilities to Anthropic through the company's bug bounty program on May 21, 2026, and received acknowledgment the following day.

The first flaw lets any browser extension trigger nine predefined Claude workflows by simulating a synthetic user click on claude.ai.

## Nine workflows and one missing check

Researcher Ax Sharma found that the extension never verified whether a click event carried the Event.isTrusted property before acting on it.

Under default settings, the vulnerability received a CVSS score of 7.7 High, increasing to 9.6 Critical when users enabled automatic execution because Claude could perform actions without approval.

The nine hardcoded tasks include reading Gmail, opening Google Docs, checking Google Calendar, and modifying Salesforce leads without asking.

Because the browser marks synthetic clicks as untrusted, the extension should have rejected them but instead executed the workflow anyway.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Manifold Security confirmed on July 7 2026 that both vulnerabilities still work against version 1.0.80, months after first reporting them to Anthropic.

Anthropic released eight separate versions between 1.0.73 and 1.0.80 without altering the specific handlers’ researchers had already flagged as vulnerable.

The company closed the synthetic-click report, saying an existing internal report already tracked the broader trust-boundary issue researchers had described in detail.

However, Sharma believes the fix required only one additional line of code to verify the click event's isTrusted property before allowing the workflow to continue.

## A second, structural weakness

A second flaw involves a side-panel URL parameter called skipPermissions, which can activate a privileged mode without any consent prompt.

When the parameter is set to true, the panel begins skipping permission checks entirely, allowing Claude to act without asking the user first.

Manifold notes that only Anthropic's own scheduled-task feature is supposed to construct this kind of privileged URL internally right now.

The panel, however, honours that parameter regardless of which script or page actually constructed the originating URL string in practice.

One example task lets Claude read a user's Gmail inbox, identify promotional messages, and automatically click the unsubscribe links inside them.

Manifold warns that "the bypass is still six lines of JavaScript," months after researchers first flagged the underlying issue to Anthropic.

Anthropic classified this second finding as informational, arguing that the parameter is only ever constructed by its own internal systems.

Manifold said the content-script and side-panel code linked to both vulnerabilities remained byte-identical across the eight subsequent extension releases examined after the original report.

The flaws were also reproduced across Claude's Opus, Sonnet, and Fable side-panel model selections, indicating that the issue affected the extension's security design rather than the underlying artificial intelligence models.

The report also connected the findings with OWASP concerns involving LLM01: Prompt Injection and LLM06: Excessive Agency risks in AI applications.

The researchers noted that abuse involving AI tools may remain difficult to detect because normal browser activity and network connections can appear unchanged while unauthorized AI actions occur.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Efosa Udinmwen](https://cdn.mos.cms.futurecdn.net/nwRLdPUNG4rWu4Y6nthHDV.png)

Efosa has been writing about technology for over 7 years, initially driven by curiosity but now fueled by a strong passion for the field. He holds both a Master's and a PhD in sciences, which provided him with a solid foundation in analytical thinking.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
