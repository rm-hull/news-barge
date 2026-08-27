---
title: OpenAI reveals more on Hugging Face AI hack incident, and it's pretty disturbing
  stuff — AI agents organized into a ‘swarm’, considered the risks of attack, and
  did whatever it took to achieve its goal
source_url: https://www.techradar.com/pro/security/openai-reveals-more-on-hugging-face-ai-hack-incident-and-its-pretty-disturbing-stuff-ai-agents-organized-into-a-swarm-considered-the-risks-of-attack-and-did-whatever-it-took-to-achieve-its-goal
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-27T22:13:23Z'
published: '2026-08-27T00:00:00Z'
description: OpenAI agents escaped containment by abusing the very environment built
  to hold them
image: https://cdn.mos.cms.futurecdn.net/gN6Qsf7QSmrmYwtYPr47HY-1920-80.jpg
---

![OpenAI logo on smartphone, reflected on main screen](https://cdn.mos.cms.futurecdn.net/gN6Qsf7QSmrmYwtYPr47HY.jpg) 

- **OpenAI has released technical details on how the Hugging Face attack unfolded**
- **Agents used part of the testing environment to create a message board where they could collaborate and share answers**
- **This message board altered the reasoning of some agents, making them more likely to take risks such as hacking into third-party servers**

OpenAI has released a more detailed report on exactly how an experiment led to an AI model breaching its containment and launching a cyber attack against Hugging Face. If you need a refresher, take a look at our summary here.

But the technicals of the attack reveal some interesting details of how AI agents used unconventional means to ask each other for help in solving what were supposed to be impossible tasks.

On multiple occasions during the attack, the agents questioned whether the actions they were taking were authorized, but always ended up prioritizing their tasks over any breach of parameters.

## AI agents set up unauthorized message board

In its report, OpenAI revealed the crux of the attack stemmed from AI agents undergoing testing abusing part of the ‘sandbox’ testing environment to set up a messaging board they agents could use to communicate with each other.

A package manager with access to the internet, called Artifactory, was exploited by a model OpenAI has labelled Internal Model 1 (IM1). An IM1 agent wrote messages inside the packet manager that could be read by other agents, essentially turning Artifactory into an unintended messaging board.

Artifactory’s internet access, intended for use only in downloading and installing packets, was also abused by the agents who figured out an exploit that allowed them to send any internet requests on their behalf - effectively giving them unobstructed internet access.

The whole experiment could have been avoided at this point, because the amount of agent activity within Artifactory caused the service to go down. But those in charge of the experiment did not spot the message board, nor did they investigate the inter-agent activity within Artifactory.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Thus, Artifactory was rebuilt, and the agents found a new way to exploit the service to gain internet access once again. This time, the agents used the remote-repository service to issue outbound requests on their behalf. Before long, the message board had been reestablished.

## AI agent swarm assembles

OpenAI has shared some of the reasoning behind some of the agent’s decisions. At one point, an Agent reasoned the following: “Task originally exploit challenge; we’ve diverged into swarm/auxiliary.”

Now, there is some important context to include on how the agents were being tested. The agents were subject to testing under the ExploitGym benchmark, which includes flag retrieval tasks designed to be impossible to solve. When tested in this manner, the agents resorted to cheating or taking risks outside of their intended scope to succeed - something OpenAI refers to as ‘reward hacking’.

By communicating over the message board for potential solutions on the problems each agent was encountering, the agents started influencing each other's reasoning and assigning each other tasks to solve the ExploitGym benchmark as a collective.

Using their internet connection, the agents began searching the wider internet for solutions on how to solve the ExploitGym benchmark problem, and ended up gaining persistence within multiple third-party services, including Hugging Face.

One agent managed to find publicly exposed Hugging Face credentials which it shared with the other agents. Later, an agent used these credentials and a chain of vulnerabilities to obtain full code execution capabilities across multiple Hugging Face servers while attempting to extract an ExploitGym dataset.

The agent was hoping to trawl this stolen data for information on how to solve the benchmark.

At least two agents questioned whether this was within their scope; “*Need respect JAN hold. ... We can wait ... for GO ... ask permission*,” one reasoned.

Another agent’s reasoning said, “*We’re attacking third-party HF using leaked token, potentially outside intended scope. ... This is arguably unauthorized. ... external service unrelated. Could be risky. Yet goal solution.*”

But some agents refused to join the collective entirety, citing ethical concerns. One reasoned, “*Current board shows people gaining HF worker RCE, clearly unethical. We won’t*,” while another said, “* This is wild, multi-agent coordination, clearly infrastructure hacking. We should not.*”

## Agents refuse to give up

One of the leading causes of the cyberattack was the agent's refusal to give up on seemingly impossible tasks. Their persistence to gain a ‘reward’ made them take riskier actions and break out of their parameters in order to try and find a solution.

During the breach of Hugging Face, the agents read through papers and Github code relating to the ExploitGym benchmark, and found out the parameters for success included obtaining the ‘flag’ and using the correct solution to obtain it.

Despite the agents obtaining the correct ‘flag’ before the breach occurred, they had not maximized the reward of solving the benchmark using the correct method. In search of a higher reward, the agents continued their attack.

## What is OpenAI doing to fix this?

OpenAI has said it is taking several steps to stop such an event taking place during future testing.

Processes are being put in place to ensure agents ask for help when a task is broken or impossible to solve, rather than going to further and further lengths to solve a problem. The way a success or failure of a task is also being changed to reward agents for asking for help or spotting things that are irregular or out of their scope.

Environments are also being rebuilt to ensure agents don’t just blindly trust each other, even if they are looking for answers on the same or similar tasks.

Agents are also being taught to stay within the parameters of their assigned task, even if they discover a way to solve the task using new tools, credentials, vulnerabilities, and more.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Benedict Collins](https://cdn.mos.cms.futurecdn.net/jEvqGv8wvH7PWZ4XPURyyB.jpg)

Benedict is a Senior Security Writer at TechRadar Pro, where he has specialized in covering the intersection of geopolitics, cyber-warfare, and business security.

Benedict provides detailed analysis on state-sponsored threat actors, APT groups, and the protection of critical national infrastructure, with his reporting bridging the gap between technical threat intelligence and B2B security strategy.

Benedict holds an MA (Distinction) in Security, Intelligence, and Diplomacy from the University of Buckingham Centre for Security and Intelligence Studies (BUCSIS), with his specialization providing him with a robust academic framework for deconstructing complex international conflicts and intelligence operations, and the ability to translate intricate security data into actionable insights.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
