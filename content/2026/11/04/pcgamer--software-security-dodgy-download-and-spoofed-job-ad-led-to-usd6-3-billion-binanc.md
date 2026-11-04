---
title: Record $6.3 billion hack all began with a dodgy download
source_url: https://www.pcgamer.com/software/security/dodgy-download-and-spoofed-job-ad-led-to-usd6-3-billion-binance-hack-attacker-offered-fake-software-and-fake-job-to-infiltrate-company-wallets-and-steal-billions/
source_site: PC Gamer
source_slug: pcgamer
description: I'm feeling fresh appreciation for my company's mandatory cybersecurity
  awareness course.
image: https://cdn.mos.cms.futurecdn.net/eDGcGRApH6Ut5G9XMKVRHB-2560-80.jpg
published: '2026-11-04T00:00:00Z'
scraped_at: '2026-11-04T14:25:08Z'
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Binance
- Homebrew
- Razer Blade
- Yi He
locations: []
organisations:
- AI
- Alienware
- Binance
- DPRK
- Engineer A
- Engineer B
- Engineer C
- FBI
- Homebrew
- Lenovo LOQ
- MSI Vector
- PC Gamer
- SANS Technology Institute
- Wallet DevOps
---

![The Binance logo on a screen.](https://cdn.mos.cms.futurecdn.net/eDGcGRApH6Ut5G9XMKVRHB-1920-80.jpg)

A chain of events that led to a record-breaking $6.3 billion mega-hack began with a dodgy download, so says the company that was hacked, Binance.

The world's largest cryptocurrency exchange says that the hack was not a "single isolated breach or simple phishing incident"; multiple steps were required to break through its security measures. It all began when a Wallet DevOps engineer (named Engineer A) downloaded a tampered Homebrew installation that was suggested to them by an unnamed search engine.

Homebrew is a third-party package manager for macOS. A report from the SANS Technology Institute, linked to in Binance's investigation, suggests that malicious adverts for Homebrew have been spotted in search engine results, hoping to ensnare users into installing malware on a user's PC.

"Our security team detected the anomaly, replaced the device, and rotated all related credentials as a proactive security action," Binance says. "However, Engineer A’s role and his related colleagues on our wallet infrastructure team was exposed to the hacker."

Then came a separate incident with a software engineer (named Engineer B). They were contacted through a job hunting platform (Binance says it was a legitimate platform) and was asked to attend a first-round interview with a HR representative. This was followed by up a second-round interview with the CEO. Not the HR representative, nor the CEO, however, were real; the company was made up.

The aim of the interviews? To offer Engineer B an 'assignment' that was really a repository of malicious code that executed during setup. The malware ran a series of commands and evasion techniques to avoid detection, thus avoiding Binance's security checks.

The attacker used Engineer B's now-compromised computer and an internal AI tool to gain control over two further machines: that of Engineer A and another Wallet Software engineer (Engineer C). They discovered a container deployment permission token on Engineer A's machine. With this, they could log into Engineer C's computer using the stolen credentials to create a container and trigger a malicious script to start the mega-hack that would drain $6.3 billion worth of funds from wallets used to store transitory funds by the exchange.

Keep up to date with the most important stories and the best deals, as picked by the PC Gamer team.

So, basically, the internet is a bad place, and you can't trust anyone. Or, at least, you have to have your wits about you—especially if you happen to have the key to a multi-billion dollar company's finances stored on your PC somewhere. Luckily, my PC is just pictures of my cat and a Steam backlog that won't quit.

That's actually some of the criticism levelled at the company. Should it have been possible to get this level of access even with spoofed ads and jobs?

> TLDR: If DPRK are reading this, they should be saying "time for round 2". Takeaways: - critical infra engineers are free to download arbitrary software on work laptops. - the day-to-day work setup can connect to billion dollar signing environments. - no human oversight or physical confirmation for moving 10-figs of value / EIP-7702 code change. - various AI vibe-based tools running in corp environments doing god knows what except serving as a remote compromise surface, framed as a good thing btw. - none of the above labelled as the problem. - instead, reads as blaming employees for falling for social engineering, and anti-virus not catching the malware. This is a dog-ate-my-homework level excuse deployed after a nuclear-failure level event. Sincerely hoping binance have more reloads available to cover the next losses too. Reaching exchange hot wallets will never be near impossible, but it should not be this easy either.November 3, 2026

And here's Binance co-founder Yi He on taking that criticism...

> Regarding criticism and suggestions about Binance’s security and access management, we accept them all. We have always believed that transparency builds trust. We read every comment one by one. Binance is not a perfect company, but a company that is constantly evolving. Criticism shows that people have expectations and standards for Binance, and these are sources of motivation for our growth. Binance has never shirked responsibility where problems exist. At present, as a trading platform, Binance needs to address three issues: 1）Will users’ funds be affected? Binance will bear full responsibility，this is what we should do. Legally, if the funding gap is large, one could file for bankruptcy and run away, but Binance operates in a “user-centric” way, with contractual spirit and a sense of moral responsibility. 2）How did the problem occur? Before publication, many professionals advised that it would be best not to include details, but we believe transparency creates trust. If this report is of reference value to other peers regarding the complexity of social engineering and the warning about AI permission boundaries, then the report is meaningful. 3）How can it be prevented in the future? We have already restructured security boundaries across departmental access management, security environments, updated devices, reset AI tools, and in accordance with zero-trust and least-privilege principles. A security audit will subsequently issue a report. Finally, we welcome more top AI security experts and technical talent to join Binance. You can DM me directly or apply on the Binance website for positions you are interested in. Joining Binance to verify this security system is the best way to validate it. 关于对币安的安全和权限管理的批评建议，我们都认。我们一直相信坦透明会建立信任，大家的评论都有一条一条看，币安不是完美的公司，但是一个一直在进化的公司，批评说明对币安有期望，对币安有标准，这些都是我们成长的动力源泉。 币安有问题的地方也从来没有推卸过责任。当下，币安作为交易平台需要解决三个问题： 1）用户的钱会不会受影响？币安会完全承担，这是我们应该做的。法律上资金缺口大可以申请破产跑路，但币安经营是“以用户中心”，是契约精神和大义。 2）问题是怎么发生的？发布前很多专业人士的意见是最好没有细节，但我们认为透明产生信任，如果这个报告在社会工程的复杂度，在AI权限边界的警示对其他同行有参考意义，那么这个报告就有意义。 3）以后如何杜绝？当前已经从各部门权限管理，安全环境，更新设备，重置AI工具，并遵循0信任、最小化原则重构安全边界，后续会由安全审计出具报告。 最后欢迎更多顶尖的AI安全专家和技术人才加入币安，您可以直接DM我本人，也可以在币安网站申请你感兴趣的岗位。加入币安来验证这套安全体系是最好的验证办法。November 4, 2026

Reminder that the FBI reckons a North Korean hacking group is behind the attack, which North Korean officials have unsurprisingly denied. Binance has frozen roughly half of the funds that were initially stolen, and has already covered the rest.

![Razer Blade 16 gaming laptop](https://cdn.mos.cms.futurecdn.net/YwnnY4PZ7TcCYKRYDho7VW-140-80.jpg)

**1. Best overall:Razer Blade 16 (2025)2. Best budget:Lenovo LOQ 15 Gen 103. Best 14-inch:Asus Zephyrus G144. Best mid-range:MSI Vector 16 HX AI5. Best high-performance:Lenovo Legion Pro 7i Gen 106. Best 18-inch:Alienware 18 Area-51**
