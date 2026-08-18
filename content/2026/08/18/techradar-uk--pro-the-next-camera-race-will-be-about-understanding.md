---
title: The next camera race will be about understanding
source_url: https://www.techradar.com/pro/the-next-camera-race-will-be-about-understanding
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-18T19:35:56Z'
published: '2026-08-18T00:00:00Z'
description: How AI inference is reshaping what camera sensors are for
image: https://cdn.mos.cms.futurecdn.net/wZAaq2s2qH4tHBJTEBNZXM-2560-80.jpg
---

![An abstract pattern of blue lines and orange-yellow dots on a dark blue background, to represent a digital environment](https://cdn.mos.cms.futurecdn.net/wZAaq2s2qH4tHBJTEBNZXM.jpg) 

![](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9-200-100.png) 

The demo that convinced me happened at an art exhibition I'd built myself.

We couldn't afford a team of docents, so I put together a side project to stand in for one. There was no prompt box and nothing to type. You pointed your phone at something and it told you what you were looking at. Then the show closed, and people kept using it anyway.

They pointed it at buildings, flowers, their kids' toys, posters on the street, none of which had anything to do with the exhibition.

Without anyone asking them to, they had decided a camera should be able to explain the world back to them.

Founder and CEO of Chance AI.

That expectation is now the industry's to deliver on, and it arrives just as AI shifts from a training problem to an inference one, with more of the real work happening on-device while someone points a phone at an uncooperative real world.

A model needs different things from a frame than your eye does: edges to lock onto, and structure it can recover when the shot is full of glare or blur. The color and contrast that make a photo look good are, to the model, mostly in the way.

The sensor you'd want for a human viewer and the one you'd want for a model call for different designs.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The sensor has become a perception problem, and the people building real-time vision systems now care about it the way photographers once did.

## Where the sensor came from

Eric Fossum's CMOS active-pixel sensor, developed in the early 1990s, is why a capable camera now sits in nearly every pocket.

His later work heads somewhere else entirely: the Quanta Image Sensor, which counts individual photons. That arc previews what is happening to AI now: it runs from capturing a frame a person will like toward capturing the cleanest signal for a machine to reason over.

The sensor is turning into an instrument of perception, and photography is becoming only one of the things it is for.

## Why inference changes the job

Inference is what makes the problem urgent. Back when AI was mostly about training, the camera's role was indirect: it produced data to be labeled and learned from later, at leisure. Inference is not leisurely. It happens live, on a device short on power and already running warm.

When a system has to recognize something while you're still pointing at it and answer before the moment passes, the weakest link is whatever reaches the model, and it sets the ceiling on everything the product can do.

Part of the industry is still betting on the wrong thing. The assumption is that a big enough model will clean up whatever the camera hands it. I've watched this hold up product roadmaps for two years running, and I don't think it survives contact with physics.

No amount of model size recovers detail that motion blur or glare already destroyed, or that a beauty-first pipeline discarded before the model ever saw the frame. The bottleneck is moving upstream, toward the sensor and what sits between it and the model.

## What the hardware is already doing

Some sensors now do part of the processing on-chip, so the first computations happen before data leaves the pixel array. Event-based sensors, sometimes called neuromorphic, register only the parts of a scene that change, which suits real-time perception far better than streaming whole frames. Global shutters help too, by cutting the motion artifacts that wreck machine reading.

Even high dynamic range, long tuned to make skies dramatic, is being retuned around what a model can read cleanly in high contrast. Different as these are, they point the same way, toward a version of the world a model can work with.

## From recognition to reasoning

The obvious thing to build is visual search: you point at something and get a label back. Point your phone at a menu, though, and what you want is help deciding what to eat; point it at a poster, and the useful move might be saving the event to your calendar. Recognizing the object is only the starting condition. The product lives in knowing what should happen next. That move is where the sensor becomes the first link in a longer chain of interpretation, beyond simple capture.

I never meant to build a camera product at all; it began as a cheap way to avoid hiring docents for one exhibition. But that small project taught me the instinct is already out there. The next camera race will run across the entire stack: the sensor, the image pipeline, the edge compute, the model orchestration, and what the system does with an answer.

Device makers have spent years perfecting image quality, and they will have to take inference quality just as seriously. And whoever writes the software can't treat capture as someone else's problem: how a signal is grabbed and routed shapes the result long before a user sees it. The old boundary between hardware and software matters less the further you push into real-time perception.

Startups still have room here. Their advantage is speed of definition: framing a problem before the larger players finish arguing about it. Generic model capability, on its own, is getting harder to defend. The open question is what happens once a single system can see, reason about what's in front of it, and act on the same event, and who gets there first with a product that holds together.

## Human eyes vs machine minds

My bet is that the next few years will sort companies into two camps: the ones optimizing for human eyes and the ones optimizing for what a machine has to read. Inside a flagship phone, those goals still overlap enough to ignore the difference.

As a strategy, they are already diverging. The more durable position belongs to whoever can turn the messy real world into the cleanest signal for a machine to reason over.

And that starts at the sensor.

*This article was produced as part of**TechRadar Pro Perspectives**, our channel to feature the best and brightest minds in the technology industry today.*

*The views expressed here are those of the author and are not necessarily those of TechRadarPro or Future plc. If you are interested in contributing find out more here:**[https://www.techradar.com/pro/perspectives-how-to-submit*](https://www.techradar.com/pro/perspectives-how-to-submit*)

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
