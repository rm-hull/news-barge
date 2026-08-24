---
title: Why accurate weather forecasting is still so difficult — and why real-time
  data matters
source_url: https://www.techradar.com/pro/why-accurate-weather-forecasting-is-still-so-difficult-and-why-real-time-data-matters
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-24T16:52:05Z'
published: '2026-08-24T00:00:00Z'
description: AI is making forecasts faster
image: https://cdn.mos.cms.futurecdn.net/Y9gz3ntBvZYTntd8XpFxfL-2560-80.jpg
---

![A blue digital cloud containing lots of symbols on a dark blue background](https://cdn.mos.cms.futurecdn.net/Y9gz3ntBvZYTntd8XpFxfL.jpg) 

![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png) 

When you open a forecasting app, you simply select a location, choose an hour and read the answer.

Behind that screen, however, lies one of the hardest prediction problems in science.

The atmosphere is a three-dimensional, constantly changing system.

Founder and CEO of Rainbow.ai.

Before a model can predict what it will do next, it must first answer a surprisingly difficult question: what exactly is the atmosphere doing right now?

## We never see the whole atmosphere

No single instrument provides a complete picture of the weather. Weather radars detect precipitation particles. Satellites observe clouds, moisture and temperatures from space. Ground stations measure conditions at individual locations. Weather balloons and aircraft provide information from different altitudes.

Each source has its own resolution, update frequency, coverage gaps and measurement errors. Building the current state of the atmosphere is therefore like reconstructing traffic across an entire city using cameras that point in different directions, refresh at different times and leave many streets completely invisible.

Meteorologists call the process of combining observations with a previous forecast “data assimilation”. It produces an estimate of the current atmospheric state, known as an analysis, from which the next forecast begins.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

As ECMWF explains, forecast quality depends crucially on the accuracy of this analysis. Even an excellent model will struggle if its starting picture is incomplete, inaccurate or already out of date.

## Why apps lie

One common short-term forecasting technique is optical flow. It analyses consecutive radar images, estimates how precipitation is moving and extrapolates that motion into the future. This can work well when a rain band is moving steadily. The problem is that storms are not static shapes sliding across a map. They form, intensify, weaken, split and merge. A new convective cell can appear where no rain existed 20 minutes earlier.

Imagine a storm approaching a mountain. A simple extrapolation may predict that it will continue moving at the same speed. In reality, the terrain can alter airflow, slow the system and contribute to heavier rain or hail. The challenge is therefore not only predicting where existing precipitation will move. A useful model must also predict how the weather system itself will change.

Another issue is that large-scale models are good at describing weather fronts, pressure systems and atmospheric circulation across countries and continents. But many events that affect people and businesses happen on a much smaller scale. A thunderstorm may affect one part of a city while leaving another almost dry.

A cloud front can sharply reduce output at one solar farm but miss another facility 20 kilometers away. Wind conditions can differ substantially between the ground, a rooftop and the altitude at which a drone operates. Those they can’t predict.

Weather is also highly sensitive to its initial state. Small uncertainties in temperature, humidity or wind can grow as a forecast extends further into the future. This is the real meaning of the “butterfly effect”. It does not mean that one faulty sensor automatically destroys a global forecast. It means that we can never measure the atmosphere perfectly, and uncertainty in its initial state grows over time.

That is why modern forecasting systems increasingly produce ensembles: multiple plausible forecasts rather than one supposedly certain answer. For many decisions, knowing that there is a 30% probability of a severe storm is more useful than receiving a confident prediction that later turns out to be wrong.

## Not to late

Latency is one of the least discussed sources of forecast error. Consider a model that produces an excellent forecast based on atmospheric conditions measured two hours ago. If a thunderstorm formed 20 minutes ago, the forecast may already be operationally useless, regardless of how sophisticated the model is.

The World Meteorological Organization defines nowcasting as detailed local forecasting from the present up to six hours ahead. For real-world applications, however, nowcasting is more than a forecast horizon. It requires a continuous pipeline that collects new observations, checks their quality, synchronizes them in time, runs the model and delivers an updated result within minutes.

At the same time, real-time weather forecasting does not mean literally zero delay. What system does is keeps listening to the atmosphere and updates quickly enough to influence the decision being made.

And that means a lot for some industries. A consumer deciding whether to take an umbrella may tolerate an imperfect hourly forecast. Many operational systems cannot. A delivery drone needs to know whether heavy precipitation, icing or dangerous wind will cross its route before it reaches the area. An airport may need to adjust runway operations as a thunderstorm develops nearby.

A solar operator needs to anticipate a fast-moving cloud front before generation suddenly falls. Logistics and mobility platforms can reroute vehicles before flooding or severe rain disrupts a road network.

The same principle applies to outdoor events, emergency services, agriculture and energy trading. These users do not simply need “tomorrow’s weather”. They need to know what is changing, where it is changing and whether there is still time to act.

## AI makes forecasting faster, but speed alone is not enough

AI weather models can generate forecasts much faster and with less computing power than many traditional numerical models. Some already outperform physics-based systems on particular variables and forecast horizons. But AI does not eliminate the observation problem.

Most global AI forecasting models still begin with an atmospheric analysis produced by traditional numerical weather prediction infrastructure. If that analysis is several hours old, fast inference cannot make the initial state current again.

AI models can also underestimate the intensity of rare events because extreme examples are underrepresented in their training data and because some training methods favor smoother, more statistically likely outcomes. Recent research has found that leading AI models can produce larger errors than physics-based systems when forecasting record-breaking heat, cold and wind events.

This is why the future is unlikely to be a simple contest between AI and physics. ECMWF already runs its operational AI forecasting system alongside its traditional physics-based model.

The strongest architecture will combine global models, high-frequency local observations, AI-based nowcasting, physical constraints and probabilistic estimates of uncertainty.

*This article was produced as part of**TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:**[https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
