---
title: Experts warn expired credit cards can be brought back from the dead to make
  contactless payments
source_url: https://www.techradar.com/pro/security/experts-warn-expired-credit-cards-can-be-brought-back-from-the-dead-to-make-contactless-payments
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-22T01:46:39Z'
published: '2026-08-21T00:00:00Z'
description: Back from the dead to pay for someone's grocery run?
image: https://cdn.mos.cms.futurecdn.net/fL8Ba8CiJjt2qsAVpr6UmK-2560-80.jpg
---

![A credit card passed between two hands](https://cdn.mos.cms.futurecdn.net/fL8Ba8CiJjt2qsAVpr6UmK.jpg) 

- **Researchers show how an expired contactless card can still complete a real purchase because the expiry date the terminal reads is not covered by its signature**
- **The attack needs physical possession of the discarded card and two ordinary smartphones, and results vary per bank, with Visa cards being susceptible in testing**
- **Existing EMV protections can detect the relay, but they are optional and were not enabled on any card or terminal tested, and neither Visa nor the notified banks have confirmed a fix is in the works**

For a layman, the date printed on a credit card looks like a hard stop, but that might not always be the case.

Researchers at the University of Massachusetts Amherst found that a 'zombie card' past its expiration date can be persuaded to complete a contactless purchase at a real checkout terminal, creating a real security threat.

The irony is that it is not that EMV cryptography is not bypassed in any way, but rather that card expiry is enforced in a different way for contactless payments, as a policy check between two parties rather than as a fixed property of the card itself, and interestingly, the parties do not always know who is the one checking.

## Dead plastic can still be used to pay under certain conditions

Building on the last part, a contactless transaction involves a card, a point-of-sale terminal, the merchant's bank, a card network, and the issuer. Each holds a fragment of the decision that eventually results in a successful or declined card transaction.

The EMV contactless flow is only selectively authenticated: some fields travel between the card and terminal in unencrypted text and are linked to cryptographic verification later, opening a potential attack vector for users with physical access to an expired card.

The exposure here is not that those fields can be read, since the expiry date is printed on the card anyway, but that it can be changed with relative ease. The Application Expiration Date that the terminal reads sits in the unprotected portion.

In the Visa configuration the team tested, that field is not covered by the card's digital signature and is subsequently not cryptographically bound to the expiry value the issuer sees in the online authorization request.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

While this should not be the case, it opens an attack vector for a device between the card and the terminal that processes the charge by simply modifying the expiry value to one that is still valid. The issue is compounded by a second issue: cards carry an expiry date inside the digital certificate used to establish the card-to-terminal conversation, and researchers have found that the certificate outlasts the printed date on the plastic. In essence, a check that might have caught the problem is looking at a clock set further ahead.

The scope of the attack, however, is narrow: it affects Visa contactless cards only, with Mastercard, Discover, and American Express rejecting the altered expiry outright. It also requires physical access to the card and two smartphones to pull it off, making it a slightly more complex endeavor, to say the least.

The irony is that EMV does have a protection that would essentially undo such an attempt altogether: Relay Resistance Protocol, which measures timing to detect an inserted relay and can stop the transaction altogether, but it remains optional and was not enabled on any of the terminals or cards the researchers tested.

The team notified Visa and the relevant banks in May 2025 and again in December 2025, supplying a reproduction guide, transaction traces, and a video. Visa's report passed initial triage, and the company's red team was reproducing it.

However, as of publication, neither Visa nor the notified banks had confirmed a mitigation attempt, and Visa also did not respond to a press request from *The Register* for comment.

The underlying failure, however, is based on how payment decisions have now spread across multiple players, including chip, terminal, network, and bank architectures, all of which assume that expiry is someone else's problem, an approach that could come back to haunt them and their customers. For now, the researcher's advice remains important until a fix is rolled out: stop treating dead plastic as harmless, destroy the underlying chip, and cut through the card numbers to prevent abuse.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Rahim Amir](https://cdn.mos.cms.futurecdn.net/9xKZFBamtEZKSChRvywbPB.png)

Rahim Amir is a UAE-based tech writer who enjoys building PCs as much as he enjoys writing about them. He has been professionally writing about PC hardware since 2023, focusing on buyer’s guides, hardware reviews, and sponsored content and features related to tech.

Having built hundreds of gaming PCs and being an avid gamer in his spare time, Rahim tends to have stronger opinions about hardware than most. This is particularly on display when he gets his way with powerful, but minimalistic RGB builds even as Small Form Factor (SFF) PCs come a close second.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
