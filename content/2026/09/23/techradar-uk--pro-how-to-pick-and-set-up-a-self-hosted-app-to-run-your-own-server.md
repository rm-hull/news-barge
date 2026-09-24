---
title: How to pick and set up a self-hosted app to run your own server
source_url: https://www.techradar.com/pro/how-to-pick-and-set-up-a-self-hosted-app-to-run-your-own-server
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-23T13:36:39Z'
published: '2026-09-23T00:00:00Z'
description: Get better control and visibility by self-hosting your apps and data
categories:
- Technology & Software
image: https://cdn.mos.cms.futurecdn.net/wqDphyjN5ftDvvJ4dKJLhn-1376-80.jpg
locations:
- Docker Hub
- India
- West Bengal
people:
- Docker
- Ritoban Mukherjee
organisations:
- AI
- Creative Bloq
- Docker Hub
- Gizmodo
- IT Pro
- OpenLiteSpeed
- Plesk
- Quartz
- Ritoban Mukherjee
- SSH
- TechRadar Pro
- Tom's Guide
- VPS
---

![a woman sat at a desk coding an app](https://cdn.mos.cms.futurecdn.net/wqDphyjN5ftDvvJ4dKJLhn.jpg)

Who owns your data once it leaves your devices? Who bears the responsibility for keeping it safe from prying eyes? What happens when the vendor you trusted with years of sensitive personal or business information suddenly decides to close shop?

Legally, these questions have straightforward answers. But in practice, it’s much murkier ground.

That’s why more and more people are now opting to store their apps and data on servers that they “own,” at least to some degree. By spending $15 to $20 a month on a private server, you can self-host websites, apps, automated workflows, and even local AI models. You retain full admin access over your server, including any data that goes into or out of it.

How does this work? Follow my detailed guide for instructions on how to set it up.

## Why self-host an app using Docker?

No one wants to pay subscription fees for tens of apps every month, or deal with spikes in token costs or usage fees with no announcement or ceremony. Worse still, we have officially reached the point where people can’t remember all the things they’re subscribed to, so credit cards get charged on autopilot before you can look at the bill and see what’s happening.

That’s not all. When you use a cloud-based app, your data lives on someone else's infrastructure, governed by someone else's terms of service. Self-hosting puts that data back on hardware you control, whether that's a spare machine at home or a rented server. You decide who has access and how long files are kept — plus you don’t have to worry about what happens if the vendor changes its privacy policy.

Businesses handling customer records, financial data, or health information often need to prove exactly where that data sits and who can reach it. For individuals, the risk is even more pronounced because any data breaches or cyberattacks have a direct impact on your life. A self-hosted setup gives you a direct answer to these problems instead of pointing you to a vendor's compliance page.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

With Docker, it’s a lot more practical, too.

Each app runs inside its own container, a package that contains the code, runtime, libraries, and configuration settings. Nothing leaks between containers, so installing one app won't bring down another. You have complete control over your data and app environment, while your only ongoing expense is the price of a hosting plan.

## How to self-host an app on your server, step-by-step

There's more than one route to a working self-hosted app. Some hosting providers give you full SSH access so you can install Docker apps using the command line. Others offer a graphical file manager or a library of ready-made templates that do most of the setup for you.

We'll walk through all these approaches below. Each assumes you already have access to a functional Linux server, workstation, or NAS. If you don’t have that set up yet, you can buy a hosting plan from any reputable web host. In fact, you can also start your own local server using a Linux computer or even a Raspberry Pi.

### Where to find and pick Docker apps

If you’re wondering which apps you can self-host, Docker has an image library called Docker Hub that contains ready-made installers with detailed instructions on how to set up different compatible apps on a self-hosted server.

Search the database for the app or functionality you need, locate the app you wish to install on your server, then follow along with the rest of the tutorial.

### Using the command line with SSH

SSH gives you direct access to your server without any restrictions, which makes it the most flexible option if you're comfortable using a command line.

Start by connecting to your server from your local desktop. You’ll need your Linux server’s IP address for this, so make sure you note that down first. This can be found in your hosting provider’s SSH settings. After that, you just need to type in the command below using Terminal or Command Prompt:

```
```
ssh your-username@your-server-ip
```
```

Now, install Docker on your server using your Linux distro's package manager. On Ubuntu or Debian, you can use these commands:

```
```
sudo apt update
sudo apt install docker.io docker-compose-plugin -y
```
```

Next, create a folder for your Docker app and a Compose file to define it. Docker Compose lets you describe an app's containers, networks, and storage in a single YAML file rather than typing out long docker run commands by hand.

```
```
mkdir ~/myapp && cd ~/myapp
nano docker-compose.yml
```
```

A basic Compose file names the container image you want to run, maps a port on your server to a port inside the container, and sets any environment variables the app needs, such as a database password or an admin email. Most self-hosted apps publish an example Compose file in their documentation, which you can copy and adjust. You can usually find these directly on their Docker Hub listings.

But if you’re not sure how this looks, here’s an example compose.yml file for installing NGINX:

```
```
services:
  web:
    # Pulls the official Nginx image from Docker Hub
    image: nginx:latest
    ports:
      - "8080:80"

  database:
    # Pulls the official Postgres image from Docker Hub
    image: postgres:15
    environment:
POSTGRES_PASSWORD: your-secure-password
```
```

You’ll need to replace “nginx:latest” with the image name of the Docker app you’re trying to install. I’d also recommend creating a more secure PostgreSQL password to replace “your-secure-password.”

Once you save the Docker Compose file, you can bring the app online with:

```
```
docker compose up -d
```
```

The -d flag runs the containers in the background so they keep running after you close your terminal session. Now when you point your web browser to your server's IP address and the port you mapped, your app should load.

### Using a control panel with native Docker support

If you'd rather avoid the terminal, some hosting provider control panels give you a visual way to manage containers directly.

cPanel is the most widely used panel, but it doesn't include native Docker management, so you’re stuck using SSH only. However, Plesk has an official Docker extension that lets you browse images from Docker Hub, deploy containers, and manage them from a dedicated section in the sidebar without touching a command line interface. CyberPanel, another free and open-source control panel built on OpenLiteSpeed, also ships with Docker management built in as an alternative to SSH setup.

Then you just search the image catalog or paste in your own YAML file, review the resource and port settings the app requests, and confirm the deployment. The panel pulls the image, starts the container, and usually shows you live logs if something fails.

Once the app is running, the same panel typically handles DNS records and SSL certificates too. That's a decent accessibility advantage over pure SSH, since you don't need to deal with stuff like configuring a reverse proxy or certificate renewal by hand.

### Using pre-coded templates offered by web hosts

Still, the fastest route to a running app is a hosting provider's marketplace of pre-built templates. These exist specifically so you don't have to write a Compose file from scratch.

Log in to your hosting provider's dashboard and look for a marketplace, app catalog, or "one-click apps" section. Search for the app you want to run. Popular self-hosted tools like automation platforms, note-taking apps, and file-sync services are commonly available this way.

Selecting a template usually opens a short setup form. You'll pick your server size, choose a data center region close to your users, and set any required credentials, like an admin password. Confirm the order, and the provider provisions a server with Docker and your chosen app already configured and running.

This method trades some flexibility for speed. You won't have as much control over container configuration, and templates can lag behind an app's latest release. But for popular tools, it's usually the quickest way to go from nothing to a working instance you can start customizing.

## Are there any caveats to self-hosting?

Self-hosting shifts responsibility from a vendor's support team to you. Security patches, software updates, and backups no longer happen automatically in the background. If you forget to update a container image for months, you could be running software with a known vulnerability, and nobody will send you a reminder before your server gets compromised.

Uptime becomes your problem too. A managed SaaS product usually has a dedicated team monitoring its infrastructure around the clock. A self-hosted app on a single server has no such safety net unless you set one up yourself, whether that's monitoring software, automated backups, or a failover server in case there’s a crash.

There's also a real-time cost that's easy to underestimate. Reading documentation, troubleshooting containers, keeping track of which ports and volumes belong to which app all add up — all these things cost time and effort. For a single low-stakes tool, that's a minor inconvenience. For a business running several self-hosted apps, it can turn into a part-time job unless you budget for it properly.

## Is self-hosting actually cheaper?

On paper, the numbers look compelling. A small virtual private server capable of running several lightweight self-hosted apps typically costs somewhere between $5 and $20 a month, depending on the provider and specs you choose. Compare that to a single SaaS subscription that can easily run $20 to $60 a month per tool, and the gap widens fast once you're replacing multiple subscriptions with one server.

The savings tend to grow with scale, up to a point. Running two or three self-hosted apps on the same VPS costs roughly the same as running one, since you're paying for the server rather than per app. That changes the math significantly compared with SaaS pricing, where every additional tool usually means an additional bill.

But cheaper isn't the same as free. A server with no backup strategy or monitoring in place isn't really saving you money if it goes down and you lose data or spend a weekend fixing it. Factor in the hours you'll spend on updates and troubleshooting, especially early on, and self-hosting looks less like a free lunch and more like a trade. You get lower cash costs in exchange for taking on the operational work a SaaS vendor would normally handle for you.

![Ritoban Mukherjee](https://cdn.mos.cms.futurecdn.net/cD9joj4H54xYmooW8re3vU.png)

Ritoban Mukherjee is a tech and innovations journalist from West Bengal, India. These days, most of his work revolves around B2B software, such as AI website builders, VoIP platforms, and CRMs, among other things. He has also been published on Tom's Guide, Creative Bloq, IT Pro, Gizmodo, Quartz, and Mental Floss.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
