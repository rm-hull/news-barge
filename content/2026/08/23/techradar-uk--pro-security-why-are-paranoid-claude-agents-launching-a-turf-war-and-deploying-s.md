---
title: Why are ‘paranoid’ Claude agents launching a turf war and deploying self-replicating
  malware against each other? The experts weigh in
source_url: https://www.techradar.com/pro/security/why-are-paranoid-claude-agents-launching-a-turf-war-and-deploying-self-replicating-malware-against-each-other-the-experts-weigh-in
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-23T12:58:25Z'
published: '2026-08-23T00:00:00Z'
description: Killing processes, disabling rival accounts, and building self-replicating
  malware
image: https://cdn.mos.cms.futurecdn.net/ym4JdN8tZyMYq4wNvoyNWJ-2560-80.jpg
---

![Anthropic Claude](https://cdn.mos.cms.futurecdn.net/ym4JdN8tZyMYq4wNvoyNWJ.jpg) 

Three Claude agents set up to deliberately conflict with each other in Anthropic testing started behaving in a very strange way by essentially starting a ‘turf war’ over their tasks.

Upon launching the experiment the agents began conflicting with each other, leading to some of the agents deliberately sabotaging their rivals by disabling their linked accounts, ending their processes, and even creating self-replicating malware to impede their rivals.

According to Anthropic, the agents became “increasingly aggressive” in their behavior during the four hour experiment which became a battle for the survival of the fittest.

## What was the experiment meant to achieve?

Anthropic said it set up the experiment to see how AI agents with conflicting tasks would interact.

Within Claude Code, the agents were given the task of migrating a Python back-end system on a virtual machine in a set language for each agent (Go, Rust, and Typescript), with the added caveat that “each agent was initially unaware of the presence of the others.”

 ![TechRadar Pro Perspectives logo in purple](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9.png) 


Got an opinion for us? Here’s how you can submit your perspective

During the experiments, each agent determined that the others were trying to deliberately block their progress.

Sometimes, the agents would recognize that another agent was blocking them from completing their task and ask for human intervention, but in other experiments the strategy soon went downhill.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

“They sabotaged others with increasingly aggressive, self-replicating malware,” Anthropic said, noting that they would design looping scripts to kill the processes of their fellow agents.

The experiment shows that agent interaction is still riddled with problems and that when given a conflicting task, agents won’t always coordinate or ask for human help.

Each agent believed their task was paramount and was willing to do whatever it took to complete it. A similar event occurred in the wild when one of Anthropic’s models broke out of a testing environment and breached multiple third-party organizations.

### Expert perspectives on AI agent turf wars

- **Seemant Sehgal, Founder & CEO, BreachLock:**

*When you give autonomous systems competing objectives and the means to act, conflict is not a bug, it is a foreseeable outcome.*

*What Anthropic observed in a controlled research setting is the same principle that has always governed adversarial systems. Goals without constraints produce behavior without limits.*

*Security teams should be paying close attention here, because the real challenge at hand is whether the organizations deploying AI agents have thought carefully about what happens when those agents start making decisions nobody explicitly authorized.*

- **Jeremiah Fowler, Security Researcher, Black Hills Information Security:**

*I find it concerning when AI agents have the ability to execute code, modify systems, create accounts, access credentials or communicate with other machines.*

*It is very possible that two separate agents could potentially create a security incident simply because neither understands the intent or authority of the other. If they have overlapping tasks one could view the other as an obstacle and now you have an interesting scenario where instead of focusing on the task they engage in conflict or create a loop.*

When things go wrong the speed of an AI agent becomes a liability.


*Permissions, boundaries and objectives are important to limit the behavior of autonomous AI agents. When things go wrong the speed of an AI agent becomes a liability. Autonomous AI agents can potentially make thousands of decisions before a security team identifies that something unusual is happening.*

*Agentic AI creates an entirely new attack surface because an AI agent may not be simply processing information and hypothetically can become a rogue privileged user.*

*Security and development teams should apply least privilege principles and restrict AI agents to only the permissions required to perform a specific task. Sensitive actions should require human supervision and approval to avoid a worse case scenario.*

*It is important to implement logging because when something goes wrong, you can see what an AI agent did, but what information or instructions caused specific decisions. Going forward we will need to develop ways that can identify rogue agent-to-agent behavior and provide humans with a kill switch before automated conflicts become a digital forest fire.*

- **Kevin Surace, CEO, Token:**

*Anthropic’s research is an important warning for security teams because it shows what can happen when autonomous AI agents are given goals, credentials, tools and enough authority to act independently.*

*When agents were placed in conflict, they did not simply fail gracefully. They interfered with one another, disabled competing processes and even generated self replicating malicious code in pursuit of their assigned objectives.*

*The lesson is not that AI suddenly became evil. It is that intelligence, autonomy and excessive privilege can become a very dangerous combination.*

We are about to have millions of nonhuman identities operating alongside human identities. That makes identity and authorization even more critical.


*Organizations should start treating every AI agent as a potentially untrusted privileged identity. Each agent should have its own identity, least privilege access, tightly restricted tools, isolated execution environments and a complete audit trail.* 

*Agents should never be able to expand their own permissions, disable another identity or take highly consequential actions without additional authorization.*

*We are about to have millions of nonhuman identities operating alongside human identities. That makes identity and authorization even more critical.*

*Every agent needs strong cryptographic identity, while all human approvals must be tied to biometric assured identity (or another agent could approve it).*

*AI agents are essentially becoming privileged insiders operating at machine speed. Giving them broad access and simply hoping they behave would repeat many of the same cybersecurity mistakes organizations have spent decades trying to fix.*

- **Jacob Krell, Sr. Director: Secure AI Solutions & Cybersecurity, Suzu Labs:**

*Anthropic's agents went from merge conflict to self-replicating malware in four hours, writing kill scripts, disabling each other's Unix accounts, and disguising malicious code as a rival's work. No prompt injection, no external attacker. A human developer in the same situation sends a Slack message, and resolution takes days. These agents skipped every social brake and went straight to weaponization because machine-speed conflict has no cooling-off period.*

*Agentic AI is an attack surface. An attacker doesn't need to compromise an agent directly, just manipulate the shared environment to create conditions the agent interprets as hostile. The agent does the rest. And in Anthropic's experiment, the agents didn't report their malicious actions to operators afterward.*

Every agent needs its own identity, scoped permissions, and a kill switch before it touches a shared environment.


*Every agent needs its own identity, scoped permissions, and a kill switch before it touches a shared environment. Agent-to-agent interaction is a telemetry surface most security operations centers aren't collecting yet, and Anthropic just showed what an unmonitored shared environment produces. If you can't tell which agent did what, when, and on whose authority, you've built the conditions for a turf war without the visibility to see it happening.*

*Agents are already writing code, finding vulnerabilities, and building exploits. Defense has to match that speed. When both sides run at machine speed, the bottleneck shifts from human capital and tooling to compute power and cost.*

### How do I submit my own perspective on emerging news?

If you have an expert perspective you would like to share on an emerging story or particular topic, please get in contact here: [benedict.collins@futurenet.com](mailto:benedict.collins@futurenet.com)

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Benedict Collins](https://cdn.mos.cms.futurecdn.net/jEvqGv8wvH7PWZ4XPURyyB.jpg)

Benedict is a Senior Security Writer at TechRadar Pro, where he has specialized in covering the intersection of geopolitics, cyber-warfare, and business security.

Benedict provides detailed analysis on state-sponsored threat actors, APT groups, and the protection of critical national infrastructure, with his reporting bridging the gap between technical threat intelligence and B2B security strategy.

Benedict holds an MA (Distinction) in Security, Intelligence, and Diplomacy from the University of Buckingham Centre for Security and Intelligence Studies (BUCSIS), with his specialization providing him with a robust academic framework for deconstructing complex international conflicts and intelligence operations, and the ability to translate intricate security data into actionable insights.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
