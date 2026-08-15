---
title: '‘Every other industry running mission critical infrastructure solved this
  problem years ago’: Why autonomous networking is in dire need of a digital twin'
source_url: https://www.techradar.com/pro/every-other-industry-running-mission-critical-infrastructure-solved-this-problem-years-ago-why-autonomous-networking-is-in-dire-need-of-a-digital-twin
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-15T12:55:29Z'
published: '2026-08-15T00:00:00Z'
description: We’re not short of network outages – could digital twins solve them?
image: https://cdn.mos.cms.futurecdn.net/pVCXKrhThqmUjYVSZBjV5Z-2560-80.jpg
---

![Hands on a laptop with overlaid logos representing network security](https://cdn.mos.cms.futurecdn.net/pVCXKrhThqmUjYVSZBjV5Z.jpg) 

Networking never fails to surprise me when it comes to dependencies and its live nature – it’s a world that’s continually changing, and yes upgrades designed to improve performance or security are often the ones that cause outages.

Even carefully planned updates can have consequences that might initially be difficult to see during early pilots and test, due to a highly dependent mix of switches, firewalls, clouds and more – not to mention the challenges that come with interoperability in a world of mixed vendors.

Until now, it’s mostly been a firefighting exercise of responding to incidents and outages as they happen, admitting that they’re just an inevitable outcome of virtually any change.

## Autonomous networking needs a safety-first design

Forward (formerly Forward Networking) wants to challenge this in its entirety, though, and the work it and companies like it are doing could fundamentally revolutionize network stability and uptime, significantly reducing costs.

Its solution is a mathematically accurate digital twin of the production environment, giving companies space to make changes and observe unintended impacts without actually affecting the real deal.

The principle isn’t anything new at all, and it’s been used in software development and other areas for decades, but where it could really shine is in an upcoming age of automated networking. Forward argues that providing a place for systems to autonomously test changes pre-deployment is a necessary stage to true automation.

I wanted to know whether technology like this could have prevented some major high-profile incidents lately, including those we’ve seen relating to Amazon, Cloudflare and more, and spoke to Forward’s co-founder and Chief AI Officer, Nikhil Handigol, on some of the technology’s biggest challenges, including how the digital twin could stay current and why pre-deployment proof could become essential in the world of autonomy.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

- **Forward proposes to prevent 100% of network outages caused by configuration errors. Are there any strings attached? And what does a “mathematically accurate digital twin of the entire production network” actually mean?**

There are no strings, but let’s be precise on what that rests on. Forward Predict eliminates network risks through routing validation, end-to-end path analysis, firewall and ACL verification, segmentation and compliance verification, and automated regression testing.

The closest parallel is what software development did with continuous integration. No code goes to production without being tested first. Forward Predict brings that same discipline to networking.

Every proposed change is tested against the full production-equivalent model before it touches a live environment – routing validation, end-to-end path analysis, firewall and ACL verification, segmentation and compliance verification, and automated regression testing.

That model isn’t a sample or a simplification. It's built from the configuration and operational state of every device in the network — every vendor, every OS, every layer from L2 to L7, on-premises and in the cloud — using header space analysis to trace every possible path any packet can take.

The platform regularly collects state from the live network, and you can trigger a fresh snapshot on demand immediately before a push, so the "digital twin" you're testing against is always current. That continuous synchronization is what makes the math trustworthy: a proof is only as good as its inputs, and this is how we keep the inputs honest.

Run a change through that model and you get a deterministic outcome with evidence, not a guess. If it breaks something, if it opens a security hole, if it creates an unintended path, you see exactly why.

And because the answer comes from mathematical path analysis rather than a probabilistic risk score, it doesn't degrade as the network grows more complex.

Pair that with Forward AI and the platform does not just flag the problem, it iterates on its own until it lands on a change that is verified to deliver the intended behavior. Change windows that once took weeks now take minutes. There is no anxiety pushing a change live, because you already know how it ends. Weekends are for time off, not change windows and war-rooms.

- **One point I wanted to raise is that you're essentially pegging it against a snapshot. Sysadmins will tell you that networks change. Firmware get updated, access points get refreshed, switches swapped and servers decommissioned. How do you make sure that Forward remains relevant throughout the lifecycle of the production network?**

Forward Enterprise regularly collects configuration and state from every device in the estate, and you can trigger an on-demand snapshot immediately before pushing a change for absolute certainty.

When firmware gets patched, when an access point gets refreshed, when a switch is swapped, when a server is decommissioned, any change to the network is updated in the digital twin, it is a mathematically accurate model of the entire production network.

This is exactly why the underlying model holds up under scrutiny. Our engineering team validates the software against real behavior on live test hardware from every supported vendor, so the model's fidelity is proven before it ever reaches a customer network.

Then in production, that same discipline continues against the customer's own, constantly changing estate. Sysadmins are right that networks never sit still. Neither does the network digital twin. That is the only way proof stays proof instead of becoming a guess based on past behavior.

- **Are there other companies that compete with Forward? How does your proposition differ from theirs?**

The competitive threat isn't another vendor. It's a set of processes built over decades, in an era before a network could be modeled at all, that include change windows, war rooms, and the belief that the only place to truly test a network change is the production network itself.

Every other industry running mission critical infrastructure solved this problem years ago. Airlines train pilots on flight simulators instead of real aircraft. Pharmaceutical companies model outcomes before anything reaches a patient.

Manufacturing validates changes on a digital twin before touching the factory floor. Software development has run on continuous integration for two decades, where no code ships without being tested first.

Networking is the industry that never got its equivalent, not because nobody wanted one, but because building a mathematically accurate network digital twin is genuinely hard.

Against observability and monitoring vendors, the difference is which question gets answered. Those tools are essential for understanding what already happened on the network. Forward Predict answers a different question entirely, what will happen if this change is made, and it answers it with a deterministic proof rather than an educated guess.

Against other platforms using the words “digital twin,” the difference is a decade of foundational work building a model with header space analysis across all major vendors, every device, and every layer, rather than a partial view stitched together after the fact. That foundation cannot be a shortcut, and it is the part everyone else in the category is still missing.

- **How do you see Forward evolving in terms of features and roadmap? Could this pre-emptive, predictive approach find a receptive audience in other sectors?**

The roadmap moves in one direction, widening the aperture of what gets proven before it goes live. Today Forward Predict proves the outcome of changes to connectivity and security. Next is broader impact analysis.

We are not predicting what may happen, we are proving what a network will do, because a network's behavior can actually be modeled with mathematical certainty in a way human intent cannot.

That distinction is exactly why this belongs anywhere teams run complex, interconnected infrastructure with the same stakes, critical infrastructure operators running their own networks underneath everything else.

Wherever teams are changing complex systems without a way to prove the outcome first, the same problem exists, and the same fix applies.

Where this is headed fastest, though, is autonomous networking. As agents start proposing and executing changes at machine speed, a mistake stops being a single event and starts propagating at scale.

Proof is not an added feature there. It becomes the precondition for letting an agent operate at all.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.* 

![Desire Athow](https://cdn.mos.cms.futurecdn.net/oEw3XiohQwun9z7gMxKzkB.jpg)

Désiré has been musing and writing about technology during a career spanning four decades. He dabbled in website builders and web hosting when DHTML and frames were in vogue and started narrating about the impact of technology on society just before the start of the Y2K hysteria at the turn of the last millennium.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
