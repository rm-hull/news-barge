---
title: Experts reveal Google Password Manager can be hijacked to let hackers steal
  passkeys and gain access to all your secrets
source_url: https://www.techradar.com/pro/security/experts-reveal-google-password-manager-can-be-hijacked-to-let-hackers-steal-passkeys-and-gain-access-to-all-your-secrets
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-04T18:01:21Z'
published: '2026-08-04T00:00:00Z'
description: Three Pass-ta-key techniques allowed security researchers to work around
  biometrics-protected locks.
image: https://cdn.mos.cms.futurecdn.net/qGbky6N99QiLtik8fjzcUL-970-80.jpg
---

![Circuit board and shield icon, Hardware security, computer data protection and electronic technology concept,](https://cdn.mos.cms.futurecdn.net/qGbky6N99QiLtik8fjzcUL.jpg) 

- **Palo Alto Networks’ Unit 42 detailed three Google passkey exploits**
- **Attacks require prior malware infection; methods ranged from impersonating victims to stealing the master secret protecting synced passkeys**
- **Google implemented fixes after disclosure, with some services (e.g., eBay) patching vulnerabilities directly**

Security researchers from Palo Alto Networks’ Unit 42 have found three ways to exploit Google’s passkey system and log into people’s PIN- or biometrics-protected accounts.

They named these ways ‘Pass-ta-key’, ‘Silver Pass-ta-key’, and ‘Golden Pass-ta-key’, each being progressively more dangerous than the previous one.

While it sounds mighty dangerous, there are major caveats to the exploit, and some of the holes have been plugged already.

## Trusting the wrong device

The biggest caveat is that the victim’s device needs to be infected with malware beforehand. Malware can do all sorts of things, from stealing session cookies to exfiltrating sensitive data, so if a device is tainted with malware, it’s already in trouble.

Still, Unit 42’s findings were important enough to warrant a fix from Google.

In the first technique, the attackers pretend to be the victim. By using malware, they can “ask” Google to log into a passkey-protected account as if it was the victim themselves. Usually, the service being logged into would require a PIN or a fingerprint to confirm the authenticity of the request, but in this scenario, that wasn’t the case.

The method doesn’t work everywhere, though. Unit 42 could not replicate the attack on GitHub, but they succeeded on eBay. The latter later fixed the problem.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

In the second attack, Unit 42 managed to make Google “trust” the threat actor’s device, meaning the victim’s computer was no longer necessary.

In the third attack, the researchers managed to steal the “master key”.

Google Password Manager syncs the passkeys between devices, and to do that, it uses a master secret that protects all of the synced passkeys. The researchers found that, under certain circumstances, malware can grab this master secret while Chrome is temporarily using it, unlocking all of the synced passkeys, copying them to another computer, and being able to use them at a later date.

The researchers disclosed their findings with Google before publication, and some fixes were already implemented. Google is yet to comment on the findings and confirm that all of the flaws were addressed.

*Via* BleepingComputer

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
