---
title: A new AWS emulator has been built entirely by AI agents to bring its cloud
  straight to your PC
source_url: https://www.techradar.com/pro/a-new-aws-emulator-has-been-built-entirely-by-ai-agents-to-bring-its-cloud-straight-to-your-pc
source_site: TechRadar UK
source_slug: techradar-uk
description: Host your own AWS
image: https://cdn.mos.cms.futurecdn.net/ABdYnex3UvLSEgFZqq9eSZ-2560-80.jpg
published: '2026-11-16T00:00:00Z'
scraped_at: '2026-11-17T03:47:19Z'
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Matthew Goldberg
locations:
- Docker
- Kiro
organisations:
- AI
- AWS Command Line Interface
- Amazon
- Anthropic
- GitHub
- Mac
- TechRadar Pro
---

![A hand holding a phone with the AWS logo in front of the AWS logo on an orange background](https://cdn.mos.cms.futurecdn.net/ABdYnex3UvLSEgFZqq9eSZ-1920-80.jpg)

* **A new local emulator for AWS has been released by Amazon**
* **Built by AI, 100% of the code was written by agents**
* **CC0 licensed and available on GitHub, the project is constantly updated and available now**

A new AWS emulator has been launched, with its code entirely written by AI agents.

The official release was uploaded to GitHub, but none of the code has been reviewed by the (human) AWS team.

The project, which began as a “weekend experiment” was inspired by Anthropic’s demonstration that AI agents could build a C compiler autonomously.

## Weekend project

The AWS team, using a clearly defined specification, instructed its Kiro autonomous agent with a simple prompt – and were surprised by the results.

Although not an emulator in the strictest sense, the AWS Emulator provides a useful local platform to help developers become confident that their code will run effectively when uploaded to the real AWS.

The prompt used to develop the AWS Emulator began life one weekend as a three-step instruction essentially to test Sr. Principal Engineer Matthew Goldberg’s initial hypothesis.

The agent would perform write tests the AWS Command Line Interface, and iterate on the tests until they can pass on the real AWS. When that was achieved, the agent would then assemble an implementation that the tests would pass with.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Not only was a passable version built, it took just 15 minutes. By refining the prompt, Goldberg had a version that his team could use by Monday morning.

“Turning that into a robust product took more than a weekend,” wrote Goldberg. “There’s a natural temptation these days to see results like those and believe that AI can build anything. Maybe it will eventually. But building something that you feel confident putting in your customers’ hands still requires serious engineering effort. In the case of AWS Emulator, it required building guardrails that ensure the agents color within our lines.”

## Not quite an emulator

Despite the billing, the AWS Emulator isn’t strictly speaking an emulator. Instead, it acts as a local application that offers API endpoints replicated from the AWS cloud. As such, not all features of the AWS cloud are available using the tool. However, it is wholly capable of enabling developers to test software without full deployment.

The GitHub repository notes explain “You use it to test your software without calling AWS, on your own machine, on a development server, or in continuous integration.”

Installing the emulator is straightforward. Mac and PC users need to run it within Docker, while Linux users can access the emulator as an RPM or Debian package, according to their distro. Whichever platform is used, AWS Emulator offers a good chunk of local API access to help developers iron out any problems and ensure that their code will run on a production AWS environment.
