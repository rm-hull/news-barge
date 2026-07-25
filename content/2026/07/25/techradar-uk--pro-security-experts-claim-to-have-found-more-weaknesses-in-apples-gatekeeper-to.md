---
title: Experts claim to have found more weaknesses in Apple's Gatekeeper tool — but
  it doesn't seem too bothered
source_url: https://www.techradar.com/pro/security/experts-claim-to-have-found-more-weaknesses-in-apples-gatekeeper-tool-but-it-doesnt-seem-too-bothered
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-25T17:11:47Z'
published: '2026-07-25T00:00:00Z'
description: Locally built app bundles are not covered by macOS guards
image: https://cdn.mos.cms.futurecdn.net/ctUFkwkvMxVyJJwJmZLPJ5-1920-80.jpg
---

![A person using iPhone Mirroring on a MacBook Pro running macOS 27 Golden Gate.](https://cdn.mos.cms.futurecdn.net/ctUFkwkvMxVyJJwJmZLPJ5.jpg) 

- **Researchers show Gatekeeper can be bypassed by replacing a previously run legitimate macOS app with malware**
- **Attack requires prior user‑level code execution, then swaps in a malicious app that Gatekeeper won’t re‑verify**
- **Apple dismissed the issue, saying locally rebuilt bundles fall outside Gatekeeper’s scope, leaving risk to social engineering**

A pair of researchers claims to have found a way around Gatekeeper, a built-in macOS security feature that helps protect users from running malicious or untrusted software. However Apple doesn’t really see it that way and has seemingly decided not to pursue the issue further.

Gatekeeper’s modus operandi is rather simple - when a user downloads an app from outside the App Store, it verifies the product comes from an identified developer and is notarized by Apple. If it can’t verify it - it won’t allow it to run on the machine.

Now, security researchers Talal Haj Barky and Tommy Mysk claim that, as long as a legitimate app was run at least once on a macOS device, it can be replaced with a malicious version, and Gatekeeper won’t even blink its virtual eye.

## Locally built

That also means the attack is not that straightforward to pull off. The threat actor needs to have a way to execute user-level code (for example, a malicious app, a compromised software package installed through a package manager, or a prompt injection attack that tricks an AI agent).

Once that is obtained, they can archive a legitimate app, remove the original, then replace it with malware, and Gatekeeper will not try to re-authorize it. That malicious version can then trick the victim into compromising the device even further, since a certain level of trust was already established.

After reporting the issue to Apple, the company apparently just closed it.

"Apple doesn't consider this attack to be 'modifying' the signed executable," Mysk said. "Instead, Apple says that by archiving/restoring the app bundle, the proof-of-concept code overwrites the entire app bundle, making it locally built. Locally built app bundles are not covered by macOS guards. And this is why access to Keychain or TCC protected directories require system authorization prompts. And for users to accept those is a matter of social engineering attacks that Apple considers out of scope."

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

*Via**The Register*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
