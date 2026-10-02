---
title: A Flaw in ChatGPT’s Mac App Could Have Let Hackers Grab Sensitive Data
source_url: https://www.wired.com/story/a-flaw-in-chatgpts-mac-app-could-have-let-hackers-grab-sensitive-data/
source_site: Wired
source_slug: wired
scraped_at: '2026-10-02T17:55:05Z'
published: '2026-10-02T00:00:00Z'
description: While the focus has been on AI agents’ hacking capabilities, a recently
  patched vulnerability in a ChatGPT app shows that AI software is itself an inviting—and
  vulnerable—target.
image: https://media.wired.com/photos/6abc2c32f3865c0127252ad0/191:100/w_1280,c_limit/GettyImages-2278945913.jpg
categories:
- Technology & Software
- Science
- Business & Entrepreneurship
people:
- Meta
- Patrick Wardle
- Shane Bauer
locations: []
organisations:
- ChatGPT
- Dots AI
- Muse AI
- Objective-See Foundation
- OpenAI
- Sea
- WIRED
---

Hardly a day goes by lately without news of AI agents autonomously hacking websites or AI tools being used by cybercriminals and scammers. But a recently patched vulnerability in the macOS version of OpenAI’s ChatGPT underscores the potential value to attackers of compromising AI software itself as these apps proliferate more and more.

The bug could have been exploited to essentially take over ChatGPT on a victim’s computer, giving an attacker access to all the chat logs and other data stored by the app, as well as interconnections like browser sessions. Discovered by researchers at the Objective-See Foundation, the vulnerability illustrates the deep system access and trust that AI platforms are afforded in order to work—and the target that this puts on their backs.

“Agents need a lot of access to do their job,” says Objective-See Foundation software analyst and longtime macOS researcher Patrick Wardle. “They are like the building manager who has access to the keys to all the rooms. So if they can be corrupted or subverted, that’s super problematic. It can mean that unprivileged code could then potentially have access to all the things.”

OpenAI publicly acknowledged the security flaw and fix in its system change log on September 25. “We continue to evolve our security practices, but recognize a need to move faster,” OpenAI spokesperson Shane Bauer told WIRED in a statement.

The ChatGPT macOS app includes multiple components that communicate with each other securely by checking for digital signatures. The idea is to confirm with these validity checks that both processes are OpenAI components and not outside, potentially malicious software making a request. And the system design goes so far as to require these signature checks at three layers of remove from the request, to ensure that malicious software isn’t somehow directing an OpenAI component to be a proxy and make a seemingly trusted request.

Objective-See Foundation researchers found, though, that there is a trusted component, a script interpreter, that would accept an untrusted script (or list of commands to run) and could then be manipulated to deliver this script into the main ChatGPT process. “They also check the parent and grandparent of that process, but the malicious script just spawns the script interpreter three times and then makes the request so it will satisfy the requirements,” Wardle says.

The vulnerability was “insanely trivial” to exploit, he adds, and his proof of concept only required about a dozen lines of code. In addition to accessing ChatGPT chat logs, the vulnerability could also be used to get ChatGPT to run commands for the attacker, such as accessing a browser or other sensitive applications, with the requests appearing as legitimate instructions issued by the OpenAI software.

Wardle will present analysis of a number of AI macOS application bugs at Objective by the Sea, an Apple-focused security conference in November.

He recently found a flaw, now patched, in the dictation feature of Meta’s new Muse AI assistant that could have been exploited by a local attacker to grab a mishandled authentication token and gain access to user data. And he says that he has already submitted a new vulnerability finding to OpenAI related to the integration between ChatGPT and the company’s new always-on Dots AI assistant. OpenAI is currently reviewing his report.

“AI companies are fixated on adding features right now,” Wardle says. “But as always, the more features, the broader the attack surface. So all of these companies need to be fully focused on security, and from what I can see, it still often seems like an afterthought.”
