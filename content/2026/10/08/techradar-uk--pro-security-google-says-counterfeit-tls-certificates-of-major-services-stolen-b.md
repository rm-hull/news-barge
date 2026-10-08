---
title: Google says counterfeit TLS certificates of major services stolen by hackers
source_url: https://www.techradar.com/pro/security/google-says-counterfeit-tls-certificates-of-major-services-stolen-by-hackers
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-08T18:50:24Z'
published: '2026-10-08T00:00:00Z'
description: Three country-code top-level domains were hijacked
image: https://cdn.mos.cms.futurecdn.net/HU8VZ2jkrVAHBpb3Aqqg8j-1920-80.jpg
categories:
- Technology & Software
people: []
locations:
- American Samoa
- DigiNotar
- Ghana
- Sierra Leone
organisations:
- ACME
- CAA
- CAs
- CRLSets
- Certification Authorities
- Comodo
- Cybercriminals
- Dutch Certificate Authority
- Google
- Microsoft
- Mozilla
- Skype
- Symantec
- TechRadar Pro
- Thawte-branded Certificate Authority
- Yahoo
---

![Female hands typing on a laptop in neon light. A lock as a symbol of cybersecurity on a foreground.](https://cdn.mos.cms.futurecdn.net/HU8VZ2jkrVAHBpb3Aqqg8j-1920-80.jpg)

* **Attackers hijacked three country-code domains to obtain fraudulent HTTPS certificates for major websites**
* **Fake certificates could enable convincing traffic interception and phishing against affected domains**
* **Google revoked the certificates, protected Chrome users, and warned impacted organizations**

Cybercriminals recently managed to hijack three country-code top-level domains (ccTLDs) and used the access to generate HTTPS certificates covering several Google domains, as well as those belonging to other organizations. Google said the attack placed thousands of websites at risk, but stressed that the certificates have since been revoked.

According to Google, the domains that were hijacked are .gh (Ghana), .sl (Sierra Leone), and .as (American Samoa). During the attacks, the threat actors modified authoritative DNS records, obtaining HTTPS certificates covering not just Google, but other organizations, too.

In other words, any website operating on these domains was at risk, as well as all of the visitors. By manipulating authoritative DNS records, threat actors could redirect traffic away from legitimate websites and towards malicious ones under their control, all the while telling users they were visiting the legitimate one by showing the padlock icon. Visitors entering login credentials, payment information, or other data, would easily lose them to the attackers, and depending on the circumstances, they could also end up installing malware.

“Due to the nature of the attacks, we have no reason to believe the Certification Authorities (CAs) that issued the impacted certificates did anything wrong,” Google said.

## Affecting major brands

Although Google blocked the unauthorized certificates in Chrome and worked to have them revoked, it warned that its interventions might not have identified every affected domain or protected users of other browsers.

“As part of our usual incident response process, we immediately acted to protect users by blocking the use of unauthorized certificates for Google properties in Chrome via CRLSets,” Google added. “We also worked with the issuing CAs to ensure the certificates were revoked to protect users in clients other than Chrome.”

The risk for websites wasn’t theoretical. Google said “several leading global brands and widely used online services” were impacted by these attacks, and stressed that all of the certificates used in these attacks were blocked.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

“Where possible, we reached out to impacted organizations to alert them to our findings and actions,” Google concluded. The company did not say which of its own domains were affected, and did not want to name the victim companies. We also don’t know how many organizations were impacted.

Chrome users don’t need to take any action to be protected, it was said, but domain owners do have a thing or two to do. That includes performing ongoing monitoring of Certificate Transparency for all of the domains, and publishing restrictive CAA records with ACME account bindings.

## Not the first rodeo

Attacks like this have happened before - in 2011, cybercriminals compromised Dutch Certificate Authority DigiNotar, generating 531 fraudulent certificates for domains belonging to Google, Microsoft, Mozilla, Skype, and more. Some of these certificates were allegedly used to intercept encrypted communications of Iranian internet users, and the incident ultimately forced major browser vendors to withdraw their trust in DigiNotar, putting the company out of business.

Earlier that year, threat actors stole an account belonging to a registration authority partnered with Comodo, obtaining nine fraudulent certificates for domains operated by Google, Yahoo, Microsoft, and others. Something similar happened in 2015, when Google discovered that Symantec's Thawte-branded Certificate Authority had improperly issued an unauthorized certificate during internal testing, covering Google's domains.

This incident, however, was more of an internal failure and less of an attack. Subsequent investigations uncovered numerous additional misissued certificates.

“In parallel with domain-owner defenses, we will continue to work alongside the broader community to limit the impact of transient routing and DNS compromises on the safety of the web,” Google concluded. “To keep our users safe, we are committed to long-term HTTPS ecosystem improvements, such as reducing certificate validity and DCV reuse, through the Chrome Root Program and the new Chrome Quantum-resistant Root Program.”

*Via* * Ars Technica*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
