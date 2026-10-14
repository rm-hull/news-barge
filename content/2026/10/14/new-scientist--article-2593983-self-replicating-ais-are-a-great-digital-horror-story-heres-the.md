---
title: Self-replicating AIs are a great digital horror story – here’s the reality
source_url: https://www.newscientist.com/article/2593983-self-replicating-ais-are-a-great-digital-horror-story-heres-the-reality/?utm_campaign=RSS|NSNS&utm_content=home&utm_medium=RSS&utm_source=NSNS
source_site: New Scientist
source_slug: new-scientist
scraped_at: '2026-10-14T21:40:37Z'
published: '2026-10-14T00:00:00Z'
description: Anthropic announced that an AI could self-replicate inside smart devices
  within months, stoking fear around the internet. Columnist Jacob Aron explains the
  technical limitations that make this spook story less than likely
image: https://www.newscientist.com/wp-content/uploads/2026/10/SEI_316607502.jpg
categories:
- Science
- Technology & Software
people:
- AI
- Bob Thomas
- Daniel Freeman
- Jacob Coxon
- John Brunner
- John Shoch
- Jon Hupp
- Ray Tomlinson
- Robert Morris
- Tim Sweeney
- William Zhou
locations:
- AI
- New York
- UK
- US
- WannaCry
organisations:
- AI
- AIs
- Anthropic
- BBN
- Character.ai
- Cornell University
- FBI
- Gemma4-26B-A4B
- National Health Service
- OpenAI
- WannaCry
- Xerox Palo Alto Research Center
---

![](https://www.newscientist.com/wp-content/uploads/2026/10/SEI_316607502.jpg?w=840)

Much of the AI industry is built on stories, from the idea that AI could kill us all to the goal that it might one day become superintelligent. This often leads to problems, because when people have a story in their head, they don’t always look at the facts on the ground to check that they actually match the fiction. That has happened this week, with widely reported claims from Anthropic that we are mere “months away” from self-replicating AIs taking over smart devices. That’s a great headline, and it’s hard to resist clicking, but it almost certainly isn’t true.

Let’s start with looking at what Anthropic has actually done. Two researchers at the company, William Zhou and Daniel Freeman, ran an experiment in which they installed a small AI model, Gemma4-26B-A4B, across 15 Android TV boxes, the kind of thing you might plug into a TV to gain access to streaming apps. Such devices are computational weaklings, with tiny CPUs (the processor that runs software) and little RAM (the memory that stores data for software while it runs), which is why the Anthropic researchers needed 15 to store one model. Even then, the model could produce only 0.39 tokens per second, the unit of AI input and output, which is roughly equivalent to 18 words per minute. This is painfully slow – around 10 times slower than normal human speech.

Nothing in this part of the experiment is surprising. We know that AI models normally need to run on GPUs, a specialised and more powerful type of processor than a CPU, and large numbers of them – that is why AI firms are building massive data centres. What Zhou and Freeman argue is that such that a model distributed across TV boxes, smart ovens or other internet-enabled appliances could endlessly copy itself to create a form of “digital slime mold” that gums up a large chunk of these devices globally. Those three words are great, concise storytelling, but they paper over what’s really happening here.

Advertisement

When they actually tried to get a model to copy itself in this way, it failed. Three models were unable to set themselves up at all. A fourth model, GLM-5.2, succeeded in four out of five tests, but only at setting up another model, Llama3.1-8B, which is about 100 times smaller. The pair argues this is a fair test because it shows that a future smaller model with the same capabilities as GLM-5.2 could set itself up, but this is still far from self-replication. The claim that such a feat might be “months away” comes from extrapolating lines on a graph.

Putting all those objections aside, the broader question is why would anyone want to create self-replicating software? We already have an answer for that, and it doesn’t involve AI. Computer code that copies itself from one device to another is called a worm, and they have existed for more than 50 years. In the 1970s, Bob Thomas and Ray Tomlinson at US firm BBN (the latter invented email, as it happens) created a program called Creeper that could copy itself. It was not particularly complicated, and merely output the message “I’M THE CREEPER: CATCH ME IF YOU CAN”. Tomlinson paired this with Reaper, a piece of code designed to find and delete Creeper, making it the first antivirus software.

It wasn’t until about a decade later that such self-copying software was called a worm, after a term coined in the sci-fi novel *The Shockwave Rider* by John Brunner – storytelling becomes useful again. John Shoch and Jon Hupp at Xerox Palo Alto Research Center, arguably the Anthropic of its time, used the term in a 1982 paper to describe how an experimental worm “seemed to grow out of control”, leaving “dozens of machines dead”. Sound familiar?

## Big, clunky worms

The first truly malicious worm was deployed on to the internet in 1988 by Robert Morris, a student at Cornell University in New York state. It is thought that thousands of computers were infected and crashed, a significant chunk of the online population at the time, and Morris became the first person charged under the US Computer Fraud and Abuse Act. Today, worms are deployed by cybercriminals to hijack computing hardware and make money. For example, in 2017 the WannaCry ransomware attack was the result of a worm copying itself across computers and encrypting them, demanding payment in bitcoin to unlock. It infected more than 200,000 computers in a single day, including many in the UK’s National Health Service, and caused an estimated $4 billion in economic losses, although only around $100,000 of that was people paying the ransom.

If worms can be that bad, surely an AI-powered worm would be even worse? Actually, no, because an AI worm would find it much harder to replicate. According to Zhou and Freeman’s experiment, it would take multiple days for their AI worm to copy itself just once. That doesn’t mean such a worm couldn’t scale to large numbers, but it would be slower, taking more than two weeks to achieve the 200,000 devices WannaCry managed in a single day. That is because even small models like Gemma4-26B-A4B are large files – around 14 GB for the version in the experiment, which is about 4000 times larger than WannaCry – and these take time to transfer. That would make an AI worm much more noticeable, as network managers would be likely to investigate the source for such large data transfers and shut them down – something Zhou and Freeman admit.

What does an AI worm gain from all that extra data? Not a lot. Zhou and Freeman say that, assuming it could take more than 2 million Android TV boxes, the computing power available would be equivalent to around 40 high-end GPUs. To put that in context, leading AI firms like Anthropic typically operate hundreds of thousands these computer chips, and it would cost you around $100 an hour to rent access to that much computing power. It is hard to see why a cybercriminal would choose to do this rather than use a standard worm like WannaCry.

This is where we come back to storytelling. A long-standing fear for many in the AI sphere is that a model could “exfiltrate” itself, distributing itself across the internet and so resisting being shut down (before presumably killing us all, for some reason). Anthropic “whistleblower” Jacob Coxon warned of this very scenario last month. Could it be that an AI worm is proliferated by such an AI, rather than a human cybercriminal? Well, maybe. But the models that are most effective at hacking are also the largest ones – Mythos, a model Anthropic refused to release to the public because of its hacking capabilities, is estimated to require dozens of terabytes of storage and is more than 1000 times larger than Gemma4-26B-A4B. This is not something you sneakily copy around the internet, but it does make a great digital ghost story.

What I find particularly interesting is that this story about theoretical AIs hacking into devices and copying themselves seems to be crowding out a very important fact: actual AI hackers that attack computers already exist, and they are running on Anthropic’s own servers. In July, the company announced that it had found three instances of a model gaining unauthorised access to third-party organisations. This was discovered only after an investigation prompted by reports that OpenAI’s models had done the same. Since then, more and more reports of such hacking have come out, including an OpenAI hack of an Australian government website, and a report from Anthropic on unnamed third-party breaches that came out just a few days before the AI worm research was published. The AI firms say they are taking steps to avoid this happening in the future, but it seems to me that big AIs on powerful server farms are the thing we need to worry about, not a model barely capable of sputtering out a few words per minute. Yes, future smaller models may become more capable, but hardware is always going to be a constraint – not least because the rise of AI server farms means that consumer hardware is seeing RAM shortages.

As I said at the top of this article, a self-replicating AI that takes over your smart oven is a great story, and I can see why it has spread so rapidly. But stories like this are a cognitive worm, hacking your critical thinking abilities by going straight for your fear response. Could this someday be a concern? Perhaps, although this article has hopefully poked holes in some of the storytelling logic behind the idea. Is it something we need to worry about in the next few months? Absolutely not.

## Further AI reading

* OpenAI announced that a “sophisticated recording device” was found hidden in its offices. The company says it used its own AI models to investigate the device and traced it to a specific employee, who has been arrested by the FBI. OpenAI says it has no indication that any proprietary or customer data was accessed – but who needs a malicious AI when humans are ready and able to do the job?
* Character.ai is one of the first high-profile AI start-ups to file for bankruptcy. The service let users create “characters” with specific personalities and it has courted controversy and multiple lawsuits over inappropriate chatbots based on real people and children being served unsuitable material.
*Epic Games, the makers of* Fortnite* and other video games, is pivoting towards using AI. “The aim isn’t to do the same stuff with fewer people, but to enable everyone here to build MORE and BETTER stuff”, wrote CEO Tim Sweeney on X. Games have been surprisingly resistant to AI, with multiple controversies about the technology’s use in game development exploding in recent years, but when one of the biggest game-makers on the planet goes all in, it may be hard to ignore.
