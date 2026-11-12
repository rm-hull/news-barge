---
title: Apple’s HomeView Tries Face Authentication Without FaceID
source_url: https://www.wired.com/story/apples-homeview-tries-face-authentication-without-faceid/
source_site: Wired
source_slug: wired
description: Apple’s FaceID has long provided robust authentication. But for its smart
  home device, HomeView, the company is betting on new “person recognition” technology
  that has yet to be challenged in the wild.
image: https://media.wired.com/photos/6af4fdf535927e964a65305d/191:100/w_1280,c_limit/Security_Apple%E2%80%99s%20HomeView%20Won%E2%80%99t%20Have%20FaceID.%20It%E2%80%99ll%20Have%20Something%20Worse_v1.jpg
published: '2026-11-12T00:00:00Z'
scraped_at: '2026-11-12T19:51:46Z'
categories:
- Technology & Software
- Science
- Business & Entrepreneurship
people:
- HomeView
locations:
- Secure Enclave
organisations:
- Apple Watch
- Apple’s HomeView
- FaceID
- iCloud
---

Apple’s HomeView, which debuts on Friday, is a smart home device—think of it as a an iPhone-Apple Watch hybrid sitting on your counter—that can be personalized for up to six people and connected to each of their iCloud accounts. Using ambient face and voice data, it is designed to seamlessly switch between users while maintaining each of their privacy. You can ask HomeView about your schedule for the day and what movie your friend recommended in a text, but you’ll be stopped from asking about your roommate’s travel plans or her texts from last night. The feature doesn’t rely on one of Apple’s battle-tested biometric locks, like FaceID or TouchID, though. Instead, it uses new “person recognition” technology built off of an Apple architecture for securing sensor data.

This is a key departure for Apple. On the one hand, the company has still been very careful to think about security and privacy comprehensively. Not only does HomeView check for your face and voice before accessing your data from iCloud, it is also designed like an Apple Watch to check that your iPhone or iPad is on the same Wi-Fi network as the HomeView and has been recently unlocked (with FaceID or a PIN). On the other hand, expanding the architecture used to process biometric data and authenticate users creates more opportunities for mistakes and potential vulnerabilities. And when it comes to attempting to access users’ Apple data, both law enforcement and exploit brokers consistently go to great lengths to attempt to break the company’s on-device defenses.

FaceID is built for the use case where a person is staring at their device head-on from less than an arm’s length away. It provides reliable security that’s difficult to defeat because it stores your biometric data on a special, physically isolated chip known as the Secure Enclave—first introduced in 2013 for the iPhone 5s. The architecture is so robust that Apple also relies on the Secure Enclave as the foundation of a device’s entire encryption scheme. But Apple concluded that FaceID wasn’t the best fit for the HomeView, because it needs to bounce quickly between users and relies on AI processing, which can’t all be squeezed into the Secure Enclave.

As a result, HomeView uses Apple’s recently announced Secure Exclave (note the “x”) to handle the video and audio data the device uses to evaluate who is in a room at a given time. Apple says it has actually been laying the groundwork for the Secure Exclave for a long time—early versions of the architecture were already in place for the iPhone 16 and 17 and MacBook Neo. Instead of being an entirely separately chip, the Secure Exclave is a dedicated, memory-protected space in recent Apple processors. It is in Apple’s latest S11 chip for Apple Watch Series 12 and Apple Watch Ultra 4, as well as the A20 Pro chip for iPhone 18 Pro and iPhone Duo.

Even though the Secure Exclave isn’t based on the tried and true Secure Enclave technology, Apple argues that it is robust and expands the company’s ability to secure a range of features, including improving the security of existing mechanisms. In a blog post on Thursday, the company even goes into some detail about how it used the mathematical technique known as formal verification to vet the “microkernel” designed for the Secure Exclave.

“This work both benefits our newest features and strengthens the security of features we already ship, such as ‘Hey Siri’ detection,” the company writes in a blog post. “Our goal is to keep ambient sensor data secure even against highly sophisticated attacks.”

HomeView also uses the Secure Exclave to govern the indicator light that tells users when their camera or microphone is active. The MacBook Neo uses the Exclave in this same way, though only to indicate when the camera is active, not the microphone. The goal is to isolate this process and the chain of command governing it to make it even more difficult for attackers to try to disable an indicator light when it should be on or stop it from coming on in the first place.

The HomeView’s “person recognition” technology is simply not as comprehensive as FaceID, though, and it is possible that the technology is more susceptible to reconstructed 3D depth map attacks—and potentially voiceprint attacks—than FaceID.

Of course, you don’t have to have a HomeView in your house. Or if you do, you can use it on guest mode or a less involved “personalized” mode that only incorporates things like your playlists for other users to access as well and doesn’t access calendar or Messages data. But as Apple forges deeper into AI integration, HomeView’s departure from FaceID provides insight into the scale of the changes Apple is planning.

*Updated 11/12/2026 at 11:35 am ET to clarify when the MacBook Neo indicator light is verified by the Secure Exclave.*
