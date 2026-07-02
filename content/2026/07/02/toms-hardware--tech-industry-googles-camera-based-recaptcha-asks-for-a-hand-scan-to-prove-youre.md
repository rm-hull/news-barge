---
title: Google testing controversial webcam-based reCAPTCHA that asks for a hand scan
  to prove you're human — testers beat it with a stock photo
source_url: https://www.tomshardware.com/tech-industry/googles-camera-based-recaptcha-asks-for-a-hand-scan-to-prove-youre-human
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-02T10:51:31Z'
published: '2026-07-02T00:00:00Z'
description: The experimental hand-gesture check maps 21 points of your hand.
image: https://cdn.mos.cms.futurecdn.net/ja6KC8oV8j6EJwxEq8uCj-1920-80.jpg
---

![Razer Blade 18 (2026)](https://cdn.mos.cms.futurecdn.net/ja6KC8oV8j6EJwxEq8uCj.jpg) 

Google is testing a reCAPTCHA check that switches on a user's camera and asks them to wave or hold up an open palm, mapping 21 coordinates of the hand to decide whether a real person is present. The experimental method, which is rolling out as a limited test, was defeated within days by testers who fed a static stock photo of a hand through the OBS Virtual Camera and passed with no live person, no video, and no AI involved.

The check sits inside Google Cloud Fraud Defense, the platform behind reCAPTCHA on login screens, sign-up forms, and checkout pages. It’s meant to catch what the older challenges increasingly miss, such as automated account creation and credential stuffing.

When the challenge triggers, the browser requests camera permission and prompts the user through a short gesture. Google’s machine-learning model records a brief video and extracts hand-landmark data covering 21 finger and knuckle points, using the same landmark scheme that powers its MediaPipe hand-tracking tools.

Google's documentation states that the footage is deleted once verification completes, that no audio is recorded, and that the video is never tied to a user's identity or shared with third parties. The same page adds that any data collected is used and stored under the Google Privacy Policy, so it’s not entirely clear which is true or what data is collected. Users who can’t perform the gestures fall back to the existing visual and audio puzzles, and the feature is optional for now. The gesture check doesn’t retire those older challenges, but instead layers a camera-based biometric step on top of them.

Following its launch, it didn’t take long for the Internet to get around the new method. Using nothing but a stock image of a person waving into an OBS Virtual Camera, testers pointed reCAPTCHA at that virtual feed and cleared the challenge after a few adjustments to the image position. Because the whole sequence can be driven by a short script, gesture reCAPTCHA in its current state appears to do nothing but add friction for ordinary users while offering little resistance to an attacker.

😁 Google's new captcha asks you to show hand gestures on your webcam, but people are already bypassing it with stock photosThis system was supposed to be "the best way to tell humans from AI."Here we are again. [https://t.co/Q3oK6yXwmY](https://t.co/Q3oK6yXwmY) pic.twitter.com/RwR3mHnTsfJune 29, 2026


reCAPTCHA has been struggling with similar challenges for years. In 2024, researchers reported a 100% success rate against reCAPTCHAv2 using off-the-shelf object-detection models, and last year, an OpenAI agent was recorded clicking through a Cloudflare “I am not a robot” check while narrating each step. The hand-gesture test raises the stakes for users since a hand scan is biometric information — regardless of whether Google promises it isn’t harvesting your data.

Less than two weeks ago, Cloudflare, Google, Mozilla, and Microsoft jointly proposed Private Access Control Tokens (PACT), a cryptographic scheme meant to replace CAPTCHA challenges with a privacy-preserving proof that a request comes from a legitimate client. The proposal comes on the back of findings that roughly 58% of global HTTP requests come from bots, a threshold Cloudflare hadn’t expected before 2027.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

“We can build a better solution that maintains strong privacy and provides a much less annoying experience for real humans using the web,” said Bobby Holley, CTO for Firefox at Mozilla, in the announcement.

Google hasn’t said whether the hand-gesture test will graduate to general availability.

  


*Follow**Tom's Hardware on Google News**, or**add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Luke James](https://cdn.mos.cms.futurecdn.net/C4FAi2KzwaGLUrBqzX5aBM.png)

Luke James is a freelance writer and journalist. Although his background is in legal, he has a personal interest in all things tech, especially hardware and microelectronics, and anything regulatory.
