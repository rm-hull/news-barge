---
title: '‘One of the worst outcomes for companies is reacting in a knee-jerk fashion
  before the rewards can be reaped’: How game engines, version control software, and
  AI are delivering new benefits and challenges to almost every industry'
source_url: https://www.techradar.com/pro/one-of-the-worst-outcomes-for-companies-is-reacting-in-a-knee-jerk-fashion-before-the-rewards-can-be-reaped-how-game-engines-version-control-software-and-ai-are-delivering-new-benefits-and-challenges-to-almost-every-industry
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-12T15:00:44Z'
published: '2026-09-12T00:00:00Z'
description: AI isn't the only technology seeing widespread adoption
image: https://cdn.mos.cms.futurecdn.net/AvZcjmUMtehpuha5oJLcTB-2560-80.jpg
---

![Who will win the AI race?](https://cdn.mos.cms.futurecdn.net/AvZcjmUMtehpuha5oJLcTB.jpg) 

Now that businesses of all sizes are adopting AI technologies, the next step is to prove the technology is delivering measurable benefits and improvements. But nailing down a singular metric to show these benefits is proving difficult.

Sure, businesses can see exactly how much it is costing them, but measuring output is another beast entirely. Tokkenmaxxing has shown that arbitrary targets of use are not necessarily the best way to measure the productive impact of AI.

But perhaps there is a lesson to be learned from the adoption of other, quieter technologies that are delivering measurable benefits in new industries, and how AI can fit into workflows alongside this new and exciting tech infrastructure.

## AI isn't the only tech seeing widespread adoption

Perforce’s 2026 State of Real-Time Workflows Report found it isn’t just AI seeing widespread adoption across industries. Game engines and real-time 3D engines, once used almost exclusively by game developers, have seen a huge wave of adoption across the aerospace and defense, public sector and education, and even media and entertainment.

These tools show measurable improvements in productivity before adoption because they are tried and tested. They have decades of proven returns shown by the gaming industry. AI on the other hand is yet to show sustained, measurable return on investment for many businesses. But there are also a host of other issues accompanying AI use.

Version control software is also seeing a rapid growth in adoption in real-time workflows. AI is a driving force in this adoption as businesses now have to handle significantly more assets and content within each project. Having visibility into who changed what - especially with AI agents now involved in workflows - is no longer a choice, but a necessity.

One of the main concerns remains job replacement. Perforce’s report found that 50% of employees who had adopted AI in their workflows feared they would be replaced by the technology. But AI concerns also extend into the work they are doing; 49% feared their AI tools would produce poor or inaccurate content and 48% held ethical or compliance concerns about their use of AI technology.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

To understand the challenges businesses are facing in showing measurable return from AI adoption, I spoke to the author of Perforce’s report, Brent Schiestl. Brent leads Perforce’s Digital Creation business unit and is the Senior Director of Product Management.

- **Businesses may be seeing greater productivity gains when adopting AI into workflows, but it is having a negative effect on the creative outlet for employees and the perception of brands by consumers. What steps are businesses taking to maintain trust with both groups?**

We see a distinction in perception when comparing AI usage in generating source code vs. binary assets. For example, if a team is using AI to autonomously fix a bug in source code, consumers seem more accepting of that use case. A bug fix is a well-defined problem where creativity is usually not the key to solving it.

In fact, one could argue that engineers are being freed from mundane work to focus more on creative work when deploying AI this way.

Where we see more negative perception is with binary assets (images, audio files, movies, etc.). Because many LLMs were trained on data without originating author consent, producing binary assets via AI tends to get more scrutiny.

Some steps we have seen companies take to maintain trust include establishing clear public AI usage disclosure policies, making it clear that humans remain in the loop for final asset creation, and maintaining strong provenance data for how the asset came to be.

With these steps, the end consumer is given a complete enough data set to decide whether they feel the AI usage clears their own ethical hurdles or not.

- **There is a clear move away from tokenmaxxing to measure the value of AI. What metrics are businesses now using to show the cost-to-benefit ratio of AI deployment and what new problems has this introduced?**

This is the single biggest question we get regularly from our customers. Our customers are using AI more than ever but struggling to prove that AI is benefiting them in a way that justifies the expense.

Some examples of metrics that we see related to the cost-benefit ratio of AI include release frequency, amount of content in each release, and telemetry to understand how new features are being used, for example.

In addition, we see industry standard metrics like DORA rising in importance as customers want to benchmark their productivity more broadly.

One key is to consider Goodhart’s Law, which states that when a measure becomes a target, it ceases to be a good measure.

Introducing new metrics around measuring the value of AI can lead to engineering teams gaming metrics at the expense of doing what is best for the final product.

In addition, isolating AI’s contribution from all other release activities is a new challenge that all companies are wrestling with.

- **Why are game engines being adopted so readily by so many industries, and what blockers previously prevented their use in these industries? Are there lessons that other, less technical industries can learn from this adoption?**

I believe that one of the biggest blockers was literally in the name itself, as formally referring to them as “game engines” siloed the use case right out of the gate for anyone not in gaming.

These engines were historically hard to deploy outside of a gaming context including, but not limited to, licensing, tooling for non-artists, and integration with enterprise systems.

For example, Epic Games has had to figure out how to monetize Unreal Engine outside of gaming. Even we at Perforce have historically surveyed our customers and up until last year we used to refer to our official report as the “State of Game Technology Report”.

This year we renamed the report to the “State of Real-Time Workflows Report”. Once adjacent industries realized that these engines are really a bundle of rendering, physics, networking, and asset pipelines, new industry verticals literally sprang out of nowhere. Sometimes it’s more about positioning than anything else.

- **What effect is the adoption of new technologies such as AI, game engines, and 3D modelling software having on the infrastructure costs of industries that traditionally did not use these tools?**

Infrastructure costs including GPU compute, storage for large binary/3D assets, bandwidth, specialized workstations, and licensing for engines/DCC tools, have led to businesses needing to justify these new expenses.

The easiest way to justify is to realize an increase in revenue based on the investment. The challenge is that these sorts of investments can oftentimes take years to realize the benefits.

Companies, especially CFOs, need to remain patient in the early stages. One of the worst outcomes for companies is reacting in a knee-jerk fashion before the rewards can be reaped.

Another challenge is that these industries often lack the IT muscle sized for this new (to them) infrastructure, meaning the cost isn't just the compute/storage line item, it's also the organizational capacity to run it.

- **What tools are businesses using to manage the associated technical debt that comes with AI productivity? How are these tools helping manage quality, compliance, and security?**

Technical debt is rising from new sources such as unreviewed AI-generated code (by humans and/or by agents), dependencies pulled in by AI that no one owns, license contamination, and model version drift.

Some tools that we’re seeing fill this space include AI-aware code review (e.g., CodeRabbit, Greptile, P4 Code Review, etc.), SAST/DAST tools tuned for AI output (e.g., vulnerability patterns in AI-generated code), license/provenance scanners (e.g., copyleft contamination risk), and version control practices that treat AI-generated commits as first-class artifacts.

- **How is AI changing the open source market, helping businesses develop their own solutions, and what effects will it have on the traditional software licensing market in the future?**

AI is changing the open source market in a couple of ways. First, it’s never been easier to develop, and then if desired, open source your own solution.

On the other extreme, we’re seeing reports of previously open source repositories being turned private due to the sheer number of AI-generated pull requests being raised and the inability of the repository owner to keep up.

Traditional software licensing that is purely seat-based is being tested as the assumption is that companies may either downsize or at least not grow at the same pre-AI rates that we had become accustomed to.

The main question that feels unanswered today is whether the build vs. buy math is genuinely changing or not.

One of my favorite memes goes something like, “I saved $30,000 in subscription costs by building my own solution and it only cost me $100,000 worth of tokens to do it.”

While the meme exists to poke fun, it is something that needs to be taken seriously because initial build and ongoing maintenance plus support needs to be accounted for.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Benedict Collins](https://cdn.mos.cms.futurecdn.net/jEvqGv8wvH7PWZ4XPURyyB.jpg) 

Benedict is a Senior Security Writer at TechRadar Pro, where he has specialized in covering the intersection of geopolitics, cyber-warfare, and business security.

Benedict provides detailed analysis on state-sponsored threat actors, APT groups, and the protection of critical national infrastructure, with his reporting bridging the gap between technical threat intelligence and B2B security strategy.

Benedict holds an MA (Distinction) in Security, Intelligence, and Diplomacy from the University of Buckingham Centre for Security and Intelligence Studies (BUCSIS), with his specialization providing him with a robust academic framework for deconstructing complex international conflicts and intelligence operations, and the ability to translate intricate security data into actionable insights.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
