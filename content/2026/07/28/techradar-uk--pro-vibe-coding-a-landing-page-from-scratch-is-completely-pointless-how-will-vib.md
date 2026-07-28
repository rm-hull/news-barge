---
title: '"Vibe-coding a landing page from scratch is completely pointless": How will
  vibe coding really impact the future of website building?'
source_url: https://www.techradar.com/pro/vibe-coding-a-landing-page-from-scratch-is-completely-pointless-how-will-vibe-coding-really-impact-the-future-of-website-building
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-28T14:30:32Z'
published: '2026-07-28T00:00:00Z'
description: Is vibe-coding really the answer to all your website-building needs?
image: https://cdn.mos.cms.futurecdn.net/4Z3dRaFbPa4jdSkQtjfvhe-1920-80.png
---

![Nikita Obukhov headshot on a purple background](https://cdn.mos.cms.futurecdn.net/4Z3dRaFbPa4jdSkQtjfvhe.png) 

Vibe coding lets you create everything from one-page websites to complex applications simply by explaining what you want in plain English. 

This relatively new technology is an undeniable game-changer, tearing down barriers, helping small businesses and entrepreneurs build tools that just would not have been accessible before. 

But is vibe coding really all it is made out to be? 

I caught up with Nikita Obukhov, Founder and CEO of website-building platform Tilda, to get his thoughts on how vibe coding is, and isn't, going to change how we approach website building. We also dive into some of the risks associated with vibe coding and hear some advice on where it can be best applied to help you grow your business.

![headshot Nikita Obukhov](https://cdn.mos.cms.futurecdn.net/CtoBhGepUwva6xVxLLpNqi.jpg) 

![Owain Williams](https://cdn.mos.cms.futurecdn.net/yLKEi5rn5TCTcqYsfAHXDf.jpg) 

## How is vibe coding challenging the more established drag-and-drop website builder space?

The rate of progress in neural networks is insane. Everything is moving very fast: new top-tier models arrive every six months, and what looked impossible a year ago is now generated at really good, really stable quality. Naturally, for us — and for every website builder out there — that's stressful, a zone of discomfort.

Tilda made building a website accessible to a non-professional. Before that, you had to deploy WordPress or some CMS, and if you weren't a technical specialist, you couldn't really do it properly on your own.

Now building a site has been democratised and is as accessible as editing an ordinary Google Doc. The whole concept of the modern website builder is exactly that: letting anyone create a site without technical skills. Now, what AI generates simplifies the process even further.

For site builders, this is a moment of discomfort and stress. And it sets off a search: where can site builders still be useful? It strongly affects the overall product roadmap.

I can't say that the search is finished. We're in the middle of working it out, of finding the point: why not just go to the neural network — why go to a site builder as well? It's a process of transformation, and we hope we'll come through it and stay useful to the user.

## How does vibe coding a website differ from using an AI website builder?

Vibe coding brings in editing by voice: you tell the agent in text or out loud what you want, and the agent generates it. It's genuinely new.


The term "vibe coding" is itself very blurry. You can call it vibe coding when you simply ask a chat interface to generate code and get plain HTML back; then there's vibe coding where an agent builds you a full site out of several files, spins up a virtual environment on localhost so you can test, and lets you connect databases if you need more than a static site.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Site builders brought visual editing — making editing simpler without touching code. Vibe coding brings in editing by voice: you tell the agent in text or out loud what you want, and the agent generates it. It's genuinely new.

Vibe coding lets you work in your own infrastructure. Most often you either pick a service to host your generated code and deploy, or you go the classic route: take a virtual server and set up deployment there.

With an AI website builder, all the interaction happens on the platform itself. Even though the neural network underneath is effectively the same in both cases (both vibe coding and the builder are usually running some top-tier model under the hood), that's exactly where the fundamental difference lies: either you work entirely in your own — or rather, rented — environment, or you work inside the website builder's ecosystem.

Both have their pros and cons. Pure vibe coding gives you the most control. You're no longer limited by the site builder's platform, but it adds complexity. You need to think about things most people don't anticipate when they start.

Take image loading. You need to know the current best practice: images should ideally sit on a CDN. So now you also have to work out how to deploy your images to a CDN. With a website builder, all the code and everything else lives on the builder's infrastructure, so you never think about it.

Second, protection from DDoS attacks. If your business has any visibility at all, taking down a site on an ordinary VPS is very easy. So you have to think about how to protect it. Fortunately, Cloudflare has a nominally free tier, but it's still something to think about, because DDoS attacks are fairly common.

Ultimately, with vibe coding, you write everything yourself via an agent that simplifies a lot for you; you barely touch the code. With a builder, you work inside the site builder's ecosystem, using the interface — and, naturally, using prompting to create the design as well.

## Will vibe coding eventually replace drag-and-drop website builders?

Realistically, I think we'll end up with both. Vibe coding still has a difficult entry point; it's slower and harder. Site builders are integrating vibe coding themselves, Tilda included: we've released a vibe coding tool called Vibe Block, where you generate blocks or entire pages from a prompt in exactly the same way.

But site builders go further. I don't believe they'll disappear entirely. It's a whole platform; site builders take hosting off your hands completely and give you a convenient tool for controlling things not only by voice but graphically.

On top of that, AI may not fully understand you, may not quite do what you need if you want your own high-quality, distinctive solution. Take Zero Block, for instance: it's a Photoshop or Figma equivalent, a fully graphical interface where designers work and produce exactly what the client needs. That's hard to achieve through vibe coding.

For ordinary users, a website builder is simply faster. It absorbs a huge amount of what you'd otherwise have to do yourself. An ordinary entrepreneur running a small organisation has no need to get into server hosting or how to issue a certificate. They have other things to do. So they'll go to a site builder regardless.

## Greater control isn’t always a good thing. How does Tilda set guardrails to protect against poor design decisions?

Tilda doesn't constrain you at all and, unfortunately, doesn't protect you from bad design decisions.

If a user doesn’t have graphic design skills — they use the ready-made blocks from the block library, and that protects them. Those are good, proven design decisions that stop you from making a complete mess. And as your level rises and you're no longer afraid of free-form design, Zero Block lets you make anything at all.

Users are protected in a lot of places from bad practice, because a great deal of niche, purely technical work sits under the hood. By default, all images load lazily. Under the hood, they're also adapted, converted to modern formats, and compressed. The platform takes all that nonsense on itself.

## Vibe coding offers users an opportunity to build complex tools using plain-English prompts. Does using it for simple tasks like landing page creation risk overcomplicating things?

Vibe-coding a landing page from scratch is completely pointless.


In my view, vibe-coding a landing page from scratch is completely pointless — regardless of the website builder. On one hand, as a user, it's interesting. Plenty of people who love technology will get a kick out of going through it.

But if you look under the hood — do the site's visitors actually get any benefit from it being vibe-coded rather than built on a site builder? No. On the contrary, there are more opportunities to make a mistake.

For example, how do you share editing rights? That's a simple thing a site builder always gives you out of the box. With a website builder, you can let someone manage products but not page content, for example. That's a perfectly ordinary question of permissions management, and it protects your site. With vibe coding, you still have to work out how to do it properly and grant those rights.

In my opinion, vibe code is excessive for most sites. It’s brilliant for building micro-SaaS. But for building landing pages or simple sales material? Absolutely not, because it still ends up cheaper and faster on a builder, even if in this current wave of enthusiasm it doesn't feel that way.

## Vibe coding outputs often need repetitive tweaking to make them fit for purpose. Is vibe coding really the time saver it is made out to be?

On one hand, a neural network gives you freedom, but on the other, you have to be able to articulate what you want. That's a problem. Users try vibe code, write something, and aren't happy with the result because the neural network generated it badly. Then you have to sit there prompting and fiddling to get the quality you want.

A site builder still works very well when you don't know what you want. You get a large block library and a large template library — you can pick a style visually and see exactly what you're going to get, rather than waiting for it all to generate and cycling through ten attempts.

The biggest problem with prompting, of course, is the time between iterations. You wait while the neural network generates and regenerates the code, and that's slow. Sometimes it's very hard to make exactly the change an interface would let you make easily. Explaining in a prompt that you want this changed to that can be devilishly hard. In the end, you're spending time on something as trivial as recolouring a button: five seconds in the interface, whereas here you write a prompt, it thinks, it regenerates the style — that's a minute.

So making changes through prompts is fairly tiring. Which is why we see the future in synergy: you get the first result with vibe code, then refine the details through the interface.

## Are there any security issues users should be aware of when using vibe coding to create websites?

If you're selling products, say, vibe-coding an online store…well, good luck.


First, security in the sense of things simply working: a neural network can break your project, taking it from working to non-working through some internal error or problem. A neural network is a roulette wheel — it can hit the jackpot or lose everything. It's much the same here.

Second, you still need to write the code correctly. If you're selling products, say, vibe-coding an online store…well, good luck. I wouldn't risk it, because there are price calculations, stock checks, a lot of things we've been doing for a very long time.

A neural network is a roulette wheel — it can hit the jackpot or lose everything.


Equally, you don't always understand what it has written. If you're building in interaction with users and personal data and taking it further, you're creating risk for the users who trust you with that data. If you've also vibe-coded some mini-CRM of your own inside, that adds to the exposure.

If you have a static site — just a landing page that displays things — there's nothing much there; a static site is hard to do anything with. But once you start processing orders or submissions inside it, or accumulating user data, that puts your service at serious risk, and the risk is a certainty. We see it in practice, and it shows up in the news: people get a fast result, and it turns out to be unreliable. So you have to assess the risks soberly, and it's better to avoid them.

![Owain Williams](https://cdn.mos.cms.futurecdn.net/yLKEi5rn5TCTcqYsfAHXDf.jpg)

Owain has been building websites and online stores for his own and his client's businesses for over 8 years. Having taken on a role at TechRadar Pro in 2023, he now leads on all website builder and CRM content, spending his days researching, testing, and reviewing some of the best website building and CRM platforms on the market. He also has a passion for helping people get a great deal on website builders, delivering the best coupon and promo codes on the market. With an extensive background in business, Owain holds a BA(Hons) in Business and Marketing and has written for several leading publications including MarketingProfs, Website Builder Expert, Digital Doughnut, and NealSchaffer.com.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
