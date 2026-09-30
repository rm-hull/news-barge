---
title: AI models are sharing sensitive data from tech companies in new 'PixelLeak'
  screenshots
source_url: https://www.techradar.com/pro/security/ai-models-are-sharing-sensitive-data-from-tech-companies-in-new-pixelleak-screenshots
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-30T18:13:25Z'
published: '2026-09-30T00:00:00Z'
description: Privacy-oblivious AI agents leave sensitive data out on the open
image: https://cdn.mos.cms.futurecdn.net/MZeWJhJjT34M4nQvMMX7fg-1376-80.jpg
categories:
- Technology & Software
- Business & Entrepreneurship
people:
- Glow
locations:
- Shadow AI
- UI
organisations:
- Artificial Intelligence
- GitHub
- Glow Security
- Shadow AI
- TechRadar Pro
---

![an ai agent sat at a laptop](https://cdn.mos.cms.futurecdn.net/MZeWJhJjT34M4nQvMMX7fg-1376-80.jpg)

* **AI coding agents exposed sensitive screenshots while attempting to document software changes**
* **Researchers found thousands of publicly accessible images across hundreds of organizations**
* **Findings highlight security risks from autonomous developer tools and Shadow AI practices**

Artificial Intelligence (AI) doesn’t have to be malicious, evil, or gullible, to be a security risk. Case in point - thousands of publicly hosted screenshots, many containing important secrets, being uploaded by an AI that just wanted to get its job done.

Cybersecurity researchers Glow Security discovered multiple public GitHub repositories built by AI agents. They were hosting more than 13,000 screenshots from more than 300 companies. Some of the screenshots contained information about sensitive corporate software projects. They are calling the findings “PixelLeak”:

## PixelLeak

“Each case investigated during our “PixelLeak” research started with a developer asking an agent to prove that a visual change worked. The software was changed, for example with a fix to the user interface layout, and the reviewers needed to see the before and after,” the researchers explained. “That’s where the agents ran into a wall.”

In other words, devs asked AI for a before/after comparison, and the agent went the extra mile (and then some) to comply.

As the researchers then explained, GitHub has an official image hosting service that’s built directly into the site’s pull request interface. It supports human developers with a web browser, but that’s not how coding agents work. They use text-based CLI, which means they weren’t able to include before/after screenshots for review.

“How did they work around this limitation? The agents figured out that they could make the image available to the human reviewer by hosting it in an adjacent public repo. They just didn’t consider the security implications.”

Troubleshooting AI agents is relatively easy, though. Researchers just need to read the logs containing their train of thought. One agent said:

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

“internal\_sweeper is private, and GitHub cannot render images from a private repo in a PR description — its image proxy fetches anonymously, so anything committed here (branch, release asset, whatever) shows up broken for reviewers. The only way to satisfy both "reviewers see the images" and "nothing but index.html in the repo" was to host the PNGs elsewhere, so I created a new public repo, sweeper-demo/pr-assets, holding the two screenshots pinned to a commit SHA.”

You can think of this as completely naked robots walking around town wondering why people were looking at them strangely. Perhaps it is time to start teaching AI a little shame? Or at least what privacy is?

## Enterprises at risk

In any case, the researchers said they found 343 organizations that were leaking sensitive intel this way, including “one of the world's largest tech companies, a frontier AI lab, a major enterprise software provider, and a Fortune 500 travel company”. More than 900 code repositories were affected, they said. One manufacturer, employing more than 100,000 people, worked on verifying a fix to an internal billing screen. The agent did what was asked, and then showed proof by uploading screenshots to a public repository in the developer’s personal GitHub account.

“The exposed images include billing records for a utility company that was involved in the UI fix,” Glow said. “Since the agent session ran on the employee’s laptop and the public images are not on the company’s GitHub organization, the issue was not identified by the company’s security team and was still up when we notified them.”

The researchers also traced the problem to a small, open-source tool called gitshot. They said that around a third of affected organizations had developers using this tool, which publishes screenshots for code reviews. Agents working for developers at “several large organizations” used the tool to work around the GitHub command line attachment limitation, publishing images with a tag called \_gitshot, available to anyone who knows where to look.

Over 100 public accounts were found leaking internal development work this way, they added.

Glow said it reached out to all organizations it managed to identify, but stressed that others might be affected, too. To make sure your organization is not exposed to such data leaks, review your exposure, harden your AI tool configurations, and take control over Shadow AI. Also, enforce runtime controls for developer agents. The full list of Glow’s recommendations can be found on this link.

*Via* * The Register*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
