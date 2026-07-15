---
title: '‘A candidate who was hostile from day one never produces that baseline’: Nation
  states spies applying for legit jobs are hard to spot'
source_url: https://www.techradar.com/pro/security/a-candidate-who-was-hostile-from-day-one-never-produces-that-baseline-nation-states-spies-applying-for-legit-jobs-are-hard-to-spot
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-07-15T19:09:05Z'
published: '2026-07-15T00:00:00Z'
description: Nation states are infiltrating intelligence organizations as fake employees
image: https://cdn.mos.cms.futurecdn.net/mdjvPqJZZunuCQDrfEuBFM-2560-80.jpg
---

![A hooded figure in front of a laptop. Digital symbols obscure his face and appear to be pouring out of his head](https://cdn.mos.cms.futurecdn.net/mdjvPqJZZunuCQDrfEuBFM.jpg) 

Geopolitical tensions are mounting, and nation states are employing new types of strategies to gain intelligence. A recent Five Eyes warning, for example, accused Chinese military intelligence officers of using professional networking sites and online job platforms to target individuals of interest.

In this specific case, the agents pose as recruiters advertising seemingly legitimate work to build relationships and, ultimately, get their hands on non-public information. Popular sites like LinkedIn, Indeed and Upwork have all seen this new type of attack take place.

At the same time, a parallel threat sees operatives applying for jobs within trusted organizations with access to intelligence, creating insider threats that experts warn AI might be mostly responsible for.

Generative AI, for example, can create documents, write applications and even supply live answers during real-time remote interviews, meaning that a small group of fake applicants can extend their reach much more quickly.

## Rather than attacking existing workers, nation states are creating their own job candidates

Once inside an organization and with access to company tools like PCs, emails and other internal systems, nation state spies can then move laterally to acquire the information they sought.

Security experts at Exabeam warn that, because this technique is still evolving, it might not always be so easy to spot. Additionally, motives can differ, with Chinese intelligence operations typically seeking military, political or economic information. North Korean agents, on the other hand, tend to be tied to stealing money, which could also come with the side effect of data and intelligence theft.

Exabeam even observed this type of attack first-hand, when a North Korean-affiliated applicant used a false identity to apply for a job at the company. After passing technical tests, a video interview and other standard checks, the suspect’s laptop was quickly flagged for unusual activity.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

In the following Q&A with AI Strategy and Security Research VP Steve Povolny, I discuss these new types of attacks, who’s responsible for stamping them out and what we can do to prevent similar incidents from happening more commonly.

- **The Five Eyes alliance recently warned that foreign intelligence groups are using job platforms to recruit insiders. How significant is this threat, and what is driving its growth?**

This is among the most serious access-driven threats facing cleared workers, and it keeps growing because the economics now favor the attacker.

Foreign intelligence services no longer need handlers and dead drops when they can post a job ad on LinkedIn or Upwork and let candidates self-select based on the access listed in their own resumes. Generative AI lets them run thousands of these conversations at once, drafting outreach and scoring which applicants sit closest to sensitive information without a trained officer.

The Five Eyes alert describes a scaled, automated funnel, and that scale is what makes it dangerous.

- **A parallel risk runs alongside that warning: adversaries who secure employment directly rather than recruiting an existing employee. Which scenario presents the greater defensive challenge, and why?**

The infiltration model gives defenders less to work with, which makes it the harder problem. When an adversary recruits someone already on staff, most of the suspicious behavior happens outside the company on platforms the employer never sees, yet the insider remains a known person with a verified identity and a real history.

When the adversary becomes the employee, the company has onboarded a fabricated person and handed them a laptop and standing network access on day one. No behavioral baseline exists, since everything that account does counts as a first. The deception also clears the controls most organizations trust, so the failure lands before any security tool gets a vote.

- **Exabeam identified a North Korea-affiliated individual who gained employment at the company. How did the operative clear Exabeam's hiring process, and what first signaled that something was wrong?**

He cleared it by performing well on the parts we test and forging the parts we verify. Applying under the alias Trevor Rothluebber, he aced the technical interview and take-home assessment, passed the video interview and cleared our standard pre-employment process including the background check and I-9 validation.

Our hiring team flagged a suspicion that he leaned on generative AI for live help during the video call, the first soft signal. The hard signal arrived the moment he logged into his corporate account. Our threat intelligence feed matched his username to activity previously associated with North Korean operatives and rated it high risk, and that single match reframed how the team read everything that followed.

Simultaneously, Exabeam’s platform detected a number of anomalies inconsistent with a brand new employee’s first day, and escalating in severity within hours. Incident response quietly isolated and reimaged his laptop before any real damage could be done.

- **The candidate completed applications, interviews and assigned work without raising alarm. In retrospect, what indicators were present, and why did standard screening miss them?**

The indicators existed, but they lived in places our screening was never built to read. The driver's license he submitted was either AI-generated or very badly manually modified, and the tell was physical. The image had unique aberrations, such as the ears in the photo which had an unnatural and pixelated modification an artifact that image generators still produce, and a reviewer skims past.

The live AI assistance during the interview was another, since his answers carried a fluency that did not match the natural hesitation you expect when someone reasons through an unfamiliar problem. Standard screening missed all of it because background checks and identity validation confirm whether documents are internally consistent and whether a record exists, and they never ask whether the human attached to those documents is real.

Further fabrication of documents such as I-9 were missed by a 3rd party identity verification company, and validation of (fake) job references was not properly identified.

- **How did AI contribute to the deception? What did the fraudulent documentation involve, and what capabilities does AI introduce that traditional forgery methods lack?**

AI showed up at nearly every stage. The fraudulent documentation centered on a forged driver's license we believe was generated rather than physically produced, paired with a stolen identity that gave the paperwork a real history to rest on.

During the interview the candidate appeared to have run an AI copilot feeding him answers in real time, and many of these tools now stay invisible to everyone else on the call even while the candidate shares a screen. What AI adds over traditional forgery is volume and believability together. A skilled forger could always produce one convincing passport, but the craft capped how many operations could run at once.

Generative tools remove that ceiling, so a single actor can fabricate convincing documents and coach themselves through a live technical interview across dozens of applications at once, and the forgery stopped being the bottleneck it used to be.

- **The Five Eyes warning focused on China, while the Exabeam case involved North Korea. Do these actors share tactics and objectives, or do they represent distinct operational models that overlap on method?**

They overlap heavily on method while running on different motives, which defenders should sit with. The Chinese operation the Five Eyes described aims at intelligence collection, pulling government and military insight out of people who already hold access.

The North Korean program that hit us and so many others in this industry is funded differently, since much of its purpose is revenue for a sanctioned regime, with intrusion and theft riding alongside the paycheck. The objectives diverge, yet the tradecraft has converged on one toolkit of fabricated identities, AI-assisted documents, manufactured professional histories and the patient relationship-building that lets an operative stay quiet.

When two adversaries with separate goals reach the same playbook, that tells you the playbook works and other actors are already watching.

- **Conventional insider threat programs are built to detect employees who become compromised over time. How should organizations identify a candidate who was an adversary from the point of hire?**

Our mindset must shift toward treating the moment of hire as the start of the highest-risk window rather than the end of vetting. Traditional insider programs watch for drift, the employee who gradually turns after a financial shock or a grievance, so they depend on a baseline built over months.

A candidate who was hostile from day one never produces that baseline, which forces you to scrutinize the earliest behavior most closely. In our case, the catch came from putting new accounts under enhanced monitoring and letting an AI agent correlate scattered signals that no single alert would have justified escalating.

The working principle is to give hiring workflows and new-hire activity the same suspicion you already apply to production access.

- **Where should accountability for this threat reside within an organization? Is it a security function, an HR function, or a gap that persists because ownership is unclear?**

Accountability most often lives in the gap right now, and that gap is exactly why the threat works. Hiring sits with HR and talent acquisition, who are measured on filling roles quickly and are not equipped to run identity verification at an intelligence-grade level.

Detection sits with security, which usually gains no visibility into a candidate until that person already holds a badge and a laptop, and the adversary exploits the seam between the two.

The workable answer is shared ownership with a clean handoff, where security sets the identity and behavioral standards hiring must meet and stays involved through the first weeks of employment rather than inheriting the problem once onboarding closes.

- **Many mid-sized companies lack dedicated threat intelligence resources. What practical measures can such organizations implement to reduce their exposure?**

Useful defense does not require a dedicated threat intelligence team. The interview itself is the cheapest control available, and small changes make it far more revealing.

Underspecifying a problem on purpose shows whether a candidate asks clarifying questions like a real engineer or simply produces a confident answer and switching the problem partway through tests whether they adapt or whether something is feeding them responses.

Asking for an external webcam that shows the workspace instead of a shared screen removes one of the easiest hiding spots for an interview copilot. Beyond hiring, the highest-leverage move is placing every new employee on a watchlist for closer monitoring through their first weeks, which costs configuration time rather than budget.

Even a basic, low-cost threat intelligence feed would have surfaced the username match that broke our case open.

- **What is the most contested prediction on this issue, one that many security leaders would currently dispute?**

My contested prediction is that within a couple of years the verified human interview, run live and in person for any role with meaningful access, returns as a security requirement. Many security leaders will fight that because it breaks the remote-first hiring model they spent years optimizing.

The objection I expect is that it does not scale and shrinks the talent pool, and those concerns are legitimate. My counter is that the economics have already flipped for high-access roles, since the cost of onboarding a single fabricated adversary now dwarfs the friction of one in-person verification step.

The deeper claim underneath it is that remote identity verification as we practice it today is no longer reliable for sensitive positions, and AI is what made it unreliable. Most security leaders are not ready to say that out loud yet.

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


*Follow TechRadar on Google News* and



**add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Desire Athow](https://cdn.mos.cms.futurecdn.net/oEw3XiohQwun9z7gMxKzkB.jpg)

Désiré has been musing and writing about technology during a career spanning four decades. He dabbled in website builders and web hosting when DHTML and frames were in vogue and started narrating about the impact of technology on society just before the start of the Y2K hysteria at the turn of the last millennium.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
