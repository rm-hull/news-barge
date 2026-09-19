---
title: 'Exclusive: OpenSSL tells us how to prepare for a post-quantum internet'
source_url: https://www.techradar.com/pro/the-fixes-are-architectural-not-bigger-pipes-openssl-president-on-what-businesses-can-expect-and-how-to-prepare-for-a-post-quantum-internet
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-19T18:35:13Z'
published: '2026-09-19T00:00:00Z'
description: I spoke to OpenSSL President Tim Hudson to learn how business can prepare
  for a post-quantum internet and the logistical nightmare of securing encryption.
categories:
- Technology & Software
- Business & Entrepreneurship
image: https://cdn.mos.cms.futurecdn.net/UVm4pWzxzFfM3waNQDdPrD-1920-80.jpg
---

![Quantum computing concept. Digital communication network. Technological abstract.](https://cdn.mos.cms.futurecdn.net/UVm4pWzxzFfM3waNQDdPrD.jpg)

Knowing what ‘quantum’ is and why it affects the internet may not be something most people understand. How a physics concept changes the security of the internet isn’t really at the forefront of most people’s worries.

But the change is already happening. The internet is preparing for a post-quantum world that renders much of the encryption the world has relied on obsolete. To understand just how powerful post-quantum decryption is, think of enigma: an encryption machine that took the entire secret operation of Bletchley park over a year to crack would be solved almost instantly. For today’s standard public-key encryption algorithms, it's a matter of days or hours.

By some estimates, the viability of quantum computers capable of this level of decryption are still several years away. But preparations are already happening - and not just by the good guys.

## How the good guys and bad guys are preparing for Q-Day

Given that quantum computers capable of decrypting the current algorithms many businesses rely on today are all but inevitable, hackers have begun stealing troves of files that they cannot currently crack but will have huge value once commercially available quantum computers become available.

To get ahead of the curve, governance bodies have begun introducing regulations to ensure businesses and services are fully protected ahead of time, using longer, more robust encryption methods that can hold up against the quantum threat.

But the shift to protecting against quantum threats introduces new problems for the wider internet. Longer signatures during exchanges add to congestion, and when multiplied by the millions of terabytes of data transferred across the internet each day, this could compound into a serious logistical problem if the necessary steps are not taken.

OpenSSL is one of the world's most widely deployed open source cryptographic libraries. It has been developing open-source post-quantum cryptography to help secure businesses (and the internet) in the billions of secure online interactions that happen every day.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Ahead of OpenSSL Conference 2026, I spoke to Tim Hudson, President of OpenSSL Corporation, about the post-quantum challenges and how organizations can best prepare for a post-quantum internet.

* **What challenges will infrastructure providers face in trying to handle a quantum-safe internet that requires significantly larger digital signatures? What sort of capacity, bandwidth, and latency increases could we expect to see and how can they be addressed?**

It helps to separate two migrations that are usually collapsed into one. Key exchange is largely solved and already deployed — hybrid post-quantum key agreement has been running in mainstream browsers and CDNs for well over a year, and most people reading this have been using it without noticing. Signatures are the unsolved part.

The numbers drive everything. An ML-DSA-44 signature is 2,420 bytes with a 1,312-byte public key, against 64 bytes for ECDSA P-256. Add certificate chain signatures and the two Certificate Transparency timestamps browsers require, and a naive substitution adds somewhere between 7KB and 10KB to every new connection.

The problem is not aggregate bandwidth, which is cheap. It is that this pushes handshakes past the initial congestion window — roughly 14KB — and past QUIC's anti-amplification limit. Cross those and you buy an extra round trip on every fresh connection. That is a tail-latency problem, and it lands hardest on mobile, satellite, lossy links and constrained devices.

The fixes are architectural, not bigger pipes: Merkle Tree Certificates, trust anchor negotiation, and suppressing intermediates. This is a PKI redesign, not a library upgrade.

* **How would you recommend CISOs navigate budgetary constraints when trying to secure their business for the quantum era? What are the critical assets to secure?**

Two principles save real money. First, inventory before procurement. You cannot budget a migration you have not scoped, and the discovery phase in a complex estate runs six to twelve months. A cryptographic bill of materials is now explicitly on the regulatory agenda, so this work is not optional in any case.

Second, buy agility rather than algorithms. Products marketed as "quantum-safe" are a poor investment. The ability to change algorithm without redesigning the surrounding system will still be valuable in fifteen years; any specific algorithm choice may not be.

For prioritisation, the useful distinction is between confidentiality and authentication. Recorded traffic can be decrypted retrospectively, so anything requiring long-term secrecy is urgent today. Signatures cannot be forged retroactively — a signature made in 2026 and verified in 2026 is not at risk — so authentication is a scheduling problem, not an emergency.

That points at the genuinely critical assets: hardware roots of trust, firmware and code-signing keys, HSM-held key material, PKI roots with twenty-year validity, and long-lived embedded or operational technology. Those are the things you cannot retrofit later. Everything else is a software update.

* **Are there any technologies that businesses can leverage now to maintain backwards compatibility with their existing data and processes as they adopt quantum-safe cryptography?**

Several, and most are already in production. Hybrid key establishment is the obvious one. TLS 1.3 negotiates it cleanly and falls back to classical algorithms when the peer does not support post-quantum, so deployment carries little compatibility risk. For certificates, composite and dual-chain approaches let a single deployment satisfy both old and new relying parties during transition.

The less visible but more important layer is cryptographic abstraction. The OpenSSL Library provider architecture exists precisely so algorithm implementations can be replaced without touching application code, and that is the mechanism that makes the transition survivable for anyone with a large codebase.

On the interface side, PKCS#11 v3.2 defines post-quantum mechanisms so HSM-backed applications share a common API, and KMIP handles key lifecycles across multi-vendor estates. I work on both of those standards, and the aim is the same: rotate the algorithm without re-plumbing the system.

One caution. Hybrid is a transition, not a destination — the Australian Signals Directorate is explicit on that point. If you deploy a hybrid, budget for the second migration now rather than discovering it in 2029.

* **What role will open source infrastructure play in the post-quantum internet, and are there any unique challenges or opportunities open-source technologies face?**

Interoperability is the whole problem, and open source is where interoperability actually gets settled.

Agreeing on an algorithm is necessary but nowhere near sufficient. A working internet migration requires implementations that genuinely interoperate at the byte level, across every vendor, under real conditions.

That agreement gets reached in shared, publicly testable code far more reliably than in specification documents. The practical consequence is that a handful of open source implementations effectively set the pace of the entire transition.

The opportunity is scrutiny. Post-quantum algorithms are new, and most real-world cryptographic failures are implementation defects rather than mathematical ones. Side-channel weaknesses are found by people who can read and attack the code.

The challenges are the familiar ones, and unresolved. Funding remains disproportionate to dependency. Validation lag is the sharper issue: FIPS and Common Criteria validated modules trail published standards by years, so regulated organisations facing 2030 deadlines may find conformant code exists but validated code does not.

That ecosystem problem is a large part of why the OpenSSL Conference in Prague in October each year is scoped across cryptography and security generally rather than around any single project.

* **In your opinion, is regulation and governance moving fast enough to prepare businesses of all sizes for Q-day? Are there any shortfalls you would like to see addressed?**

The direction is right; the coverage is uneven. The pace has changed materially in 2026. In June the US issued Executive Order 14412 and OMB Memorandum M-26-15, setting hard dates for federal civilian systems and putting cryptographic bills of materials on the agenda.

Australia's Signals Directorate holds one of the more demanding positions globally, expecting a refined transition plan by the end of this year and traditional asymmetric cryptography retired by the end of 2030. The EU roadmap runs national plans to end-2026, high-risk systems to 2030, and full transition to 2035.

Four shortfalls. Guidance is written for large regulated enterprises; smaller organisations receive exhortation rather than tooling. Validation throughput is a binding constraint that no mandate addresses.

Nothing credible covers deployed embedded and operational technology with fifteen to twenty-five year service lives and no update path — that is a replacement program, not a migration, and nobody has funded it. And procurement rules should require demonstrated agility and CBOM (Cryptographic Bill of Materials) disclosure rather than algorithm checkboxes.

I would also retire the "Q-day" framing. The deadlines that will actually bind organisations are being set by regulators, insurers and procurement teams, not by physics.

* **What should those outside of the business world expect to see changing as we approach a quantum-safe internet, and what can they do to prepare?**

Mostly, they should expect not to notice. The browser and operating system on your desk have very likely been performing post-quantum key exchange for more than a year without announcing it. That is what a well-run infrastructure migration looks like.

The visible effects will be modest and mostly indirect: slightly larger handshakes, occasionally slower first connections over poor mobile or satellite links, more frequent firmware updates, and some devices losing support earlier than owners expect because their hardware cannot be upgraded to support the new algorithms.

The practical advice is unglamorous. Keep software current - that genuinely is most of it. Expect shorter useful lifetimes for anything with a hardware root of trust. And treat consumer products marketed as "quantum-safe" with scepticism; there is very little a consumer can buy that addresses a risk not already being handled upstream.

The one real personal consideration is long-lived confidential data. Anything that must stay secret for fifteen years or more and is transmitted today could be recorded now and read later. That is a reason to care which services have migrated, not a reason to buy anything.

![Google logo on a black background next to text reading &#039;Click to follow TechRadar&#039;](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg)

***Follow TechRadar on Google News***and** add us as a preferred source** * to get our expert news, reviews, and opinion in your feeds.*

![Benedict Collins](https://cdn.mos.cms.futurecdn.net/jEvqGv8wvH7PWZ4XPURyyB.jpg)

Benedict is a Senior Security Writer at TechRadar Pro, where he has specialized in covering the intersection of geopolitics, cyber-warfare, and business security.

Benedict provides detailed analysis on state-sponsored threat actors, APT groups, and the protection of critical national infrastructure, with his reporting bridging the gap between technical threat intelligence and B2B security strategy.

Benedict holds an MA (Distinction) in Security, Intelligence, and Diplomacy from the University of Buckingham Centre for Security and Intelligence Studies (BUCSIS), with his specialization providing him with a robust academic framework for deconstructing complex international conflicts and intelligence operations, and the ability to translate intricate security data into actionable insights.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
