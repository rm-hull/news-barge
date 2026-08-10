---
title: Quantum voting trickery could make elections more secure | New Scientist
source_url: https://www.newscientist.com/article/2583747-quantum-voting-trickery-could-make-elections-more-secure/?utm_campaign=RSS|NSNS&utm_content=home&utm_medium=RSS&utm_source=NSNS
source_site: New Scientist
source_slug: new-scientist
scraped_at: '2026-08-10T13:38:04Z'
published: '2026-08-10T00:00:00Z'
description: In an election, how can you make sure that everyone's votes are counted
  but also kept entirely secret? Quantum mechanics may have the answer
image: https://www.newscientist.com/wp-content/uploads/2026/08/SEI_307616464.jpg
---

![](https://www.newscientist.com/wp-content/uploads/2026/08/SEI_307616464.jpg?w=840)

A combination of mathematical and quantum trickery baked into a voting system can guarantee, in theory, that every vote is counted and remains anonymous. The approach has now been tested to show that it works.

Many countries use some form of electronic voting in their elections, and the companies who make the machines have a wide range of tools to stop anyone from being able to interfere with the vote. Nevertheless, quantum physics has the potential to take those protections to the next level by guaranteeing a vote can never be undermined.

A few years ago, researchers in France came up with the theory behind such a quantum approach to voting. Now, both they and another, independent team of researchers have tested it in practice.

Advertisement

To see how the protocol works, consider a vote with four people who are deciding on whether to eat mushroom stew or a tofu stir-fry for dinner. They could use a pen and paper to vote, but they don’t trust each other, nor do they trust anyone else to administer the mini-election. Instead, they turn to the quantum approach.

The protocol says there needs to be four rounds of voting because there are four voters. Each voter is given a secret and unique “index” between 1 and 4, and they vote only in the round that matches their index. They all also receive a secret unit of information, or a bit, equal to 0 or 1. Each bit is random, but the total number of 1s given out must be even.

In each round of voting, everyone who doesn’t have a matching index transmits their bit. The person with the matching index keeps their bit the same to vote for the mushroom dish or changes it to vote for tofu. For example, if a voter, Alice, has an index of 2 and is given 0 as a bit, then in round 1, she simply transmits 0, effectively sitting this round out. In round 2, she sends 0 to vote mushroom or 1 to vote tofu. And then she effectively sits out rounds 3 and 4.

After each round, anyone who is collecting or stealing the voting information sees only a random sequence of 1s and 0s, with no way to tell who cast which vote. At the end of all voting, the votes can be tallied by determining whether the number of 1s stayed even or not. This is because whenever a person votes for tofu, the number of 1s changes, so if there are more rounds with an odd number of 1s than an even number, tofu wins.

But what if the person handing out bits and indexes is untrustworthy? This is where quantum mechanics comes in, as the four bits used for voting are replaced by four photons, or particles of light, prepared in a specific entangled state.

In the experiments that tested the protocol, this involved shooting lasers at a special crystal that then produced the photons. This process guaranteed that no one could know the exact details of each four-bit collection from the jump, but the friends could vote and tally the votes by interacting with their own photon. Moreover, any nefarious actor that tried to tamper with a photon could be detected by measuring the properties of the other three.

The researchers have tested the protocol both with two choices and four voters, and with 16 choices and and eight voters.

These are nice proof-of-principle experiments, says Mark Hillery at Hunter College in New York, who was not involved in the research. However, scaling the approach to larger elections poses several technical challenges, he says. Notably, the entangled states are fragile and have so far not been transmitted across large distances without losing their special quantum properties.

Because of this, the most likely near-term use for this voting protocol could be in smaller elections, such as among small councils, says Nicolas Laurent-Puig at Sorbonne University in France, part of the original team.

Joey Marcellino at the University of Geneva in Switzerland, who worked on the other team that tested the protocol, says that it could also power a secure and anonymous message board or distribute a secret computation across several untrusted quantum computers.
