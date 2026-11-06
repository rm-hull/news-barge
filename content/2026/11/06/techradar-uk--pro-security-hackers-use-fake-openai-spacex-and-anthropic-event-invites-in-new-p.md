---
title: Hackers use fake OpenAI, SpaceX, and Anthropic event invites in new phishing
  scam to steal Microsoft and Google accounts
source_url: https://www.techradar.com/pro/security/hackers-use-fake-openai-spacex-and-anthropic-event-invites-in-new-phishing-scam-to-steal-microsoft-and-google-accounts
source_site: TechRadar UK
source_slug: techradar-uk
description: No, you're not getting SpaceX shares
image: https://cdn.mos.cms.futurecdn.net/vg86aqqGf8Pqp6mnfQPGGf-1920-80.jpg
published: '2026-11-06T00:00:00Z'
scraped_at: '2026-11-06T23:06:16Z'
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Claude
- Cofense
- Kali365
- Push
locations:
- Kali365
organisations:
- AI
- ANY.RUN
- AWS
- GoTo Webinar
- Google
- Grok Heavy
- MFA
- Microsoft
- OpenAI Academy
- Push Security
- SpaceX
- TechRadar Pro
- URL
- VoidProxy Push
- Zapier
---

![Phishing](https://cdn.mos.cms.futurecdn.net/vg86aqqGf8Pqp6mnfQPGGf-1920-80.jpg)

* **AI-themed phishing campaigns found using fake OpenAI, Anthropic, and SpaceX events to steal corporate credentials**
* **Attackers combine device-code phishing, reverse proxies, and MFA bypass techniques targeting Microsoft and Google accounts**
* **Researchers warn employee interest in AI tools is increasingly being exploited as a high-success phishing lure**

If you suddenly get invited to an exclusive SpaceX event and even offered free access to Grok Heavy, kindly turn it down, as this is most likely part of a new phishing attack that’s been circulating around the web.

A report from security researchers Push Security found threat actors are using different AI-themed lures to get people to share their corporate login credentials.

As per Push’s report, threat actors were recently seen creating fraudulent websites for nonexistent events: an OpenAI Academy livestream, a private SpaceX briefing on AI marketing, an Anthropic presentation at AWS re:Invent, and similar.

People who landed on these pages were told they can get free goodies, as well: a free ChatGPT Pro subscription, access to Grok Heavy, and even shares of SpaceX. However, to claim these rewards, the victims were first told to log in - using either their Microsoft, or Google account.

And this is where the scam lies. Instead of actually logging in and getting the rewards, all victims would be doing is sharing their login credentials with the hackers.

"Employees want access to the latest AI tools, making them excellent bait for attacks," Push Security said in its analysis of the campaign.

## Kali365 and VoidProxy

Push says threat actors are using two phishing-as-a-service (PhaaS) platforms in this campaign, called Kali365 and VoidProxy. Depending which route they choose (Microsoft or Google), they get served a different path, both ending in credential exposure.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Those that choose to continue with their Microsoft credentials trigger an attack through Kali365. The victim receives a device code and instructions to enter it on Microsoft’s legitimate device login page. Once the victim signs in and approves the request, Microsoft issues an authentication token to the attacker’s Kali365 session. The fake event page then redirects the victim to a fake Microsoft sign-in page operated by VoidProxy, which captures additional credentials and session cookies.

Those that choose “Continue with Google” trigger a different technique. Here, the victim is shown a reverse-proxied version of Google’s legitimate sign-in page, operated by VoidProxy. The proxy relays the authentication process while capturing the victim's password, MFA response, and session cookie, which allows the attackers to grab an authenticated session without needing to move past MFA.

Push doesn’t know exactly how the links are distributed. It’s safe to assume they’re being moved through phishing emails, social channels, or Telegram groups. What we do know is that the attackers are using Google and Zapier to shorten the links and redirect the visitors, in order to avoid being detected by security scanners and URL reputation systems.

## Abusing the trends

"All of these detection evasion techniques, plus the MFA-bypassing AiTM and device code phishing payloads, mean this attack is designed to get around or through the controls that most organizations rely on to stop phishing attacks today," Push said.

It’s now been five years since the first version of ChatGPT was released, and since then the tool has captivated people from all walks of life, and was successfully used in countless phishing campaigns. In the past we’ve reported on campaigns involving Claude installation pages promoted through search advertisements, as well as malicious links disguised as legitimate AI content (shared conversations, downloadable artifacts, and custom GPTs).

In July 2026, ANY.RUN reported fake event invitations impersonating Meta, OpenAI, and Anthropic, hosted on legitimate Zoom event pages. More recently, Cofense observed a campaign revolving around fake Anthropic invitations distributed through GoTo Webinar.

As these tools get better, and as they penetrate deeper into every aspect of our private and business lives, they will be abused by threat actors more and more.

*Via* * BleepingComputer*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
