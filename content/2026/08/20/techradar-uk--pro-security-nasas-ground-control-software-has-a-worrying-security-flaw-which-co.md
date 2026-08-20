---
title: NASA's ground control software has a worrying security flaw which could let
  hackers contact spacecraft
source_url: https://www.techradar.com/pro/security/nasas-ground-control-software-has-a-worrying-security-flaw-which-could-let-hackers-contact-spacecraft
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-20T20:40:18Z'
published: '2026-08-20T00:00:00Z'
description: Ground control to major hack
image: https://cdn.mos.cms.futurecdn.net/S52AXmcF8SwjhEHAXXYc7k-2560-80.jpg
---

![NASA](https://cdn.mos.cms.futurecdn.net/S52AXmcF8SwjhEHAXXYc7k.jpg) 

- **NASA’s ground control software has a critical vulnerability that could allow third-party access to spacecraft**
- **The flaw has been found in a browser-based variant of NASA’s AMMOS Instrument Toolkit**
- **NASA has not publicly responded to the flaw’s disclosure**

NASA’s open source ground control software has a critical vulnerability that could enable an unauthenticated attacker to gain access and take control of spacecraft. The AMMOS Instrument Toolkit’s browser-based interface is the source of the vulnerability, which has since been resolved.

The AIT-GUI (AMMOS Instrument Toolkit Graphical User Interface) tool up to version 2.5.1 has been identified as vulnerable, but the fault has been fixed in v2.5.2, according to researcher Yuval Elbar.

If the vulnerability had been found by a third party, it would have given access to issue commands to spacecraft, instruments, and execute server-side scripts. In addition, command sequences could potentially have been run by an attacker, leaving craft almost wholly beyond NASA’s control.

## Weak API

Elbar, who works with the Cycode Agentic Development Security Platform, disclosed the vulnerability on August 18, 2026. The problem appears to start with AIT-GUI running as a web server with all network interfaces open, rather than the host’s setting. Incredibly, the API also has no authentication, or authorization protection. In addition, the CSRF (cross-site request forgery) protection on changing endpoints is also absent on affected versions of AIT-GUI.

Attackers can exploit basic access-control security failings in AIT-GUI, exposing the /cmd and /script/run and /seq prompts while also setting up filesystem paths. This enables files (potentially malware, or custom-built scripts) to be passed directly to NASA craft via a vulnerable AIT-GUI browser session, potentially escalating to full control.

To emphasize the scale of the weakness, Elbar introduced the disclosure with “A web GUI used to drive spacecraft and instrument commanding shipped a server that listens on every network interface, asks nobody for a password, and can be steered by any web page an operator happens to open.”

## External access

As if this wasn’t concerning enough, the attacker doesn’t need to be on the same network. Direct access via an exposed port, or directing an operator to a web page hiding malicious code, or even simply a web page under live control by an attacker, can afford access to a third party.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Elbar adds “operational and ground-system software inherits the same web weaknesses as everything else, but with a far higher cost of failure. Auth, CSRF defense, and input confinement are not optional extras on a panel that commands hardware.”

Cycode advises administrators of AIT systems to upgrade AIT-GUI to v2.5.2 and run checks on the console port. They should also review command history.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Christian Cawley](https://cdn.mos.cms.futurecdn.net/zBDYnjPnB2XPvhKbYX9Kuc.png)

Christian Cawley has extensive experience as a writer and editor in consumer electronics, IT and entertainment media. He has contributed to TechRadar since 2017 and has been published in Computer Weekly, Linux Format, ComputerActive, and other publications.

He currently heads up the team at smart home website Matter Alpha, and writes about retro gaming at Gaming Retro.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
