---
title: Occam’s razor has lost its edge. Can we sharpen our search for truth?
source_url: https://www.newscientist.com/article/2531862-occams-razor-has-lost-its-edge-can-we-sharpen-our-search-for-truth/?utm_campaign=RSS%7CNSNS&utm_source=NSNS&utm_medium=RSS&utm_content=home
source_site: New Scientist
source_slug: new-scientist
scraped_at: '2026-07-08T17:49:42Z'
published: '2026-07-08T00:00:00Z'
description: Seeking out the simplest, most elegant explanations has served scientists
  well for centuries, but cognitive scientist Marina Dubova’s experiments are revealing
  better ways to uncover reality
image: https://images.newscientist.com/wp-content/uploads/2026/06/25195753/SEI_302860476.jpg
---

![New Scientist. Science news and long reads from expert journalists, covering developments in science, technology, health and the environment on the website and the magazine.](https://images.newscientist.com/wp-content/uploads/2026/06/25195807/SEI_302818460.jpg)

KLAWE RZECZY

Limited by the knowledge of his time, the ancient Greek astronomer Ptolemy imagined that the planets and sun of our solar system orbited Earth. Every new observation that pushed against this image required a slight tweak to that theory, until centuries later Nicolaus Copernicus’s reimagining toppled it once and for all. A more elegant explanation proposed that all the planets orbited the sun, kicking off a scientific revolution that changed our understanding of the entire universe.

Simpler explanations have supplanted prevailing knowledge time and again – special relativity won out over the luminiferous aether, continental drift more easily explained similar fossils on separate continents than ocean-spanning land bridges that sank eons ago. This is the spirit of Occam’s razor, the principle attributed to the 14th-century friar William of Ockham, which tells us to opt for the simplest explanation that fits the facts.


But what if scientific progress doesn’t always work that way? What if it’s better to zoom out and start from complexity instead of simplicity? Only then might we begin to magnify the hidden structures that were previously invisible.

Cognitive scientist and philosopher Marina Dubova at the Santa Fe Institute in New Mexico, argues that Occam’s razor is just one of several rules of thumb obstructing our efforts to paint a true picture of reality. By building computer simulations and putting researchers in “micro-world” experiments, Dubova turns the principles of psychology and cognition on scientists themselves. She’s finding that some of the most cherished assumptions about the best way to search for truth are on shaky ground.

Looking to a future in which large parts of science may be automated, these lessons could be decisive for building “AI scientists”. *New Scientist* asked Dubova about the risks of embedding old ways of thinking into the future of science, how we can learn better and faster by maximising our contact with reality, and what this tells us, on a fundamental level, about what science actually is.

**Thomas Lewton: What is the principle of Occam’s razor and how do scientists use it?**

Marina Dubova: Occam’s razor is the preference for simpler explanations. Students in many scientific fields, myself included, are taught that it’s a good idea, no matter what you’re studying, to start with the simplest possible theory. If you see in the data something that is really not accounted for, then you add one more variable or one more mechanism, but you always start in the simplest possible way. Scientists apply that in different ways: sometimes it is a preference for explanations that make minimal assumptions, or a preference for theories that presuppose fewer causes or mechanisms; sometimes it’s a preference for explanations that are less flexible, so they make very specific predictions.

**Is this simplistic approach limited just to science, or do we all do it?**

We have evidence that if you ask people to explain different events, they tend to come up with explanations that are simple and broad. Psychologist Tania Lombrozo at Princeton University, among others, has found that we often prefer explanations that both appeal to fewer causes or mechanisms and that can account for the most data. For example, asked to diagnose an alien who has two symptoms, study participants favoured an explanation that the alien has a single disease that accounts for both symptoms over two diseases that cause one symptom each, even when the two-disease explanation is presented as more probable.

**Is there empirical evidence on whether Occam’s razor leads to scientific progress?**

We tested these ideas using a computational model in which AI agents build representations of some ground truth based on a limited set of data. We create some agents that want to come up with a theory for the ground truth with the fewest variables. Then, on the other end of the spectrum, we have agents designed to create explanations that are far more complex than the phenomena they’re studying. Imagine you’ve got a system with three important variables – these latter agents would create explanations that would have 1000 variables. That’s a very interesting reverse kind of preference that we don’t often see, at least in science. If we applied this to the alien disease example, the complexity-preferring agent wouldn’t be attributing the symptoms to one or two diseases. It would instead build an explanation that draws on a thousand factors, like the alien patient’s age, maternal and paternal genetic risk scores, the temperature and air quality on their home planet and so on.

Surprisingly, if we look at how well these representations end up helping the agents make predictions about new data coming from the same ground truth, sometimes the agents that had the explicit complexity preference would be able to do the task just as well as the parsimony-preferring ones, or sometimes even better. These insights are very surprising and force us to reconsider a lot of assumptions that we have about how we, as scientists, learn about the world.

**You said assumptions, plural. So it isn’t just Occam’s razor that might be leading us astray?**

Another common rule of thumb is the idea that an experiment must be motivated by the theories that we already have. Whether you’re studying life on other planets or a new type of phenomenon in human memory, a common requirement is to first formulate a theory to do a theory-guided experiment. For example, the famous eclipse expeditions led by Arthur Stanley Eddington in 1919 were organised specifically to test general relativity’s prediction that the sun’s gravity bends starlight. The experiment let scientists decide between two competing accounts: Albert Einstein’s general relativity predicted a larger deflection, while Newtonian assumptions predicted a smaller one. The idea is that we should not conduct experiments in vain, everything must have reasoning behind it.

![](https://images.newscientist.com/wp-content/uploads/2026/06/25195758/SEI_302861293.jpg)

A solar eclipse image taken in 1919 confirmed Albert Einstein’s theory of general relativity. Stars near the sun (marked here by horizontal lines) appeared to be slightly shifted because their light was curved by its gravitational field

ROYAL ASTRONOMICAL SOCIETY/SCIENCE PHOTO LIBRARY

**Science is often called the pursuit of reason. Is that the wrong approach?**

Using similar computational models, we make agents whose strategy is to try and falsify their theories or resolve disagreements with their colleagues through carefully chosen experiments. Another strategy is to conduct experiments that could prove your theory correct – a kind of confirmation bias. Then we had two more exploratory strategies: one is choosing experiments randomly and the other is choosing novel experiments that no one has done before.

**Who came up with the best theories?**

The agents using the exploratory strategies, both the novelty-driven and random experimentation, developed the best theories of the underlying ground truth. We were so surprised by this that we ran four more experiments with the model to try to falsify the result.

**And you’ve also observed these behaviours in actual scientists?**

Yes. We had neuroscientists try to learn about a toy brain segment by using brain imaging and lesioning. Their goal was to learn what the underlying causal structure is. Neuroscientists were quite successful at this task, but they would sometimes fail to revise their prior beliefs. For example, the toy brain sometimes violated the “one-to-one” assumption that each brain region is responsible for a single ability, like having separate areas for face processing or language. We’d set it up so that one region of the toy brain controlled several abilities, yet some neuroscientists kept insisting there must be subtle differences and that there were really two slightly different regions, each responsible for one behaviour. Just as the less exploratory agents had a harder time revising their theories, real scientists let their hypotheses steer which experiments they run and how they interpret their results.

**What should scientists take from your experiments?**

In science, our institutions are not set up to promote exploration – it has to be very deliberate. We need to be aware that our theories and concepts are influencing all our decisions in a way that may prevent us from getting closer to understanding reality in a new way. For example, the theory of general relativity, the periodic table in chemistry or the taxonomy of mental conditions in psychiatry, these are things that affect how we as scientists engage with reality and can help us make further progress, but they can also limit our exploration.


**But science, in all its forms, does gradually go through revolutions in which concepts and theories are overturned. Is that not enough?**

When a scientific revolution happens, there is a dramatic change in what we do as scientists and how we perceive the world. But does it have to take decades or centuries to overturn these ideas? If we explore with fewer guard rails, we could potentially speed up discovery.

**Are there examples of how simple explanations have led us down the wrong path?**

Take neuroscience. The field has increasingly moved toward seeing the brain as a distributed network in which many regions interact, and where a single region often participates in several functions rather than owning just one. There was an analogous assumption in genetics: one gene is responsible for a particular trait. That holds for some special single-gene cases, but the general idea has also been actively revised. Current understanding is that most traits emerge from many genes interacting across the genome, often shaped by the environment as well.

**You could say those simpler, earlier ideas were a practical way to at least start grappling with what are highly complicated phenomena.**

As humans, we are cognitively limited. We cannot conceive of all possible 1000-dimensional, 1000-variable theories that could account for everything we are studying. Parsimony, in some ways, may have been a necessity. Artificial intelligence can help us start exploring higher-dimensional, more complex explanations.

You see this happening in a field called statistical learning, the mathematical study of how systems learn from data. One recent finding is called the “double descent of generalisation”. We previously thought that the larger a model was, the worse it might perform. The intuition here was that you had to compress the environment a model is interacting with: why make the model bother with memorising all the details if nothing in the environment is going to happen in the same exact way again? But it turns out that as a model increases in complexity, its error rate will dip, then peak, then dip even further. These systems are better at generalising – coming up with rules to follow in new scenarios, or predicting how things will play out with unseen data – when they form representations that are more complex than the actual data. They’re memorising every single detail and transforming these details in many ways to generalise successfully.

**Does this have implications for how we try to build “AI scientists”?**

I think there’s not enough discussion over what aspects of the scientific method we want to keep and which we want to reconsider. Were we just doing the best job we could do, given our cognitive limitations, rather than it being the best scientific method? That’s essential to understand as we move forward with automating some parts of the scientific process. Otherwise, I’m worried we might replicate some of our biases and blind spots, but at a massive scale.

**What do your experiments suggest about what science is deep down?**

The goal of science is to grasp for some reality, to learn something about the world. But there are so many angles from which you can explore the same phenomenon, you have to poke at it from different perspectives. Hasok Chang, a philosopher at the University of Cambridge, describes it as maximising our contact with reality. We’re so used to visual metaphors of science, such as something that is mirroring nature. But what we’re really doing is exploring reality in a tactile-like way – something that philosopher Mazviita Chirimuuta at the University of Edinburgh, UK, calls haptic realism. Often when we poke something, it deforms, or else we don’t have access to its entirety. Science is about interacting with the world in many ways to learn as much as we can.


Topics:
