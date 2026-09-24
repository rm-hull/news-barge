---
title: Google’s PQC roadmap puts traditional digital certificates under pressure
source_url: https://www.techradar.com/pro/googles-pqc-roadmap-puts-traditional-digital-certificates-under-pressure
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-22T13:23:30Z'
published: '2026-09-22T00:00:00Z'
description: Google's post-quantum cryptography migration deadline move raises concerns
categories:
- Technology & Software
- Business & Entrepreneurship
image: https://cdn.mos.cms.futurecdn.net/pVCXKrhThqmUjYVSZBjV5Z-2560-80.jpg
locations:
- Merkle
people:
- Jason Soroko
organisations:
- Apple
- CA
- CAs
- Chrome
- Cloudflare
- Future plc
- Geomys
- Google Trust Services
- Google's
- IETF
- Let's Encrypt
- MTC
- MTCs Google
- Merkle Tree Certificate
- Merkle Tree Certificates
- NIST
- NSA
- PKI
- PQC
- SVP of Product
- Sectigo
- TechRadar Pro
- TechRadarPro
---

![Hands on a laptop with overlaid logos representing network security](https://cdn.mos.cms.futurecdn.net/pVCXKrhThqmUjYVSZBjV5Z.jpg)
![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png)

In March, Google moved its own post-quantum cryptography (PQC) migration deadline forward to 2029, a full six years ahead of NIST's guidance, and two ahead of the NSA's requirement for national security systems. It was a terrific bit of security signaling, but now it is backed up by a new product-by-product roadmap organized around three risk domains, with milestones attached to named services.

Jason Soroko is the SVP of Product at Sectigo.

For anyone whose job touches digital trust, the most significant of those three domains is Google’s attempt at enhancing foundational capabilities for cryptographic agility: building flexible systems that can adopt new cryptographic standards with minimal engineering effort as those standards evolve.

The message is that organizations should prepare for a future in which standards, certificate formats, and operational requirements continue to evolve, and evolve regularly, requiring cryptographic agility.

## Why quantum risk is already a digital trust problem

Adversaries are already harvesting and storing encrypted data today on the assumption that a future quantum computer will decrypt it (harvest now, decrypt later). Anything with a long confidentiality tail, from health records to national archives to intellectual property, is already exposed to a machine that does not yet exist.

Quantum-resistant algorithms, like ML-DSA, solve the cryptographic problem, but they introduce much larger keys and signatures. Deployed through today's public key infrastructure (PKI), they would inflate or possibly break the systems behind secure connections. Legacy systems and high-latency networks would feel it most.

## What is a Merkle Tree Certificate (MTC)?

At the time this article is being written, the most significant development in Google's roadmap may be the easiest to miss. Under Domain 2, Integrity and non-repudiation, a single line reads:

“Google Trust Services, Merkle Tree Certificates, 2028”.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Merkle Tree Certificates (MTCs) are a new kind of website domain certificate designed to keep secure connections fast in the coming era of quantum computers. Today a website proves its identity by presenting a certificate that carries several digital signatures, and the quantum-resistant versions of those signatures are so bulky they would slow down every secure connection on the internet.

MTCs solves this by having the certificate authority (CA) record everything it issues in a public, tamper-evident log, organized as a Merkle tree. Rather than carrying heavy signatures, the website presents a short trail of digital fingerprints showing its certificate sits in that log, and the browser checks the trail against a summary of the log it already received through its normal software updates.

Of note, MTCs do not abandon X.509. They are X.509 certificates, carrying a proof where a signature used to sit, issued alongside conventional directly-signed certificates rather than replacing them.

The result is a certificate that stays small, stands up to quantum computers, and is publicly verifiable by default. For the regular everyday person: we get to keep using the internet fast and uninterrupted with quantum resistance underneath.

## MTCs make transparency structural

In today's web PKI, transparency is bolted onto issuance as a separate step. The CA signs a certificate, submits it to independent CT logs, and collects SCTs, each of which is a log's signed promise to publish the certificate within a fixed window. A misbehaving or compromised log can vouch for a certificate that never becomes visible to the monitors watching for misissuance.

MTCs change that relationship. The CA certifies by logging, and a certificate is literally a proof that its entry appears in the CA's public issuance log, verified by the browser on every connection. If it is not in the log, it is not a certificate. Under MTC, transparency does not merely survive the post-quantum transition. It comes out stronger.

## Who is developing Merkle Tree Certificates

When the vendor with the dominant browser share proposes a new certificate format and a new root store to hold it, it is reasonable to ask whether the rest of the ecosystem is being consulted or simply informed.

However, MTCs are not Google's alone. At the time of writing, the IETF draft's authors span Google, Apple, Cloudflare, and Geomys. Cloudflare has been involved from the outset, CAs including Sectigo have contributed to the underlying research, and Let's Encrypt publicly committed to MTCs in June 2026. The result will be an open standard any CA can implement, controlled by no single vendor.

The organizations that will shape post-quantum web trust are the ones in the working group now. Root programs, CAs, and large implementers who stay outside it will inherit decisions rather than influence them. That choice is available to everyone, and the window is open today.

## How organizations should prepare for MTCs

Google’s 2028 date for MTCs deserves a roadmap's usual caveats. Google ties it to standardization work still in progress at the IETF, and dates like these move. The direction, however, resembles something that seems settled.

Chrome's planned Quantum-resistant Root Store will support quantum-resistant certificates only in the MTC format, not as post-quantum signatures bolted into traditional X.509. Compact classical signatures and X.509 served the web extraordinarily well for three decades, but with the dawn of quantum computing, we are due for a redesign.

For everyone else, the practical implication of Google's roadmap is not that you need MTCs. It is that you need to be capable of adopting them (or whatever else emerges) without a multi-year engineering program. Which is precisely the cryptographic agility Google put at the foundation of its own plan.

In concrete terms, organizations should focus on:

* A complete inventory of certificates and cryptographic assets, because you cannot migrate what you cannot see
* Automated certificate lifecycle management, because shorter certificate lifetimes will make manual processes untenable well before quantum computers arrive
* A written post-quantum roadmap from your CA, which every organization should be asking for

The full scope of what MTCs can do is still coming into focus, and they may not be the only answer the industry ultimately adopts. What is already clear is that organizations that invest in cryptographic agility, certificate lifecycle management, and complete visibility today will be best positioned to adapt as post-quantum standards mature.

The future of digital trust will belong to organizations that can evolve as quickly as the cryptography they depend on.

*This article was produced as part of* * TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:* * [https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

Jason Soroko is the SVP of Product at Sectigo. Jason has 20 years of experience researching, innovating, educating markets, developing intellectual property, and contributing to national-level guidance and consortium standards.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
