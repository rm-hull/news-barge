---
title: Novel attack slashes computing power needed to crack textbook RSA cryptography
  — attacks within state-actor reach, could target Apple and Cloudflare privacy services
source_url: https://www.tomshardware.com/tech-industry/cyber-security/novel-attack-on-rsa-cryptography-might-bring-computation-requirements-for-cracking-down-to-manageable-levels
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-26T15:47:06Z'
published: '2026-09-26T00:00:00Z'
description: Not very practical yet, but could serve as the basis for future improvements.
image: https://cdn.mos.cms.futurecdn.net/WjhboXMQFhrhWUebgWihfP-1920-80.jpg
categories:
- Technology & Software
- Hardware
people:
- Bruno Ferreira
- Tom
locations:
- California
- France
- UC San Diego
organisations:
- Apple
- Cloudflare Privacy Pass
- ECC
- Get Tom's Hardware
- Google News
- Inria Nancy
- Nvidia Spectrum-X
- PC
- RSA
- Thales Luna HSMs
- Tom's Hardware
- iCloud Private Relay
---

![Security](https://cdn.mos.cms.futurecdn.net/WjhboXMQFhrhWUebgWihfP.jpg)

Factoring attacks against the RSA algorithm were generally considered infeasible, but that may change dramatically if the findings in a paper from UC San Diego (California) and Inria Nancy (France) prove correct after peer review. The paper outlines a new attack that breaks RSA in record time. That's concerning because RSA-based encryption was in use for quite some time, and although it's been generally deprecated in favor of ECC and post-quantum algorithms, it's still employed today in a substantial portion of services.

![The Nvidia Spectrum-X SN6800 Ethernet Switch](https://cdn.mos.cms.futurecdn.net/utcjC72BFWzJtfv8CPGCkf.jpg)

Assuming the research holds up and the attack conditions are met, the number of necessary operations for cracking an RSA-encrypted key (and thus, inspecting network traffic encrypted with it) drops dramatically. (From 280, 2112, 2128, and 2144 down to 265, 290, 2105, and 2119 — for 1024, 2048, 3072-, and 4096-bit key lengths, respectively.)

Even for the 1024-bit keys, performing 265 calculations is still a *lot*, but it starts getting into the range where it's feasible for an entity with large resources at their disposal, like a number of state actors. Crucially, the paper indicates that the algorithms the team used are far from optimized and could hypothetically be significantly sped up after optimization passes, potentially with the help of AI tools and by leveraging GPUs for the task.

The attack only works against the textbook (or "raw") variant of RSA, which isn't widely used for commonplace computing like website certificates and remote access, but is nevertheless present in services like Cloudflare Privacy Pass, iCloud Private Relay, and Private Cloud Compute. Equipment and services using PKCS #11, like many smart cards, USB security tokens, code-signing pipelines, hardware security (HSM) and trusted platform (TPM) modules also use this variation. But fulfilling the attack conditions is much easier said than done.

In order to reach a point where an attacker can decipher data, they first must perform an exceedingly high number of queries against the key they're attacking, collecting enough data points from the key's oracle. In practical terms, this often means repeatedly poking a live server that's using that key to encrypt traffic, *billions* of times over, though it can also be done against a standalone hardware device.

In the practical context of an encryption algorithm, an oracle takes a number in, runs it through a computation involving a private key, and spits it back out, without revealing its key. The textbook variant of RSA under attack here lets the oracle be queried with *any* number, thus allowing the attacker to collect enough data points to perform the mathematical wizardry described in the paper. They can then proceed to throw a lot of computing power to ultimately inspect whichever traffic they captured that was using*that same encryption key*.

As network administrators have certainly figured out by now, running billions of queries against a live service is almost guaranteed to earn them an IP ban, among other measures. It's a reasonable assumption that entities like Cloudflare and Apple have those kinds of controls in place. Still, not everyone does, especially in the case of key management services that aren't closely monitored, including hardware-based ones. The scientists worked their magic on Thales Luna HSMs, in both hardware and online service form.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Although the bar for a practical application of this attack remains quite high, the key finding is that it may be significantly lowered. This opens the possibility that oracle data collected today may be used to decrypt saved traffic in a matter of weeks or months, especially in the near future as hardware advances. It's also possible that other scientists can take this idea and expand on it, finding additional flaws.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.
