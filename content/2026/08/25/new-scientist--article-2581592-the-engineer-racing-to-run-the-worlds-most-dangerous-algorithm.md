---
title: The engineer racing to run the world’s most dangerous algorithm | New Scientist
source_url: https://www.newscientist.com/article/2581592-the-engineer-racing-to-run-the-worlds-most-dangerous-algorithm/?utm_campaign=RSS|NSNS&utm_content=home&utm_medium=RSS&utm_source=NSNS
source_site: New Scientist
source_slug: new-scientist
scraped_at: '2026-08-25T16:50:34Z'
published: '2026-08-25T00:00:00Z'
description: Craig Gidney is largely unknown outside of quantum computing, but his
  pioneering work on quantum circuits could have huge consequences for us all, ushering
  in both useful quantum computers, and the end of digital privacy and security as
  we know it
image: https://www.newscientist.com/wp-content/uploads/2026/07/SEI_306263420.jpg
---

![](https://www.newscientist.com/wp-content/uploads/2026/07/SEI_306263420_5da1ce.jpg?w=840)

When I first started reporting on quantum computing several years ago, I had a lot to learn about the workings of these complicated, potentially groundbreaking machines and the cast of characters leading their development. Since then, I have been lucky to speak with many of them. But there is one person who has always eluded me – until now.

Everyone with ties to quantum computing seems to know the name Craig Gidney. I’ve also noticed that any study he has co-authored in recent years has made waves. Yet Gidney, who is based at Google Quantum AI in California, has written no books, gives no splashy keynote lectures to general audiences and rarely speaks to the press. One of the few digital traces of him is his rather technical blog.

It wasn’t merely my curiosity that was driving me to want to speak to Gidney, though. He is working on finding a way to run what could be the world’s most dangerous algorithm on quantum computers. That makes him a hugely consequential figure, as if and when this algorithm does run on a real machine, it could unleash a crisis known as Q-Day, when it will suddenly become possible to crack the encryption systems that secure everything from our emails to our bank accounts.

Advertisement

To understand Gidney’s story, it helps to start with encryption. Today, much of our private data is protected by encryption systems that can’t be broken without solving a difficult mathematical problem. One common choice is factoring very large numbers. Another involves abstract mathematical objects called elliptic curves. Conventional computers struggle to solve these problems, so our data and savings remain safe. But in 1994, theoretical computer scientist Peter Shor at the Massachusetts Institute of Technology discovered that a large enough quantum computer would excel at these challenges. The countdown to Q-Day, then, is really a countdown to a quantum computer successfully running Shor’s algorithm.

In the 1990s, Q-Day seemed more distant science fiction than real threat, because quantum computers were themselves not real. These machines derive their power from the quantum effects that govern their basic building blocks, qubits. A truly powerful quantum computer would need millions of qubits, and that has long seemed out of reach. But the tide is turning. Several firms and research teams have made remarkable progress in the past few years, prompting the question: how soon could Shor’s idea be implemented for real?

It is largely Gidney’s work that has some people thinking it could be worryingly soon. For several years now, he has been leading the charge on how to make Shor’s algorithm run on smaller quantum computers – ones that we could more plausibly build in the near future. If Shor provided a recipe for an ideal-case scenario, Gidney’s work is akin to discovering how to make it work with as minimal a pantry of ingredients as possible.

So, when I finally secure an interview with Gidney, I am intrigued to find out the truth about this shadowy quantum wizard. One ordinary Monday afternoon, he logs on to a video call from a hotel room in California, where he is attending a conference. When the room turns out to be mysteriously devoid of chairs, he simply sits on the floor – and we begin.

Speaking to the man himself, though, it is clear that unleashing chaos really isn’t his goal. In fact, he tells me that his goals are twofold: to prove that quantum computers can work, and to inform cryptographers on how to keep us safe from them.

Gidney’s fascination with quantum computers is about more than just the machines themselves. Most physicists see the world as fundamentally quantum in nature, with its most basic building blocks being quantum particles and fields. Gidney views building quantum computers as an attempt to tap into the fundamental structure of reality. “The whole universe is made out of quantum information at its foundational level and we can’t manipulate it,” he says.

When it comes to the human-scale world of chairs, bricks and ovens and so on, we can buy gadgets that tell us nearly everything about them: thermometers, cameras, rulers and more. Could there be a quantum version of all of that? This is what drives Gidney. “I just want the quantum computer to work,” he says. In this light, his focus on Shor’s algorithm is a means to an end, not the end in itself. It is simply the clearest, most direct route to proving that quantum computers are worth the hype.

The question of how exactly quantum computers will be useful is still debated. One oft-cited possibility is that they could be brilliant at simulating new candidate drug molecules, but no one has yet shown how this could be done in a way that reliably and unambiguously bests all conventional simulation methods. Ditto for myriad other applications, from optimising airline schedules to discovering new sustainable materials.

But Shor’s algorithm is an exception. Unless the laws of quantum mechanics are incorrect, there is no question that only a quantum computer could run Shor’s algorithm. “I really like it as a proof of quantumness. If you do it with a quantum computer, there could be no objection that quantum computers work,” says Gidney. Additionally, it shares some features of algorithms that could be useful for, for instance, chemistry calculations. So, Gidney’s hope is that nailing the implementation of Shor’s algorithm would have a real knock-on effect in making quantum computers more useful for other tasks.

# **Higher dimensions**

Certainly, there is also a dark side to Shor’s algorithm, which raises questions about the responsibilities of those studying it. But before we discuss that, I want to know what Gidney’s secret is. He has a reputation as a singular driving force in making quantum algorithms better suited for real-world quantum computing hardware. How does he do it?

Quantum computing wasn’t originally part of his career plans, he tells me. When he joined Google in 2017 it was as a software engineer, not a quantum computing researcher. But he was already curious about quantum algorithms and began teaching himself the subject. “It wasn’t taught to me,” says Gidney. “I was working through textbooks before I joined the quantum computing team.”

As we talk, I realise he has a mental model of the quantum world that is starkly different from the one I learned studying quantum theory at university. In my mind, the quantum realm consists of particles and fields, which, sure, can be strange, but still reside in three spatial dimensions. Gidney thinks in terms of quantum information instead, and seems to be comfortable within abstract, higher-dimensional spaces where mathematical representations of interactions between qubits live. “A qubit is the foundation of my understanding of quantum physics,” he says.

When it comes to running Shor’s algorithm – or indeed any quantum algorithm – what matters are quantum circuits, the recipes for sequential manipulation of the various qubits’ states. The better-optimised your circuit, the more you can do with the same number of qubits. This is what Gidney specialises in. Early on, he tells me, he taught himself to depict how quantum circuits work as a coloured, three-dimensional diagram and now spends hours on end in this abstracted world. One of the most pressing challenges for quantum computing is how to catch the errors the devices invariably make. For Gidney, the answers lie in these diagrams, which he has developed a strong intuition for. Sometimes, the arrangement of colours in the diagram just looks jarring, he says. “I think quantum computing has this reputation for being extremely difficult and it’s not completely undeserved – there are things that are very counterintuitive about it.”

# **Q-Day is coming**

So how close has research brought us to running Shor’s algorithm for real? In 2018, about a year after Gidney joined the quantum computing team at Google Quantum AI, the best available estimate indicated that researchers would need a quantum computer with more than 100 million qubits to pull that off. But in March, Gidney and his colleagues published a new estimate based on their circuit optimisation, saying it could, in fact, be achieved with an array of just 500,000 qubits. That is much larger than the state-of-the-art quantum computers today – the largest quantum computing array so far created has just over 6000 qubits – but still a 200-fold improvement. The finding was shocking enough to stir people into action. In the wake of the news, quantum cybersecurity firms were in high demand, with one seeing a tenfold increase in inquiries from businesses looking to become more quantum-safe.

That estimate from Gidney and his colleagues deliberately left out some details of how the quantum circuits were configured as a safety measure because of the algorithm’s connection to encryption. Yet, within only three months, André Schrottenloher at the Inria Centre at Rennes University in France filled in most of those hidden details. Though his solution wasn’t identical to that of Gidney and his colleagues, it underlined the interest and importance of the work that they had done. It wasn’t meant to be a challenge, but it inspired other researchers. “Because of this element of not telling people the circuits, the paper drew interest and people realised ‘oh, actually, it is very possible to improve quantum circuits’,” says Gidney. “I think it’s sort of delightful.”

![](https://www.newscientist.com/wp-content/uploads/2026/07/SEI_306602849.jpg?w=840)

All this brings me to perhaps the most important question I want to ask Gidney. Does he worry his work could be immensely harmful in nefarious hands? Gidney says he acknowledges that his work has contributed to mounting pressure on businesses and governments everywhere to begin to change their encryption methods in the face of a possible quantum threat. But that’s not a bad thing, he also reckons. “I’m very happy that it seems like we’ve managed to convince the security community to start doing things sooner rather than later,” he says. “Last year, I was a little bit worried about how much people seemed to be ignoring it.”

He doesn’t want to speculate on how soon Q-Day may happen, but in his view, the work he is doing ought to help blunt its impact. Indeed, we do have ways of protecting ourselves post-Q-Day. In the US, the National Institute of Standards and Technology began testing “post-quantum” encryption algorithms in 2017, and in 2022 its researchers announced several that ought to become the new standard for safe and reliable encryption. Gidney says his work is helping to explore how much time we have to implement these protections, an engineering process that will be costly and difficult. “We don’t want it to be the case that people underestimate how expensive these things [needed for implementing protection] are, and they’re not done in time,” says Gidney.

Overall, though, Gidney is optimistic about the future of quantum computing. His work on error correction and circuits isn’t just about Shor’s algorithm, but about getting quantum computers to a point that they work well enough to do useful jobs. On his blog, he has written that he expects a massive jump in quantum error correction, which will improve how reliably quantum computers can run complex programs. The way he speaks about it is permeated with unwavering positivity.

But he surprises me when I ask whether he will still be optimising quantum circuits in 10 or 15 years. “I don’t know,” he says. What gives him pause is the rapid development of artificial intelligence and large language models (LLMs) like ChatGPT. “It may be that two to five years down the road you give them a circuit to optimise, and they just do things that I wouldn’t think of, and everything I would think of they would think of [too]. But we’re not there yet,” he says.

I came into my chat with Gidney curious about his work’s potentially detrimental impact on privacy. I left it understanding that there is nothing all that mysterious or shadowy about him. Craig Gidney isn’t some dangerous figure looming over the burgeoning quantum computing industry, he is just deeply intrigued by quantum information – and really good at thinking about it.

Still, whether he intends it or not, he stands at a tricky intersection between technological benefit and risk. When it comes to Q-Day, however, the flag that he’s waving could certainly help us avoid catastrophe.
