---
title: Hobbyist turns $45 USB-C hub into a working Nintendo Switch 2 dock by patching
  its firmware — console’s proprietary handshake needs about 540 bytes of code to
  answer
source_url: https://www.tomshardware.com/uk/video-games/nintendo/hobbyist-turns-usd45-usb-c-hub-into-a-working-nintendo-switch-2-dock-by-patching-its-firmware-consoles-proprietary-handshake-needs-about-540-bytes-of-code-to-answer
source_site: Tom's Hardware
source_slug: toms-hardware
description: A hobbyist patched a Cable Matters USB-C hub’s firmware so the Nintendo
  Switch 2 accepts it as a dock for TV mode and HDR.
image: https://cdn.mos.cms.futurecdn.net/ESNdAUX4LtVoZ3CVgpuXtT-1461-80.jpg
published: '2026-11-12T00:00:00Z'
scraped_at: '2026-11-13T01:48:30Z'
categories:
- Technology & Software
- Hardware
people:
- Tom
locations:
- USB
organisations:
- Cable Matters
- Get Tom's Hardware
- Google News
- HDMI
- HDR
- I2C
- Nintendo
- Nintendo’s
- Realtek
- Shane Downing
- Tom’s Hardware
- VIA Labs
- VL
- VRR
- WITRN
- mkopec
---

![A black Cable Matters USB-C hub with a short flat cable on a wooden table.](https://cdn.mos.cms.futurecdn.net/ESNdAUX4LtVoZ3CVgpuXtT-1461-80.jpg)

A hobbyist going by mkopec turned an approximately $45 Cable Matters USB-C hub into a working Nintendo Switch 2 dock, using only about 540 bytes of code to mod the firmware. That mod lets the hub masquerade as an official dock, as mkopec detailed in a blog post.   
The edited firmware replies to Nintendo’s vendor messages and returns the same identity as the official dock, and makes TV mode work, which was not the case with the hub’s stock firmware. A separate fix with minor firmware rewriting also corrects washed-out HDR over HDMI, a nice bonus.

The modder, who writes that “Nintendo went in a proprietary direction (as they so often do),” decided to modify the hub’s firmware to make a working travel dock, as Nintendo’s official dock can be bulky. Unlocking the additional functionality did not come with a noticeable cost, as the hub “still works normally with my PC and my phone.” Grabbing an off-the-shelf USB-C hub and turning it into something more is quite the trick.

The stock hub has no problem charging the console, but it shows no picture, even though it negotiates both power and DisplayPort Alt Mode. Capturing the official Switch 2 dock’s traffic with a USB Power Delivery (USB-PD) sniffer, the modder found that it advertises two Standard or Vendor IDs: one for DisplayPort and one for Nintendo’s own mode.

The console enters Nintendo’s mode first, then DisplayPort, and, once DisplayPort is configured, it sends Nintendo’s vendor messages. This is the exchange of proprietary messages for negotiation, although the company told us last year that it “does not have any intention to hinder or invalidate legal third-party dock compatibility.”

The modification only required adding about 540 bytes to a firmware of just 32 KiB. The Cable Matters 7-in-1 triple display hub, like most, is simply an amalgamation of separate, specialized chips, in this case: a VL103 as the USB-PD controller, a VL817 USB hub chip for the USB ports, an RTD2142 DisplayPort Multi-Stream Transport chip for the DisplayPort-to-HDMI function, and XT25F16B flash memory chips. The VL chips are from VIA Labs, the RTD2142 is from Realtek, and the stock hub reports VIA’s vendor ID, which is an identity that needed to be changed for this mod.

The modder first used the WITRN K2 inline USB-PD sniffer on the official dock. Then, it was a matter of dumping the VL103’s firmware with the vli plugin of fwupd, the Linux firmware update tool, before flashing the VL103 with the changes over USB and through the VL817.

Changes were made incrementally, with seven versions in all, starting with answers to Nintendo’s discovery, mode entry, and echo commands, then an update to power delivery to offer 15 V at 2.8 A like the dock, changing the reported vendor ID to Nintendo’s, masquerading entirely as the official dock and getting TV mode working, and finally a full sequence match that removed a pause of about 3 seconds.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

The process appears to contradict claims two accessory makers made to *The Verge* that the dock check uses encryption with a dedicated chip, as, in this case, copied identity data and fixed replies were sufficient.

Getting TV mode to work would have already been an accomplishment worth celebrating, but the modder took it further: the picture over HDMI was washed out with HDR turned on, and it was simply a matter of narrowing down the cause. The end theory was a mistake in how the hub’s AVI InfoFrame signaled BT.709, the standard dynamic range color space, instead of HDR’s wider BT.2020.

The theory was confirmed by a 108-byte patch to the RTD2142’s firmware, flashed with flashrom over I2C carried on the DisplayPort AUX channel through the same USB-C cable, which marks the signal as BT.2020 whenever HDR is in use. One third-party dock’s firmware contains a debug string, “switch2 color space patch,” which suggests this is a known issue. HDR through the hub’s own DisplayPort port is still washed out.

Separately, the hub’s firmware has no variable refresh rate (VRR) support, but because the patched hub identifies as the official dock, the console now offers VRR. However, turning VRR on froze the DisplayPort picture, and HDMI remained at 60 Hz. In a separate Linux test, with the hub patched to advertise Adaptive-Sync and an EDID override in place, the screen went black as soon as the frame rate varied, so the feature was left off.

The modder’s post shares no code, patch files, or repository, although the method is well-explained. The USB ports and Ethernet weren't tested rigorously, and the post does not say which Switch 2 system version was used. The modder also doesn’t understand many of Nintendo’s commands, so the hub’s version replies are copies of the official dock’s, and unrecognized commands still get the hub’s stock reply.

That’s important because Nintendo’s system update 21.0.0 left some third-party docks charging but with no video output. While vendors provided updated firmware as a fix, the modder’s ad hoc solution has no vendor behind it, so would-be modders could end up on their own.



*Download the Tom's Hardware app for up-to-the-minute updates on* * iOS* * and* * Android**. Also follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Shane Downing](https://cdn.mos.cms.futurecdn.net/Zosi9VrDytS9FkgJiHvc69-140-80.png)

Shane Downing is a Contributing Writer for Tom’s Hardware, covering consumer storage, PC hardware, and AI.
