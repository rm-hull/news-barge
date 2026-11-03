---
title: OpenAI, Google, Microsoft and Anthropic are joining forces to give website
  owners more control over AI training — here's how to opt out
source_url: https://www.techradar.com/ai-platforms-assistants/we-believe-this-is-a-practical-step-toward-an-open-web-dont-want-ai-companies-training-on-your-website-openai-google-and-microsoft-are-backing-a-new-way-to-opt-out
source_site: TechRadar UK
source_slug: techradar-uk
description: OpenAI will now honor AI scraping rules contained within the robots.txt
  file
image: https://cdn.mos.cms.futurecdn.net/8iN8JcsjaeEppccYgURuY9-1920-80.jpg
published: '2026-11-03T00:00:00Z'
scraped_at: '2026-11-03T17:04:30Z'
categories:
- Technology & Software
people: []
locations: []
organisations:
- AI
- Anthropic
- Google
- IP
- Library of Alexandria
- Microsoft
- OpenAI
- Reddit
---

![The ChatGPT and Claude mobile apps on a phone screen next to a digitized image of a robot](https://cdn.mos.cms.futurecdn.net/8iN8JcsjaeEppccYgURuY9-1920-80.jpg)

OpenAI, Google, Microsoft and Anthropic have agreed to support a new way for website owners to stop their content being used to train AI models. The companies are backing a shared opt-out signal in a website’s robots.txt file, which tells AI crawlers whether they're allowed to use its content for training.

Like a modern day Library of Alexandria, the internet is the single largest source of human knowledge that exists. Countless people have spent their lives cataloguing and uploading the entire history of humanity for the betterment of everyone.

AI companies are a tinderbox in this regard. To train and develop better capabilities for their models, AI companies are repeatedly scraping every corner of the internet to create archives of training data. Compounded by changes in search and how people seek information, AI threatens to become the single point of access to information.

But just because you have a website, it doesn’t mean you want it constantly scraped by bots stealing your answers to life’s difficult questions so people can access them elsewhere.

Luckily, you’re not alone. Outrage from users and website hosts across the internet has been fueled into developing methods to keep AI companies from harvesting data from your websites.

Like layering slices of Swiss cheese, these methods work best to keep out scrapers when used in a defense-in-depth manner. But some malicious bots will still find ways to navigate through the holes. Here’s a few ways to keep the honest bots at bay:

![A man on a laptop, close on the hands hovering over the keys](https://cdn.mos.cms.futurecdn.net/djX7joLwsdetjvNWwzvmjE-1200-80.png)

## 1. Robots.txt

This is the crux of OpenAI’s method to honor anti-web scraping markers. The ‘robots.txt’ text file sits in the root directory of your website and provides guidance on how bots should behave. This can be a useful way to provide a digital map to search engine crawlers and can also prevent your site’s servers from becoming overburdened by bot requests.

Sign up for breaking news, reviews, opinion, top tech deals, and more.

But by adding just a few characters to this file, you can block the majority of bot traffic from accessing your website. Of course, this unfortunately only applies to scrapers that actually abide by the rules of your robots.txt file.

OpenAI has set something of a precedent for other AI companies here, adding that, "We encourage other AI providers to honor the signal."

There are a few ways to manage which specific bots you would like to allow on your website, but to block AI traffic you can take the following steps:

* Open your robots.txt file, or create one if you don’t have one using a text editor
* Add a section to the file using the heading ‘**# AI crawlers**’
* To block all AI crawlers, add a line below stating ‘**Disallow: /**’
* To block a specific AI crawler, such as ChatGPT, place ‘**User-agent: ChatGPT-User**’ on one line, with ‘** Disallow: /**’ underneath
* You can prevent AI crawlers from accessing specific pages by adding the web address after the ‘/’. For example, I could stop AI crawlers from accessing my author page by using the rule ‘**Disallow: /author/benedict-collins**’
* Update your robots.txt file in the source files of your website

## 2. User-only viewing

Alternatively, you could take the planned Reddit approach to blocking AI traffic by requiring all users to have an account in order to access your website. This is an excellent way to filter out human traffic from bot traffic because user accounts usually need to be verified with an email or phone number - something mostly humans have.

But this comes with its own caveats, and Reddit is finding out the hard way in feedback from users. Not requiring an account gives users from all over the web an easier search experience. They can find the information they need without any obstacles, and without handing over personal information to yet another website.

Having to log in or create an account to view web content can cause people to ‘bounce’ - they click on your website, see they need to create an account, and immediately back out of your site to seek the information they need elsewhere. So tread carefully if your traffic matters to you.

## 3. IP limiting

AI bots may descend en-masse using a single IP address to access your website. Third-party services offer this as an option to prevent your website’s servers from being bombarded with quick-moving traffic, but it can come with a monetary cost.

This method can be used to set up a timer on specific IP addresses that are detected as bot traffic. For example, if a single IP is sending multiple access requests, you can adjust the settings so that only 5 requests from the IP can be made in a 10 second period.

But beware that some AI bots or web scrapers will use rotating IPs, hopping between them to avoid a block from a single IP.

## 4. Captchas

A slightly archaic method of human verification that most people have a love/hate relationship with. I don’t mind counting the number of buses or bicycles, or aligning the correct jigsaw piece with its place, but some people see it as a humiliating ritual to prove their humanity.

What’s worse is that some AI models are getting good enough to solve captchas themselves.

It can help to filter out relentless attempts from web scrapers and less capable AI bots, but it could also cause users to bounce - especially those with a particular fear of ClickFix attacks who may see a complicated captcha as a way to hijack their device.

So use these methods cautiously for they is a double-edge sword. You can stop your data from being harvested by AI bots but it may also harm the experience of your users.

![An Apple MacBook Air against a white background](https://cdn.mos.cms.futurecdn.net/LocVgRosBUWfJzDitFzhKR-140-80.png)

➡️ **Read our full guide to the best laptops1. Best overall:**Apple MacBook Air 13-inch M5** 2. Best budget:**Apple MacBook Neo** 3. Best Windows 11 laptop**Microsoft Surface Laptop 13-inch** 4. Best thin and light:**Lenovo Yoga Slim 9i** 5. Best Ultrabook**  
Asus Zenbook S 16
