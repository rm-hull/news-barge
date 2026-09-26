---
title: ChatGPT-6 Astra cracks 85-year-old 1941 Enigma-coded message in two days —
  autonomous AI coded its own simulator to crack code that was unsolved since it was
  shared online back in 2005
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/chatgpt-6-astra-cracks-1941-enigma-coded-message-in-two-days-autonomous-ai-coded-its-own-simulator-to-crack-code-that-was-unsolved-since-it-was-shared-online-back-in-2005
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-26T11:27:46Z'
published: '2026-09-26T00:00:00Z'
description: Before it started cracking, the LLM developed Python and C++ software
  for an Enigma simulator and Enigma Bombe.
image: https://cdn.mos.cms.futurecdn.net/Gpd4WXYpC44LG25KjWMRMN-1920-80.jpg
categories:
- Technology & Software
- Hardware
people:
- Mark Tyson
- Tom
locations:
- Lorenz
- Rosenow
- WWII
organisations:
- Astra
- Crypto Cella
- Crypto Cellar
- Crypto Cellar Research
- Death’s Head) Division
- Enigma
- GPT6-Astra
- GTP-Astra
- German Army
- Get Tom's Hardware
- Google News
- LLM
- MVUEH
- MVUEHA Cryptanalysis Case Study
- SIPVX
- SS-Totenkopf
- Tom's Hardware
---

![A WWII Enigma machine](https://cdn.mos.cms.futurecdn.net/Gpd4WXYpC44LG25KjWMRMN.jpg)

A German Army Enigma transmission from 85 years ago, known as the MVUEH message, has been cracked by GTP-Astra in two days, reports the Crypto Cella. MVUEH was sent by the German Army to the SS-Totenkopf (Death’s Head) Division on July 10, 1941, at the height of the Nazi military power in WWII. This uncracked Enigma message was shared with enthusiasts online in 2005, but its secrets had remained concealed until now.

Crypto Cellar researchers highlight that what Astra managed to do in just two days “would take a human researcher weeks or even months.” Currently, the awestruck researchers are still picking through logs to determine how Astra managed this feat and how it did it so quickly.

One of the most impressive things about Astra’s tackling of MVUEH was that it “did it entirely on its own,” says the source. It was merely asked whether it could break any of the unbroken Enigma machine messages published on the Crypto Cellar Research web page. In response, Astra picked Nr. 172, MVUEH as a promising target and thought it might be related to the plaintext of Nr. 173, SIPVX.

With its target decided and expecting the repeated place name "ROSENOW ROSENOW" as a probable plaintext clue, Astra developed Python and C++ software for an Enigma simulator and an Enigma Bombe. Its hunch appears to have been correct. You can see a demo of the radio message being decrypted online at the MVUEHA Cryptanalysis Case Study site (screenshot below).

![Enigma machine message decoding](https://cdn.mos.cms.futurecdn.net/c6ufpPhhdHae4tNVcRmCPN.jpg)

In brief, the encrypted 82-letter MVUEH cipher looked like this: **ICRVSORMCCWQTATYEVFXDBZGGSNXWLPSYWZYTCBSWULRTBZCVGODVJUSLSOOMJQJZSXSEBZPEYMDNXJYTC**

Decrypted, with spaces added as appropriate, it looks like this: **BTTE UM ANGABE DES MARSQWEGES X BEFINDE MIQ IN X ROSENOW ROSENOW X SOFORT FUNKANTWORT X WASCHBBSCH**

An approximate English translation is:**Please specify the route of march. I am in Rosenow, Rosenow. Immediate reply by radio**

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Note that there was a spelling mistake at the front of the original message, which wouldn’t help decoding efforts.

We’ve looked at Enigma machines before, as efforts to crack wartime ciphers from them, as well as from Lorenz machines, would lead to some of the first general-purpose digital computer designs.

The Enigma featured a 26-key keyboard, with 26 light-up letters on the ‘lampboard’ positioned above it. Behind the lampboard, three rotors were installed from a set of five. The signal from a keyboard press traveled through an input wheel, then the three manually turnable rotors with 26 pins each, then a reflector to return the signal, which lit up the lampboard. Making it even more tricky to crack, the rotors would advance every keypress. Thus, if you keep pressing the same letter, a different letter on the lampboard would be shown each time. Yet another layer of obfuscation was added via the plugboard at the front of the machine, where users swapped more letters around. Operators used up to 10 plugboard rerouting wires.

Before using the Enigma machine, four settings must be dialed in by the operator: rotor order, ring setting, rotor starting positions, and plugboard connection(s). These settings were distributed separately, and they changed following a calendar. Even if the enemy had an Enigma machine, they’d also need to know the settings on the day to decode the message(s).

We reported on GPT6-Astra's deciphering skills just last week. The LLM was behind the cracking of a 108-year-old unsolved WWI German code that had been encrypted using the ADFGVX method.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Mark Tyson](https://cdn.mos.cms.futurecdn.net/56vqMYLDaKRHPhHZgbADFR.jpg)

Mark Tyson is a news editor at Tom's Hardware. He enjoys covering the full breadth of PC tech; from business and semiconductor design to products approaching the edge of reason.
