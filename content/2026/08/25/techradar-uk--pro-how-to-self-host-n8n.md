---
title: How to self-host n8n
source_url: https://www.techradar.com/pro/how-to-self-host-n8n
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-25T13:07:47Z'
published: '2026-08-25T00:00:00Z'
description: Run your own automation platform, your rules
image: https://cdn.mos.cms.futurecdn.net/NuuAdt9MomVTTvn9K6vxzB-1376-80.jpg
---

![n8n workflow](https://cdn.mos.cms.futurecdn.net/NuuAdt9MomVTTvn9K6vxzB.jpg) 

Frustrated by workflow limits and token-based billing on AI automation platforms? n8n is a “fair-code” automation platform that you can host on your own device or servers, free from the usage restrictions that plague cloud-based platforms.

We’ve covered n8n on TechRadar before, so head over to our first-time user guide and list of compatible hosting solutions if you’re looking for more information. For now, however, I’ll walk you through the exact step-by-step process of setting up a self-hosted n8n environment using Docker, Docker Compose, and a Linux-based virtual machine or server.

## What you'll need for this setup

- A virtual machine, server, or NAS with at least 2 vCPUs and 4GB of RAM. Heavier workloads will benefit from more CPU cores and memory.
- A compatible version of Linux installed on your server or machine, such as Ubuntu, Debian, or Raspberry Pi OS. CentOS Stream, Fedora, and RHEL are also supported.
- Access to the Docker and Docker Compose repositories using your Linux distro’s package installer. All of this can be installed through the Linux terminal.
- A managed Kubernetes cluster if you intend to run production-grade workflows (optional).

## Step-by-step installation guide for self-hosting n8n

 ![n8n screenshot](https://cdn.mos.cms.futurecdn.net/S7mSpofYkYyTToNNPUyozK.png) 


## 1. Install Docker and Docker Compose

Power up your Linux terminal. Then update your Linux software catalog by running this command:

*sudo apt-get update* 

This will update your software packages, install any necessary certificates, and prep the system for installing Docker. Once done, execute the next command to install Docker and Docker Compose, along with any dependencies your system needs:

*sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin* 

You can manually confirm that your Docker engine is installed and running by executing this command:

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

*docker --version**docker compose version* 

## 2. Write your Docker Compose file

Create a new directory for your n8n setup, then navigate into it:

*mkdir n8n-compose cd n8n-compose* 

Now, you need to create a new .env file inside the new directory. It should look like this:

*DOMAIN_NAME=**example.com** SUBDOMAIN=n8n GENERIC_TIMEZONE=Europe/London SSL_EMAIL=**[you@example.com](mailto:you@example.com)* 

Make sure to replace these values with your domain name, time zone, and email address. If you’re running n8n locally on your device, you can simply remove the domain name, subdomain, and SSL email fields to leave only the GENERIC_TIMEZONE field in there.

Next up, we need to create a compose.yaml file in the same directory along with the .env file. It should read like this:

*services:**n8n:** image:**docker.n8n.io/n8nio/n8n** restart: always**ports:**- "127.0.0.1:5678:5678"** environment:**- N8N_HOST=${SUBDOMAIN}.${DOMAIN_NAME}**- N8N_PORT=5678**- N8N_PROTOCOL=https**- NODE_ENV=production**- WEBHOOK_URL=** [https://${SUBDOMAIN}.${DOMAIN_NAME}/**-](https://${SUBDOMAIN}.${DOMAIN_NAME}/**-) GENERIC_TIMEZONE=${GENERIC_TIMEZONE}**- TZ=${GENERIC_TIMEZONE}** volumes:**- n8n_data:/home/node/.n8n**- ./local-files:/files** volumes:**n8n_data:*

This maps n8n to port 5678 on your device and stores all your workflows, credentials, and encryption key in a Docker volume. Again, if you’re installing locally, you can simply remove the N8N_HOST, N8N_PROTOCOL, and WEBHOOK_URL lines.

In the same directory, create a local-files folder to store all your workflows:

*mkdir local-files*

 ![n8n screenshot](https://cdn.mos.cms.futurecdn.net/VbHLhXh5fr7jEEuUHp3EyK.jpg) 


## 3. Launch n8n

You can launch all your Docker Compose containers simultaneously using a single one-line command:

*docker compose up -d* 

After about a minute or so, run this command to see if the containers are up and running:

*docker compose logs -f n8n* 

You can now open the n8n editor at [https://localhost:5678](https://localhost:5678) on your local device using any web browser.

## 4. Create a n8n account

When you launch the n8n editor in your browser for the first time, it will ask you to create a new account. Enter your email, name, and a password with at least one capital letter and a number. Once you complete the form, you’ll become the instance owner, which is similar to a super-admin in n8n.

This will give your account full access to every workflow and credential, but you should still set up member-level accounts if you intend to have other people use your instance and want to track changes.

## 5. Build your first AI workflow

You’ll now be able to access n8n’s workflow editor. This is a node-based visual interface that looks a bit like a flowchart with the option to add triggers and actions to create complex automations. If you’ve used a tool like Zapier or Make before, it shouldn’t take you long to figure out the basics.

n8n lets you use the **Execute step** button to trigger different parts of a workflow during editing, which is useful in testing and troubleshooting. Once you’re confident that everything works, you can save the workflow and toggle it on so that it stays active.

 ![n8n screenshot](https://cdn.mos.cms.futurecdn.net/dPAZjwXorMGBjpfGEiMmwK.jpg) 


## FAQs

### Is n8n open-source?

n8n isn’t open-source but free-to-use with certain limitations. It’s distributed under a fair-code license that lets you use the platform for personal or internal business workflows free of cost. If you wish to commercialize it as a consumer-facing product, however, you’ll need to pay for a commercial license.

### Does it cost anything to self-host n8n?

There’s some cost involved in setting up a self-hosted n8n environment, but it’s much less compared to how much you’d pay with a cloud-based automation platform with a subscription. Your only expenses here are your hosting costs for the server you use, but even that can be removed if you have a powerful enough local rig that can run workflows on its own.

### Does n8n come with its own database?

n8n comes pre-loaded with SQLite on with every installation, which is fine for internal use. If you want to run production workflows, however, I’d recommend switching to PostgreSQL, which can better support complex multi-user workflows.

### How do I keep my n8n instance secure?

Make sure to run your n8n instance over an HTTPS connection instead of plain HTTP. If you’re using an external server or a local network that’s shared by other users, take extra care to keep your encryption keys secure and do not put them directly in your .env file. Depending on your server configuration, you can use a secret manager like Azure Key Vault or Google Cloud Secret Manager to avoid attackers from reading your API keys by scanning the source code in plain text.

![Ritoban Mukherjee](https://cdn.mos.cms.futurecdn.net/cD9joj4H54xYmooW8re3vU.png)

Ritoban Mukherjee is a tech and innovations journalist from West Bengal, India. These days, most of his work revolves around B2B software, such as AI website builders, VoIP platforms, and CRMs, among other things. He has also been published on Tom's Guide, Creative Bloq, IT Pro, Gizmodo, Quartz, and Mental Floss.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
