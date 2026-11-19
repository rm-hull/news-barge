---
title: '''COLD RELIC remains an active threat'': Google warns Russian hackers are
  hitting public sector firms with sophisticated phishing and malware campaigns'
source_url: https://www.techradar.com/pro/security/cold-relic-remains-an-active-threat-google-warns-russian-hackers-are-hitting-public-sector-firms-with-sophisticated-phishing-and-malware-campaigns
source_site: TechRadar UK
source_slug: techradar-uk
description: There is more than one way to make use of stolen information
image: https://cdn.mos.cms.futurecdn.net/85kAnS2rcuxwyaibPRC4Ze-2000-80.jpg
published: '2026-11-19T00:00:00Z'
scraped_at: '2026-11-19T20:30:04Z'
categories:
- Technology & Software
- Business & Entrepreneurship
people: []
locations:
- Russia
- West
organisations:
- COLD RELIC
- COLDRIVER
- Callisto
- DoJ
- FBI
- FIDO2
- FSB
- Federal Security Service
- GTIG
- Google Titan
- Gossamer Bear
- MFA
- Mandiant
- Star Blizzard
- TechRadar Pro
- Threat Intelligence Group
- UNC4057
- US Department of Justice
---

![russian flag](https://cdn.mos.cms.futurecdn.net/85kAnS2rcuxwyaibPRC4Ze-1920-80.jpg)

* **Google says Russian-linked espionage group COLD RELIC uses stolen accounts and internal data to fuel follow-on phishing attacks**
* **Attackers harvest emails, contact lists, and organizational details to impersonate trusted contacts and compromise new targets**
* **Researchers recommend phishing-resistant MFA, session monitoring, and stronger cloud-access controls to disrupt the campaign**

Google has sounded the alarm on a Russian state-sponsored threat actor known as COLD RELIC, claiming it continues to target high-value individuals and organizations with sophisticated phishing and malware campaigns.

In its report, Google’s Threat Intelligence Group (GTIG) shared new details about the group’s espionage methods, and how it hops from one victim to another using stolen identities.

## COLD RELIC

Google said it saw COLD RELIC steal a single cloud account from one company, pull a significant amount of sensitive data from the victim’s environment, and then use it to launch a separate attack - against other firms connected to the original victim. The group is also called COLDRIVER, UNC4057, Star Blizzard, Callisto, and Gossamer Bear, Google says, stressing that the US Department of Justice (DoJ) placed it well within Russia’s Federal Security Service (FSB) - essentially Russia’s FBI.

The threat actor has been active for more than a decade, taking aim primarily at individuals and organizations with information of strategic or political interest to the Russian governments. Its victims include government officials, defense contractors, and non-government organizations (NGOs) in the West.

"The group is known for implementing sophisticated phishing and malware campaigns with the aim to gain access to information of strategic or political relevance to the Russian government," Google said.

The report focuses on COLD RELIC’s ability to use information stolen during one intrusion to make subsequent attacks more convincing. Instead of just grabbing sensitive data from a compromised company’s environment and calling it a day, the threat actors use stolen emails and identities to impersonate legitimate contacts and approach new targets.

Google detailed two intrusions that Mandiant investigated, both of which were against US-based organizations. The first one happened last year, when COLD RELIC stole the login credentials of a Super Admin and used them to waltz into an organization’s cloud productivity environment. The account had multi-factor authentication (MFA) enabled, so the attackers spammed the target with hundreds of approval requests until they just approved one to make the notifications stop.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

They then downloaded everything they found in the cloud storage, exported employee lists, and launched a domain-wide data export. They also deleted security investigation and email audit logs to cover their tracks.

## Bunny hopping to other targets

The information found there eventually helped them launch a separate attack against an entirely different US-based organization. A year later, they impersonated an employee of the previously compromised company, contacted a new victim, and shared phishing links designed to steal login credentials and authentication tokens for Microsoft Entra ID.

It worked, and the technique is now something COLD RELIC frequently uses in its attacks. "Once COLD RELIC compromises a target, it uses stolen emails and data to establish authentic pretexts and impersonate contacts when reaching out to subsequent targets," the report explains.

The threat actors collect organizational rosters, contact lists, resumes, and event schedules - pretty much anything that would help them build convincing pretexts for future phishing attacks. Google warns that COLD RELIC remains active, and that GTIG observed evidence of new phishing attacks earlier this month.

To defend against pesky Russian spies (and all other, for that matter), Google recommends organizations strengthen their authentication security and enforce phishing-resistant MFA (Hardware security keys such as Google Titan, FIDO2/WebAuthn authentication, and passkeys). It also advises organizations monitor suspicious passkey and device registrations, and revoke existing sessions and OAuth permissions when responding to suspected account compromises.

Finally, businesses should monitor logins coming from residential proxy networks, since this seems to be the stable of COLD RELIC attacks. Google said it will continue tracking and disrupting the group's infrastructure to protect cloud users.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
