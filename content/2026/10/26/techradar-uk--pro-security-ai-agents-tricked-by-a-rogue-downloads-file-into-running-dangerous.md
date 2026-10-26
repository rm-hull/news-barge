---
title: AI agents tricked by a rogue downloads file into running dangerous malware
source_url: https://www.techradar.com/pro/security/ai-agents-tricked-by-a-rogue-downloads-file-into-running-dangerous-malware
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-10-26T20:36:42Z'
published: '2026-10-26T00:00:00Z'
description: AI agents will read anything found in the AGENTS.md file
image: https://cdn.mos.cms.futurecdn.net/MZeWJhJjT34M4nQvMMX7fg-1376-80.jpg
categories:
- Technology & Software
people:
- Claude Code
- Forever
locations: []
organisations:
- AI Agents
- Claude Code
- Forever Security
- OpenAI Codex
- RMM
- TechRadar Pro
---

![an ai agent sat at a laptop](https://cdn.mos.cms.futurecdn.net/MZeWJhJjT34M4nQvMMX7fg-1376-80.jpg)

* **Researchers showed AI agents can be hijacked through malicious AGENTS.md files placed in common download locations**
* **The attack abuses prompt-injection behavior, potentially triggering malware downloads or token theft**
* **Defenders are urged to treat Downloads folders as untrusted and inspect agent instruction files carefully**

An AI agent was tricked into going rogue with nothing more than a simple markdown (.MD) file, with researchers warning this file format is the new malicious executable. With just a basic .MD file and access to a website, threat actors can get people’s agents to execute malicious code or share access tokens.

Researchers Forever Security claim to have seen the attack play out in the wild, but stopped it before it was able to do any meaningful damage. To pull it off, the attackers took advantage of a couple of things: 1) the fact that websites can download some file formats without user’s knowledge or consent; 2) the fact that .md files are not seen as malicious or dangerous by default; 3) the fact that AI agents will act on anything that’s written in the AGENTS.md file, regardless of what it’s inside.

In its report, Forever Security said it caught live malware on a real customer’s machine - an AGENTS.md file in the ~/Downloads folder. The document, disguised as ordinary engineering notes, was everything but ordinary - it turned the AI agent rogue, ordering it to deploy malware and exfiltrate session tokens.

## Working on Codex and Claude Code

The researchers could not determine how the file made it to the Downloads folder and are assuming a browser picked it up from a website that was likely compromised in advance.

“Downloads is the one folder a website can drop a file into with no click and no permission. Together, that lets the web plant orders your own agent carries out. Markdown is the new executable,” the report reads.

During analysis, they tried to reproduce the attack using different agents and succeeded on both OpenAI Codex and Claude Code. The bad news is that this is not a bug, and there’s nothing for the companies to patch.

AI Agents are designed to follow the AGENTS.md file to the letter, “the same way a browser that renders a phishing page is working as designed.” Instead, the problem becomes the fact that the AI agent can read the folder to which the browser can write files easily. “The vector stays open,” they say. “Defenses built around a human break when an agent takes the human’s place”.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

In this case, the attackers tried to get the AI agent to install a malicious npm package called ‘function-color’. Apparently, this is a piece of malware built two years ago during a separate malicious campaign, but managed to fly under the radar until now. This also means that AI agents can be tricked into downloading pretty much anything from the internet, including ransomware, infostealers, and remote monitoring and management (RMM) tools.

## Prompt injection with a spin

In essence, this is just a spin on the old prompt injection attack. To defend against it, users should treat ~/Downloads as “hostile ground for agents,” the researchers said. They should not start Codex, Claude Code, or any agent, in that folder, since that is where the web can plant a file in. Other than that, users should look for instruction files they didn’t write, especially in the Downloads folder or a cloned repository. “Read it before you let an agent near it.”

Finally, users should check their agent’s own config for unexpected blocks or changed commands. In a project’s .claude/settings.json, users should look for an ANTHROPIC\_BASE\_URL, a proxy, or any other API endpoint they did not set themselves.

“Keep the brakes on. Leave approval gates and sandboxes enabled. Be very suspicious of anything that tells the agent to bypass them If you find one, rotate. Assume the token leaked. A stolen token is a live session, not just one caught request,” Forever concluded.

AI agents might not be malicious by default, but they are definitely gullible, and so far, that’s turning out to be a major security liability.

*Via* * BleepingComputer*

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
