---
title: Someone targeted security researchers using a fake crypto conference as a lure
  | TechCrunch
source_url: https://techcrunch.com/2026/08/20/someone-targeted-security-researchers-using-a-fake-crypto-conference-as-a-lure/
source_site: TechCrunch
source_slug: techcrunch
scraped_at: '2026-08-20T20:41:53Z'
published: '2026-08-20T00:00:00Z'
description: A hacker pretending to work for a leading cryptocurrency news website
  targeted several cybersecurity professionals using Google Docs as a way to deliver
  malware.
image: https://techcrunch.com/wp-content/uploads/2018/02/gettyimages-887454272.jpg?resize=1200,797
---

If you are a malicious hacker, cybersecurity professionals may very well be the worst people in the world to try to hack, as there is a very good chance they are going to catch you.

A person pretending to work for a leading crypto news site targeted several cybersecurity professionals around the time of the Black Hat and Def Con hacking conferences earlier this month. The hacker approached attendees on the social media site X, both via public replies and DMs, and then leveraged Google Docs in an attempt to trick the targets into installing malware, according to researchers.

On Wednesday, security firm Huntress published a blog post detailing the hacking campaign, which targeted one of its researchers, who pretended to go along with it to learn what the hacker was trying to do.

In broken English, the hacker asked the researcher if they had plans to attend a conference next, and then mentioned a conference allegedly organized by the crypto news website, according to a screenshot of the conversation.

After that, the hacker shared a legitimate Google Doc that looked like it was a planning document for the fake conference. The document displayed a sidebar designed to make the target think it was encrypted. The goal was to first trick the target into entering a fake decryption key provided by the hacker. That was the first step in a process that would lead to the installation of malware for macOS and Windows, depending on the operating system used by the target, according to Huntress.

To make the sidebar appear real, the hacker used Google App Script, a platform that allows developers to customize the user interface of Google Docs with menus and sidebars, for example.

![A screenshot of the Google Doc sent by the hacker to the Huntress researcher.](https://techcrunch.com/wp-content/uploads/2026/08/huntress-fake-crypto-conference-google-doc.png)

**Image Credits:** Huntress/Screenshot

The hacker tried to trick Huntress’ researcher into installing an infostealer for Apple computers; a remote desktop viewing tool repurposed as malware for Windows; and a fake installer for the cryptocurrency wallet Ledger.

The person behind the account identified by Huntress researchers as the hacker did not respond when TechCrunch sent them a private message on X.

Hackers of all kinds — whether they are unknown government hackers using advanced spyware or North Korean government hackers using fake Twitter profiles — have targeted cybersecurity professionals before. What made this campaign a bit more believable was the use of a legitimate Google Doc and Google feature.

Google did not immediately respond when TechCrunch reached out asking if the company had seen this or similar hacking campaigns.
