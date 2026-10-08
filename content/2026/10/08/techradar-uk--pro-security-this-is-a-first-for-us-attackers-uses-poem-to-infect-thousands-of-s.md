---
title: '''This is a first for us'': Attackers uses poem to infect thousands of servers
  with malware'
source_url: https://www.techradar.com/pro/security/this-is-a-first-for-us-attackers-uses-poem-to-infect-thousands-of-servers-with-malware
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-08T18:47:00Z'
published: '2026-10-08T00:00:00Z'
description: Someone's been reading too much Dan Brown
image: https://cdn.mos.cms.futurecdn.net/sqGgDPxHyGtqunPo56h9cL-2560-80.jpg
categories:
- Technology & Software
- Self-Improvement
people:
- PoeLLM
- Robert Langdon
locations:
- GitHub
- Italy
organisations:
- Black Lotus
- Black Lotus Labs
- LiteLLM
- Lumen’s Black Lotus Labs
- PoeLLM
- TechRadar Pro
- The Register
---

![A pink triangle with a red exclamation mark inside on a blue digital landscape](https://cdn.mos.cms.futurecdn.net/sqGgDPxHyGtqunPo56h9cL-1920-80.jpg)

* **A threat actor built malware that reads poems posted on GitHub**
* **The poems are a secret code for the location of C2 servers**
* **The servers instruct the malware to deploy cryptojackers and scanners**

Somewhere in the trackless wastes of cyberspace, a digital Robert Langdon is decoding an ancient poem to find the location of his masters and receive instructions on his next steps. I might be exaggerating a bit, but this is the gist of a rather bizarre story on cyberattacks and cryptocurrency mining.

Cybersecurity researchers from Lumen’s Black Lotus Labs found a piece of malware that gets the instructions on the location of the C2 server from a poem shared on GitHub.

By looking for specific words and decoding them into numbers, the malware can get an IP address where the C2 server is located and receive instructions on what to do next - Black Lotus calls it “adversarial poetry” and says it’s never seen anything like it.

## Adversarial poetry

The attacker, who seems to be of Italian origin (or at least based in Italy), first hunts for vulnerable internet-facing services, such as LiteLLM or Ollama, and installs a piece of malware called PoeLLM.

This malware then goes to GitHub to look for a poem which seems to be AI-generated. Here are the lines:

*In the silent hum of driver, the machines begin to speak,*

*Each pulse of diode threading light through copper veins.*

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

*we taught the dark to carry meaning, byte by byte —*

*A language built from lightning, cold and clean.*

*Beyond the wall of encryption, a signal finds its way,*

*the tick of distant servers answering back.*

*Data moves like water through the cracks of ordered thought,*

*and somewhere in the code, the world stays on track.*

It then looks for specific words in this poem: driver, diode, decryption, tick, and matches them to corresponding numbers (its dictionary is hardcoded). When they are combined, they form an IPv4 address where the server is located.

PoeLLM then reaches out to the server and gets instructions on what to do next. In most cases, it just deploys a cryptocurrency miner called XMRig, using the device’s electrical energy, compute, and access to the internet to mine Monero tokens and enrich the malicious poet.

The malware can also run as a scanner, searching for additional vulnerable systems, and allowing the attacker to worm his way into even more devices.

## Changing the song

If the attacker needs to move the infrastructure, all they need to do is change certain words in the GitHub poem. Therefore, when infected machines retrieve the updated version, they can calculate the new C2 address without needing a malware update. In fact, this already happened multiple times.

According to The Register the poem, titled “On the Nature of Connection,” has been updated 11 times since its initial commit. The latest update happened in September 2026.

“The Canto Incognito campaign appears to be relatively unique in its targeting of multiple AI-related services,” the researchers told *The Register*.

“Other notable campaigns this year, including the LiteLLM supply chain compromise, focused on a single service and impacted roughly 2,500 victims, according to open sources. The collection of more than 3,000 PoeLLM victims appears to exhibit multiple vulnerable services at any given time.”

In other words, the adversarial poetry campaign has been rather successful, so far infecting more than 3,000 (confirmed) devices.

The PoeLLM malware developer “has been extremely successful in identifying vulnerable servers, deploying exploits, and conscripting victims to continue expanding the campaign,” Black Lotus Labs said.

“If the actor had only focused on one or two vulnerabilities, the potential victim pool might have quickly dried up, but the expanding scope allowed for a bigger, more powerful (and more profitable) botnet.”

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
