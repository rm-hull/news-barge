---
title: 'Manchester Airports hack: Experts weigh in on 8.7M data leak'
source_url: https://www.techradar.com/pro/security/why-did-fulcrumsec-hackers-try-to-extort-manchester-airports-group-and-what-happens-now-the-data-is-leaked-the-experts-weigh-in
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-09-04T18:59:19Z'
published: '2026-09-04T00:00:00Z'
description: After hackers failed to extort Manchester Airports Group and posted the
  data of nearly 9 million people online, we asked the experts what's really going
  on.
image: https://cdn.mos.cms.futurecdn.net/RYNpvpkwHbue2Dnhv3oLpL-1920-80.jpg
---

![Airport](https://cdn.mos.cms.futurecdn.net/RYNpvpkwHbue2Dnhv3oLpL.jpg) 

Following the aftermath of the Manchester Airports Group cyberattack - where hackers made off with the data of 8.7 million people - the hackers have now posted the entire database for sale on the dark web.

The group behind the attack, FulcrumSec, attempted to get Manchester Airports Group (MAG) to pay for the security of the database, promising that it wouldn’t be released if the company paid a settlement. But as all companies should do when faced with extortion, MAG didn’t play ball.

Now FulcrumSec wants to try and maximise the damage of the cyberattack, and has listed the database containing email addresses, phone numbers, vehicle registrations and postcodes online in the hopes a fellow hacking group will find value in the data.

## What happens when extortion fails, and why didn’t MAG pay?

In the past, when companies faced ransomware attacks or data breaches, they would sometimes quietly pay the hackers for their silence.

Companies feared serious reputational harm and loss of business would cost more in the long run than the perpetrators were asking for. But this created an incentive for hackers to carry out more attacks.

After all, if companies aren’t kicking up a fuss about being hacked or reporting the attack to the authorities, hacking groups can launch more attacks on other companies that are completely unaware of their tactics.

 ![TechRadar Pro Perspectives logo in purple](https://cdn.mos.cms.futurecdn.net/iGCEJhusMZf623FQovppd9.png) 


Got an opinion for us? Here’s how you can submit your perspective

In order to counter this, authorities and cyber experts from around the world issued guidance that under no circumstances should companies pay for the safe return of their data. By removing the incentive from ransomware attacks and data breaches, the hope is that hackers will get bored or not see enough ROI, and therefore stop.

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

But the 500GB database of data on over 8.7 million people is ripe pickings for other cybercriminals looking to launch highly specific phishing attacks or scam campaigns. While FulcrumSec may not make any money from the attack, they can seriously enhance the damage of the attack by offering the data for free for others to use.

A successful scam or phishing attack can steal banking and financial details, allowing other groups to steal even more money off the back of the attack.

### Expert perspectives on MAG extortion and customer data

- **Dray Agha, senior manager of security operations at Huntress:**

*While Manchester Airports Group followed official guidance by refusing to pay the ransom, the release of 8.7 million records creates an immediate risk for passengers.*

The release of 8.7 million records creates an immediate risk for passengers


*We expect other criminals to use this freely available database of vehicle registrations, postcodes and contact details to craft highly convincing phishing attacks.*

*Anyone who has used parking, lounges or Wi-Fi at these airports must treat unexpected messages about their travel with extreme caution.*

- **Muhammad Yahya Patel, vCISO and cybersecurity advisor for EMEA at Huntress**

*The "free release" model is deliberately designed to maximise harm and reputational damage as a warning to the next target.* 

It's a marketing campaign aimed at every other organisation watching


*Publishing almost nine million records for free isn't just punishment for MAG it's a marketing campaign aimed at every other organisation watching.*

*Pay up, or your customers' data gets handed to every fraudster and scammer on the internet at no cost. Refusing to pay a ransom is the right call. But nearly nine million people are now paying a different price for a decision that was never theirs to make.*

- **Danny Jenkins, Co Founder & CEO at ThreatLocker**

*Unfortunately, once data is made public, it can’t be hidden again. The most important thing consumers can do is focus on basic cyber hygiene. Use a unique password for every website, learn how to identify phishing scams, and monitor your credit report.*

Be highly suspicious of emails that create a sense of urgency, offer something that seems too good to be true, or ask you to reset your password.


*When in doubt, look up the phone number for the alleged sender yourself, rather than using a number provided in the email, and call to confirm whether the communication is genuine.*

- **Brian Higgins, security specialist at Comparitech:**

*Whilst the airports breached in this attack don't appear to have had any financial data compromised the risk to affected or associated customers is very real. With so much other information freely available in the wild it is vital that airport users stay highly vigilant for some time to come.*

Research advice from trusted sources like the NCA or Information Commissioner and share it with your family and friends.


*Any and all unsolicited contact; whether online, by telephone or even home visit approaches, should be viewed as suspicious. Never engage until you've taken time to check credentials/veracity etc.*

*Research advice from trusted sources like the NCA or Information Commissioner and share it with your family and friends. Look for ways to increase digital and physical security like two factor authentication on Apps and devices or Smart Home tech.* 

*When this breach was first reported by the Manchester Evening News the comments were quite telling. Affected parties were quick to identify potential vulnerabilities over and above the breach of financial and banking details.* 

*Home addresses, vehicle registrations and time spent away from home all add up to some excellent opportunities for criminal exploitation, not to mention the usual follow-up phishing campaigns common in this type of incident.*

*As AI makes data aggregation swift and easy consumers are waking up to the fact that criminals can monetise successful breaches in increasingly inventive ways. It’s no longer enough for data owning organisations to advise post-attack vigilance and turn to their backups.*

*Victim communities rightly expect better protected networks and systems over and above established norms. As the marketplace grows less fearful and more angry when breaches are made public we may see more emphasis on cyber crime prevention which can only be a good thing.*

- **Denis Calderone, CTO at Suzu Labs:**

*The 8.7 million number is attention-grabbing, but it deserves some context. MAG has confirmed that the vast majority of those records are email addresses collected through airport WiFi sign-ups.* 

*A much smaller subset includes phone numbers, vehicle registrations, and postcodes from customers who actually completed parking or lounge bookings.*

What remains unclear is whether the data was exfiltrated directly from that third-party environment or whether it was pulled back through MAG's network first.


*No payment data, no passwords, no passport information. So despite this affecting airports, which is obviously a sensitive subject, the actual data sensitivity for most affected individuals is relatively low.*

*What's more interesting to us from a technical standpoint is the attack path. MAG told The Register that attackers compromised one of their internal systems and then went on to steal files from a database hosted by a third party. That's a pivot upstream into a data provider, not downstream into operational systems.*

*What remains unclear is whether the data was exfiltrated directly from that third-party environment or whether it was pulled back through MAG's network first. That distinction matters for understanding where detection controls failed and who was responsible for monitoring the egress.*

*The UK's Civil Aviation Authority has a Cyber Assessment Framework for Aviation, developed with the NCSC, that mandates strict separation between IT systems and operational technology.*

*We don't know whether MAG was formally operating under that framework at the time of this incident, but I would be very interested to find out. Because the segmentation appears to have held here. Flight operations, baggage handling, terminal systems, etc., all were unaffected.* 

*The lateral movement went upstream toward a data provider, not downstream toward the systems that keep planes in the air.*

- **Seemant Sehgal, CEO and Founder at BreachLock:**

*This data was initially collected because passengers needed a login, and somewhere along the way, the sensitivity of what was accumulating in that database stopped getting the same scrutiny as the network itself.*

Whoever held it for ransom understood its value better than the organization storing it did


*Vehicle registration details, postcodes, and contact information across three major airports are a profiling dataset, and whoever held it for ransom understood its value better than the organization storing it did.*

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
