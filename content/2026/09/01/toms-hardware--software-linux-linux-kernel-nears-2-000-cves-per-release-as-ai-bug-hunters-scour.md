---
title: Linux kernel nears record 2,000 vulnerabilities per release as AI bug hunters
  scour 40 million lines of code — maintainers say they are 'completely overwhelmed'
  by CVE finds
source_url: https://www.tomshardware.com/software/linux/linux-kernel-nears-2-000-cves-per-release-as-ai-bug-hunters-scour-40-million-lines-of-code-maintainers-say-they-are-completely-overwhelmed
source_site: Tom's Hardware
source_slug: toms-hardware
scraped_at: '2026-09-01T13:28:35Z'
published: '2026-09-01T00:00:00Z'
description: Maintenance teams are now fighting AI with AI
image: https://cdn.mos.cms.futurecdn.net/4ZEnSpa7JtJezKZH6YwC5b-1600-80.jpg
---

![Linux logo in front of clocks](https://cdn.mos.cms.futurecdn.net/4ZEnSpa7JtJezKZH6YwC5b.jpg) 

The Linux kernel is approaching a staggering 2,000 CVEs fixed per release, up from roughly 500 through much of the Linux 6.x era, as AI and large language models increasingly scour the operating system’s enormous codebase for vulnerabilities. According to an August 28 Phoronix report, Linux stable maintainer Greg Kroah-Hartman revealed the trend in a slide teasing an upcoming presentation at Kernel Recipes 2026, showing CVE counts jumping above 1,000 with Linux 7.0 and exceeding 1,500 with Linux 7.2. If the current trajectory continues, Linux 7.3 could push the figure beyond 2,000.

Rather than a change in Linux’s security or a rise in vulnerabilities, the spike is mainly due to “detectives” using AI tools to scour the Linux kernel source tree, which has grown to over 40 million lines over 35 years of Linux’s existence. These tools can examine countless obscure sections humans may rarely revisit, occasionally finding genuine defects; Linux CVE records this year already explicitly credit AI-assisted static analysis with finding vulnerabilities subsequently confirmed by Intel Product Security. However, many of the findings have been low-priority vulnerabilities — often within obscure driver code — questionable patches, and outright hallucinations, leaving human maintainers to separate useful work from noise.

This problem already constitutes a nuisance for kernel teams that have to fix these issues. In the Linux 7.3 networking pull request, maintainer Jakub Kicinski estimated that between one-third and one-half of the 648 net-next patches handled during the cycle appeared to be low-priority fixes, clean-ups, or clarifications driven by AI. "We are completely overwhelmed,” Kicinski wrote.

The issue has also led Linux maintainers to question whether decades-old drivers are worth keeping alive. In April, developer Andrew Lunn proposed removing nearly 28,000 lines of legacy networking code covering old ISA and PCMCIA-era hardware. While these drivers historically required little attention because they barely had any users, the AI and fuzzing tools started finding defects that maintainers were obligated to investigate and fix, regardless of whether anyone actually runs the hardware.

Linux 7.3 is removing old SGI and IBM driver code, while other ancient components have also been retired as maintainers reassess whether their compatibility value justifies their new maintenance cost. The FreeVxFS filesystem driver, for example, was removed after its maintainer said the decades-old compatibility code now largely served as fodder for automated bug checkers.

Now, the kernel community is not simply rejecting AI; Kroah-Hartman himself has successfully used locally-running AI-assisted fuzzing tools to uncover kernel bugs. The bone of contention is unverified AI output dumped onto humans for validation. Kroah-Hartman recently barred LLM-generated patches from the kernel’s staging subsystem except for legitimate security fixes, while updated kernel guidance warns that AI-generated reports submitted without human verification can waste maintainer time.

The team has also increasingly had to fight AI with AI. It has now secured access to multiple frontier models to help review patches and filter out hallucinated results, and is considering pushing more routine administrative work onto LLMs in subsequent development cycles. Kroah-Hartman is expected to discuss the trend further at Kernel Recipes, which is slated to run from September 21 to 23 in Paris. Linux 7.3 itself has already entered testing, with Linus Torvalds releasing Linux 7.3-rc1 on August 30 after closing its two-week merge window.

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

  


*Follow**Tom's Hardware on Google News**, or** add us as a preferred source**, to get our latest news, analysis, & reviews in your feeds.*

![Etiido Uko](https://cdn.mos.cms.futurecdn.net/BBrMt7jWtSo2Dc3iKoroyD.jpg)

Etiido Uko is a news contributor for Tom's Hardware covering the latest updates in big tech and the PC industry. He is a mechanical engineer and senior technical writer with over nine years of experience in documentation and reporting. He is deeply passionate about all things engineering and technology, and is an expert in gadgets, manufacturing, robotics, automotive, and aerospace.
