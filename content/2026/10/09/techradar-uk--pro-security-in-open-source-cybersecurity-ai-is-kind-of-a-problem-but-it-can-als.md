---
title: In open source cybersecurity, AI is kind of a problem — but it can also be
  a solution
source_url: https://www.techradar.com/pro/security/in-open-source-cybersecurity-ai-is-kind-of-a-problem-but-it-can-also-be-a-solution
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-09T18:22:15Z'
published: '2026-10-09T00:00:00Z'
description: '''Tsunami in vulnerability disclosures'''
image: https://cdn.mos.cms.futurecdn.net/hsp2hXrMRpqTNDhd2ZFJof-970-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Jamie Thomas
- Linus Torvalds
locations:
- AI
organisations:
- AI
- Enterprise Security
- Google
- HackerOne
- IBM
- Linux Foundation
- Open Source Security Foundation
- OpenSSF
- TechRadar Pro
---

![open source software](https://cdn.mos.cms.futurecdn.net/hsp2hXrMRpqTNDhd2ZFJof-970-80.jpg)

The last few years have seen a growing wave of vulnerability disclosures heading towards the cybersecurity industry, and the people working on fixing these flaws are often struggling to keep up. And while AI is a major contributor to this problem, but also an essential part of the solution.

Speaking at the recent Linux Foundation Open Source Summit, Jamie Thomas, IBM's Chief Client Innovation Officer for Enterprise Security, warned there is “a bit of a tsunami in vulnerability disclosures,” with approximately 66,000 unique entries expected to emerge in 2026 alone.

At the keynote, titled The Future of Open Source Security in the Age of AI, Thomas stressed this represents a fourfold increase compared to seven years ago.

So, how can the cybersecurity industry possibly keep up with this pace, Thomas asked, especially when the expectations placed on developers and security professionals continues to grow?

The answer seems to be the same as with everything these days - AI.

## Attackers are moving faster than ever

The volume of attacks is definitely an issue, but it’s not the only issue. Cybercriminals are also a lot faster at exploiting them, giving defenders an ever-shrinking window to identify and remediate different security issues.

Citing publicly available data, Thomas said the time required to exploit a vulnerability shrunk from days to as little as 29 minutes.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

“And in fact, we're seeing a rapid increase in cyberattacks, as well as malware attacks,” she said.

For businesses that rely heavily on open source, this is definitely cause for serious concern. A vulnerability in a widely used component can potentially affect hundreds, if not thousands, of downstream applications and businesses. To add insult to injury, cybercriminals don’t really wait for the cybersecurity community to publicly disclose a vulnerability before they can exploit it.

“We're seeing the time to exploit is actually negative,” she said. “Many times we're getting a disclosure and we don't have a patch yet.”

That is the position the defenders are in, right now. They are expected to respond to a rapidly growing number of security issues in a shrinking timeframe, while attackers take advantage of automation to accelerate their operations.

## AI is making life harder for open-source maintainers

And then, along comes AI for the sucker punch.

Sure, AI-powered tools are capable of identifying vulnerabilities and improving software security, but they are also more than effective when it comes to creating a pile of inaccurate, duplicated, and otherwise unactionable vulnerability reports.

Where does that leave open source maintainers, you might ask? Large companies typically have dedicated security teams, and even those struggle with an influx of low-quality reports, as you’ll see below. Many open source projects, on the other hand, are maintained by small groups of devs, sometimes even by a single individual.

Earlier this year, the developers of curl, the popular open-source command-line tool and software library, terminated their HackerOne bug bounty program, saying the financial incentives had people submitting poorly researched, and sometimes entirely fake, reports. The influx, which included AI-generated submissions, was simply unmanageable for the project’s security team.

Even the almighty Google bent the knee, recently being forced to temporarily suspend its Open Source Software Vulnerability Rewards Program following a significant increase in invalid and irrelevant reports (many of which were AI-generated, apparently). As of October 1, 2026, the company is no longer accepting new submissions and will reassess the program in early 2027.

Even Linux creator Linus Torvalds complained about the problem, recently saying AI-powered bug hunters have made the Linux security mailing list "almost entirely unmanageable." He criticized the enormous duplication of reports, saying different researchers were using the same AI tools to identify vulnerabilities that were already fixed, or at least reported.

## IBM wants AI to become part of the solution

So what’s the solution? According to Thomas, the security community should not abandon AI-powered vulnerability discovery but should instead use the same technology to help maintainers handle the growing workload.

This is where the Linux Foundation’s Open Source Security Foundation (OpenSSF) initiative, could step in. A collaboration between tech firms, developers, and the wider open-source community could allow OpenSSF to strengthen the supply chain security, and for IBM, the priority is now to reduce the burden on maintainers. That can be done by making vulnerability management more efficient and that, in turn, can be done with AI-powered tools filtering out duplicate and bogus reports, assessing the severity of different bugs, and identifying issues that need urgent attention.

AI can also help remediate issues, help developers understand vulnerable code, suggest fixes, and evaluate whether patches introduce additional problems. This is an important caveat, since some earlier reports found the majority of AI-generated remediation suggestions caused more problems than they solved.
