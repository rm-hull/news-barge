---
title: DeepMind AI gives an extra day of warning ahead of deadly cyclones | New Scientist
source_url: https://www.newscientist.com/article/2583547-deepmind-ai-gives-an-extra-day-of-warning-ahead-of-deadly-cyclones/?utm_campaign=RSS|NSNS&utm_content=home&utm_medium=RSS&utm_source=NSNS
source_site: New Scientist
source_slug: new-scientist
scraped_at: '2026-08-07T00:56:08Z'
published: '2026-08-06T00:00:00Z'
description: An AI model from DeepMind can predict cyclones three days ahead with
  a level of accuracy that previous models can only hit a day later
image: https://www.newscientist.com/wp-content/uploads/2026/08/SEI_307533951.jpg
---

![](https://www.newscientist.com/wp-content/uploads/2026/08/SEI_307533951.jpg?w=840)

DeepMind has developed an AI model that can predict deadly cyclones one day further out than existing methods, potentially saving lives by allowing more accurate and timely decisions about evacuations.

Many existing weather forecasts are based on physics simulations run on powerful supercomputers that model and extrapolate weather patterns as accurately as possible. AI models may represent a faster and less costly method.

WeatherNext is able to generate a 15-day forecast in less than a minute on one of Google’s custom Tensor Processing Unit chips. Meanwhile, physics-based models can consume days of high-powered computer time.

Advertisement

The new model works on a simulation of the atmosphere where the smallest cell is 28 square kilometres, making it a hundred times less granular than traditional models. It was trained on nearly 20 terabytes of global atmospheric data, as well as data on 5000 historical storms, which Ferran Alet at DeepMind says was crucial to improving WeatherNext’s accuracy at predicting the behaviour of new cyclones.

The DeepMind team compared its WeatherNext AI model with Google’s GenCast model, the European Centre for Medium-Range Weather Forecasts’s ENS model and the National Oceanic and Atmospheric Administration’s Hurricane Analysis and Forecast System. It found that WeatherNext was able to produce accurate predictions three days out that could only be matched by current models two days out, in terms of maximum wind speed and the distance error between a cyclone’s predicted location and actual eventual location.

“The longer time goes [on], the worse you’re going to do, because weather is chaotic. So the question is, how much can we push this chaos barrier? How much can we see into the future?” says Alet. Because of the time taken to publish the work in an academic journal, he says that things have moved on since, and that DeepMind is actively working on building even faster and more accurate models.

The firm has a long history of attempting to improve weather forecasting. In 2021, it developed an extremely short-term and local model that could predict whether it would rain or not in the next 90 minutes more accurately than existing models. In 2023, it released a model that could provide accurate 10-day weather forecasts, and in 2024, it launched a tool that dramatically slashed the time and energy needed to make forecasts.

Hannah Cloke at the University of Reading, UK, who wasn’t involved in the research, says she has never experienced a faster and more dramatic shake-up in meteorology than the effect of AI in the past couple of years.

“This is one of the most exciting fields to work in at the moment, and one of the reasons is the rise in machine-learning forecasting and the absolute speed and power with which we’re moving forward in this field,” she says. “You go on holiday for a week… and find out something else has happened.”

Cloke says that advances are far outpacing the speed of academic journals, meaning that the cutting edge is actually 18 months ahead of what we read in papers like this one.

Global forecasting agencies have tested AI models alongside their traditional physics models in recent years, but there is increasing consensus that AI models are faster, cheaper and, in many cases, more effective than physics-based methods, she says. However, she stresses it is still important to maintain meteorological expertise.

“A lot of the new people that I encounter working in this field have come through data science and they don’t necessarily have the meteorological background that you do need in order to to understand whether the models are producing something sensible or not,” says Cloke. “So there is a real tension there between the new techniques that are really exciting and making sure that we are able to take the correct decisions in terms of deploying these models.”

But despite their rapid success in meteorology, not everyone is convinced that AI models are the future of forecasting – or, at least, they need to be tested far more rigorously before we ditch traditional models.

Tim Palmer at the University of Oxford is concerned that models will struggle to predict truly anomalous, one-off events because, by their nature, they will have no analogue in the training data. For that reason, he has advocated for a new kind of test that removes previous such events from training data, then assesses AI models on whether or not they can successfully predict them. He believes that this ability will become crucial as climate change makes weather patterns increasingly chaotic.

“We don’t test for that,” he says. “Relying on an AI which has been trained on 40 or 50 years of past data could lead us up the garden path.”

Another concern for Palmer is that weather models and climate change models share as much as 90 per cent of their code. Giving up numerical, physics-based models in weather forecasting would be detrimental to climate modellers, forcing them to work without the knowledge and data gleaned from weather forecasting, or to replicate all the work that used to take place in weather forecasting in order to continue their work as before.

“The code is virtually identical,” says Palmer. “If we start to lose our capability of doing weather forecasting with physics-based models, the climate predictions will suffer.”
