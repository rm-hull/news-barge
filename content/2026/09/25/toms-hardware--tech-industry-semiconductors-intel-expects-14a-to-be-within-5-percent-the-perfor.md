---
title: Intel expects 14A to be 'within 5%' the performance of TSMC's A14 — conservative
  forecast clashes with 18A's frequency lead and promised 20% gains
source_url: https://www.tomshardware.com/tech-industry/semiconductors/intel-expects-14a-to-be-within-5-percent-the-performance-of-tsmcs-a14-conservative-forecast-clashes-with-18as-frequency-lead-and-promised-20-percent-gains
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-25T13:40:31Z'
published: '2026-09-25T00:00:00Z'
description: Which does not sound too good given prior projections.
categories:
- Technology & Software
- Hardware
image: https://cdn.mos.cms.futurecdn.net/XSmGCAUBerwsBhZgUEkxS-2560-80.jpg
---

![Intel](https://cdn.mos.cms.futurecdn.net/XSmGCAUBerwsBhZgUEkxS.jpg)

Intel's 14A (1.4nm-class) process technology is expected to deliver performance 'within 5%' of TSMC's A14 (1.4nm-class) production node, Naga Chandrasekaran, the chief technology and operations officer as well as general manager of Intel Foundry, told investment banking firm KeyBanc (via @Alex\_Intel\_). Given TSMC's track record of delivering steady performance, power, and area (PPA) gains with every new node, this might sound like entirely good news. However, the statement deserves a closer examination.

Delivering 'within 5%' performance is an ambiguous statement that may mean that 14A will be 5% faster than A14, or that 14A will be 5% slower than A14. While 'within 5%' performance compared to the direct rival of the same class may sound like a good competitive position, in recent years Intel's process technologies trailed TSMC's nodes in transistor density and remained competitive in performance or power. This was, to a large degree, attributed to Intel's historic focus on CPU performance, but not necessarily transistor density, as its own fabs have offset additional costs associated with larger dies.

In fact, actual shipping processors suggest Intel's 18A is at least competitive with TSMC's N2 in maximum achievable CPU frequency as Intel's Core Ultra X9 388H 'Panther Lake' can hit 5.10 GHz (at an 80W max turbo power), AMD's EPYC 9586F has the highest single-core clock of 5.0 GHz (at a default 500W CPU power), Apple's A20 Pro can achieve 4.93 GHz, whereas Apple's M6 can hit 4.78 GHz. These numbers should not be converted directly into a statement such as '18A is X% faster than N2,' because the processors use different architectures, voltages, standard-cell libraries, thermal envelopes, and physical implementations. However, they do provide a useful real-world reference point: the available N2 processors do not show a substantial frequency advantage over 18A. If anything, the highest observed CPU frequencies favor Intel's process.

Based on internal estimates, Intel officially states that compared to its already fast 18A, its 14A is expected to provide 15% – 20% higher performance at the same power, or 25% – 35% lower power at the same frequency and transistor count. By contrast, TSMC expects its A14 to be 10% - 15% faster than N2 at the same power, or 25% - 30% lower power at the same clocks and transistor count.

Combining the observed 18A and N2 CPU frequencies of Intel's 18A and TSMC's N2 with Intel's stated 15% – 20% 14A gain and TSMC's assumed 10% – 15% A14 gain would ordinarily suggest a modest 14A performance advantage of A14 even in most conservative scenarios for Intel. Therefore, Intel's new expectation that 14A will be 'within 5%' of A14 is notably less ambitious than one might infer from the company's published process specifications, even though the 'within 5%' statement does not tell us which process Intel expects to lead.

In fact, advantages of Intel's 14A over TSMC's A14 can be calculated using the highest observed 18A and N2 CPU clocks combined with Intel's and TSMC's official iso power performance projections.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Scenario | Intel 14A gain vs. 18A | TSMC A14 gain vs. N2 | 14A extrapolation from 5.10 GHz | A14 extrapolation from 5.00 GHz | Implied 14A advantage |
| Intel worst TSMC best | 15% | 15% | 5.865 | 5.75 | 2.00% |
| Both minimum gains | 15% | 10% | 5.865 | 5.5 | 6.60% |
| Both maximum gains | 20% | 15% | 6.12 | 5.75 | 6.40% |
| Intel best TSMC worst | 20% | 10% | 6.12 | 5.5 | 11.30% |

*Starting points: Intel 18A = 5.10 GHz (Core Ultra 9 388H); TSMC N2 = 5.00 GHz (EPYC 9586F).*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

With Intel’s Core Ultra X9 388H and AMD’s EPYC 9586F as the starting points, the official iso-power performance projections imply a 2% – 11.3% potential performance advantage for 14A over A14, depending on the combination of process-performance assumptions.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Scenario | Intel 14A gain vs. 18A | TSMC A14 gain vs. N2 | 14A extrapolation from 5.10 GHz | A14 extrapolation from 4.788 GHz | Implied 14A advantage |
| Intel worst TSMC best | 15% | 15% | 5.865 | 5.506 | 6.50% |
| Both minimum gains | 15% | 10% | 5.865 | 5.267 | 11.40% |
| Both maximum gains | 20% | 15% | 6.12 | 5.506 | 11.20% |
| Intel best TSMC worst | 20% | 10% | 6.12 | 5.267 | 16.20% |

*Starting points: Intel 18A = 5.10 GHz (Core Ultra 9 388H); TSMC N2 = 4.78 GHz (Apple M6).*

Using Apple's M6 as the real-world N2 reference, a similar calculation gives Intel 14A a 6.5% – 16.2% implied advantage over TSMC A14. Even the worst possible combination for Intel — 14A achieves only +15% while A14 achieves the full +15% — puts Intel's node well beyond the 'within 5%' estimate given by Naga Chandrasekaran.

It should be clearly noted that our calculations do not predict 14A or A14 CPU frequencies, as we use clocks from current CPU architectures with improvement claims for upcoming process technologies. The calculation is useful primarily for illustrating what the companies' published numbers imply relative to today's products.

Intel's 'within 5%' assessment raises an interesting question: why does Intel expect 14A and A14 to be so close when the companies' published process gains appear to suggest a larger gap? Perhaps Intel's assessment incorporates factors that these simple calculations do not capture. Or perhaps the head of Intel Foundry took a page from his boss Lip-Bu Tan's book and now prefers to underpromise.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Anton Shilov](https://cdn.mos.cms.futurecdn.net/uMZ5kNphxA2Ut6whdLaSQV.png)

Anton Shilov is a contributing writer at Tom’s Hardware. Over the past couple of decades, he has covered everything from CPUs and GPUs to supercomputers and from modern process technologies and latest fab tools to high-tech industry trends.
