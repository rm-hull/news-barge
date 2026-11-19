---
title: Hackers steal over 1 million credit card details across 20 countries — attackers
  hit old Windows bug to infect over 700 point-of-sale terminals
source_url: https://www.techradar.com/pro/security/hackers-steal-over-1-million-credit-card-details-across-20-countries-attackers-hit-old-windows-bug-to-infect-over-700-point-of-sale-terminals
source_site: TechRadar UK
source_slug: techradar-uk
description: Most victims are located in Brazil
image: https://cdn.mos.cms.futurecdn.net/VYZ9EiBJ5dpuaFKr5CoP95-1920-80.jpg
published: '2026-11-19T00:00:00Z'
scraped_at: '2026-11-19T20:29:57Z'
categories:
- Technology & Software
people: []
locations:
- Brazil
- Russia
- United States
organisations:
- Bank Identification Numbers
- CERT
- CLFS
- Computer Emergency Response Team
- Cybernews
- PII
- TechRadar Pro
---

![Credit card](https://cdn.mos.cms.futurecdn.net/VYZ9EiBJ5dpuaFKr5CoP95-1920-80.jpg)

* **Researchers uncover a payment-card theft campaign that compromised 782 point-of-sale systems and exposed data from over one million cards**
* **Attackers used outdated Windows systems and malware to harvest card details, banking information, and transaction data**
* **Consumers across more than 20 countries face increased risks of fraud, account takeover, and targeted phishing attacks**

Someone stole details of more than a million credit and debit cards, potentially allowing them to make fraudulent purchases or account takeovers. Consumers in more than 20 countries around the world are now at risk, according to the researchers who discovered the theft.

Security researchers from *Cybernews* discovered an exposed server containing complete infrastructure used in a hacking attack against point-of-sale (POS) terminals - devices merchants use in stores to process card payments.

That infrastructure included the source code of the malware used in attacks, various exploitation tools, as well as a carding panel named “VINY JUNIOR TRILHAS” which stored exfiltrated payment card data.

## Card numbers and other details

The malware was used against POS terminals running different but outdated versions of Windows and Windows Server. It leveraged a bug tracked as CVE-2024-49138, a privilege elevation flaw in Windows Common Log File System (CLFS) driver that requires initial access before it can be abused. It was patched almost two years ago, which means the victims used a severely outdated and vulnerable endpoint for years.

In total, 782 systems were compromised, most of which were in Brazil (677). Other notable mentions include the United States with 22 endpoints, and Russia with 8.

Using the malware, the attacker installed an infostealer on the endpoints, and pulled data as it was running through, including Primary Account Numbers (PANs), validity periods, Bank Identification Numbers (BINs), issuing countries, issuing banks, exfiltration dates, and card types and brands.

The attacker also stole information about the compromised POS terminals, including the operating system versions and geographic locations (both country and city). On the server, the Cybernews team also found the attackers primarily targeted Brazilian banks.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The researchers said this was not a one-off smash-and-grab, but rather a prolonged campaign in which the POS terminals were relaying daily transactions. The exposed server was finally locked down on August 31 2026, while Cybernews reported it to the country’s Computer Emergency Response Team (CERT) on September 8.

“At least a million cardholders face potential financial fraud, including unauthorized purchases and account takeovers,” the researchers warned. “The risk depends on individual banks' fraud detection systems and cardholder protection policies.”

“Cardholders may experience financial damages depending on their issuing bank's fraud protection policies and how quickly fraudulent transactions are detected and reported.”

## Leveraging stolen data

Personally identifiable information (PII) gets stolen every day. Credit and debit card data - not so much. The latter is, obviously, infinitely more disruptive, since the victims can end up with their bank accounts entirely drained, but most banks have different limits and fraud protection policies which make it somewhat difficult for attackers to actually spend people’s money. Most transactions can also be traced, meaning the attackers are risking unveiling their identities in the process.

But there are things they can use the cards for - to buy bulletproof hosting services where they can host malware and other hacking tools; to purchase ads on reputable ad networks and promote malware or even ransomware; or to buy redeemable gift cards that are practically untraceable. Losing hundreds of thousands of dollars is not entirely off the table, but there are better chances crooks would make relatively smaller purchases instead.

They can also just sell the data on the dark web and let someone else worry about spending the money.

Finally, they can use the information about the credit cards to launch convincing phishing attacks and escalate the compromise even further. For example, they could “warn” a victim that their credit card is being used and urge them to immediately block it by clicking on a link in the email. That could result in ransomware deployment, from which the attackers could extort millions of dollars that are much harder to trace.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
