---
title: '''If you choose to install a spyware OS, expect to be spied on'': Windows
  11 process sparks controversy and user accusations of ''spying'' which are false
  — but Microsoft must still do better with privacy'
source_url: https://www.techradar.com/computing/windows/is-windows-11-spying-on-you-via-a-new-background-process-no-it-isnt-but-the-controversy-around-this-clearly-shows-microsoft-must-do-better-with-privacy
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-04T18:00:44Z'
published: '2026-08-04T00:00:00Z'
description: This affair highlights the ongoing distrust of Microsoft
image: https://cdn.mos.cms.futurecdn.net/4of3ZAPctcpMepFWehwaTL-2000-80.jpg
---

![The Windows 11 battery life indicator on a Dell 16 Plus](https://cdn.mos.cms.futurecdn.net/4of3ZAPctcpMepFWehwaTL.jpg) 

- **A controversy has erupted over a background process in Windows 11**
- **It turns out that process isn't new, and neither is it a surprise introduction from Microsoft that 'does nothing for you' except pipe telemetry back**
- **A Microsoft exec clarified the purpose of the process, and that it doesn't send any data back unless you want to do that**

There's been some more controversy over privacy and telemetry in Windows 11, and while this particular alarm bell turned out to be falsely rung in the end, it does point to wider issues around the mistrust of Microsoft in general.

As Windows Latest reports, this story starts with a post on X from a user called Xilly who drew attention to an apparent new process in Windows 11 called 'Windows Health and Optimized Experiences'.

However, as Windows Latest – and others on X – observe, this isn't a new background service in Microsoft's OS at all. In fact, it has been kicking around in Windows 11 for over a year now (since May 2025).

The additional nuance, though, is that this process was only introduced in testing in the Canary channel back in May of last year, and it seems to have only just come through to Windows 11 release builds now. That's as far as I can tell, and this is what Xilly points out on X.

So, it is in fact relatively new to release builds – and presumably rolling out now – but nonetheless the service itself has been known about for a long time. The real problem here is the way Xilly frames it as monitoring your PC for certain metrics related to laptop battery management, and that: "If you are on a desktop gaming PC it does nothing for you except run in the background" (while eating resources and engaging in telemetry, "sending data to Microsoft every 15 minutes").

Xilly's post prompted a response from Scott Hanselman, who is a VP and member of technical staff at Microsoft as well as a prominent voice in the Fix Windows 11 campaign.

Hanselman made it clear that the process is not new, as already discussed, and that it's for system diagnostics: "When Windows detects slow or sluggish behavior, it can record targeted performance traces locally under %SystemRoot%\Temp\DiagOutputDir\Whesvc that can be filed with Feedback Hub. It's not laptop specific."

Sign up for breaking news, reviews, opinion, top tech deals, and more.

So, this is a process that detects poor performance and files diagnostics locally, which can then be fed back to Microsoft if the user wishes.

Hanselman also highlights the dramatic approach Xilly took ("saying things in all capitals"), and Windows Latest further points out that the X user runs a business for optimizing gaming PCs, and pushes that service in a reply to their own original post.

## Analysis: trust, telemetry, and what Microsoft needs to do

 ![Samsung Galaxy Book 4 Edge](https://cdn.mos.cms.futurecdn.net/rF4iZ3MzgSf6hvwrTQyDG.jpg) 


To summarize, then, Xilly's description of the service is incorrect, and while this background process does collect diagnostic data on how Windows 11 is running, it's written locally (with a negligible performance impact) and only sent to Microsoft if you actively submit feedback from your PC (via the Feedback Hub). The key phrasing in Hanselman's response is that the relevant data "can" be filed with Microsoft (not "will" be filed, as in it'll automatically happen).

Xilly also suggested that this was something Microsoft just sneaked in (hence the 'all caps' warning), when in fact it has been documented in preview builds before, and as Windows Latest notes, it's part of the Adaptive Energy Saver feature for helping to extend battery life.

The long and short is that there's nothing to worry about here, but what this episode serves as is a reminder of how Microsoft is short on trust when it comes to issues around privacy.

It's clear how quickly some Windows 11 users were to believe Xilly's accusation on X and other social media such as Reddit. For example, in this Reddit thread, despite one poster pointing out the reality of the situation in a nutshell (pretty much), there's a notable amount of complaining about why this process is sending data to Microsoft (which it isn't), or broader complaints along the lines of: "If you choose to install a spyware OS, expect to be spied on."

In fact, the most upvoted comment is: "Honestly, if any big tech giant wants to spy on you, they don't need a separate service. The MSA/online account [Microsoft account] is more than enough."

There are many people out there online who believe that, one way or another, Microsoft is spying on them to quite an extent with Windows. That stems from a broader level of distrust that's been stoked by the historical level of telemetry in Microsoft's desktop operating system since Windows 10 emerged, with reports periodically popping up to highlight these issues in that OS and Windows 11. Add to that all of Microsoft's promotional activity (and some outright adverts), as well as the likes of the Recall feature helping to pile on the skepticism (Microsoft handled that one really badly), and you can see why there's a problem with doubters here.

I keep saying that one thing Microsoft isn't properly addressing with the fix Windows 11 campaign is the level of telemetry performed by the OS, and I think it's high time that the company did this, and introduced a new choice for a zero level of telemetry (save for baseline security-related aspects). That option is lacking on Windows 11 Home, and it should be present and easily accessible, as this would go a long way to help cure some of the ill feeling out there around Windows 11 'spying' on people.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![An Apple MacBook Air against a white background](https://cdn.mos.cms.futurecdn.net/LocVgRosBUWfJzDitFzhKR.png) 

➡️ **Read our full guide to the best laptops1. Best overall:**

Apple MacBook Air 13-inch M5**2. Best budget:**

Apple MacBook Neo**3. Best Windows 11 laptop**

Microsoft Surface Laptop 13-inch**4. Best thin and light:**

Lenovo Yoga Slim 9i**5. Best Ultrabook**

Asus Zenbook S 16

Darren is a freelancer writing news and features for TechRadar (and occasionally T3) across a broad range of computing topics including CPUs, GPUs, various other hardware, VPNs, antivirus and more. He has written about tech for the best part of three decades, and writes books in his spare time (his debut novel - 'I Know What You Did Last Supper' - was published by Hachette UK in 2013).

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
