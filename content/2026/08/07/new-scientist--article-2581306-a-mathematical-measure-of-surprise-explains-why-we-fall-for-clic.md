---
title: A mathematical measure of surprise explains why we fall for clickbait | New
  Scientist
source_url: https://www.newscientist.com/article/2581306-a-mathematical-measure-of-surprise-explains-why-we-fall-for-clickbait/?utm_campaign=RSS|NSNS&utm_content=home&utm_medium=RSS&utm_source=NSNS
source_site: New Scientist
source_slug: new-scientist
scraped_at: '2026-08-07T09:13:35Z'
published: '2026-08-07T00:00:00Z'
description: 'Why are we so susceptible to clickbait? Columnist Jacob Aron traces
  it to a surprising source: a mathematical framework that paved the way for much
  of how the modern world works'
image: https://www.newscientist.com/wp-content/uploads/2026/07/SEI_306237288.jpg
---

![](https://www.newscientist.com/wp-content/uploads/2026/07/SEI_306237288.jpg?w=840)

This one weird trick allows journalists to grab your attention! This kind of clickbait works because it promises information without actually delivering it – in fact, clickbait headlines go out of their way to be as uninformative as possible. A headline such as “Trump wins election” contains more information than “You’ll never believe who just won the election”, despite the latter containing far more words.

It might seem paradoxical that more information can be conveyed using fewer words, but there is a mathematical framework that explains exactly why this is the case. And this so-called information theory, first developed in 1948 at the dawn of the computer age, paved the way for how much of the modern world works.

The theory was born when Claude Shannon, a mathematician working at Bell Labs in New Jersey, was trying to solve a problem that plagues us even today: how to communicate when you have a bad signal. Bell Labs was then the research arm of the American Telephone and Telegraph Company, better known today as AT&T. It was very much the Google of its time, inventing everything from the transistor and solar panels to lasers – civilisation-altering stuff.

Advertisement

Shannon’s creation, while far more theoretical, is easily as important as those three. His mathematical breakthrough was to realise that the specific meaning of a message is irrelevant when attempting to communicate it. Or, as he put it in his famous paper *A mathematical theory of communication*, “semantic aspects of communication are irrelevant to the engineering problem”.

Instead, what matters is how surprising a message is – to put it in mathematical terms, the probability of a specific message being selected for transmission. It might seem strange to think of messages as having probabilities, but because they are built from a limited alphabet, in principle we can calculate them.

To take a very simple example, imagine we want to transmit the outcome of a coin flip as either H for heads or T for tails. Assuming the coin is fair, there is a 50 per cent chance of either outcome. If we land on H or T, either way, we will get new information with each flip. But what if the coin is doctored to always land on heads? In that case, we will transmit H 100 per cent of the time and T 0 per cent of the time, meaning that whatever happens, we aren’t communicating any new information.

Shannon’s insight was that we can perform this calculation for any message, and so quantify the information transmitted, using a formula now called Shannon entropy. It states that the entropy *H* is equal to -∑p(x)log(p(x)). Stick with me, let’s unpack this.

We have *x*, which is simply the message that we want to transmit, so in the coin example, this is either H or T. And the p(x) is the probability of message x occurring. If every message is equally likely, this is simply 1 divided by the number of possible message, but there can also be more complicated cases that I will ignore for this explanation.

Next, we need to take the logarithm of the probability. What is a logarithm? It’s like a reverse exponent: for example, if 23 = 2*2* 2 = 8, then log 8 = 3, in base 2. Finally, ∑ tells us that we should perform these calculations for all possible values of x and add them together.

That might seem complicated, but understanding the power of logarithms is key to information theory. In his paper, Shannon explained that your choice of base – the number of digits a system uses to represent numbers – determines the unit for measuring information. He proposed using base 2, as in the example above, resulting in a unit called binary digits, or “bits” for short – a name he took from his colleague, John Tukey. It is these bits, typically represented by a 0 or a 1, that underpin all our digital communications today.

To go back to the coin example, for a fair coin we have a probability of 0.5 for either heads or tails, and log(0.5) = -1. Plugging this into Shannon’s formula, we get –(0.5*-1 + 0.5*-1) = 1. In other words, a fair coin communicates 1 bit of information. For the doctored coin, the outcome is 0. It offers no surprises, so it can’t transmit information.

What does all of this have to do with clickbait? Well, surprise, or novelty, is the currency of journalism. There’s a saying that “dog bites man” isn’t news – it’s too commonplace an event – but “man bites dog” is worth a story. This is exactly the same intuition that drove Shannon’s mathematical formulation of information, but there are important moments when maths and journalism diverge. Remember, Shannon wasn’t concerned with the meaning of messages, but merely with the probability. Crucially, this says nothing about whether the information is accurate or meaningful.

The most famous example of this might be a headline published a few months after Shannon’s 1948 paper. The US presidential election that year was between the incumbent Harry S. Truman and his opponent Thomas E. Dewey. On the eve of the election, the *Chicago Daily Tribune* found itself in the unfortunate position of having to go to press for its early edition before the results were finalised. Based on polling at the time of press, the paper predicted that Dewey would win, running the headline “Dewey Defeats Truman”.

From Shannon’s point of view, this is information communicated perfectly. With two possible outcomes, and a roughly equal chance of either candidate winning, the headline communicates around 1 bit of information, very similar to the fair coin. The only problem is that, in reality, the polling was wrong and Truman had won, leading to one of the most gleeful pictures ever published of someone reading the news.

![](https://www.newscientist.com/wp-content/uploads/2026/07/SEI_306237600.jpg?w=840)

The paper’s error was unfortunate, but it also provided an early warning sign that Shannon’s theory doesn’t encompass the value we place on one piece of information over another – the semantic meaning that he was so dismissive of. In the 21st century, this gap became weaponised in the form of clickbait.

A clickbait headline has a single job to do: to get you to click it. This is a very different job to traditional print headlines like “Dewey Defeats Truman” (or indeed the correct “Truman Defeats Dewey”), which are designed to convey the maximum amount of information in the smallest possible space, constrained as they are by the realities of print. Shannon would strongly approve of this effort at efficient communication.

By contrast, the more information a clickbait headline provides, the worse it is at its job. To go back to the example at the start of this article, “Trump wins election” tells you everything you need to know. You might choose to click through and read the particular details, such as the vote share, but in the 2024 contest between Donald Trump and Kamala Harris, these three words efficiently communicate around 1 bit of information (you could even shorten it to just “Trump wins”).

The rise of Google and, more importantly, ad-funded online publications changed the calculation. The goal became for publishers to attract as many visitors to their website as possible to maximise advertising revenue. To do this, publications, whether knowingly or not, hacked Shannon’s information theory to exploit our attention. The headline “You’ll never believe who just won the election” primes us for information without delivering it, like a coin that is mid-toss. Only by clicking can you complete the communication as Shannon originally envisaged it. If it turns out to be an unsurprising, low-information article, too bad – the publication already got your click.

That’s not to say Shannon’s work isn’t useful today – far from it. As I said earlier, Shannon was attempting to figure out how to communicate in the face of bad signal, or as he put it, over a noisy channel. His entropy formula showed that, by studying the probability distribution of possible messages, we could encode them in such a way as to preserve them in the face of noise, giving rise to everything from streaming video to space travel. No one denies that Shannon’s information theory made the modern world, but what it can’t do is solve our modern information overload.
