---
title: Watch out — Microsoft login pages are being abused as hackers try and lure
  in unlucky victims, here's what to look out for
source_url: https://www.techradar.com/pro/security/watch-out-microsoft-login-pages-are-being-abused-as-hackers-try-and-lure-in-unlucky-victims-heres-what-to-look-out-for
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-05T03:27:27Z'
published: '2026-08-04T00:00:00Z'
description: Attackers sent victims to a legitimate Microsoft login page and then
  asked them to approve app permissions.
image: https://cdn.mos.cms.futurecdn.net/AboNpeASJNf5nBHAARoLnF-1920-80.jpg
---

![A laptop with digitally inserted hack warnings around it](https://cdn.mos.cms.futurecdn.net/AboNpeASJNf5nBHAARoLnF.jpg) 

- **Phishing campaign used fake Teams notifications to route victims to a genuine Microsoft sign-in page**
- **Rather than stealing passwords, attackers asked victims to approve permissions for an attacker-controlled app, gaining access to mail, files, Teams, SharePoint, OneDrive and calendars without defeating MFA**
- **Check Point says the technique has been commoditized in 2026 into a rentable service; the practical defense is restricting app consent rather than relying on users to spot a fake**

A phishing campaign that ran from late June into July 2026 did something that breaks most of the advice organizations have spent a decade teaching their staff: it sent victims to a real Microsoft login page.

Check Point's email research team, which disclosed the campaign, identified more than 200 phishing emails targeting users across roughly 120 organizations worldwide.

The lure was a fake Microsoft Teams notification with a genuine destination; what actually compromised accounts was not a stolen password but a permissions prompt that the victim clicked through voluntarily.

## A sophisticated attack that relied on tricking users into granting permissions

Check Point noted in its brief that what actually compromised the accounts was not a stolen password but a permissions prompt that the victim clicked through voluntarily. This is a reminder of a stark change in attackers' tactics: they have stopped forging Microsoft's front door and started walking through it.

The email appeared to be a Microsoft Planner task-assignment notification. The sender name read "There's New Activity On Team," the subject line claimed that HR had sent three messages via Teams chat, and the body referenced a payroll and benefits update, along with a counter showing four overdue employee tasks.

To someone who works in security, the message had its own telltale signs of being a typical phishing attempt: every link in the email, including both call-to-action buttons, routed through the same redirect. And the visible sender address belonged to the recipient's own organization, meaning the email appeared to have been sent to the same person it came from.

The link opened a real OAuth authorization URL on login.microsoftonline.com, not a look-alike domain. Signing in displayed a permissions prompt asking the user to approve the permissions or accept them on behalf of their organization.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

If they did, Microsoft redirected the browser to the redirect address specified in the original request, which in this particular campaign was an AWS API Gateway endpoint under the attackers' control. The authorization code was delivered there, and the attackers exchanged it for access. No password was stolen at any point, and there was no fake page to spot.

This is not unlike how the phishing-as-a-service Kali365 platform compromises Microsoft accounts, but instead of stealing session cookies or OAuth tokens, it opts for a more permanent illicit grant of consent.

This runs counter to the usual security training checklist, which emphasizes adhering to norms rather than going against the grain; users are told to check the URL, look for the padlock, and watch for misspelled domains. None of those measures matter because there is nothing forged to catch. The domain and certificate are Microsoft's, while the sign-in page is the one the user sees every morning, offering a false sense of security to a user not looking for this particular attack vector.

Multi-factor authentication does not help either; it protects the login sequence but not access to the user's data post-login. The attacker never needs the password or the second factor because they walk away with a token granted by the user's valid session, a technique called 'consent phishing'.

There are many ways to prevent this, but the simplest two are asking users to check every single permission/consent screen they click (the phishing attempt still requires users to allow it) and limiting access to permissions for user accounts that applications can request via Microsoft Entra at the system administrator level.

It would be prudent to do the latter at a minimum, even as Check Point notes that the campaign is no longer active because the underlying technique it used is not going anywhere.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Rahim Amir](https://cdn.mos.cms.futurecdn.net/9xKZFBamtEZKSChRvywbPB.png)

Rahim Amir is a UAE-based tech writer who enjoys building PCs as much as he enjoys writing about them. He has been professionally writing about PC hardware since 2023, focusing on buyer’s guides, hardware reviews, and sponsored content and features related to tech.

Having built hundreds of gaming PCs and being an avid gamer in his spare time, Rahim tends to have stronger opinions about hardware than most. This is particularly on display when he gets his way with powerful, but minimalistic RGB builds even as Small Form Factor (SFF) PCs come a close second.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
