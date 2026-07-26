---
title: Physicists turn particles in chaotic orbits into liquid computers — but this
  fluid hardware still trails memristor rivals
source_url: https://www.tomshardware.com/tech-industry/physicists-build-a-computer-from-400-particles-orbiting-in-liquid-with-10-times-the-error-of-memristor-rivals
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-07-26T17:12:18Z'
published: '2026-07-26T00:00:00Z'
description: A fluid array of micro‑oscillators can tackle forecasting and stealth
  anomaly detection with surprising finesse.
image: https://cdn.mos.cms.futurecdn.net/Zr9dQ4i4FpNLAqyWzhyAqW-1672-80.jpg
---

![Physicists build a computer from 400 particles orbiting in liquid with 10 times the error of memristor rivals.](https://cdn.mos.cms.futurecdn.net/Zr9dQ4i4FpNLAqyWzhyAqW.jpg) 

Physicists at the Universities of Konstanz and Stuttgart have run chaotic-signal forecasting and anomaly detection on 400 microscopic particles orbiting in a drop of liquid, in work published in Communications AI & Computing. The array predicted a chaotic Mackey-Glass series and picked out anomalies that leave a signal's mean, variance, and short-time autocorrelation untouched, scoring an F1 of 0.90 on that harder task. It also came in roughly 10 times less accurate than memristor-based reservoirs, a gap the paper admits candidly.

Each oscillator is a silica sphere of 3μm radius, capped on one side with 80nm of carbon and suspended in a water-lutidine mixture held at 28°C. A 532nm laser heats the cap and drives the particle toward an assigned target point, but the delay between imaging a particle and repositioning the beam means it overshoots and settles into a small orbit instead. Flow fields in the liquid couple neighboring orbits, and data enters the system as displacements of the target points.

Lattice spacing sets coupling strength, since hydrodynamic forces fall off with distance, and a damping threshold sets how far each particle swings. Both are adjustable while the experiment runs, with a forecasting error that varies by more than a factor of three across that parameter space. Accuracy also held up when the input reached only 20% of the oscillators, and when individual particles stopped responding to the laser or clumped together.

The colloidal array reached a normalized root-mean-squared error of about 0.1 on the one-step Mackey-Glass prediction. Memristor devices now reach 0.01 or better on the same benchmark, the paper notes, adding that those results depend on time-multiplexing and follow nearly a decade of concentrated work.

The authors write that their reservoir doesn't outperform established physical implementations. An arXiv preprint from January, however, framed it differently, arguing that avoiding time-multiplexing set the platform apart from nearly all existing physical reservoirs, photonic, memristive, and spintronic ones included.

Running the reservoir takes a 532nm laser, a two-axis acousto-optical deflector scanning at 100 kHz, real-time microscopy with particle tracking, a temperature-controlled quartz cell, and a conventional computer for the 1,000 Gaussian kernels and ridge regression that produce the output. No energy stats appear anywhere in the paper, despite energy efficiency being the stated motivation, and the authors concede that the laser-driven setup might not be practically applicable and instead point toward simpler actuation schemes, such as electrode-driven colloids.

Clemens Bechinger, professor of soft condensed matter at the University of Konstanz, said in the university's announcement that the dynamics don't need to be fully understood, only to respond reliably, at which point "its physics can be directly harnessed for computation."

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

A separate team synchronized 105,000 nano-oscillators in 45 nanoseconds this month on a platform projected to run at tens of gigahertz.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Luke James](https://cdn.mos.cms.futurecdn.net/C4FAi2KzwaGLUrBqzX5aBM.png)

Luke James is a freelance writer and journalist. Although his background is in legal, he has a personal interest in all things tech, especially hardware and microelectronics, and anything regulatory.
