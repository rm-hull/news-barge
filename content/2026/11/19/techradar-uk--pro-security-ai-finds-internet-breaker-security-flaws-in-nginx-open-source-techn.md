---
title: AI finds 'internet breaker' security flaws in NGINX — open source technology
  responsible for running hundreds of millions of websites has decades-old issues
  which can be hijacked to steal data
source_url: https://www.techradar.com/pro/security/ai-finds-internet-breaker-security-flaws-in-nginx-open-source-technology-responsible-for-running-hundreds-of-millions-of-websites-has-decades-old-issues-which-can-be-hijacked-to-steal-data
source_site: TechRadar UK
source_slug: techradar-uk
description: Another day, another critical flaw in critical internet infrastructure
image: https://cdn.mos.cms.futurecdn.net/kCbP2VkzMgQpYqJDgMQ8UZ-2560-80.jpg
published: '2026-11-19T00:00:00Z'
scraped_at: '2026-11-19T20:30:53Z'
categories:
- Technology & Software
people:
- AI
- Tomer Schwartz
locations:
- AI
organisations:
- Apache
- AppSec
- CISA
- F5
- Ikotas Labs
- Metnir
- NGINX
- Netcraft
- Rapid7
- TechRadar Pro
- US Cybersecurity and Infrastructure Security Agency
- WebAtla’s
- Wiz CTO
- Xint
---

![Cybersecurity](https://cdn.mos.cms.futurecdn.net/kCbP2VkzMgQpYqJDgMQ8UZ-1920-80.jpg)

* **F5 patches multiple NGINX vulnerabilities, including two critical flaws that could enable unauthenticated remote code execution**
* **The bugs affect widely deployed internet infrastructure and prompted an out-of-band security release**
* **Organizations are urged to upgrade to NGINX 1.31.9 immediately, especially when HTTP/2 is enabled**

We can add NGINX to the growing list of crucial software containing critical severity vulnerabilities that need urgent patching.

F5 has published an out-of-band security notification addressing 10 flaws in NGINX, including two that allow unauthenticated threat actors to launch arbitrary code on the servers, remotely.

## Who the what now?

NGINX is an open source web server software owned by F5, and used to deliver websites and web applications to users. It can also act as a reverse proxy, load balancer, and HTTP cache, helping websites handle large amounts of traffic more efficiently.

The tool is often found on web servers and cloud infrastructure where it’s installed between users’ browsers and the applications or services hosting a website.

It is one of the most widely deployed web server technologies in the world. Approximately 73 million websites use NGINX according to WebAtla’s November 2026 figures, representing around 22% of all websites on the internet. Netcraft’s figures are somewhat different (225 million websites, 15.3% of all sites surveyed), but one thing is for certain - NGINX is a significant piece of internet infrastructure.

These days it’s trendy to use AI to uncover critical-level vulnerabilities in technologies powering most of today’s internet. First came PHP - in late October two critical vulnerabilities in its runtime were found, which could allow unauthenticated attackers to remotely execute malicious code on vulnerable web servers, or access sensitive data stored in their memory. The flaws were later nicknamed PHP2Shell.

Then came Apache HTTP server with CVE-2026-119618, then Java with a critical memory-corruption vulnerability in the Base64 decoder, creatively named Java4Shell. This one, too, allowed unauthenticated attackers to execute code remotely and was significant enough to warrant a warning from the US Cybersecurity and Infrastructure Security Agency (CISA) to patch up immediately.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

## NGINX joins the fray

Now, it’s NGINX’s turn. According to *The Register*, it was Tomer Schwartz (Wiz CTO of exposure management and AppSec), together with researchers from Ikotas Labs, Metnir, Rapid7, and Xint working independently, who discovered the flaws. AI tools were, obviously, used in the process. Speaking to the publication, Schwartz said this wave of AI-discovered vulnerabilities “point to a new reality.”

“We need to treat every internet-connected system as potentially vulnerable,” Schwartz said. “AI has changed not only which vulnerabilities can be found, but how quickly longstanding risks can become real threats.”

Real threats they are, but hackers still haven’t exploited them, it seems. “At this time, we have found no evidence of active exploitation of any of these vulnerabilities in the wild,” an F5 spokesperson told *The Register*. “We continue to monitor closely and will share updates via myF5 as we learn more.”

Of the 10 bugs that F5 addressed, two require more attention: CVE-2026-123633 and CVE-2026-123007. Both carry a 9.2/10 (critical) rating, and the latter affects versions back to 1.9.5 which was pushed a decade ago. Both require HTTP/2 to be enabled on the affected NGINX server.

“Both vulnerabilities are memory-safety issues in how NGINX handles HTTP/2 traffic,” Schwartz said in a new blog covering the topic. “In CVE-2026-123633, a connection's memory is freed while a request still needs it, creating a use-after-free. In CVE-2026-123007, incorrect flow-control accounting leads to an invalid memory copy.”

While all this news of critical flaws left and right might sound apocalyptic, Schwartz keeps a positive outlook. “In the long run, AI-powered vulnerability research will harden foundational software,” he said. Not before it breaks a lot of things, though, so we will need to weather one hell of a storm in the meantime.

One security team, Rapid7, also released a Proof-of-Concept (PoC) exploit code, using CVE-2026-123007 to achieve unauthenticated remote code execution on a vulnerable linux/amd64 Docker image running nginx version 1.31.8.

To make sure you don’t get caught unprepared, update your NGINX instance to version 1.31.9 without delay.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
