---
title: '''Whatever you try to fix breaks things even more'': How to avoid the hidden
  dangers of AI code'
source_url: https://www.techradar.com/pro/whatever-you-try-to-fix-breaks-things-even-more-how-to-avoid-the-hidden-dangers-of-ai-code
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-18T19:00:42Z'
published: '2026-09-18T00:00:00Z'
description: Gabriela Moreira, CEO of Quint, explains how catching flaws early can
  limit AI code nightmares
image: https://cdn.mos.cms.futurecdn.net/XtCYe6fmkjnRuMpRFwTEbc-2560-80.jpg
---

![headshot of Gabriela Moreira — CEO, Quint](https://cdn.mos.cms.futurecdn.net/XtCYe6fmkjnRuMpRFwTEbc.jpg) 

You no longer need knowledge of advanced coding languages to build apps. AI has torn down the barriers to coding, making it as simple as describing what you want in plain English.

Or at least, it can appear that way. 

But coding isn't just about writing syntax. It's about systems architecture, understanding how people will really use a platform, and ensuring the right measures are in place to limit vulnerabilities. 

I spoke with Gabriela Moreira, CEO of Quint, about how people using AI tools to write code can better understand the associated risks and put in place early checks and processes to limit unmaintainable code and catastrophic bugs.

![headshot of Gabriela Moreira — CEO, Quint](https://cdn.mos.cms.futurecdn.net/FP39PVPSniApg5uLVNekkK.png) 

![Owain Williams](https://cdn.mos.cms.futurecdn.net/yLKEi5rn5TCTcqYsfAHXDf.jpg) 

## Can AI be trusted to write production-ready code without human oversight? If not, what makes AI-generated bugs distinct from human error?

Oversight is definitely needed, because AI exists to serve humans, and therefore humans need to tell AI what to do and evaluate its results. 

Now, which type of evaluation is the most adequate? You can read its code line by line or ship to production and monitor for problems, to talk about two extremes. Both of these are already techniques used to oversee code that might contain human error. 

The main differences that AI brings to the table are the amount of potentially wrong code that gets produced and the cognitive disconnection of any human to the elements of what gets produced. Code review and monitoring are both harder at this load scale and cognitive disconnection.

## Which core business systems are most vulnerable to AI coding flaws?

The ones that are harder to test, like concurrent and distributed systems, or any system with a high level of non-determinism where there are too many paths to consider. 

AI is a generation tool, which is only as good as our ability to decide if a generated solution is correct or not. If I have good tests, or some other kind of verification harness I trust, I can accept AI solutions with less risk. If a system is hard to test or verify, there might be too many blind spots where flaws can sneak in.

## What are the hidden operational and security risks of deploying AI-generated code without formal verification?

There’s no magical solution, and combining different strategies is the wisest thing to do.


Perhaps the best way to think about risk in 2026 is by considering the asymmetry: defenders must protect all parts of their code, while attackers may only find one vulnerability to cause huge damage. 

AI companies are already taking this asymmetry into account when they decided to give a model like Mythos only to companies in a program to secure themselves, before they land in the hands of potential attackers. 

Formal verification is probably the strongest tool we know that can fight this asymmetry, but there are still many challenges in the area that make it infeasible to verify all the code surface, and vulnerabilities can still be found in unverified components. There’s no magical solution, and combining different strategies is the wisest thing to do.

## Why is catching a design-level bug early in the process so important?

I’m extremely concerned about the design process involving mostly markdown files that cannot be compiled or executed.


The answer to this question before AI wrote the code was quite different: because rewriting code is very expensive and error-prone if you catch the bug after months of development instead. I don’t think this is a strong argument anymore. 

So, the new answer is: you are way more likely to find this problem in the scope of a design you can still reason about than after AI writes thousands of lines of code with the bug hiding in one of them. 

You could maybe notice the problem as you typed the code, thinking “wait, we didn’t consider this scenario!” But this is less likely to happen if AI wrote the code for you, so more careful design is important.

Developers are used to reasoning about possibilities and bugs while compiling and executing different versions of code, so I’m extremely concerned about the design process involving mostly markdown files that cannot be compiled or executed, or interacted with in any way other than reading.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## What simple checks, tools, and safety nets can dev teams put in place to verify AI code before it hits production?

First of all, tests! But tests that actually help with trust, not just any AI-generated test that makes some arbitrary assertions and has to be updated all the time.

I like to think about tests in terms of which behaviors they are exercising and which kinds of regressions they are preventing. If controlling the quality of tests becomes a challenge, formal models can help by either being a generator of scenarios to test or by validating that existing tests enforce interesting behavior.

Additionally, mutation testing is very helpful in measuring the quality of tests by how many different regressions they could catch.

## What level of human oversight do you recommend to balance development speed with code quality and reliability?

This depends so much on context and risks. The best I can recommend is to do whatever allows you to ship with enough confidence and to feel enabled to make software changes without fear of breaking what is already working.

The worst scenario is always to get hacked or leak other people’s data. The second worst is to get to a state where there are a lot of things wrong with the software, but whatever you try to fix results in breaking things even more, so it gets stuck in a bad state.

I think it’s quite easy for AI-generated code to end up in this state. Interestingly, I think the way to escape it is very similar to how we handled legacy code that became too hard to maintain: first add enough tests to be confident your oversight is enough, and then change it.

![Owain Williams](https://cdn.mos.cms.futurecdn.net/yLKEi5rn5TCTcqYsfAHXDf.jpg) 

Owain has been building websites and online stores for his own and his client's businesses for over 8 years. Having taken on a role at TechRadar Pro in 2023, he now leads on all website builder and CRM content, spending his days researching, testing, and reviewing some of the best website building and CRM platforms on the market. He also has a passion for helping people get a great deal on website builders, delivering the best coupon and promo codes on the market. With an extensive background in business, Owain holds a BA(Hons) in Business and Marketing and has written for several leading publications including MarketingProfs, Website Builder Expert, Digital Doughnut, and NealSchaffer.com.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
