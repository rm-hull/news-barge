---
title: Why was there an 'evil’ Delta airlines Wi-Fi network? The experts weigh in
source_url: https://www.techradar.com/pro/security/why-was-there-an-evil-delta-airlines-wi-fi-network-the-experts-weigh-in
source_site: TechRadar UK
source_slug: techradar-uk
scraped_at: '2026-08-15T16:37:14Z'
published: '2026-08-15T00:00:00Z'
description: A passenger set up an evil Wi-Fi network on a post-DEF CON Delta flight
image: https://cdn.mos.cms.futurecdn.net/KZMrozx7RQQq5F2nbhK2iZ-1920-80.jpg
---

![Wi-Fi](https://cdn.mos.cms.futurecdn.net/KZMrozx7RQQq5F2nbhK2iZ.jpg) 

As many attendees of this year’s DEF CON hacker conference departed Las Vegas recently, many unsuspecting passengers on Delta Flight 591 attempted to access an onboard Wi-Fi network.

What they didn’t know was that ‘Delta WiFi Fast’ was actually a fake network, allegedly set up by a fellow passenger intended to mimic the actual onboard Wi-Fi network and scam other users.

The unknown passenger was able to disable the legitimate Wi-Fi networks for 30 minutes while they launched the attack, and in doing so, may have violated United States federal law.

## How did the attack take place?

According to Aircraft Communications Addressing and Reporting System (ACARS) messages, the situation was first brought to light by the crew of the flight, who shared the following message:

“HEY ALERT CORP SECURITY WE HAVE A PAX [passenger] ON THAT HAS CREATED A SCAM WIFI CALLED DELTA WIFI FAST WE BELIEVE THEY ARE TRYING TO SCAM THE OTH PAX”

Another message read:

“NO INFO AS OF NOW WE HAVE A BUNCH OF PAX THAT WERE AT A CYBER CONFRENCE IN LAS THE WERE ABLE TO JAM OUR WIFI AND BRODCAST THERE SIGNIAL”

Sign up to the TechRadar Pro newsletter to get all the top news, opinion, features and guidance your business needs to succeed!

The actual details of what happened on the flight outside of these messages isn’t clear, but according to Monika Hathaway, head of press for DEF CON, similar attacks happened in Las Vegas: “Our conference this year also suffered from multiple similar ‘deauthorization’ Wi-Fi attacks and it impacted some of our operations.”

Delta airlines confirmed that no aircraft operating systems were affected and flight safety was never in question.

Wi-Fi deauthorization attacks can be launched with cheap, widely available ‘deauth boards’ which are small, battery powered devices that send deauthentication frames to devices within their range. On board a plane, these could easily reach most devices.

Once the legitimate Wi-Fi has been jammed and the other users booted from the network, the attacker can then set up an ‘evil twin’ network that users will attempt to connect to, which can be used to snoop on their internet traffic, steal credentials, and perform other malicious activities.

### Expert perspectives on the Delta Wi-Fi attack

## ‘Evil twin’ attacks and the risks of connecting

**Aras Nazarovas, Senior Information Security Researcher at Cybernews:**

*An evil twin attack is when hackers create fake Wi-Fi networks with the goal of stealing sensitive information from people, or exploiting known vulnerabilities present on victim devices. The fake networks often have a very similar (or identical) name to the legitimate network, which was the case here.*

*Once a person connects to the hacker’s Wi-Fi network, the hacker may be able to see what the victim is doing online and what data they transfer. However, since most websites have HTTPS/TLS encryption, much of what the user does, even on the rogue network, is private.*

*The risk here is that the hacker may attempt to redirect the victim to a phishing website – for instance, in this case, it may have been a fake Delta login page asking for personal data like name, email, address, etc. Or, the hacker may even go further and provide fake login pages for banks, social media, and try to extract login details from the victims.*

Connecting to a network controlled by a threat actor allows them to probe your device for potential vulnerabilities and maliciously redirect your internet traffic to their own servers.


*Connecting to such a network comes with some risk in itself. Connecting to a network controlled by a threat actor allows them to probe your device for potential vulnerabilities and maliciously redirect your internet traffic to their own servers.* 

*If a person entered credentials into a Wi-Fi login page, noticed security warnings popping up after visiting a website, downloaded something, or entered payment information into an unfamiliar page, then they may have had their data stolen. In that case, the victim should immediately change any passwords that were transmitted, do a thorough scan of their device for malware, and if bank details were transmitted, freeze the bank account until new credentials are received.*

*However, if a user just connected and disconnected to the Wi-Fi without entering any details or clicking suspicious links, they should be fine.*

## Who would launch the attack?

**Seemant Sehgal, Founder & CEO, BreachLock:**

*Flying out of Vegas after Black Hat myself just a few days before this incident, I can tell you the security conference crowd that passes through that airport is unlike any other, and the crew on Flight 591 made the right call with the information they had in front of them.*

The people most likely to pull something like this on a DEF CON departure flight are the ones who know exactly where that line is, which makes crossing it a choice rather than a mistake. Disabling the Wi-Fi and investigating was exactly the right instinct.


*Rogue access points impersonating a legitimate network are one of the oldest tricks in the book, and doing it on an aircraft to scam passengers is a federal crime regardless of the sophistication involved.*

*The people most likely to pull something like this on a DEF CON departure flight are the ones who know exactly where that line is, which makes crossing it a choice rather than a mistake. Disabling the Wi-Fi and investigating was exactly the right instinct.*

**Denis Calderone, CTO, Suzu Labs:**

*Hackers will hack. I go to DEF CON most years, and it's pretty common to have a terrible wifi experience on those flights because everyone is playing with their WiFi Pineapples and whatnot. That said, my flight home this year had no rogue SSIDs that I could see, and although, as usual, the wifi was shoddy, I never took the time to analyze the radio signals in the cabin, but if a few deauths were flying around, I wouldn't have been too surprised. It is concerning to hear about attempted credential harvesting on the flight though, and I feel that that's taking the expected hijinks way too far.*

These sorts of wifi threats are very common. DEF CON still displays their famed Wall of Sheep which displays the sniffing clear text credentials on the conference network, and every year the WiFi Pineapples have been selling out at the Hak5 booth.


*The deauthentication and evil twin combination used on Flight 591 is a well-documented attack that the security community has been demonstrating for a good two decades. These sorts of wifi threats are very common. DEF CON still displays their famed Wall of Sheep which displays the sniffing clear text credentials on the conference network, and every year the WiFi Pineapples have been selling out at the Hak5 booth.*

*But there's a significant difference between demonstrating a technique at a conference and deploying it against 199 unsuspecting passengers on a commercial aircraft. Last November, an Australian man was sentenced to seven years and four months in prison for running the exact same attack on domestic flights using a WiFi Pineapple and now the FBI is already involved in this case. There is definitely a legal exposure here.*

*For anyone who travels for work, in-flight WiFi should be treated as an untrusted network, period. The enterprise advice is encrypted DNS through your MDM and always-on VPN with captive portal remediation configured. But honestly, a VPN is something every traveler should be using, not just corporate road warriors. I make sure mine is on whenever I travel, and my family does the same.*

*Beyond that, if a WiFi network on a plane doesn't match what the crew announced or what's printed on the seat card, don't connect to it. If a network asks you to log in with your Google account or email credentials to get WiFi access, that's not how airline WiFi works. Airline captive portals ask for a credit card or a loyalty account, not your personal email password. If you're being asked for something that doesn't make sense for the context, you're probably not on the real network.*

## Reputational harm for the cybersecurity industry

**Jacob Warner, Director of IT, Xcape, Inc.:**

*While a rogue Wi-Fi access point on a commercial airliner poses zero direct risk to air-gapped flight safety controls, it creates a serious enterprise security hazard for business travelers relying on inflight networks.*

*Dismissing an onboard network impersonation as a harmless prank ignores the reality of man-in-the-middle attacks, credential harvesting, and fake authentication portals targeting captive passengers connecting to the Internet.*

Given that the flight departed Las Vegas immediately following DEF CON, it requires little imagination to conclude an attendee deployed the unauthorized access point.


*This juvenile behavior is precisely why hackers suffer such a poor reputation among non-technical audiences and why security professionals struggle to build mainstream trust. Enterprise security teams must mandate always-on virtual private networks or zero-trust network access, disable automatic connections to open SSIDs on corporate endpoints, and instruct travelers to treat cabin wireless environments as untrusted networks.*

*Setting up an evil twin at 30,000 feet does not make you a clever researcher; it just proves why we cannot have nice things.*

**John Strand, Owner, Black Hills Information Security, Inc.:**

*This one hits differently because this is my community. These are my people. When security professionals engage in this kind of behavior, they’re betraying the very community they’re claim to represent.*

There’s nothing impressive about it. It doesn’t make you look clever, and it certainly doesn’t make you an elite hacker. In most cases, these attacks aren’t even technically sophisticated.


*There’s nothing impressive about it. It doesn’t make you look clever, and it certainly doesn’t make you an elite hacker. In most cases, these attacks aren’t even technically sophisticated. They’re simply people with enough technical knowledge taking advantage of others who don’t have the experience to recognize what’s happening. That isn’t skill. It’s bullying.*

*I hope the people responsible are held accountable. This isn’t funny, it isn’t clever, and it doesn’t demonstrate technical excellence. It’s just people abusing their knowledge to prey on those who are at a disadvantage. That’s not what this profession should stand for.*

 ![Google logo on a black background next to text reading 'Click to follow TechRadar'](https://cdn.mos.cms.futurecdn.net/diM9tpwF2Lz85R8q85CT78.jpg) 


***Follow TechRadar on Google News***and** add us as a preferred source***to get our expert news, reviews, and opinion in your feeds.*

![Benedict Collins](https://cdn.mos.cms.futurecdn.net/jEvqGv8wvH7PWZ4XPURyyB.jpg)

Benedict is a Senior Security Writer at TechRadar Pro, where he has specialized in covering the intersection of geopolitics, cyber-warfare, and business security.

Benedict provides detailed analysis on state-sponsored threat actors, APT groups, and the protection of critical national infrastructure, with his reporting bridging the gap between technical threat intelligence and B2B security strategy.

Benedict holds an MA (Distinction) in Security, Intelligence, and Diplomacy from the University of Buckingham Centre for Security and Intelligence Studies (BUCSIS), with his specialization providing him with a robust academic framework for deconstructing complex international conflicts and intelligence operations, and the ability to translate intricate security data into actionable insights.

You must confirm your public display name before commenting

Please logout and then login again, you will then be prompted to enter your display name.
