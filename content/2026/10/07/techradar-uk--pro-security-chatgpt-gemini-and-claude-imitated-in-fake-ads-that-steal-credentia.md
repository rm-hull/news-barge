---
title: ChatGPT, Gemini, and Claude imitated in fake ads that steal credentials and
  MFA codes
source_url: https://www.techradar.com/pro/security/chatgpt-gemini-and-claude-imitated-in-fake-ads-that-steal-credentials-and-mfa-codes
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-07T20:38:22Z'
published: '2026-10-07T00:00:00Z'
description: Cybercriminals are on the hunt for advertiser accounts
image: https://cdn.mos.cms.futurecdn.net/Ramk8kAMZnG58FVJidCvuF-800-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Claude
locations:
- Island
organisations:
- Artificial Intelligence
- ChatGPT
- Facebook
- GitHub
- Google Ads
- Google Gemini
- Island
- MCC
- MFA
- Manus
- Meta
- Muse
- Perplexity
- TechRadar Pro
---

![Fraude en ligne phishing](https://cdn.mos.cms.futurecdn.net/Ramk8kAMZnG58FVJidCvuF-800-80.jpg)

* **Fake AI marketing tools impersonate ChatGPT, Gemini, Claude, and others to steal business accounts**
* **Attackers use realistic browser-in-the-browser phishing and live operators to capture credentials**
* **Stolen advertising accounts provide access to payment methods, budgets, and linked client accounts**

Cybercriminals are offering fake AI-powered products for advertisers and marketing managers, in an attempt to steal their Google business accounts.

Most of today’s biggest AI names, including Chat-GPT, Google Gemini, Claude, Manus, and Muse, are being abused in this campaign, and people are still falling for it.

Security researchers Island have published a new report detailing how the campaign works. Apparently, the operators left the source code for earlier versions of their work open on a misconfigured public GitHub repository, giving the researchers unique insight into the operation and its success.

What researchers found was an advanced phishing platform that was used to target advertisers and marketing managers. It was used to create websites offering fake marketing-related products powered by Artificial Intelligence.

“Every brand gets its own pitch. ChatGPT promises a Monday Google Ads brief. Gemini promises MCC (manager account) and linked-client support. Claude gets its own advertising portal, Perplexity offers campaign planning and spend audits, and Manus offers a private Meta integration,” the researchers explained.

## All about connecting

Each site asked the victim to do the same thing - connect their Google account. After pressing “connect”, the platform launches a typical browser-in-the-browser (BitB) attack - it displays an entire browser, address bar and all, within the actual browser.

Therefore, victims not paying attention to the details might see a legitimate domain in their address bar, for example accounts.google.com. However, if they were to lift their gaze just a few inches higher, they would see the actual domain, which has nothing to do with Google, or OpenAI, or any other legitimate business.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The phishing kit is advanced, too. The fake browser adapts to whatever the visitor runs, so it won’t happen that a victim running macOS suddenly sees a Windows, well, window. Newer builds also come with nifty little details, like Safari’s URL pill, Chrome’s custom tabs, and even a dark mode.

As the victim tries to log in, a “human operator” (the scammer) on the other end follows them through the process. They see each submission, and decide what the victim sees next. They can fake a mistyped password error, or they can choose which MFA screen they see. The device gets fingerprinted, from IP and location, all the way down to screen size and WebGL.

The platform supports Google, Meta, TikTok, and Okta workflows, it was said.

## Targeting advertisers

At the end of the day, it’s all about money. Island says the crooks are deliberately going for business accounts because these are connected to credit cards, which they can later abuse.

“The lures are written for agency staff, media buyers, and manager-account administrators, because an advertising account is a spending account. It carries a stored payment method and an approved budget, and a manager account can reach several client accounts, each with its own billing profile and linked users.”

This is hardly new. Both Google and Facebook have their own advertising networks, displaying ads to billions of people every day. However, getting accounts, payment methods, and ads approved, is a stringent, painstaking process, which is why it’s a lot easier for crooks to simply use someone else’s account, especially if that someone already walked through Google’s fire barefoot.

Unfortunately, Island could not disrupt the operation or tear it down. At the moment of writing, the campaign was still ongoing, and the researchers saw “hundreds of victim submissions to the platform”.

The researchers are urging organizations to treat fictional AI integrations as account-access requests, inspect the outermost origin, correlate the client pattern, and hunt for the control vocabulary. Finally, they should use phishing-resistant authentication, and review advertising control changes.

“Origin-bound passkeys and hardware-backed authentication remove the reusable password and one-time-code material this platform is built to collect,” they said. “After exposure, check every client account the identity could reach for new managers or partners, changed recovery details, and campaigns or spend nobody approved.”

*Via* * The Hacker News*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
