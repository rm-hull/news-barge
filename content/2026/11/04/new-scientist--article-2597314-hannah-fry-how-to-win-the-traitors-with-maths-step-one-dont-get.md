---
title: 'Hannah Fry: How to win The Traitors with maths (step one, don’t get made a
  traitor)'
source_url: https://www.newscientist.com/article/2597314-hannah-fry-how-to-win-the-traitors-with-maths-step-one-dont-get-made-a-traitor/?utm_campaign=RSS|NSNS&utm_content=home&utm_medium=RSS&utm_source=NSNS
source_site: New Scientist
source_slug: new-scientist
description: With a little help from Alan Turing and Thomas Bayes, I came up with
  a mathematical model I hoped would help me win The Traitors. Unfortunately, events
  then got in the way, writes Professor Hannah Fry in her latest column
image: https://www.newscientist.com/wp-content/uploads/2026/11/SEI319273841-1.jpg
published: '2026-11-04T00:00:00Z'
scraped_at: '2026-11-04T14:30:44Z'
categories:
- Science
- Technology & Software
people:
- Alan Turing
- Alzheimer’s
- Dmitry Davydov
- George E
- Hannah Fry
- Joanne McNally
- Julie Hesmondhalgh
- Maya Jama
- P. Box
- Richard E. Grant
- Thomas Bayes
locations:
- Argentina
- England
- Russia
- UK
organisations:
- BBC One
- New Scientist
---

![Hannah Fry appearing on The Celebrity Traitors](https://www.newscientist.com/wp-content/uploads/2026/11/SEI319273841-1.jpg?w=840)

*The Celebrity Traitors*In the late 1980s, in Soviet-era Russia, a young psychologist called Dmitry Davydov came up with a game about power and information. He called it* Mafia* and originally intended it as a teaching device, a way to demonstrate how a small, informed minority could manipulate the dynamics of a much larger, uninformed group and wield outsized power over those who were left floundering in uncertainty and paranoia.

Almost 40 years later, that game has evolved into *The Traitors* – a TV show that is such a massive cultural phenomenon in the UK that the opening episode of this year’s celebrity edition drew more viewers to BBC One than watched England’s World Cup semi-final against Argentina.

And recently I found myself in the middle of it.

Advertisement

In case you’ve been living under a rock, or just happen to have better things to do with your life than watch reality television (in which case, lucky you), the premise is simple. A small number of players, the traitors, secretly know who is on their side and get to “murder” someone each night. The remaining players, the faithful, are tasked with working out who the traitors are, voting to banish one suspect each evening. Inevitably, they spend most of their time rounding on innocent people and making them disintegrate. Which I strongly suspect might be at least half of what makes the whole thing so damn entertaining.

Here’s the thing. When I got the call asking if I wanted to be on the show, of course I jumped at the chance. A game of incomplete information? That’s a mathematician’s dream, I thought. What a fun, stress-free way to try out some of my theories.

On reflection, past me was an idiot. But we’ll come to that.

The challenge, as I saw it, was to find a way to cut through the uncertainty. All I had to do was monitor the evidence as the game unfolded, use the patterns in people’s behaviour to identify the traitors and then just persuade everyone else to vote them out. Bish bash bosh, victory.

I started by combing through every previous series of the UK show, turning the joyful, chaotic mess of the series into a clean, delicious spreadsheet, determined to use all the statistical tricks I had at my disposal. Who voted for whom? Who travelled in cars together? Were there subtle statistical differences in the way traitors and faithful behaved that might give the game away?

It turned out there were. For example, I discovered that traitors often make what I came to think of as “burn votes”. They don’t necessarily want to send down an innocent person, nor do they want to persuade others into joining a stampede, drawing attention to themselves in the process. So, instead, they throw their vote away on someone nobody else is voting for.

They will also vote to banish their fellow traitors, but only when the writing is already on the wall. Someone who suddenly joins the vote against a traitor on the night they are finally banished, having never voted for them before, was a signal worth keeping an eye on.

There were clues pointing in the other direction, too: failing to vote for a traitor on the night they are banished turned out to be a good signal that someone is faithful. And then there was a particularly ingenious observation made by viewers online: the producers often send the players who were shortlisted for murder into breakfast last. Occasionally, they throw one traitor into that group to keep everyone guessing, but never two. Which means that if someone arrived late to breakfast alongside a player who was subsequently revealed to be a traitor, that was a potentially useful clue that they were faithful.

![Joanne McNally, Maya Jama, Julie Hesmondhalgh and Hannah Fry at breakfast in The Celebrity Traitors](https://www.newscientist.com/wp-content/uploads/2026/11/SEI319273852-1.jpg?w=840)

*The Celebrity Traitors*

As far as I could tell, there were no surefire ways to identify someone as a traitor (although Richard E. Grant would later do a spectacular job of proving me wrong). The faithful are so gloriously unpredictable (ahem. Joanne McNally) that anything suspicious could almost as easily have been done by a perfectly innocent player. But even so, buried in the noise, there were some small signals that could accumulate over time.  
Fortunately, there is a neat mathematical way to combine lots of weak evidence together – and it just so happens to have been used by Alan Turing to help crack the enigma code in the second world war. So, inspired by Turing, with a little help from our mutual, close personal friend Thomas Bayes, I set about building a Bayesian model that I could bring with me into the castle.

It’s actually pretty simple: a points system that lets you update the odds of someone being a traitor as you go. The scores came from what had happened in previous series, and are almost entirely based on people’s voting patterns. +0.47 for a burn vote. -0.83 if you fail to vote for a traitor on the night they go down.  
For the nerdier among you, the units I was using are nats – a measure of how strongly the accumulated evidence favours one hypothesis over another – but you can just think of them as traitor points.

I was as confident as I could be that, at the very least, the famous words of statistician George E. P. Box would prove true: “All models are wrong, but some are useful.”

Unfortunately, there was one rather significant problem with my plan. Within about 15 minutes of arriving in the castle, they made me a traitor. (Technically I could have refused, but it happened in such a way that it would have meant my immediate downfall.)

I went back to my room and sobbed into my spreadsheets.

Still, I’m not about to let the small matter of being made a traitor (and catastrophically failing to be deceitful on national television) get in the way of a good mathematical experiment. So, now that the final has aired and I know the way that the votes fell, I can finally run the numbers to see how the model would have played out in real time.

And I’m delighted to say that the maths worked. Brilliantly, in fact. At every single round table, the maths has a traitor as top, or joint top. Not every innocent player escaped suspicion, and the model certainly wasn’t infallible. But there really are signals buried in that noise, and you really can use mathematics to detect them. (And yes, the irony that literally being buried is what got me into this mess is not lost on me).

The trouble is, a mathematical model has one enormous advantage over a contestant on *The Traitors*. It doesn’t have to convince anyone to trust it. It doesn’t have to worry about being murdered or defend itself against accusations over breakfast, while trying to remember what normal facial expressions look like. And so even if I’d been a faithful, I suspect there was never any realistic chance of putting the mathematics to use within the game itself. Because, as* Mafia* was designed to demonstrate, the real power in a game like this isn’t just knowing the truth, it’s being able to shape what everyone else believes.

And so, George, it turns out some models *are* right. It’s just that, sometimes, that’s the least of your problems.

![](https://www.newscientist.com/wp-content/uploads/2026/10/SEI317847486.jpg)

My lovely father died of Alzheimer’s last year, and since then, I’ve been digging into the disease to try to understand what happened to him. I was astonished to discover that scientists think it may start in the nose, says New Scientist’s new columnist, Professor Hannah Fry
