---
title: In Spain, football matches knock thousands of websites and online services
  offline
source_url: https://www.euronews.com/next/2026/09/18/in-spain-football-matches-knock-thousands-of-websites-and-online-services-offline
source_site: Euronews
source_slug: euronews
scraped_at: '2026-09-18T04:33:25Z'
published: '2026-09-18T00:00:00Z'
description: Spain's football season kick-off has revived LaLiga's court-backed mass
  IP blocking against piracy, but thousands see websites and services fail whenever
  a match begins.
image: https://images.euronews.com/articles/stories/09/91/03/90/1200x675_cmsv2_6cb05931-ebd0-5050-a51f-0cd76e690367-9910390.jpg
categories:
- Europe
- News & Politics
- Sports
locations:
- Barcelona
- Córdoba
- Europe
- Madrid
- Spain
people:
- Demis Hassabis
- Halliday
- Javier Tebas
- Jensen Huang
- Junts
- King Charles
- LaLiga
- Vinicius
organisations:
- Akamai
- Alibaba Cloud
- Amazon AWS
- Amnesty International
- Apple
- Arsenal
- Biomedical Research Networking Centre
- CDN
- Cloudflare IPs
- Commercial Court
- Compromís
- DIGI
- ECH
- ERC
- Elche C.F.
- Greenpeace
- LaLiga
- LaLiga**
- Meta
- Microsoft
- Movistar
- MásOrange
- Nvidia
- OONI
- Ollama
- Open Observatory of Network Interference
- PNV
- PP
- PSOE
- RAE**
- Real Madrid
- Redsys**
- Sumar
- Telefónica Audiovisual Digital
- UNHCR
- UNICEF
- URL
- VPNs
- Vodafone
- Vox
---

## Spain's football season kick-off has revived LaLiga's court-backed mass IP blocking against piracy, but thousands see websites and services fail whenever a match begins.

Every new football season also brings back one of the most aggressive digital filtering mechanisms in Europe. Backed by court rulings, **LaLiga**, the league body headed by Javier Tebas, orders Spanish operators to block in real time hundreds of IP addresses supposedly linked to the illegal broadcasting of matches.

The original aim is to curb piracy, but the real effect is another: the internet does not work with dedicated servers for each website, so when an IP is cut off, a whole series of services that have nothing to do with football are dragged down with it. In other words, **LaLiga has court-backed powers that allow it to notify a set of IPs and have them blocked in Spain**. And this clearly undermines the principle of net neutrality.

The problem is that **not every website or web service has its own IP address** acting as an ID card. There are hosting services that serve many websites from a single parent address and this is where the problems begin, because when that address from which services and websites hang is blocked, they also stop working. That is collateral damage for any internet user who tries to visit them while a match is on.

To illustrate the point, it would be like saying that in Madrid (the hosting service) among the millions of people in the city there is a neighbour who is stealing electricity (pirating LaLiga's IPTV signal), and ordering the power to be cut off for the whole of Madrid.

In an interview Tebas went so far as to claim that there were no mass blocks and that the complaints they were receiving came from "a few geeks". Yet the reality is clear, with blocks that do affect third-party services and between 500 and 1,000 IPs blocked per match.

## How do the blocks work?

Blocking starts shortly before kick-off and is lifted when the broadcast ends. LaLiga identifies IP addresses associated with pirate services and asks operators to cut them off during that time slot. On the opening matchday of the 2026-2027 season, 15 August 2026, around 550 IP addresses were blocked simultaneously. Since then, the blocks have continued on every match day.

The Open Observatory of Network Interference (OONI) estimates that **in the first half of 2026, 7,441 addresses belonging to 36 different providers were blocked**, including Amazon AWS, Cloudflare, Akamai, Alibaba Cloud, Microsoft and Meta.

LaLiga maintains that these are dynamic blocks that are neither massive nor indiscriminate, and justifies them by pointing to annual losses, which it puts at between 600 and 700 million euros, because of piracy of its broadcasts. But innocent parties end up paying the price.

The underlying problem is **the way the internet works, which clashes directly with the method proposed by LaLiga as a solution** and, contrary to its claims, does in fact hit thousands of websites every time there is a match in Spain. In fact, there is a web service to check whether this type of cut-off is happening: hayahora.futbol*(source in Spanish)*.

A content delivery network (CDN) such as Cloudflare *(source in Spanish)* caches under a single IP address thousands of pieces of content from services that are independent of each other. It improves loading times by serving content from locations closer to the end user with less latency and also minimises problems caused by DDoS attacks.

If the CDN's IP is blocked, content from thousands of services and sites is blocked, and the current system cannot tell whether the user was trying to access that pirate stream or a **site such as that of the RAE**, Amnesty International, Greenpeace, UNICEF, UNHCR or Caritas, courts, universities and projects such as** Hugging Face**, which hosts AI LLM models, or even** some football clubs' websites and those of their sponsors**, pure rhetorical irony of this blocking method.

The OONI report, which cross-referenced measurements recorded in Spain between January and June 2026 with a list of 9.2 million domains, estimates that more than 554,000 legitimate domains were affected at some point. **Cloudflare** took the brunt of the damage: with only 30% of the blocked IPs,**it accounted for 90% of the affected domains, more than 501,000**.

In Spain, one of the best-known cases is the payment service **Redsys**, which has suffered repeated failures in confirming online payments during LaLiga matchdays, without affected retailers even knowing where the problem lay. At other times** WikiDex**, the largest encyclopaedia on Pokémon in Spanish, has also been hit, reporting access problems to its image servers.

## A practical case during Real Madrid's match on 15 September

In my own case, with DIGI fibre, I have noticed blocks during previous matches when downloading open LLM models to my server from Hugging Face (usually hosted on AWS), when using services for a pair of smart glasses (Halliday) or even when trying to view certain websites. If anyone can find the connection between those sites or services and the piracy that LaLiga talks about, please let me know.

The blocks began to increase after the start of the Elche C.F. v Real Madrid match, with Cloudflare IPs blocked by Spain's five main internet operators.

During the match night, **some websites are completely inaccessible**, such as mandalaweb.es, a site offering mandalas to colour in, or todopuntodecruz.com, a site with a shop selling kits and patterns for cross-stitching.

If we use **a VPN from outside Spain, the sites mandalaweb.com or todopuntodecruz.com load without problems**, even though they have nothing to do with pirating LaLiga's IPTV match signal.

Tebas has said that the complaints come from only a few people, and has labelled them geeks, but **it is neither a small number of domains nor only minor ones**. Sites such as linuxmint.com, the supermarket froiz.es or the website of the Biomedical Research Networking Centre have all been inaccessible. The verdict is clear: this is a nationwide block carried out via internet providers, DIGI in my case.

Another example: the next day, Wednesday 16 September 2026, I tried to **download the Qwen 3.8 27b LLM model from Ollama** to my server, and the requests returned an error due to the request timing out while receiving the TLS certificate, during that day's matches, at 19:41 when I wanted to download it. Ollama's models are hosted on Cloudflare and, of course, an AI LLM model has nothing to do with football.

As can be seen below, there is also a series of blocks like the day before, due to LaLiga matches. On **15 September** the disruptions began at around 21:20 and ended after 00:00. That is to say,**almost three hours of blocking**.

On **Wednesday 16 September** the blocking began at 18:45 and lasted until shortly before 00:00, so we are talking about**between five and six hours of blocking**. In these two cases, both were weekdays; at the weekend the duration is, at best, similar.

## Technical alternatives, legal framework and expiry date

There are now more precise ways than taking down an entire IP address: acting on the domain, the URL, the account or the specific server that distributes the pirate signal, and asking the relevant provider to remove it.

**The rule should be to block the infringing content**, not shared infrastructure, because the damage caused is incalculable, with collateral harm to services and users who can no longer use the internet and apps normally during football matches. Several websites report the losses registered by services and sites.** LaLiga's cuts have already caused more than 3.1 million euros in impact**.

The legal basis for these blocks is the judgment handed down by Commercial Court No. 6 in Barcelona on 18 December 2024, upholding the claim brought by LaLiga together with Telefónica Audiovisual Digital.

The **ruling authorises the immediate cessation of access to identified IPs and allows them to be updated dynamically on a weekly basis**, even during matches, without the need for a new court order for each address. Movistar, Vodafone, DIGI and MásOrange acquiesced in the proceedings, in other words, they accepted the measures without challenging them in court.

In parliament there has been a first move, albeit still without legal force: on 29 April 2026 a non-binding motion (Proposición No de Ley) to reform the Digital Services Act *(source in Spanish)* was approved, promoted by ERC and agreed with the PSOE, with the backing of Sumar, Bildu, the PNV and Compromís. The PP and Vox voted against and Junts was absent. If it goes ahead, the reform would introduce requirements of proportionality and limits on court rulings so that they do not delegate the management of blocklists to the league body without supervision.

In response to the cut-offs, **some users have opted to use virtual private networks (VPNs) to get around them**, a tool that European courts consider neutral software and a legitimate way of using the internet.

LaLiga responds that VPNs, as a technological intermediary, also bear responsibility for the content that circulates through their infrastructure, and recalls that the Commercial Court in Córdoba has already ordered interim measures in this regard.

Nor has ECH encryption, promoted by Cloudflare and Apple to conceal the domain a user connects to, so far managed to displace IP blocking as the main containment tool.

**The 2026/2027 season will be**, in any case,** the last covered by the current ruling**, which expires on 20 June 2027, coinciding with the end of the Segunda División.

LaLiga and Telefónica are expected to request an extension in this match they have been winning for several years. However, the legal and regulatory context has changed compared with two years ago, creating real uncertainty over whether they will again obtain such a broad endorsement.

## Read more

![Real Madrid's Vinicius during the Champions League quarter-final second leg match between Real Madrid and Arsenal on 16 April 2025.](https://images.euronews.com/articles/stories/09/29/61/75/480x270_cmsv2_f2ea950b-7905-5cb6-9f26-7a0b22df9483-9296175.jpg) 

![When there's a football match, half of Spain's internet grinds to a halt.](https://images.euronews.com/articles/stories/09/91/03/90/480x270_cmsv2_6cb05931-ebd0-5050-a51f-0cd76e690367-9910390.jpg) 

![King Charles walks with Nvidia chief executive Jensen Huang and Sir Demis Hassabis. 17 September 2026](https://images.euronews.com/articles/stories/09/91/77/78/480x270_cmsv2_a89ef78c-9ef7-5b7f-91cb-f74b5f2b1dd8-9917778.jpg)
