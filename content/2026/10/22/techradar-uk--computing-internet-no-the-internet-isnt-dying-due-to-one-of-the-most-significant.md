---
title: What is PHP2Shell and what does it mean for you — is it unsafe to visit some
  websites now this exploit is out there?
source_url: https://www.techradar.com/computing/internet/no-the-internet-isnt-dying-due-to-one-of-the-most-significant-vulnerabilities-of-2026-but-this-is-what-you-need-to-know
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-22T17:16:48Z'
published: '2026-10-22T00:00:00Z'
description: Everything you need to know about PHP2Shell in terms of what it is, and
  what this security flaw means for the average person browsing the web.
image: https://cdn.mos.cms.futurecdn.net/jrDcfCchNnA7ZHeb6VM58V.gif
categories:
- Technology & Software
people:
- Dane Knecht
- Malwarebytes
- Sergey Lozhkin
locations:
- UK
organisations:
- Amazon Threat Intelligence
- Cloudflare
- Exploitation A
- Hacker News
- Head of Research Center for APAC
- Kaspersky GReAT
- Kaspersky It
- META
- Malicious
- NCSC
- PHP
- PHP2Shell
- TechRadar
- WordPress
---

![Gif collage representing internet security](https://cdn.mos.cms.futurecdn.net/jrDcfCchNnA7ZHeb6VM58V.gif)

You've probably heard about PHP2Shell and how this freshly emerged security issue affects a ton of websites, as well as warnings on how website owners need to urgently apply patches to fix this.

It sounds like a big deal – and it is – so you've likely got questions. Maybe for starters: what is PHP2Shell exactly and what does it affect? And what does it mean for you as someone using a web browser today – is it not safe to visit some websites now?

This article aims to provide answers to the common questions about PHP2Shell and explain all the key points that you need to know about this vulnerability (well, actually it's two vulnerabilities to be precise).

## What is PHP2Shell?

PHP2Shell is the name given to a security flaw in the PHP programming language that's used by many websites and web applications across the globe. In fact, PHP is used by almost 70% of websites as Wikipedia estimates, and it's employed in the likes of WordPress, Drupal, Joomla, and other common systems that drive websites – which is why the possible impact is so widespread.

> In practical terms, attackers could potentially execute malicious code on affected systems, including the deployment of web shells, thereby gaining control over vulnerable servers.
>
> Sergey Lozhkin, Head of Research Center for APAC and META at Kaspersky

It consists of two separate memory-related vulnerabilities labelled CVE-2026-109618 and CVE-2026-109619. These flaws in the way PHP works could be exploited by a malicious attacker to compromise a site that's using PHP (which is the majority of the web, as noted), and potentially this could lead to the ability to remotely execute code.

It's a serious incident with these vulnerabilities being rated as 9.2 out of 10 for severity.

## What happens if an attacker manages to exploit a website using these vulnerabilities?

Sergey Lozhkin, Head of Research Center for APAC and META at Kaspersky GReAT, explained to TechRadar: "The potential impact is considerable: if successfully exploited, this vulnerability could enable remote code execution, one of the most serious forms of cyber compromise. In practical terms, attackers could potentially execute malicious code on affected systems, including the deployment of web shells, thereby gaining control over vulnerable servers."

Sign up for breaking news, reviews, opinion, top tech deals, and more.

In other words, the attacker could run their own code and alter the content of a website to nefarious ends (stealing data for example), or redirect you to their own malicious site for phishing purposes (or even directly installing malware).

## Has PHP2Shell been exploited yet?

PHP2Shell has been a trickier customer than expected because these vulnerabilities were disclosed before the official announcement of the security issue was made. As we reported yesterday, someone leaked the details of these flaws on the Hacker News forum before the embargoed announcement happened, leaving security experts scrambling to get defenses in place more quickly than they anticipated.

This meant that there were early attempts to exploit PHP2Shell, and indeed one of those dates back to before the flaw was even leaked (let alone announced). According to Amazon Threat Intelligence, an attempt at exploitation was made as early as October 17, although it "remains unclear how the actor acquired exploit information prior to disclosure."

As Malwarebytes points out, Dane Knecht, the chief technology officer at Cloudflare, reported "early attacks emerging" too, before the PHP team rolled out patches to fix the security holes.

Amazon Threat Intelligence warns that: "PHP2Shell is now being broadly exploited in the wild."

![Annotated image](https://cdn.mos.cms.futurecdn.net/nos92bovteW8KcinhcDuVj-2560-80.png)

#### The target

The attack starts with a server running vulnerable versions of PHP. PHP is a core programming language used to power millions of web applications and servers worldwide, making any runtime vulnerability here exceptionally dangerous.

#### Malicious request

An unauthenticated attacker (meaning they don't need valid login credentials or prior access) sends a specially crafted, unauthorized payload request directly to the PHP web server.

#### Exploitation

A critical flaw in the core PHP runtime allows this incoming payload to hijack the ongoing backend process. As the PHP backend processes the code, an execution error or breakout occurs.

#### System takeover

Because the runtime is hijacked, the attacker could successfully execute remote commands, giving them access to the user's operating system, compromising the entire device.

![TechRadar Logo](https://cdn.mos.cms.futurecdn.net/dAwPEozB9GMMhAngdFJTHb-2560-80.png)

## So is this fixed now, and am I safe from the exploit?

Patches have indeed been deployed to seal up these exploits. The PHP team issued emergency security updates yesterday for PHP 8.5, 8.4, 8.3, and 8.2 – the relevant fixed versions are 8.5.12, 8.4.27, 8.3.36, and 8.2.35.

Of course, having the patch ready is just the first move – the owners of the affected websites must then apply it. They may need to install the update themselves, or contact their hosting provider to ensure that this has been done.

Obviously given the urgency of the situation, this patching work should have been done by now – and you should be safe on any given website in theory. However, the caveat here is that there's no cast-iron guarantee, and you need to bear this in mind.

It's worth noting that in terms of taking action, there's nothing you need to do yourself as a person browsing the web. These aren't patches for web browsers – this is something website owners have to sort out. (Although if you do run a website using, say, WordPress, then you must check with your hosting provider that PHP has been updated to the fixed versions noted above).

## In terms of practical realities, what should I be aware of when browsing the web today?

For starters, you may encounter websites which are down for maintenance because they are busy applying the mentioned patch to fix the PHP2Shell vulnerabilities. That's a potential annoyance, but a short-term one, and obviously it's a good thing (these patches need to be installed). At this point, though, major websites who are affected and use PHP are likely to have done this work already (given the urgency).

Otherwise, take some extra care about where you're browsing for the rest of this week – though you should always be cautious and bear in mind basic internet safety principles as a matter of course – and be on the lookout for anything that feels suspicious. Be especially careful if you're suddenly redirected to another website, or something obviously suspect happens like a download firing up out of nowhere. In such an eventuality, close the website (and browser) and don't go back, then fire up your antivirus and run a scan.

If you can, it's advisable to steer clear of the potentially less well-maintained corners of the web, too, as a hidden danger is sites which are still running versions of PHP that aren't officially supported (meaning 8.1 or older). Due to that lack of support, these won't get the relevant security updates piped through until the PHP version is upgraded to one that's supported. Those running PHP 8.1 (or earlier) who can't organize such an upgrade are being advised in some cases to take their website offline for the time being (or at least use mitigations as a stopgap, as per a post from the NCSC in the UK).

## Is AI to blame for this?

No, but if you've heard AI mentioned in connection with PHP2Shell, it's because these days, AI is more broadly making life easier for would-be malicious actors when they catch wind of fresh exploits like this.

> Be especially careful if you're suddenly redirected to another website, or something obviously suspect happens like a download firing up out of nowhere.

Amazon Threat Intelligence explains: "In the past, most exploitation we observed came after a public proof of concept was released. A small number of capable actors built exploits, and everyone else waited for them. That dependency is weakening. AI-assisted analysis makes it cheaper to turn a patch diff or advisory into a working exploit. As a result, more actors can act within hours or even minutes once technical details of a vulnerability are disclosed."

The other side of the coin is that AI is being used in defending against the bad actors out there, too, but the worry remains that in the longer run, it's likely to cause more harm than good in terms of accelerating how emerging vulnerabilities are capitalized on.
