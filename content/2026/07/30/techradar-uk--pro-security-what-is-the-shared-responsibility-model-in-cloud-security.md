---
title: What is the Shared Responsibility Model in cloud security?
source_url: https://www.techradar.com/pro/security/what-is-the-shared-responsibility-model-in-cloud-security
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-30T21:20:22Z'
published: '2026-07-30T00:00:00Z'
description: Figuring out where your cloud provider's security ends and yours begins
image: https://cdn.mos.cms.futurecdn.net/7Gf69TkDxGzZPDGHpU4cN7-2560-80.jpg
---

![An abstract image of cloud storage.](https://cdn.mos.cms.futurecdn.net/7Gf69TkDxGzZPDGHpU4cN7.jpg) 

Imagine you’re a company. You’ve got sensitive data you need kept safe, and you’ve got a cloud service provider that’s protecting it. But do you know how far that protection goes, and at what point it’s your turn to take over?

The sheer number of data breaches due to human error, specifically database misconfiguration, suggests that many don’t know that they, not the provider, are responsible for securing all the data properly (or are unsure how to do it).

In this article, we’ll look into the shared responsibility model: what it is, why it’s relevant, its benefits, its limits, and what happens when companies disregard it.

## What is the Shared Responsibility Model?

The Shared Responsibility Model is a security and compliance framework that defines the divided responsibilities of cloud service providers (CSPs) and their customers. This means that each has their own tasks in maintaining security.

In short, the provider is responsible for securing the underlying cloud infrastructure, but the customer needs to secure their own data, configurations, and any applications they may have.

In more detail, the provider takes care of:

- Physical security: Secures physical data centers and hardware.
- Host infrastructure: Secures and maintains networking, servers, and storage.
- Data protection: Provides encryption for data in transit and at rest, but does not secure customers’ data.
- Applications: Potentially provides app hosting platforms or tools, but does not secure customers’ apps.

On the other hand, the customer secures everything they own:

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

- Data protection: Secures, classifies, backs up, and encrypts its own stored information properly.
- Information access: Manages secure access to sensitive data, user accounts, permissions, and multi-factor authentication.
- Configuration: Sets up firewalls and network settings properly.
- Applications: Develops, maintains, and configures apps and their secure application codes.

 ![Shared responsibility model overview](https://cdn.mos.cms.futurecdn.net/M5sCHDstYwCUcBAFb7giYM.png) 


## The first step is defining it - now meet your provider

It would make things a lot easier if these rules and divisions were standardized, so when you understand them for one provider, you understand them for all. Alas, that’s not the case.

The above guidelines are general because the model somewhat differs between providers, and this lack of uniformity contributes to security gaps between the provider and the customer.

That said, make sure you understand your full responsibilities with each provider you use. For example, AWS says “customers should carefully consider the services they choose as their responsibilities vary depending on the services used, the integration of those services into their IT environment, and applicable laws and regulations.”

AWS makes a clear distinction between these responsibilities, saying that the customer is in full charge of managing the guest operating system, including updates and security patches. They must also configure the AWS-provided security group firewall and manage any other application software they own.

 ![AWS customer data](https://cdn.mos.cms.futurecdn.net/tPsMxPbrGegg9MNcs33tVC.jpg) 


Microsoft further explains that responsibilities vary depending on where the workload is hosted: on software as a service (SaaS), platform as a service (PaaS), infrastructure as a service (IaaS), or in an on-premises datacenter.

However, “for all cloud deployment types, you own your data and identities,” it says. “You're responsible for protecting the security of your data and identities, on-premises resources, and the cloud components you control.”

 ![Microsoft cloud responsibilities](https://cdn.mos.cms.futurecdn.net/rsMGQpmHybMbcLWpgGbcJ7.png) 


## Google Cloud’s ‘Shared Faith’

Google Cloud went with yet a third approach, differentiating between the shared model of other providers and its own “shared faith”:

Given that understanding the shared responsibility model properly in order to secure one’s data can be challenging, “Google believes that the shared responsibility model stops short of helping cloud customers achieve better security outcomes,” it writes. “Instead of shared responsibility, we believe in shared fate.”

The explanation of this approach focuses on “partnership” between the provider and the customer for increased security, as well as offering support and resources to help organizations secure data on their end.

The provider states that “a key component of shared fate is the resources that we provide to help you get started, in a secure configuration in Google Cloud. Starting with a secure configuration helps reduce the issue of misconfigurations, which is the root cause of most security breaches.”

 ![Shared responsibility vs shared faith](https://cdn.mos.cms.futurecdn.net/QpuZ8gxqZA6zHNUN6qKGsH.png) 


## Why does shared responsibility matter, and what happens when companies disregard it?

The shared responsibility model is meant to provide a division of security, compliance, and ethical duties. The number one goal is to cover all bases to ensure all security controls are managed, thus preventing security gaps and potential breaches.

Should a breach happen, this shared control system is theoretically designed to help contain it faster and more efficiently. I say “theoretically” because security gaps do exist, as we’ll see later.

Additionally, the model is designed to ensure that neither the provider nor the client duplicates security steps unnecessarily, wasting their time and effort.

Finally, the security and infrastructure cost is much lower than managing one’s own cloud, and the deployment speed is much higher.

Overall, the model provides the benefits of the public cloud without having to maintain its infrastructure.

According to AWS, this shared model “can help relieve the customer’s operational burden as AWS operates, manages and controls the components from the host operating system and virtualization layer down to the physical security of the facilities in which the service operates.”

However, failing to follow it for any reason carries significant risks:

- data breaches
- cyberattacks
- financial loss (ransomware, regulatory fines, remediation costs)
- legal liability and potential lawsuits
- reputational damage.

The first is the one you should be the most worried about: should it happen, all the others will follow.

Simple misconfiguration mistakes can lead to data breaches, and unfortunately, this happens all the time.

## Cracks in the model

This is a good time to discuss the issues with this system, and the first one is certainly the problem of misunderstanding, which leads to overlooked responsibilities and, subsequently, to security gaps in the customer’s databases, hence between the provider and the customer as well.

This issue results in misconfiguration - the direct culprit for most cloud security breaches.

Understanding responsibilities in a constantly changing environment is difficult. Sometimes organizations try to follow it, but overlook something. Sometimes they’re not even aware that they have this responsibility, presuming it all falls on the provider. And often they fail to protect certain data that may seem less relevant, such as backup files.

Either way, the end result is the same: databases are left unprotected and exposed for all to see and download.

This is so far from being theoretical that it’s nearly the norm. Just recently, security researcher Jeremiah Fowler discovered yet another unprotected database, with 666,369 records, including names, email addresses, phone numbers, IP addresses, and hashed passwords of the Tribeca Festival employees and attendees.

Potential consequences are massive and far-reaching for both the organizations that failed to protect the data and the individuals whose data was exposed.

Other issues in the shared model system include getting full visibility into the cloud environment, a lack of effective integrations that sustain and improve collaboration, challenges integrating tools and platforms, etc.

And if you’re managing security in a multi-cloud environment, that’s a larger beast to deal with.

## Final thoughts

Protecting data is neither only the cloud service provider’s job nor that of the company. Rather, the job is divided between “mine” and “yours”. Generally speaking, providers protect what they’ve created, their house, so to speak. Customers are in charge of making sure all their own data and related services in the rented rooms are properly secured.

This is more easily said than done, given that, despite the many advantages of sharing this responsibility (including significant time and cost savings), mistakes happen a lot for many reasons, and the customers’ databases end up exposed. It’s a key issue to overcome if this model is to function successfully long-term.

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
