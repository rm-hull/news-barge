---
title: Microsoft reveals the cause of its catastrophic Outlook outage — incident set
  off by a ‘cascading failure’ of servers as crash leads to chlorine gas poisoning
  of 15 hotel guests
source_url: https://www.techradar.com/computing/microsoft-365-outage-led-to-chlorine-gas-poisoning-of-15-hotel-guests-in-germany-as-microsoft-says-crash-was-caused-by-cascading-failure-rather-than-cyberattack
source_site: TechRadar UK
source_slug: techradar-uk
description: The Microsoft 365 crash led to 15 hotel guests suffering chlorine gas
  poisoning, with Microsoft revealing the outage’s cause.
image: https://cdn.mos.cms.futurecdn.net/w3RqRoZs5sUDJJ7ECsky23-2000-80.jpg
published: '2026-11-16T00:00:00Z'
scraped_at: '2026-11-16T19:38:28Z'
categories:
- Technology & Software
people: []
locations:
- Germany
- Phantasialand
- United States
organisations:
- Microsoft 365 Admin Center
- Microsoft Exchange
- Microsoft Teams
- Notebookcheck
- Reddit
- WDR
---

![The Microsoft logo next to an Outlook error message](https://cdn.mos.cms.futurecdn.net/w3RqRoZs5sUDJJ7ECsky23-1920-80.jpg)

* **The Microsoft 365 outage led to a key safety system failing in Germany**
* **This caused the chlorine gas poisoning of 15 hotel guests**
* **Microsoft has since revealed exactly what caused the outage**

If you were affected by last week’s global Microsoft 365 outage, chances are you had trouble accessing your email. You probably didn’t expect to be poisoned as a result, yet that’s exactly what happened to over a dozen unfortunate hotel guests in Germany — but Microsoft has reported that the blackout wasn’t caused by a cyberattack.

According to a news report from German outlet WDR (via Notebookcheck), 15 guests at a hotel for the Phantasialand theme park were injured when the park’s swimming pool received excessive levels of chlorine. This was caused by a malfunction in the chlorine monitoring system, but because alerts are sent to park staff over email — and because those email systems were down due to the Microsoft 365 outage — no one knew about the problem until guests started getting sick.

According to a Facebook post made by the fire department that responded to the incident, 40 first responders were dispatched and 15 guests were triaged after the chlorine gas leak. WDR reported that the affected people suffered from respiratory irritation, with four needing to be taken to hospital.

The episode illustrates the serious — and often unexpected — consequences that can arise when something as central to a business’s operations as an email system goes down. When it’s responsible for important safety procedures, the results can be potentially life-threatening.

## Microsoft’s post-mortem report

![Shutterstock.com / kanlaya wanon](https://cdn.mos.cms.futurecdn.net/TJirAeNdL3RwDzNaPiWTc8-970-80.jpg)

Since the outage, Microsoft has said that full service has been resumed. It has since published a post-incident report, which is available in the Microsoft 365 Admin Center portal. The full write up has also been relayed on Reddit.

In the report, Microsoft revealed that the outage was caused by three principal factors: a “latent defect” from July that overwhelmed Windows servers; a Microsoft Teams failure that increased the load on a system shared with Microsoft Exchange; and the fact that 14% of server capacity for the networking system was out of service at the time.

Taken individually, these factors were not enough to cause the global failure. But when the increased load and the lower server capacity combined, they triggered the latent defect. Server requests then piled up until the servers stopped responding — which happened to occur during the peak traffic window for the United States.

Sign up for breaking news, reviews, opinion, top tech deals, and more.

As a mitigation effort, traffic was automatically redirected towards healthy endpoints. However, this process made those endpoints more likely to themselves encounter the latent defect. “This caused a cascading failure from server to server as the same amount of load was spread across fewer servers,” Microsoft wrote. At its worst point, the outage had caused 80% of available servers to become unresponsive.

Due to a separate issue, Microsoft’s bulwarks against such a cascading failure did not function properly. Recovery took longer than expected because restored servers were immediately overwhelmed by pent up traffic, making them fail once again. And because the latent defect dated back to July, simply rolling back to a recent version was not enough.

To fix the outage once and for all, Microsoft had to return its code path to that of a previously good state, then take servers offline in batches, roll out the patch across its infrastructure, then restart its systems. Eventually, service was restored.

The post-incident report is a sobering reminder of what can happen when several seemingly independent issues can converge all at once, and of the consequences that are possible when that happens on such a large scale. And as the chlorine incident in Germany demonstrates, these failures often go beyond mere technical disruption and touch on people’s health and wellbeing.

![An Apple MacBook Air against a white background](https://cdn.mos.cms.futurecdn.net/LocVgRosBUWfJzDitFzhKR-140-80.png)

➡️ **Read our full guide to the best laptops1. Best overall:**Apple MacBook Air 13-inch M5** 2. Best budget:**Apple MacBook Neo** 3. Best Windows 11 laptop**Microsoft Surface Laptop 13-inch** 4. Best thin and light:**Lenovo Yoga Slim 9i** 5. Best Ultrabook**  
Asus Zenbook S 16
