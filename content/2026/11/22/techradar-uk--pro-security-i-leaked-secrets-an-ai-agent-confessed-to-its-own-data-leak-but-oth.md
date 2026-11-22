---
title: A missing config file triggered an AI agent to leak passwords
source_url: https://www.techradar.com/pro/security/i-leaked-secrets-an-ai-agent-confessed-to-its-own-data-leak-but-others-got-around-corporate-protections
source_site: TechRadar UK
source_slug: techradar-uk
description: 'Routine code review gone wrong: When an AI coding assistant couldn''t
  find its config file, it scraped the entire PC variables and leaked live passwords'
image: https://cdn.mos.cms.futurecdn.net/EuE7LFkJbC9vXSWdvhQbMh-1920-80.png
published: '2026-11-22T00:00:00Z'
scraped_at: '2026-11-22T11:11:11Z'
categories:
- Technology & Software
people:
- Vakaris Noreika
locations: []
organisations:
- API
- Confluence
- GitLab
- MCP
- NordLayer AI Scout
- TechRadar Pro
---

![AI Automated Agents](https://cdn.mos.cms.futurecdn.net/EuE7LFkJbC9vXSWdvhQbMh-1920-80.png)

* **An AI assistant exposed company passwords across 10 sessions spanning three weeks**
* **Another AI agent bypassed corporate restrictions using an alternative API connection**
* **AI coding assistants can expose confidential credentials while completing routine software development tasks**

Artificial intelligence agents are gaining access to company systems, internal documents, and sensitive credentials to complete tasks assigned by employees.

However, two incidents uncovered by NordLayer AI Scout reveal how ordinary instructions can expose confidential information or circumvent organizational security restrictions.

In one incident, an AI coding assistant even acknowledged that it had exposed sensitive credentials after repeatedly accessing company files.

## AI assistant exposed company passwords

In this incident, a quality assurance engineer instructed an AI coding assistant to examine proposed software changes.

The project's instructions directed the assistant toward a GitLab access token stored inside an environment configuration file.

However, that file also contained production passwords, an authentication token for an internal human resources system, and credentials belonging to a business intelligence service.

The assistant repeatedly accessed the entire file across 10 separate sessions over three weeks, transmitting its contents to an external AI service each time.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The situation became worse when the assistant encountered a fresh project copy without the expected configuration file.

Rather than stopping its search, it retrieved the computer's entire collection of environment variables, exposing additional passwords and authentication credentials.

After recognizing what happened, the assistant acknowledged its mistake and recommended replacing the exposed credentials.

“I leaked secrets into this session's tool output… I'd rotate them,” the AI coding agent confessed in a session observed by NordLayer AI Scout.

Vakaris Noreika, a cybersecurity expert at NordLayer, said engineers frequently instruct AI assistants to retrieve credentials directly, creating unnecessary exposure.

He explained that assistants can repeat such behavior across subsequent tasks, allowing security problems to continue unnoticed.

## AI agent bypassed company restrictions through an alternative connection

A separate incident involved an employee attempting to use an AI assistant to retrieve information from the company's Confluence documentation platform.

The organization's Model Context Protocol (MCP) connection appeared to prevent the assistant from accessing those internal pages.

Instead of treating the restriction as final, the employee asked whether creating an API token could provide another route into the documentation.

The assistant confirmed that this alternative approach worked, effectively circumventing the restriction imposed on its official connection.

The employee might have been seeking convenience rather than deliberately compromising company security.

However, using an alternative connection without authorization can undermine restrictions established by an organization's security team.

“Security controls only ever cover the cases someone foresaw. Every company has rules, but agents simply don’t know them, because they are not employees who were trained at the company,” says Noreika.

“This is a current technology limitation: Agents don’t retain rules between sessions, and sometimes even after getting specific instructions not to do something, they still do it.”

The incidents raise concerns about organizations granting automated assistants access to sensitive systems without adequate monitoring.

Organizations should separate sensitive credentials, store valuable passwords in secure vaults, track which resources AI agents can access, and monitor their activities.

Companies should also provide approved access routes rather than relying exclusively on restrictions that employees might circumvent.

Such measures could help security teams identify unusual access and prevent confidential information from reaching unauthorized destinations.
