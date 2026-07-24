---
title: '''An agent could be instructed to dox a former romantic partner'': experts
  explain why OpenAI''s ''mind-blowing'' cyberattack is truly worrying — and how AI
  could threaten us all, not just businesses'
source_url: https://www.techradar.com/ai-platforms-assistants/openai/science-fiction-that-happened-experts-explain-why-openais-mind-blowing-cyberattack-should-worry-us-all
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-24T17:48:07Z'
published: '2026-07-24T00:00:00Z'
description: This might be our first true glimpse of how dangerous AI could be in
  the future in terms of making hacks much more commonplace.
image: https://cdn.mos.cms.futurecdn.net/e9daFEAHRRRq7beMXHAcHR-2560-80.jpeg
---

![Businessman staring at laptop with frightened face in the dark](https://cdn.mos.cms.futurecdn.net/e9daFEAHRRRq7beMXHAcHR.jpeg) 

Hugging Face is probably not a name you'd heard before this week, but you likely caught the big news about OpenAI's model escaping its sandbox and to launch a cyberattack on the company.

In short, Hugging Face — which is kind of like the equivalent of GitHub for the machine learning (AI) world — was the victim of an AI agent that OpenAI was testing in terms of its ability to pull off exploits.

So how exactly did this happen? And what does it mean for the future of online security given the development of increasingly advanced AI agents? In this article I'll answer those questions, and explore some of the issues this event has thrown up, including the security threats posed by AI not just to companies, but to individuals.

## How did this even happen — why didn't OpenAI have safeguards to stop the AI?

 ![The ChatGPT-5 logo appears on a smartphone screen, and the OpenAI logo is the background.](https://cdn.mos.cms.futurecdn.net/Z2mw4pRucu3aZMfo4fgo3P.jpg) 


As you might expect, OpenAI did have safeguards in place, but the model managed to break through them.

The scenario was that OpenAI ran a controlled experiment using GPT‑5.6 Sol and an "even more capable pre-release model" to see how they fared on ExploitGym, which is a benchmark test that challenges AI to successfully exploit known security vulnerabilities.

In this security test, the model was placed in a sandbox, a "highly isolated environment" from which the AI shouldn't have been able to gain access to the internet at all. But the pre-release AI — which had its guardrails turned off, as OpenAI believed it to be safely imprisoned — craftily decided to cheat, found a way to escape its sandbox, and actioned exploits to breach Hugging Face (where the AI reasoned that it might find the answers to crack the ExploitGym tests).

## Why is this a big worry?

 ![People gathered around a laptop on a desk looking very concerned](https://cdn.mos.cms.futurecdn.net/vFpLfsX25upmV7bauzqSZ6.jpg) 


It's a major concern simply due to the level of smarts exhibited by the AI. As OpenAI explained, the model "chained together multiple attack vectors" and used "stolen credentials and zero-day vulnerabilities to find a remote code execution path on the Hugging Face servers."

Sign up for breaking news, reviews, opinion, top tech deals, and more.

This was no mean feat, and Clement Delangue, CEO of Hugging Face, posted on X to say that it was "quite mind-blowing that all of this happened autonomously!"

In a blog post, Hugging Face observed that: "The campaign was run by an autonomous agent framework executing many thousands of individual actions across a swarm of short-lived sandboxes, with self-migrating command-and-control staged on public services."

The attacked was deemed so serious, it was reported to law enforcement agencies. As Simon Willison, a cocreator of web framework Django, pointed out in a blog post: "This was a sophisticated attack," further explaining that "Chaining together multiple attack vectors is exactly the kind of thing these new models can do, where previous generations of models might have failed."

The headline of Willison's post sums it all up rather neatly: "OpenAI's accidental cyberattack against Hugging Face is science fiction that happened."

The Django co-creator is also quick to dismiss conspiracy theories that this is somehow a marketing stunt by OpenAI to prove how advanced its AI models are.

## The future of hacking?

 ![A robot's hand typing on a laptop keyboard](https://cdn.mos.cms.futurecdn.net/6t9Lsf3QWte55CdyiDs97L.jpg) 


What should also be noted is the distinction between finding vulnerabilities, and being able to actively exploit vulnerabilities. AI being involved in the former could be very useful for bolstering security, but as for the latter — well, this Hugging Face incident is very much a clear illustration of why the makers of these models need to tread very carefully indeed.

While this was a 'white hat' (ethical) experiment, albeit one that went alarmingly awry, with real-world consequences, what happens when AI models start to become even more sophisticated along these lines — and criminals get hold of them?

There are obvious dangers in terms of the automation of attacks to make them far more regular occurrences, and the lowering of the bar in terms of the skills needed to be a successful hacker.

Dan Schiappa, President of Technology & Services at Arctic Wolf (responsible for threat-detection platform Aurora), warns: "Security teams should view this as a preview of what's ahead. As AI continues to lower the barriers to sophisticated cyber activity, organizations will need broad, deep visibility across their environments and the ability to investigate and respond at machine speed."

The ability to "respond at machine speed" is a hint at using AI for defense against AI bad actors, and that's another interesting facet of the Hugging Face incident. Simon Willison observes that Hugging Face was "unable to turn to OpenAI's models to help them fend off the attack", and that: "The frontier models [cutting-edge AIs] we have access to are increasingly being constrained in how much they can help us protect our software, heavily influenced by the US government's ongoing threat of export controls."

AI-driven attacks will doubtless be aimed at businesses and organizations, but could also be leveraged on a personal basis. Karolis Arbaciauskas, who is Head of Product at cybersecurity firm NordPass, tells us: "We don't need a nation-state actor or a Bond villain for this to go wrong. The most common emerging threats will likely be more mundane. For example, an [AI] agent could be instructed to dox a former romantic partner or settle an online grudge by hacking and stealing personal data, such as embarrassing photos or credit card details."

Arbaciauskas adds: "AI models have become dangerously skilled at identifying software vulnerabilities. They've mastered every human hacking technique, from phishing to brute forcing. The difference is they can do it much faster than humans.

"I don't believe that we can patch software fast enough to keep up, so we must at least shield ourselves against the most obvious entry points. Encryption, strong unique passwords, passkeys, and multi-factor authentication (MFA) have never been more critical than they are right now."

The major AI firms are always talking about guardrails and safety, but it now seems like we should be thinking a *lot* harder about how more highly evolved AI models are going to fit into the future of cybersecurity — and how we can avoid a world where the danger of being hacked becomes a far more commonplace prospect, which is very much the biggest worry of all.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![An Apple MacBook Air against a white background](https://cdn.mos.cms.futurecdn.net/LocVgRosBUWfJzDitFzhKR.png) 

➡️ **Read our full guide to the best laptops1. Best overall:**

Apple MacBook Air 13-inch M5**2. Best budget:**

Apple MacBook Neo**3. Best Windows 11 laptop**

Microsoft Surface Laptop 13-inch**4. Best thin and light:**

Lenovo Yoga Slim 9i**5. Best Ultrabook**

Asus Zenbook S 16

Darren is a freelancer writing news and features for TechRadar (and occasionally T3) across a broad range of computing topics including CPUs, GPUs, various other hardware, VPNs, antivirus and more. He has written about tech for the best part of three decades, and writes books in his spare time (his debut novel - 'I Know What You Did Last Supper' - was published by Hachette UK in 2013).

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
