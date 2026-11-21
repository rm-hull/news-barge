---
title: New Windows 11 lock screen zero-day unlocks BitLocker-protected PCs with just
  a few keystrokes — Win+U keyboard trick lets physical attackers run USB payloads
  or create new admin accounts
source_url: https://www.tomshardware.com/tech-industry/cyber-security/new-windows-11-lock-screen-zero-day-unlocks-bitlocker-protected-pcs-with-just-a-few-keystrokes-win-u-keyboard-trick-lets-physical-attackers-run-usb-payloads-or-create-new-admin-accounts
source_site: Tom's Hardware
source_slug: toms-hardware
description: Windows 0-day lets attackers run software by partially bypass the lock.
  screen with just some keystrokes — even BitLocker-protected machines are seemingly
  vulnerable
image: https://cdn.mos.cms.futurecdn.net/sR3wn4pbkQv44DiMtCfRCY-2048-80.jpg
published: '2026-11-19T00:00:00Z'
scraped_at: '2026-11-21T10:55:55Z'
categories:
- Technology & Software
- Hardware
people:
- Abdelhamid Naceri
- Bruno Ferreira
- Reddit
- Tom
locations:
- Narrator
organisations:
- Bitlocker
- CIS
- Center for Internet Security
- Google News
- Microsoft
- PC
- TechieTwo
- Tom's Hardware
---

![Security vulnerability](https://cdn.mos.cms.futurecdn.net/sR3wn4pbkQv44DiMtCfRCY-1920-80.jpg)

Considering the current status of the cybersecurity landscape, some may well say that "0-day" has lost its meaning, The latest high-stakes vulnerability pertains to a bug in Windows 11 (and possibly 10), wherein an attacker can partially bypass the lock screen and run software as the logged-in user, and seemingly access their data. If true, the vulnerability means even BitLocker won't help keep users' files protected.

Unsurprisingly, the bug was discovered by Abdelhamid Naceri, the prolific Windows hacker known to the world as Nightmare Eclipse, and is responsible for about a dozen zero-day findings in Microsoft's operating system. The exploit requires physical access to the machine, but that's precisely the scenario that lock screens and/or BitLocker are supposed to protect against.

To trigger the vulnerability, all you need is a keyboard. In the Windows 11 lock screen, click "Forgot my PIN," then hit Win+U to bring up the voice narrator. The window will be hidden behind the lock screen, which, for practical purposes, is just a veneer, but you can interact with it using the keyboard if you hold down the Caps Lock key and use the arrows and Enter.

After some brief navigation through Narrator, you'll actually be in Settings, and then have multiple avenues for further shenanigans. One obvious one is going into Bluetooth and Devices and setting Autoplay to show a USB stick's files and folders, then plugging in your own with your software of choice to run. Additionally, on a personal machine, the user is bound to have administrator permissions, so you can just create your own account.

This bug is quite fresh, so there isn't widespread reporting or testing. The author claims "the vulnerability seems to be extremely consistent in every machine I tested it in." We did encounter a sysadmin on Reddit, danrhodes1987, who claims they've tested it on machines they manage, and sure enough, it works, though only on their InTune-enrolled devices. He says that "you can launch anything you want in the context of the user logged onto the device."

Additionally, they found it possible to invisibly navigate whichever programs the user had open before they locked their screen, which all but guarantees that the victim's entire data and programs will be fully accessible. As a Windows sysadmin friend of mine remarked, Windows' lock screen implementation always felt like a kludge, and he posits this won't be the last hack found for it.



*Download the Tom's Hardware app for up-to-the-minute updates on* * iOS* * and* * Android**. Also follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G-140-80.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.

* If I remember correctly - it's been many years - about 15 years ago I encountered a random website that had a simple universal hack for windows based on a similar process of bringing up a file dialogue when clicking on the Accessibility button/settings. I tried it once way back when, and it worked on the versions of windows I had access to at the time. Kind of blows my mind that such a simple crack has been potentially hiding in plain sight, in some form or another, for decades.Reply
* a bit of a misunderstanding of bitlocker.  
  bitlocker protects the data at rest, once the PC boots into windows bitlocker isn't part of the equation, so this doesn't bypass bitlocker, and would function the same whether the PC is protected by bitlocker or not Reply
* Ok, my narrator was already switched off by default. then I went into settings and disabled all settings individually -- like verbosity to minimum. no context, etc. should make my machine more difficult to hackReply
* Phew. Thankfully, any corp would have disabled usb devices with ZERO users running as full admin. Even the administrator.  
    
  Come on MS, fix this.  
    
  TechieTwo said:Ya just gotta trust your security to MS... or maybe NOT. :(Group policies are awesome. Home users?? They all run as admin, so what does anyone expect???!! Reply
* I feel like this existence of this article is pointless. The source did not go further than showing the possibility of accessing the settings app and messing around with settings. I would actually like to see the writer here try out the vulnerability himself and demonstrate that it can indeed lead to accessing a users files. As long as there is no proof that it can happen, this article is useless.  
    
  Note that i said THIS ARTICLE is useless. I am not saying the vulnerability is useless. Reply
* psyconz said:If I remember correctly - it's been many years - about 15 years ago I encountered a random website that had a simple universal hack for windows based on a similar process of bringing up a file dialogue when clicking on the Accessibility button/settings. I tried it once way back when, and it worked on the versions of windows I had access to at the time. Kind of blows my mind that such a simple crack has been potentially hiding in plain sight, in some form or another, for decades.  
  If this is the one where you  
  use the recovery environment to rename cmd.exe to utilman.exe  
  run cmd.exe by clicking on the accessibility icon on the login screen (which normally points to utilman.exe)  
  use "net user*username password* " to change the password of any locally stored account on the PC  
  then login with the new passwordthen yes, yes it still works. Or it did the last time I answered the 'help! I forgot my password' cry three months ago. Reply
* chemistu said:If this is the one where you  
  use the recovery environment to rename cmd.exe to utilman.exe  
  run cmd.exe by clicking on the accessibility icon on the login screen (which normally points to utilman.exe)  
  use "net user*username password* " to change the password of any locally stored account on the PC  
  then login with the new passwordthen yes, yes it still works. Or it did the last time I answered the 'help! I forgot my password' cry three months ago.unlikely, cause to unlock the drive you'd need a bitlocker recovery key or credentials. Reply
* excalibur1814 said:Phew. Thankfully, any corp would have disabled usb devices with ZERO users running as full admin. Even the administrator.  
    
  Come on MS, fix this.  
    
    
  Group policies are awesome. Home users?? They all run as admin, so what does anyone expect???!!Most orgs with a decent security posture will have also disabled Microsoft consumer accounts using GP's. If one of the prerequisites are disabled for the exploit to work, the exploit is effectively dead in the water... though new exploits might find another way...  
    
  **Computer Configuration → Windows Settings → Security Settings → Local Policies → Security Options → Accounts: Block Microsoft accounts**: Users can't add or log on with Microsoft accounts  
    
  One of the many CIS (Center for Internet Security) Windows controls that help reduce attack surface. As you said though, Home users are screwed on this.  
    
  Personally, I run Windows Pro on all of my Windows machines at home as Microsoft's default security settings on Home are too soft, plus there are other non-security-related settings that I can control in Windows using Local Group Policy Editor, not to mention it's way easier to keep using local, offline accounts. Reply
* vv211 said:bitlocker protects the data at rest, once the PC boots into windows bitlocker isn't part of the equationBitlocker is still responsible for decrypting the data from disk even after Windows boots. While data that has been loaded into RAM will be unencrypted at the lock screen, data on disk is still encrypted and you need the keys/Bitlocker to decrypt that data before the content can be read successfully.  
    
  For this vulnerability, Bitlocker's encryption at rest/on disk could bypassed with this scenario since you can run an arbitrary program with Auto Run enabled which could allow Bitlocker protected/encrypted data to potentially be copied as an unencrypted file to a thumb drive or folder in the could or on the local network.  
    
  So while the statement is technically true, it's not entirely accurate, because you could bypass its data at rest protections with this vulnerability. Reply
