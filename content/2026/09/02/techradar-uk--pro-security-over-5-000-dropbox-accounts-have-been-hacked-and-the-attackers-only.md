---
title: Over 5,000 Dropbox accounts have been hacked, and the attackers only needed
  an email address
source_url: https://www.techradar.com/pro/security/over-5-000-dropbox-accounts-have-been-hacked-and-the-attackers-only-needed-an-email-address
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-02T19:22:01Z'
published: '2026-09-02T00:00:00Z'
description: A bug in Lenovo's ID verification system made it possible to access Dropbox
  accounts
image: https://cdn.mos.cms.futurecdn.net/HXBM93dGYwGkVGnjAoWzpE-1920-80.jpg
---

![Dropbox logo is seen on a smartphone.](https://cdn.mos.cms.futurecdn.net/HXBM93dGYwGkVGnjAoWzpE.jpg) 

- **Hackers exploited Lenovo’s flawed email verification to hijack ~5,000 Dropbox accounts**
- **Attackers created Lenovo IDs with victims’ emails, bypassing login; 2FA absence worsened impact**
- **Dropbox ended Lenovo ID logins, expired sessions, and urged password changes plus 2FA setup**

Around 5,000 Dropbox user accounts were compromised when hackers found a vulnerability in the Lenovo ID verification process. What does a Lenovo flaw have to do with people’s Dropbox accounts, you might ask? Here is what happened:

Earlier this week, Dropbox started notifying affected individuals about the incident. In the data breach notification email, the company explains:

“Dropbox partners with Lenovo as an identity provider so that users can log in to their Dropbox accounts using verified Lenovo IDs. While you may not have an existing Lenovo ID, our investigation determined that an issue with Lenovo’s email verification process allowed an unauthorized party to register a Lenovo ID using your email address and then use that Lenovo ID to log into the Dropbox account associated with that email address.”

## Fixing the flaw

In other words, all criminals needed to have to pull this off was people’s email addresses. Using that information, they created Lenovo IDs and simply waltzed right into Dropbox accounts.

The attack took place between August 4 and 21, the company further said, adding that most of the accounts that were accessed did not have 2FA enabled. In around a third of them, there is evidence stored documents were either viewed or downloaded.

The vulnerability has since been addressed, and further steps taken to protect Dropbox users’ privacy. The company said it “promptly expired all sessions logged in through Lenovo IDs,” and terminated all links between Lenovo and Dropbox accounts. Now, it made it mandatory to submit a password when logging in through a Lenovo ID.

“No one can access your Dropbox account via a Lenovo ID without first entering your Dropbox password,” it said. Still, it urged users to change their passwords, enable two-step verification, and change the password for their email accounts.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

“Every single one of the compromised accounts lacked multi-factor authentication. In 2026, for cloud storage accounts holding data, that’s an indefensible gap and it’s one that users could have closed themselves regardless of what Lenovo or Dropbox did or didn’t do with their legacy integration," said Muhammad Yahya Patel, vCISO and cybersecurity advisor for EMEA at Huntress.

"The combination of an unreviewed third-party authentication pathway and accounts without MFA is essentially an open invitation. The practical lesson is straightforward and applies well beyond this specific incident. Every organisation and every individual should periodically audit what third-party services have authentication access to their accounts. OAuth grants, SSO connections, and third-party login integrations accumulate silently and rarely get removed when the relationship that created them ends.”

*Via**Cybernews*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
