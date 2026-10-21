---
title: You might need to update your BIOS for COD MW4 online play
source_url: https://www.pcgamer.com/games/call-of-duty/dont-get-hit-with-the-bios-update-hammer-for-cod-mw4-like-my-colleagues-heres-how-to-ensure-you-can-play-multiplayer-and-dmz/
source_site: PC Gamer
source_slug: pcgamer
scraped_at: '2026-10-21T17:10:30Z'
published: '2026-10-21T00:00:00Z'
description: TPM and Secure Boot requirements strike again.
image: https://cdn.mos.cms.futurecdn.net/ADf8vRbBtWTiViXXLTEKWT-1913-80.jpg
categories:
- Technology & Software
- Video Gaming
people: []
locations:
- GameSir
organisations:
- AMD fTPM
- Activision
- Elgato Facecam
- Intel PTT
- PC Gamer
- Razer BlackShark V34
- Razer Viper
- ReBAR
- Secretlab Magnus Pro XL3
- Secretlab Titan Evo2
- Secure Boot
- Shure
- TPM
- Wireless5
---

![A screenshot of the COD: MW4 operator selection screen.](https://cdn.mos.cms.futurecdn.net/ADf8vRbBtWTiViXXLTEKWT-1913-80.jpg)

If you're itching to get your pupils up against Call of Duty: Modern Warfare 4 on PC at launch on Friday, you should probably double-check your system is up to date. We've already had a couple of colleagues here flung against the wall of requirements with the new COD, requiring a BIOS update to play online.

That's because Activision explains that both TPM 2.0 and Secure Boot are required to play any online game mode (multiplayer or DMZ). More specifically, though, you must have a new enough version of PTT (Platform Trust Technology) for Intel systems, and fTPM (Firmware Trusted Platform Module) for AMD ones.

Secure Boot and TPM requirements themselves are part of the toolkit that many modern online games use to keep cheaters out. We've seen requirements for both, for instance, to play Battlefield 6. Secure Boot is what gives your firmware and kernel themselves signatures to ensure they are legit, and the TPM helps verify that everything boots up in order with no extra, malicious software or firmware thrust into the boot process. Intel PTT and AMD fTPM are implementations of TPM.

The key confusion with COD MW4 is that just having Secure Boot and TPM 2.0 doesn't seem to be enough on its own—old versions of PTT or fTPM won't work.

Activision says that, for Intel systems, if your TPM version is some form of 302.1.2.X or 303.1.2.X (where X can be anything), your motherboard may require a firmware update.

For AMD ones, 3.X.0.X versions aren't compatible and will require a firmware update.

To update either PTT or fTPM, you need to update your BIOS.

Keep up to date with the most important stories and the best deals, as picked by the PC Gamer team.

To check your TPM version, press Win+R and run 'tpm.msc'. It should show you your version under 'TPM Manufacturer Information' at the bottom. If your TPM info window says one of those aforementioned versions you'll need to update your BIOS.

Bear in mind that this isn't just a problem with very old CPUs, as we've had two colleagues here at PC Gamer run into the issue despite running an Intel Core i5 12400KF and AMD Ryzen 5 5800X, respectively. Though they have admitted their BIOS versions were many years old.

If you've not updated your BIOS in a very long time, it's probably a good idea to do so before COD drops. One can fix vulnerabilities and even sometimes resolve pretty serious stability and longevity issues, as was the case with Intel's 14th Gen chips a few years back.

## How to update your BIOS

![A screenshot of COD: MW4, aiming down-range at a target.](https://cdn.mos.cms.futurecdn.net/YCfD5BENn8KFH9od8t5TdT-1200-80.jpg)

* **Download the most recent stable version for your specific motherboard from its manufacturer's website.**
* **Store it on a USB drive and plug that directly into your motherboard at the back of your PC**
* **Reboot and head into your BIOS.**
* **Find your BIOS update section**
* **Choose to do a local/offline install**
* **Select your newly downloaded BIOS file to install from.**

Oh, and then back away slowly, and don't trip over that power cable while it installs. Kidding, it'll be fine—just take your time and do everything by the book.

If you're struggling to actually get into your BIOS via the traditional Del/F2 route—if your monitor stays black during POST for example—then you can hold down the Shift key while you restart your PC from the Windows shutdown menu. This will boot into a start menu that will allow you to go into an advanced options screen that lets you boot into your UEFI BIOS.

## How to get set up after your BIOS update

![Modern Warfare 4 release times - Soldiers on a helicopter](https://cdn.mos.cms.futurecdn.net/FWTAmnRbksM8Lg3gqrnMUM-1200-80.jpg)

Bear in mind that updating your BIOS resets everything, so you might need to adjust some settings to get things back how they were.

Most important, given the reason we're doing all this, is checking you have Secure Boot, TPM, and PTT/fTPM enabled. These settings will usually be found in a Security or Boot section, but the exact location will depend on your motherboard and BIOS.

You'll also want to check your memory profile, which adjusts your RAM speed and timings. If you have a specific one you selected previously, you'll have to find that again, but for most people simply enabling XMP (for Intel) or EXPO (for AMD) will do, as these should get your RAM running at faster timings. Most BIOSes should have an obvious toggle for this, though you might have to navigate to a page containing your memory settings.

You might also want to adjust your fan profiles if you prefer a manual curve. It will be worth checking your primary boot drive is recognised and set with first boot priority, too. And lastly, you should check Resizable BAR (ReBAR) is enabled, which is usually found in Advanced or PCIe menus.

Once all is in order, you can boot up into Windows and, with any luck, get into COD without issue.

![Secretlab Titan Evo gaming chair in Royal colouring, on a white background](https://cdn.mos.cms.futurecdn.net/7rTxS5WgHWFPDRsqLd28vh-140-80.png)

**1. Best gaming chair: Secretlab Titan Evo2. Best gaming desk: Secretlab Magnus Pro XL3. Best gaming headset: Razer BlackShark V34. Best gaming keyboard: Asus ROG Strix Scope II 96 Wireless5. Best gaming mouse: Razer Viper V4 Pro6. Best PC controller: GameSir G7 Pro7. Best steering wheel: Logitech G Pro Racing Wheel8. Best microphone: Shure MV6 USB Gaming Microphone9. Best webcam: Elgato Facecam MK.2**
