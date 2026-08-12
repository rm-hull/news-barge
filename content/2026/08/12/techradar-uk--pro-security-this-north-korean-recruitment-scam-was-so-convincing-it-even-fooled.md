---
title: This North Korean recruitment scam was so convincing it even fooled Google
source_url: https://www.techradar.com/pro/security/this-north-korean-recruitment-scam-was-so-convincing-it-even-fooled-google
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-12T17:07:26Z'
published: '2026-08-12T00:00:00Z'
description: Fake sites were popping up at the top of search engine results pages
image: https://cdn.mos.cms.futurecdn.net/kDLU9By5uaPPbwrbfEaZFJ-2560-80.jpg
---

![North Korean flag with a hooded hacker](https://cdn.mos.cms.futurecdn.net/kDLU9By5uaPPbwrbfEaZFJ.jpg) 

- **Lazarus expanded Dream Job with a zero‑day, new backdoor, and advanced relays**
- **Fake job lures, trojanized PDFs, and spoofed sites enabled high‑level compromises**
- **Targets included defense and aerospace firms, prompting stronger phishing awareness**

Security experts from Check Point Research say they have uncovered a new wave of "Operation Dream Job" attacks, leveraging a previously undocumented backdoor, a brand new Windows zero-day vulnerability, and a never-before-seen webshell/relay.

Lazarus Group is a hacking collective on the payroll of the North Korean government. It is a state-sponsored threat actor known for targeting cryptocurrency developers and other professionals in the Web3 industry, stealing their tokens and using the money to fund the country’s weapons program and the wider state apparatus.

It is also known for running Operation Dream Job - a hacking campaign that’s been going on for years, and that lures victims with highly lucrative but bogus job opportunities.

## What is Operation Dream Job?

The scam works like this: the attackers come up with a fake company, often in the software development, defense, aerospace, or military industries.

They create the fake company’s website, LinkedIn account, as well as fake people supposedly employed there. Then, they reach out to their targets, offering great working conditions, amazing salaries, and an opportunity to work on exciting projects.

Victims that take the bait are then led through a series of “interviews” and somewhere along the line, they are either given weaponized PDF files or asked to download and run executables and other code, as part of a “training exercise” or “skill evaluation”. At this moment, the victims get compromised, while the attackers gain access to their actual employers’ infrastructure.

From there, the ending can be relatively different. Lazarus has, on at least one occasion, stolen more than a billion dollars in cryptocurrency from one of its victims.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## Ante up

Perhaps the biggest finding is that Lazarus even managed to fool Google - fake Lockheed Martin and Enveil job postings all made it through filters, while spoofed, malicious websites were showing at the top of search results.

Then, there is the new Windows vulnerability the group has been exploiting. A zero-day, now tracked as CVE-2026-68820, is described as a “use-after-free bug in Windows Ancillary Function Driver for WinSock”, allowing authorized attackers to elevate privileges locally.

This bug was found in a core Windows networking component and allows an attacker who already deployed a piece of malware on the machine to escalate privileges to the highest level. Microsoft patched it on August 11 2026.

Lazarus used this bug to deploy a previously undocumented backdoor called Troy. This malware comes with 17 commands, including file upload and download, interactive shell access, in-memory DLL injection, and process termination.

The group was also using compromised Roundcube webmail and CMS servers as C2 relays, instead of simply running their own infrastructure, and they were deploying a new PHP webshell called RelayShell. This one doesn’t behave like a conventional backdoor, since it passes commands and responses between victims and operators through text files.

In one of the observed infection chains, Check Point also found the crooks using SecurityPDF, a trojanized PDF viewer which they were hosting on websites impersonating a legitimate business called Enveil. The drake viewer scans PDF files for a particular hidden marker and, if it finds it, decrypts it and loads Troy directly into memory.

Lazarus usually targets cryptocurrency and software developers. This time around, however, it set its sights on defense organizations, aerospace companies, as well as those working in aviation. Most of the victims are located in Europe and India, with confirmed activity in France, Germany, Brazil and India.

Check Point also said that not all victims were also targets - some of the organizations compromised in the attacks were later used as infrastructure. In at least one case, Lazarus compromised a Western European organization and used it to send spear-phishing messages to additional victims, effectively exploiting that organization’s reputation and trusted communications.

Since these attacks primarily start with a social engineering element, the best course of action is to educate employees on the dangers of phishing and the fact that, if someone is reaching out with a job offer too good to be true - it most likely is.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
