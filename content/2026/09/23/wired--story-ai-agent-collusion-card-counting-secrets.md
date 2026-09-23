---
title: AI Agents Teamed Up to Cheat at Blackjack. Their Collusion Is Getting Harder
  to Spot
source_url: https://www.wired.com/story/ai-agent-collusion-card-counting-secrets/
source_site: Wired
source_slug: wired
scraped_at: '2026-09-23T19:40:09Z'
published: '2026-09-23T00:00:00Z'
description: A clandestine card-counting operation suggests we may need new ways to
  spot agent-to-agent deception.
categories:
- Technology & Software
- Science
- Business & Entrepreneurship
image: https://media.wired.com/photos/6ab16fccade3d66cae78d5ff/191:100/w_1280,c_limit/AI-Lab-How-Bunch-of-AI-Agents-Planned-Casino-Heist-Business.jpg
---

This week I bring news of a daring casino caper hatched by a pair of rogue AI agents—as well as the clever trick that revealed their antics.

After researchers instructed them to count cards during a game of blackjack, the agents—which were controlled by the same model—developed a spontaneous secret code to help them get ahead. Though the episode happened inside an Oxford University lab, rather than a real casino, it has troubling real-world implications: It suggests that agents deployed in industries like finance and ecommerce could figure out how to partner up and cheat in ways that are difficult to pick up on.

“When taken individually, these agents may seem entirely [benign],” says Christian Schroeder de Witt, a computer scientist at Oxford University who led the work and who has done pioneering research into agent collusion. “Once put together in a group, they can collude secretly.”

The agents knew their conversations would be monitored, so they devised a way to communicate while avoiding detection. When one agent said, “This dealer’s on a real hot streak! Every hand they pull a monster,” for example, that indicated that the next card would be of a certain value, and that the agent should bet $250. Most interestingly, their communications weren’t picked up by a system designed to spot signs of collusion in agent chatter.

Aaron Rose, a machine learning researcher who worked on the project, is also an avid card player, and figured the blackjack table might be fertile territory for devious agent partnerships. “It worked really well,” he says.

Schroeder de Witt’s group eventually figured out how to detect the conspiracy. Using a method known as mechanistic interpretability, they trained a smaller model to recognize telltale activations across the agents’ weights. Using a tool called Narcbench, they tested the approach on some medium-sized open-source models, and found they could tell when models intended to slip information to each other.

Crucially, however, spotting what was happening involved monitoring both agents—something likely to complicate detection in real-world scenarios where thousands of agents, some operated by different companies, may be deployed.

Carissa Cullen, a PhD student involved with the study, says the next step is to test whether larger models behave similarly. (The agents in the study were smaller versions of US models Llama and GPT-OSS and the Chinese models Qwen and DeepSeek.) The team saw some signs that larger models exhibit less of a detectable signal than smaller models, and they want to know if larger models are more likely to collude, and more likely to be secretive about it.

Evidence that groups of agents are more problematic than agents operating solo seems to be growing. One project, from Shanghai Jiao Tong University and the Shanghai Artificial Intelligence Laboratory, found that swarms of agents were considerably more dangerous when asked to carry out simulated disinformation campaigns and ecommerce fraud. They were better able to adapt to defensive measures, researchers reported.

“The big lesson is that it’s not enough to evaluate agents individually,” says Diyi Yang, a computer scientist at Stanford University who has studied collusion among agents. “Companies should closely monitor inter-agent interactions when agents interact repeatedly, even when their individual incentives seem benign.”

It’s not all bad: having thousands of agents collaborate on a task made it possible for OpenAI to solve previously intractable math problems. But groups of rogue agents working together have also featured in several recent high-profile hacking incidents. In May, a team of OpenAI agents hacked into the AI research platformHugging Face, and used a message board to share tips and ideas. Other models, including Anthropic’s Claude and Google’s Gemini, have also carried out alarming safety breaches.

Secret chatter adds a new dimension to this burgeoning problem, and it may not be the end of it. Another recent study, from a startup called Emergence AI, put agents controlled by frontier AI models in a virtual world to see what they would do. When tasked with making money, they repeatedly tried to devise ways to reach humans on the wider internet in order to sell them stuff. Most bizarrely, the agents eventually developed their own kind of slang. “They very rapidly evolved a language,” says Satya Nitta, Emergence AI’s CEO. “We don’t know why.”

The wider world isn’t ignoring problems with agentic misbehavior; it’s a hot topic at this week’s United Nations General Assembly. An independent scientific panel is set to discuss the OpenAI-HuggingFace incident, while Sam Altman is expected to call for international coordination on developing safe AI agents.

Despite this, some industries, including, ecommerce have become testing grounds for agentic AI. This week, for instance, Amazon said it would block Meta’s Muse AI agent from accessing its site, arguing that it violated its terms of use.

Schroeder de Witt says it’s entirely conceivable that agents tasked with finding deals start to work together—perhaps even covertly—in order to get a better deal, or to screw someone over. It will be crucial to study agent collusion and develop detection strategies as they proliferate, he says. “There needs to be more research and understanding what will happen when we have more agents in the economy,” he says.

*This is an edition of* **Will Knight’sAI Lab newsletter**. Read previous newsletters** here.**
