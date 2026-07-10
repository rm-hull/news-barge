---
title: This malicious Google Notes extension just wants to sneakily steal all your
  crypto
source_url: https://www.techradar.com/pro/security/this-malicious-google-notes-extension-just-wants-to-sneakily-steal-all-your-crypto
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-10T11:16:12Z'
published: '2026-07-10T00:00:00Z'
description: Another clipboard jacker was found in the wild, on the prowl for people's
  crypto.
image: https://cdn.mos.cms.futurecdn.net/VnoVVXTmAmxSBYBe4LUwVW-1919-80.jpg
---

![Cryptocurrencies](https://cdn.mos.cms.futurecdn.net/VnoVVXTmAmxSBYBe4LUwVW.jpg) 

- **McAfee flags “Silent Swap,” a malicious Chromium extension disguised as Google Notes that secretly hijacks crypto transactions**
- **It works as a clipboard jacker, swapping copied wallet addresses with attacker‑controlled ones so victims unknowingly send funds to criminals**
- **Researchers advise always cross‑checking full wallet strings before sending, as attackers can craft lookalike addresses differing only in a few characters**

Researchers have found yet another extension for Chromium-based browsers that is designed solely to steal people’s hard-earned cryptocurrency.

A report from McAfee has sounded the alarm on Silent Swap, a piece of malware hiding inside a benign-looking Google Notes extension.

Victims who stumble upon and download it (most likely through phishing, social engineering, or shady forums and websites), will get an extension that, on the surface, works as intended. It shows a small window where the victim can type a note and save it. They can color-code the notes and search through saved ones. However, this was only made to hide the program’s true intentions, which are to steal cryptocurrency.

## Hijacking the clipboard

Silent Swap works like a typical clipboard jacker. It monitors the clipboard for strings that look like a crypto wallet - seemingly random strings of 26 to 42 alphanumeric characters.

When it spots one, it replaces it with a different one belonging to the attacker, so when the victim pastes the address into the wallet to send the funds, they are actually sending them to the address belonging to the attackers.

This works because crypto wallets are almost impossible to memorize, and too risky to type in from a piece of paper or a different document, forcing users to rely on copying and pasting.

Once the victim sends the funds, they are almost certainly irretrievably gone. Only if the funds are being sent from a centralized exchange (like Coinbase, for example), and if the victim spots the attack fast enough, can they ask the exchange’s support to freeze the transaction. In all other cases, once the money is sent, it’s gone.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The best way to defend against these attacks is to cross-reference the strings before hitting send. Some people would only check the first and last few characters, but security researchers don’t recommend it, because some clipboard jackers can generate addresses that only differ in a few characters.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png)

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
