---
title: Hostinger cut server response times by 35% – here's how to speed up your website
  even further
source_url: https://www.techradar.com/pro/hostinger-cut-server-response-times-by-35-percent-heres-how-to-speed-up-your-website-even-further
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-13T16:58:18Z'
published: '2026-10-13T00:00:00Z'
description: Mario Bañares Colastra, Head of Web Hosting at Hostinger, explains how
  they've sped up users' websites – and why it won't cost you anything
image: https://cdn.mos.cms.futurecdn.net/QPzNuVoKGp9mLqDeQL4snd-2000-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
- Creator Economy & Marketing
people:
- Hostinger
- Mario Bañares Colastra
locations:
- Hostinger
organisations:
- CPU
- ECDSA
- Hostinger CDN
- Owain Williams
- RSA
- SSL
- TechRadar Pro
- Web Hosting
---

![headshot on a purple background ](https://cdn.mos.cms.futurecdn.net/QPzNuVoKGp9mLqDeQL4snd-1920-80.jpg)

(Image credit: Future)

When Hostinger told me that they had cut server response times by 35%, all without investing in additional hardware or infrastructure, I was both impressed and intrigued.

Typically, hosting providers have to invest a notable sum to improve response times – the cost of which is then handed back to users in the form of subscription increases.   
I wanted to know more. How did they do it? What does better server response times actually mean for users? Will subscription costs increase?   
I caught up with Mario Bañares Colastra, Head of Web Hosting at Hostinger, to get some answers.

![headshot of Mario Bañares Colastra, Head of Web Hosting at Hostinger](https://cdn.mos.cms.futurecdn.net/MNoivTE2E4XVGYih2YWppG-140-80.jpg)
![Owain Williams](https://cdn.mos.cms.futurecdn.net/yLKEi5rn5TCTcqYsfAHXDf-140-80.jpg)

## Why did Hostinger decide to look at altering code and architecture instead of investing in more hardware or infrastructure?

We had already looked at the hardware route. Putting the CDN on all web hosting plans would have required roughly doubling our server count. Making the CDN itself more efficient was the better option.

That worked. We cut the computing resources needed to run the CDN by 45 to 50%, with no new servers or hardware. The result is faster sites for customers. Even sites that don’t use the CDN got faster because our servers are under less pressure overall.

## Can you briefly walk us through the process you followed to audit your setup and identify areas where performance could be improved?

We measured first, then fixed.   
We set up dashboards for each server and monitoring based on real visitors’ experience, so we could see how the CDN performed in practice. Then we looked closely at where the processing power (CPU) was going. Encrypted connections and image processing stood out.

Before changing the certificates, we checked that visitors’ browsers and devices would keep connecting without problems. After the change, we checked the results against real-user data.

## Which area turned out to be the biggest bottleneck in your existing infrastructure? How did you overcome it?

The biggest drain on processing power was encrypted connections and image processing.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

For encryption, we moved our SSL certificates from RSA to a more efficient type called ECDSA, which cut the CPU used for SSL operations to about a third. We also adopted kernel TLS and improved session resumption, so returning visitors cost less to serve.

For repeated work, image conversions now happen once and get reused across the network instead of being repeated in several places. Requests also go through the CDN location closest to where the website is hosted, over connections that are already open and ready to use.

## A 35% cut in server response times sounds impressive, but what does that actually mean for small businesses using Hostinger?

It means our customers’ websites start responding faster when someone opens them. On average, that’s about a quarter of a second sooner. It sounds small, but it happens on every visit, to every page.

Across our infrastructure, the average wait fell from 965 milliseconds to 714, about 26%. On our older servers, it was 35%, which is where the number comes from. These are still early results.

Speed also depends on things like image sizes and plugins, so results will vary from site to site.

The change also helped our lower-priced plans. Their servers used to be busier than the ones for our higher plans, and now they are less busy, which gives them more room to work.

There’s more to come. Subdomains, such as shop.yoursite.com, weren’t included in the earlier rollouts. We’re enabling the Hostinger CDN on them this quarter too, so the improvement could be even bigger for sites that use subdomains.

## As website assets continue to get heavier, what else can small businesses be doing to prepare their websites for the future?

Heavier pages mostly come from images, scripts, and plugins. Start with the basics:

* Images. Use modern formats like WebP or AVIF. Hostinger CDN can also resize and convert images on the fly, so you don’t need to change your site.
* Caching. Turn on browser caching, and for WordPress use a caching plugin.
* Plugins and scripts. Keep analytics, chat widgets, and extra fonts to the ones you really use, since each one adds requests.
* Lazy loading. Load images below the fold only when visitors scroll to them.
* Monitoring. Check resource usage and measure Core Web Vitals. A good goal is a page load in under two seconds.

Ideally, the platform handles as much of this as possible, so business owners don’t have to become performance experts.

## Why did you decide to roll this out to all users for free?

Once the CDN became cheaper to run, we decided every customer should get it, not only those on higher plans. We offer it at no additional cost.  
Our optimization cut the resources needed to run it drastically, so there was no good reason to keep it for higher-priced plans. It also took pressure off our lower-tier web hosting servers, which helps customers and our infrastructure at the same time. We believe improvements like this should be standard, not something people pay extra for.
