---
title: Quantum trick lets you share your location super securely
source_url: https://www.newscientist.com/article/2599509-quantum-trick-lets-you-share-your-location-super-securely/?utm_campaign=RSS|NSNS&utm_content=home&utm_medium=RSS&utm_source=NSNS
source_site: New Scientist
source_slug: new-scientist
description: A new experiment demonstrates how quantum devices could verify a person’s
  position extremely securely, making it much harder to hack sensitive messages.
image: https://www.newscientist.com/wp-content/uploads/2026/11/SEI_321132085.jpg
published: '2026-11-18T00:00:00Z'
scraped_at: '2026-11-18T20:30:29Z'
categories:
- Science
- Technology & Software
people:
- Florian Speelman
- Gautam Kavuri
- Krister Shalm
- Philip Verduyn Lunel
- Robert Malaney
- Verduyn Lunel
- Wolfgang Löffler
- Yanbao Zhang
locations:
- Boulder
- China
- Colorado
- Europe
- Hefei
- Netherlands
- Paris
- Tennessee
organisations:
- Leiden University
- NIST
- National Institute of Standards and Technology
- Oak Ridge National Laboratory
- QPV
- Rolls Royce
- Sorbonne University
- University of Amsterdam
- University of Colorado Boulder
- University of New South Wales Sydney
---

![NIST's campus in Boulder, Colorado](https://www.newscientist.com/wp-content/uploads/2026/11/SEI_321132085.jpg?w=840)

Financial institutions and critical infrastructure could be made far more secure in the near-future using quantum particles.

For years, researchers have predicted that quantum particles could enable someone to share their location, and to verify someone else’s, in a way that is exceedingly difficult to hack. This would allow one branch of a bank to confirm that a request for funds or client information is coming from another branch and not from a hacker. Likewise, hackers could be stopped from trying to remotely control a power grid, a nuclear plant – or even commercial freezers, which have recently been hacked across Europe.

Gautam Kavuri at the University of Colorado Boulder and his colleagues have now shown that quantum devices really can provide such location verification, offering a level of security impenetrable to most hackers.

Advertisement

“From a security perspective, it’s sort of the gold-plated Rolls Royce of protocols. It’s got the best security you can have in principle, while making the least assumptions,” says team member Krister Shalm at the National Institute of Standards and Technology (NIST) in Colorado. “And you can actually do it.”

In the researchers’ experiment, two verifier devices had to confirm the location of a third device called the prover. Each device was in a different location: the verifiers were 195 metres apart in different labs and the prover was in a third location between them. Kavuri says it was important for these devices to be in different rooms on the NIST campus, rather than all in the same lab, because this is closer to a practical scenario in the real world. The devices were connected with electrical cables and optical fibres and could exchange quantum particles of light that had been connected into pairs through the inextricable link of quantum entanglement.

To begin the new quantum position verification (QPV) protocol, a verifier would send one photon from an entangled pair to the prover and, simultaneously, each verifier would also send a random number that instructed the prover on which particle property to measure. Next, the prover sent the outcome of that measurement to both verifiers. They used the time it took to receive this information to calculate the prover’s position.

Several quantum tricks made this procedure more secure than any conventional one. First, quantum information, such as that carried by particles of light, can never be copied or cloned surreptitiously. Additionally, the researchers leveraged a procedure called a Bell test, which is specific to entangled particles, and would be failed if a hacker tampered with them. The net effect was that any conventional strategy for faking the position would set off one of these quantum safeguards.

In this way, the new work builds on past theoretical results that promise to make it nearly impossible for position verification to be hacked once you go beyond conventional communication and turn to quantum tricks, says Philip Verduyn Lunel at Sorbonne University in Paris.

“QPV is a possible ‘killer app’ for quantum networks,” says Wolfgang Löffler at Leiden University in the Netherlands. Although several outstanding problems will need to be solved to make this protocol fully practical, the new experiment is a big step towards doing just that, he says. Löffler says that it must have been a massive effort to get all the timings and device fidelities just right.

![](https://www.newscientist.com/wp-content/uploads/2023/09/13213251/SEI_171463847.jpg)

A network that connects quantum devices and a central server that spans Hefei, China, can allow multiple secure quantum chats at once

“They have really pushed all the experimental constraints to their limit,” says Verduyn Lunel.

Robert Malaney at the University of New South Wales Sydney says the new protocol is attractive for practical applications in part because it is compatible with conventional wireless communication infrastructure. But if several nefarious actors could quantum entangle devices that they use for hacking, they could still cheat the current implementation of the protocol, he says. This is because, in this case, the hackers could perform some computations without having to send each other extra messages.

Going forward, the protocol must also be adapted to work over longer distances, which could require new computational steps and devices, says Florian Speelman at the University of Amsterdam. This will be a challenge, but the new work still moves us closer to QPV being a reality, he says.

The researchers are now working on tweaking their protocol to make it more resilient to any photons getting lost as well as being more impervious to hackers looking to leverage quantum entanglement, says team member Yanbao Zhang at Oak Ridge National Laboratory in Tennessee.
