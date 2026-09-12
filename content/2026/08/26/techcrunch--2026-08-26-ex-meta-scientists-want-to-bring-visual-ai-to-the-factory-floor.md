---
title: Ex-Meta scientists want to bring visual AI to the factory floor | TechCrunch
source_url: https://techcrunch.com/2026/08/26/ex-meta-scientists-want-to-bring-visual-ai-to-the-factory-floor/
source_site: TechCrunch
source_slug: techcrunch
scraped_at: '2026-08-26T16:56:24Z'
published: '2026-08-26T00:00:00Z'
description: Perceptron offers an AI model that it says can help machines navigate
  the world while also providing in-depth visual intelligence.
image: https://techcrunch.com/wp-content/uploads/2026/07/Perceptron-Team-Photo.jpg?resize=1200,800
---

AI is transforming everything around us but, thus far, it has largely remained contained to the digital realm. Increasingly, however, startups are looking to take it into the real world.

Perceptron, a startup started by two former Meta research scientists, is one such company. Founded in November 2024, the firm develops frontier vision models that aim to help machines more competently interact with their physical environments.

This week, the company launched its latest model, Isaac 0.5, which its creators say is designed to provide machines with the ability to “perceive, reason and act” in industrial settings. Specifically, the software is capable of helping vision-guided robots navigate complex environments like warehouses or factory floors. It also helps companies extract visual intelligence from videos recorded by those bots.

Isaac 0.5 is also being released as an open-weight model, so its parameters and training materials can be inspected by anyone.

The startup was co-founded by Armen Aghajanyan and Akshat Shrivastava, who previously worked for Meta’s Fundamental AI Research (FAIR), the tech giant’s AI research division. The duo see their software as the future of industrial automated deployment.

“Physical AI today forces a false choice: generalist foundation models that need multiple dedicated cloud GPUs for every instance, or narrow models that handle perception or control, but never both,” the company says.

Aghajanyan and Shrivastava say their tool is unlike existing models in the space because it is general-purpose, meaning that it’s not built for one specific, repetitive task. Instead, they say, the model is designed to be flexible depending on the particular environment (or situation) it is in.

In an interview, Shrivastava asked me to consider what goes into a simple physical process like organizing boxes: “Imagine there’s a robot being deployed to sort packages right now. What are the tasks it would need to do?”

Such a relatively simple task indeed consists of many steps. A robot would first have to read the label on the package, do some spatial analysis to understand where the boxes are, and decide which one to pick up. If it’s picking up a series of boxes, it would have to plan which boxes to pick up and in which order.

Perceptron’s software is designed to help robots find their way through each step of the process. To be clear, the industry already has software that can help machines do most of those tasks, but there are few programs that are designed to do it flexibly.

Where does the data for this algorithmic alchemy come from?

Models like Isaac 0.5 learn operational skills by ingesting gargantuan amounts of video training data. Perceptron says its new model was fed on a million hours of what is known as general video to teach its algorithm to identify particular settings, visuals, and scenarios. The company also relied heavily on what is known as ego video — video captured, typically through a GoPro or a wearable camera, from the perspective of a person completing a physical task — as well as UMI video, which are similarly used to teach AI systems movements by recording repetitive human actions.

While Perceptron isn’t disclosing the sources of its training data, Shrivastava said that the company had “internally built petabyte-scale datasets that span across modalities, whether it’s images, text, video, etc. all the way through robotic trajectories.”

The utility of a software that can help robots operate competently in warehouses is obviously vast, and Perceptron thinks it’s well-positioned to lead that wave of automation. The startup is ready to market its software to a variety of vendors, and thus potentially see its intelligence layer integrated into a broad array of industries.

Those industries include manufacturing, logistics and warehousing, security, mobility, as well as media and entertainment.

“Nothing like this really exists out there,” said Aghajanyan. “We’re really excited about it.”

*An earlier version of this story incorrectly reported recent funding round. It has been updated to correct this information.*
