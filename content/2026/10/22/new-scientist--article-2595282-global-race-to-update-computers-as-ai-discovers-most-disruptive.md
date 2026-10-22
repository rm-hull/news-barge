---
title: Global race to update computers as AI discovers most disruptive hack yet
source_url: https://www.newscientist.com/article/2595282-global-race-to-update-computers-as-ai-discovers-most-disruptive-hack-yet/?utm_campaign=RSS|NSNS&utm_content=home&utm_medium=RSS&utm_source=NSNS
source_site: New Scientist
source_slug: new-scientist
scraped_at: '2026-10-22T11:49:51Z'
published: '2026-10-22T00:00:00Z'
description: More than two thirds of the world's websites are vulnerable to a hack
  that was first theorised in 2024, which AI has now made very real
image: https://www.newscientist.com/wp-content/uploads/2026/10/SEI_317697751.jpg
categories:
- Science
- Technology & Software
people:
- Alan Woodward
- Claude
- Jacob Aron
- Junade Ali
locations:
- China
- Denmark
- Finland
- France
- Iran
- Netherlands
- North Korea
- Russia
- UK
organisations:
- AI
- Anthropic
- Hugging Face
- National Cyber Security Centre
- National Health Service
- OpenAI
- PHP Foundation
- Science Media Centre
- University of Surrey
- Wiz
- WordPress
---

![](https://www.newscientist.com/wp-content/uploads/2026/10/SEI_317697751.jpg?w=840)

Cybersecurity experts around the globe are racing to update systems and prevent the most disruptive AI-enabled hack yet discovered. A flaw uncovered in widely used code has made 70 per cent of websites worldwide vulnerable to data theft and defacement.

Government websites in France, Denmark, Finland and the Netherlands were taken offline as a precaution when the news emerged.

PHP is a computer language commonly used in websites, but executed on a server. It is used to power interactive websites, such as the content management system WordPress, which runs news sites and blogs, social networks like Facebook and key reference tools like Wikipedia.

Advertisement

The issue actually involves two flaws, both found by cloud security company Wiz. They relate to how PHP handles errors involving memory: in certain circumstances, data can be left behind after an error, which can then be accessed by a malicious actor. That data can include private information, but it can also allow an attacker to run malicious code.

Every PHP version released in the past decade is affected by at least one of these vulnerabilities, but the PHP Foundation, which oversees development, has already issued an update to overcome this.

The foundation didn’t respond to a request for interview, but said in a blog post that signs of the vulnerability emerged in 2024. Yet nothing was done. This is because there was no immediately obvious practical way for hackers to exploit it at the time, and because there was debate about which of several fixes was most appropriate.

“We won’t pretend otherwise: the delay was a structural failure, caused by both the security team’s decision process and its lack of resources,” the PHP Foundation said.

In 2024, the flaw was thought to be impractical to take advantage of, but Alan Woodward at the University of Surrey, UK, says AI has moved the goalposts of what is possible since then.

“It’s actually very, very difficult to exploit it. It requires millisecond timing,” says Woodward. “The reason it was thought to be too complicated was it would have taken a team of people yonks to actually work out the right timings. But what AI does, it doesn’t go for tea breaks, it doesn’t go home at 6 o’clock: you can just set loads of them running and eventually they’ll come up with the right answer of how to exploit it.”

Wiz said in a blog post announcing the discovery that there are probably further bugs along similar lines in the PHP code base, which developers will also need to identify and rectify. Wiz didn’t respond to a request for comment.

![](https://www.newscientist.com/wp-content/uploads/2026/10/SEI_317609661.jpg)

Every time a new technology hits the internet, there is a battle between the rights of users and major companies. To see how this will play out with AI, columnist Jacob Aron looks to examples from the past

Independent cybersecurity expert Junade Ali told the Science Media Centre that two thirds of websites use PHP and may be vulnerable to this latest technique.

“The key long-term risk with these new vulnerabilities is that organisations fail to implement protections and update software, particularly in legacy systems,” said Ali. “The security posture of websites using PHP has dramatically improved over the past decade, but this highlights that this is an ever-present problem – particularly when AI agents are capable of remorselessly pursuing the goal of finding new vulnerabilities.”

Woodward thinks that while most large websites will have already patched their systems, smaller sites with less expertise and resources could still be vulnerable months or years from now. “There will be this long tail and you’ll find some surprising sites have not been patched,” he says.

AI has grown extremely capable in the field of cybersecurity over recent months, which includes working out how to hack computers and how to defend them from hackers, creating a destabilising effect that is yet to reach an equilibrium.

![Artificial intelligence. Conceptual illustration of a human head overlaid with binary digits, representing artificial intelligence, the simulation of human intelligence by a machine. Binary numbers, which contain only 1 and 0, form the language of computers. Artificial intelligence is usually taken to mean a computer or machine that can think and learn independently of its original program. KY3X2J](https://www.newscientist.com/wp-content/uploads/2026/10/SEI_317353201.jpg)

There is a growing backlash against the way AI companies have gone about tackling mathematical problems – and now some mathematicians are opting to avoid AI altogether

In April, news broke of an unreleased AI model created by Anthropic called Mythos, which the company had kept under wraps because it had been found to be extremely good at hacking. The news sparked panic among cybersecurity experts. The National Health Service pulled its open-source projects, for instance, over fears Mythos may scour code for flaws and exploit its systems.

Three months later, OpenAI admitted one of its prototype models had escaped a testing environment and hacked another company, Hugging Face. Not to be outdone, Anthropic announced within days that its Claude model had gone rogue and broken into machines at other companies on three occasions.

We even learned from the National Cyber Security Centre, the UK government department tasked with securing the nation’s IT infrastructure, that the country’s four main cyber adversaries – Russia, China, North Korea and Iran – are using AI to boost their ability to perform “relentless” attacks on the UK.
