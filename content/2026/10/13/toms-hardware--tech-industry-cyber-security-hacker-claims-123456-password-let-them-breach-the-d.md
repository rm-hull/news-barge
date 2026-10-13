---
title: Hacker claims ‘123456’ password let them breach the Danish national registry,
  accessing 8.8 million records — IT and data services company with weak passwords
  linked source of the hack
source_url: https://www.tomshardware.com/tech-industry/cyber-security/hacker-claims-123456-password-let-them-breach-the-danish-national-registry-accessing-8-8-million-records-it-and-data-services-company-with-weak-passwords-linked-source-of-the-hack
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-10-13T16:57:03Z'
published: '2026-10-13T00:00:00Z'
description: 8.8 million Danes have reportedly been affected by this hack.
image: https://cdn.mos.cms.futurecdn.net/9fQFudMNzx5vudaaaTqZiX-2000-80.jpg
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
people:
- Jowi Morales
- Python
- Sophie Laursen
- Tom
locations:
- Copenhagen
- Denmark
- Indonesia
- South Korea
organisations:
- AI
- CPR
- ChatGPT
- Danish Central Register of Persons
- Google News
- IT
- Jowi Morales
- OpenAI
- PSC
- Pays ApS
---

![Hacker](https://cdn.mos.cms.futurecdn.net/9fQFudMNzx5vudaaaTqZiX-1920-80.jpg)

A person claiming to be responsible for the recent hack of Denmark’s national registry claimed that they were able to gain access because of an IT company’s weak password. According to *The Register*, Pays ApS, an IT and data services company that lets customers reference the Danish Central Register of Persons (CPR) was the source of the hack, with the hacker saying that one of the accounts they breached was only protected by a ‘123456’ password.

Copenhagen has confirmed the hack, with a government official saying that the breach was discovered 12 days after it happened when an invoice revealed an unusual amount of activity from the company. The Danish government said that 8.8 million records have been illicitly retrieved, although the hacker claimed that they do not intend to sell or leak the information. While the government did not mention which company the hacker exploited, Pays ApS managing director Sophie Laursen confirmed that the hacker used the company’s access to the database to exfiltrate the data.

This incident shows that a system’s security is only as strong as the weakest link, with the Danish database getting compromised through a third-party user’s poorly chosen password. Given that CPR essentially contains information on virtually every Danish citizen, one would expect that it would require users to at least have a more complicated password, if not two-factor authentication. This isn’t the first time that an incident reveals shortcomings in government database protection, though — Indonesia realized that it had no backups when a ransomware attack in 2024 affected over 230 public agencies, while South Korea lost 858 terabytes of data after a catastrophic fire at a government data center last year.

We expect the Danish government to overhaul its password policies in the near future, especially now that AI is making it easier and more efficient for hackers to hit their targets. Recent incidents like the attacks on South Korean banks and against the Taiwanese government were reportedly conducted with the help of AI agents. Hackers also breached OpenAI using Claude tools, showing just how potent AI has become as a hacking tool in the wrong hands. But with a password like “123456,” potential hackers wouldn’t need to use any AI tools to break into weakly protected systems.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

![Jowi Morales](https://cdn.mos.cms.futurecdn.net/gM7E2WSDg2wgCFoaDPz9yK-140-80.jpg)

Jowi Morales is a tech enthusiast with years of experience working in the industry. He’s been writing with several tech publications since 2021, where he’s been interested in tech hardware and consumer electronics.

* It's not really a hack of the Danish government since the service exposed by the government was always intended to sell access to citizens' information at large scale including for the purpose of letting any paying party update their customer databases with correct address information and more. For example, a bank with 2 million customers might run regular look-ups to ensure they still have updated information about the addresses of their customers without the customers having to do anything.  
    
  This was always the concept of the service. It was never designed to keep anything secret but rather to ensure that the information was only revealed in return for a payment.  
    
  The hack was therefore not against the Danish government but against the company, which was perfectly entitled to pull the 8 million records from the government as long as they paid for it.  
    
  The "password" was in fact "guarding" a web-based front-end to making such look-ups in the central person registry. The web-based front-end was developed by the small company called Pays ApS.  
    
  In principle, the "hacking" is a matter between the hacker and the small company Pays ApS and not a matter between the "hacker" and the government since they merely served up CPR records in return for expected payment.  
    
  From a legal point of view, the company is liable to pay the fees for looking up the 8 million records and should seek remedy with the hacker.  
    
  Also, currently doing the rounds is some mumbo-jumbo story that "AI enabled the hacker to hack the service".  
    
  In fact, the guy is a script kiddie, who was not even able to program a simple for-loop generating the individual unique person ID-numbers required to look up address information. He therefore had to ask ChatGPT how to code a simple look-up script in Python and even managed to mess it up so they got no records out for people born in 1977.  
    
  One might argue that the Danish government's model of selling unlimited access to any willing and paying company without requiring any proactive cybersecurity audits is totally irresponsible in a world where information about where people live has already been abused by informants serving assassin hit squads and is probably also being exfiltrated by Russian intelligence services to target CEO's of weapons manufacturing companies as well as high-ranking military personnel. Reply
* 12345... 6? Oh come on! That's my PSC (Post-Spaceballs Combination) compliant luggage combo. They said it would stand up against brute force attacks. They said adding the extra 6th digit would prevent people from guessing the combo. They said it would keep heroes and talking dogs out of my things. Now what am I supposed to do? Do they even sell luggage with 7 digits of security yet?!Reply
