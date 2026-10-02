---
title: '‘We’re gonna be able to preserve that data for an infinite amount of time’:
  Cops found a way to weaken your iOS security, with potentially worrying consequences
  for your private data'
source_url: https://www.techradar.com/computing/cyber-security/report-claims-cops-have-breached-one-of-ioss-most-secure-features-and-it-could-put-your-private-data-at-risk
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-02T22:15:10Z'
published: '2026-10-02T00:00:00Z'
description: Police agencies have a new tool to get around a vital iOS security feature,
  a new report claims.
image: https://cdn.mos.cms.futurecdn.net/LDhAvwf8iNk2Em3bdkAZEb-2000-80.jpg
categories:
- Technology & Software
people:
- Jiska Classen
- John Ternus
locations:
- China
- Cupertino
- Russia
organisations:
- 404 Media
- AFU
- Airplane Mode
- Apple
- BFU
- GrayKey
- Magnet Forensics
---

![Best iPhone VPN ](https://cdn.mos.cms.futurecdn.net/LDhAvwf8iNk2Em3bdkAZEb-1920-80.jpg)

* **Police may be able to bypass one of iOS’s strongest security features**
* **The revelation is from a leaked video from the GrayKey device’s creator**
* **It has worrying ramifications for your data privacy**

A company that works with law enforcement says it has bypassed a key iOS security feature that protects your sensitive information from being extracted from your iPhone without your permission. But it could be a step backward for user privacy and the security of your personal data.

According to a report from 404 Media, Magnet Forensics — the company behind the GrayKey device police use to crack open iPhones — has developed a new workaround that lets anyone with a GrayKey sidestep Apple’s Inactivity Reboot feature, plus a whole lot more. And it’s been using this exploit since at least early 2025, when a video seen by 404 Media was dated.

Inactivity Reboot is an iOS feature that automatically restarts your iPhone if it hasn’t been unlocked in 72 hours. This puts it into a more secure state called Before First Unlock (BFU), which protects certain sensitive data with encryption keys that aren't released until you enter your device passcode. After you’ve logged in, your iPhone enters a less secure state called After First Unlock (AFU).

In a video uncovered by 404 Media, Magnet Forensics claims that it can now freeze the iPhone in AFU mode using a new device called GrayKey Preserve, and that AFU mode is apparently maintained even if your iPhone restarts. That frozen state gives GrayKey easier access to the device’s data because it is not as strongly encrypted as in BFU mode.

In addition, GrayKey Preserve — and an associated mode for the regular GrayKey called Evidence Preservation Mode — can recover materials that iOS automatically purges after a certain period, including location data, iMessages, and deleted images. “We’re gonna be able to preserve that data for an infinite amount of time,” says a Magnet employee in the leaked video.

The video did not reveal Magnet Forensics’ technical solution in detail, but an employee hinted that enabling Airplane Mode and blocking radio transmissions (including Wi-Fi, Bluetooth and cellular) could play a role. And security expert Jiska Classen told 404 Media that the new GrayKey might be manipulating iOS’s built-in clock, “slowing down time” for the cops or even “stopping the clock from ticking” entirely, thereby indefinitely preventing Inactivity Reboot and iOS’s automatic deletion workflows from running.

## Apple’s security stance

![iPhone being updated](https://cdn.mos.cms.futurecdn.net/qBYKunQfbbd6hVqhnsT59D-1200-80.jpg)

Apple is well-known for the security of its devices and its strong stance against weakening the protections afforded to its users. While Apple says it complies with legitimate police requests, it has actively worked to thwart tools like GrayKey from accessing iPhone data. It has also pushed back against law enforcement requests to build a backdoor into its operating systems that police can use.

Sign up for breaking news, reviews, opinion, top tech deals, and more.

Why would Apple seek to frustrate law enforcement agencies like this? Well, part of the justification Apple has given is that there’s no such thing as a backdoor that only works for the good guys. Any software flaw can be exploited by hackers, stalkers, identity thieves, and all manner of other bad actors. Given the highly private data — including credit card details, medical records, and personal photos — on billions of iPhones worldwide, that’s a serious risk Apple isn’t willing to take.

As well as that, tools like GrayKey are known to be used by authoritarian regimes and hostile nation-states around the world to suppress free speech and harass critics. Apple has taken its fair share of criticism for making concessions to repressive governments in countries like China and Russia, but building an iOS backdoor for them is apparently a step too far for John Ternus’s company.

In the past, Apple has worked quickly to patch exploits used by Magnet Forensics and its competitors, and there’s no doubt that 404 Media’s report will have rung alarm bells in Cupertino and prompted furious work on a fix. But the fact that this vulnerability has been actively exploited since at least early 2025 will be disturbing news for people both inside and outside Apple.
