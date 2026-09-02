---
title: We explored early DLSS 5 performance with community mods — and the limits of
  the 12V-2x6 power connector may hold it back on the RTX 5090
source_url: https://www.tomshardware.com/pc-components/gpus/we-explored-early-dlss-5-performance-with-community-mods-and-the-limits-of-the-12v-2x6-power-connector-may-hold-it-back-on-the-rtx-5090
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-02T19:22:49Z'
published: '2026-09-02T00:00:00Z'
description: A single 12V-2x6 plug might not deliver enough juice to let DLSS 5 run
  free.
image: https://cdn.mos.cms.futurecdn.net/CBBS7c4u3Y3LJcY55ryv2W-2560-80.jpg
---

![A GeForce RTX 5090 graphics card](https://cdn.mos.cms.futurecdn.net/CBBS7c4u3Y3LJcY55ryv2W.jpg) 

It's been a wild few days for gamers, as a version of the DLSS 5 model leaked with *NBA2K27* and promptly got modded into every game under the sun. After initial builds that relied on ReShade to make the model work, the community has since wrapped up DLSS 5 into an Optiscaler package that makes adding it to most games nearly painless. With that development, we wanted to get a sense of how the tech performs ahead of its official release.

We're not going to weigh in on the aesthetic or philosophical implications of applying DLSS 5 to a particular title here. That ground has been extremely well trodden already, and if you haven't been stuck under a rock this past week or so, you've likely seen what DLSS 5 can do for yourself.

We're more interested in getting an idea of the performance cost of getting DLSS 5 running, along with the power requirements it incurs. Whether you love or hate this model's effect on a game's appearance, you can weigh your feelings against the performance cost involved in getting there.

Before we get to the numbers, some caveats: the Optiscaler DLSS 5 injection method may not represent the behavior of this model when developers integrate it through Nvidia's Streamline framework. Streamline may offer less overhead and better performance than what we saw here.

But Nvidia's technical paper on DLSS 5 says that the model takes 8 ms to execute on a 4K frame, and that's essentially identical to the performance metrics that we saw from Optiscaler when it's running. So it seems unlikely that the official version will be far off the performance we measured if it's implemented in these titles using the proper channels.

For these limited tests, we chose to focus on the RTX 5090 Founders Edition's behavior under DLSS 5 to explore the largest performance drop one might expect from this community implementation of the tech.

Out of curiosity, we also grabbed MSI's RTX 5090 Lightning Z from the TH arsenal. This RTX 5090 has a unique two-12V-2x6 connector power setup and a 1000W power limit available through its Extreme vBIOS. Given the apparent arithmetic intensity of DLSS 5, we wanted to see whether running it would consume any of the extra available power headroom from that card's twin-plug design.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

For our small sample of games, we used the following basic settings: a 4K output resolution target fed by DLSS Performance upscaling (i.e., a 1920x1080 input) without frame generation, as well as maximum raster and ray-tracing quality settings (or path tracing, in the case of *Cyberpunk 2077*) and DLSS Ray Reconstruction where it was available.

We didn't use Multi Frame Generation in these tests. We want to cleanly represent the performance baseline you can expect from DLSS 5 given the above constraints.

### Cyberpunk 2077 performance

We started our performance explorations with *Cyberpunk 2077.* Optiscaler was an easy install for this game, and we confirmed that neural rendering was making the expected difference in facial detail and lighting realism when we activated it.

 ![Cyberpunk 2077 DLSS 5 performance](https://cdn.mos.cms.futurecdn.net/ijCwxLHyXQixXUASapGtYY.png) 


In exchange for those enhancements, the RTX 5090 Founders Edition takes a 42% hit from DLSS 5. Although the Lightning Z takes a slightly smaller 39% hit, its baseline performance is higher than the Founders Edition, so the MSI card maintains a 60 FPS average and much higher 1% lows than the single-connector card. That difference in smoothness is evident.

 ![Cyberpunk 2077 DLSS 5 performance](https://cdn.mos.cms.futurecdn.net/vCkRAv2SvDqhcGsAb5fAYY.png) 


Part of that difference in performance comes down to power. As we noted, the RTX 5090 Lightning Z has a much larger 1000W power limit to play with, and it puts that headroom to use here.

The jump in power consumption from DLSS 5 on the Lightning Z is eye-popping: 580 W to 723 W, or a 25% increase. The RTX 5090 Founders Edition only goes from 482 W to 551 W, which means that it's practically power-limited.

### Hogwarts Legacy performance

Unlike *Cyberpunk 2077*,* Hogwarts Legacy* doesn't implement path tracing, but its extensive RT effects are still impressive. Importantly for our purposes, it's easy to get Optiscaler into this title.

 ![Hogwarts Legacy DLSS 5 performance](https://cdn.mos.cms.futurecdn.net/fWZ5dvmd7XtXpWhcRAT5B6.png) 


*Hogwarts* exhibits the largest performance drop of these three games on the RTX 5090 FE, at 49%. The Lightning Z card drops just 42%, though, and its higher baseline performance makes for a smoother experience.

 ![Hogwarts Legacy DLSS 5 power](https://cdn.mos.cms.futurecdn.net/MNyWN9nULswei8UsZY3EoG.png) 


The Lightning Z once again illustrates just how much power DLSS 5 can pull if it's available, even in this "lighter" RT title. Without DLSS 5, the MSI card draws 480 W on average. With neural rendering enabled, it pulls 720 W, or a whopping 50% more power.

### Control performance

Finally, we tried the game that started the community DLSS 5 wave last week: 2019's *Control*. This early RT title still poses a stiff challenge for modern hardware if you crank its RT settings to the absolute max, as we did here.

 ![DLSS 5 Control performance](https://cdn.mos.cms.futurecdn.net/XhbdaCeAfd5jSoBVtxrmBP.png) 


The RTX 5090 Founders Edition takes another 42% hit to performance under these conditions, and the Lightning Z also drops 42%. But the higher power limits of the MSI card let it deliver 20% higher average frame rates and much higher 1% lows than the Founders Edition, and that's a smoothness boost you can really feel.

 ![DLSS 5 Control power measurements](https://cdn.mos.cms.futurecdn.net/aR5UAyYqLJNXdZDR4Ef3ES.png) 


That extra performance does come at the expense of significantly higher power draw. The Lightning Z is already pulling a shocking 691 W without DLSS 5, but enable neural rendering, and it jumps to 802 W. The Founders Edition just runs into its 575 W power limit again.

### Bottom Line

At least in our experience with the community-made mod packages available so far, DLSS 5 has a large performance cost, similar to what we saw with ray tracing before the wide availability of DLSS: in the range of 39% to 49%, according to our small sample of results so far.

Official versions of DLSS 5 may perform better, but we won't know for sure until later this week. In any event, our observations of the behavior of the tech as implemented by the community match up with Nvidia's published guidance so far.

We don't expect vastly different or better *performance* from first-party implementations, although a developer's official DLSS 5 recipe could certainly*look better* in a given title than the current free-for-all with sliders that were never meant to be exposed to end users. We'll have to see what happens as developers take the time to tune DLSS 5 for their games as the tech makes its way into more titles through official channels.

Officially, DLSS 5 only supports RTX 50-series graphics cards, and if you're interested in running it with RT or PT, our results show that you're likely going to need to enable the full stack of Nvidia software tech available from Blackwell: DLSS Performance or Ultra Performance to achieve solid baseline frame rates, plus Multi Frame Generation for acceptable output fluidity.

Some have suggested that you don't need to run RT or PT alongside DLSS 5, but that doesn't make any sense at all given our experience thus far. Applying DLSS 5 to purely rasterized input does make it look better than it otherwise would, but it makes the higher-quality input of RT or PT titles look even better still. You definitely don't want to give up those advanced rendering techniques just because DLSS 5 exists.

But those software factors aren't the biggest hurdle that might affect DLSS 5's delivered performance, at least at the extremes. We were surprised to find that the RTX 5090 Founders Edition design is probably holding back the performance of DLSS 5 on that card, even with its 575W TGP. The Founders Edition was consistently at or near its power limit in our tests with neural rendering enabled, which tracks with the demonstrated evidence that, like other image generation models, DLSS 5 is extremely demanding of the Tensor Cores that power its underlying diffusion model.

The exotic MSI RTX 5090 Lightning Z and its 1000W power limit show that when it's stacked on top of ray tracing or path tracing, DLSS 5 can and will happily slurp down hundreds more watts than the Founders Edition—or any other RTX 5090 with a single power connector—is built to provide.

And when you pair that fact with its large performance cost on today's hardware, it's clear that DLSS 5 is a multi-generational technology built to take full advantage of graphics cards that don't exist yet, whether they're RTX 50 Super-series products with higher power limits or future GeForce products built with more advanced Tensor Cores on a newer silicon process node.

Even as it stands, the results we've seen from DLSS 5 so far in both official demos and in its rapid proliferation through community mods suggest that neural rendering techniques like this will mark a new epoch of photorealistic fidelity for real-time graphics and new generations of hardware that are better suited to running demanding AI models like this in real time.

It's an exciting new frontier out there, even if things feel a bit like the Wild West for DLSS 5 right now. Hold on to your hats.

![Jeffrey Kampman](https://cdn.mos.cms.futurecdn.net/8JCjGs5yVZds2YdKmzjUDE.jpg) 

As the Senior Analyst, Graphics at Tom's Hardware, Jeff Kampman covers everything that has to do with graphics cards, gaming performance, and more. From integrated graphics processors to discrete graphics cards to the hyperscale installations powering our AI future, if it's got a GPU in it, Jeff is on it.

- 
Yikes.Reply
 Pure Nvidia garbage IMO.
 Entirely dependent on their entire software stack and therefore forced to buy their overpriced GPU's.
And of course the only GPU's that can actually make effective use of their software stack will be the $2000+ ones.
- 
Good catch. All of the other Nvidia GPUs are more likely to hit their power limits and this seems like a pretty thirsty setting.Reply
 
 That being said, the DLSS5 change in facial image, that is generally an improvement, seems to be very detrimental to facial animation quality in terms of coherent facial expression.
 _hD7WRzfpuk*View: [https://youtu.be/_hD7WRzfpuk*](https://youtu.be/_hD7WRzfpuk*)
 Maybe I'm just hung up by the standard of the original since I enjoyed it, but DLSS5 seems to make these scenes look like the "actors" completely phoned in their roles. With DLSS5 they seem distant, unengaged, like they don't want to be there. Losing the subtle facial details that occur in most expressions would leave you with vapid NPCs and make many compelling stories boring.
 
Perhaps I'm being overly critical and others don't see this, but turning performances vapid and ruining my interest in even playing the game is a dealbreaker for me. Maybe when the official version comes out this issue will be greatly mitigated and we can have both engaging performances and AI enhanced models.
- 
Reply
 It's not "garbage" since many people like the idea. Of course it's dependent on Nvidia tech. They came up with it.....cknobman said:Yikes.
 Pure Nvidia garbage IMO.
 Entirely dependent on their entire software stack and therefore forced to buy their overpriced GPU's.
And of course the only GPU's that can actually make effective use of their software stack will be the $2000+ ones.
- 
I assume this high power consumption is a result of slamming all of the shader and tensor cores at the same time. Where tensor cores would be comparatively lightly used for upscaling.Reply
 
Finally getting off the TSMC 4N node used for both 40 and 50 series will be a breath of fresh air. (Coming 2028.)
- 
Reply
 of photorealistic fidelity
 nobody asked for this.
 Only ones who care are big corpo ceos and maybe a few devs.
 
 Gamers were fine with graphics from Horizon Zero Dawn ages ago (as in 2017...near a decade ago)
 
 Very few games need as "realism" looks as they keep chasing. (basically cinematic "games" that are basically more visual novel than game)
 
The increase in requirement isnt worth it to most people. Also fact that as was with "dlss" and "FG" devs will use them as a crutch to cut cost on dev and brute force performance by making it run awfully unless you run dlss with 6x mfg which only viable on higher tier gpu as you need a high enoguh base fps to make use of mfg w/o it looking (and feeling) like crap.
- 
Replycknobman said:Yikes.
 Pure Nvidia garbage IMO.
 Entirely dependent on their entire software stack and therefore forced to buy their overpriced GPU's.
 And of course the only GPU's that can actually make effective use of their software stack will be the $2000+ ones.
 Yeah, I don't really see this taking off for a couple of reasons:
 No consoles can use it. No next-gen consoles can use it. 90% of the market can't use it.
 
 No sane developer is going to spend their very limited time and budget on assets only a very small fraction of the user base will even be able to turn on, and even a large portion of those who can, won't. They'll simply focus on the assets everyone can use.
 
I expect this to be about as relevant as HairWorks. There will be a handful of games (mostly paid by Nvidia) to implement, and nobody else will bother.
- 
Reply
I dare you to block ads. Give your CPU a break.Greywulffcvg said:Tom's Hardware is the only site that I have run across that has these ads that cover and block the entire article and can't be closed.
