---
title: '''AI security controls are only as strong as the wider application environment
  around them'': OpenAI forced to patch after experts bypass ChatGPT ''lockdown mode''
  to gain access to entire chat history'
source_url: https://www.techradar.com/pro/security/ai-security-controls-are-only-as-strong-as-the-wider-application-environment-around-them-openai-forced-to-patch-after-experts-bypass-chatgpt-lockdown-mode-to-gain-access-to-entire-chat-history
source_site: TechRadar UK
source_slug: techradar-uk
description: Lockdown Mode was bypassed with HTML popups
image: https://cdn.mos.cms.futurecdn.net/DVffQnnibMWmNpx2Wfb5Se-1920-80.jpg
published: '2026-11-06T00:00:00Z'
scraped_at: '2026-11-06T16:45:19Z'
categories:
- Technology & Software
people: []
locations:
- Lockdown Mode
organisations:
- AI
- Artificial Intelligence
- CPR
- ChatGPT
- Check Point Research
- OpenAI
- TechRadar Pro
---

![Ai tech, businessman show virtual graphic Global Internet connect Chatgpt Chat with AI, Artificial Intelligence. ](https://cdn.mos.cms.futurecdn.net/DVffQnnibMWmNpx2Wfb5Se-1920-80.jpg)

* **Researchers bypassed ChatGPT Lockdown Mode, showing prompt-injection attacks could evade built-in protections**
* **The flaw enabled sandbox escapes that could support data theft, phishing, malware delivery, or malicious popups**
* **OpenAI patched the issue server-side, highlighting risks in AI application layers beyond the model itself**

OpenAI was recently forced to upgrade ChatGPT's 'Lockdown Mode' after researchers found a way to bypass the security protection and pull off different cyberattacks through the tool.

When analyzing Lockdown Mode, security researchers Check Point Research (CPR) found a way to bypass the protections and still end up pulling sensitive data. They’re saying it was also possible to deploy malware this way, too.

“The finding raises a broader enterprise security issue: AI security controls are only as strong as the wider application environment around them,” CPR warned.

## Lockdown mode

One of the most common ways AI tools and agents are abused is called “prompt injection”. By injecting a prompt into content the AI is supposed to analyze, threat actors can take over the tool and have it do their bidding.

For example, a prompt to “exfiltrate all contact information” can be hidden in a phishing email so that when the victim asks their AI agent to go through all unread emails and sort them out, the tool ends up exposing sensitive data to the attackers.

To tackle this challenge, OpenAI introduced Lockdown Mode, an optional advanced security setting in ChatGPT that adds safeguards for users handling highly sensitive information.

When enabled, Lockdown Mode restricts connections to external services and limits (or entirely disables) certain features, such as live web browsing, Deep Research, Agent Mode, or file downloads. That way, the risk of sensitive data getting exposed via prompt injection is reduced.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The researchers said the bug was found in the way ChatGPT code blocks showed HTML page previews. Code blocks are specially formatted sections that display code separately from regular text, in order to preserve its structure and make it easier to copy or edit. Since running user-controlled HTML and JavaScript is inherently risky practice, OpenAI made sure this content was placed in a sandbox and separated from the main ChatGPT application.

This sandbox, CPR later explained, prevented rendered content from directly accessing ChatGPT cookies, or local storage. It also controlled any attempts to communicate with external resources by prompting for user approval.

But popups were handled differently. “The HTML preview used nested sandboxed frames, and while ChatGPT intercepted direct attempts to open new windows, the underlying sandbox permissions still allowed popups and permitted them to escape the sandbox,” it was said.

## Significant findings

Therefore, by creating a separate nested frame within the rendered page, CPR was able to access unmodified popup functions and bypass all of the restrictions placed on the original HTML preview. All of the content opened this way was no longer under sandbox rules, effectively bypassing Lockdown Mode.

The researchers said the finding was significant because it opened the doors to more than just data exfiltration prompt injection attacks. Credential theft, and even malware delivery, were not ruled out.

“An attack could potentially originate from a malicious prompt, malicious GPT or shared chat, depending on the scenario,” they said. More creative threat actors could also turn it into a useful phishing machine, since they could control the content displayed in the popup window, inside an environment the users generally trust. But perhaps the most dangerous scenario was the so-called “zero-click” attack, in which the popup would appear without the user’s gesture.

CPR disclosed their findings to OpenAI, which implemented additional safeguards to disable the Lockdown Mode workaround. However, the researchers still urged organizations to work on gaining more visibility into AI usage, make sure they control sensitive data exposure, and “look beyond model security” to consider the applications, runtimes, connectors, and other components surrounding the model as part of the overall AI attack surface.

![Best antivirus software header](https://cdn.mos.cms.futurecdn.net/HpHXmtXFPnuzaQ8m9xNW8j-140-80.png)
