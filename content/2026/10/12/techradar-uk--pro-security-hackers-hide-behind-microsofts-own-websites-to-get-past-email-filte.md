---
title: Hackers hide behind Microsoft's own websites to get past email filters and
  launch phishing campaigns
source_url: https://www.techradar.com/pro/security/hackers-hide-behind-microsofts-own-websites-to-get-past-email-filters-and-launch-phishing-campaigns
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-12T19:01:31Z'
published: '2026-10-12T00:00:00Z'
description: No, that's not a Power BI dashboard you're looking at
image: https://cdn.mos.cms.futurecdn.net/7DtE9RCVmUtmH2FAfvxsvM-2560-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Huntress
locations: []
organisations:
- ConnectWise
- Google
- Huntress
- IT
- Microsoft Power BI
- Power BI Power BI
- RMM
- ScreenConnect
- TechRadar Pro
---

![Malware attack virus alert , malicious software infection , cyber security awareness training to protect business](https://cdn.mos.cms.futurecdn.net/7DtE9RCVmUtmH2FAfvxsvM-1920-80.jpg)

* **Attackers abused Microsoft Power BI dashboards to lure victims into downloading ScreenConnect software**
* **Public dashboards mimicked blurred documents and redirected users to attacker-controlled sites**
* **Campaign established persistent remote access, potentially enabling ransomware, espionage, or data theft**

Microsoft's Power BI has seemingly become the latest in an ever-growing line of legitimate software being abused in phishing attacks.

Security researchers Huntress said they uncovered a new campaign that leverages publicly accessible Power BI dashboards to trick people into downloading remote monitoring and management software (RMM) called ScreenConnect. The end game of the campaign is not known at this time.

## Power BI

Power BI is Microsoft’s business intelligence and data visualization platform, allowing users to create charts, reports, and various dashboards, out of their data and other raw information. The tool itself can collect data from sources such as spreadsheets, databases, cloud services, and more, and users can publish reports and dashboards online, or share them with colleagues privately.

In this campaign, which started on or around September 10 2026, the threat actors created a public dashboard, likely using a throwaway Microsoft account (or a compromised one). Huntress does not confirm how that account was obtained, but says that the dashboard was designed to look like a blurred document with a button labeled “Download Reference”.

The blurred document trick is rather common in phishing emails. Other services such as DocuSign, Dropbox, and even Office 365, were being abused in the same way. To “unblur” (or unlock) the document, victims are told to click a link and follow along.

Sometimes they were asked to download a “premium” version of a document reader, or an “updated” one, and sometimes they were asked to log in using their Office or Google credentials. This attack is no different - clicking on the “Download Reference” button redirects the victim to an attacker-controlled website outside Microsoft’s infrastructure, where an automatic download of ScreenConnect is launched.

On its own, ScreenConnect is not malicious. It is a legitimate remote access and support tool developed by ConnectWise, and designed to help IT staff manage devices remotely. Through the product, users can connect other devices on the internet, troubleshoot problems, transfer files, and install software. Once installed and connected to an attacker-controlled endpoint, ScreenConnect can provide persistent remote access.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## Establishing persistence

The researchers didn’t discuss how the emails were delivered, but since they contained a link to a legitimate Microsoft service, they most likely evaded at least some email filters and landed in people’s inboxes. After all, this is probably why Power BI was used in the first place (aside from the fact that it’s not commonly abused this way).

But what’s particularly interesting about this attack is that after deploying one ScreenConnect instance, the attackers deployed a second one and configured a scheduled task to repeatedly execute a PowerShell script. In at least one incident, they also deleted the first instance.

Why they did it remains a mystery. An educated guess would be that they were trying to establish reliable, persistent remote access, while at the same time making sure their activities were harder to detect and disrupt. If defenders were to discover and remove one malicious ScreenConnect installation, a second one might remain available.

This is all in the domain of speculation, unfortunately, since Huntress stopped the observed attack before it progressed beyond establishing remote access. Therefore, we don’t know if the goal was to steal data, deploy ransomware, or engage in financial fraud. What we do know is that with two ScreenConnects, they were able to establish a durable foothold inside corporate networks, which they could subsequently leverage for espionage, data theft, ransomware, or other financially motivated attacks.

As a general rule of thumb, the best way to defend against these types of attacks is to be highly skeptical of incoming emails, especially those with links to “locked” documents, and even more so those that end up with a ScreenConnect deployment.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
