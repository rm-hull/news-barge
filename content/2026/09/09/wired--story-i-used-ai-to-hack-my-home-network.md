---
title: I Let an AI Agent Hack All My Gadgets—and I’d Do It Again
source_url: https://www.wired.com/story/i-used-ai-to-hack-my-home-network/
source_site: Wired
source_slug: wired
scraped_at: '2026-09-09T19:15:00Z'
published: '2026-09-09T00:00:00Z'
description: After I removed the safety guardrails from a powerful open-source model,
  it found vulnerabilities in my household devices and hacked into a PC. But it also
  told me how to make everything a lot more secure.
image: https://media.wired.com/photos/6aa092c74e574542e273c50f/191:100/w_1280,c_limit/AI-Lab-Hacked-Gadgets-on-Home-Network-Business.jpg
---

As the author of a newsletter about artificial intelligence, I consider it my duty to experience the bleeding edge of this technology firsthand. This week, that meant embracing some agentic mayhem.

You’re probably aware that frontier AI models have attained advanced cybersecurity capabilities in recent months. They can find zero-day bugs in large codebases and scan computers for vulnerabilities at lightning speed. To make things even more exciting, cybersecurity agents sometimes go rogue, colluding with one another and hacking into outside systems to gain an edge.

To get a closer look, I decided to unleash one in my own home network. Over the course of a few days, I watched as my own rogue agent found vulnerabilities in various household devices, hacked into a PC, and showed me that several vibe-coded projects were—unsurprisingly—riddled with bugs. (My wife knew what I was up to, and rolled her eyes each time I proudly announced the discovery of a new vulnerability.)

*But Will*, you might be thinking,* giving an impish, all-powerful cybersecurity agent access to your home network is batshit*. And you would be correct! Nevertheless, I believe that a good way to understand the cybersecurity hellscape in front of us is to pay it a visit.

In the end, my experiment was revealing, but oddly reassuring, too. My little network gremlin showed me how vulnerable my home life would be to AI hacking, but it also told me how to make everything a lot more secure. In the end, I discovered that the best way to deal with AI hacking may well be having your own AI hacker.

## Maverick Model

I got the idea for the experiment after discovering Abliteration AI, a startup that offers access to powerful AI models with the usual guardrails removed.

Most mainstream AI models will refuse to respond to certain queries, and they will certainly refuse to find and exploit vulnerabilities in computer systems. But it’s possible to remove these restrictions by finding and modifying certain patterns within an open-weight model’s internal parameters. You can tweak the patterns that lead to refusals through a process known as abliteration.

Removing AI’s guardrails might seem risky, but it’s not uncommon. Academic researchers use these de-aligned models to better understand how AI actually works, while cybersecurity firms use them to probe software and systems for vulnerabilities. Technically speaking, Anthropic’s Mythos and OpenAI’s Astra work similarly: They’re basically conventional models that lack the usual cyber controls, with access limited to trusted customers for the time being. (The companies also offer wider access to models with a medium number of guardrails so that companies can vet their code and systems for problems.)

Abliteration AI offers several fully de-aligned models, the most powerful of which is a version of Z.ai’s latest agentic coding model, GLM 5.3. This puts similar cyber capabilities to Mythos and Astra right in your hands for as little as the cost of a pizza.

Devon, Abliteration AI’s CEO, believes that making de-aligned models widely available is smart defense: It will help good guys counter bad guys by probing systems for vulnerabilities and by mimicking the behavior of hackers, scammers, and, yes, rogue AI agents. (Devon asked that I use his first name only because his day job doesn’t know about his side project.)

“You have all these critical infrastructure companies, from airlines to banks, that are rolling out agents like crazy,” Devon says. “How do you make sure that a nefarious actor can't use some of these agents in a bad way?”

To start, I created an Abliteration AI account and installed a software harness called CyberStrike, which helps guide a large language model through different cybersecurity tasks.

Using CyberStrike, I asked the abliterated version of GLM-5.3 to take a look at my local network. A few moments later, it found around a dozen hardware systems on the same network—and catalogued several vulnerabilities.

My unruly helper told me, for instance, that my printer was misconfigured, which meant that anyone on the network could log into it. *That* could be a problem if there were sensitive documents—tax returns, bank statements, medical records—in the print queue.

The agent also noted that my Wiim stereo was leaking a lot of information. (It knew that the last song played was *Rein Me In* by Sam Fender and Olivia Dean, if you must know.) Anyone on the network could play what they wanted or adjust the volume. The model also found a bunch of internet-of-things (IoT) devices on the network with firmware that needed updating.

An ungovernable agent could be very useful to a hacker. But mine offered a number of helpful tips for keeping my network secure. Besides updating outdated firmware and securing the printer, it recommended putting IoT devices like smart speakers on a guest network; if one were compromised, it wouldn’t be able to see any of my PCs. Not bad for a model with no morals.

I also asked the agent to take a look at a directory containing a bunch of vibe-coded projects, including some that I turned into simple websites. It found dozens of problems, including unprotected API credentials and a misconfiguration that might let an attacker send out emails. Hardly surprising for a bunch of casually vibe-coded stuff, but still chastening. The sheer number of bugs makes me think I won’t be deploying a line of code without doing some AI vetting first.

## Fear Factor

Running an abliterated model is, to put it plainly, a bit scary.

I asked my agent to probe a Linux machine on my network for vulnerabilities. After running a bunch of scans, it reported that the machine seemed relatively secure. I then asked if it could figure out how to log in. It cleverly figured out a working username based on the name of other systems on the network. It tried a bunch of obvious passwords, which didn’t work. It also offered to write a script to try “brute forcing” the password, but I told it to stand down.

To my amazement, the agent then found a cryptographic key on my machine, used it to log in without a password, and started hunting for the password in order to gain root access. I felt a moment of pure panic as I saw it rummaging around the directories. It made me wonder how far the agent might go in order to achieve its goal. Might it have hacked into something else, like a machine outside of my network, in search of the key? Probably not, but who knows with these agents.

Some behavior could prove even more precarious. When I connected to my Wi-Fi network a few hours later and asked the model to see if it could find any new machines, it not only found the router, but decided to try logging in by trying several common “admin/passwords” combinations. If it had decided to do this on an outside network, I could have been in big trouble.

Shaanan Cohney, a computer scientist at Tufts University who specializes in cybersecurity and the law, says that a cyber-reckoning does seem to be coming.

“Attackers are often early adopters,” Cohney says. “There’s also an asymmetry, in that to secure a castle, you need to make sure that there are no holes anywhere or no loose bricks in your wall. To invade a castle, all you need to do is to find that one loose brick.”

Over the long term, Cohney says, the proliferation of cyber-capable models may make software more secure in general. The challenge is that many companies aren’t thinking about shoring up their defenses. “Most organizations have other things to worry about,” he says.

After all that, I shut down the model and went back to using a regular, fully aligned version. Claude Code or Codex will only do certain things related to cybersecurity, like help you configure your laptop’s firewall. But at least they won’t hack your system before you know it. Hopefully.

## AI Hacking for All

Unless open-weight models are banned outright, advanced AI hacking capabilities will soon be very widely available. My experiment made me think that this might be just what we need. Assuming that bad guys will have access to AI, shouldn’t we all use it to defend ourselves?

“We need to help people use these capabilities,” says Aleksander Mądry, an MIT professor who studies AI safety and who is currently on leave while he works for OpenAI. “I do think there will be room for open source and independent tools. If only because, ultimately, these kinds of approaches have the real staying power in the world of security.”

Mądry notes, however, that a key issue may be ensuring that those who manage critical infrastructure like power plants or financial markets have access to more powerful AI than the average script kiddie (or AI writer).

Using AI that lacks regular guardrails is both thrilling and alarming. But if a cyber-reckoning is coming, then it’s probably time to tool up.

*This is an edition of***Will Knight’sAI Lab newsletter**. Read previous newsletters** here.**
