---
title: Nvidia, Palantir, and others restrict advanced AI model usage over privacy
  concerns, report claims — 'paranoia' rising over customer intellectual property
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-palantir-and-others-restrict-advanced-ai-model-usage-over-privacy-concerns-report-claims-paranoia-rising-over-customer-intellectual-property
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-14T20:17:58Z'
published: '2026-09-14T00:00:00Z'
description: Zero data retention policies and air-gapped servers have become vital
  to some big AI users.
image: https://cdn.mos.cms.futurecdn.net/u9ek9duZ3S5dDDNM6EaY7k-2000-80.jpg
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
locations:
- U.S.
people:
- Claude
- Jensen Huang
- Oliver Haslam
- Tom
organisations:
- AI
- Anthropic
- C Spire
- Fable
- Get Tom's Hardware
- Google News
- Microsoft
- Northrop Grumman
- Novo Nordisk
- Nvidia
- Oliver Haslam
- OpenAI
- Toms Hardware
---

![ChatGPT, Claude, and Gemini apps on an iPhone](https://cdn.mos.cms.futurecdn.net/u9ek9duZ3S5dDDNM6EaY7k.jpg) 

Anthropic and OpenAI are both facing uncomfortable questions from some large AI customers over concerns about how proprietary data may be used to train AI models. Some companies are so worried that they have begun demanding assurances about how their data is handled or going so far as to place limitations on which models their employees can use, and for which tasks, *The Information* reports. They fear that models may be trained on their intellectual property and information.

The issue can be traced back to a June change by Anthropic. Following the change to its flagship Fable model's policies, Anthropic can now retain customer data. The company argues that it only does so to ensure that Fable isn't being misused. But some companies have raised concerns that it means sensitive business data will be caught up in the sweep.

While both OpenAI and Anthropic point out that they don't train their models on the information given to them by companies with specific enterprise contracts by default, that doesn't tell the full story. Both companies do collect metadata from the same corporate customers, and while information on exactly what that metadata contains is hard to come by, OpenAI notes that it's only used “to better understand how our services are used." Anthropic also argues that any data it collects about how customers use its products is aggregated and anonymized. And that metadata isn't used to train models.

Regardless, there are still concerns over a perceived lack of clarity about what is collected. Telecoms outfit C Spire has agreements with both OpenAI and Anthropic that prevent either from using its data to train models, the report says.

However, the contracts do allow both OpenAI and Anthropic to collect C Spire technical usage data. C Spire believes that includes information about what applications AI models are connected to as well as usage data. It also worries that the AI companies may collect information about what their models get up to between generating responses.

For its part, OpenAI says that it does not use this "chain-of-thought" data to train its models. But C Spire still believes it needs a better understanding of what data is being collected, the report adds. It argues that neither AI company is being clear in its explanations.

## Taking the private approach

One solution to any privacy concerns could be to use air-gapped servers, something aerospace company Northrop Grumman has already chosen to do. *The Information* reports that the company runs open-source AI models on its own air-gapped servers rather than trusting the likes of OpenAI and Anthropic.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Alternatively, Microsoft is already trying to take advantage of any data privacy concerns by tempting OpenAI and Anthropic customers to its own secure AI platforms. Microsoft's isolated cloud environments run AI models on private servers that don't send any data to external AI companies. But this approach is costly, and the report notes that at least one customer is still considering Microsoft's alternative approach.

Pharmaceutical company Novo Nordisk has taken a slightly different approach. While it continues to use Anthropic's Claude for some tasks, it has a ban on allowing any proprietary data to be used by the model.

It's clear that a lack of trust has the potential to cost AI companies real money, and in one instance, it already has. The same report notes that a large U.S. utility company has already canceled its plans to test Anthropic's Fable. The utility company wanted to know if Fable could run its core power infrastructure but ultimately pulled the plug over Anthropic's refusal to agree to a nonrevocable zero data retention (ZDR) policy.

Nvidia has also decided to use Fable for tasks that don't require it to gain access to sensitive data. The company points to the same lack of ZDR guarentees as the reason. Instead, Nvidia uses its own in-house AI solution for tasks that it deems too sensitive for Anthropic's model. Nvidia CEO Jensen Huang has famously remarked that its employees should use AI tokens worth half their annual salary every year.

*Toms Hardware* reached out to Nvidia for comment but did not receive one by publication.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Oliver Haslam](https://cdn.mos.cms.futurecdn.net/3XaHYJa7vPsa7PG8i5U8F5.jpg) 

Oliver Haslam has written about technology of all shapes and sizes for over 15 years, both online and in print. He's fascinated by how personal computing continues to change as tower PCs give way to foldable phones and beyond.

- 
I think the world has an expectation that OpenAI, Anthropic, and any other cloud AI provider can and should have the means to discover malicious uses, report on it (transparency), and stop the abuse. Anthropic just released a report on several threat actors that they caught and most part stopped. True NZD makes this much harder.Reply
 
Just goes back to the on-prem (and remember that you can run your own private cloud) vs. public cloud debate in IT, which is decades old now.
