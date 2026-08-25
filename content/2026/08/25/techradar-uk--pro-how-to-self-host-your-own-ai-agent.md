---
title: How to self-host your own AI agent
source_url: https://www.techradar.com/pro/how-to-self-host-your-own-ai-agent
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-25T16:50:58Z'
published: '2026-08-25T00:00:00Z'
description: Run your own private AI assistant
image: https://cdn.mos.cms.futurecdn.net/ucFZ7tKSFWyGKUEuuJ74ig-1376-80.jpg
---

![openclaw on a mac](https://cdn.mos.cms.futurecdn.net/ucFZ7tKSFWyGKUEuuJ74ig.jpg) 

When you run AI agents like ChatGPT Work or Microsoft Copilot, your files and prompts all pass through third-party servers that you’re not in control of. Essentially, you’re paying a subscription fee for the privilege of letting someone else handle your data, when you could be running the same tasks locally from your own hardware.

For professionals and teams that work in regulated industries or need to ensure strict local compliance, this can be an ongoing challenge. Even when you’re opting out of model training in ChatGPT or Claude, you’re trusting them to honor that agreement with very little legal recourse in case they don’t.

However, self-hosting your own agents is not as complicated as it used to be. You can easily set up a private OpenClaw environment on your local workstation, VPS, or NAS. Then if you want, you can go the extra mile by layering your OpenClaw setup with Open WebUI’s polished visual interface. I’ve run this setup myself on my home computer, and I’ll show you how easily you can do it too.

## What you'll need before we start

- A local desktop, virtual machine, VPS, or NAS device running Linux. It should have at least 4GB of RAM and 20GB of free storage space.
- Sudo access to your Linux operating system.
- Node.js 22 or later installed on your OS (Node.js 24 is the recommended version).
- An API key for your preferred LLM vendor, such as OpenAI or Anthropic.
- Or if you have the GPU for it, you can run an open-weight LLM like Llama 3.3 locally on your system with Ollama (optional).

 ![Openclaw screenshot](https://cdn.mos.cms.futurecdn.net/HyvADZwV2u7eu5KxDHp2Xi.png) 


## Step-by-step installation guide for self-hosting your own AI agent

## Step 1: Install OpenClaw

OpenClaw is an open-source autonomous agent framework that can run shell commands, browse the web, read/write files, and connect to messaging apps using your local infrastructure. You can install it using the official script.

*curl -fsSL [https://openclaw.ai/install.sh](https://openclaw.ai/install.sh) | bash*

Once installed, run the onboarding wizard. This is where you'll connect your model provider's API key and give your OpenClaw agent a name.

*openclaw onboard*

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

Follow the on-screen instructions to configure a default AI model and paste in your API key after picking. You can also choose to run an open-weight AI model like Llama 3.3 or Qwen 3.7 locally on your hardware, by downloading the model repo from an online database like Hugging Face. The wizard writes its output to a configuration file at ~/.openclaw/openclaw.json, which you'll need to edit again in the next step.

## Step 2: Enable the API endpoint

Open WebUI talks to OpenClaw through an OpenAI-compatible endpoint, but that endpoint is switched off by default for security reasons. Open the configuration file in a text editor using the nano command.

*nano ~/.openclaw/openclaw.json*

Now add or update the following block so the API endpoint is enabled.

```
json
{
  "gateway": {
    "http": {
      "endpoints": {
        "chatCompletions": {
          "enabled": true
             }
          }
       }
    }
}
```
Save the file and close the editor. If the gateway is already running, you'll need to restart it for the change to take effect.

## Step 3: Start the gateway

With the endpoint enabled, we need to start the gateway process.

*openclaw gateway*

The gateway starts on port 18789 by default. Confirm it's running with the built-in status check.

*openclaw gateway status*

 ![Openclaw screenshot](https://cdn.mos.cms.futurecdn.net/gCmHmYqr9JYXiKacbsFDYi.jpg) 


## Step 4: Install Docker and run Open WebUI

Open WebUI offers a polished visual interface that makes it easier to create and run OpenClaw agents without interacting with the CLI in terminal every time. Open WebUI recommends installing it as a containerized Docker application, so we first need to install Docker Engine and Docker Compose.

Before we do anything else, open a terminal window and update your package index.

*sudo apt-get updatesudo apt-get install -y ca-certificates curl*

Add Docker's official GPG key, which lets your system verify that the packages actually came from Docker.

`sudo install -m 0755 -d /etc/apt/keyringssudo curl -fsSL [https://download.docker.com/linux/ubuntu/gpg](https://download.docker.com/linux/ubuntu/gpg) -o /etc/apt/keyrings/docker.ascsudo chmod a+r /etc/apt/keyrings/docker.asc`
Now register Docker's repository with apt.

`echo \  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] [https://download.docker.com/linux/ubuntu](https://download.docker.com/linux/ubuntu) \  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/nullsudo apt-get update`
Install Docker Engine and Docker Compose.

*sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin*

Now run Open WebUI as a container.

```
docker run -d \
  --name open-webui \
  --restart unless-stopped \
  -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -v open-webui-data:/app/backend/data \
ghcr.io/open-webui/open-webui:main
```
**Note:** Because Open WebUI runs in a container and OpenClaw runs directly on the host, Open WebUI can't reach the gateway using localhost. Using the --add-host flag here lets it reach the host machine instead, where the OpenClaw gateway is listening on port 18789.

## Step 5: Connect Open WebUI to your OpenClaw agent

Open a browser and navigate to [http://your-server-ip:3000.](http://your-server-ip:3000.) Create an admin account on first launch, since the very first user to sign up becomes the administrator.

Once you're logged in, head to the connections settings.

- Go to **Admin Settings**>** Connections**>** OpenAI** .
- Click **Add Connection** .
- For the URL, enter [http://host.docker.internal:18789/v1.](http://host.docker.internal:18789/v1.)
- For the API key, paste your OpenClaw gateway bearer token, which you'll find in ~/.openclaw/openclaw.json under the gateway authentication section.
- Click the checkmark to verify the connection, then save.

Your OpenClaw agent should now appear as a selectable model in Open WebUI's chat window. Pick it from the dropdown and send a test message to confirm everything is wired up correctly.

 ![Openclaw screenshot](https://cdn.mos.cms.futurecdn.net/9qpqEtyCcdQ9LSfJvjieWi.png) 


## What to do now that you’re all set up?

With your OpenClaw setup complete and the UI functional, you can now start exploring the kind of automated workflows you can run with this system. If you’re flummoxed by all the options, here are some pointers on what you could look into first:

- OpenClaw has a community-driven Skills library that features tons of working automations for everything from GitHub repo maintenance to data visualization to vibe coding. Take a look at the ClawHub to get started.
- Apart from Open WebUI, OpenClaw can also be integrated with your favorite communication apps like Slack, Telegram, Discord, or WhatsApp. Or better yet, you can use the built-in integration tools offered by OpenWebUI to set up a chatbot for Telegram, WhatsApp, Signal, and others. Just navigate to Settings > Admin > Bots in Open WebUI to configure chatbots using API tokens.
- If you want to run automated workflows on repeat, OpenClaw lets you set up cron jobs that trigger automatically according to a set frequency. View the OpenClaw documentation for details on how to set these up.
- If you’re running this setup on a personal workstation, make sure to back up all your important files and log out of active online accounts that you don’t want your agents to have access to. OpenClaw has system-wide privileges enabled by default, so it can read and write any file or execute tasks on its own, which can be a problem if you have sensitive data on the device. This is also why setting up OpenClaw on a VPS server is the recommended method for data isolation.

## FAQs

### Do I need coding experience for OpenClaw?

No, you don’t need to know any programming languages for OpenClaw, although some basic familiarity with command-line interfaces does help during setup. Once the first-time setup is complete, though, you can simply rely on Open WebUI’s chat-based interface to configure and run OpenClaw agents.

### Is this really more private? Does my data never leave the system?

It depends on which options you chose when following this tutorial. If you’re connecting OpenClaw a cloud-hosted AI model’s private API, the model provider will have access to any data you process through the LLM. However, running an open-weight model locally on your system hardware keeps everything confined to your own environment with no cloud involvement.

### Are there any subscription fees or costs associated with this setup?

OpenClaw and Open WebUI are both free to use. If you use a cloud-based AI model to run OpenClaw, however, you’ll still need to pay for API credits based on your LLM’s token consumption. This is still much more cost-effective than a fully managed AI agent platform, which will bill you separately for each automated job you run.

![Ritoban Mukherjee](https://cdn.mos.cms.futurecdn.net/cD9joj4H54xYmooW8re3vU.png)

Ritoban Mukherjee is a tech and innovations journalist from West Bengal, India. These days, most of his work revolves around B2B software, such as AI website builders, VoIP platforms, and CRMs, among other things. He has also been published on Tom's Guide, Creative Bloq, IT Pro, Gizmodo, Quartz, and Mental Floss.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
