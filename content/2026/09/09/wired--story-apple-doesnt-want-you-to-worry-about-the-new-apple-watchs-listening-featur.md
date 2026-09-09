---
title: Apple Doesn’t Want You to Worry About the New Apple Watch’s Listening Features
source_url: https://www.wired.com/story/apple-doesnt-want-you-to-worry-about-the-new-apple-watchs-listening-features/
source_site: Wired
source_slug: wired
scraped_at: '2026-09-09T22:30:04Z'
published: '2026-09-09T00:00:00Z'
description: The new Apple Watch includes several “intelligent” listening features
  that have privacy and security baked in. But the protections can’t change the facts
  of what the tools do.
image: https://media.wired.com/photos/6aa1b207ccc1bba18de2d004/191:100/w_1280,c_limit/GettyImages-2293832136.jpg
---

The new Apple Watch Series 12 and Ultra 4 come not just with better fitness tracking and upgraded noise reduction, but also a whole new way to listen.

Apple announced on Wednesday that the two smartwatches come with four opt-in “audio intelligence” tools that are powered by audio gathered by the watches’ microphones. They include sound and music recognition, a conversation recap feature, and “Live Rewind” so a user can see a transcription of anything that was said in their environment in the previous 15 seconds.

Seemingly wary that the features could make it feel like the walls have ears, Apple is emphasizing that all of them are built to prioritize privacy and security using the extensive infrastructure the company has developed to protect its other Apple Intelligence and Siri services. As more and more of these types of features debut, though, the audio intelligence announcements are a reminder that AI-powered tools are becoming increasingly universal in all areas of computing and life.

“These features do not create or store audio recordings, and raw audio used for processing is completely inaccessible to the operating systems, apps, the user, or Apple,” the company wrote in a report shared with WIRED.

The new Apple Watch features are designed to process as much data locally on devices as possible, so potentially sensitive data doesn’t go to the cloud. Sound Recognition, for example, alerts users about sounds in their environment—including doorbells, sirens, alarms, or, say, a baby crying—without sending any data off the watch. The tools that do send information out to the cloud preprocess the data so it isn’t raw audio files, then use Apple’s Private Cloud Compute infrastructure.

Apple emphasizes that its on-device capabilities for Apple watches have expanded thanks to the company’s new S11 chips. The chips include a special memory-protected space that Apple calls the Secure Exclave. Designed specifically for sensor data, the exclave is an isolated buffer that is inaccessible to the rest of the operating system where Apple Watch can hold and process audio data in a protected space.

A new Shazam feature “listens” for music and will generate a signature of a song that is stored in the Secure Exclave. If the user navigates to Shazam to find out what the music is, the tool will send that signature—not an audio file—to Shazam’s servers for identification. (Shazam is an Apple-owned service.) If the user doesn’t prompt to identify the music, or as soon as they do, the special signature is “immediately” deleted from the watch.

The recap feature, known as Siri Recap, can be set to be on all the time and generate recaps of any substantive conversation, or it can be given a schedule to listen in at certain times during the day. A dedicated AI model determines when speech is occurring without recording or transcribing any data. If it detects a conversation, audio goes into a protected buffer within the Secure Exclave on the Apple Watch, the watch encrypts it, and then transmits it using Apple’s special secure Bluetooth pairing to the Secure Exclave on a user’s iPhone. Then the audio is immediately deleted from the Apple Watch.

The iPhone uses local speech recognition and language models on-device to transcribe the audio and then generate a minimal version of the transcript that removes nonessential elements like extra words and repeated phrases. Then the raw audio is immediately deleted from the iPhone as well. The last step on the iPhone is a safety model that “screens the text to omit potentially harmful terms,” according to Apple. From there, the distillation of the conversation is encrypted, and the iPhone sends it out to Private Cloud Compute.

“Contextual information is also sent to improve summary quality,” Apple says. “For example, Now Playing data helps the model understand that speech may have originated from music or a podcast. Calendar data can help generate accurate titles of summaries. High-level location labels such as home, work, and school, along with locality information such as city, state, and country, add context to the summarization. Point-of-interest categories like ‘grocery store’ or ‘park’ may also be included. Precise location and specific points of interest are not included.”

Finally, the condensed transcript is run through Apple’s foundation models in Private Cloud Compute to create a title and summary, which is then encrypted and sent back to the iPhone and Apple Watch. Apple says that Siri Recap is built to remove sensitive information like financial data, ID numbers, or other personal identifiers from its summaries.

The Live Rewind features that lets users ask for a text version of the last 15 seconds of what was said in their environment uses the Secure Exclave buffer to continuously hold audio on a rolling basis, where old sound is replaced by new audio and doesn’t amass. To get a transcript through Live Rewind, users must double-press the Apple Watch’s Digital Crown each time. Once activated, the watch sends the last 15 seconds of buffered audio from its Secure Exclave to the Secure Exclave of the paired iPhone. If the iPhone is not available, the transfer will fail, and the audio will automatically be deleted. (Siri Recap has similar fail-safes if the transfer from the watch to the iPhone fails.) If the transfer goes through, the iPhone does on-device speech-recognition processing to make a transcript and then deletes the audio and sends the text back to the Apple Watch. Users read the transcript and then can discard it or save it in the Siri app.

It's hard to ignore that, in spite of all of these data protections, anyone wearing a new Apple Watch could be siccing “audio intelligence” on, say, your intimate vent session, private family update, or accidental slip-up about a secret. To try to mitigate blatant privacy violations, Apple says that the watch produces an audible chime when a watch owner initiates a Live Rewind transcript to alert other people in the area—even if it is on silent mode or paired with headphones. And the features are built to omit or filter out potentially identifying information about speakers. But the sheer scope and breadth of the tools is extremely noteworthy.

Apple has invested significantly over many years in its secure AI processing infrastructure—far beyond what almost any other company has done. The new audio features highlight, though, that over time the AI attack surface, or sheer quantity of services and systems that could include flaws or mistakes and be attacked, is growing faster than the implications can be fully understood.
