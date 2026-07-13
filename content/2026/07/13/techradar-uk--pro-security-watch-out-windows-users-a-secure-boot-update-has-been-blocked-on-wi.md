---
title: Watch out Windows users, a Secure Boot update has been blocked on Windows 11
  PCs due to failing on some devices — here's how to check if you're affected
source_url: https://www.techradar.com/pro/security/watch-out-windows-users-a-secure-boot-update-has-been-blocked-on-windows-11-pcs-due-to-failing-on-some-devices-heres-how-to-check-if-youre-affected
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-13T21:09:36Z'
published: '2026-07-13T00:00:00Z'
description: Certain older devices that cannot receive updates via their OEM may not
  be able to install the latest Secure Boot certificate.
image: https://cdn.mos.cms.futurecdn.net/ww7R2LTJaqg8pcT4n7C7HD-2560-80.jpg
---

![Checking windows update on laptop screen close up view](https://cdn.mos.cms.futurecdn.net/ww7R2LTJaqg8pcT4n7C7HD.jpg) 

- **Microsoft has blocked Secure Boot updates on some devices**
- **There have been issues with some devices updating from the 2011 certificate to the latest 2023 certificate**
- **Some older devices or those not supported by their OEM may be restricted in downloading the latest Secure Boot certificates**

Microsoft has blocked some Windows 11 PCs from installing Secure Boot updates due to known issues with certificate updates.

The company is currently rolling out an update for Secure Boot on devices using certificates issued in 2011, which are now expired. The new 2023 certificate is being applied through Windows Update, but issues on devices with faulty firmware have forced Microsoft to halt the rollout.

“Devices in this group are affected by a known issue. To reduce risk, Secure Boot certificate updates are temporarily paused while Microsoft and partners work toward a supported resolution,” Microsoft said.

## Secure Boot issues

Secure Boot has long been a device-saving feature when it comes to removing malicious files, as it allows the device to verify and load only authentic software before booting to Windows. However if the device cannot receive certificate updates it can fall victim to threats at the boot-level before Windows is loaded.

Microsoft is currently working with manufacturers to issue a patch that will allow affected devices to install the new Secure Boot 2023 certificate, with HP issuing a BIOS update to allow the installation of the latest certificate.

What this means in practice is that some older devices, or devices that no longer receive updates via their Original Equipment Manufacturer (OEM), will not be able to apply Secure Boot and Boot Manager protections. Microsoft clarified that, “this results in a gradual reduction in long-term security—not an immediate risk or system failure. Continue to follow standard security practices, including staying current with Windows updates.”

So even if your device is blocked from installing the latest Secure Boot certificate, it will continue to work properly, other Windows updates will continue to work, and your Secure Boot version will continue to protect against known vulnerabilities. It’s just future vulnerabilities that users affected by this issue will need to be aware of.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Many users may not be aware of issues until they need to use Secure Boot, so the silver lining in Microsoft’s warning is that now is the perfect time to check if your Secure Boot is working properly.

## How to check Secure Boot is up to date

To check if you are using the latest Secure Boot certificate, take the following steps:

- Open the Windows Security app using the search bar
- Navigate to the Device Security dashboard using the menu on the right hand side
- Look at the Secure Boot section, and check for the following messages:

 ![The Windows Secure boot section on the Device Security dashboard, showing that Secure Boot is working properly.](https://cdn.mos.cms.futurecdn.net/HyNkMVJGXkiKSxMuxhgDcT.png) 


- **"Secure Boot is on"**

If you see this message, Secure Boot is likely working properly. However, this does not display your certificates’ current state. Microsoft has been rolling out an update to show if your Secure Boot is running on the latest certificate, so make sure your don't have any pending Windows updates.

 ![The Windows Secure boot section on the Device Security dashboard, showing that Secure Boot is affected by a known issue but can be updated by the OEM.](https://cdn.mos.cms.futurecdn.net/zjzGsDEjkxDUWRwcCydtnh.jpg) 


- **“Devices in this group are affected by a known issue.”**

Devices with this message will likely be able to install the latest certificates once a firmware update has been issued by your OEM. Check your OEM update channel for availability.

 ![The Windows Secure boot section on the Device Security dashboard, showing that Secure Boot is not supported for the latest Secure Boot certificate.](https://cdn.mos.cms.futurecdn.net/R3cbzEW7HbsAAKce4H9DPn.jpg) 


- **“Secure Boot is on, but your device does not support the automated Secure Boot certificate update due to hardware or firmware limitations.”**

Devices with this message may no longer be supported by your OEM, or the OEM might no longer be able to provide the firmware updates needed. Microsoft recommends checking your OEM’s Secure Boot support page to confirm whether your device is out of support.

Via *WindowsLatest*

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Benedict Collins](https://cdn.mos.cms.futurecdn.net/jEvqGv8wvH7PWZ4XPURyyB.jpg)

Benedict is a Senior Security Writer at TechRadar Pro, where he has specialized in covering the intersection of geopolitics, cyber-warfare, and business security.

Benedict provides detailed analysis on state-sponsored threat actors, APT groups, and the protection of critical national infrastructure, with his reporting bridging the gap between technical threat intelligence and B2B security strategy.

Benedict holds an MA (Distinction) in Security, Intelligence, and Diplomacy from the University of Buckingham Centre for Security and Intelligence Studies (BUCSIS), with his specialization providing him with a robust academic framework for deconstructing complex international conflicts and intelligence operations, and the ability to translate intricate security data into actionable insights.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
