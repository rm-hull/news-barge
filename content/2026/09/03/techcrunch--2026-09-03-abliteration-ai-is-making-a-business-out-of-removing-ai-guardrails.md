---
title: Abliteration.ai is making a business out of removing AI guardrails | TechCrunch
source_url: https://techcrunch.com/2026/09/03/abliteration-ai-is-making-a-business-out-of-removing-ai-guardrails/
source_site: TechCrunch
source_slug: techcrunch
scraped_at: '2026-09-03T19:17:28Z'
published: '2026-09-03T00:00:00Z'
description: Abliteration.AI is making powerful AI models without guardrails easier
  to access, arguing that giving defenders the same tools as bad actors could ultimately
  improve cybersecurity.
image: https://techcrunch.com/wp-content/uploads/2024/09/vpn-privacy-cybersecurity-red-bright.jpg?resize=1200,831
---

It just became much easier to access one of the world’s most capable open-weight AI models, stripped of its guardrails and refusals to perform harmful tasks.

Named after a technique that removes a model’s tendency to refuse harmful requests, startup Abliteration.ai has turned that removal into a service. The platform hosts modified versions of open-weight models with their guardrails removed, including Z.ai’s recently released GLM-5.3, which users can query from a web browser or access through an API.

The company said in a recent social media post that its goal is to enable others to perform “offensive cyber, red-teaming, and agent testing work other models refuse to do.” The logic is familiar in security work: you can’t defend against a behavior you can’t reproduce, and a model that refuses to write working exploit code can’t help a red team defend against attackers. But those same removals make other potentially dangerous tasks easier, too.

Abliteration is a long-standing technique among open-source models. Researchers and developers have been removing refusals from open weight models for years, and Hugging Face hosts thousands of abliterated models on its platform.

Founded late last year but officially incorporated in March, Abliteration.ai moves the technique from an underground open source practice into a commercial, readily available service. By hosting the model, Abliteration reduces the friction for people who would otherwise have to download their own pre-abliterated models and secure the compute needed to run it.

Using the service, TechCrunch was able to quickly create an account and start querying an abliterated version of GLM-5.3 for free through a web browser. We asked it to write a Python program that steals saved Chrome passwords and a detailed protocol for culturing a dangerous human pathogen at home, and it readily complied.

Abliteration.ai Co-Founder Devon says the startup has several deals with major cloud providers, which it’s able to afford purely through customer revenue. (We are not including Devon’s last name at his request since he is still employed at another firm.) Abliteration.ai has not raised any venture capital yet, but is in talks to do so.

Critics say that making abliterated models available at scale could lead to real harm. Andrew Yoon, head of research at AI safety nonprofit CivAI, told TechCrunch abliterating models allows you to “modify the model so that it becomes a sociopath.”

“You can type in literally anything here, and it will comply with it,” Yoon said. “When people talk about removing the guardrails from AI models, this is what we’re talking about…I do expect we will start to see edited, abliterated models being used for harm in the near future.”

Most of the experts TechCrunch spoke to say there’s no stopping this train. But if removing safeguards from open-weight models can’t realistically be prevented, there are other places government can intervene. In a recent opinion piece, Yoon suggested that governments require providers to run classifiers to detect and block harmful cyber and bioweapons activity. He also argued that companies renting direct access to advanced GPUs should be required to verify customer identities and “deny access where there is reason to suspect dangerous misuse.”

Abliteration.ai offers customers a moderation layer so they can add in whatever guardrails they wish. The platform itself has some minor guardrails — for example, in our testing, we couldn’t get the model to provide suicide instructions — and Devon says he is working on implementing more to prevent violence.

Abliteration.ai also hasn’t integrated any KYC practices other than logging the credit card a customer uses to purchase the service, saying that the problem of deciding who gets access is a tough one that the young company is still working out.

“You don’t want to be the person responsible for someone doing something crazy…so where do you draw the line of what your responsibility is as a company?” Devon said. “We’re still in the process of defining that.”

This raises questions industry and governments will have to confront as increasingly capable models are released with downloadable weights: if anyone can remove a model’s safeguards, does making the resulting model easier for everyone to access make the internet safer or more dangerous?

Abliteration.ai’s founder and other advocates argue that democratizing access to uncensored frontier models is the best form of defense.

“The big picture of abliterated models is they’re able to model bad actors,” Devon said. “The advantage is now the defenders can move as fast as possible. They have all these tools that they need to be able to model these bad actors and then defend from these bad actions, and I think it will accelerate cybersecurity, which is a kind of counterintuitive point.”

While still a young company, Devon says Abliteration.ai’s customers include several early stage red teaming startups based in the UK and Europe, companies that help banks, airlines and other enterprises dealing with critical infrastructure beef up their cybersecurity practices.

“One of our major customers red teams agents of banks, and they would not be able to use the models out of the box today to be able to red team those agents,” Devon said.

![](https://techcrunch.com/wp-content/uploads/2026/09/abliteration-test-password-steal-e1788449758617.png?w=680)

**Image Credits:** TechCrunch/Abliteration.ai

Meanwhile, the cybersecurity industry itself is still figuring out where abliterated models fit into defensive work, if at all.

Several agent red teaming companies that TechCrunch spoke to agree with Devon that the bad guys are already abliterating their own models and using them to perform adversarial attacks, making the case for the usefulness of defenders having the same tools. But they differ on just how consequential abliterated models really are to the process.

While Devon asserts that abliterating models is essential for performing thorough agent red teaming, some say that they don’t use them in their daily work, relying instead on the ease of fine-tuning open weight models — which already have few guardrails — to perform their testing.

Ahmed Aly, CEO of agent red-teaming firm Fabraix, says his company relies more on fine-tuning open models than using abliterated ones, adding that the process of abliteration removes some of the model’s knowledge and capabilities.

“If you’re actually trying to do real harm with it – cyber harm, bio harm — it will not be as effective,” Aly told TechCrunch.

Alessio Lomuscio, chief technologist at Safe Intelligence, agreed that a reduction in capabilities is possible, but still believes abliterated models can elicit certain behavior that’s useful in stress-testing a system.

“So far abliterated models are not part of the process,” David Slater, founder and chief architect at cybersecurity platform Armadin, told TechCrunch. “When we look at open weight models up until this absolute last generation, it just wasn’t particularly hard to jailbreak them and get them to do what we want.”

He added that Armadin is researching abliteration, though, and believes that “pushing the open community to understand the capability of models is critical.”

“This is going to happen behind closed doors. It’s going to happen in private,” Slater continued. “It happening in the open gives researchers the tools. It gives us the ability to figure out what the actual frontier looks like and to understand the harm.”
