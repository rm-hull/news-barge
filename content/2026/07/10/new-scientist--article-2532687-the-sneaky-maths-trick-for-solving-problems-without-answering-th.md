---
title: The sneaky maths trick for solving problems without answering them
source_url: https://www.newscientist.com/article/2532687-the-sneaky-maths-trick-for-solving-problems-without-answering-them/?utm_campaign=RSS%7CNSNS&utm_source=NSNS&utm_medium=RSS&utm_content=home
source_site: New Scientist
source_slug: new-scientist
scraped_at: '2026-07-10T11:17:44Z'
published: '2026-07-10T00:00:00Z'
description: How can you have a proof without proving anything? Mathematicians found
  a way and, in the process, came to blows over it – but 100 years on, this trick
  is a common part of modern maths, says columnist Jacob Aron
image: https://images.newscientist.com/wp-content/uploads/2026/07/01190421/SEI_302858031.jpg
---

![](https://images.newscientist.com/wp-content/uploads/2026/07/01190421/SEI_302858031.jpg)

How do you prove a proof? Sometimes, you don’t

Lucidio Studio, Inc./Getty Images

A mathematician opens her office door to find a small fire. Without panicking, she looks around the room and spots a fire extinguisher. “Ah, a solution exists!” she says, before closing the door and continuing on with her day. Simply knowing it is possible to extinguish the fire is proof enough that the problem can be solved – why bother to actually go through the motions to do it? This old joke sums up how a lot of modern mathematics gets done, thanks to a sneaky tactic for problem-solving: the non-constructive proof.

It is a tricky idea to get your head around, so here’s a mostly non-mathematical example. Say there are 367 people in a room – what are the chances that two of them share a birthday? The answer is 100 per cent, because (assuming we account for leap years) there are only 366 possible birthdays, and each person must have a birthday, so at least two people must have the same birthday. This is an example of what mathematicians call the “pigeonhole principle” – the people are the pigeons, the holes are the birthdays – and it’s a classic way of approaching non-constructive proofs. We know that two people must share a birthday, even if we have no idea who out of the 367 people they are.


Traditionally, proofs were the exact opposite of this. If you proved something, generally you had grasped a concrete mathematical object and laid it out on display for everyone to see. That all began to change in the 19th century, when non-constructive proofs became a more powerful and popular tool in a mathematician’s arsenal. At the forefront of this new way of doing mathematics was David Hilbert, one of the great mathematicians of his time and, at least in the eyes of some, a troublemaker.

The problem Hilbert was investigating is a complex one and requires a little table-setting. Let’s start by thinking about a square. You can rotate a square by 90 degrees and it ends up looking the same – you may be familiar with this as being called rotational symmetry. Another way to describe it is that the square is “invariant” under 90-degree rotations.

Hilbert was interested in invariants, not for geometrical objects like squares but algebraic ones, like equations. For a given class of algebraic object, mathematicians had realised that there are essentially an infinite number of invariants. The question then became: how many do you actually need? Can you start with a few key invariants and use them to build any other invariant you like? Hilbert wasn’t the first person to tackle identifying a “generating set” for invariants – another mathematician, Paul Gordan, had spent his entire career investigating it. Gordan had discovered finite generating sets for a few objects, but his proof was messy and complex. He was astonished, then, when in 1888 Hilbert came along and proved that it was true for a much larger class of algebraic objects – without actually specifying the make-up of the generating sets. He did this by first assuming that there is an invariant that cannot be produced by a generating set, and then showed that this would lead to the creation of an infinite stream of more invariants in a manner that isn’t allowed by the algebraic rules Hilbert was operating in – a logical contradiction. The only way to resolve the contradiction then is that the generating set must always exist.

![New Scientist. Science news and long reads from expert journalists, covering developments in science, technology, health and the environment on the website and the magazine.](https://images.newscientist.com/wp-content/uploads/2025/06/16102059/the_daily_2025_ed_newsletter_landingtiles_2400px5.jpg)

Gordan’s reaction to this non-constructive proof was initially negative. “That is not mathematics, that is theology,” he said, aghast that Hilbert would ask him to believe in the existence of a generating set without providing one – surely that doesn’t count as an answer? Gordan came around to Hilbert’s way of thinking though, later stating that “theology does have its advantages”.

Hilbert’s battles weren’t over yet. Just as he was a young upstart challenging Gordan, so too came a younger upstart in the form of L.E.J. Brouwer. Hilbert spent a good few decades building up the mathematical philosophy of formalism, which essentially takes the view that mathematics is a game of manipulating symbols in a logical way to produce proofs, without being too concerned about the real-world or mathematical objects those symbols might correspond to. For formalists, a non-constructive proof is simply one of many ways to win the game.

Brouwer hated this idea. His philosophy was intuitionism, which argues that mathematics is a creation of the human mind. He rejected the manipulation of symbols as the underlying activity of mathematics, seeing them only as a way for relaying thought from one mathematician to another. In this view, a non-constructive proof is cheating – for a mathematical object to be real, you must be able to construct it in your mind.

Where these two philosophies really clash is over something called the law of the excluded middle. This is an ancient principle of logic that states that for every logical proposition, either that proposition is true or its negation is. In other words, if I say, “Hilbert was a cat”, either that must be true or Hilbert wasn’t a cat (it’s the latter, for the avoidance of doubt).

![](https://images.newscientist.com/wp-content/uploads/2026/07/01190427/SEI_302848044.jpg)

Human mathematician David Hilbert

ullstein bild via Getty Images

This may seem obvious, but it turns out to be a useful mathematical tool. In Hilbert’s 1888 proof, he assumed that “not all invariants can be produced by a finite generating set” and found a contradiction, making that proposition false. By the law of the excluded middle, “all invariants can be produced by a finite generating set” must be true, even without showing how to construct such a set.

Brouwer’s objection was in applying the law of the excluded middle to an infinite set of objects, as Hilbert was doing. He had no issue in using it for finite sets, because, in principle, you could check every object in the set and convince yourself that they have or don’t have a certain property. But for infinite sets, this can’t be done.

Hilbert thought this was ridiculous, comparing restrictions on the law of the excluded middle to “prohibiting the boxer the use of his fists”. Brouwer, in turn, referred to Hilbert as “my enemy”. This was a problem, because both men worked on *Mathematische Annalen*, then and today one of the most important journals in mathematics. Hilbert was one of three editors, alongside Albert Einstein, while Brouwer was on the editorial board. Hilbert was so incensed at Brouwer’s influence over the journal that in 1928 he fired the entire editorial board just to get rid of him. In response, Einstein resigned from his post as well, asking “What is this frog and mouse battle among the mathematicians?”

In practical terms, Einstein was right to dismiss the argument. Today, very few mathematicians concern themselves with an explicit philosophy, and the vast majority are happy to employ non-constructive proofs as a useful tool. You could say this meant Hilbert won, and certainly Brouwer became an increasingly isolated and irrelevant figure after his dismissal from *Mathematische Annalen*. But as I’ve written previously, Hilbert’s formalism would soon be dealt a fatal blow by Kurt Gödel, whose incompleteness theorem showed that the game of manipulating symbols could never be fully consistent. Gödel was not an intuitionist – in fact, his completeness theorem, a precursor to the incompleteness one, relies on the law of the excluded middle – but he did take inspiration from Brouwer in his own fight against Hilbert.

Gödel and Brouwer’s ideas would later become important in computer science, informing the work of Alan Turing and questions about which problems are computable. Today, such ideas are coming back into fashion as mathematicians turn to AI and formal proof verification, in which every step of a proof must be made machine-readable to verify it as true. That, in turn, may one day lead to a non-constructive proof, verified as logically true, that mathematicians nevertheless don’t fully understand because it was created by an AI that can’t explain it to human minds. If that comes to pass, Brouwer will get the last laugh.

Topics:
