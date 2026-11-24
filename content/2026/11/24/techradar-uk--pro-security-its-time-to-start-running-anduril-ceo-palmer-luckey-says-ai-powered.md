---
title: '‘It’s time to start running’: Anduril CEO Palmer Luckey says AI-powered cyberattacks
  are moving faster than outdated defenses'
source_url: https://www.techradar.com/pro/security/its-time-to-start-running-anduril-ceo-palmer-luckey-says-ai-powered-cyberattacks-are-moving-faster-than-outdated-defenses
source_site: TechRadar UK
source_slug: techradar-uk
description: Palmer Luckey says AI attackers are outrunning legacy defenses
image: https://cdn.mos.cms.futurecdn.net/sDfT4RfctpUq5qQqTQqBQL-1920-80.jpg
published: '2026-11-24T00:00:00Z'
scraped_at: '2026-11-24T02:12:16Z'
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Andrew Ross Sorkin
- Anduril
- Bryan Bedford
- Calif
- Implicator
- JD Vance
- Jay Clayton
- Marco Rubio
- Mark Warner
- Markwayne Mullin
- Matthew Prince
- Nick LaLota
- Palmer Luckey
- Wiz
locations:
- AI
- Manila
- North Korea
- US
- Wall Street
- Washington
- White House
organisations:
- AI
- Amazon
- Anduril
- Apple
- Associated Press
- Booz Allen
- CNBC
- Censys
- Cloudflare
- Congress
- Costco
- CrowdStrike
- DNI
- FAA
- Fox Business
- Gambit
- Google
- HPE Juniper
- Homeland Security
- Intelligence Committee
- Internet Archive
- JPMorgan Chase
- Lattice
- Microsoft
- NSA
- NSANet
- National Intelligence
- National Security Agency
- Navy
- Oculus
- OpenAI
- PHP
- PHP2Shell
- Palmer Luckey
- Pentagon
- TechRadar Pro
- The National News Desk
- The New York Times DealBook Summit
- The Washington Sun
- Visa
- Wiz
- Zelle
---

![A picture of Anduril CEO Palmer Luckey](https://cdn.mos.cms.futurecdn.net/sDfT4RfctpUq5qQqTQqBQL-1920-80.jpg)

* **Anduril co-founder Palmer Luckey claims AI-built exploits are outpacing legacy defenses**
* **Luckey predicted AI will favor defenders in the long run, but only if they move much faster now**
* **US officials say the recent outage wave came from botched updates and rushed patches, not cyberattacks**

Palmer Luckey has a blunt message for anyone still running yesterday's infrastructure: "It's time to start running."

Speaking with Andrew Ross Sorkin at the recent The New York Times DealBook Summit, the Anduril co-founder and Oculus founder warned that AI tools are letting attackers build exploits faster than older systems can be defended.

The setting gave Luckey's warning extra weight, as that same morning, Vice President JD Vance pulled out of his own DealBook appearance shortly before he was due on stage, staying in Washington for meetings about a run of outages that had hit Microsoft, the FAA, JPMorgan Chase, Zelle and the National Security Agency.

## An interesting argument at a time when the call was coming from inside the building

Luckey argued that the consequences of advanced AI are already visible, describing what is happening as "the natural effects of a lot of these advanced AI tools" being used to create exploits. When Sorkin asked how worried people should be, he said it "depends on how well prepared you are," then added, without elaborating, that the audience would "find out what's going on soon enough."

The core of his case is a speed mismatch: On one side are attackers he called "very fast-moving," quick to put new technology to work. On the other are "old, outdated systems" that cannot adopt new technology as quickly as it is developed. People who say everything can be hacked, he said, "are right, for now." He also said US adversaries are exploiting that gap for strategic and financial reasons and singled out North Korea, though Luckey offered no specific incidents.

Luckey was not fatalistic about where this ends, however: In the long run, Luckey said, the advantages will "accrue to the side that is most effectively using AI for defense." The danger is the stretch between now and then, and he said, "people are going to have to pick up the pace."

What Luckey did not say, at least in the remarks reported, is that the outages themselves were attacks. That distinction matters here because nearly every official account also says they were not.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

"This is not a cyberattack, and this is not a coordinated effort by a nation-state," Director of National Intelligence Jay Clayton told CNBC. Secretary of State and National Security Adviser Marco Rubio, speaking in Manila, said the country was "not under systemic attack" and that the incidents were not linked, the Associated Press reported.

Microsoft traced its two-day Outlook and Teams collapse to a cascading failure across its servers rather than an intrusion. The FAA's nationwide ground stop was reportedly caused by two newly installed HPE Juniper routers flooding its aging communications network with connection requests. FAA Administrator Bryan Bedford said there was "zero evidence of anything AI-related," while HPE said the router had behaved as its installer configured it, according to Implicator.

JPMorgan Chase blamed a software bug in on-premises hardware and said there was no evidence it was cyber-related, even as a ransomware group called n0n added the bank and Visa to its leak site, a claim JPMorgan has denied. Apple put its outage down to an internal update.

## All roads lead to AI? Not quite

The NSA is where the story turns back toward AI. The agency's classified NSANet network recently went down, and while its own statement cited scheduled maintenance, Clayton said on *Fox Business* the failure followed a patch for major vulnerabilities disclosed last month, with patched systems failing to come back up as expected.

Those vulnerabilities have a name: PHP2Shell is a pair of critical flaws in the PHP runtime, tracked as CVE-2026-109618 and CVE-2026-109619, rated 9.2 out of 10 and disclosed on October 21. Calif found one of them with help from an OpenAI model, and Wiz independently found both using frontier models from Google and OpenAI.

Wiz argued the episode shows how AI can "change the practical exploitability of longstanding vulnerabilities," and says the bugs reach back to PHP 5.4. PHP powers an estimated 70% of websites, and in October 2026 sites as large as Wikipedia and the Internet Archive briefly went dark to patch.

This is where Luckey's speed argument and the official accounts converge: Attackers did not wait for even a moment. Amazon says it saw a PHP2Shell exploitation attempt four days before public disclosure, and Cloudflare CEO Matthew Prince reported thousands of attempts in the 10 hours before the patch, climbing to hundreds of thousands within two hours. Within nine days, researchers had documented Chinese attackers chaining PHP2Shell with a Linux privilege escalation flaw to gain root on 25 servers, some tied to the US government.

Faced with that, defenders did what Luckey prescribes: they ran. Wall Street executives and the NSA told members of Congress that the outages came from rushed attempts to fix AI-identified vulnerabilities, The Washington Sun reported, citing three anonymous sources.

One congressional official said patches were being pushed through all at once, "more than the system was designed for." Homeland Security Secretary Markwayne Mullin told *CNBC* that new technology is being layered onto very old systems, and warned that more such disruptions are coming.

Read that way, the outages are not evidence against Luckey's thesis; They are what the gap he described looks like from the defender's side: AI surfaces a decade-old flaw, attackers move within days, and organizations sitting on legacy stacks break their own systems trying to keep up.

The patch-rush explanation should not be stretched over the whole cluster, however: Microsoft's root cause was a latent bug introduced in a July 2026 update, well before PHP2Shell was disclosed. The FAA's trouble began with router work during a copper-to-fiber upgrade, and its administrator explicitly ruled out an AI link. Even the NSA and the DNI did not describe the agency's outage the same way.

Lawmakers have noticed the mixed messaging. Senator Mark Warner, the Intelligence Committee's top Democrat, said the White House had offered no clear explanation and that "people are freaking out," The National News Desk reported. Republican Representative Nick LaLota said he worried the week's events went beyond coincidence. Shoppers cleared Costco shelves of water and batteries, and most of its pricier generators sold out online.

None of this makes Luckey wrong about the threat. AI-driven offense is well documented. In September 2026, Gambit researchers described a likely Chinese, financially motivated operation in which autonomous AI agents stole more than 600,000 payment records, compromising 27 organizations to varying degrees in under a week, with roughly $7,000 in spend over four weeks. CrowdStrike and Censys have tracked ARTEX, an AI agent layer for reconnaissance, being used against South Korean banks, with more than 1,400 exposed consoles found online.

Via *TechCrunch*

## Anduril: Not exactly a neutral party

Luckey is not a neutral commentator: Anduril sells AI-driven defense systems built around its Lattice software, has partnered with Booz Allen to run cyber capabilities on its Menace hardware, and recently landed a Navy deal worth up to $2.9 billion days after Luckey joined a Pentagon weapons initiative. "The side most effectively using AI for defense" is, among other things, a fair description of Anduril's sales pitch, and it echoes his earlier line that there is "no moral high ground in using inferior technology."

That does not make the argument wrong, but it does expose its gap. AI for defense is exactly what found PHP2Shell, and finding bugs faster only helps if organizations can ship fixes without breaking things. On this month's evidence, the bottleneck is less about detection than about legacy stacks, thin testing, and rollouts that cannot absorb emergency change at AI speed. Running requires legs that many institutions do not yet have.

Luckey may well be right that the public will find out what is going on soon enough. If the past week is a preview, though, the next big failure may look less like a hack and more like a fix.
