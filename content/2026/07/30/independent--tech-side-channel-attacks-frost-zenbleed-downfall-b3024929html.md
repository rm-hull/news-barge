---
title: 'Side-channel attacks: How computers can leak secrets without being hacked'
source_url: https://www.independent.co.uk/tech/side-channel-attacks-frost-zenbleed-downfall-b3024929.html
source_site: The Independent
source_slug: independent
scraped_at: '2026-07-30T21:20:43Z'
published: '2026-07-30T00:00:00Z'
description: The attacker does not steal a password directly or break into the computer,
  but instead studies the traces left behind by the machine while it is operating
image: https://static.the-independent.com/2026/07/30/19/09/iStock-1497901160.jpg?trim=0,180,0,180&width=1200&height=800&crop=1200:800
---

When people hear the word cyberattack, they usually imagine someone guessing a password, planting malware, stealing a computer, hacking an organization’s network or exploiting a flaw in software. A side-channel attack works differently. It looks for clues a computer gives away while doing ordinary work.

A simple analogy is a locked safe. A thief may not know the combination and may not be able to break the lock. But if the thief can listen closely as the dial turns, small clicks or churns or pauses might reveal something about what is happening inside. The safe is not meant to share that information, but its physical behavior still leaks clues.

Modern computers have their own versions of such clues. For example, each computer might take different amounts of time to complete different tasks or may use different amounts of electricity. The hardware – processors, memory, graphics cards and storage drives – may leave tiny patterns as they work.

I’m a computer scientist who studies security and privacy. I define a side-channel attack as an attempt to observe these indirect clues and use them to infer something private.

![Side-channel attacks are a reminder that computers do not have to intentionally reveal secrets to leak them. Sometimes the smallest clues left behind while they work can say more than anyone expected](https://static.the-independent.com/2026/07/30/19/09/iStock-1497901160.jpg)

This is what makes these side-channel attacks unusual. The weakness comes from the way a machine performs its work. The attacker does not steal a password directly or break into the computer, but instead studies the traces left behind by the machine while it is operating.

## History of leaking

The idea is not new. In 1985, Dutch researcher Wim van Eck showed that electromagnetic signals from video display units could be captured and decoded, raising the possibility of eavesdropping on what a screen displayed. The screen was not intentionally broadcasting its contents. It was leaking signals as a side effect of operating.

In the 1990s, side-channel attacks became especially important in cryptography, the science of protecting information. In 1996, cryptography researcher Paul Kocher showed that carefully measuring how long certain operations took could reveal private information from systems using common cryptographic methods. A few years later, Kocher and fellow cryptographers Joshua Jaffe and Benjamin Jun showed that measuring power consumption could help recover secret keys from tamper-resistant devices such as smart cards.

These discoveries changed how engineers thought about security. It was not enough to ask whether an encryption algorithm was mathematically secure. It was even more important to ask whether the device running the algorithm leaked hints through timing, power, sounds or other physical behavior.

There are several common types of side channels:

- A timing attack looks for small differences in how long operations take.
- A power attack studies electricity use.
- Electromagnetic attacks examine unintended signals.
- Acoustic attacks use sound.

In one striking example, researchers showed that the faint noise produced by a laptop during certain cryptographic operations could be used, under experimental conditions, to extract a 4,096-bit secret cryptographic key.

The examples that brought side-channel attacks into wider public discussion were processor attacks. Modern computer processors such as CPUs are extremely fast because they predict what a program is likely to do next. This technique, known as speculative execution, helps computers run more efficiently. But in 2018, cybersecurity researchers discovered two vulnerabilities, dubbed Meltdown and Spectre, in the technique. They showed that these predictions could leave behind measurable traces. A malicious program could use those traces to learn information that should have been protected from it.

Meltdown and Spectre mattered because they challenged one of the basic premises of modern computing: that different programs running on the same machine should be kept separate. They also showed that performance features built deep into computer chips could have security consequences.

## New tech, new side channels

Since then, researchers have continued to find new side-channel attacks in modern hardware. One such side-channel attack revealed in 2022, called Hertzbleed, showed that changes in processor frequency – normally used to save power and manage performance – could become a timing signal that could, in some cases, expose remote servers’ cryptographic secrets.

Another side-channel attack, dubbed Downfall and revealed in 2023, affected certain Intel processors. It showed how a feature called Gather could leak older pieces of data left inside the processor after earlier work. Zenbleed, also revealed in 2023, affected AMD Zen 2 processors and could allow sensitive information from another process to appear where it should not.

## About the author

Chetan Jaiswal is an Associate Professor of Computer Science at Quinnipiac University. This article was first published by The Conversation and is republished under a Creative Commons licence. Read the original article.

Side-channel research has also moved beyond CPUs. GPU.zip showed that graphics processors, or GPUs, can sometimes leak visual clues through the way they handle image data behind the scenes, including the pixels from another webpage in the Google Chrome browser. GoFetch, published in 2024, showed that a hardware feature in many Apple processors designed to predict future memory needs could undermine protections in cryptographic software and help extract secret keys.

The latest attack, called FROST, short for “fingerprinting remotely using OPFS based SSD timing,” involves solid-state drives, or SSDs. These drives are an extremely common form of fast storage on almost all modern computers. FROST shows that a malicious website can use a browser storage feature called the origin private file system to create and access files inside a protected area, called sandbox, that the browser sets aside for that website, then measure tiny delays in SSD activity.

The intuition is simple. If several programs are using the same storage device, they can slow one another down slightly, like cars sharing the same road. By measuring those delays in a browser, the FROST researchers showed that a website could, under specific conditions, infer information about other activity on the same computer, such as websites visited or applications used.

## Lessons more than losses

So, how often are side-channel attacks used? The honest answer is that while they can be damaging, they are not the everyday cyberattack most people encounter. Most real-world cybercrime still relies on easier and cheaper methods, such as exploiting software vulnerabilities, stealing credentials, phishing, malware and ransomware. Verizon’s 2026 Data Breach Investigations Report, for example, highlights software vulnerabilities and ransomware as major sources of breaches, not side-channel attacks as a routine entry point.

This does not make side-channel attacks unimportant. Many are discovered by researchers before they are seen in widespread criminal use. But they matter because they expose weaknesses in the assumptions behind modern computing. They influence chip design, browser security, cloud computing, cryptographic libraries and the way engineers think about privacy.

Side-channel attacks are a reminder that computers do not have to intentionally reveal secrets to leak them. Sometimes the smallest clues left behind while they work can say more than anyone expected.
