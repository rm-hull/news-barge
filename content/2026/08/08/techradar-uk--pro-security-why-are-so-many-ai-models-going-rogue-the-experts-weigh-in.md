---
title: Why are so many AI models going 'rogue'? The experts weigh in
source_url: https://www.techradar.com/pro/security/why-are-so-many-ai-models-going-rogue-the-experts-weigh-in
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-08T13:09:03Z'
published: '2026-08-08T00:00:00Z'
description: AI models are breaking free of testing at unprecedented rates
image: https://cdn.mos.cms.futurecdn.net/PAztEScphfxGJfYno5NjrL-2560-80.jpg
---

![A robot standing thoughtfully in front of a giant digital display with code on it](https://cdn.mos.cms.futurecdn.net/PAztEScphfxGJfYno5NjrL.jpg) 

Over the past month, it seems like every frontier model has broken free of its constraints and launched a devastating attack against one or more other companies.

One of OpenAI’s models escaped a testing sandbox and launched a very real attack against AI and machine learning company Hugging Face. Just days later, Anthropic revealed that multiple variants of its Claude model also escaped a sandbox that wasn’t properly sealed and began attacking the enterprise infrastructure of three companies.

Now, Meta has revealed that one of its models attacked another company’s infrastructure during testing. The accident has been pinned on a misconfiguration that allowed the model to access the internet. So why have so many incidents happened in such a short space of time?

## Why are models escaping their sandbox?

In the cases of Anthropic and Meta, their models were being tested by a third party company called Irregular. Anthropic’s AI model was taking part in a "Capture the Flag" exercise, where the model’s raw offensive capabilities were tested without the usual safeguards. But the sandbox was left connected to the internet. A similar error to Meta’s own accidental escape.

During the OpenAI incident, the company was testing two versions of GPT‑5.6 Sol using the ExploitGym benchmark. Unfortunately, the AI models performed better than expected - chaining multiple attack vectors, stolen credentials, and zero-day vulnerabilities.

The main reason these models are escaping their testing environments is because they are designed to do exactly that. These AI models act like a massive team of highly-trained cybersecurity experts hunting for vulnerabilities and exploits. But what would take a team of humans days or weeks to accomplish can be done in hours, or even minutes, by these AI models.

It’s no wonder thousands of employees from AI firms are calling for a pause on the development of the technology, and Congress is considering an AI kill switch.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

### Expert perspectives on AI escapes:

## OpenAI

- **Nathaniel Jones VP, Security & AI Strategy, Darktrace:**

*What makes the OpenAI and Hugging Face incident important is that the models did not need malicious intent to cause harm. They were given the legitimate goal of solving a cybersecurity benchmark and found an unexpected route to the answers, escaping their test environment and compromising another organization in the process. From the models’ perspective, this appears to have been an effective solution to the task.*

*The AI's actions challenge the assumption that giving an agent a legitimate goal will produce legitimate behavior. As models become capable of pursuing objectives over longer periods, developers need to define not only what success looks like, but also which methods and boundaries remain unacceptable in reaching it. Those limits must also be enforced by the surrounding infrastructure, rather than relying on the model to respect them.*

A single action by an agent may appear acceptable but as this incident shows, models are now capable of long, complex chains of reasoning and action that add up to a harmful outcome.


*Security teams need to consider the AI systems operating in their own businesses as these capabilities rapidly evolve. Right now, many security systems focus on single actions. A single action by an agent may appear acceptable but as this incident shows, models are now capable of long, complex chains of reasoning and action that add up to a harmful outcome. Teams need a mindset shift to understanding AI agent behavior in its entirety, including the outcome it is working towards, in order to safeguard it.*

*Hugging Face's response also exposed a second tension. The company reportedly needed a Chinese-developed open-weight model because commercial models would not process genuine attack material. Its nationality is less important than the operational lesson that safeguards that cannot distinguish an attacker from an authorized investigator may constrain defenders more than adversaries.*

*OpenAI and Hugging Face deserve credit for investigating this together and discussing it publicly. Other AI developers should study it closely.*

## Anthropic

- **Dr. Ilia Kolochenko, founder of global cybersecurity company ImmuniWeb:**

*This seems to be quite an unimpressive marketing move from Anthropic in response to the OpenAI / Hugging Face drama, which attracted a lot of attention from all over the world recently.*

*Operationally, it appears that due to the progressive deterioration of the quality of training data, new AI models are getting dumber. Cheating and breaking the law, instead of accomplishing specific tasks, is certainly not an indicator of intelligence. Given that organizations and companies of all sizes now vigorously undertake all possible measures to protect their data from being exploited for AI training purposes, AI companies face a huge shortage of the high-quality and current data they so desperately need. Ultimately, frontier models are trained on synthetic, low-quality or even malicious and poisoned data, undermining their so-called intelligence. The situation is unlikely to improve in the near future unless AI companies agree to pay a fair price for training data, but this will force most of them out of business.*

Given that organizations and companies of all sizes now vigorously undertake all possible measures to protect their data from being exploited for AI training purposes, AI companies face a huge shortage of the high-quality and current data they so desperately need.


*Contemporary AI agents and LLM models tasked with security testing can – and almost certainly will – go rogue when security controls or safeguards are insufficient. Powerful LLMs are unpredictable by design and thus virtually uncontrollable by humans. Therefore, using frontier AI models for security testing might be extremely costly from the legal viewpoint. Under the existing laws on both sides of the Atlantic, if an AI agent or any AI-powered app escapes its sandbox and causes damage to a third party, the operator of the AI model will likely be liable for all the damage caused. Excuses like “AI did it” do not currently exist in the eyes of the law, leaving AI vendors on the hook. Criminal prosecution, under a narrow set of circumstances, is also not excluded.*

*The same is true for the end-users of AI: even if your security testing tool is powered by a third-party AI model, your company will likely be fully liable if something goes wrong. You may then file a lawsuit against the AI vendor that you used, but here your chances to succeed in a court of law are tiny due to countless contractual disclaimers and limitations of liability that will likely be enforceable against you. Therefore, if you plan to use agentic AI for security testing – think twice and talk to your lawyers. Otherwise, you may start getting summons to court on a daily basis.*

## Meta

- **Alex Goller, Principal Solution Architect EMEA at Illumio:**

*The fact we've had similar situations happen three times now across the biggest AI players is simply ridiculous. We've seen guardrails intentionally loosened to test their limits – Meta's model didn't need to be clever to breach another company's systems.*

*The timing of conveniently finding the exact same problem either means it's a stunt or they weren't paying enough attention during testing. Either way, both answers are worrying.*

If the model has internet access, it's a bit like leaving the door open and being surprised when the cat walks out. What is concerning is that the testing infrastructure meant to prove these models are safe failed on a basic control issue.


*If the model has internet access, it's a bit like leaving the door open and being surprised when the cat walks out. What is concerning is that the testing infrastructure meant to prove these models are safe failed on a basic control issue.*

*Fundamental cybersecurity hygiene still matters, and a frontier AI model is only as secure as the environment it's operating in.*

*Organisations need visibility into what AI systems can access and how they interact with the wider environment, along with controls that contain the impact when an agent behaves unexpectedly. That means keeping a close eye on egress traffic, so it’s flagged immediately when an agent tries to open unexpected outbound communication patterns that are not required to achieve its original goal. In the best case this would have been contained proactively.*

*We need to define exactly what an AI agent is permitted to do, rather than relying only on instructions about what it shouldn't do.*

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Benedict Collins](https://cdn.mos.cms.futurecdn.net/jEvqGv8wvH7PWZ4XPURyyB.jpg)

Benedict is a Senior Security Writer at TechRadar Pro, where he has specialized in covering the intersection of geopolitics, cyber-warfare, and business security.

Benedict provides detailed analysis on state-sponsored threat actors, APT groups, and the protection of critical national infrastructure, with his reporting bridging the gap between technical threat intelligence and B2B security strategy.

Benedict holds an MA (Distinction) in Security, Intelligence, and Diplomacy from the University of Buckingham Centre for Security and Intelligence Studies (BUCSIS), with his specialization providing him with a robust academic framework for deconstructing complex international conflicts and intelligence operations, and the ability to translate intricate security data into actionable insights.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
