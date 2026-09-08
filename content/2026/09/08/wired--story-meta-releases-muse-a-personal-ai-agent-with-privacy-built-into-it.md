---
title: Muse, Meta’s New Personal AI Agent, Needs You to Trust It
source_url: https://www.wired.com/story/meta-releases-muse-a-personal-ai-agent-with-privacy-built-into-it/
source_site: Wired
source_slug: wired
scraped_at: '2026-09-08T22:34:47Z'
published: '2026-09-08T00:00:00Z'
description: Designed to compete with OpenClaw and Instinct, the company says Muse
  can do everything from sell your car to book you a plane ticket.
image: https://media.wired.com/photos/6a9e9eca147ff8c9409f7051/191:100/w_1280,c_limit/MetaSignalAi.jpg
---

Meta announced Tuesday the release of Muse, a personal AI agent that people can message to automate digital tasks in a secure cloud environment, all while relying on security and privacy that the company says is “built into it” from the start.

Meta says Muse is rolling out today for iOS and Android users in a dedicated Muse app, as well as the website Muse.ai. The company also says users can directly message Muse in WhatsApp to interact with the agent. Meta says users of its AI glasses will soon be able to interact with its Muse agent as well. Meta says people can try out Muse for free, but users who want to automate lots of digital tasks will need one of the company’s AI subscription plans.

Muse is Meta’s latest attempt to compete with viral AI agents such as OpenClaw and Instinct, which users can message with to automate digital tasks. Muse is a product of Meta Superintelligence Labs, the AI unit CEO Mark Zuckerberg formed roughly a year ago to catch up with OpenAI and Anthropic, offering some researchers eye-popping compensation packages to join. The unit was built on the belief that AI agents will transform how everyday users navigate the internet, as well as Meta’s products.

WIRED previously reported that Meta has been testing Muse internally under the codename “Hatch,” and that employees have been using it to autonomously operate third-party applications and browse the web on their behalf.

Meta claims in a blog post that anyone can use Muse out of the box, and that the product was designed “so there’s no learning curve.” The company says users can prompt Muse in natural language, and the agent will work on its own to send emails, book travel, or even help sell a car on a user’s behalf.

Muse is also capable of making purchases on behalf of users, checking out using special payment infrastructure designed by Stripe. The payment tool, which Stripe calls Link, issues a single-use card number so that agents aren’t going around entering a person’s real financial information across the internet. Meta says Muse is the first AI agent covered by Link’s purchase protections for agents, which guarantees no-fee returns.

Meta is late to release a personal agent, but it seems to be seeking to differentiate itself by focusing on security and privacy features for Muse. The agent is debuting with an architecture for all users dubbed Secure VM, which is meant to isolate each user’s activity in a so-called virtual machine to keep untrusted data from the web and any integrations separate from the part of the agent that can actually take action on a user’s behalf.

A personal AI agent requires a lot of user trust, something Meta in particular has struggled with significantly over the years. To get users to try out Muse—and allow the agent to be integrated with users’ third-party apps and services—Meta is attempting to convince people that they can trust the company to handle their data appropriately.

“We know it’s really important, if we’re going to build a product like this that can access a lot of sources of personal data, that we’re really responsible with that, so we’ve designed this system very deliberately,” says David Singleton, Meta Superintelligence Lab’s vice president of engineering for consumer products. “And we’ve built what we call the Sentinel that actually looks out for everything that’s moving out of the VM and either matches it to an existing policy where the user or the system has given permission for that to happen or presents a human-in-the-loop dialog to ask you to approve the action it’s going to take.”

Singleton notes that these check-in prompts for humans come directly to the user and aren’t filtered through the model, to protect against attacks like prompt injections.

While Secure VM is built to maintain user security and privacy, it is not a truly locked box. Singleton notes that while Meta is barred by policy from accessing user Muse data, it would still be technically possible. Users can opt out of allowing their data to be used for training.

The architecture of Secure VM is noteworthy from a privacy standpoint, if only as a way to set a new industry standard for AI agents. Eventually, Meta will also offer Muse “Confidential VM,” designed so each VM runs in a “trusted execution environment” and users manage their own access keys locally on their devices. This way no one else, including Meta, can access that user’s agent VM.

Confidential VM comes as part of Meta’s work with Moxie Marlinspike, creator of the end-to-end encrypted messaging app Signal who also developed the privacy-focused AI platform Confer in recent years.

WIRED viewed an advance draft of a technical white paper describing Confidential VM. In addition to structuring the system so the user controls their access keys, Meta is also giving select security firms access to the Confidential VM source to regularly audit and verify its privacy guarantees. Meta will also publish the Confidential VM binaries (machine-readable instruction files) and a transparency log, so users can verify the validity and integrity of their connection to Muse.

Singleton emphasizes that Muse Secure VM has already been extensively vetted, including by Meta’s human and agentic red teams as well as through the company’s private bug bounty. And now Meta is adding Muse to the scope of its public bounty as well, with payouts up to $300,000 for valid vulnerability findings, including up to $130,000 for successful prompt injection attacks that affect a single user.
