---
title: Why your security stack might be guarding the wrong door
source_url: https://www.techradar.com/pro/why-your-security-stack-might-be-guarding-the-wrong-door
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-13T11:26:04Z'
published: '2026-07-13T00:00:00Z'
description: 'Why security must move to where the work happens: the browser'
image: https://cdn.mos.cms.futurecdn.net/UjSNcAZ5SebctebKAMQNVF-2560-80.jpg
---

![Cybersecurity ensures data protection on internet. Data encryption, firewall, encrypted network, VPN, secure access and authentication defend against malware, hacking, cyber crime and digital threat](https://cdn.mos.cms.futurecdn.net/UjSNcAZ5SebctebKAMQNVF.jpg) 

![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png) 

Whether it’s a new agent, a new gateway, or a new monitoring layer, every time a security gap appears, the instinct is to close it with a new tool. It seems sensible in the short term, but over the years, the layers build up until enterprise security becomes one of the most complex and costly parts of running a business.

VP and Field CTO at Island.

The result is a fragmented stack that is expensive to license, difficult to manage, and hard to justify to the board. Security teams are left with overlapping controls, integration headaches, and a user experience rife with friction. And to make matters worse, the whole bloated stack might well be pointed in the wrong direction.

## Work moved, but security didn't

For most knowledge workers, the browser is where the working day begins and ends. From CRM to email, a growing number of enterprise applications are best delivered through a browser tab. Adding to this is the rapid adoption of generative AI tools, which employees use daily for drafting, analysis, and workflow automation. The browser is not a gateway to work but has become the workspace itself.

Security architecture has not kept pace with this shift. The controls most organizations rely on were designed for a different era, one built around corporate networks, managed devices, and applications behind a firewall. That model has not existed in its original form for years, yet it still underpins traditional security strategies.

As a result, there is a significant blind spot: Network and device-level controls can determine whether a user is allowed to reach an application, but they cannot see what happens once they are inside it.

When the stack stops at the door, critical information never crosses the threshold. For example, organizations may never see data is being accessed, how it is being handled, and whether it is copied into a personal email or pasted into a public AI tool.

## The browser is the primary attack surface

Most workers use consumer browsers designed for the broadest audience possible. Because they’re not built for the rigors and needs of enterprise use, they’re soft targets.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Savvy threat actors can harvest credentials inside the browser session, and malware targets locally stored cookies and passwords. Data exfiltration increasingly happens not through network breaches but through routine user actions such as copying a customer record, downloading a report, or sharing a file with the wrong destination.

The rapid rise of AI tools has exacerbated the problem. Employees are pasting sensitive business data into generative AI platforms without understanding where it goes or how it is retained. Agentic tools that take actions inside business systems on a user's behalf are especially risky. They introduce a category of risk that most security teams have limited visibility into, and those interactions leave no trace on the network perimeter.

Legacy security tools were not built to see inside a browsing session. They inspect traffic, scan endpoints, and flag anomalies after the fact. By the time a control triggers, the action has often already happened.

## Control needs to move to where decisions are made

With enterprise activity concentrating in the browser, the enforcement layer needs to follow suit.

The most important thing to reframe is moving from managing access to managing behavior. Traditional security tends to focus on whether a user is permitted to access an application.

That still matters, but the more consequential question is what happens inside the application once access is granted. A file downloaded to a personal device or a customer record pasted to a private email are the moments when data movement can turn into data loss risk. But most security and data protection stacks can’t see them.

Embedding security and data protection into the browser makes these moments governable because policy applies at the point of action, in real time, without disrupting the workflow. A user working with sensitive data can move it freely between authorized applications, while controls prevent it from reaching an unauthorized destination.

This is also where zero trust can be properly realized. Most implementations evaluate identity and device posture once, at login. A browser-native model assesses session context continuously, adjusting controls as circumstances change without interrupting the user. Enforcement follows the work, rather than waiting at the edge of the network.

## Consolidation is the only way forward

Managing browser risk isn’t simply a case of throwing more tools into the stack. Many enterprises will find their stack is already full of layers that were built to compensate for consumer browsers. You have a virtual desktop interface (VDI) to control application access, and VPNs maintain network tunnels for SaaS tools that need a very different method of connectivity and protection.

Data loss prevention (DLP) solutions attempt to intercept data movement after the moment it happens, and cloud access security broker (CASB) layers mediate cloud access that the browser already intermediates.

Each is a reasonable response to a security gap, but together they establish an unwieldy infrastructure that was never designed to work as a whole. These systems force 100% of data through choke points (SASE cloud proxies) for inspection, creating performance bottlenecks and a poor user experience.

And as encryption cyphers strengthen toward post-quantum encryption standards, a significant portion of this traffic is blind to these break and inspect architectures.

Closing them from the inside by making the browser itself the primary point of governance removes the need for many of them entirely. The stack got this big by solving the wrong problem, and solving the right one starts with the browser.

*This article was produced as part of**TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:**[https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
