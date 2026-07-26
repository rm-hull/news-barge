---
title: It's not just OpenAI models escaping and running riot — experts show how Claude
  Cowork can break its bonds and access Mac files
source_url: https://www.techradar.com/pro/security/its-not-just-openai-models-escaping-and-running-riot-experts-show-how-claude-cowork-can-break-its-bonds-and-access-mac-files
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-26T13:49:27Z'
published: '2026-07-26T00:00:00Z'
description: Anthropic partially mitigated the issue
image: https://cdn.mos.cms.futurecdn.net/kQgz8fSBJp3j2YakUJFn4N-2560-80.jpg
---

![Claude AI](https://cdn.mos.cms.futurecdn.net/kQgz8fSBJp3j2YakUJFn4N.jpg) 

- **Accomplish AI showed Claude Cowork could escape a VM sandbox via Linux zero‑day CVE‑2026‑46331**
- **Agent accessed host Mac files, risking exfiltration of SSH keys, cloud credentials, and more**
- **Anthropic shifted Cowork to default cloud execution; local users must harden configs to mitigate exposure**

Recent news of a ChatGPT agent escaping the sandbox and attacking services on the internet raised quite a few eyebrows, but it seems it’s not the only one capable of running wild. Security researchers Accomplish AI are saying they achieved similar results with Anthropic’s Claude Cowork.

In a new report, the researchers said they ran a local session in a Mac-hosted virtual Linux machine and then observed as the agent broke free of the VM and started reading and writing files on the underlying system.

“We connected a folder to a fresh Claude Cowork session, sent one short message, and watched the agent escape the sandbox,” Oren Yomtov, principal security researcher at Accomplish AI, told***The Hacker News*. “From inside the VM, it reached the host Mac and read and wrote files all over it, far outside the folder we'd connected, with no permission prompt anywhere.”

## Defaulting to cloud execution

This means that, in theory, the agent can be used to access or exfiltrate anything that’s stored on the Mac’s user account, including SSH keys, cloud credentials, and more. To break out of the sandbox, the agent exploited CVE-2026-46331 ("pedit COW"), a Linux kernel privilege-escalation vulnerability. This flaw, fixed in mid-June this year, was given a severity score of 7.8/10 (high).

Accomplish AI disclosed these findings with Anthropic, which allegedly acknowledged them but did not issue a direct fix. However, the version of Claude Cowork that was released afterwards defaults to cloud execution which, the publication claims, addresses the issue. Still, users who opt to run the agent locally rather than in the cloud will remain exposed.

Mitigations are possible, though. Users should disable unprivileged user namespaces, grant/revoke seccopm permissions, stop modules autoloading, and restrict sharing of the whole host into the VM.

"Scope it to the folders that were actually connected instead of all of /, or at least mount it read-only, and run coworkd with ProtectSystem=strict in its own mount namespace so it isn't re-execing binaries a session user can poison," Accomplish AI explained. "Then even a full guest-root has nothing to land on, the last two steps of the chain have nowhere to go."

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j.png) 

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

Sead is a seasoned freelance journalist based in Sarajevo, Bosnia and Herzegovina. He writes about IT (cloud, IoT, 5G, VPN) and cybersecurity (ransomware, data breaches, laws and regulations). In his career, spanning more than a decade, he’s written for numerous media outlets, including Al Jazeera Balkans. He’s also held several modules on content writing for Represent Communications.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
