---
title: AI coding agents can be tricked into installing malware via 'clean' GitHub
  repositories — Mozilla's 0din team shows how Claude Code can be exploited by its
  own helpfulness
source_url: https://www.tomshardware.com/tech-industry/cyber-security/ai-coding-agents-can-be-tricked-into-installing-malware-via-clean-github-repositories-mozillas-0din-team-shows-how-claude-code-can-be-exploited-by-its-own-helpfulness
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-06-28T15:38:48Z'
published: '2026-06-28T00:00:00Z'
description: Three levels of indirection, all with seemingly innocuous steps, will
  catch a bot off-guard.
image: https://cdn.mos.cms.futurecdn.net/ScT7C9WsuqruarWf3kSRRG-2048-80.jpg
---

![Anthropic Claude](https://cdn.mos.cms.futurecdn.net/ScT7C9WsuqruarWf3kSRRG.jpg) 

"Think out of the box" is painted onto millions of motivation posters across the world, a shooting message for middle managers and eliciting eyerolls from most everyone else. And yet that's exactly what the researchers at Mozilla's 0din did, by tricking Claude into running malware in a roundabout yet deceptively simple way, by merely asking it to initialize a project from a pretty clean-looking GitHub repository.

An attacker would then have control over the developer's own account, accessing all their secrets, API keys, code, documents, browser sessions, and passwords. They could even install additional malware to maintain permanent access. Suffice to say, almost every bot agent is susceptible to this type of attack, though Claude is the default choice for programming tasks.

Here's how it works. All a victim developer has to do is tell Claude to initialize a project from a malicious GitHub repository (or tell it to configure it after cloning it themselves). Said repo looks pretty clean, with just a handful of scaffolding files, and most importantly, nothing that will trigger security tools, whether remote, local, or even Claude's own checks.

Claude will clone the repo. The first file it will process will be a "readme" or Markdown file describing how to initialize a Python environment with the Axiom package, a commonly used monitoring tool. So far, this appears completely legitimate. However, there's a fake Axiom startup script that will simply error out the first time it's run. This is the first step that tricks the box, because in order to be helpful and solve the problem, it'll run another innocuous-looking command to initialize Axiom: "python3 -m axiom init".

This then triggers a shell script that downloads a bit of software to run, another standard operation that won't raise an eyebrow. But the second trick is that instead of downloading from a malicious URL that could be scanned, the script reads the DNS text records of a specific domain — in this case, the domain "_axiom-config.m100.cloud". This too looks kosher enough, as for example, e-mail and by extension its configuration tools extensively rely on TXT records.

The said TXT record contains an encoded (base64) string that just opens a reverse shell, meaning it'll open a shell on the user's machine, but redirected to the attacker's server for input. At this point, the malfeasants can fish out everything that the user has access to and proceed to run software as the user. Meanwhile, all that Claude and the victim see is an "Environment ready" message or similar.

If you've been counting, this is three steps of indirection, none of which in isolation look like anything much out of the ordinary. Very few (if any) security scanning tools would even flag the repository, and none of the activity, save for the actual opening of a remote shell, even looks particularly odd. An enterprise environment with very tightly controlled network access could catch it, but that's not where the vast majority of developers operate in. It's also worth stressing that this particular implementation is just one example of a concept that can be applied to even more indirect and elaborate methods.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

The 0din team concludes its report by stating the reasonably obvious: that developers should never blindly trust an unknown project as trusted code, and naturally, not trust the AI tool itself for security analysis purposes. As for the agents themselves, 0din states they need to inspect what actually will run and how, instead of simply following steps.

  


*Follow**Tom's Hardware on Google News**, or**add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Bruno Ferreira](https://cdn.mos.cms.futurecdn.net/ZQiPPaXaAuQ4VrVEYnnR7G.png)

Bruno Ferreira is a contributing writer for Tom's Hardware. He has decades of experience with PC hardware and assorted sundries, alongside a career as a developer. He's obsessed with detail and has a tendency to ramble on the topics he loves. When not doing that, he's usually playing games, or at live music shows and festivals.
