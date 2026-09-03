---
title: Google's latest AI weather model gives you no excuse to forget your umbrella
  | TechCrunch
source_url: https://techcrunch.com/2026/09/03/googles-latest-ai-weather-model-gives-you-no-excuse-to-forget-your-umbrella/
source_site: TechCrunch
source_slug: techcrunch
scraped_at: '2026-09-03T19:17:13Z'
published: '2026-09-03T00:00:00Z'
description: WeatherNext 3 is the latest wave of a sea change in meteorology brought
  out by deep learning techniques. Google says it will start feeding into weather
  information users see in search, Google Maps, and Gemini.
image: https://techcrunch.com/wp-content/uploads/2026/09/2-Figure-How-WeatherNext-3-works.png?resize=1200,675
---

Scientists at Google DeepMind and Google Research released a new artificial intelligence model for weather forecasting today that sees our changing atmosphere more clearly and predicts its behavior more often.

WeatherNext 3 is the latest wave of a sea change in meteorology brought out by deep learning techniques, and Google says it will start feeding into weather information users see in search, Google Maps, and Gemini, as well as being available to users and researchers on Google’s cloud platforms.

“This is going to be the first time that some of the core variables feed and power a lot of the Google products,” Samier Merchant, a Google senior staff engineer, told TechCrunch.

The new model has already proven to be the most accurate among leading contenders tested on Operational WeatherBench, a utility for comparing AI forecasts built by the startup Brightband. It looks at metrics like temperature, windspeed, and humidity.

As well as beating out other deep-learning models built by Google, Microsoft, Nvidia, and the European Center for Medium-Range Weather Forecasting (ECMWF), it also beats traditional forecasts from the U.S. National Weather service and the ECMWF.

![](https://techcrunch.com/wp-content/uploads/2026/09/30-day-weather-champion.png?w=680)

**Image Credits:** Brightband

Most weather forecasts come from government-owned supercomputers laboriously churning through mathematical equations written to describe the physics of weather; while these systems have become remarkably accurate, they are expensive and comparatively slow. After the ECMWF released more than half a century of weather data produced by these systems in 2018, deep learning researchers began training models that could make predictions far more quickly and with comparable accuracy to government tools.

“Weather is chaotic, and so small differences really start to perturb massively…Machine learning targets the problem we are really solving, which is approximate noisy physics from incomplete information and finite compute, and so it learns patterns from a lot of data,” said Ferran Alet, a staff research scientist manager at DeepMind.

Since then, model-makers have pushed on the key weaknesses of AI forecasting models: They tend to forecast over a wider area — 15 to 25 square km — than is truly useful, they’re not always great with rain, and they still depend on the formatted datasets produced by government agencies.

WeatherNext 3 takes on all three challenges. On key variables, researchers told TechCrunch, it can predict down to a resolution of 5 km. Its evaluations on rain are 60% improved over WeatherNext 2, and it can now produce hourly forecasts, instead of the standard prediction every six hours.

![](https://techcrunch.com/wp-content/uploads/2026/09/3-Figure-Surface-temperature-still-image-1.png?w=680)

**Image Credits:** Google

Those improvements are the result of specific choices made by the designers. WeatherNext 3 is a larger model, with 2.4 times more parameters than its predecessor, tailoring the targets for the decoder heads to give more useful answers. While most weather forecasts output as metrics averaged across a 3D grid, DeepMind researchers have already won plaudits by tuning their model to also visualize cyclone paths.

This time around, the designers also trained the model to target its forecasts to specific weather data stations. This is important not only for offering more granular predictions, but also for being able to evaluate its work against specific, ground-truth data.

“The idea, with a lot of AI applications, is to try to run tasks as end-to-end as possible,” Daniel Rothenberg, an atmospheric scientist at Brightband, said. “Adding a capability where this model is now also predicting, say, what Denver’s airport’s weather station is going to measure on an hourly basis, just connects that forecasting task closer to the core.”

The model is able to forecast more frequently because it can ingest weather satellite data collected in real time on an hourly basis. Feeding AI models on raw empirical observations, rather than the analysis produced by weather supercomputers, promises a more accurate forecast, but it is still technically challenging to get models to work with unformatted data.

Google says WeatherNext 3 is the “first” AI model to directly incorporate raw observations for a high-resolution global forecast, but the AI weather startup WindBorne says its model, WeatherMesh 6, has been incorporating raw observations from its fleet of weather balloons and other sources since late 2025. Asked about that, Google pointed out that its forecasts are higher resolution across the globe. Regardless, both models still rely on national weather datasets to perform forecasts, so more work will be required for true direct data assimilation.

While LLMs get the bulk of the attention, the transformer revolution in meteorology has been just as important. European and U.S. weather agencies are already using AI models in their forecast products, and their speed and low cost promise to bring economic impact to poorer regions where the expense of high-quality sensors and supercomputers has put accurate forecasts out of reach.

Bill Gates recently cited AI-powered weather forecasting as a crucial benefit of the technology, with better forecasts improving crop yields in developing countries. Alet, the DeepMind researcher, said that higher-resolution forecasts of wind, rain, and cloud cover will be useful to make renewable energy projects more dependable.

“At the end of the day, I think Google is about providing useful information to the user, and a lot of what users are looking for has to do with the weather in some way or another,” Alet said.
