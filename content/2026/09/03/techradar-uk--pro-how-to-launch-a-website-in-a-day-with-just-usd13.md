---
title: How to launch a website in a day with just $13
source_url: https://www.techradar.com/pro/how-to-launch-a-website-in-a-day-with-just-usd13
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-03T12:48:18Z'
published: '2026-09-03T00:00:00Z'
description: Get a working website in 24 hours, no coding required
image: https://cdn.mos.cms.futurecdn.net/pn8mi5bwjphoGzQMBBhCDP-1376-80.jpg
---

![a man building a website on a macbook in a minimalist office](https://cdn.mos.cms.futurecdn.net/pn8mi5bwjphoGzQMBBhCDP.jpg) 

Let's say you've got an idea for a new business. A landing page is usually the first piece of "real estate" you invest in, long before you think of retail space or even a marketing brochure.

Websites cost a lot less today than they did ten years ago, but they cost even less if you know what you need (or don't).

In this guide, I'll show you how to set up a professional website for a solo or small business for as little as $13 in setup costs. You'll need a GitHub account, a free or low-cost vibe coding app, and $5 to $20 of spare cash for a domain registration.

But the best part is that you can scale this setup as you grow, adding just what you need without a single cent wasted. Slow season? You can also scale those resources back down. Here's exactly how I would structure it.

## Launching a website in a day with $13: What to expect

My stack works best for landing pages, portfolios, small business sites, and simple lead generation forms. You'll end up with a mobile-friendly site on your own domain, built without any coding skills by describing what you want in plain English.

There's always a trade-off with these setups, which is scale. You can't collect payments, running complex workflows will crash your website, and storage is limited if you want to host audiovisual content.

But if you structure it right, you can keep space to expand things later without having to go through an expensive migration to a premium platform. There's no vendor lock-in, your existing stack is designed for scalability, and you're not stuck with any one provider.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

**Does it really cost $13?**

Yes, because you'll only have to pay for the domain and a small subscription fee if you want to access one of the better vibe coding or AI website builders.

A .com domain from a mainstream registrar runs somewhere between $5 and $15 for the first year, which covers the budget in this guide with room to spare.

There's no upcharge for connecting your domain, AI tools don't always bill you for every additional token, and there are no additional monthly charges for hosting or storage, etc.

**What tools will I need?**

You'll need three things, and possibly a couple more if your site needs to store data or display dynamic content. Each category has many options with generous free plans. None of them require you to enter a credit card to get started.

Here's the exact stack you'll use to build and launch a website using this guide.

- A vibe coding tool. Look for one that supports code sync and export to an external repository, even on the free plan.
- A free GitHub account with a new repository that has GitHub Pages enabled.
- A custom top-level domain, such as a .com or .org, which costs roughly $10 to $20 a year.
- A free Supabase account for handling logins and storing form submissions. This one is entirely optional.
- A free AI code editor, like Cursor or Claude Code, installed on your computer for minor tweaks and updates. Also optional.

## Step-by-step instructions for launching a $13 website in one day

All of these steps take anywhere from a few minutes to an hour individually. Work through them in order, and you should have a live site well before dinner.

### Step 1: Describe your site to a vibe coding tool

Open your chosen vibe coding platform and describe the site you want in plain language. Mention the type of business, the pages you need (home, about, contact, pricing), and any specific sections like a lead capture form or testimonials block.

Most tools generate a working preview within a minute or two. From there, refine it with follow-up prompts:

- Ask for changes to layout, color scheme, or copy one section at a time, rather than everything at once.
- Request a working contact or sign-up form early, since this is often the trickiest part to get right.
- Check the mobile preview, since most visitors will land on your site from a phone.

Remember that on most free tiers, vibe coding tools will limit the number of prompts you can enter in a day. So make sure to read up on these limits and be certain about what you want so you can describe it verbatim. Also mention that you'll be hosting the website using GitHub Pages in your prompt itself, so that the AI can structure the code to be Pages-compatible.

### Step 2: Connect a GitHub repository

Once you're happy with the design, look for the option to sync or export your project to GitHub. Most vibe coding tools have a one-click GitHub connection built in. You can also just export the code as a ZIP file and upload the contents directly to GitHub.

Create a free GitHub account, then create a new repository for the project. Keep it public so you can enable GitHub Pages, because Pages hosting is free for public repositories but requires a Premium plan for private ones.

### Step 3: Turn on GitHub Pages

In your repository, go to Settings, then Pages. Choose the branch your site should deploy from (usually main) and save your changes.

GitHub will generate a free web address in the format yourusername.github.io/repository-name. This confirms your site is live, even before you attach a custom domain.

### Step 4: Buy your domain

Pick a domain registrar and search for the domain name you want. Prices vary depending on the extension you pick, so a .com will usually cost more than a less common option like .dev or .site.

Stick to a mainstream registrar with clear pricing and no surprise renewal jumps. Skip any add-ons you don't need, like a premium DNS, to keep your total below $10.

### Step 5: Point your domain at GitHub Pages

Back in your GitHub repository's Pages settings, enter your custom domain in the relevant field. This creates a small configuration file in your repository that tells GitHub which domain to serve your site from.

Then, in your domain registrar's dashboard, add the DNS records GitHub provides. This usually means a few A records pointing to GitHub's servers, plus a CNAME record if you're using a "www" version of your domain. These changes can take anywhere from a few minutes to a few hours to fully take effect.

### Step 6: Set up Supabase (optional)

If your site needs to collect sign-ups, store bookings, or handle a login system, create a free Supabase project. Supabase gives you a hosted database along with authentication tools, without needing to manage a server yourself.

Most vibe coding tools have a direct Supabase integration, so you can usually connect your project with an API key rather than writing database code by hand. Ask your vibe coding tool to build the specific form or login flow you need. It will typically wire up the Supabase connection for you. When you connect or upload the files and code to GitHub, the integration will stay intact.

### Step 7: Test everything before you call it done

Open your site on both desktop and mobile, and click through every link, button, and form. Submit a test entry through any lead capture form to confirm it actually reaches Supabase or your inbox.

Check that your custom domain loads correctly with https:// rather than throwing a security warning, since GitHub Pages issues free SSL certificates automatically once your DNS is set up correctly. Fix anything that looks off before sharing the link with anyone.

For small fixes, like a typo or a button that's misaligned, it's often faster to open the project in a free AI code editor like Cursor or Claude Code and make the change directly, rather than going back through your vibe coding tool's chat interface. Once you push the update to GitHub, your live site refreshes automatically.

## What to do when you outgrow your $13 website

At some point, your free tiers will start to feel tight. Maybe you're approaching Supabase's storage or user limits, or your traffic has grown to the point where you want more control over performance and analytics.

The good news is that none of the upgrades below require you to rebuild your site from scratch. Because your code lives in a standard GitHub repository, you can move it to almost any hosting provider without losing your design or content.

- Upgrade your Supabase project to a paid tier once you're close to the free plan's storage, bandwidth, or user limits, rather than waiting until you hit a hard wall.
- Move hosting from GitHub Pages to a platform built for dynamic sites, such as Vercel or Netlify, if you need server-side features GitHub Pages doesn't support.
- Add a content delivery network in front of your site once traffic grows, so pages load quickly for visitors regardless of where they're located.
- Bring in a developer to review and harden any AI-generated code before it handles sensitive customer data, particularly around authentication and payments.
- Set up proper analytics and monitoring so you know when you're approaching a limit, instead of finding out when something breaks.

## Low cost alternatives

The approach I have outlined above gives a great level of flexibility and scalability with a small upfront cost. However, there are other options out there if you are looking to create a website on a budget. 

For example, you may pick an AI website builder and build your website entirely within that platform. This offers a simpler, all-in-one approach, although it can make it tricky to move your website elsewhere if you find it doesn't meet your needs in the future. 

The best AI website builders start at around $2.99 a month, although this price will often rise to anywhere from $10 to $150 a month once the introductory period is over and depending on your website needs.

![Ritoban Mukherjee](https://cdn.mos.cms.futurecdn.net/cD9joj4H54xYmooW8re3vU.png) 

Ritoban Mukherjee is a tech and innovations journalist from West Bengal, India. These days, most of his work revolves around B2B software, such as AI website builders, VoIP platforms, and CRMs, among other things. He has also been published on Tom's Guide, Creative Bloq, IT Pro, Gizmodo, Quartz, and Mental Floss.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
