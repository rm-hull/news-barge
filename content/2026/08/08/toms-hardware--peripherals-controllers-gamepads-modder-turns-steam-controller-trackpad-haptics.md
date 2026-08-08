---
title: Modder turns Steam Controller trackpad haptics into stereo speakers with custom
  HID tool — Wired connection transmits 16-bit audio that sounds surprisingly full
source_url: https://www.tomshardware.com/peripherals/controllers-gamepads/modder-turns-steam-controller-trackpad-haptics-into-stereo-speakers-with-custom-hid-tool-wired-connection-transmits-16-bit-audio-that-sounds-surprisingly-full
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-08-08T13:08:45Z'
published: '2026-08-08T00:00:00Z'
description: And it works with any file.
image: https://cdn.mos.cms.futurecdn.net/afqXySTxPCEC6t4PTDCq7m-1920-80.jpg
---

![Valve Steam Controller](https://cdn.mos.cms.futurecdn.net/afqXySTxPCEC6t4PTDCq7m.jpg) 

Valve's second-gen Steam Controller has been a major hit with the community thanks to the company's open approach to its hardware. Modders have already used the haptic motors inside to move it across a desk and charge automatically, while others have built their own open-source pucks. Now, a new project from *Pixel1011*,**called "Steam Haptics Player," can turn these motors into a stereo speaker capable of playing music both wired and wirelessly.

![Want you gone on a Steam Controller - YouTube](https://img.youtube.com/vi/xfg437QMPSw/maxresdefault.jpg) 

For context, the Steam Controller doesn't have a speaker; there are two linear actuators under each trackpad that vibrate to provide haptic feedback. Previous projects have leveraged these components to make the controller vibrate in a certain way. Since vibrations are the basis of sound, Valve itself built a secret easter egg into the controller that randomly makes it do a Wilhelm scream when dropped from certain heights.

Pixel 1011 discovered that the haptic motors inside can be targeted with low-level HID (Human Interface Device) feature commands using HIDAPI. As such, Steam Haptics Player takes an audio file, downsamples it through FFmpeg, splits it into chunks of a PCM stream, and sends those packets directly to the controller, bypassing high-level software like Steam Input. The controller's firmware then feeds this raw data to the motors, at which point they vibrate to produce sound.

Because of the DIY nature of this process, bandwidth is an issue, especially wirelessly, since the puck isn't designed to carry audio data over its radio signal. This means the audio has to be compressed, and there's a limit to the overall quality the motors can transmit — 8-bit 8kHz (μ-law) over the puck and 16-bit 8kHz PCM over a wire.

Still, the 16-bit audio is enough to produce a surprisingly loud and balanced result that can deceive you as if it's coming from a speaker. The video at the start features Pixel1011 playing the song "*Want You Gone*" from the end credits of* Portal 2, *and you can hear the quality for yourself. There's a genuine low-end that you would never expect from a jerry-rigged setup like this, even if it's sitting on top of a towel on a flat surface to give it its best chance.

The wireless audio quality is rough in comparison; it crackles and pops and even cuts off in between because of the bandwidth limitations. *Pixel1011* is using 8-bit mu-law companding here, which actually offers dynamic range similar to 14-bit audio while keeping the byte footprint of an 8-bit stream. Even through this compression, the puck is struggling, but the fact that this is even possible is still very impressive, and perhaps there's room for improvement down the line.

![Still Alive on a Steam Controller - YouTube](https://img.youtube.com/vi/iLLmQzjEhYs/maxresdefault.jpg) 

You can try Steam Haptics Player yourself on your own second-gen Steam Controller with pretty much any audio file in any format. Just download the archive from the GitHub repo, install FFmpeg (for transcoding, if you don't have it already), and run the program via a PowerShell window in the original directory. Detailed steps are on the linked GitHub page, but we don't know how this affects the controller's battery life. Just don't go all out with your Spotify playlist on these haptic motors.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Hassam Nasir](https://cdn.mos.cms.futurecdn.net/SxxNFHt95eGK37mKPhJpdZ.jpg)

Hassam Nasir is a die-hard hardware enthusiast with years of experience as a tech editor and writer, focusing on detailed CPU comparisons and general hardware news. When he’s not working, you’ll find him bending tubes for his ever-evolving custom water-loop gaming rig or benchmarking the latest CPUs and GPUs just for fun.
