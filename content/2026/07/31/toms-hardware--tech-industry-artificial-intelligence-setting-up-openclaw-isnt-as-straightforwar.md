---
title: Setting up OpenClaw isn’t as straightforward as the internet wants you to think
  – running local AI on humble hardware
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/setting-up-openclaw-isnt-as-straightforward-as-the-internet-wants-you-to-think-running-local-ai-on-humble-hardware
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-31T14:29:41Z'
published: '2026-07-31T00:00:00Z'
description: Lies, deceit, and HammerClaw.
image: https://cdn.mos.cms.futurecdn.net/WZEQZhhmWUU6DvnnYh7p9G-1280-80.png
---

![Setting up OpenClaw](https://cdn.mos.cms.futurecdn.net/WZEQZhhmWUU6DvnnYh7p9G.png) 

Unless you’ve been living under a rock, OpenClaw has dominated headlines, both good and __bad__, for much of early 2026. Developed by Peter Steinberger, the tool is an engine that spins up an AI agent that can autonomously act on your behalf, going so far as having the ability to run files, browse the web, and much more. Using a system named “Skills,” you can even teach your AI assistant to perform new tasks, with more integrations popping up daily. But how useful is it for the average person? I took it upon myself to answer that question by using the relatively humble Beelink SER10 MAX mini PC, which comes pre-installed with OpenClaw, to find out.

To kick things off, when setting up your OpenClaw installation, there’s a fairly large decision one has to make: Do you want to rely on Cloud resources and more powerful AI models, or run something locally? Beelink’s SER10 MAX ships with Qwen-3.5 9B, which is a relatively older and more outdated AI model. Since I want to keep things fairly simple, I opted for the local AI route first. To run larger models, you’ll need a lot of memory, so I first tweaked the humble Mini PC’s video memory up to 48GB, which should allow us to keep a larger, more complex model in memory. It also leaves us 16GB of system memory to play around with, which should be more than enough to run the terminal and ensure that everything else works as intended.

## Selecting the ideal local AI model

Having 48GB of available video memory should allow us to run a fairly powerful AI model on the system. However, the downside of running a larger model is that token speeds are likely to be slightly lower than expected. However, for running the super-smart AI that does things for us locally, we want as much intelligence as we can get. For this exercise, I chose Google Gemma 4 31B (UD-Q8_K_XL), a near-lossless quantization, somewhat ambitiously, as I will learn shortly.

After downloading the model and running it in llama.cpp, we managed to attain 2.34 tok/s. On average, everyday queries took 116 tokens to generate, at 2.34 tok/s. That’s still too slow for fast everyday use. So, I took a deep breath and conceded that the humble __Ryzen AI 9 HX 470__ didn’t have fast enough memory or memory bandwidth to run such a large model at acceptable token speeds. Even if I had dropped the quantization to 4-bit, we’re still looking at the theoretical maximum of around 5 tok/s for that model in particular. If you had a faster machine with rapid RAM speeds, such as a Strix Halo system like the __Framework Desktop__, it might be more workable, but for a lower-end piece of silicon with relatively humble DDR5-5600 speeds, you’ll just have to accept a slightly more neutered model.

So, I eventually conceded that the smaller Gemma 12B (Q4_K_M) was a much more sensible choice for a device of this caliber. After loading things up into llama.cpp, we managed to get a much more sensible 10.64 tok/s on a general knowledge query: “What is Tom’s Hardware?” Now that I have a little piece of talking electrified sand on my desk, it’s time to configure OpenClaw.

## Hatching HammerClaw

 ![Setting up OpenClaw](https://cdn.mos.cms.futurecdn.net/CuqKsiN7yojuGtcWA3pNXF.jpg) 


The device I am using, the Beelink SER10 MAX, comes with OpenClaw pre-installed. The only real dependency it has is llama.cpp, which we configured earlier while testing which AI model to use. Since the llama.cpp port is open, OpenClaw leverages that to talk to the AI model, with all of its additional fanciness included. The OpenClaw installer is fairly straightforward in getting things up and running, including setting up a Telegram channel to communicate with our AI model remotely and configuring a gateway, so we can configure things without relying on Ubuntu’s terminal commands.

Within the installer, we start to define our new AI assistant: It asks what its name and identity are, some basic details about the user, as well as what principles it should uphold, in a very extravagant file named __SOUL.md__. Remember, our talking sand isn’t alive, so it’s all quite dramatic. Generating a __SOUL.md__ file takes a while for our humble local AI model, which I’ve named HammerClaw. But can it do anything useful for me to justify its nascent AI existence? Right now, it’s taken five minutes to think about exactly what it is and what it’s doing.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

After a little while, our little HammerClaw “hatches,” asking what its purpose is, who I am, and how it should talk. Personally, I don’t like it when AI models are verbose, so it’s straight and to the point, and should never, ever lie to me. When AI models can scale to rather humble devices like this one, the smaller, less-intelligent models can be error-prone. With our little local AI agent alive and kicking, it’s time for it to automate a task for us; it couldn't be that difficult… right?

## Stumbling blocks

HammerClaw quickly wakes up, and I offer it a task: to gather ten news articles from trusted outlets and different parts of the day, ensuring freshness, with a small digest of what’s happened. Since most of my work on *Tom’s Hardware Premium* is centered around chipmaking and data centers, I want it to focus on those topics. HammerClaw then quickly takes the task and starts working out how to pull it off. It’ll use its built-in cron tools and felo-search to pull stories from the internet.

Now, here’s where things go bad for poor HammerClaw. It then begins to simulate the action, instead of actually performing it, despite saying that it had set up the cron jobs and skills required for the automated scheduling. Even worse, it hallucinated a list of links that went absolutely nowhere. After pointing the error out, it gets apologetic and investigates why things went wrong. As it turns out, some additional parts need to be configured, which it tried to do and failed once again. Agentic Tool use is now a specific benchmark, but when asking Gemma 4 12B to set up a multi-step task like this, it simply couldn’t manage with the conversational tone of my prompts.

![Setting up OpenClaw](https://cdn.mos.cms.futurecdn.net/YgmH8TghSbPpmTq6YgDjGF-1200-80.jpg) 

![Setting up OpenClaw](https://cdn.mos.cms.futurecdn.net/pvYmFpHW7Q2nZ8jrbWvQGF-1200-80.jpg) 

![Setting up OpenClaw](https://cdn.mos.cms.futurecdn.net/MzzMM3jgQcFD8mUJm7cDHF-1200-80.jpg) 

![Setting up OpenClaw](https://cdn.mos.cms.futurecdn.net/YgmH8TghSbPpmTq6YgDjGF-1280-80.jpg) 

![Setting up OpenClaw](https://cdn.mos.cms.futurecdn.net/pvYmFpHW7Q2nZ8jrbWvQGF-1280-80.jpg) 

![Setting up OpenClaw](https://cdn.mos.cms.futurecdn.net/MzzMM3jgQcFD8mUJm7cDHF-1280-80.jpg) 

It’s at this point that I asked HammerClaw to give itself a grade, to which it offered itself a B- on accuracy for hallucinating and making up news stories. Now, I don’t want to say that all OpenClaw AI agents would do this, as we are running a relatively light local model. I would expect that larger local models would be able to identify what they need to do much more efficiently due to having a significantly higher model parameter count. With that in mind, I wondered if another AI model could help HammerClaw along a little bit with this task. And so, I went onto my OpenRouter account and opened a chat with the big, beefy__ 2.8 Trillion Parameter Kimi K3__.

## Kimi K3 saves the day

Comparing a cloud-based frontier model like Kimi K3 and Gemma 4 12B just isn’t fair. One takes up terabytes of RAM to run, while Gemma fits inside a Mini PC that lives on my desk.

Instead of using Kimi K3 to run the AI itself, I tasked it with actually helping me set up the job that HammerClaw seemingly didn’t have the skills to pull off. This hybrid workflow – of using a local LLM in tandem with a more powerful one in the cloud- is a common setup for many AI enthusiasts. After about a dollar in tokens, it sent me a list of OpenClaw commands, skills, and instructions, after reading the current documentation for OpenClaw CLI to ensure it got everything right. It was flawless. I followed the instructions Kimi K3 gave me and entered them into an Ubuntu Terminal, where it successfully created a new skill for HammerClaw named ‘News-Intel,’ instructed me on how to enable the web-search functions, and set up the Cron jobs for the automated sends. Bearing in mind that I had never used OpenClaw before, it was all surprisingly smooth, even if our local model couldn’t do all of these tasks itself.

 ![Setting up OpenClaw](https://cdn.mos.cms.futurecdn.net/rLQ2eLqaxybbugKqPwmgDF.jpg) 


With everything set up, the buck is then passed back to our much humbler Gemma 4 12B model-powered HammerClaw to execute the rest – after all, this is supposed to be a test for how Local AI models function. I executed the command for a manual run while checking the operational logs, where it was successfully calling all of the tools, and thought, against all odds, HammerClaw might actually be able to do it. A few minutes later, I received a Telegram message. HammerClaw had managed to locally execute the task and send me a digest of ten news stories.

 ![Setting up OpenClaw](https://cdn.mos.cms.futurecdn.net/didkurbhR6EkRCW7ohnGFF.jpg) 


Of all of the things to automate, this is likely one of the simplest examples of how someone can use OpenClaw. While simple, it’ll also save me a bit of time every day staring at an RSS feed and looking for stories myself. But, it’s quite a distance away from the “speak, and it’ll do whatever you want it to!” promise that drew so many into a frenzy earlier this year.

## Is it worth it for the average person?

If all you heard about OpenClaw is that it’s a magical AI agent that can do anything, as I’ve learned, it’s not quite the truth. Unless you’re well-versed in several elements, like understanding model choices and getting your head around what models perform well for tool-calling. Running a humble local setup might be fun, or interesting to tinker around with, but the true power for Local AI developers and tinkerers lies with the obvious: More power to run bigger, complex models, and more agents running tasks consecutively. In fact, we’ve taken a look at how these workflows can be used in practice with a mixture of __Local and Cloud AI models for __*Tom’s Hardware Premium*__.__

The issue here is that for our local model, this simple task – of running and sending us 10 news stories- could not set itself up, and that’s using hardware that already costs north of $1,500. As our resident local AI expert and GPU guru Jeff Kampman has recently tested, for those serious about AI who want real power without relying on the cloud entirely, you might want to save up your pennies to run stronger, faster local models, either using dedicated GPU-accelerated setups, or dedicated boxes such as the __DGX Spark__, or a __cluster of Dell Pro Max GB10s__, both of which will cost you north of $5,000. You’d hope that the models capable of running on that hardware wouldn’t fumble the setup of a relatively simple Cron job.

The real question is, will having a local AI inference box meaningfully change how you work, or the work you do, to pay for itself? For many, that’s the lingering question that many are asking themselves. For now, HammerClaw is sending me more articles every few hours, a task that can be performed by simple scripting. But the manual “sift” is being handled by an LLM. As neat as it is, I wouldn’t pay $1,500 for the privilege. Luckily, it’s not merely a box made for AI inference; there’s a whole computer attached.

![Sayem Ahmed](https://cdn.mos.cms.futurecdn.net/xsPCakGobuUWmyECbrEM2T.jpg)

Sayem Ahmed is the Subscription Editor at Tom's Hardware. He covers a broad range of deep dives into hardware, both new and old, including the CPUs, GPUs, and everything else that uses a semiconductor. He has worked as a professional tech journalist since 2015 and has written for Gamespot, IGN, and Dexerto.
