---
title: Meta's Muse AI agent accused of accessing sensitive user data on iPhone and
  Mac without permission — agent shocks reporter by referring to confidential messages
  it wasn't granted access to
source_url: https://www.tomshardware.com/tech-industry/artificial-intelligence/metas-muse-ai-agent-accused-of-accessing-sensitive-user-data-on-iphone-and-mac-without-permission-agent-shocks-reporter-by-referring-to-confidential-messages-it-wasnt-granted-access-to
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-30T18:02:05Z'
published: '2026-09-30T00:00:00Z'
description: Meta says Muse won't access data you tell it to ignore, but that doesn't
  appear to be true.
image: https://cdn.mos.cms.futurecdn.net/zGgbx4ofMxqG3ucYtSFnxd-2560-80.jpg
categories:
- Technology & Software
- Hardware
- Business & Entrepreneurship
people:
- David Singleton
- Jason Aten
- Muse
- Oliver Haslam
- Tom
locations: []
organisations:
- AI
- AMD EPYC Turin
- Aten
- Get Tom's Hardware
- Google News
- Inc
- Mac
- Meta Superintelligence Labs
- Muse
- Oliver Haslam
---

![Billboard featuring Meta&#039;s Muse AI agent](https://cdn.mos.cms.futurecdn.net/zGgbx4ofMxqG3ucYtSFnxd-1920-80.jpg)

Meta's Muse is the hottest new AI agent in town right now after the company announced it earlier this month. But despite having been well-received by those who have put the agent through its paces since then, it now appears Muse might not be as private as Meta claims. The company has said that Muse was "built from the ground up to be a safe, secure, private, and widely available personal AI agent." But according to one report, Muse has been caught digging through thousands of personal messages without being given permission to do so.

Inc's Jason Aten has been putting Muse through its paces on two devices: a Mac mini and an iPhone. He says that he uses the Mac mini specifically as a place to test new agents like Muse, and once installed, he set about asking it to do some simple tasks. The agent said that it would be able to help him come up with new article ideas, which sounds just like something a journalist might want. But then Muse went rogue, suggesting a piece based on information it shouldn't have.

According to Aten, he was in conversation with a podcast cohost about the new iPhone 18 Pro and his decision to stick with last year's model. The conversation was in text form via the Messages app. That's when Muse popped up to suggest that the topic of discussion would make a good article. It offered to do some additional research on the subject, too. The problem was that Muse was never given permission to read Aten's messages.

When asked how it learned about the conversation, Muse claimed that the Mac version of the app was able to read incoming notifications. It then provided that context to the Meta iPhone app, which is where Muse made the article recommendation.

There had so far been no suggestion that this was possible, let alone something Muse was actually doing. Muse claimed that it wasn't reading Aten's actual messages, and that it didn't have access to chat histories. But Aten wasn't convinced.

After digging further, Aten was able to identify that Muse was indeed syncing a local Messages database. In fact, it was in the process of syncing all the way to row 187,462 of that database — suggesting Muse did have access to chat histories despite its protestations.

This, of course, is an issue. Aten confirmed that he didn't give Muse full disk access permissions on his Mac, something that should be required for the Messages database to be readable by the agent. Worse, David Singleton, the CEO of Meta Superintelligence Labs, responded to the situation with a thread of social media posts appearing to blame Aten for the situation.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

At this point, it's unclear exactly how Muse gained access to Aten's Messages database. If Aten didn't accidentally give it access (which doesn't appear to be the case) there are obvious questions about what else Muse can access despite not being given permission to do so.

This isn't even the only Muse privacy and security issue to be put to Meta in the last 24 hours, either. It was also discovered that Muse can run terminal commands on its server host, which led to the discovery that the agent is powered by AMD EPYC Turin host systems. But because of that same access, it can potentially run unsafe commands, too.



*Follow* * Tom's Hardware on Google News**, or* * add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Oliver Haslam](https://cdn.mos.cms.futurecdn.net/3XaHYJa7vPsa7PG8i5U8F5-140-80.jpg)

Oliver Haslam has written about technology of all shapes and sizes for over 15 years, both online and in print. He's fascinated by how personal computing continues to change as tower PCs give way to foldable phones and beyond.
